#include <Python.h>
#include <stdlib.h>
#include <string.h>
#include "lz4hc.h"
#include "lz4.h"

#define MAGIC_HEADER 0xDEADBEEF
#define MAX_CHUNK_SIZE (4 * 1024 * 1024)   // 4MB max
#define MIN_CHUNK_SIZE (64 * 1024)         // 64KB min
#define DEFAULT_CHUNK_SIZE (512 * 1024)    // Default starting size

// Auto-tune chunk size depending on input length
static size_t auto_tune_chunk_size(size_t input_size) {
    if (input_size < MIN_CHUNK_SIZE) return MIN_CHUNK_SIZE;
    if (input_size > MAX_CHUNK_SIZE * 128) return MAX_CHUNK_SIZE;
    return DEFAULT_CHUNK_SIZE;
}

// -------------------- COMPRESS --------------------
static PyObject* compress(PyObject* self, PyObject* args) {
    const char* input;
    Py_ssize_t input_size;

    if (!PyArg_ParseTuple(args, "y#", &input, &input_size))
        return NULL;

    // Handle empty input
    if (input_size == 0) {
        int magic = MAGIC_HEADER;
        return PyBytes_FromStringAndSize((const char*)&magic, sizeof(int));
    }

    size_t chunk_size = auto_tune_chunk_size(input_size);
    size_t chunk_count = (input_size + chunk_size - 1) / chunk_size;

    size_t header_size = sizeof(int) + sizeof(int) + chunk_count * 2 * sizeof(int);
    size_t max_compressed_size = header_size + (chunk_count * LZ4_compressBound((int)chunk_size));

    char* output = (char*)malloc(max_compressed_size);
    if (!output) return PyErr_NoMemory();

    int* header = (int*)output;
    header[0] = MAGIC_HEADER;
    header[1] = (int)chunk_count;

    size_t in_offset = 0;
    size_t out_offset = header_size;

    for (size_t i = 0; i < chunk_count; ++i) {
        size_t remaining = input_size - in_offset;
        size_t current_chunk_size = remaining < chunk_size ? remaining : chunk_size;

        int max_out = LZ4_compressBound((int)current_chunk_size);
        char* dest = output + out_offset;

        int compressed_size = LZ4_compress_HC(
            input + in_offset,
            dest,
            (int)current_chunk_size,
            max_out,
            9
        );

        if (compressed_size <= 0) {
            free(output);
            return PyErr_Format(PyExc_RuntimeError, "Compression failed on chunk %zu", i);
        }

        header[2 + i * 2] = compressed_size;
        header[2 + i * 2 + 1] = (int)current_chunk_size;

        in_offset += current_chunk_size;
        out_offset += compressed_size;
    }

    PyObject* result = PyBytes_FromStringAndSize(output, out_offset);
    free(output);
    return result;
}

// -------------------- DECOMPRESS --------------------
static PyObject* decompress(PyObject* self, PyObject* args) {
    const char* input;
    Py_ssize_t input_size;

    if (!PyArg_ParseTuple(args, "y#", &input, &input_size))
        return NULL;

    if (input_size < sizeof(int)) {
        return PyErr_Format(PyExc_ValueError, "Invalid input (too small)");
    }

    const int* header = (const int*)input;

    if (header[0] != MAGIC_HEADER) {
        return PyErr_Format(PyExc_ValueError, "Invalid header magic");
    }

    // ✅ Handle empty input case (just the magic header)
    if (input_size == sizeof(int) && header[0] == MAGIC_HEADER) {
        return PyBytes_FromStringAndSize("", 0);
    }

    int chunk_count = header[1];
    if (chunk_count <= 0 || chunk_count > 1000000) {
        return PyErr_Format(PyExc_ValueError, "Unreasonable chunk count: %d", chunk_count);
    }

    size_t header_size = sizeof(int) + sizeof(int) + chunk_count * 2 * sizeof(int);
    size_t total_size = 0;

    for (int i = 0; i < chunk_count; ++i) {
        total_size += header[2 + i * 2 + 1];
    }

    char* output = (char*)malloc(total_size);
    if (!output) return PyErr_NoMemory();

    size_t out_offset = 0;
    size_t in_offset = header_size;

    for (int i = 0; i < chunk_count; ++i) {
        int comp_size = header[2 + i * 2];
        int orig_size = header[2 + i * 2 + 1];

        if (in_offset + comp_size > (size_t)input_size) {
            free(output);
            return PyErr_Format(PyExc_ValueError, "Compressed chunk out of bounds");
        }

        int actual = LZ4_decompress_safe(
            input + in_offset,
            output + out_offset,
            comp_size,
            orig_size
        );

        if (actual < 0) {
            free(output);
            return PyErr_Format(PyExc_RuntimeError, "Decompression failed on chunk %d", i);
        }

        out_offset += orig_size;
        in_offset += comp_size;
    }

    PyObject* result = PyBytes_FromStringAndSize(output, out_offset);
    free(output);
    return result;
}

// -------------------- PYTHON MODULE --------------------
static PyMethodDef methods[] = {
    {"compress", compress, METH_VARARGS, "Compress data using LZ4HC"},
    {"decompress", decompress, METH_VARARGS, "Decompress data using LZ4"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "fastcompress",
    "High-speed hybrid compression with auto-chunk tuning",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_fastcompress(void) {
    return PyModule_Create(&moduledef);
}


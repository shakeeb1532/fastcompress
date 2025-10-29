import time
import zlib
import lzma
import fastcompress
import sys

def benchmark_codec(name, compress_fn, decompress_fn, data):
    print(f"\n🚀 Benchmarking: {name}")

    try:
        start = time.time()
        compressed = compress_fn(data)
        comp_time = time.time() - start
    except Exception as e:
        print(f"❌ Compression error: {e}")
        return

    try:
        start = time.time()
        if name == ".warp (fastcompress)":
            decompressed = decompress_fn(compressed, len(data))
        else:
            decompressed = decompress_fn(compressed)
        decomp_time = time.time() - start
    except Exception as e:
        print(f"❌ Decompression error: {e}")
        return

    if decompressed == data:
        print("✅ Data matches original")
    else:
        print("❌ Data mismatch!")

    ratio = (len(compressed) / len(data)) * 100
    print(f"📦 Compression ratio: {ratio:.2f}%")
    print(f"⏱️ Compression time: {comp_time:.3f}s")
    print(f"⏱️ Decompression time: {decomp_time:.3f}s")

def run_benchmark(data):
    benchmark_codec("zlib", zlib.compress, zlib.decompress, data)
    benchmark_codec("lzma", lzma.compress, lzma.decompress, data)
    benchmark_codec(".warp (fastcompress)", fastcompress.compress, fastcompress.decompress, data)

def benchmark_file(path):
    print("========================================")
    print(f"📂 Benchmarking file: {path}")
    print("========================================")

    with open(path, "rb") as f:
        data = f.read()

    print(f"\n📂 Reading file: {path}")
    run_benchmark(data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python benchmark_diagnostic.py <file>")
        sys.exit(1)
    benchmark_file(sys.argv[1])


<<<<<<< HEAD
# fastcompress
Ultra-fast compression library using LZ4HC with chunking and auto-tuning, optimized for large files.
=======
# WarpCompress

**WarpCompress** is a blazing-fast, low-overhead compression library for Python, powered by an optimized LZ4HC backend written in C with custom chunking and adaptive tuning.

Designed for:

* High-speed compression and decompression
* Extremely low memory usage
* Support for massive files (tested up to 5 GB)
* Efficient handling of small files and edge cases

---

## 🚀 Features

* Chunked compression (auto-tuned for file size)
* High-speed decompression (faster than `zlib`, `lzma`)
* Robust C backend (LZ4HC + custom header logic)
* Handles empty input, corrupted headers gracefully
* Cross-platform (macOS / Linux / Windows)

---

## 📦 Installation

```bash
# Clone and install locally
$ git clone https://github.com/yourusername/warpcompress.git
$ cd warpcompress
$ python setup.py build_ext --inplace
```

Ensure you have a working C compiler (e.g., clang, gcc).

---

## 🧪 Usage

```python
import fastcompress

data = b"hello world" * 100_000
compressed = fastcompress.compress(data)
decompressed = fastcompress.decompress(compressed)

assert data == decompressed
```

---

## 📊 Benchmarks

### Input: 500MB Executable File

| Codec    | Ratio      | Compress  | Decompress |
| -------- | ---------- | --------- | ---------- |
| zlib     | 31.25%     | 6.71s     | 0.64s      |
| lzma     | 18.44%     | 42.72s    | 2.80s      |
| **warp** | **35.01%** | **4.77s** | **0.10s**  |

### Input: 500MB Random File

| Codec    | Ratio       | Compress   | Decompress |
| -------- | ----------- | ---------- | ---------- |
| zlib     | 100.03%     | 9.39s      | 0.15s      |
| lzma     | 100.00%     | 171.06s    | 0.64s      |
| **warp** | **100.39%** | **10.98s** | **0.12s**  |

### Input: 500MB Text File

| Codec    | Ratio     | Compress  | Decompress |
| -------- | --------- | --------- | ---------- |
| zlib     | 0.24%     | 1.92s     | 0.22s      |
| lzma     | 0.01%     | 4.42s     | 0.84s      |
| **warp** | **0.39%** | **0.02s** | **0.17s**  |

> ✅ Tested on: Apple Silicon (macOS), Python 3.13

---

## 📁 Project Structure

```
warpcompress/
├── fastcompress/         # C-extension module
│   ├── warp_compress.c   # Core compressor
│   └── lz4.c / lz4hc.c   # LZ4 backend
├── test_all_files.py     # Unified test suite
├── benchmark_diagnostic.py
├── setup.py
├── README.md
└── test_data/
```

---

## 🛠 Development

To rebuild the extension manually:

```bash
python setup.py build_ext --inplace
```

To run full tests:

```bash
python test_all_files.py
```

---

## 📜 License

MIT License. See `LICENSE` file.

---

## 🙌 Acknowledgments

* Based on [LZ4](https://github.com/lz4/lz4) by Yann Collet
* Inspired by real-world performance bottlenecks in archive and data science workloads

---

## 🌍 Contribute

Pull requests welcome! For major changes, please open an issue first to discuss what you’d like to change.

>>>>>>> daa97cf (Initial commit of fastcompress)

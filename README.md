# ⚡ fastcompress

### Ultra‑fast, memory‑safe, high‑efficiency compression engine written in C with Python bindings.

`fastcompress` combines **LZ4** and **optimized C routines** to deliver blazing‑fast compression and decompression for text, binary, and mixed workloads — achieving sub‑second performance even on gigabyte‑scale data.

---

## 🧑‍💻 Author
**Salman Shakeeb**  
📧 shakeeb1532@gmail.com  
GitHub: [@shakeeb1532](https://github.com/shakeeb1532)

---

## 🚀 Features

- 🔥 High‑speed compression / decompression  
- 🧠 Auto‑tuned chunk size for optimal performance  
- 🧩 Safe memory handling (malloc/free checks)  
- 📦 Works on all major OS (Linux / macOS / Windows)  
- 🐍 Simple Python API  
- 🧪 Battle‑tested with 0 → 5 GB datasets  

---

## 🛠️ Installation

### From source
```bash
git clone https://github.com/shakeeb1532/fastcompress.git
cd fastcompress
python setup.py build_ext --inplace
🐍 Usage Example
python
Copy code
import fastcompress

data = b"hello world" * 100000
compressed = fastcompress.compress(data)
decompressed = fastcompress.decompress(compressed)

assert decompressed == data
print("✅ Compression round‑trip successful!")
📊 Benchmark Results
Benchmarks were run on an Apple M1 system (Python 3.13, macOS 11, Oct 2025).

🧩 Synthetic 500 MB “Mixed” Dataset
Codec	✅ Verified	Compression Ratio	⏱️ Compression Time	⏱️ Decompression Time
zlib	✅	 50.16 %	 5.85 s	 0.26 s
lzma	✅	 50.01 %	 89.91 s	 0.78 s
brotli	✅	 50.00 %	 186.99 s	 0.34 s
.warp (fastcompress)	✅	 50.39 %	 6.08 s	 0.16 s

🧪 Small‑File Tests
Test	Original Size	Compressed Size	Ratio	✅ Status
 1 	 0 B 	 4 B 	 0.00 % 	 ✅ OK 
 2 	 1 B 	 18 B 	 1800.00 % 	 ✅ OK 
 3 	 13 B 	 30 B 	 230.77 % 	 ✅ OK 
 4 	 64 B 	 27 B 	 42.19 % 	 ✅ OK 
 5 	 1 KB 	 30 B 	 2.93 % 	 ✅ OK 
 6 	 512 KB 	 2.03 KB 	 0.40 % 	 ✅ OK 
 7 	 512 KB 	 2.04 KB 	 0.40 % 	 ✅ OK 
 8 	 1 MB 	 4.08 KB 	 0.40 % 	 ✅ OK 

🏋️ Large‑File Tests
File Size	Compressed Size	Ratio	⏱️ Compression	⏱️ Decompression	✅ Status
 512 MB 	 2.03 MB 	 0.40 % 	 0.05 s 	 0.26 s 	 ✅ OK 
 1 GB 	 4.02 MB 	 0.39 % 	 0.09 s 	 0.49 s 	 ✅ OK 
 5 GB 	 20.10 MB 	 0.39 % 	 0.49 s 	 5.10 s 	 ✅ OK 

🧱 Real‑World Data (500 MB Tests)
Dataset Type	Codec	✅ Verified	Compression Ratio	⏱️ Compression Time	⏱️ Decompression Time
 Executable Data	zlib	✅	 31.25 %	 6.66 s	 0.62 s
 	lzma	✅	 18.44 %	 43.86 s	 2.61 s
 	fastcompress	✅	 35.01 %	 4.77 s	 0.09 s
 Random Data	zlib	✅	 100.03 %	 9.39 s	 0.15 s
 	lzma	✅	 100.00 %	 171.06 s	 0.65 s
 	fastcompress	✅	 100.39 %	 10.98 s	 0.12 s
 Text Data	zlib	✅	 0.24 %	 1.93 s	 0.22 s
 	lzma	✅	 0.01 %	 4.42 s	 0.85 s
 	fastcompress	✅	 0.39 %	 0.02 s	 0.17 s

⚙️ CLI Example
bash
Copy code
python -c "
import fastcompress
data = open('input.bin','rb').read()
open('output.fc','wb').write(fastcompress.compress(data))
"
To decompress:

bash
Copy code
python -c "
import fastcompress
data = open('output.fc','rb').read()
open('restored.bin','wb').write(fastcompress.decompress(data))
"
🧰 Project Structure
python
Copy code
fastcompress/
├── warp_compress.c
├── lz4.c / lz4hc.c / lz4.h / lz4hc.h
├── setup.py / pyproject.toml
├── test_all_files.py / test_small_files.py / test_large_files.py
├── benchmark.py / benchmark_diagnostic.py
├── run_diagnostics_all.sh / run_real_world_benchmarks.sh
├── generate_mixed_file.py
├── test_data/
│   ├── test_exec_500mb.bin
│   ├── test_random_500mb.bin
│   └── test_text_500mb.bin
└── README.md
🧪 Run Tests
bash
Copy code
python test_all_files.py
# or
./run_diagnostics_all.sh
🧩 Build for PyPI (Optional)
bash
Copy code
pip install build twine
python -m build
twine upload dist/*
📜 License (MIT)
sql
Copy code
MIT License

Copyright (c) 2025 Salman Shakeeb

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
💬 Summary
✅ fastcompress demonstrates production‑grade performance:

Compression ratio ~35 % for binaries

Sub‑second compression up to 1 GB

Excellent stability (verified on 0 → 5 GB data)

Ideal for developers seeking maximum speed with solid compression efficiency.

Created by Salman Shakeeb — 2025

yaml
Copy code

---

Would you like me to include a short “PyPI‑style badge section” (e.g. build | license | Python version) at the top? It helps make the repo look even more professional on GitHub and PyPI.

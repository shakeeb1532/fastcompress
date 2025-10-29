import time, os, sys
import lz4.frame
import snappy
import zstandard as zstd
import fastcompress

def read_file(path):
    with open(path, "rb") as f:
        return f.read()

def time_fn(label, compress_fn, decompress_fn, data):
    start = time.time()
    compressed = compress_fn(data)
    t1 = time.time()
    decompressed = decompress_fn(compressed)
    t2 = time.time()

    match = decompressed == data
    ratio = len(compressed) / len(data)

    print(f"\n🔹 {label}")
    print(f"  ⏱️ Compress time   : {t1 - start:.4f}s")
    print(f"  ⏱️ Decompress time : {t2 - t1:.4f}s")
    print(f"  📦 Ratio           : {ratio:.2%}")
    print(f"  ✅ Lossless        : {'YES' if match else 'NO'}")

def run_benchmark(data):
    time_fn(".warp (hybrid)",
            fastcompress.compress_bytes,
            fastcompress.decompress_bytes,
            data)

    time_fn("lz4.frame",
            lz4.frame.compress,
            lz4.frame.decompress,
            data)

    cctx = zstd.ZstdCompressor(level=3)
    dctx = zstd.ZstdDecompressor()
    time_fn("zstd (level 3)",
            cctx.compress,
            dctx.decompress,
            data)

    time_fn("snappy",
            snappy.compress,
            snappy.decompress,
            data)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print(f"📂 Reading file: {path}")
        data = read_file(path)
    else:
        print("⚠️  No file specified — using generated test data.")
        data = b"The quick brown fox jumps over the lazy dog.\n" * 100000

    run_benchmark(data)


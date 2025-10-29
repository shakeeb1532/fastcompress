import fastcompress
import os
import time

def format_size(bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} TB"

def generate_test_data(size_bytes):
    # Generate highly compressible repeated pattern
    pattern = b"The quick brown fox jumps over the lazy dog.\n"
    return (pattern * (size_bytes // len(pattern) + 1))[:size_bytes]

def test_large_file(size_bytes):
    print(f"\n🔍 Testing large file: {format_size(size_bytes)}")

    data = generate_test_data(size_bytes)

    # Compress
    t0 = time.time()
    compressed = fastcompress.compress(data)
    t1 = time.time()

    # Decompress
    t2 = time.time()
    decompressed = fastcompress.decompress(compressed, len(data))
    t3 = time.time()

    ratio = 100 * len(compressed) / len(data)
    print(f"✅ Data match: {decompressed == data}")
    print(f"📦 Compression ratio: {ratio:.2f}%")
    print(f"⏱️ Compression time: {t1 - t0:.2f}s")
    print(f"⏱️ Decompression time: {t3 - t2:.2f}s")
    print(f"📐 Original: {format_size(len(data))} → Compressed: {format_size(len(compressed))}")

# List of large sizes to test (in bytes)
test_sizes = [
    512 * 1024 * 1024,     # 512 MB
    1024 * 1024 * 1024,    # 1 GB
    5 * 1024 * 1024 * 1024 # 5 GB
]

for size in test_sizes:
    test_large_file(size)


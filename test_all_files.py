import fastcompress
import time
import os

def human_readable_size(num):
    for unit in ['bytes','KB','MB','GB','TB']:
        if num < 1024.0:
            return f"{num:.2f} {unit}"
        num /= 1024.0
    return f"{num:.2f} PB"

def run_test(data, label):
    try:
        start = time.time()
        compressed = fastcompress.compress(data)
        compress_time = time.time() - start

        start = time.time()
        decompressed = fastcompress.decompress(compressed)
        decompress_time = time.time() - start

        assert decompressed == data

        ratio = (len(compressed) / len(data)) * 100 if data else 0
        print(f"{label:<10} | ✅ OK | Orig={human_readable_size(len(data)):<10} → Compressed={human_readable_size(len(compressed)):<10} | Ratio={ratio:6.2f}% | ⏱️ C: {compress_time:.2f}s | D: {decompress_time:.2f}s")
    except Exception as e:
        print(f"{label:<10} | ❌ FAIL | Exception: {str(e)}")

def test_small_files():
    print("\n🔍 Testing small files")
    test_cases = [
        b'',                              # Empty
        b'A',                             # 1 byte
        b'Hello, world!',                 # 13 bytes
        b'A' * 64,                        # 64 bytes
        b'A' * 1024,                      # 1 KB
        b'A' * (512 * 1024),              # 512 KB
        b'A' * (512 * 1024 + 1),          # Just over 512 KB
        b'A' * (1024 * 1024 + 100),       # ~1 MB
    ]
    for i, data in enumerate(test_cases):
        label = f"Small {i+1}"
        run_test(data, label)

def test_large_files():
    print("\n🔍 Testing large files")
    sizes = [512 * 1024 * 1024, 1024 * 1024 * 1024, 5 * 1024 * 1024 * 1024]  # 512MB, 1GB, 5GB

    for size in sizes:
        label = f"{size // (1024*1024):>4}MB"
        try:
            data = b'A' * size
            run_test(data, label)
        except MemoryError:
            print(f"{label:<10} | ❌ FAIL | MemoryError - skipping")
        except OverflowError:
            print(f"{label:<10} | ❌ FAIL | OverflowError - possible integer limitation")
        except Exception as e:
            print(f"{label:<10} | ❌ FAIL | Exception: {str(e)}")

if __name__ == "__main__":
    test_small_files()
    test_large_files()


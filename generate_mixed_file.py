import os
import random

def generate_mixed_file(filename, total_mb=500):
    half_size = total_mb * 1024 * 1024 // 2

    print(f"📄 Generating {total_mb}MB file with 50% compressible, 50% random data...")

    with open(filename, "wb") as f:
        # Compressible data: repeating pattern
        pattern = b"The quick brown fox jumps over the lazy dog.\n"
        while f.tell() < half_size:
            f.write(pattern * 100)

        # Incompressible data: random bytes
        while f.tell() < total_mb * 1024 * 1024:
            f.write(os.urandom(1024))

    print(f"✅ File generated: {filename} ({total_mb}MB)")

if __name__ == "__main__":
    generate_mixed_file("mixed_500mb.bin")


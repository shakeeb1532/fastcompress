import fastcompress

def test_small_file_handling():
    test_cases = [
        b"",                          # Empty input
        b"A",                         # 1 byte
        b"Hello, world!",             # short text
        b"A" * 64,                    # 64 bytes
        b"A" * 1024,                  # 1KB
        b"A" * (512 * 1024),          # Exactly 1 chunk
        b"A" * (512 * 1024 + 1),      # Slightly over 1 chunk
        b"A" * (2 * 512 * 1024 + 100) # 2 chunks + a bit
    ]

    print("🔍 Testing small file handling...\n")
    
    for i, data in enumerate(test_cases):
        try:
            compressed = fastcompress.compress(data)
            decompressed = fastcompress.decompress(compressed, len(data))
            match = data == decompressed
            ratio = len(compressed) / len(data) * 100 if len(data) > 0 else 0
            print(f"Test {i+1:>2}: Size={len(data):>10} bytes → "
                  f"Compressed={len(compressed):>10} bytes → "
                  f"Ratio={ratio:5.2f}% → {'✅ OK' if match else '❌ Mismatch'}")
        except Exception as e:
            print(f"Test {i+1:>2}: ❌ Exception occurred: {e}")

test_small_file_handling()


from setuptools import setup, Extension

module = Extension(
    "fastcompress",
    sources=["warp_compress.c", "lz4.c", "lz4hc.c"],
    include_dirs=["."],
    extra_compile_args=["-O3", "-std=c99"],
)

setup(
    name="fastcompress",
    version="1.0.0",
    description="Ultra-fast compression library using LZ4 with auto-tuned chunking",
    author="Salman Shakeeb",
    author_email="shakeeb1532@gmail.com",
    ext_modules=[module],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)


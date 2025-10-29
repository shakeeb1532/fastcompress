#!/bin/bash

echo "📊 Running benchmark_diagnostic.py on all test_data/*.bin files"

for file in test_data/*.bin; do
    echo "======================================="
    echo "📂 Benchmarking file: $file"
    echo "======================================="
    python benchmark_diagnostic.py "$file"
    echo ""
done


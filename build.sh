#!/bin/bash

# Create output directory
mkdir -p output

# Build PDF
pandoc metadata.yaml \
    chapters/*.md \
    --listings \
    --number-sections \
    --toc \
    --toc-depth=2 \
    --pdf-engine=xelatex \
    -o output/book.pdf

echo "Build complete! Check output/book.pdf"

# Optional: Build HTML version
pandoc metadata.yaml \
    chapters/*.md \
    --toc \
    --standalone \
    --mathjax \
    -o output/book.html

echo "HTML version: output/book.html"
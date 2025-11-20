#!/bin/bash
# Build script for Amazon Affiliate Site

echo "======================================"
echo "Amazon Affiliate Site Builder"
echo "======================================"
echo ""

# Step 1: Generate pages from CSV
echo "Step 1: Generating pages from CSV..."
python scripts/generate_pages.py

if [ $? -ne 0 ]; then
    echo "Error: Failed to generate pages"
    exit 1
fi

echo ""

# Step 2: Build with Hugo
echo "Step 2: Building with Hugo..."
hugo --minify

if [ $? -ne 0 ]; then
    echo "Error: Hugo build failed"
    exit 1
fi

echo ""
echo "======================================"
echo "Build completed successfully!"
echo "======================================"
echo ""
echo "Next steps:"
echo "1. To preview locally: hugo server --buildDrafts"
echo "2. To deploy: git add . && git commit -m 'Update products' && git push"
echo ""

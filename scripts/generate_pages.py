#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert CSV product data to Hugo Markdown pages
Usage: python scripts/generate_pages.py
"""

import csv
import os
import sys
from datetime import datetime

# Fix encoding on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configuration
CSV_FILE = 'data/products.csv'
CONTENT_DIR = 'content/products'

def ensure_dir_exists():
    """Create content/products directory if it doesn't exist"""
    os.makedirs(CONTENT_DIR, exist_ok=True)

def read_csv():
    """Read products from CSV file"""
    products = []
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found")
        return []

    return products

def generate_markdown(product):
    """Generate Markdown content from product data"""

    # Parse pros and cons (comma-separated)
    pros_list = [p.strip() for p in product['pros'].split(',')]
    cons_list = [c.strip() for c in product['cons'].split(',')]

    pros_md = '\n'.join([f"- {p}" for p in pros_list])
    cons_md = '\n'.join([f"- {c}" for c in cons_list])

    # Create front matter and content
    content = f"""---
title: "{product['name']}"
date: {datetime.now().isoformat()}
draft: false
category: "{product['category']}"
price: "{product['price']}"
rating: {product['rating']}
reviews: {product['review_count']}
image: "{product['image_url']}"
amazon_url: "{product['amazon_url']}"
affiliate_link: "{product['affiliate_link']}"
---

## Overview

{product['description']}

**Rating:** {product['rating']}/5 ({product['review_count']} reviews)
**Price:** ${product['price']}

## Pros

{pros_md}

## Cons

{cons_md}

## Buy Now

[View on Amazon]({product['affiliate_link']})

---

*This is an affiliate link. If you make a purchase through this link, we may earn a small commission at no extra cost to you.*
"""

    return content

def main():
    """Main function to generate all product pages"""
    ensure_dir_exists()

    products = read_csv()

    if not products:
        print("No products found in CSV file.")
        return

    for product in products:
        # Create filename from product ID
        filename = f"{CONTENT_DIR}/{product['id']}-{product['name'].lower().replace(' ', '-')}.md"

        # Generate markdown content
        markdown_content = generate_markdown(product)

        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"[OK] Generated: {filename}")

    print(f"\n[SUCCESS] Successfully generated {len(products)} product pages!")

if __name__ == '__main__':
    main()

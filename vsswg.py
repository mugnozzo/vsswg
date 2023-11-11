#!/bin/env python

import os
import shutil
import re

def replace_blocks(original_file, blocks_dir):
    with open(original_file, 'r') as file:
        content = file.read()

    # Find all block placeholders and replace them with the corresponding block content
    for block_match in re.finditer(r'\{\{\s*block\s+(\w+)\s*\}\}', content):
        block_name = block_match.group(1)
        block_file_path = os.path.join(blocks_dir, f'{block_name}.html')

        if os.path.exists(block_file_path):
            with open(block_file_path, 'r') as block_file:
                block_content = block_file.read()
            content = content.replace(block_match.group(0), block_content)

    with open(original_file, 'w') as file:
        file.write(content)

def process_directory(source_dir, dest_dir, blocks_dir):
    for root, dirs, files in os.walk(source_dir):
        relative_path = os.path.relpath(root, source_dir)
        new_dir = os.path.join(dest_dir, relative_path)

        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        for file in files:
            original_file = os.path.join(root, file)
            new_file = os.path.join(new_dir, file)
            shutil.copy2(original_file, new_file)
            replace_blocks(new_file, blocks_dir)

def main():
    source_directory = 'pages'
    destination_directory = '..'
    blocks_directory = 'blocks'

    # Process the directory
    process_directory(source_directory, destination_directory, blocks_directory)

if __name__ == "__main__":
    main()


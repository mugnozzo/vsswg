#!/bin/env python

import os
import shutil
import re

page_vars = {}

def replace_with_dict(match):
    key = match.group(1)  # Get the matched group
    print(page_vars)
    return page_vars.get(key, '')  # Return the corresponding value from page_vars

def replace_blocks(original_file, blocks_dir):
    with open(original_file, 'r') as file:
        content = file.read()
    global page_vars
    page_vars = {}

    # Find all variable placeholders and store them in page_vars
    var_regexp = r'\{\{\s*var\s+(\w+)\s*=\s*([-\w]+)\s*\}\}'
    for var_match in re.finditer(var_regexp, content):
        var_name = var_match.group(1)
        var_value = var_match.group(2)
        page_vars[var_name] = var_value
    content = re.sub(var_regexp, "", content)
    print(page_vars)

    # Find all block placeholders and replace them with the corresponding block content
    for block_match in re.finditer(r'\{\{\s*block\s+(\w+)\s*\}\}', content):
        block_name = block_match.group(1)
        block_file_path = os.path.join(blocks_dir, f'{block_name}.html')

        if os.path.exists(block_file_path):
            with open(block_file_path, 'r') as block_file:
                block_content = block_file.read()
                block_content = re.sub(r'\{\{\s*(\w+)\s*\}\}', replace_with_dict, block_content)
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


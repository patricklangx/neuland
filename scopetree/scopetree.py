#!/usr/bin/env python
# coding: utf8

import os
from collections import defaultdict
import codecs
import webbrowser
import argparse
import random
import string

def build_tree(data):
    tree = {}
    for path in data:
        current_level = tree
        for part in path:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
    return tree

def convert_to_js(tree):
    js_object = "const directoryTree = " + str(tree).replace("'", '"') + ";"
    return js_object

def remove_last_char_if_matches(string, char):
    if string and string[-1] == char:
        return string[:-1]
    return string

def main(urls_file, tree_height=None, tree_width=None):
    filter_tags = ['css', 'woff2', 'ico', 'png', 'svg', 'gif', 'jpeg', 'jpg'] # lines with those tags are filtered out

    urls = []
    for url in codecs.open(urls_file, 'r', encoding='utf-8', errors='ignore'):
        url = url.replace('https://', '').replace('http://', '').replace('//', '/').rstrip('\n').split('?')[0]
        
        if not any(word in url for word in filter_tags):
            if url not in urls:
                urls.append(remove_last_char_if_matches(url, '/'))
    
    dict_structure = [i.split('/') for i in list(set(urls))]
    tree_structure = build_tree(dict_structure)
    js_structure = convert_to_js(tree_structure)

    file_template = open('template.html').read()
    new_content = file_template.replace('$$$DATA$$$', js_structure).replace('$$$WIDTH$$$', tree_width).replace('$$$HEIGHT$$$', tree_height)

    rand_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    with open('tree-' + rand_string + '.html', 'w') as f:
        f.write(new_content)

    webbrowser.open(f'file://{os.path.abspath("tree-" + rand_string + ".html")}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', type=str, help='Path to the urls input file')  
    parser.add_argument('-height', type=str, help='Tree structure height')
    parser.add_argument('-width', type=str, help='Tree structure width')
    args = parser.parse_args()
    
    main(args.file, args.height, args.width)
    
"""
This script generates the ToC from a markdown file

Usage: generateToC.py file

positional arguments:
  file -> Input markdown file

"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', help='Input markdown file')
args = parser.parse_args()

with open(args.file) as f:
    for line in f:
        if line.startswith('##'):
            count = len(line.split(' ')[0])
            print("%s1. [%s](#%s)" %
                  ((count - 2) * "   ", line[count + 1:].strip(), line[count + 1:].lower().replace(" ", "-").strip()))

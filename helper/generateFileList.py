"""
This script generates a list of the files in a folder in markdown

Usage: generateFileList.py folder

positional arguments:
  folder -> Input folder

"""

import argparse
from glob import glob

parser = argparse.ArgumentParser()
parser.add_argument('folder', help='Input folder')
parser.add_argument('-s', help='Split the path and only use the file name', action='store_true')
args = parser.parse_args()

for f in glob('%s/*.*' % args.folder):
    f = f.replace('\\', '/')
    if f.endswith(".md"):
        with open(f) as fi:
            line = fi.readline()
        title = line.split('# ')[-1].strip() if len(line) > 0 else f.split('/')[-1]
    else:
        title = f.split('/')[-1]
    print('1. [%s](%s)' % (title, f.split('/')[-1] if args.s is True else f))

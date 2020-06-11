from glob import glob

oneFile = ""

for f in glob('*/*.md'):
    f = f.replace('\\', '/')
    if f.endswith(".md"):
        with open(f) as fi:
            oneFile += fi.read()

with open('all.md', 'w') as f:
    f.write(oneFile)


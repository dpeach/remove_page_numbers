import sys
import re

file = sys.argv[1]

def step1():
    with open(file, 'r+') as f:
        content = f.read()
        content = re.sub(r'([.!?])\n\n\d.+\n\n', r'\1\n\n', content)
        f.seek(0)
        f.write(content)
        f.truncate()
        f.close()

def step2():
    with open(file, 'r+') as f:
        content = f.read()
        content = re.sub(r'\n\n\d.+\n\n', r' ', content)
        f.seek(0)
        f.write(content)
        f.truncate()
        f.close()
        
step1()
step2()
import sys
f = open('test.txt')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)


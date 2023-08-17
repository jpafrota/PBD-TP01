import sys
import io
import re

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for line in input_stream:
    line = line.strip()
    line = re.sub(r'[^\w\s]', '',line)
    line = line.lower()
    for x in line:
        if x in punctuations:
            line=line.replace(x, " ")

    words = line.split()
    print('%d\t%s' % (int(words[1]), words[0]))
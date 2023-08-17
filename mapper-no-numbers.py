import sys
import io
import re
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')
for line in input_stream:
  line = line.strip()
  line = re.sub(r'[^\w\s]', '',line)
  line = line.lower()
  for x in line:
    if x in punctuations:
      line=line.replace(x, " ") 

  words=line.split()
  for word in words: 
    if not (re.match(r"[A-Za-z]+", word)): 
        continue
    print('%s\t%d' % (word, 1))
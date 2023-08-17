import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.lower()

    # parse the input we got from mapper.py
    count, word = line.split('\t')

    print ('%d\t%s' % (int(count), word))
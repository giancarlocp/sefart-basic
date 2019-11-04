#!/bin/python3
from functools import reduce
from mispar import mispar
letters = mispar.keys()


condi = lambda s: s[1] != 'x'
clean = lambda l: l.split()[1:-1]
def readBook(fn):
  with open(fn,'r',encoding='utf-8') as fi:
    book_raw = filter( condi, fi.readlines() )

  book = map( clean, book_raw )
  return book


suma = lambda x,y: x+y
gema = lambda c: mispar[c] if c in letters else 0
gematria = lambda w: reduce( suma, map(gema, w) )
def processBook(book):
  for line in book:
    for word in line:
      gem = gematria(word)
      if gem:
        print( '{0:>9} {1:>4d} {1:012b}'.format(word, gem) )
      else:
        print(word,end='')


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    print('''Use:  python3 gematria.py Genesis.txt
The file can be downloaded from:
  https://tanach.us/Server.txt?Genesis*&content=Consonants''')
    sys.exit()

  filename = sys.argv[1]
  book = readBook(filename)
  processBook(book)

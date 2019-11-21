import io
import re 
import string

encoding = 'utf8-*-'

with io.open('data.txt', 'r', encoding=encoding, newline='\n') as fin:
    text2 = fin.read()

regex = re.compile('[%s]' % re.escape(string.punctuation))

print(text2)
#removing non-ascii(non-utf-8 char)
def nonasc(text3):
	return ''.join([c if ord(c) < 128 else ' ' for c in text3])

def nonpun(text3):
	return regex.sub('', text3)

u=nonasc(text2)
k=nonpun(u)

print(k)
with io.open('data1.txt', 'w', encoding=encoding, newline='\n') as fout:
    fout.write(k)

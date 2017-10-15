import hashlib
import sys
import binascii
import itertools
import time
import numba

sha = '67ae1a64661ac8b4494666f58c4822408dd0a3e4'
word = 'qwinQWIN'
wordlist = list(itertools.combinations(word,4))
num = '580%(='
numlist = list(itertools.combinations(num,3))

def str_hash(message):
    sha1 = hashlib.sha1(message)
    return sha1.hexdigest()

def burp(message):
    message = ''.join(message) # convert to strings
    strhash = str_hash(message)
    if sha == strhash:
        print 'The message is:',message 
        return
    #return message

@numba.jit()        
def clean(check, word):
    for x in check:
        for i in xrange(len(word) / 2):
            if set((word[i], word[i + len(word)/2])).issubset(x):
                if x in check:
                    check.remove(x)

def main():
    stat = time.time()
    clean(wordlist,word)
    clean(numlist,num)
    for x in wordlist:
        for y in numlist:
            words = ''.join(x+y)+'*'
            message = itertools.permutations(words)
            map(burp, message)
    end = time.time()
    print 'Total used %d s.' % int(end-stat)

if __name__ == '__main__':
    main()

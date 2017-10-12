import hashlib
import itertools as itr
import time
startt = time.time()
import sys

def str_hash(str):
    sha = hashlib.sha1(str)
    encrypts = sha.hexdigest()
    return encrypts

chars = [('Q', 'q'), ('W', 'w'), ('%', '5'), ('(', '8'), ('=', '0'), ('I', 'i'), ('N', 'n'), ('*', '+')]

keyset = []

for i in xrange(256):
    keyset = ''
    for j in xrange(8):
        if (bin(i)[2:].zfill(8))[j] == '1':
            keyset += chars[j][1]
        else:
            keyset += chars[j][0]
#    if (('Q'in keyset) or ('W'in keyset) or ('%'in keyset)) and (('('in keyset) or ('='in keyset) or ('I'in keyset) or ('N'in keyset)):
    if (keyset.count('Q')+keyset.count('W')+keyset.count('%') >= 1) and ((keyset.count('(')+keyset.count('=')+keyset.count('I')+keyset.count('*')+keyset.count('N')) >= 2):
         keys = itr.permutations(keyset)
    for key in keys:
            k = str_hash(''.join(key))
            if k == '67ae1a64661ac8b4494666f58c4822408dd0a3e4':
                endt = time.time()
                print endt-startt
                print ''.join(key)
                break
#sys.exit()
#key = '(Q=win*5'
#time = 6.08299994469

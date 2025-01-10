'''
from secret import FLAG
from random import randint

def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def encrypt(m):
    c = ''
    for i in range(len(m)):
        ch = m[i]
        if not ch.isalpha():
            ech = ch
        else:
            chi = to_identity_map(ch)
            ech = from_identity_map(chi + i)
        c += ech
    return c

with open('output.txt', 'w') as f:
    f.write('Make sure you wrap the decrypted text with the HTB flag format :-]\n')
    f.write(encrypt(FLAG))
'''

def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)


def load_data(filename: str) -> str:
    with open(filename) as f:
        f.readline()
        enc = f.readline()
    return enc

def decrypt(enc: str) -> str:
    flag = ''
    for i in range(len(enc)):
        ech = enc[i]
        if not ech.isalpha():
            ch = ech
        else:
            echi = to_identity_map(ech)
            ch = from_identity_map(echi - i)
        flag += ch
    return flag

def pwn():
    enc = load_data('output.txt')
    flag = decrypt(enc)
    print(enc)
    print(f'HTB{{{flag}}}')

if __name__ == '__main__':
    pwn()

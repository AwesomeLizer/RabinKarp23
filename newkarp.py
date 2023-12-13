from random import randint

mod = 2**127 - 1
base = randint(1, mod)

def rabin_karp(s, p):
    pos = []
    hash_p = 0
    hash_s = 0
    h = 1

    for i in range(len(p)):
        hash_p = (base * hash_p + ord(p[i])) % mod
        hash_s = (base * hash_s + ord(s[i])) % mod
    
    for i in range(len(p) - 1):
        h = h*base % mod

    for i in range(len(s) - len(p) + 1):
        if hash_s == hash_p:
            pos.append(i)

        if i < len(s) - len(p):
            hash_s = (hash_s - ord(s[i])*h) % mod
            hash_s = (base * hash_s + ord(s[i+len(p)])) % mod
    return pos
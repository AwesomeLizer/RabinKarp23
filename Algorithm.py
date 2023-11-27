#Строки состоят из строчных и прописных английских букв.

base = 91
mod = 10**100
pattern = input()
text = input()

def p_hash(text, base, mod):
    L_hash = [0]
    p = 1
    for sym in text:
        L_hash.append(((L_hash[-1] * base) % mod + ord(sym)) % mod)
        p = (p * base) % mod
    return(L_hash, p)

pattern_hash, p = p_hash(pattern, base, mod)
pattern_hash = pattern_hash[-1]
text_hash, _ = p_hash(text, base, mod)
pos = []
for left_lim in range(len(text) - len(pattern) + 1):
    right_lim = left_lim + len(pattern)
    if pattern_hash == ((text_hash[right_lim] - (text_hash[left_lim] * p) % mod) % mod):
        pos.append(left_lim)

if pos:
    print(*pos)
else:
    print(-1)
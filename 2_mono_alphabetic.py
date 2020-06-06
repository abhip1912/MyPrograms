def E(s, d):
    ct = ''
    for i in s:
        if i.isspace():
            ct += ' '
            continue
        ct += (d[i])
    return ct

def D(s, d):
    pt = ''
    keys = list(d)
    values = list(d.values())
    for i in s:
        if i.isspace():
            pt += ' '
            continue
        pt += keys[values.index(i)]
    return pt
count = {'a':'m', 'b':'n', 'c':'b', 'd':'v', 'e':'c', 'f':'x', 'g':'z', 'h':'l', 'i':'k', 'j':'j', 'k':'h', 'l':'g', 'm':'f', 'n':'d', 'o':'s', 'p':'a', 'q':'p', 'r':'o', 's':'i', 't':'u', 'u':'y', 'v':'t', 'w':'r', 'x':'e', 'y':'w', 'z':'q'}
for i in count.items():
    print(i, end=' ')
print()
s1 = input("Enter string: ")
s1 = s1.lower()
s2= E(s1, count);
print("Encrypted text: ", s2)
s3 = D(s2, count);
print("Decrypted text: ", s3)

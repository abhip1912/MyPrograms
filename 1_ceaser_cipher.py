import time
def E(pt, k):
    ct = ''
    for i in pt:
        if i.isspace():
            ct += ' '
        elif i.islower():
            ct += chr((((ord(i)-97) + k) % 26) + 97)
        else:
            ct += chr((((ord(i)-65) + k) % 26) + 65)
    return ct

def D(ct, k):
    pt = ''
    for i in ct:
        if i.isspace():
            pt += ' '
        elif i.islower():
            pt += chr(((((ord(i)-97) - k) + 26) % 26) + 97)
        else:
            pt += chr(((((ord(i)-65) - k) + 26)% 26) + 65)
    return pt

print("Abhishek here...")
s1 = str(input("Enter any string: "))
key = int(input("Enter any interger key: "))

s2 = E(s1, key)
print("Encrypted string: ", s2)
s3 = D(s2, key)
print("Decrypted string: ", s3)
time.sleep(15)

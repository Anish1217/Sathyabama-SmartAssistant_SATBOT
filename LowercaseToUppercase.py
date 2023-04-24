st = input("Type here: ")
out = ''
for n in st:
    if n not in 'abcdefghijklmnopqrstuvwqxyz':
        out = out + n
    else:
        k = ord(n)
        l = k - 32
        out = out + chr(l)
print(out)

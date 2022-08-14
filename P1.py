s = str(input())
sl = list(s)
rev = []
pos = []
result = ''

for i in range(len(sl)):
    if ord(sl[i]) < ord('A') or (ord(sl[i]) > ord('Z') and ord(sl[i]) < ord('a')) or  ord(sl[i]) > ord('z'):
        pos.append(i)

for i in range(len(sl)):
    if ord(sl[len(sl)-i-1]) < ord('A') or (ord(sl[len(sl)-i-1]) > ord('Z') and ord(sl[len(sl)-i-1]) < ord('a')) or  ord(sl[len(sl)-i-1]) > ord('z'):
        pass
    else:
        rev.append(sl[len(sl)-i-1])

for i in range(len(sl)):
    if i not in pos:
        result += '' + rev[i]
    else:
        rev.insert(i, sl[i])
        result += '' + sl[i]

print(result)
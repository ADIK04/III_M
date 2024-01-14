znak_ascii  = chr(33)
print(znak_ascii)

for i in range(33,128):
    znak_ascii = chr(i)
    print(znak_ascii, end=' ')
    if i % 16 == 15:
        print()
print()
#cyrylica
print('Cyrylica')
print()
for i in range(1024,1279):
    znak_ascii = chr(i)
    print(znak_ascii, end=' ')
    if i % 16 == 15:
        print()

print()
#cyrylica
print('Tajski')
print()
for i in range(3584,3711):
    znak_ascii = chr(i)
    print(znak_ascii, end=' ')
    if i % 16 == 15:
        print()



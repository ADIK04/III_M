znak = '🌞'
znak1 = ord(znak)
znak2 = ord('🙂')

while znak1 <= znak2:
    print(znak, end = ' ')
    if znak1 % 16 == 15:
        print()
    znak1 += 1
    znak = chr(znak1)
print()







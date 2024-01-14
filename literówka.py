a = 10
zmienna = 'Dane'
b = 10.5

print(a)
print(zmienna)
print(b)
a = 10 * 10
print(a)

STALA = 'jAKIS TEKST'

# SZUKAMY LITERÓWKA
INF_OK = 'Hasło do serwisu wysłaliśmy na adres email: '
INF_BLAD = 'Podane adresy email sa rozne! '

imie = input('Podaj imie: ')
nazwisko = input('Podaj nazwisko: ')

adres_1 = input('Podaj adres email: ')
adres_2 = input('Podaj adres email: ')

print()

if adres_1 == adres_2:
    print(INF_OK + adres_1)
else:
    print(INF_BLAD)










# Lista zakupów, która usuwa duplikaty(powtarzające się słowa)
N = 5

wynik = []
i = 1
nowy = input()
wynik.append(nowy)

stary = nowy
nowy = input()

while nowy !='***' and i < N:
    if nowy != stary:
        if nowy not in wynik:
            i +=1
            wynik.append(nowy)
        stary = nowy
    nowy = input()

for j in range(i):
    print(wynik[j])



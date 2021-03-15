file_name = input() # podaj nazwę pliku wejsciowego
# file_name2 = input()  # podaj nazwę pliku wyjsciowego, jezeli chcesz zapisać do pliku

with open(f"{file_name}", "r") as plik:
    linie = plik.readlines()

# wczytanie danych
n = linie[0][:-1]  # liczba sloni
m_list = linie[1][:-1].split(sep=" ")  # masy sloni, jako lista
current_list = linie[2][:-1].split(sep=" ")  # wejsciowa kolejnosc sloni, jako lista
target_list = linie[3][:-1].split(sep=" ")  # docelowa kolejnosc sloni, jako lista

# zmiany wartosci str na int
n = int(n)
m_list = [int(el) for el in m_list]
current_list = [int(el) for el in current_list]
target_list = [int(el) for el in target_list]


chosen_list = []   #lista indeksów po które już mają cykl
cycles_m_list = []   #lista list mas w podziale na cykle

#glowna petla wyszukujaca masy w podziale na cykle
for i in range(1, n + 1):
    if i in chosen_list:  #jezeli ten indeks juz wystapil w innym cyklu idz dalej
        continue
    x_start = target_list.index(i)  # indeks w liscie targetu o i-tej wartosci slonia
    mass_list = [m_list[i-1]] #dodaj mase sprawdzanego slonia (indeksy numerowane od 0 a sloni od 1, wiec pomniejsz o 1)

    #pętla cyklu
    while True:
        if current_list[x_start] == i:  # jak trafimy na te sama wartosc - koniec cyklu
            break

        nowy_index = current_list[x_start]

        if nowy_index not in chosen_list:
            chosen_list.append(nowy_index)  #dodaj do listy z uzytymi indeksami
        mass_list.append(m_list[nowy_index-1])   #dodaj mase slonia z wybranej pozycji (indeksy numerowane od 0 a sloni od 1, wiec pomniejsz o 1)
        x_start = target_list.index(nowy_index)  # wyliczenie kojelnego indeksu startowego

    # po zakonczeniu cyklu dodaj liste masy sloni z danego cyklu
    cycles_m_list.append(mass_list)


#obliczenia, dwie metody i całość

def metod_1(cycle):
    return sum(cycle) + (len(cycle) - 2) * min(cycle)


def metod_2(cycle):
    return sum(cycle) + min(cycle) + (len(cycle) + 1) * min(m_list)

#koncowy rezultat
res = 0
for cycle in cycles_m_list:
    res += min(metod_1(cycle), metod_2(cycle))

#zapisz wynik do pliku
# with open(f"{file_name2}", "w") as plik:
#     plik.write(str(res))

# wypisz wynik
print(res)

# TO-DO - change into english

from tic_tac_toe.TTT import KolkoIKrzyzyk
#zapisywanie wyników do pliku
with open('wyniki.txt', 'w') as plik:
    plik.write('Nowa gra\n')

while True:
    #wyświetl instrukcje
    print(KolkoIKrzyzyk.instrukcja())
    user_input = input()
    if user_input == 'q':
        break
    elif user_input == 'n':
        nowa_gra = KolkoIKrzyzyk()
        print(nowa_gra)
        print(nowa_gra.opcje_gry())
        wybor_gry = input()

        #gra użytkownika z komputerem
        if wybor_gry == '1':
            login = input('Podaj swój login: ')
            with open('wyniki.txt', 'a', encoding='utf-8') as file:
                file.write(f'Użytkownik {login} ("O") vs komputer ("X") \n')

        #gra komputera z komputerem
        elif wybor_gry == "2":
            with open('wyniki.txt', 'a', encoding='utf-8') as file:
                file.write(f'Komputer ("O") vs komputer ("X") \n')
            nowa_gra.gra_komputer()
        else:
            print('niepoprawny wybór')
            continue
    else:
        continue

#główna pętla gry
    while True:
        if nowa_gra.gracz == 'O' and not nowa_gra.komputer:
            wybrane_pole = input(f'Gdzie postawić "{nowa_gra.gracz}"?:  ')        #wybór użytkownika

        else:
            wybrane_pole = nowa_gra.komputer_input()    #wybór komputera

        if wybrane_pole == 'q':
            break

        nowa_gra.ustaw_wybor(nowa_gra.gracz, wybrane_pole)  #przesyła informacje o ruchu

        nowa_gra.opis()  #info czyj jest ruch
        nowa_gra.rysuj_plansze()  # wyrysowanie obecnej planszy

        wynik = nowa_gra.sprawdz_czy_wygrana()  #sprawdzenie czy jest wygrana
        if wynik:               #jeżeli jest wygrana to zakoncz i zapisz info do pliku
            print(f'Wygrywa {nowa_gra.gracz}')
            with open('wyniki.txt', 'a', encoding='utf-8') as file:
                file.write(f'Wygrywa {nowa_gra.gracz}\n')
            break
        else:
            pass

        if '-' not in nowa_gra.plansza:     #jeżeli nie ma już ruchu - remis
            print('koniec gry, remis')
            with open('wyniki.txt', 'a', encoding='utf-8') as file:
                file.write(f'Remis')
            break

        nowa_gra.zmien_gracza()         #zmienia gracza po każdej turze

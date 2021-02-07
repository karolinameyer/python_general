from random import choice

class KolkoIKrzyzyk():
    def __str__(self):
        return ("Gra w kółko i krzyżyk")

    def __init__(self):
        self.plansza = '---------'
        self.gracz = 'X'
        self.komputer = False

    #zmienia gracza po każdej turze
    def zmien_gracza(self):
        if self.gracz == 'X':
            self.gracz = 'O'
        elif self.gracz == 'O':
            self.gracz = 'X'

    #włącza tryb komputer vs komputer
    def gra_komputer(self):
        self.komputer = True

    #wybór pola przez komputer
    def komputer_input(self):
        if (self.plansza[0:3] == "-O0") or (self.plansza[::3] == "-0O"):
            return 1
        if (self.plansza[0:3] == "O-0") or (self.plansza[1::3] == "0-O"):
            return 2
        if (self.plansza[0:3] == "OO-") or (self.plansza[2:7:2] == "-OO") or (self.plansza[2::3] == "-OO"):
            return 3
        #rozpisać resztę opcji dla "myślącego komputera

        wolne_miejsca = []
        for i, p in enumerate(self.plansza):
            if p == '-':
                wolne_miejsca.append(str(i+1))
        return choice(wolne_miejsca)

    #sprawdzenie poprawności wyboru i ustawienie wybranego pola
    def ustaw_wybor(self, gracz, wybor):
        if not wybor.isdigit() or int(wybor) not in range(1, 10):
            print('Zły wybór, nie podałeś liczby od 1 do 9 ')
            self.zmien_gracza()
        elif self.plansza[int(wybor)-1] == "-":
            self.plansza = self.plansza[:int(wybor)-1] + gracz + self.plansza[int(wybor):]
        else:
            print('Wybrane pole jest już zajęte')
            self.zmien_gracza()

    #sprawdzenie wygranej
    def sprawdz_czy_wygrana(self):
        if self.gracz * 3 in [
                self.plansza[:3],
                self.plansza[3:6],
                self.plansza[6:],
                self.plansza[::3],
                self.plansza[1::3],
                self.plansza[2::3],
                self.plansza[::4],
                self.plansza[2:7:2]]:
            return True
        else:
            return False
    def opis(self):
        print(f"\nRuch {self.gracz}")

    #wyrysowanie aktualnej planszy
    def rysuj_plansze(self):
        print(self.plansza[:3],self.plansza[3:6],self.plansza[6:9],sep="\n")

    @staticmethod
    def instrukcja():
        return 'KÓŁKO I KRZYŻYK \n "n" - nowa gra \n "q" - zakończ grę'

    @staticmethod
    def opcje_gry():
        return 'wybierz opcje gry: \n 1. ja vs komputer \n 2. komputer vs komputer'

import functions
import sys

class PrzetwarzanieSygnalow:
    def __init__(self):
        self.ilosc_wspolczynniki = 3
        self.probkowanie = 100

    def active_mode(self):
        while True:
            self.active = input()
            if self.active == 'q':
                sys.exit()
            try:
                self.active = int(self.active)
            except ValueError:
                print('Wpisz odpowiednia wartosc')
                continue
            else:
                return self.active

    def opcje_funkcji(self):
        while True:
            print("Wpisz 1 jesli chcesz zapisac funkcje\n"
                  "Wpisz 2 jesli chcesz wyswietlic funkcje\n"
                  "Wpisz 3 jesli chcesz zaszumic funkcje\n"
                  "Wpisz 4 jesli chcesz uzyc filtru\n"
                  "Wpisz 5 jesli chcesz wrocic\n"
                  "Wpisz q jesli chcesz wyjsc")
            self.active = self.active_mode()
            if self.active == 1:
                functions.zapis_funkcji(self.xvalues, self.wyniki)
                continue
            if self.active == 2:
                functions.rysuj_funkcje(self.xvalues, self.wyniki)
                continue
            if self.active == 3:
                self.wyniki = functions.zaszum_funkcje(self.wyniki)
                continue
            if self.active == 4:
                while True:
                    print("Wpisz 1 jesli chcesz uzyc filtra medianowego\n"
                          "Wpisz 2 jesli chcesz uzyc filtra sredniej\n"
                          "Wpisz q jesli chcesz wyjsc")
                    self.active = self.active_mode()
                    if self.active == 1:
                        self.wyniki = functions.filtr_mediana(self.wyniki)
                        break
                    if self.active == 2:
                        self.wyniki = functions.filtr_srednia(self.wyniki)
                        break
            if self.active == 5:
                break

    def run_app(self):
        while True:
            print("Wpisz 1 jesli chcesz wygenerowac funkcje\n"
                  "Wpisz 2 jesli chcesz wczytac funkcje\n"
                  "Wpisz q jesli chcesz wyjsc")
            self.active = self.active_mode()
            if self.active == 1:
                self.wspolczynniki = functions.wczytaj_wspolczynniki(self.ilosc_wspolczynniki)
                self.dmin, self.dmax = functions.wczytaj_dziedzine()
                self.probkowanie = functions.wczytaj_probkowanie()
                self.xvalues, self.wyniki, self.n = functions.generuj_funkcje(self.wspolczynniki, self.dmin, self.dmax,
                                                                              self.probkowanie)
                self.opcje_funkcji()

            elif self.active == 2:
                self.xvalues, self.wyniki = functions.odczyt_pliku()
                self.opcje_funkcji()
            else:
                print('Wpisz prwidlowa wartosc !!!')
                continue

if __name__ == "__main__":
    sygnal = PrzetwarzanieSygnalow()
    sygnal.run_app()
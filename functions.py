from math import sin
import matplotlib.pyplot as plt
from random import uniform
from statistics import median, mean
import csv

def wprowadz_liczbe(prompt):
    while True:
        try:
            liczba = int(input(prompt))
        except ValueError:
            print("Nie podano liczby")
            continue
        else:
            return liczba

def zwroc_string(prompt):
    while True:
        try:
            string = str(input(prompt))
        except ValueError:
            print("Podaj poprawna nazwe pliku")
            continue
        else:
            return string

def wczytaj_wspolczynniki(a):
    wspolczynniki = []
    print("y = Wspolczynnik 1 * sin( x * Wspolczynnik 2) + Wspolczynnik 3\n")
    for l in range(a):
        prompt = f"Podaj wspolczynnik {l+1} (int):\n"
        value = wprowadz_liczbe(prompt)
        wspolczynniki.append(value)
    print(wspolczynniki)
    return wspolczynniki

def wczytaj_dziedzine():
    while True:
        prompt = 'Podaj parametr dziedziny okreslajacy jej dolna wartosc:\n'
        dmin = wprowadz_liczbe(prompt)
        prompt = 'Podaj parametr dziedziny okreslajacy jej gorna wartosc:\n'
        dmax = wprowadz_liczbe(prompt)
        if dmax <= dmin:
            print("Wartość maksymalna dziedziny musi byc większa niż wartość"
                  "minimalna !!!")
            continue
        return dmin, dmax

def wczytaj_probkowanie():
    while True:
        prompt = "Podaj ilosc probek - minimum 100," \
                 " jesli podasz mniej to program przyjmie wartosc domyslna: 100 probek\n"
        probkowanie = wprowadz_liczbe(prompt)
        if probkowanie < 100:
            probkowanie = 100
            return probkowanie
        else:
            return probkowanie

def generuj_funkcje(wspolczynniki, dmin, dmax, probkowanie):
    probkowanie = (dmax - dmin) / (probkowanie)
    wyniki = []
    xvalues = []
    while dmin <= dmax:
        value = wspolczynniki[0] * sin(wspolczynniki[1] * dmin) + wspolczynniki[2]
        xvalues.append(dmin)
        dmin += probkowanie
        wyniki.append(value)
    n = int(len(wyniki))
    return xvalues, wyniki, n

def rysuj_funkcje(xvalues, wyniki):
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(xvalues, wyniki)
    plt.show()

def zapis_funkcji(xvalues, wyniki):
    while True:
        nazwa_pliku = zwroc_string("Podaj nazwe pliku bez rozszerzenia .csv:\n")
        nazwa_pliku += ".csv"
        try:
            with open(nazwa_pliku, "w") as plik:
                for i in range(len(xvalues)):
                    plik.write(str(xvalues[i]) + ';' + str(wyniki[i]) + '\n')
        except FileExistsError:
            print(f"Plik {nazwa_pliku} juz istnieje")
            continue
        else:
            print(f'Zapisano pomyslnie plik: ', nazwa_pliku)
            break

def zaszum_funkcje(wyniki):
    wyniki_zaszum = []
    for i in wyniki:
        wyniki_zaszum.append(i + uniform(-0.3,0.3))
    return wyniki_zaszum

def filtr_mediana(wyniki):
    mediana = []
    for i in range(len(wyniki)):
        if i < 2 or i > len(wyniki) - 3:
            mediana.append(wyniki[i])
        else:
            tab = [wyniki[i - 2], wyniki[i - 1], wyniki[i], wyniki[i + 1], wyniki[i + 2]]
            tab.sort()
            mediana.append(median(tab))
    return mediana

def filtr_srednia(wyniki):
    srednia = []
    for i in range(len(wyniki)):
        if i <= 2 or i > len(wyniki) - 3:
            srednia.append(wyniki[i])
        else:
            tab = [wyniki[i - 2], wyniki[i - 1], wyniki[i], wyniki[i + 1], wyniki[i + 2]]
            tab.sort()
            srednia.append(mean(tab))
    return srednia

def odczyt_pliku():
    while True:
        nazwa_pliku = zwroc_string("Podaj nazwe pliku bez rozszerzenia .csv:\n")
        nazwa_pliku += '.csv'
        xvalues = []
        wyniki = []
        try:
            with open(nazwa_pliku, 'r', newline='') as plik:
                reader = csv.reader(plik, delimiter=';')
                for row in reader:
                    xvalues.append(float(row[0]))
                    wyniki.append(float(row[1]))
        except FileNotFoundError:
            print(f"Plik {nazwa_pliku} nie istnieje")
            continue
        else:
            print("Pomyslnie wczytano funkcje")
            return xvalues, wyniki

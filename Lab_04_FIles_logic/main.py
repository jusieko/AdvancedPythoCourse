'''
LAB - Operacje na plikach w wyrażeniach logicznych
Utwórz plik i wpisz do niego kilka słów, np co widzisz za oknem :)

Utwórz funkcję, która jako parametr przyjmuje ścieżkę dostępu do pliku i zwraca ilość słów w tym pliku, jeśli potrzebujesz kroków pomocniczych oto i one:

Otwórz plik poleceniem open (możesz skorzystać z parametru encoding="utf-16" jeżeli trzeba)

Wczytaj plik do zmiennej korzystając z funkcji read()

"Rozbij" wczytaną zawartość korzystając z funkcji split()

Policz ile elementów jest zwracanych przez funkcję split()

Zwróć tą wartość

W głównym skrypcie:

zadeklaruj zmienną path i przypisz jej wartość wskazującą na plik utworzony na początku

napisz polecenie warunkowe, które sprawdzi czy plik istnieje

jeśli tak, wywoła funkcję, policzy ilość słów w pliku i wyświetli o tym informację

napisz wyrażenie logiczne, które wykona te same czynności, co wcześniej napisana instrukcja if
'''

import os


# file = open('file.txt', 'w')
# file.write(" How are you?\n It;s my python program")
# file.close()

def fun(plik):
    try:
        file = open(plik)
        content = file.read()
    except:
        print("wrong path")
        pass
    tab = content.split()
    words = len(tab)
    return words


path = 'filea.txt'

if os.path.exists(path):
    print('File has ', fun(path), 'words')

os.path.exists(path) and print('File has ', fun(path), 'words')

from datetime import datetime
import json

now = datetime.now()


def zapis_do_pliku(haslo, licznik_nieudanych, licznik_ogolny, litery, czas):
    dane_do_pliku = ''
    dane_do_pliku += f'Wylosowane hasło {haslo}\n'
    dane_do_pliku += f'Ilość prób nietrafionych {licznik_nieudanych}\n'
    dane_do_pliku += f'Ilość prób ogólnych {licznik_ogolny}\n'
    dane_do_pliku += f'Użyte litery {litery}\n'
    dane_do_pliku += f'Twój czas: {czas}'
    nazwa_pliku = input('Podaj nazwę pliku, w którym chcesz zapisać wynik gry: ')
    nazwa_pliku = nazwa_pliku + '-' + str(now)
    plik = open(f'{nazwa_pliku}.json', 'w')
    json.dump(dane_do_pliku, plik)
    plik.close()
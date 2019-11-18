#Import modułów zewnętrznych / wewnętrznych
import random
from datetime import datetime
from zapis_do_pliku import zapis_do_pliku

#Inicjalizacja krotki z grafikami szubienicy
grafiki = (
'''
    ---------
    |       |
    |       
    |       
    |
    |
    |
  -----  
''',
'''
     ---------
     |       |
     |       0
     |              
     |
     |
     |
   -----  
''',
'''
     ---------
     |       |
     |       0
     |       |     
     |       
     |
     |
   -----  
     ''',
'''
     ---------
     |       |
     |       0
     |       |       
     |       |
     |
     |
   -----  
     ''',
'''
     ---------
     |       |
     |       0
     |      /|       
     |       |
     |
     |
   -----  
     ''',
'''
     ---------
     |       |
     |       0
     |      /|)       
     |       |
     |
     |
   -----  
     ''',
'''
     ---------
     |       |
     |       0
     |      /|)       
     |       |
     |      /
     |
   -----  
     ''',
'''
     ---------
     |       |
     |       0
     |      /|)       
     |       |
     |      / )
     |
   -----  KONIEC
     '''
)

#Inicjalizacja zmiennych
new_haslo = ''
litery = ''
ilosc_sznas = len(grafiki) - 1
licznik_nieudanych = 0
licznik_ogolny = 0
chce_odpowiadac = ''
odpowiedz = ''
nazwa_pliku = ''
dane_do_pliku = ''
now = datetime.now()

#inicjalizacja krotki z słowami do odganięcia
zbior_hasel = ('amortyzator', 'roleta', 'wieszak', 'pralka', 'elektrohydrogumonapawarka', 'puszka', 'kubek', 'pizza', 'umywalka', 'autobus')

#Losowanie slowa z krotki z hasłami
haslo = random.choice(zbior_hasel)
ukryte_haslo = '-' * len(haslo)

#Opis gry
print(f'''
Witaj w grze WISIELEC, w której masz za zadanie odgadnąć wylosowane przez komputer słowo z stałej listy słow. Masz na to
zadanie jedynie {ilosc_sznas} szans. W trakcie gry możesz podawać litery, które według ciebie znajdują się w haśle. Jeżeli
jesteś pewny, że odgadłeś hasło możesz poporosić system o umożliwienie sprawdzenia hasła. Im szybciej odgadniesz hasło tym
więcej punktów dostaniesz. CZAS START. POWODZENIA !!!
''')

print(f'System wylosował dla ciebie następujące słowo do odgadnięcia {ukryte_haslo}')
start = datetime.now()

#Główna pętla progrmu
while licznik_nieudanych < 8:
    new_haslo = ''
    #Wyświetlenie podancyh przez gracza liter w trakcie gry
    print(f'Podane przez ciebie litery to: {litery}')
    litera = input('Podaj literę: ')
    #Jeżeli litera zwiera się już w ciągu liter podanych, następuje ponowne odpytanie użytkownika o nową literę
    if litera not in litery:
        litery += litera
    else:
        continue
    #Wyświetlenie odgadniętych liter z hasła, reszta pozostaje '-'
    for i in haslo:
        if i in litery:
            new_haslo += i
        else:
            new_haslo += '-'
    #Wyświtlenie grafiki z wisielcem w przypadku podania litery, która nie zawiera się w haśle
    if litera not in haslo:
        print(grafiki[licznik_nieudanych])
        licznik_nieudanych += 1
        print(f'Ilość szans pozostałych do zakończenia gry {8 - licznik_nieudanych}')
    print(new_haslo)
    #Użytkownik po każdym podaniu litery ma możliwość odgadnięcia hasła
    chce_odpowiadac = input('Jeżeli chcesz odgadnąć hasło, wpisz cokolwiek i zatwierdz ENTEREM, '
                            'w przeciwnym razie wciśnij ENTER i graj dalej')
    if chce_odpowiadac:
        odpowiedz = input('Podaj odpowiedz: ')
        break
    licznik_ogolny += 1

if licznik_nieudanych == 8:
    print('Nie udało ci się odganąć hasła, przykro mi')

if odpowiedz.lower() == haslo:
    stop = datetime.now()
    print('CZAS STOP. BRAWO, udało ci się odganąć hasło')
    czas = stop - start
    print(f'Czas, w jakim odganąłeś hasło wynosi: {czas}')
    #Zapis danych do pliku
    zapis_do_pliku(haslo, licznik_nieudanych, licznik_ogolny, litery, czas)

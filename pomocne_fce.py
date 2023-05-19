'''
Projekt ke zkoušce k rekvalifikačnímu kurzu ITnetwork
Evidence pojištění - zjednodušená verze
Autor: Jakub Orel
Kurz: Vývojář WWW aplikací (Python)
Popis: Tento soubor obsahuje pomocné funkce
'''


# Import modulů
import time
from datetime import datetime
import os

# Funkce pro čištění konzole
def cisti():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funkce pro zastavení programu na zadaný počet sekund
def zastav(sekundy):
    time.sleep(sekundy)

# Funkce vrací aktuální datum
def dnesni_datum():
    dnes = datetime.today()
    return dnes

# Funkce pro převod zadaného data na formát datetime
def prevod_string_na_datetime(datum):
    return datetime.strptime(datum, "%d.%m.%Y")
    
# Funkce pro převod data narození z databáze na formát datetime
def prevod_string_na_datetime_db(datum):
    return datetime.strptime(datum, "%Y-%m-%d %H:%M:%S") 

# Funkce pro kontrolu zadaného jména
def verifikace_jmena(jmeno):
    try:
        if len(jmeno) > 0 and jmeno.isalpha():
            return True
        else:
            return False
    except ValueError:
        return False

# Funkce pro kontrolu zadaného data narození
def verifikace_datumu(datum):
    try:
        datum_objekt = datetime.strptime(datum, "%d.%m.%Y")
        if datum_objekt > dnesni_datum():
            return False
        return True
    except ValueError:
        return False

# Funkce pro kontrolu zadaného telefonního čísla
def verifikace_telefonu(cislo):
    try:
        if len(cislo) == 9 and cislo.isnumeric():
            return True
        else:
            return False
    except ValueError:
        return False
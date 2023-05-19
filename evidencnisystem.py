'''
Projekt ke zkoušce k rekvalifikačnímu kurzu ITnetwork
Evidence pojištění - zjednodušená verze
Autor: Jakub Orel
Kurz: Vývojář WWW aplikací (Python)
Popis: Tento soubor obsahuje třídu EvidencniSystem a její metody pro zákaldní práci s databází
'''


# Import modulů
import sqlite3
import os
from datetime import datetime
from pomocne_fce import dnesni_datum, prevod_string_na_datetime, prevod_string_na_datetime_db

# Definice třídy EvidencniSystem
class EvidencniSystem:
    """Třída EvidencniSystem slouží k evidenci pojištěnců."""
    # Konstruktor třídy
    def __init__(self):
        databaze = os.path.join(os.path.dirname(__file__), "evidence_pojistencu.db") # Nastavení cesty k databázi
        self.conn = sqlite3.connect(databaze) # Připojení k databázi
        self.cursor = self.conn.cursor() # Inicilizace objektu cursor pro práci s databází
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pojistenci ( 
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                jmeno TEXT,
                                prijmeni TEXT,
                                datum_narozeni TEXT,
                                tel_cislo TEXT)''') # Vytvoření tabulky pojistenci a definice jejích sloupců, pokud již neexistuje
        self.conn.commit() # Commitnutí změn v databázi


    # Metoda pro výpočet věku pojištěnce
    def vypocet_veku(self, datum_narozeni):
        vek = dnesni_datum().year - datum_narozeni.year
        if (dnesni_datum().month, dnesni_datum().day) < (datum_narozeni.month, datum_narozeni.day):
            vek -= 1
        return vek
    
    # Metoda pro přídání nového pojištěnce do databáze
    def pridej_pojisteneho(self, pojisteny):
        datum_narozeni = prevod_string_na_datetime(pojisteny.datum_narozeni) # Převod datumu narození ze stringu na typ datetime
        self.cursor.execute("INSERT INTO pojistenci (jmeno, prijmeni, datum_narozeni, tel_cislo) VALUES (?, ?, ?, ?)", # Vložení nového pojištěnce do databáze
                            (pojisteny.jmeno, pojisteny.prijmeni, datum_narozeni, pojisteny.telefonni_cislo))
        self.conn.commit() # Commitnutí změn v databázi
    

 
    # Metoda pro vypsání všech uložených pojištěnců
    def vypis_pojistence(self):
        self.cursor.execute("SELECT * FROM pojistenci") # Výběr všech pojištěnců z databáze
        radky = self.cursor.fetchall() # Načtení všech řádků z databáze
        if radky: # Zjištění, zda databáze obsahuje řádky
            for radek in radky: # Iterace přes všechny řádky databáze
                datum_narozeni = prevod_string_na_datetime_db(radek[3]) # Převod datumu narození z databáze na objekt datetime 
                vek = self.vypocet_veku(datum_narozeni) # Výpočet věku pojištěnce
                print (f"Jméno: {radek[1]:<10} Příjmení: {radek[2]:<10} Věk: {vek:<5} Telefoní číslo: {radek[4]}") # Výpis pojištěnce
        else: # V případě, že databáze neobsahuje žádné pojištěnce
            print("Databéze neobsahuje žádné pojištěnce.")
    
    
    # Metoda pro vyhledání pojištěnce podle jména a příjmení
    def najdi_pojisteneho(self, jmeno, prijmeni):
        self.cursor.execute("SELECT * FROM pojistenci WHERE jmeno = ? AND prijmeni = ?", (jmeno, prijmeni)) # Výběr pojištěnce z databáze podle jména a příjmení
        radky = self.cursor.fetchall() # Načtení pojištěnce z databáze
        if radky: # Zjištění, zda databáze obsahuje řádky
            for radek in radky: # Iterace přes vybrané řádky
                datum_narozeni = prevod_string_na_datetime_db(radek[3]) # Převod datumu narození z databáze na objekt datetime
                vek = self.vypocet_veku(datum_narozeni) # Výpočet věku pojištěnce
                print (f"Jméno: {radek[1]:<10} Příjmení: {radek[2]:<10} Věk: {vek:<5} Telefoní číslo: {radek[4]}") # Výpis pojištěnce
        else: # V případě, že databáze neobsahuje hledaného pojištěnce
            print("Pojištěnec nenalezen.")
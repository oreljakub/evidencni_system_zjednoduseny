'''
Projekt ke zkoušce k rekvalifikačnímu kurzu ITnetwork
Evidence pojištění - zjednodušená verze
Autor: Jakub Orel
Kurz: Vývojář WWW aplikací (Python)
Popis: Hlavní soubor projektu, který obsahuje hlavní smyčku programu a volání funkcí z ostatních souborů
'''

# koment


#Import modulů
from pojistenec import Pojistenec
from evidencnisystem import EvidencniSystem
from ui import UI
from pomocne_fce import verifikace_jmena, verifikace_datumu, verifikace_telefonu, cisti, zastav
from datetime import datetime

# Vytvoření instance třídy EvidencniSystem
ev_system = EvidencniSystem()

# Hlavní cyklus programu
while True:
    moznost = UI()

    if moznost == "1": # Přidání pojištěnce
        cisti() # Vyčištění konzole
        jmeno = input("Zadejte jméno pojištěnce:\n ").strip().capitalize()
        while not verifikace_jmena(jmeno): # Kontrola zadaného jména a opakování zadání v případě špatného formátu
            print("Jméno se může skládat pouze z písmen. \n")
            jmeno = input("Zadejte znovu jméno pojištěnce:\n ").strip().capitalize()
        prijmeni = input("Zadejte příjmení pojištěnce:\n ").strip().capitalize()
        while not verifikace_jmena(prijmeni): # Kontrola zadaného příjmení a opakování zadání v případě špatného formátu
            print("Příjmení se může skládat pouze z písmen. \n")
            prijmeni = input("Zadejte znovu příjmení pojištěnce:\n ").strip().capitalize()
        datum_narozeni = input("Zadejte datum narození ve formátu dd.mm.rrrr:\n ")
        while not verifikace_datumu(datum_narozeni): # Kontrola zadaného data narození a opakování zadání v případě špatného formátu
            print("Zadané datum narození je buď neplatné, ve špatném formátu nebo v budoucnosti.")
            datum_narozeni = input("Zadejte znovu datum narození ve formátu dd.mm.rrrr:\n")
        telefonni_cislo = input("Zadejte telefonní číslo bez mezer a předvolby:\n ")
        while not verifikace_telefonu(telefonni_cislo): # Kontrola zadaného telefonního čísla a opakování zadání v případě špatného formátu
            print("Zadané telefonní číslo není ve správném formátu\n")
            telefonni_cislo = input("Zadejte znovu telefonní číslo bez mezer a předvolby:\n ")
        # Vytvoření instance třídy Pojistenec
        pojisteny = Pojistenec(jmeno, prijmeni, datum_narozeni, telefonni_cislo)
        ev_system.pridej_pojisteneho(pojisteny) # Zavolání metody třídy EvidencniSystem pro přidání pojištěnce do evidence
        input("\nPojištěnec byl úspěšně přidán do evidence.\nPro pokračovaní stiskněte libovolnou klávesu.")
        cisti() 

    elif moznost == "2": # Vyhledání pojištěnce
        cisti() # Vyčištění konzole
        jmeno = input("Zadejte jméno pojištěnce:\n ").capitalize()
        prijmeni = input("Zadejte příjmení pojištěnce:\n ").capitalize()
        pojisteny = ev_system.najdi_pojisteneho(jmeno, prijmeni) # Zavolání metody třídy EvidencniSystem pro vyhledání pojištěnce v evidenci
        input("\nPro pokračovaní stiskněte libovolnou klávesu.")
        cisti() # Vyčištění konzole
        

    elif moznost == "3": # Výpis všech pojištěnců
        cisti() # Vyčištění konzole
        ev_system.vypis_pojistence() # Zavolání metody třídy EvidencniSystem pro výpis všech pojištěnců
        input("\nPro pokračovaní stiskněte libovolnou klávesu.")
        cisti() # Vyčištění konzole
    
    elif moznost == "4": # Ukončení programu
        print("Program se ukončuje.")
        ev_system.conn.close() # Uzavření spojení s databází
        zastav(1) # Zastavení programu na 1 sekundu
        cisti() # Vyčištění konzole
        break # Ukončení while cyklu

    else: # Vyžádání správné volby
        input()("Neplatná volba, zkuste to znovu.\nPro pokračovaní stiskněte libovolnou klávesu.")
        cisti() # Vyčištění konzole
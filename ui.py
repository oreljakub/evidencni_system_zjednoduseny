'''
Projekt ke zkoušce k rekvalifikačnímu kurzu ITnetwork
Evidence pojištění - zjednodušená verze
Autor: Jakub Orel
Kurz: Vývojář WWW aplikací (Python)
Popis: Tento soubor obsahuje uživatelské rozhraní
'''


# Import modulu
import pomocne_fce

# Funkce pro uživatelské rozhraní
def UI():
    pomocne_fce.cisti() # Vyčištění konzole
    print(f"{25*'-'}\nEvidence pojištěnců\n{25*'-'}") # Hlavička programu
    print("Vyberte jednu z následujících možností:\n")
    print("1. Přidat pojištěnce")
    print("2. Vyhledat pojištěnce podle jména a příjmení")
    print("3. Vypsat všechny pojištěnce")
    print("4. Ukončit program")
    moznost = input("\n") # Uživatelský vstup
    return moznost
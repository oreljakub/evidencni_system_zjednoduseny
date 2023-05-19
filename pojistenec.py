'''
Projekt ke zkoušce k rekvalifikačnímu kurzu ITnetwork
Evidence pojištění - zjednodušená verze
Autor: Jakub Orel
Kurz: Vývojář WWW aplikací (Python)
Popis: Tento soubor obsahuje třídu Pojistenec
'''


# Definice třídy Pojistenec
class Pojistenec:
    """Třída reprezentující pojištěnce."""
    def __init__(self, jmeno, prijmeni, datum_narozeni, telefonni_cislo): # Konstruktor třídy
      self.jmeno = jmeno
      self.prijmeni = prijmeni
      self.datum_narozeni = datum_narozeni
      self.telefonni_cislo = telefonni_cislo
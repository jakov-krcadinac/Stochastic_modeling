
import random
import time
import csv
from collections import defaultdict
import sys

# SIMBOLI 
nar = "nar"  # naranca
grozd = "gro"  # grozdje
lim = "lim"  # limun
tr = "tre"  # tresnja
jag = "jag"   # jagoda
srce = "src"  # FREE SPIN srce
kesa = "kes"  # JACKPOT kesa

# reelovi bez blank polja
reel1 = [lim, tr, tr, nar, grozd, kesa, srce, jag]  # duple tresnje
reel2 = [kesa, tr, nar, lim, grozd, srce, jag, lim] # dupli lim
reel3 = [tr, grozd, lim, tr, nar, kesa, tr, jag]  # trostruke tresnje, nema srca


# funkcija za sljedeći simbol na pojedinačnom reelu
def sljedeci(r):
    r += 1 
    if r==8:
        return 0
    return r

# funkcija za vrcenje svih reelova
def azuriraj_vockice(r1, r2, r3):
    
    r1 = sljedeci(r1)
    r2 = sljedeci(r2)
    r3 = sljedeci(r3)
    
    return f"{reel1[r1]} {reel2[r2]} {reel3[r3]}", r1, r2, r3

# funkcija koja vrti samo reel 2 i 3
def azuriraj_vockice_reel_2_3(r1, r2, r3):
    
    r2 = sljedeci(r2)
    r3 = sljedeci(r3)
    
    return f"{reel1[r1]} {reel2[r2]} {reel3[r3]}", r1, r2, r3

# funkcija koja vrti samo reel 3
def azuriraj_vockice_reel_3(r1, r2, r3):

    r3 = sljedeci(r3)
    
    return f"{reel1[r1]} {reel2[r2]} {reel3[r3]}", r1, r2, r3


def procjeni_kombinaciju(a1, a2, a3):
    
    if a1 == kesa and a2 == kesa and a3 == kesa:
        #print("JACKPOT! Osvojili ste 100€")
        return 30
    if (a1 == kesa and a2 == kesa) or (a2 == kesa and a3 == kesa) or (a1 == kesa and a3 == kesa):
        #print("Osvojili ste x2 BONUS! Osvojeni iznos u sljedecoj vrtnji će se poduplati!")
        return "x2"
    if a1 == srce and a2 == srce:
        #print("Osvojili ste FREE SPIN! Sljedeca vrtnja vam je besplatna.")
        return "FS"
    if ((a1 == tr and a2 == tr and a3 == tr) or (a1 == lim and a2 == lim and a3 == lim) or
        (a1 == nar and a2 == nar and a3 == nar) or (a1 == grozd and a2 == grozd and a3 == grozd) or
        (a1 == jag and a2 == jag and a3 == jag)):
        #print("VOCNI JACKPOT! Osvojili ste 5€")
        return 3
    if ((a1 == tr and a2 == tr) or (a2 == tr and a3 == tr) or (a1 == tr and a3 == tr) or
        (a1 == lim and a2 == lim) or (a2 == lim and a3 == lim) or (a1 == lim and a3 == lim) or
        (a1 == nar and a2 == nar) or (a2 == nar and a3 == nar) or (a1 == nar and a3 == nar) or
        (a1 == grozd and a2 == grozd) or (a2 == grozd and a3 == grozd) or (a1 == grozd and a3 == grozd) or
        (a1 == jag and a2 == jag) or (a2 == jag and a3 == jag) or (a1 == jag and a3 == jag)):
        #print("DUPLE VOCKICE! Osvojili ste 1€")
        return 1
    
    #print("Kombinacija nazalost nije dobitna. Pokusajte ponovo.")
    return 0




# inicijalno postavljanje
r1, r2, r3 = -1, -1, -1   

total_profit = 0  #  ukupni profit od pokretanja slota
lista_svih_vrtnji = []     # lista u kojoj se biljeze podaci za svaku vrtnju

free_spin = False
bonus = False

# postavi zeljeni broj vrtnji
broj_vrtnji = 100000

for i in range(broj_vrtnji):
    # naplacivanje vrtnje
    total_profit += 0.5
    spin_profit = 0.5

    if free_spin:
        total_profit -= 0.5
        spin_profit -= 0.5
        free_spin = False

    # generiranje nasumične kombinacije
    izvucena_komba = [random.randint(0,7), random.randint(0,7), random.randint(0,7)]

    rezultat = procjeni_kombinaciju(reel1[izvucena_komba[0]], reel2[izvucena_komba[1]], reel3[izvucena_komba[2]])

    ishod = "fail"
    # pretvaranje rezultata u zapis ishoda za dokumentiranje
    if rezultat == 30:
        ishod = "JACKPOT"
    elif rezultat == "x2":
        ishod = "bonus_x2"
    elif rezultat == "FS":
        ishod = "free_spin"
    elif rezultat == 3:
        ishod = "Vocni_jackpot"
    elif rezultat == 1:
        ishod = "Duple_vockice"

    # provjera je li u prosloj rundi osvojen x2 bonus. Ako jest trenutni dobitak se poduplava
    if bonus and type(rezultat) == int:
        total_profit -= 2 * rezultat
        spin_profit -= 2 * rezultat
        bonus = False
    # zastavica za x2 BONUS
    elif rezultat == "x2":
        bonus = True
    # zastavica za FREE SPIN
    elif rezultat == "FS":
        free_spin = True
    # izračunaj ostverene profite pri vrtnji
    else:
        spin_profit -= rezultat
        total_profit -= rezultat 

    """
    print("Dobivena kombinacija:", reel1[izvucena_komba[0]], reel2[izvucena_komba[1]], reel3[izvucena_komba[2]])
    print("Ishod kombinacije:", ishod)
    print("Profit vrtnje:", spin_profit)
    print("Ostvaren ukupni profit:", total_profit)
    print()
    """
    komba = reel1[izvucena_komba[0]] + ", " + reel2[izvucena_komba[1]] + ", " +  reel3[izvucena_komba[2]]
    pom_lista = [komba, ishod, spin_profit, total_profit]
    lista_svih_vrtnji.append(pom_lista)

print("Ostvaren ukupni profit:", total_profit)






CSV_COLUMNS = ['Kombinacija', 'Ishod', 'Spin_profit', 'Total_profit']

# funkcija za upis evidencije svih vrtnji u csv datoteku
def upisi_u_novu_csv_datoteku(path, lista_odgovarajucih_redova):

    try:

        with open(path, 'w', encoding = 'ISO-8859-1') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(CSV_COLUMNS)
            
            for red in lista_odgovarajucih_redova:
                writer.writerow(red)

    except IOError:
        print("I/O Error")

path = "evidencija_vrtnji.csv"

upisi_u_novu_csv_datoteku(path, lista_svih_vrtnji)
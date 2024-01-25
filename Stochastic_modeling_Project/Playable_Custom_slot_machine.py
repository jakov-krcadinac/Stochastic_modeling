
import random
import time

# SIMBOLI 
nar = "\U0001F34A"  # naranca
grozd = "\U0001F347"  # grozdje
lim = "\U0001F34B"  # limun
tr = "\U0001F352"  # tresnja
jag = "\U0001F353"   # jagoda
srce = "\U0001F496"  # FREE SPIN srce
kesa = "\U0001F4B0"  # JACKPOT kesa

# reelovi bez blank polja
reel1 = [lim, tr, tr, nar, grozd, kesa, srce, jag]  # duple tresnje
reel2 = [kesa, tr, nar, lim, grozd, srce, jag, lim] # dupli lim
reel3 = [tr, grozd, lim, tr, nar, kesa, tr, jag]  # trostruke tresnje, nema srca
#for i in range (100):
#    print([random.randint(1, 10) for i in range(10)])

print("\nDobrodosli u pseudoslucajnu igru na srecu TERMINALNE VOCKICE!\nOkusajte svoju srecu vrtnjom vocne slot masine sa sljedecim reelovima:\n")

print("Reel 1: ", reel1)
print("Reel 2: ", reel2)
print("Reel 3: ", reel3)
print()

"""  test == za emotikon Unicode znakove
if nar == nar:
    print("lol")
else:
    print("nej")
"""

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
        print("JACKPOT! Osvojili ste 100€")
        return 100
    if (a1 == kesa and a2 == kesa) or (a2 == kesa and a3 == kesa) or (a1 == kesa and a3 == kesa):
        print("Osvojili ste x2 BONUS! Osvojeni iznos u sljedecoj vrtnji će se poduplati!")
        return "x2"
    if a1 == srce and a2 == srce:
        print("Osvojili ste FREE SPIN! Sljedeca vrtnja vam je besplatna.")
        return "FS"
    if ((a1 == tr and a2 == tr and a3 == tr) or (a1 == lim and a2 == lim and a3 == lim) or
        (a1 == nar and a2 == nar and a3 == nar) or (a1 == grozd and a2 == grozd and a3 == grozd) or
        (a1 == jag and a2 == jag and a3 == jag)):
        print("VOCNI JACKPOT! Osvojili ste 5€")
        return 5
    if ((a1 == tr and a2 == tr) or (a2 == tr and a3 == tr) or (a1 == tr and a3 == tr) or
        (a1 == lim and a2 == lim) or (a2 == lim and a3 == lim) or (a1 == lim and a3 == lim) or
        (a1 == nar and a2 == nar) or (a2 == nar and a3 == nar) or (a1 == nar and a3 == nar) or
        (a1 == grozd and a2 == grozd) or (a2 == grozd and a3 == grozd) or (a1 == grozd and a3 == grozd) or
        (a1 == jag and a2 == jag) or (a2 == jag and a3 == jag) or (a1 == jag and a3 == jag)):
        print("DUPLE VOCKICE! Osvojili ste 1€")
        return 1
    
    print("Kombinacija nazalost nije dobitna. Pokusajte ponovo.")
    return 0




# inicijalno postavljanje
r1, r2, r3 = -1, -1, -1   

ulog = 10
free_spin = False
bonus = False

print("Na pocetku raspolazete s 10€. Jedna vrtnja kosta 0.5€. Za zaustavljanje slot masine pritisnite kombinaciju Ctrl+C\n")
user_input = input("Pokreni vockice: (da/ne) ")
while user_input == "da":
    # naplacivanje vrtnje
    ulog -= 0.5

    if free_spin:
        ulog += 0.5
        free_spin = False

    print(f"Zavrtili ste slot. Trenutno raspolazete s {ulog}€.")

    if bonus:
        print("U ovoj vrtnji imate x2 bonus. Ako osvojite FREE SPIN, x2 bonus se prenosi na sljedecu vrtnju.")

    # PROCES VRTNJE SLOTA
    try:
        while True:
            # generiraj trenutni string 
            current_string, r1, r2, r3  = azuriraj_vockice(r1, r2, r3)

            # printanje trenitnog stringa na način da će ga sljedeći string pregaziti trenutni
            print(current_string, end='\r', flush=True)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Stisnut gumb.")
        #print(r1, r2, r3)  

        # generiranje nasumične kombinacije
        izvucena_komba = [random.randint(0,7), random.randint(0,7), random.randint(0,7)]

        # malo vrtnje nakon klika
        for i in range(5):
            current_string, r1, r2, r3  = azuriraj_vockice(r1, r2, r3)
            print(current_string, end='\r', flush=True)
            time.sleep(0.1)
        
        # vrtnja do generiranje random kombinacije
            
        # reel 1
        while r1 != izvucena_komba[0]:
            current_string, r1, r2, r3  = azuriraj_vockice(r1, r2, r3)
            print(current_string, end='\r', flush=True)
            time.sleep(0.1)

        # reel 2
        for i in range(4):
            current_string, r1, r2, r3  = azuriraj_vockice_reel_2_3(r1, r2, r3)
            print(current_string, end='\r', flush=True)
            time.sleep(0.1)  
        while r2 != izvucena_komba[1]:
            current_string, r1, r2, r3  = azuriraj_vockice_reel_2_3(r1, r2, r3)
            print(current_string, end='\r', flush=True)
            time.sleep(0.1)

        # reel 3
        for i in range(4):
            current_string, r1, r2, r3  = azuriraj_vockice_reel_3(r1, r2, r3)
            print(current_string, end='\r', flush=True)
            time.sleep(0.1)  
        while r3 != izvucena_komba[2]:
            current_string, r1, r2, r3  = azuriraj_vockice_reel_3(r1, r2, r3)
            print(current_string, end='\r', flush=True)
            time.sleep(0.1)
        
        time.sleep(0.6)
        print("\n")

        rezultat = procjeni_kombinaciju(reel1[izvucena_komba[0]], reel2[izvucena_komba[1]], reel3[izvucena_komba[2]])
        # provjera je li u prosloj rundi osvojen x2 bonus. Ako jest trenutni dobitak se poduplava
        if bonus and type(rezultat) == int:
            ulog += 2 * rezultat
            if rezultat != 0:
                print(f"Zbog x2 bonusa osvojili ste {2 * rezultat}€ umjesto {rezultat}€.")
            bonus = False

        elif rezultat == "x2":
            bonus = True

        elif rezultat == "FS":
            free_spin = True

        else:
            ulog += rezultat 

        #print("\n\nCilj:")
        #print(reel1[izvucena_komba[0]], reel2[izvucena_komba[1]], reel3[izvucena_komba[2]])
        

    #print("\niiiiii nastavljamo")
    #print(r1, r2, r3) 
    user_input = input("\nZavrti jos jednom: (da/ne) ")

if user_input == "ne":
    print(f"\nOdlazite s {ulog}€.\nHvala na igranju i doviđenja.")
#Užduotis:
#Žaidėjas atsako į klausimus, pavyzdžiui: Kas, kur, kada ir kaip? 
#Programa sugeneruoja atskiras sakinio dalis ir suformuoja sakinį į jį įvedusi žaidėjo 
# surašytus atsakymus.

#Žaidimo taisyklės:
#Kada, kur, kas, su kuo, ką veikia. Pvz. Šiandien (1 žaidėjas) Afrikoje 
# (2 žaidėjas) Petras (4 žaidėjas) su Maryte (5 žaidėjas) skaito day.lt (6 žaidėjas).

import random
import sys

print("Žaidimas \"Kas, Kur, Kada\" \n")

def Zaidimas():

    print("Parašykite atsakymus į klausimus ir spauskite \"Enter\"! \n")

    Kada = input("Kada? ")

    a = ("Afrikoje", "Šiaurės ašigalyje", "didžiausiam pasaulio užpakalyje", "geriau neklausk kur", "Nikaragvoje", "Pabezdūnų kaime")
    Kur = random.choice(a)

    Kas = input("Kas? ")

    b = ("Vaivorykštiniu vienaragiu", "jo didenybe Radžiu", "Nitanu Gausėda", "mažuoju Hitleriu Gražuliu")
    Su_kuo = random.choice(b)

    c = ("medžioja", "patruliuoja", "hipnotizuoja", "operuoja", "galvoja")
    Ka_veikia = random.choice(c)

    Ka = input("Ką? ")

    print(" ")

    txt ="{}, {} {} su {} {} {} \n"
    print(txt.format(Kada, Kur, Kas, Su_kuo, Ka_veikia, Ka))
    
    def kartot():
        k = input("Ar norėtumėte pakartoti šį žaidimą? Taip / Ne ")
        print(" ")
        while k not in ("Taip", "taip", "Ne", "ne"):
            print("Jūs, Ponas(-ia), nemokate rašyti ! ! ! \n")
            return kartot()
        else: 
            while k in ("Ne", "ne"):
                def quit():
                    sys.exit()
            else:
                if k == "Taip" or "taip":
                    return Zaidimas()
                
    kartot()
     
Zaidimas()


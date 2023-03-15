import random
import numpy as np
import pandas as pd
import colorama
from termcolor import colored

colorama.init()
verben = pd.read_csv(r"C:\Users\bchri\OneDrive\Dokumente\Programmieren\LATEIN\lattrain\vokabeln.csv")
verben = verben.loc[verben.Wortart == "v"]

to_use = []
for v in verben.Latein.values :
    s = v.split(";")
    if len(s)==3:
        to_use.append(s)
#print(to_use)
#to_use = np.array(to_use, dtype=object)

anzahl = int(input("Wie viele Stammformane sollen geübt werden? "))
#subset = np.random.choice(to_use, int(anzahl))

for i in range(anzahl):
    v = random.choice(to_use)
    print("Wie lauten die Stammformen von " + colored(f"{v[0]}", "red") + " ? ", end="")
    nix = input()
    for form in v:
        print(colored(form, "yellow"), end = "")
    print()


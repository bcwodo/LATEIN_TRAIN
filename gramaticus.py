import pandas as pd
import random

vdf = pd.read_excel("Muster_Worte.xlsx", sheet_name="verben")
sdf = pd.read_excel("Muster_Worte.xlsx", sheet_name="substantive")

def train_verb(df = vdf):
    maxzeilen = df.shape[0]-2
    maxspalten = df.shape[1]-1
    anzahl = input("Wie viele Verben willst Du üben? ")
    anzahl = int(anzahl)
    for a in range(anzahl):
        c = random.randint(4,maxspalten)
        z = random.randint(0,maxzeilen)
        verb = df.iloc[z,c]
        _ = input(f"Kennst Du die Form von '{verb}' ?")
        print(df.iloc[z,:4])


def train_substantiv(df = sdf):
    maxzeilen = df.shape[0]-2
    maxspalten = df.shape[1]-1
    anzahl = input("Wie viele Substantive willst Du üben? ")
    anzahl = int(anzahl)
    for a in range(anzahl):
        c = random.randint(2,maxspalten)
        z = random.randint(0,maxzeilen)
        kasus = df.iloc[z,0]
        numerus = df.iloc[z,1]
        deklination = df.columns[c]
        wort = df.iloc[0,c]
        _ = input(f"Kennst Du die Form der '{deklination}' [{wort}] im {kasus}, {numerus}' ?")
        print(df.iloc[z,c])

def ende():
    done = False
    while not done:
        print()
        wahl = input("Ende (e) oder Substantive (s) oder Verben (any key)? ")
        if wahl == "e":
            done = True
        elif wahl == "s":
            train_substantiv()
        else:
            train_verb()

ende()
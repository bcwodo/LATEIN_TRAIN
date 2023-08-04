import pandas as pd
import random

vdf = pd.read_excel("Muster_Worte.xlsx", sheet_name="verben")

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

train_verb()
import random
from os import path
import time
import datetime
import difflib
import numpy as np
import pandas as pd
from numpy.random import choice
from konjungator import konjungator

def load():
    df = pd.read_csv("vokabeln.csv")
    return df

def backup(df):
    backupfolder = path.join(path.dirname(__file__), "backup")
    datum = str(pd.Timestamp.today().date())
    fname = "vokabeln" + datum + ".csv"
    pfad = path.join(backupfolder, fname)
    df.to_csv(pfad, index=False)
    #print(backupfolder)
    #print(pfad)


def add(df):
    # Startwerte
    done = False
    zeile = df.shape[0]
    print("\nHier gibst Du neue Vokabeln ein!")
    print(f"Das zuletzt eingetragene Wort ist {df.iloc[zeile-1, 1]}.")
    while not done:
        #Eingabe
        la = input("\nLatein Wort: ")
        de = input("Deutsches Wort (Trennen mit ;): ")
        #Speichern
        temp = pd.DataFrame(index=[zeile], columns=["Latein", "Deutsch", "Kartei"])
        temp.iloc[0,0] = la
        temp.iloc[0,1] = de
        temp.iloc[0,2] = 1
        df = df.append(temp)

        # Loop
        weiter = input("Noch ein Wort (n = nein)? ")
        if weiter == "n":
            done = True
        else:
            zeile +=1
    return df

def training(df, n = 3):
    df.sort_values(['Kartei'], ascending=[1], inplace=True)
    modus = input("Willst Du die Worte in Latein (l) oder Deutsch (d) sehen?")
    rn = list(range(n))
    random.shuffle(rn)
    if modus == "l":
        for i in rn:
            antwort = input(f"\nÜberlege das deutsche Wort für:  {df.iloc[i,0]} ! Weiter? ")
            print(f"Das deutsche Wort ist:  {df.iloc[i,1]} !")
            richtig = input("war es richtig (j)?")
            if richtig == "j":
                df.iloc[i,2] += 1
            #zusatz = input("Konjungieren (k) oder deklinieren (d)?")
            #if zusatz == "k":
            #    konjungator(df.iloc[i,0])
    if modus == "d":
        for i in rn:
            antwort = input(f"\nÜberlege das lateinische Wort für:  {df.iloc[i,1]} ! Weiter? ")
            print(f"Das Wort in Latein ist:  {df.iloc[i,0]} !")
            richtig = input("war es richtig (j)?")
            if richtig == "j":
                df.iloc[i,2] += 1
            #zusatz = input("Konjungieren (k) oder deklinieren (d)?")
            #if zusatz == "k":
            #    konjungator(df.iloc[i,0])
    df.sort_index(inplace=True)
    return df


def menue(df):
    done = False
    while not done:
        print("\nWas möchtest Du machen?")
        eingabe = input("e = Vokabeln eingeben, t = trainieren, q = ende ")
        if eingabe == "e":
            df = add(df)
        elif eingabe == "t":
            anz = int(input("Wie viele Vokabeln möchtest Du trainieren? "))
            df = training(df, anz)
        else:
            done = True
    return df

def gruss(df):
    print("\nSalve! Willkommen beim Vokabel-Trainer")
    anzahl = df.shape[0]
    fach, anz_fach = np.unique(df["Kartei"].values, return_counts = True)
    print(f"Es sind {anzahl} Vokabeln in der Kartei.")
    for i in range(len(fach)):
        print(f"{anz_fach[i]} Karten sind in Fach {fach[i]}.")


if __name__ == "__main__":
    vok = load()
    backup(vok)
    gruss(vok)
    vok = menue(vok)
    vok.to_csv("vokabeln.csv", index=False)


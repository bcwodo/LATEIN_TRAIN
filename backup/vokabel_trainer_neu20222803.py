#!/usr/bin/env python3
import random
from os import path
import os
import sys
import time
import datetime
import difflib
import numpy as np
import pandas as pd
from numpy.random import choice
from konjungator import konjungator

os.chdir(sys.path[0])

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
        wa = input("Wortart (v/s/x) ?")
        #Speichern
        temp = pd.DataFrame(index=[zeile], columns=["Latein", "Deutsch", "Kartei", "Wortart"])
        temp.iloc[0,0] = la
        temp.iloc[0,1] = de
        temp.iloc[0,2] = 1
        temp.iloc[0,3] = wa
        df = pd.concat([df, temp])
    

        # Loop
        weiter = input("Noch ein Wort (n = nein)? ")
        if weiter == "n":
            done = True
        else:
            zeile +=1
    return df

def training(df, n = 3):
    nummer = 1
    wort_falsch = []
    antwort_falsch = []
    df.sort_values(['Kartei'], ascending=[1], inplace=True)
    modus = input("Willst Du die Worte in Latein (l) oder Deutsch (d) sehen?")
    rn = list(range(n))
    random.shuffle(rn)
    if modus == "l":
        for i in rn:
            antwort = input(f"\n{nummer}) Überlege das deutsche Wort für:  {df.iloc[i,0]} ! Weiter? ")
            print(f"Das deutsche Wort ist:  {df.iloc[i,1]} !")
            richtig = input("war es richtig (j)?")
            if richtig == "j":
                df.iloc[i,2] += 1
            else:
                wort_falsch.append(df.iloc[i,0])
                antwort_falsch.append(df.iloc[i,1])
            nummer += 1
    if modus == "d":
        for i in rn:
            antwort = input(f"\n{nummer}) Überlege das lateinische Wort für:  {df.iloc[i,1]} ! Weiter? ")
            print(f"Das Wort in Latein ist:  {df.iloc[i,0]} !")
            richtig = input("war es richtig (j)?")
            if richtig == "j":
                df.iloc[i,2] += 1
            else:
                wort_falsch.append(df.iloc[i,1])
                antwort_falsch.append(df.iloc[i,0])
            nummer += 1
    df.sort_index(inplace=True)
    if wort_falsch != []:
        wiederholung(wort_falsch, antwort_falsch)
    return df

def wiederholung(wort, antwort):
    print("\n\nJetzt schauen wir nochmal auf das, was Du nicht so gut konntest!")
    time.sleep(1)
    for w, a in zip(wort, antwort):
        antwort = input(f"\nÜbersetze nochmal:  {w}")
        print(f"Die Übersetzung ist:  {a}")
        input("Weiter mit <Enter>")
    time.sleep(1)
    print("\nMerke Dir die worte gut!")


def reorga(df):
    df["Kartei"] = df["Kartei"]- df["Kartei"].min()
    return df

def menue(df):
    done = False
    while not done:
        print("\nWas möchtest Du machen?")
        eingabe = input("e = Vokabeln eingeben, t = trainieren, eo = Karten nach vorne einordnen, q = ende ")
        if eingabe == "e":
            df = add(df)
        elif eingabe == "t":
            anz = int(input("Wie viele Vokabeln möchtest Du trainieren? "))
            df = training(df, anz)
        elif eingabe == "eo":
            df = reorga(df)
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


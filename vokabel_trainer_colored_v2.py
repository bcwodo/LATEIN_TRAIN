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
from numpy.random import default_rng
from termcolor import colored
import colorama


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
            stammform = df.iloc[i,0].split(";")
            print(f"\n{nummer}) Überlege Stammform und das deutsche Wort für: " +colored(f"{stammform[0]}", "cyan") + " !", end="")
            _ = input()
            for s in stammform[0:]:
                print(colored(f"{s}", "cyan"), end="")
            print(" !")
            print(f"Das deutsche Wort ist: " +colored(f"{df.iloc[i,1]}", "yellow") + " !")
            richtig = input("war es richtig (j)?")
            if richtig == "j":
                df.iloc[i,2] += 1
            else:
                wort_falsch.append(df.iloc[i,0])
                antwort_falsch.append(df.iloc[i,1])
            nummer += 1
    if modus == "d":
        for i in rn:
            print(f"\n{nummer}) Überlege das lateinische Wort für: " + colored(f"{df.iloc[i,1]}", "cyan") + " !", end="")
            _ = input()
            print(f"Das Wort in Latein ist:  " + colored(f"{df.iloc[i,0]}", "yellow") + " !")
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


def training_verb(df, n = 3):
    richtig = 0
    train_df = df.loc[df["Wortart"]=="v"]
    rng = default_rng()
    wahl = rng.choice(train_df.shape[0] - 1, size=n, replace=False)
    for w in wahl:
        wort = train_df.iloc[w, 0]
        frag = wort.split(";")
        input(f"Formen von {frag[0]} ?")
        for f in frag:
            print(f)
        ant = input("richtig (j) ?")
        if ant == "j":
            richtig += 1
    print(f"\n\nDu hast {richtig/n*100:.2f}% richtig!")
    return df



def wiederholung(wort, antwort):
    print("\n\nJetzt schauen wir nochmal auf das, was Du nicht so gut konntest!")
    time.sleep(1)
    for w, a in zip(wort, antwort):
        print(f"\nÜbersetze nochmal: " + colored(f"{w}", "red"), end="")
        antwort = input()
        print(f"Die Übersetzung ist: " + colored(f"{a}", "yellow"))
        input("Weiter mit <Enter>")
    time.sleep(1)
    print("\nMerke Dir die worte gut!")


def reorga(df):
    df["Kartei"] = 1 #df["Kartei"]- df["Kartei"].min()
    return df

def menue(df):
    done = False
    while not done:
        print("\nWas möchtest Du machen?")
        eingabe = input("e = Vokabeln eingeben, t = trainieren, eo = Karten nach vorne einordnen, v = Verben, q = ende ")
        if eingabe == "e":
            df = add(df)
        elif eingabe == "t":
            anz = int(input("Wie viele Vokabeln möchtest Du trainieren? "))
            df = training(df, anz)
        elif eingabe == "eo":
            df = reorga(df)
        elif eingabe == "v":
            anz = int(input("Wie viele Verben möchtest Du trainieren? "))
            df = training_verb(df, anz)
        elif eingabe == "k":
            df = korrektor(df)
        elif eingabe == "s":
            df = suche(df)
        elif  eingabe == "q":
            done = True
        else:
            print("Treffe bitte eine Auswahl!\n")
    return df


def korrektor(df):
    sprache = input("Guggst Du <D>eutsch oder <L>atein?")
    if sprache == "d":
        option = list()
        pref = input("Wie Wort anfange? ")
        for w in df["Deutsch"].values:
            if w.startswith(pref):
                option.append(w)
        for i,o in enumerate(option):
            print(i, o)
        wortnr = int(input("Also, was Wort wolle - gugg Nummer?" ))
        suchwort = option[wortnr]
        aenderung = input("Wie soll heißen? ")
        print(f"{suchwort} wurde {aenderung}")
        df.loc[df["Deutsch"]==suchwort, "Deutsch"] = aenderung

    elif sprache == "l":
        option = list()
        pref = input("Wie Wort anfange? ")
        for w in df["Latein"].values:
            if w.startswith(pref):
                option.append(w)
        for i,o in enumerate(option):
            print(i, o)
        wortnr = int(input("Also, was Wort wolle - gugg Nummer?" ))
        suchwort = option[wortnr]
        aenderung = input("Wie soll heißen? ")
        print(f"{suchwort} wurde {aenderung}")
        df.loc[df["Latein"]==suchwort, "Latein"] = aenderung
    else:
        print("Das gibt's was nicht!")
    return df

def suche(df):
    option = list()
    pref = input("Wie Wort anfange? ")
    print(df.loc[(df["Latein"].str.startswith(pref)) | (df["Deutsch"].str.startswith(pref)), :])
    

    return df

def gruss(df):
    print("\nSalve! Willkommen beim Vokabel-Trainer")
    anzahl = df.shape[0]
    fach, anz_fach = np.unique(df["Kartei"].values, return_counts = True)
    print(f"Es sind {anzahl} Vokabeln in der Kartei.")
    for i in range(len(fach)):
        print(f"{anz_fach[i]} Karten sind in Fach {fach[i]}.")


if __name__ == "__main__":
    colorama.init()
    vok = load()
    backup(vok)
    gruss(vok)
    vok = menue(vok)
    vok.to_csv("vokabeln.csv", index=False)


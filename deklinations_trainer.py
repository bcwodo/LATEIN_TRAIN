import random
from os import path
import time
import datetime
import difflib
import numpy as np
import pandas as pd
from numpy.random import choice
from deklinator import deklinator

def load():
    df_in = pd.read_csv("vokabeln.csv")
    df_out = df_in[df_in.Wortart == "s"]
    return df_out

def get_random_word(dataframe, number):
    upper = dataframe.shape[0]
    rn_list = np.random.randint(0, upper, number)
    rn_words = dataframe.iloc[rn_list, 0]
    return list(rn_words)
    

df = load()

done = False
while not done:
    n = int(input("Wie viele Substantive willst Du deklinieren? "))
    verben = get_random_word(df, n)
    for v in verben:
        input(f"\nDekliniere {v} !")
        print()
        deklinator(v)

    numol = input("Nochmal? (n = Nein) ")
    if numol == "n":
        done = True




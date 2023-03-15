import pandas as pd 
import numpy as np
df = pd.read_csv("vokabeln.csv")
df
df["Kartei"] = 1
df
df.to_csv("vokabeln.csv", index=False)
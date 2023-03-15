import pandas as pd 


def deklinator(substantiv):   #substantiv = input("Welches Wort soll ich deklinieren? ")
    if substantiv[-2:] == "us":
        stamm = substantiv[:-2]
        ns = substantiv
        np = stamm + "i"
        gs = ""
        gp = ""
        ds = stamm + "o"
        dp = stamm + "is"
        aks = stamm + "um"
        akp = stamm + "os"
        if stamm[-1] == "i":
            vs = stamm
        else:
            vs = stamm + "e"
        vp = stamm + "i" 
        fs = ""
        fp = ""
    elif substantiv[-1] == "a":
        stamm = substantiv[:-1]
        ns = substantiv
        np = stamm + "ae"
        gs = ""
        gp = ""
        ds = stamm + "ae"
        dp = stamm + "is"
        aks = stamm + "am"
        akp = stamm + "as"
        vs = substantiv
        vp = stamm + "ae" 
        fs = ""
        fp = ""
    elif substantiv[-2:] == "um":
        stamm = substantiv[:-2]
        ns = substantiv
        np = stamm + "a"
        gs = ""
        gp = ""
        ds = stamm + "o"
        dp = stamm + "is"
        aks = stamm + "um"
        akp = stamm + "a"
        vs = substantiv
        vp = stamm + "a" 
        fs = ""
        fp = ""
    elif substantiv[-3:] == "tor":
        stamm = substantiv
        ns = substantiv
        np = stamm + "es"
        gs = ""
        gp = ""
        ds = stamm + "i"
        dp = stamm + "ibus"
        aks = stamm + "em"
        akp = stamm + "es"
        vs = ""
        vp = "" 
        fs = ""
        fp = ""
    else:
        print(f"Das Substantiv {substantiv} scheint irregulär zu sein!\n")

    if "ns" in locals():
        d4t = dict(Nominativ = [ns, np], Genitiv = [gs, gp], Dativ = [ds, dp], Akkusativ = [aks, akp], Vokativ = [vs, vp], Fall6 = [fs,fp])
        tabout = pd.DataFrame(d4t, index=["Singular", "Plural"])
        print(tabout.T)


if __name__ == "__main__":
    done = False
    substantiv = input("Welches Wort soll ich deklinieren? ")
    while not done:
        deklinator(substantiv)
        substantiv = input ("\n Noch ein Substantiv (Wort oder n=Nein) ?")
        if substantiv == "n":
            done = True

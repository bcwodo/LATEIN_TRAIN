def konjungator(verb):
    AUSNAHMEN = []
    E_ENDUNG_PRAESENS = ["o", "s", "t", "mus", "tis", "nt"]
    A_ENDUNG_PRAESENS = ["o", "s", "t", "mus", "tis", "nt"]
    I_ENDUNG_PRAESENS = ["o", "s", "t", "mus", "tis", "unt"]

    stamm = verb[:-2]
    art = stamm[-1]

    if verb in AUSNAHMEN:
        print("Bäh")
    elif art == "e":
        for e in E_ENDUNG_PRAESENS:
            print(stamm + e)
    elif art == "i":
        for e in I_ENDUNG_PRAESENS:
            print(stamm + e)
    elif art == "a":
        for i,e in enumerate(A_ENDUNG_PRAESENS):
            if i == 0:
                print(stamm[:-1] + e)
            else: print(stamm + e)


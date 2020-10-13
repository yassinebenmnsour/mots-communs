#yassine benmansour
#renvoyer une liste formée des mots communs à deux textes

def mots(T1, T2):
    L1 = T1.split()
    L2 = T2.split()

    a = []

    for mot in L1:
        if mot in L2:
            a.append(mot)

    return a


T1 = "Yassine  est un nom marocaine"
T2 = "Yassine est web developper"
print(mots(T1, T2))

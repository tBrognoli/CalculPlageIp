
from tkinter.messagebox import *

def plage(listeIp, nombreHote):

    i = 0
    nbBitReseau = 0
    pasDe = 0

    while (nombreHote + 2) >= pow(2, i):
        i += 1
        nbBitReseau = 32 - i
        pasDe = pow(2, i)
        if (nombreHote + 2) <= pow(2, i):
            break

    ip = str(listeIp[0]) + "." + str(listeIp[1]) + "." + str(listeIp[2]) + "."

    resultListe = list()

    i=0
    while i<len(listeIp):
        resultListe.append(int(listeIp[i]))
        i+=1

    resultListe.append(ip)
    resultListe.append(nbBitReseau)
    resultListe.append(pasDe)
    resultListe.append(maskSsRes(nbBitReseau))
    return resultListe


def verifIpVal(listeIp):
    i=0
    while i<len(listeIp):
        listeIp[i] = int(listeIp[i])
        i +=1

    if listeIp[3] > 255:
        listeIp[2] = int(listeIp[2] + (listeIp[3] / 255)-1)
        listeIp[3] = 255

    if listeIp[2] > 255:
        listeIp[1] = int(listeIp[1] + (listeIp[2] / 255)-1)
        listeIp[2] = 255

    if listeIp[1] > 255:
        listeIp[0] = int(listeIp[0] + (listeIp[1] / 255)-1)
        listeIp[1] = 255

    if listeIp[1] > 255:
        showwarning("Erreur", "Adresse ip non valide ou nombre d'hôtes trop grand")

    return listeIp


def maskSsRes(nbBitReseau):
    lastOctetdeci = 0
    mask = ""

    if nbBitReseau <= 8:
        nbBitResLastOctet = 8 - nbBitReseau
        j = 0

        h = 7
        while j < nbBitResLastOctet:
            lastOctetdeci += pow(2, h)
            h -= 1
            j += 1
            mask = str(lastOctetdeci) + ".0.0.0"

        return mask

    elif nbBitReseau <= 16 and nbBitReseau > 8:

        nbBitResLastOctet = nbBitReseau -  8
        j = 0
        h = 7

        while j < nbBitResLastOctet:
            lastOctetdeci += pow(2, h)
            h -= 1
            j += 1

            mask = "255." + str(lastOctetdeci) + ".0.0"

        return mask

    elif nbBitReseau <= 24 and nbBitReseau > 16:

        nbBitResLastOctet = nbBitReseau - 16
        j = 0
        h = 7

        while j < nbBitResLastOctet:
            lastOctetdeci += pow(2, h)
            h -= 1
            j += 1

            mask = "255.255." + str(lastOctetdeci) + ".0"

        return mask

    elif nbBitReseau <= 32 and nbBitReseau > 24:

        nbBitResLastOctet = nbBitReseau - 24
        j = 0
        h = 7

        while j < nbBitResLastOctet:
            lastOctetdeci += pow(2, h)
            h -= 1
            j += 1

            mask = "255.255.255." + str(lastOctetdeci)

        return mask
        return 1


def valideIp(listeIp, nbHote):

#Verif Ip
    if len(listeIp) != 4:
        showwarning("Erreur", "L'adresse Ip doit être composée de 4 entiers séparé par des '.'")
        return 1
    i =0
    while i < len(listeIp):
        try:
            listeIp[i] = int(listeIp[i])
        except:
            showwarning("Erreur", "L'adresse Ip doit être composée de 4 entiers")
            return 1

        if listeIp[i] > 255 or listeIp[i] < 0:
            showwarning("Erreur", "Chaque nombre composant l'Ip doit être compris entre 0 et 255")
            return 1
        i +=1

#Verif nbHote
    try:
        nbHote = int(nbHote)
    except:
        showwarning("Erreur", "Le nombre d'hôte doit être un entier.")
        return 1
    if nbHote < 0:
        showwarning("Erreur", "Le nombre d'hôte doit être supérieur à 0")
        return 1
    return 0


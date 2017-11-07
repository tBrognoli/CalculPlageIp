from tkinter import *
from tkinter.messagebox import *
from Fonctions.fonctions import *

class fenetreGui(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(sticky="NSEW")
        self.master.title("Calculer une plage Ip")
        self.createWidgets()

    def createWidgets(self):
        #Création des objets variables
        self.ipVar = StringVar()
        self.ipVar.set("0.0.0.0")

        self.nbHoteVar = StringVar()
        self.nbHoteVar.set("0")

        self.ipSsrVar = StringVar()
        self.ipSsrVar.set("0.0.0.0/n")

        self.ipBroadVar = StringVar()
        self.ipBroadVar.set("0.0.0.0/n")

        self.maskVar = StringVar()
        self.maskVar.set("255.255.255.255")

        self.plageIp = ""
        self.j = 0

        #Création Widgets
        self.menuBar = Menu(self)
        menuFichier = Menu(self.menuBar, tearoff=0)

        self.menuBar.add_cascade(label="Fichier", menu=menuFichier)
        menuFichier.add_command(label="Afficher tableau", command=self.tableauPow)
        menuFichier.add_command(label="version .txt", command=self.versionTxt)
        menuFichier.add_separator()
        menuFichier.add_command(label="Quitter", command=self.quit)

        menuTxt = Menu(self.menuBar, tearoff=0)

        self.menuBar.add_cascade(label=".txt", menu=menuTxt)
        menuTxt.add_command(label="Afficher", command=self.versionTxt)
        menuTxt.add_command(label="Reset .txt", command=self.resetTxt)

        self.master.config(menu=self.menuBar)

        mainFrame = LabelFrame(self, text="Formulaire", borderwidth=2, relief="groove")
        mainFrame.columnconfigure(0, weight=0)
        mainFrame.columnconfigure(1, weight=1)

        ipLabel = Label(mainFrame, text="Adresse Ip :")
        ipEntry = Entry(mainFrame, textvariable=self.ipVar)

        nbHoteLabel = Label(mainFrame, text="Nombre d'hôtes :")
        nbHoteEntry = Entry(mainFrame, textvariable=self.nbHoteVar)

        validButton = Button(mainFrame, text="Valider", command=self.validerPlage)

        resultFrame = LabelFrame(self, text="Plage ip", borderwidth=2, relief="groove")
        resultFrame.columnconfigure(0, weight=0)
        resultFrame.columnconfigure(1, weight=1)


        idSsrLabel = Label(resultFrame, text="Ip SSR :")
        idSsrEntry = Entry(resultFrame, textvariable=self.ipSsrVar)

        ipBroadLabel = Label(resultFrame, text="Ip Broadcast :")
        ipBroadEntry = Entry(resultFrame, textvariable=self.ipBroadVar)

        maskLabel = Label(resultFrame, text="Masque SsR :")
        maskEntry = Entry(resultFrame, textvariable=self.maskVar)

        quitButton = Button(resultFrame, text="Fermer", command=self.quit)
        #Placement Widgets
        mainFrame.grid(column=0, row=0, sticky="NSEW")

        ipLabel.grid(column=0, row=0, sticky="NSEW")
        ipEntry.grid(column=1, row=0, sticky="NSEW")

        nbHoteLabel.grid(column=0, row=1, sticky="NSEW")
        nbHoteEntry.grid(column=1, row=1, sticky="NSEW")

        validButton.grid(column=0,columnspan=2, row=2, sticky="NSEW")


        resultFrame.grid(column=0, row=1, sticky="NSEW")

        idSsrLabel.grid(column=0, row=0, sticky="NSEW")
        idSsrEntry.grid(column=1, row=0, sticky="NSEW")

        ipBroadLabel.grid(column=0, row=1, sticky="NSEW")
        ipBroadEntry.grid(column=1, row=1, sticky="NSEW")

        maskLabel.grid(column=0, row=2, sticky="NSEW")
        maskEntry.grid(column=1, row=2, sticky="NSEW")

        quitButton.grid(column=0,columnspan=3, row=3, sticky="NSEW")


    def validerPlage(self):
        adresseIp = self.ipVar.get()
        nombreHote = self.nbHoteVar.get()

        listIp =adresseIp.split(".")

        if valideIp(listIp,nombreHote) ==0:
            i=0
            while i < len(listIp):
                listIp[i]=int(listIp[i])
                i+=1

            nombreHote = int(nombreHote)
            resultListe = plage(listIp, nombreHote)

            ipTempSSR = str(resultListe[4]) + str(resultListe[3])
            listIpSsr = ipTempSSR.split(".")
            listIpSsr = verifIpVal(listIpSsr)
            ipSsr= str(listIpSsr[0]) +"."+ str(listIpSsr[1]) +"."+ str(listIpSsr[2]) +"."+ str(listIpSsr[3]) + "/" + str(resultListe[5])
            self.ipSsrVar.set(ipSsr)

            ipTempBroad = str(resultListe[4]) + str(resultListe[3] + resultListe[6] -1)
            listIpBroad = ipTempBroad.split(".")
            listIpBroad = verifIpVal(listIpBroad)
            ipBroad = str(listIpBroad[0]) +"."+ str(listIpBroad[1]) +"."+ str(listIpBroad[2]) +"."+ str(listIpBroad[3]) + "/" + str(resultListe[5])
            self.ipBroadVar.set(ipBroad)

            self.maskVar.set(resultListe[7])

            self.j += 1
            self.plageIp += "\nPlage Ip" + str(self.j)
            self.plageIp += "\nIp sous réseau : " + ipSsr + "\nIp de broadcast" + ipBroad + "\n\n"


    def versionTxt(self):
        topTxt = Toplevel(master=self)
        textTxt = Text(topTxt)
        textTxt.insert(INSERT, "    Versions txt de vos plage Ip\n")

        textTxt.insert(END, self.plageIp)
        textTxt.pack(expand=1, fill=BOTH)

        button = Button(topTxt, text="Femer", command=topTxt.destroy)
        button.pack()


    def resetTxt(self):
        self.plageIp =""


    def tableauPow(self):
        topTab = Toplevel(master=self)

        photo = PhotoImage(file="TabFx.png")

        canvasTab = Canvas(topTab, width=874, height=493)
        canvasTab.create_image(0, 0, anchor=NW, image=photo)
        canvasTab.image=photo
        canvasTab.pack()
        button = Button(topTab, text="Fermer", command=topTab.destroy)
        button.pack()


if __name__ == '__main__':
    fenetreGui().mainloop()
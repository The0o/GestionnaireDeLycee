from tkinter import *
import tkinter
from tkinter import ttk
from tkinter.messagebox import *
import datetime
from tkinter import filedialog
import os
#from faker import Faker
from EmploiDuTemps import EmploiDuTemps
from ExportEDT import ExportEDT

def __ajout__(nom_base):
    """Methode qui simule une petite base de donnees

    Args :
    """

    f = Faker("FR_fr")
    ajouts = nom_base

    #Ajout prof
    for i in range(10):
        ajouts.add_prof(1 + i, f.first_name(), f.last_name())

    #Ajout classe
    ajouts.add_classe(1, "2nd1", 10)
    ajouts.add_classe(2, "2nd2", 11)
    ajouts.add_classe(3, "2nd3", 12)
    ajouts.add_classe(4, "2nd4", 13)
    ajouts.add_classe(5, "2nd5", 14)
    ajouts.add_classe(6, "1er1", 15)
    ajouts.add_classe(7, "1er2", 16)
    ajouts.add_classe(8, "1er3", 17)
    ajouts.add_classe(9, "1er4", 18)
    ajouts.add_classe(10, "1er5", 19)
    ajouts.add_classe(11, "TG1", 20)
    ajouts.add_classe(12, "TG2", 21)
    ajouts.add_classe(13, "TG3", 22)
    ajouts.add_classe(14, "TG4", 23)
    ajouts.add_classe(15, "TG5", 24)

    #Ajout eleve
    j = 1
    k = 0
    for i in range(400):
        if j in [1, 2, 3, 4, 5]:
            k = 0
        elif j in [6, 7, 8, 9, 10]:
            k = 1
        else:
            k = 2
        if ajouts.voir_effectif_classe(j) != 30:
            ajouts.add_eleve(i+100, f.first_name(), f.last_name(), j, f.date_between_dates(datetime.date(2005-k, 1, 1), datetime.date(2005-k, 12, 31)))
        else:
            j += 1
            ajouts.add_eleve(i+100, f.first_name(), f.last_name(), j, f.date_between_dates(datetime.date(2005-k, 1, 1), datetime.date(2005-k, 12, 31)))

    #Ajout matiere
    ajouts.add_matiere(1, "NSI")
    ajouts.add_matiere(2, "Mathematiques")
    ajouts.add_matiere(3, "Sport")
    ajouts.add_matiere(4, "Eneignement Scientifique")
    ajouts.add_matiere(5, "Philosophie")
    ajouts.add_matiere(6, "Espagnol")
    ajouts.add_matiere(7, "Histoire-Geo")
    ajouts.add_matiere(8, "EMC")
    ajouts.add_matiere(9, "Vie de classe")

    #Ajout
    s = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
    m = 0
    for i in range(5):
        for j in range(10):
            m += 1
            ajouts.add_horaire(m, 8+j, 9+j, s[i], True)

    #Ajout matiere-prof
    ajouts.add_matiere_prof(10, 1)

    #Ajout salle
    ajouts.add_salle(1, "E310", 30, "normal")
    ajouts.add_salle(2, "E311", 30, "normal")
    ajouts.add_salle(3, "E312", 30, "normal")
    ajouts.add_salle(4, "E313", 30, "normal")
    ajouts.add_salle(5, "E314", 30, "normal")
    ajouts.add_salle(6, "E315", 30, "normal")
    ajouts.add_salle(7, "E316", 30, "normal")
    ajouts.add_salle(8, "E317", 30, "normal")
    ajouts.add_salle(9, "E318", 30, "normal")
    ajouts.add_salle(10, "E319", 30, "normal")
    ajouts.add_salle(11, "E301", 30, "normal")
    ajouts.add_salle(12, "E302", 30, "normal")
    ajouts.add_salle(13, "E303", 30, "normal")
    ajouts.add_salle(14, "E304", 30, "normal")

    import random

    #Ajout cours
    horaire_hasard = [i+1 for i in range(50)]
    for z in range(35):
        hasard = f.random_int(1, 9)
        s = random.choice(horaire_hasard)
        horaire_hasard.remove(s)
        ajouts.add_cours(hasard, hasard, 1, f.random_int(1, 14), s, 101)

#NE PAS OUBLIER, POUR LES CHANGEMENTS DE DONNEES SUR LE TYPE "HEURE", DE CREER UN ONGLET SPECIAL (PROF ABSENT, COURS DEPLACE...)
#Ne pas oublier de verifier les données mises dans les input (verifier que ce soit le bon type)
#Faire quelque chose de plus propre

class InterfaceGraphique:
    """Classe à OBLIGATOIREMENT utiliser avec la classe "EmploiDuTemps".
    Cette classe cree une interface graphique de la classe "EmploiDuTemps"
    Il est obligatoire d'installer la classe ImageEmploiDuTemps pour pouvoir
    utiliser la fonctionnalite "Voir l'emploi du temps".
    Cepandant, la non-installation du module ne nuira pas au reste de la classe
    """

    def __init__(self, connecteur):
        #Connecteur de type EmploiDuTemps
        self.connecteur = connecteur

    def bouton_pdf(self):
        fenetre = tkinter.Tk()
        #fenetre.attributes("-zoomed", True)
        fenetre.wm_state("zoomed")

        label = Label(fenetre, text="Veuillez sélectionner votre action à réaliser", font = ("Time", 20, "bold"))
        label.place(height = self.hauteur / 2.5, width = self.largeur)

        texte = Label(width = self.largeur, text = "NotePro", font = ("Time", 40), bg = "purple")
        texte.place(height = self.hauteur // 6, width = self.largeur)

        bouton = Button(fenetre, text="Voir l'emploi du temps d'un professeur", command = lambda:[fenetre.destroy(), self.choisir_donnee_edt("prof")])
        bouton.place(x = 0, y = self.hauteur / 2 + (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Retour", command = lambda:[fenetre.destroy(), self.activer_fenetre()])
        bouton.place(x = 0, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Voir l'emploi du temps d'un eleve", command = lambda:[fenetre.destroy(), self.choisir_donnee_edt("eleve")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Quitter", command = lambda:[fenetre.destroy()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        fenetre.mainloop()

    def choisir_donnee_edt(self, typ):
        fenetre = tkinter.Tk()
        #fenetre.attributes("-zoomed", True)
        fenetre.wm_state("zoomed")
        milieu = (self.largeur/2-self.largeur/100)/2
        supprimer = False

        texte = Label(text = "NotePro", font = ("Time", 40), bg = "purple")
        texte.place(height = self.hauteur // 6, width = self.largeur)

        bouton = Button(fenetre, text="Retour", command = lambda:[fenetre.destroy(), self.bouton_pdf()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 4, height = self.hauteur/7, width = self.largeur/2)

        _str = StringVar()
        chemin = Entry(fenetre, width = int(self.largeur / 3))
        chemin.insert(0, "Selectionner le chemin du fichier à enregistré en cas d'export en PDF")
        chemin.place(y = self.hauteur / 1.75, x = milieu, width = self.largeur/2)

        def clear_search(event):
            if chemin.get() == "Selectionner le chemin du fichier à enregistré en cas d'export en PDF":
                chemin.delete(0, END)

        def insert_search(event):
            if chemin.get() == "":
                chemin.insert(0, "Selectionner le chemin du fichier à enregistré en cas d'export en PDF")


        choix_export = tkinter.Radiobutton(fenetre, text = "Uniquement voir l'emploi du temps", variable = _str, value = 1)
        choix_export.place(x = 0, y = self.hauteur/1.5, width = self.largeur)
        choix_export.select()

        choix_export2 = tkinter.Radiobutton(fenetre, text = "Exporter en image", variable = _str, value = 2)
        choix_export2.place(x = 0, y = self.hauteur/2, width = self.largeur)

        chemin.bind("<Button-1>", clear_search)
        chemin.bind("<FocusOut>", insert_search)

        if typ == "eleve":
            liste = self.connecteur.voir_eleve()
        else:
            liste = self.connecteur.voir_prof()
        liste_donnee = ["Voir l'emploi du temps de quel personne ?"]
        for i in range(len(liste)):
            t = ""
            for j in range(len(liste[i])):
                t += str(liste[i][j]) + " "
            liste_donnee.append(t)
        entree = ttk.Combobox(fenetre, values=liste_donnee)
        entree.current(0)
        entree.place(y = self.hauteur / 4 + self.hauteur / 100 + self.hauteur / 7, x = milieu, width=self.largeur/2-self.largeur/100)
        
        bouton = Button(fenetre, text="Voir l'emploi du temps", command = lambda:[self.verif(entree.current(), _str.get(), chemin.get(), typ, fenetre)])
        bouton.place(x = 0, y = self.hauteur / 4, height = self.hauteur/7, width = self.largeur/2)

        fenetre.mainloop()

    def verif(self, current, choix, chemin, typ, fenetre):
        if current != 0:
            if typ == "eleve":
                _id = self.connecteur.voir_info_eleve()[current-1]
                liste_cours = self.connecteur.cours_eleve(_id)
            else:
                _id = self.connecteur.voir_info_professeur()[current-1]
                liste_cours = self.connecteur.cours_prof(_id)
            liste_matiere = []
            if len(liste_cours) == 0:
                showinfo("Information", "Cette personne n'a aucun cours de programmé")
                fenetre.destroy()
                self.choisir_donnee_edt(typ)
            else:
                liste_jour = []
                liste_heure = []
                liste_heure_str = []
                liste_horaire = self.connecteur.voir_horaire()
                for i in range(len(liste_horaire)):
                    if liste_horaire[i][2] not in liste_jour:
                        liste_jour.append(liste_horaire[i][2])
                    if (liste_horaire[i][0], liste_horaire[i][1]) not in liste_heure:
                        liste_heure.append((liste_horaire[i][0], liste_horaire[i][1]))
                        liste_heure_str.append(str(liste_horaire[i][0]) + "-" + str(liste_horaire[i][1]))
                for i in range(len(liste_jour)):
                    liste_matiere.append({liste_jour[i]: []})
                    for j in range(len(liste_heure)):
                        liste_matiere[i][liste_jour[i]].append({str(liste_heure[j][0]) + "-" + str(liste_heure[j][1]): []})
                for i in range(len(liste_cours)):
                    if typ == "eleve":
                        prof = self.connecteur.voir_prof_id(liste_cours[i][0])
                        matiere = self.connecteur.voir_matiere_id(liste_cours[i][1])
                        salle = self.connecteur.voir_salle_id(liste_cours[i][3])
                        horaire = self.connecteur.voir_horaire_id(liste_cours[i][4])
                    if typ == "prof":
                        horaire = self.connecteur.voir_horaire_id(liste_cours[i][4])
                        classe = self.connecteur.voir_classe_id(liste_cours[i][2])
                        salle = self.connecteur.voir_salle_id(liste_cours[i][3])
                    for j in range(len(liste_jour)):
                        if liste_jour[j] == horaire[2]:
                            jour = horaire[2]
                            _jour = j
                    for j in range(len(liste_heure)):
                        if liste_heure[j][0] == horaire[0] and liste_heure[j][1] == horaire[1]:
                            heure = str(horaire[0]) + "-" + str(horaire[1])
                            _heure = j
                    if typ == "eleve":
                        liste_matiere[_jour][jour][_heure][heure].append(matiere)
                        liste_matiere[_jour][jour][_heure][heure].append(prof)
                        liste_matiere[_jour][jour][_heure][heure].append(salle)
                    else:
                        liste_matiere[_jour][jour][_heure][heure].append(classe)
                        liste_matiere[_jour][jour][_heure][heure].append(salle)
                edt = ExportEDT("Geosanslight.ttf")
                edt.inserer_liste_matiere((2000, 1000), liste_jour, liste_heure_str, liste_matiere)
                if choix == "2":
                    edt.save(chemin)
                else:
                    edt.show()

    def __ajouter_info__(self, nombre_input, texte_input, typ, *modifier):
        milieu = (self.largeur/2-self.largeur/100)/2
        fenetre = tkinter.Tk()
        #fenetre.attributes("-zoomed", True)
        fenetre.wm_state("zoomed")

        if modifier:
            label = Label(fenetre, text="Veuillez indiquer les nouvelles valeurs dans les champs", font = ("Time", 20, "bold"))
        else:
            label = Label(fenetre, text="Veuillez indiquer les valeurs dans les champs", font = ("Time", 20, "bold"))
        label.place(height = self.hauteur / 2.5, width = self.largeur)

        texte = Label(text = "NotePro", font = ("Time", 40), bg = "purple")
        texte.place(height = self.hauteur // 6, width = self.largeur)

        def ajouter(nombre_input):
            if nombre_input >= 5:
                e = entree5.get()
            if nombre_input >= 4:
                d = entree4.get()
            if nombre_input >= 3:
                c = entree3.get()
            if nombre_input >= 2:
                b = entree2.get()
            a = entree.get()

            if typ == "eleve":
                self.connecteur.add_eleve(a, b, c, e, d)
            if typ == "professeur":
                self.connecteur.add_prof(a, b, c)
            if typ == "cours":
                self.connecteur.add_cours(a, b, c, d, e, 105)
            if typ == "horaire":
                self.connecteur.add_horaire(a, b, c, d, True)
            if typ == "salle":
                self.connecteur.add_salle(a, b, c, d)
            if typ == "matiere":
                self.connecteur.add_matiere(a, b)
            if typ == "profmatiere":
                self.connecteur.add_matiere_prof(a, b)
            if typ == "classe":
                self.connecteur.add_classe(a, b, c)

        """def _self.__modifier_info__(modifier):
            if typ == "eleve":
                insertion = "INSERT INTO Eleve(idEleve, nom, prenom, classe, dateNaissance) "
                insertion += "VALUES (?, ?, ?, ?, ?);"""

        _nombre_input = nombre_input
        if modifier:
            if _nombre_input == 1:
                bouton = Button(fenetre, text="Modifier dans la base de données", command = lambda:[self.__modifier_info_get_info(fenetre, modifier, [entree], typ)])
            if _nombre_input == 2:
                bouton = Button(fenetre, text="Modifier dans la base de données", command = lambda:[self.__modifier_info_get_info(fenetre, modifier, [entree, entree2], typ)])
            if _nombre_input == 3:
                bouton = Button(fenetre, text="Modifier dans la base de données", command = lambda:[self.__modifier_info_get_info(fenetre, modifier, [entree, entree2, entree3], typ)])
            if _nombre_input == 4:
                bouton = Button(fenetre, text="Modifier dans la base de données", command = lambda:[self.__modifier_info_get_info(fenetre, modifier, [entree, entree2, entree3, entree4], typ)])
            if _nombre_input == 5:
                bouton = Button(fenetre, text="Modifier dans la base de données", command = lambda:[self.__modifier_info_get_info(fenetre, modifier, [entree, entree2, entree3, entree4, entree5], typ)])
        else:
            bouton = Button(fenetre, text="Ajouter dans la base de données", command = lambda:[ajouter(_nombre_input), fenetre.destroy(), self.__ajouter_info__(nombre_input, texte_input, typ)])
        bouton.place(x = 0, y = self.hauteur / 4, height = self.hauteur/7, width = self.largeur/2)

        if modifier:
            bouton = Button(fenetre, text="Retour", command = lambda:[fenetre.destroy(), self.__modifier_des_donnees__()])
        else:
            bouton = Button(fenetre, text="Retour", command = lambda:[fenetre.destroy(), self.__ajouter_des_donnees__()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 4, height = self.hauteur/7, width = self.largeur/2)

        if type(texte_input[0]) == list:
            entree = ttk.Combobox(fenetre, values=texte_input[0][1::])
        else:
            entree = Entry(fenetre)
            entree.insert(0, "Veuillez saisir " + texte_input[0])
        if nombre_input == 1:
                    entree.place(y = self.hauteur / 1.2, width=self.largeur/2-self.largeur/100, x = milieu)
        else:
                    entree.place(y = self.hauteur / 1.2, width=self.largeur/2-self.largeur/100)

        if nombre_input >= 2:
            if type(texte_input[1]) == list:
                entree2 = ttk.Combobox(fenetre, values=texte_input[1][1::])
            else:
                entree2 = Entry(fenetre)
                entree2.insert(0, "Veuillez saisir " + texte_input[1])
            entree2.place(y = self.hauteur / 1.2, x = self.largeur/2, width=self.largeur/2-self.largeur/100)

        if nombre_input >= 3:
            if type(texte_input[2]) == list:
                entree3 = ttk.Combobox(fenetre, values=texte_input[2][1::])
            else:
                entree3 = Entry(fenetre)
                entree3.insert(0, "Veuillez saisir " + texte_input[2])
            if nombre_input == 3:
                    entree3.place(y = self.hauteur / 1.4, width=self.largeur/2-self.largeur/100, x = milieu)
            else:
                    entree3.place(y = self.hauteur / 1.4, width=self.largeur/2-self.largeur/100)

        if nombre_input >= 4:
            if type(texte_input[3]) == list:
                entree4 = ttk.Combobox(fenetre, values=texte_input[3][1::])
            else:
                entree4 = Entry(fenetre)
                entree4.insert(0, "Veuillez saisir " + texte_input[3])
            entree4.place(y = self.hauteur / 1.4, x = self.largeur/2, width=self.largeur/2-self.largeur/100)

        if nombre_input >= 5:
            if type(texte_input[4]) == list:
                entree5 = ttk.Combobox(fenetre, values=texte_input[4][1::])
            else:
                entree5 = Entry(fenetre)
                entree5.insert(0, "Veuillez saisir " + texte_input[4])
            if nombre_input == 5:
                entree5.place(y = self.hauteur / 1.6, width=self.largeur/2-self.largeur/100, x = milieu)
            else:
                entree5.place(y = self.hauteur / 1.6, width=self.largeur/2-self.largeur/100)

        def clear_search(event):
            if type(texte_input[0]) == list:
                if entree.get() == "Veuillez saisir " + texte_input[0][0]:
                    entree.delete(0, END)
            else:
                if entree.get() == "Veuillez saisir " + str(texte_input[0]):
                    entree.delete(0, END)

        def insert_search(event):
            if entree.get() == "":
                if type(texte_input[0]) == list:
                    entree.insert(0, "Veuillez saisir " + texte_input[0][0])
                else:
                    entree.insert(0, "Veuillez saisir " + texte_input[0])

        def clear_search2(event):
            if type(texte_input[0]) == list:
                if entree2.get() == "Veuillez saisir " + texte_input[1][0]:
                    entree2.delete(0, END)
            else:
                if entree2.get() == "Veuillez saisir " + str(texte_input[1]):
                    entree2.delete(0, END)

        def insert_search2(event):
            if entree2.get() == "":
                if type(texte_input[1]) == list:
                    entree2.insert(0, "Veuillez saisir " + texte_input[1][0])
                else:
                    entree2.insert(0, "Veuillez saisir " + texte_input[1])

        def clear_search3(event):
            if type(texte_input[2]) == list:
                if entree3.get() == "Veuillez saisir " + texte_input[2][0]:
                    entree3.delete(0, END)
            else:
                if entree3.get() == "Veuillez saisir " + str(texte_input[2]):
                    entree3.delete(0, END)

        def insert_search3(event):
            if entree3.get() == "":
                if type(texte_input[2]) == list:
                    entree3.insert(0, "Veuillez saisir " + texte_input[2][0])
                else:
                    entree3.insert(0, "Veuillez saisir " + texte_input[2])

        def clear_search4(event):
            if type(texte_input[3]) == list:
                if entree4.get() == "Veuillez saisir " + texte_input[3][0]:
                    entree4.delete(0, END)
            else:
                if entree4.get() == "Veuillez saisir " + str(texte_input[3]):
                    entree4.delete(0, END)

        def insert_search4(event):
            if entree4.get() == "":
                if type(texte_input[3]) == list:
                    entree4.insert(0, "Veuillez saisir " + texte_input[3][0])
                else:
                    entree4.insert(0, "Veuillez saisir " + texte_input[3])

        def clear_search5(event):
            if type(texte_input[4]) == list:
                if entree5.get() == "Veuillez saisir " + texte_input[4][0]:
                    entree5.delete(0, END)
            else:
                if entree5.get() == "Veuillez saisir " + str(texte_input[4]):
                    entree5.delete(0, END)

        def insert_search5(event):
            if entree5.get() == "":
                if type(texte_input[4]) == list:
                    entree5.insert(0, "Veuillez saisir " + texte_input[4][0])
                else:
                    entree5.insert(0, "Veuillez saisir " + texte_input[4])


        entree.bind("<Button-1>", clear_search)
        entree.bind("<FocusOut>", insert_search)

        if nombre_input >= 2:
            entree2.bind("<Button-1>", clear_search2)
            entree2.bind("<FocusOut>", insert_search2)

        if nombre_input >= 3:
            entree3.bind("<Button-1>", clear_search3)
            entree3.bind("<FocusOut>", insert_search3)

        if nombre_input >= 4:
            entree4.bind("<Button-1>", clear_search4)
            entree4.bind("<FocusOut>", insert_search4)

        if nombre_input >= 5:
            entree5.bind("<Button-1>", clear_search5)
            entree5.bind("<FocusOut>", insert_search5)

        fenetre.mainloop()

    def __modifier_info_get_info(self, fenetre, modifier, liste_entree, typ):
        liste_non_valide = ["Veuillez saisir le nouveau nom", "Veuillez saisir le nouveau prenom",\
                            "Veuillez saisir la nouvelle date de naissance",\
                            "Veuillez saisir la nouvelle classe", "",\
                            "Veuillez saisir le nouveau nom de la salle",\
                            "Veuillez saisir la nouvelle capacite de la salle",\
                            "Veuillez sasir la nouvelle id du professeur principal",\
                            "le nouveau debut de l'horaire", "la nouvelle fin de l'horaire",\
                            "le nouveau jour de l'horaire", "Veuillez saisir la nouvelle classe"]
        if typ == "eleve":
            a = liste_entree[0].get()
            b = liste_entree[1].get()
            c = liste_entree[2].get()
            d = liste_entree[3].get()
            if a not in liste_non_valide:
                self.connecteur.modifier_info_eleve__("prenom", a, modifier[0])
            if b not in liste_non_valide:
                self.connecteur.modifier_info_eleve__("nom", b, modifier[0])
            if c not in liste_non_valide:
                self.connecteur.modifier_info_eleve__("classe", c, modifier[0])
            if d not in liste_non_valide:
                self.connecteur.modifier_info_eleve__("dateNaissance", d, modifier[0])
        if typ == "professeur":
            a = liste_entree[0].get()
            b = liste_entree[1].get()
            if a not in liste_non_valide:
                self.connecteur.modifier_info_professeur__("prenom", a, modifier[0])
            if b not in liste_non_valide:
                self.connecteur.modifier_info_professeur__("nom", b, modifier[0])
        if typ == "salle":
            a = liste_entree[0].get()
            b = liste_entree[1].get()
            c = liste_entree[2].get()
            if a not in liste_non_valide:
                self.connecteur.modifier_info_salle__("nom", a, modifier[0])
            if b not in liste_non_valide:
                self.connecteur.modifier_info_salle__("capacite", b, modifier[0])
            if b not in liste_non_valide:
                self.connecteur.modifier_info_salle__("type", c, modifier[0])
        if typ == "classe":
            a = liste_entree[0].get()
            b = liste_entree[1].get()
            if a not in liste_non_valide:
                self.connecteur.modifier_info_classe__("nom", a, modifier[0])
            if b not in liste_non_valide:
                self.connecteur.modifier_info_classe__("idProf", b, modifier[0])
        if typ == "matiere":
            a = liste_entree[0].get()
            if a not in liste_non_valide:
                self.connecteur.modifier_info_matiere__("nom", a, modifier[0])
        if typ == "horaire":
            a = liste_entree[0].get()
            b = liste_entree[1].get()
            c = liste_entree[2].get()
            if a not in liste_non_valide:
                self.connecteur.modifier_info_horaire__("debut", a, modifier[0])
            if b not in liste_non_valide:
                self.connecteur.modifier_info_horaire__("fin", b, modifier[0])
            if b not in liste_non_valide:
                self.connecteur.modifier_info_horaire__("jour", c, modifier[0])
        """if typ == "cours":
            fenetre.destroy()"""
        fenetre.destroy()
        self.activer_fenetre()

    def __modifier_info__(self, typ):


        def verification(label, liste_donnee, current):
            valeur = label.get()
            if valeur != "Choisissez la donnée à modifier":
                if typ == "eleve":
                    donnee_actuelles = self.connecteur.voir_info_eleve()[current-1]
                if typ == "professeur":
                    donnee_actuelles = self.connecteur.voir_info_professeur()[current-1]
                if typ == "salle":
                    donnee_actuelles = self.connecteur.voir_info_salle()[current-1]
                if typ == "classe":
                    donnee_actuelles = self.connecteur.voir_info_classe()[current-1]
                if typ == "matiere":
                    donnee_actuelles = self.connecteur.voir_info_matiere()[current-1]
                if typ == "horaire":
                    donnee_actuelles = self.connecteur.voir_info_horaire()[current-1]
                modification(typ, donnee_actuelles[0])
            else:
                fenetre.destroy()
                self.__modifier_info__(typ)

        milieu = (self.largeur/2-self.largeur/100)/2
        fenetre = tkinter.Tk()
        #fenetre.attributes("-zoomed", True)
        fenetre.wm_state("zoomed")

        texte = Label(text = "NotePro", font = ("Time", 40), bg = "purple")
        texte.place(height = self.hauteur // 6, width = self.largeur)

        bouton = Button(fenetre, text="Modifier cette donnée", command = lambda:[verification(entree, liste_donnee, entree.current())])
        bouton.place(x = 0, y = self.hauteur / 4, height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Retour", command = lambda:[fenetre.destroy(), self.activer_fenetre()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 4, height = self.hauteur/7, width = self.largeur/2)

        #entree = ttk.Combobox(fenetre, values=texte_input[3][get_liste_eleve()])
        #On apellera plus tard  la fonction get_liste_?????()
        #En attendant je simule la fonction
        #liste = ["100 Claire Rey 1 2005-07-08", "101, 'Emmanuel', 'Lebrun', '1', '2005-06-14'", "102, 'Maurice', 'Bertin', '1', '2005-06-18'"]
        #liste = [(100, 'Claire Rey', 1, '2005-07-08'), (101, 'Emmanuel', 'Lebrun', '1', '2005-06-14'), (102, 'Maurice', 'Bertin', '1', '2005-06-18')]
        #connexion = EmploiDuTemps("E:/Documents/Théo/Terminale/NSI/A rendre/Emploi du temps/base_test.db")
        #liste = connexion.voir_liste_eleve()
        if typ == "eleve":
            liste = self.connecteur.voir_eleve()
        if typ == "professeur":
            liste = self.connecteur.voir_prof()
        if typ == "matiere":
            liste = self.connecteur.voir_matiere()
        if typ == "horaire":
            liste = self.connecteur.voir_horaire()
        if typ == "salle":
            liste = self.connecteur.voir_salle()
        if typ == "classe":
            liste = self.connecteur.voir_classe()
        if typ == "heure":
            liste = self.connecteur.voir_horaire()

        remplacement = str(liste)
        """remplacement = remplacement.replace("'), (", "\", \"")
        remplacement = remplacement.replace(", '", " ")
        remplacement = remplacement.replace("', ", " ")
        remplacement = remplacement.replace("' ", " ")
        remplacement = remplacement.replace("'", "\"")
        remplacement = remplacement.replace("[(", "")
        remplacement = remplacement.replace(")]", "")
        remplacement = remplacement[0:-1].split("\", \"")"""
        liste_donnee = ["Choisissez la donnée à modifier"]
        for i in range(len(liste)):
            t = ""
            for j in range(len(liste[i])):
                t += str(liste[i][j]) + " "
            liste_donnee.append(t)
        entree = ttk.Combobox(fenetre, values=liste_donnee)
        entree.current(0)
        entree.place(y = self.hauteur / 4 + self.hauteur / 100 + self.hauteur / 7, x = milieu, width=self.largeur/2-self.largeur/100)

        #info = test.get_info_eleve()

        def modification(typ, donnee_actuelles):
            if typ == "professeur":
                fenetre.destroy()
                self.__ajouter_info__(2, ["le nouveau prenom", "le nouveau nom"], "professeur", donnee_actuelles)
            if typ == "eleve":
                liste_classe = self.connecteur.voir_classe()
                liste_donnee_classe = ["la nouvelle classe"]
                for i in range(len(liste_classe)):
                    t = ""
                    for j in range(len(liste_classe[i])):
                        t += str(liste_classe[i][j]) + " "
                    liste_donnee_classe.append(t)
                fenetre.destroy()
                self.__ajouter_info__(4, ["le nouveau nom", "le nouveau prenom", liste_donnee_classe, "la nouvelle date de naissance"], "eleve", donnee_actuelles)
            if typ == "salle":
                fenetre.destroy()
                self.__ajouter_info__(3, ["le nouveau nom de la salle", "la nouvelle capacite de la salle", ["le type de salle", "normal", "labo", "ordis"]], "salle", donnee_actuelles)
            if typ == "classe":
                liste_professeur = self.connecteur.voir_prof()
                liste_donnee_prof = ["le nouveau professeur"]
                for i in range(len(liste_professeur)):
                    t = ""
                    for j in range(len(liste_professeur[i])):
                        t += str(liste_professeur[i][j]) + " "
                    liste_donnee_prof.append(t)
                self.__ajouter_info__(2, ["le nouveau nom", liste_donnee_prof], "classe", donnee_actuelles)
            if typ == "heure":
                fenetre.destroy()
                self.__ajouter_info__(5, ["la nouvelle id du professeur", "la nouvelle id de la matiere", "la nouvelle id de la classe", "la nouvelle id de la salle", "la nouvelle id de l'horaire"], "heure", donnee_actuelles)
            if typ == "matiere":
                fenetre.destroy()
                self.__ajouter_info__(1, ["le nouveau nom"], "matiere", donnee_actuelles)
            if typ == "horaire":
                fenetre.destroy()
                self.__ajouter_info__(3, ["le nouveau debut de l'horaire", "la nouvelle fin de l'horaire", "le nouveau jour de l'horaire"], "horaire", donnee_actuelles)
            """if typ == "profmatiere":
                fenetre.destroy()
                self.__ajouter_info__(self, 4, ["le nouveau prenom", "le nouveau nom", "la nouvelle date de naissance", "la nouvelle classe"], test, True)"""

    def __supprimer_info__(self, typ):
        fenetre = tkinter.Tk()
        #fenetre.attributes("-zoomed", True)
        fenetre.wm_state("zoomed")
        milieu = (self.largeur/2-self.largeur/100)/2

        def validation(fenetre, typ, current):
            if current != 0:
                reponse = askyesno("Message", "Voulez-vous vraiment supprimer definitivement cette donnee ?")
                if reponse:
                    if typ == "eleve":
                        liste = self.connecteur.voir_info_eleve()[current-1]
                        self.connecteur.supprimer_eleve(liste[0])
                    if typ == "prof":
                        liste = self.connecteur.voir_info_professeur()[current-1]
                        self.connecteur.supprimer_professeur(liste[0])
                    if typ == "matiere":
                        liste = self.connecteur.voir_info_matiere()[current-1]
                        self.connecteur.supprimer_matiere(liste[0])
                    if typ == "horaire":
                        liste = self.connecteur.voir_info_horaire()[current-1]
                        self.connecteur.supprimer_horaire(liste[0])
                    if typ == "salle":
                        liste = self.connecteur.voir_info_salle()[current-1]
                        self.connecteur.supprimer_salle(liste[0])
                    if typ == "classe":
                        liste = self.connecteur.voir_info_classe()[current-1]
                        self.connecteur.supprimer_classe(liste[0])
                    if typ == "cours":
                        liste = self.connecteur.voir_cours()[current-1]
                        self.connecteur.supprimer_cours(liste[0], liste[1], liste[2], liste[3], liste[4])
                    if typ == "profmatiere":
                        liste = self.connecteur.voir_info_matiere_prof()[current-1]
                        self.connecteur.supprimer_matiere_professeur(liste[0], liste[1])
                fenetre.destroy()
                self.__supprimer_info__(typ)

        texte = Label(text = "NotePro", font = ("Time", 40), bg = "purple")
        texte.place(height = self.hauteur // 6, width = self.largeur)

        bouton = Button(fenetre, text="Supprimer cette donnée", command = lambda:[validation(fenetre, typ, entree.current())])
        bouton.place(x = 0, y = self.hauteur / 4, height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Retour", command = lambda:[fenetre.destroy(), self.__supprimer_des_donnees__()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 4, height = self.hauteur/7, width = self.largeur/2)

        if typ == "eleve":
            liste = self.connecteur.voir_eleve()
        if typ == "prof":
            liste = self.connecteur.voir_prof()
        if typ == "matiere":
            liste = self.connecteur.voir_matiere()
        if typ == "horaire":
            liste = self.connecteur.voir_horaire()
        if typ == "salle":
            liste = self.connecteur.voir_salle()
        if typ == "classe":
            liste = self.connecteur.voir_classe()
        if typ == "cours":
            liste = self.connecteur.voir_cours()
        if typ == "profmatiere":
            liste = self.connecteur.voir_matiere_prof()

        liste_donnee = ["Choisissez la donnée à supprimer"]
        for i in range(len(liste)):
            t = ""
            for j in range(len(liste[i])):
                t += str(liste[i][j]) + " "
            liste_donnee.append(t)
        entree = ttk.Combobox(fenetre, values=liste_donnee)
        entree.current(0)
        entree.place(y = self.hauteur / 4 + self.hauteur / 100 + self.hauteur / 7, x = milieu, width=self.largeur/2-self.largeur/100)

        fenetre.mainloop()


    def __ajouter_des_donnees__(self):
        fenetre = tkinter.Tk()
        #fenetre.attributes("-zoomed", True)
        fenetre.wm_state("zoomed")

        label = Label(fenetre, text="Veuillez sélectionner votre action à réaliser", font = ("Time", 20, "bold"))
        label.place(height = self.hauteur / 2.5, width = self.largeur)

        texte = Label(width = self.largeur, text = "NotePro", font = ("Time", 40), bg = "purple")
        texte.place(height = self.hauteur // 6, width = self.largeur)

        liste_classe = self.connecteur.voir_classe()
        liste_donnee_classe = ["la classe"]
        for i in range(len(liste_classe)):
            t = ""
            for j in range(len(liste_classe[i])):
                t += str(liste_classe[i][j]) + " "
            liste_donnee_classe.append(t)
        bouton = Button(fenetre, text="Ajouter un eleve", command = lambda:[fenetre.destroy(), self.__ajouter_info__(5, ["l'id de l'eleve", "le prenom", "le nom", "la date de naissance", liste_donnee_classe], "eleve")])
        bouton.place(x = 0, y = self.hauteur / 2 - 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Ajouter une salle", command = lambda:[fenetre.destroy(), self.__ajouter_info__(4, ["l'id de la salle", "le nom de de la salle", "la capacite de la salle", ["le type de salle", "normal", "labo", "ordis"]], "salle")])
        bouton.place(x = 0, y = self.hauteur / 2 - (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        liste_professeur = self.connecteur.voir_prof()
        liste_donnee_prof = ["le professeur"]
        for i in range(len(liste_professeur)):
            t = ""
            for j in range(len(liste_professeur[i])):
                t += str(liste_professeur[i][j]) + " "
            liste_donnee_prof.append(t)
        bouton = Button(fenetre, text="Ajouter une classe", command = lambda:[fenetre.destroy(), self.__ajouter_info__(3, ["l'id de la classe", "le nom", liste_donnee_prof], "classe")])
        bouton.place(x = 0, y = self.hauteur / 2, height = self.hauteur/7, width = self.largeur/2)

        liste_matiere = self.connecteur.voir_matiere()
        liste_donnee_matiere = ["la matiere"]
        for i in range(len(liste_matiere)):
            t = ""
            for j in range(len(liste_matiere[i])):
                t += str(liste_matiere[i][j]) + " "
            liste_donnee_matiere.append(t)
        bouton = Button(fenetre, text="Ajouter un professeur lié une matiere", command = lambda:[fenetre.destroy(), self.__ajouter_info__(2, [liste_donnee_prof, liste_donnee_matiere], "profmatiere")])
        bouton.place(x = 0, y = self.hauteur / 2 + (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Retour", command = lambda:[fenetre.destroy(), self.activer_fenetre()])
        bouton.place(x = 0, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Ajouter un professeur", command = lambda:[fenetre.destroy(), self.__ajouter_info__(3, ["l'id du professeur", "le nom", "le prenom"], "professeur")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 - 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        liste_salle = self.connecteur.voir_salle()
        liste_donnee_salle = ["la salle"]
        for i in range(len(liste_salle)):
            t = ""
            for j in range(len(liste_salle[i])):
                t += str(liste_salle[i][j]) + " "
            liste_donnee_salle.append(t)

        liste_horaire = self.connecteur.voir_horaire()
        liste_donnee_horaire = ["l'horaire"]
        for i in range(len(liste_horaire)):
            t = ""
            for j in range(len(liste_horaire[i])):
                t += str(liste_horaire[i][j]) + " "
            liste_donnee_horaire.append(t)
        bouton = Button(fenetre, text="Ajouter une heure de cours", command = lambda:[fenetre.destroy(), self.__ajouter_info__(5, [liste_donnee_prof, liste_donnee_matiere, liste_donnee_classe, liste_donnee_salle, liste_donnee_horaire], "cours")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 - (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Ajouter une matière", command = lambda:[fenetre.destroy(), self.__ajouter_info__(2, ["l'id de la matiere", "le nom"], "matiere")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2, height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Ajouter une horaire", command = lambda:[fenetre.destroy(), self.__ajouter_info__(4, ["l'id de l'horaire", "le debut de l'horaire", "la fin de l'horaire", "le jour de l'horaire"], "horaire")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Quitter", command = lambda:[fenetre.destroy()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        fenetre.mainloop()


    def __modifier_des_donnees__(self):
        fenetre = tkinter.Tk()
        #fenetre.attributes("-zoomed", True)
        fenetre.wm_state("zoomed")

        label = Label(fenetre, text="Veuillez sélectionner votre action à réaliser", font = ("Time", 20, "bold"))
        label.place(height = self.hauteur / 2.5, width = self.largeur)

        texte = Label(width = self.largeur, text = "NotePro", font = ("Time", 40), bg = "purple")
        texte.place(height = self.hauteur // 6, width = self.largeur)

        bouton = Button(fenetre, text="Modifier un eleve", command = lambda:[fenetre.destroy(), self.__modifier_info__("eleve")])
        bouton.place(x = (self.largeur/2-self.largeur/100)/2, y = self.hauteur / 2 - 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Modifier une salle", command = lambda:[fenetre.destroy(), self.__modifier_info__("salle")])
        bouton.place(x = 0, y = self.hauteur / 2 - (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Modifier une classe", command = lambda:[fenetre.destroy(), self.__modifier_info__("classe")])
        bouton.place(x = 0, y = self.hauteur / 2, height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Retour", command = lambda:[fenetre.destroy(), self.activer_fenetre()])
        bouton.place(x = 0, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Modifier un professeur", command = lambda:[fenetre.destroy(), self.__modifier_info__("professeur")])
        bouton.place(x = 0, y = self.hauteur / 2 + (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Modifier une heure de cours", command = lambda:[fenetre.destroy(), self.__modifier_info__("heure")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 - (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Modifier une matière", command = lambda:[fenetre.destroy(), self.__modifier_info__("matiere")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2, height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Modifier une horaire", command = lambda:[fenetre.destroy(), self.__modifier_info__("horaire")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Quitter", command = lambda:[fenetre.destroy()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        fenetre.mainloop()

    def __supprimer_des_donnees__(self):

        fenetre = tkinter.Tk()
        #fenetre.attributes("-zoomed", True)
        fenetre.wm_state("zoomed")

        label = Label(fenetre, text="Veuillez sélectionner votre action à réaliser", font = ("Time", 20, "bold"))
        label.place(height = self.hauteur / 2.5, width = self.largeur)

        texte = Label(width = self.largeur, text = "NotePro", font = ("Time", 40), bg = "purple")
        texte.place(height = self.hauteur // 6, width = self.largeur)

        bouton = Button(fenetre, text="Supprimer un eleve", command = lambda:[fenetre.destroy(), self.__supprimer_info__("eleve")])
        bouton.place(x = 0, y = self.hauteur / 2 - 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Supprimer une salle", command = lambda:[fenetre.destroy(), self.__supprimer_info__("salle")])
        bouton.place(x = 0, y = self.hauteur / 2 - (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Supprimer une classe", command = lambda:[fenetre.destroy(), self.__supprimer_info__("classe")])
        bouton.place(x = 0, y = self.hauteur / 2, height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Supprimer un professeur lié une matiere", command = lambda:[fenetre.destroy(), self.__supprimer_info__("profmatiere")])
        bouton.place(x = 0, y = self.hauteur / 2 + (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Retour", command = lambda:[fenetre.destroy(), self.activer_fenetre()])
        bouton.place(x = 0, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Supprimer un professeur", command = lambda:[fenetre.destroy(), self.__supprimer_info__("prof")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 - 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Supprimer une heure de cours", command = lambda:[fenetre.destroy(), self.__supprimer_info__("cours")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 - (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Supprimer une matière", command = lambda:[fenetre.destroy(), self.__supprimer_info__("matiere")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2, height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Supprimer une horaire", command = lambda:[fenetre.destroy(), self.__supprimer_info__("horaire")])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Quitter", command = lambda:[fenetre.destroy()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        fenetre.mainloop()

    def __afficher_donnee__(self):

        fenetre = tkinter.Tk()
        #fenetre.attributes("-zoomed", True)
        fenetre.wm_state("zoomed")
        milieu = (self.largeur/2-self.largeur/100)/2

        label = Label(fenetre, text="Veuillez sélectionner votre action à réaliser", font = ("Time", 20, "bold"))
        label.place(height = self.hauteur / 2.5, width = self.largeur)

        texte = Label(width = self.largeur, text = "NotePro", font = ("Time", 40), bg = "purple")
        texte.place(height = self.hauteur // 6, width = self.largeur)

        entree = ttk.Combobox(fenetre, values= ["choisir...", "voir toutes les infos des élèves", "voir nom et prénom de l'élève",
                                                "voir les professeurs et leurs matières", "voir les maiètes", "voir toute les classes",
                                                "voir les noms et prénoms des professeurs", "voir les salles",
                                                "voir les horaires", "voir les cours", "voir les information des classes",
                                                "voir information des salles", "voir information des horaires",
                                                "voir les information des matières", "voir les informations des matières des profs"])
        entree.current(0)
        entree.place(x = milieu, y = self.hauteur / 3, width = self.largeur/2)
        a = entree.current()

        bouton = Button(fenetre, text="Afficher HTML", command = lambda:[self.liste_html(entree.current())])
        bouton.place(x = milieu, y = self.hauteur / 2, height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Retour", command = lambda:[fenetre.destroy(), self.activer_fenetre()])
        bouton.place(x = 0, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Quitter", command = lambda:[fenetre.destroy()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        fenetre.mainloop()

    def activer_fenetre(self):
        """Methode qui genere l'interface graphique

        Args:
            self.connecteur (EmploiDuTemps): La variable de la classe EmploiDUTemps
        """
        fenetre = tkinter.Tk()
        #fenetre.attributes("-zoomed", True)
        fenetre.wm_state("zoomed")
        self.largeur, self.hauteur = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()

        label = Label(fenetre, text="Bienvenue dans l'écran d'accueil. Veuillez sélectionner votre action à réaliser", font = ("Time", 20, "bold"))
        label.place(height = self.hauteur / 2.5, width = self.largeur)

        texte = Label(width = self.largeur, text = "NotePro", font = ("Time", 40), bg = "purple")
        texte.place(height = self.hauteur // 6, width = self.largeur)

        bouton = Button(fenetre, text="Ajouter des données", command = lambda:[fenetre.destroy(), self.__ajouter_des_donnees__()])
        bouton.place(x = 0, y = self.hauteur / 2, height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Supprimer des données", command = lambda:[fenetre.destroy(), self.__supprimer_des_donnees__()])
        bouton.place(x = 0, y = self.hauteur / 2 + (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Voir les données", command = lambda:[fenetre.destroy(), self.__afficher_donnee__()])
        bouton.place(x = 0, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Modifier les données", command = lambda:[fenetre.destroy(), self.__modifier_des_donnees__()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2, height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Voir l'emploi du temps", command = lambda:[fenetre.destroy(), self.bouton_pdf()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + (self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        bouton = Button(fenetre, text="Quitter", command = lambda:[fenetre.destroy()])
        bouton.place(x = self.largeur / 2, y = self.hauteur / 2 + 2*(self.hauteur/7), height = self.hauteur/7, width = self.largeur/2)

        fenetre.mainloop()

    def __creation_html__(self, liste):
        debut_html = "<html>"
        fin_html = "</html>"
        head = """ <head>
                        <title>Emploi du temps</title>
                        <meta charset="UTF-8">
                        <link rel="stylesheet" href="rendu%20HTML.css">
                    </head>"""
        debut_body = '''  <body>
                            <header>
                                <h1>Voir les donnees</h1>
                                <h2>taille de la liste : ''' + str(len(liste)) + '''</h2>
                            </header>
                            <section>
                                <h3>Liste :</h3>
                                    <ul>'''
        li = ""
        #print(type(liste))
        #a = liste.voir_info_eleve()
        for i in range (len(liste)):
            li += '<li>' + str(liste[i]) + "</li>"

        fin_body = '''      </ul>
                        </section>
                    </body>
                    '''
        return debut_html + head + debut_body + li + fin_body + fin_html

    def liste_html(self, typ):
        """Methode qui genere la liste des donnees selectionnees dans une page html.
        Cette page est automatiquement genere lors de l'utilisation de l'option "Voir les donnees"

        Args:
            self.connecteur_base (EmploiDuTemps): La variable de la classe EmploiDUTemps
        """
        __sauvegarder_html__(self.connecteur, self, typ)

def __sauvegarder_html__(connecteur_base, connecteur_tkinter, typ):
    with open("liste_html.html", "w") as fh:
        #fh.write(test.creation_html(test.voir_info_eleve()))
        if typ == 0:
            connecteur_tkinter
            connecteur_tkinter.__afficher_donnee__()
        if typ == 1:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_info_eleve()))
            os.startfile("liste_html.html")

        if typ == 2:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_eleve()))
            os.startfile("liste_html.html")
        if typ == 3:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_matiere_prof()))
            os.startfile("liste_html.html")

        if typ == 4:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_matiere()))
            os.startfile("liste_html.html")

        if typ == 5:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_classe()))
            os.startfile("liste_html.html")

        if typ == 6:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_prof()))
            os.startfile("liste_html.html")

        if typ == 7:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_salle()))
            os.startfile("liste_html.html")

        if typ == 8:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_horaire()))
            os.startfile("liste_html.html")

        if typ == 9:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_cours()))
            os.startfile("liste_html.html")

        if typ == 10:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_info_classe()))
            os.startfile("liste_html.html")

        if typ == 11:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_info_salle()))
            os.startfile("liste_html.html")

        if typ == 12:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_info_horaire()))
            os.startfile("liste_html.html")

        if typ == 13:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_info_matiere()))
            os.startfile("liste_html.html")

        if typ == 14:
            fh.write(connecteur_tkinter.__creation_html__(connecteur_base.voir_info_matiere_prof()))
            os.startfile("liste_html.html")




b = EmploiDuTemps("simulation.sqlite")
#__ajout__(b)
a = InterfaceGraphique(b)
#b.add_eleve(1, "a", "b", 1, 1)
a.liste_html("eleve")
a.activer_fenetre()
b.conn.close()
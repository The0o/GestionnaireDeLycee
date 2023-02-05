from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from colorsys import hsv_to_rgb
from copy import deepcopy

liste_jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
liste_heures = ["8H-9H", "9H-10H", "10H-11H", "11H-12H", "12H-13H", "13H-14H", "14H-15H", "15H-16H", "16H-17H", "17H-18H"]


taille = (2000, 1000)

class ExportEDT:

    def __init__(self, chemin_ecriture):
        self.chemin_ecriture = chemin_ecriture

    def inserer_liste_matiere(self, taille, listes_jours, liste_heures, liste_matiere):
        self.image = Image.new("RGBA", taille, "white")
        self.im = ImageDraw.Draw(self.image)
        self.liste_matiere = liste_matiere

        #tab et tab2 permet d'avoir un espace entre le debut de l'image et le debut du premier trait
        tab = taille[0] / 10
        tab2 = taille[1] / 10
        x_sans_tab = taille[0] - tab
        taille_un_jour = x_sans_tab / len(liste_jours)
        y_sans_tab = taille[1] - tab2
        taille_une_heure = y_sans_tab / len(liste_heures)
        #liste_bbox est
        liste_bbox = [[], []]

        for i in range(len(liste_jours)+1):
            self.im.line([2*(tab / 3) + i*taille_un_jour, 1*(tab2 / 3), 2*(tab / 3) + i*taille_un_jour, taille[1]-(tab2 / 3)], fill="black")
            liste_bbox[0].append((1*(tab2 / 3), 2*(tab / 3) + i*taille_un_jour, 2*(tab2 / 3), 2*(tab / 3) + (i+1)*taille_un_jour))

        liste_bbox[0].pop(len(liste_jours))

        for j in range(len(liste_heures)+1):
            self.im.line([1.2*(tab / 3), 2*(tab2 / 3) + j*taille_une_heure, taille[0]-(tab / 3), 2*(tab2 / 3) + j*taille_une_heure], fill="black")
            liste_bbox[1].append((1.2*(tab / 3), 2*(tab2 / 3) + j*taille_une_heure, 2*(tab / 3), 2*(tab2 / 3) + (j+1)*taille_une_heure))

        liste_bbox[1].pop(len(liste_heures))


        #taille = 0

        plus_grand_jour = [0, 0]
        #Indice 0 : L'indice du jour
        #Indice 1 : La taille en x du jour
        for i in range(len(liste_jours)):
            taille_ = self.im.textbbox((0, 0), liste_jours[i], font = ImageFont.truetype(self.chemin_ecriture, 5))[2]
            if taille_ > plus_grand_jour[1]:
                plus_grand_jour[1] = taille_
                plus_grand_jour[0] = i

        plus_grande_heure = [0, 0]
        #Indice 0 : L'indice de l'heure
        #Indice 1 : La taille en x de l'heure
        for i in range(len(liste_heures)):
            taille_ = self.im.textbbox((0, 0), liste_heures[i], font = ImageFont.truetype(self.chemin_ecriture, 5))[2]
            if taille_ > plus_grande_heure[1]:
                plus_grande_heure[1] = taille_
                plus_grande_heure[0] = i

        boucle = True
        j = 30
        k = 30
        while boucle:
            taille_texte = self.im.textbbox((0, 0), liste_jours[plus_grand_jour[0]], font = ImageFont.truetype(self.chemin_ecriture, j))
            if taille_texte[3] - taille_texte[1] <= liste_bbox[0][0][2] - liste_bbox[0][0][0] and \
            taille_texte[2] - taille_texte[0] <= liste_bbox[0][0][3] - liste_bbox[0][0][1]:
                boucle = False
            else:
                j -= 1

        boucle = True
        while boucle:
            taille_texte = self.im.textbbox((0, 0), liste_heures[plus_grande_heure[0]], font = ImageFont.truetype(self.chemin_ecriture, k))
            if taille_texte[2] - taille_texte[0] <= liste_bbox[1][0][2] - liste_bbox[1][0][0] and \
            taille_texte[3] - taille_texte[1] <= liste_bbox[1][0][3] - liste_bbox[1][0][1]:
                boucle = False
            else:
                k -= 1

        for i in range(len(liste_heures)):
            taille_texte = self.im.textbbox((0, 0), liste_heures[i], font = ImageFont.truetype(self.chemin_ecriture, k))
            x = ((liste_bbox[1][i][0] + liste_bbox[1][i][2]) - (taille_texte[0] + taille_texte[2])) / 2
            y = ((liste_bbox[1][i][1] + liste_bbox[1][i][3]) - (taille_texte[1] + taille_texte[3])) / 2
            self.im.text((x, y), liste_heures[i], font = ImageFont.truetype(self.chemin_ecriture, k), fill = "black")

        for i in range(len(liste_jours)):
            taille_texte = self.im.textbbox((0, 0), liste_jours[i], font = ImageFont.truetype(self.chemin_ecriture, j))
            x = ((liste_bbox[0][i][1] + liste_bbox[0][i][3]) - (taille_texte[0] + taille_texte[2])) / 2
            y = ((liste_bbox[0][i][0] + liste_bbox[0][i][2]) - (taille_texte[1] + taille_texte[3])) / 2
            self.im.text((x, y), liste_jours[i], font = ImageFont.truetype(self.chemin_ecriture, j), fill = "black")

        boucle = True
        o = 1
        while boucle:
            taille_ = self.im.textbbox([0, 0], "Laidin Théo TG2", font = ImageFont.truetype(self.chemin_ecriture, o), stroke_width = 1)
            if (taille_[2] - taille_[0]) < taille[0] and (taille_[3] - taille_[1]) < 0.8*(tab2 / 3):
                o += 1
            else:
                boucle = False

        if o > 31:
            o = 30
            taille_ = self.im.textbbox([0, 0], "Laidin Théo TG2", font = ImageFont.truetype(self.chemin_ecriture, 30), stroke_width = 1)

        self.im.text([(taille[0] - (taille_[2] - taille_[0]))/2, (0.8*(tab2/3) - (taille_[3] - taille_[1]))/2], "Laidin Théo TG2", font = ImageFont.truetype(self.chemin_ecriture, o), fill = "black", align = "center", stroke_width = 1)
        self.im.text([0, 0], "Lycee Jean Moulin", font = ImageFont.truetype(self.chemin_ecriture, o-5), fill = "black")

        k = 0
        couleur_edt = []
        taille_heure_de_cours = []
        couleur_edt_2 = []
        couleur_edt_3 = []
        couleur_edt_4 = []
        heure_apres = []
        liste_pas_de_texte = []
        double = False
        for i in range(len(liste_matiere)):
            heure_apres.append([[]])
            cle = list(liste_matiere[i].keys())[0]
            for j in range(len(liste_matiere[i][cle])):
                cle_heure = list(liste_matiere[i][cle][j].values())[0]
                heure_apres[i].append(list(liste_matiere[i][cle][j].values())[0])
                if cle_heure:
                    if cle_heure[0] not in couleur_edt:
                        couleur_edt.append(cle_heure[0])
                        if len(cle_heure) == 1:
                            couleur_edt_3.append([cle_heure[0]])
                            couleur_edt_4.append([cle_heure[0]])
                            taille_heure_de_cours.append(str(cle_heure[0]))
                        elif len(cle_heure) == 2:
                            couleur_edt_3.append([cle_heure[0], cle_heure[1]])
                            couleur_edt_4.append([cle_heure[0] + "\n" + cle_heure[1]])
                            taille_heure_de_cours.append(str(cle_heure[0]) + "\n" + str(cle_heure[1]))
                        else:
                            couleur_edt_3.append([cle_heure[0], cle_heure[1], cle_heure[2]])
                            couleur_edt_4.append([cle_heure[0] + "\n" + cle_heure[1] + "\n" + cle_heure[2]])
                            taille_heure_de_cours.append(str(cle_heure[0]))
        intervalle = 360 // len(couleur_edt)

        plus_grande_ecriture_matiere = [0, 0]
        for i in range(len(couleur_edt)):
            h, s, v = (k*intervalle)/360, 60/100, 60/100
            k += 1
            rgb = hsv_to_rgb(h, s, v)
            couleur = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
            couleur_edt_2.append({couleur_edt[i]: couleur})

            #Indice 0 : L'indice de l'heure
            #Indice 1 : La taille en x de l'heure
            for j in range(len(couleur_edt_3[i])):
                taille_ = self.im.textbbox((0, 0), couleur_edt_3[i][j], font = ImageFont.truetype(self.chemin_ecriture, 5))[2]
                if taille_ > plus_grande_ecriture_matiere[1]:
                    plus_grande_ecriture_matiere[1] = taille_
                    plus_grande_ecriture_matiere[0] = i
                    action = "normal"
        for i in range(len(liste_matiere)):
            cle = list(liste_matiere[i].keys())[0]
            for j in range(len(liste_matiere[i][cle])):
                cle_heure = list(liste_matiere[i][cle][j].values())[0]
                for l in range(len(couleur_edt_2)):
                    m = i*10 + j-4
                    if cle_heure == heure_apres[i][j]:
                        liste_pas_de_texte.append((i-1, j-1))
                    if cle_heure:
                        if cle_heure[0] == list(couleur_edt_2[l].keys())[0]:
                            cl = list(couleur_edt_2[l].values())[0]
                            if cle_heure[0:3] == heure_apres[i][j][0:3]:
                                action = "double"
                                double = True
                            if action == "normal":
                                self.im.rectangle([2*(tab/3)+ i*taille_un_jour, 2*(tab2/3)+ j*taille_une_heure, 2*(tab/3) + (i+1)*taille_un_jour, 2*(tab2/3)+ (j+1)*taille_une_heure], outline = "black", fill = cl)
                            elif action == "double":
                                self.im.rectangle([2*(tab/3)+ i*taille_un_jour, 2*(tab2/3)+ j*taille_une_heure - taille_une_heure, 2*(tab/3) + (i+1)*taille_un_jour, 2*(tab2/3)+ (j+1)*taille_une_heure], outline = "black", fill = cl)
                                action = "notTrue"
                            elif action == "notTrue":
                                self.im.rectangle([2*(tab/3)+ i*taille_un_jour, 2*(tab2/3)+ j*taille_une_heure, 2*(tab/3) + (i+1)*taille_un_jour, 2*(tab2/3)+ (j+1)*taille_une_heure], outline = "black", fill = cl)
                                action = "normal"

        boucle = True
        j = 1
        while boucle:
            a = str(couleur_edt_4[plus_grande_ecriture_matiere[0]][0])
            taille_texte = self.im.multiline_textbbox((0, 0), str(couleur_edt_4[plus_grande_ecriture_matiere[0]][0]), font = ImageFont.truetype(self.chemin_ecriture, j))
            if taille_texte[3] - taille_texte[1] <= taille_une_heure and \
            taille_texte[2] - taille_texte[0] <= taille_un_jour:
                j += 1
            else:
                boucle = False

        j -= 8

        for i in range(len(liste_matiere)):
            cle = list(liste_matiere[i].keys())[0]
            for k in range(len(liste_matiere[i][cle])):
                cle_heure = list(liste_matiere[i][cle][k].values())[0]
                texte = ""
                for l in range(len(cle_heure[0:3])):
                    if l <=2:
                        if cle_heure[l] or cle_heure == "NULL":
                            texte += cle_heure[l] + "\n"
                if len(texte) >= 2:
                    pass
                    texte = texte[:-1]
                x_debut = 2*(tab/3) + i*taille_un_jour
                x_fin = 2*(tab/3) + (i+1)*taille_un_jour
                y_debut = 2*(tab2/3)+ k*taille_une_heure
                y_double_fin = 2*(tab2/3)+ (k+1)*(taille_une_heure) + taille_une_heure
                y_fin = 2*(tab2/3)+ (k+1)*taille_une_heure
                taille_pour_moyenne = self.im.multiline_textbbox((0, 0), texte, font = ImageFont.truetype(self.chemin_ecriture, j))
                petit_tab = ((x_fin - x_debut) - (taille_pour_moyenne[2] - taille_pour_moyenne[0])) / 2
                if cle_heure[0:3] == heure_apres[i][k][0:3]:
                    action = "double"
                if action == "normal":
                    petit_tab_y = ((y_fin - y_debut) - (taille_pour_moyenne[3] - taille_pour_moyenne[1])) / 2
                elif action == "notTrue":
                    petit_tab_y = ((y_fin - y_debut) - (taille_pour_moyenne[3] - taille_pour_moyenne[1])) / 2
                elif action == "double":
                    petit_tab_y = (((y_double_fin - y_debut) - (taille_pour_moyenne[3] - taille_pour_moyenne[1])) / 2) - taille_une_heure

                if action == "notTrue":
                    action = "normal"
                if action == "double":
                    action = "notTrue"

                self.im.multiline_text((x_debut + petit_tab, y_debut + petit_tab_y), texte, font = ImageFont.truetype(self.chemin_ecriture, j), fill = "black", align = "center")

        g = 0
        for i in range(len(liste_matiere)):
            cle = list(liste_matiere[i].keys())[0]
            for k in range(len(liste_matiere[i][cle])):
                cle_heure = list(liste_matiere[i][cle][k].values())[0]
                if cle_heure[0:3] == heure_apres[i][k][0:3] and cle_heure != []:
                    g += 1
                    for l in range(len(couleur_edt_2)):
                        if cle_heure:
                            if cle_heure[0] == list(couleur_edt_2[l].keys())[0]:
                                cl = list(couleur_edt_2[l].values())[0]
                                self.im.rectangle([2*(tab/3)+ i*taille_un_jour, 2*(tab2/3)+ k*taille_une_heure - taille_une_heure, 2*(tab/3) + (i+1)*taille_un_jour, 2*(tab2/3)+ (k+1)*taille_une_heure], outline = "black", fill = cl)
                                texte = ""
                    for l in range(len(cle_heure[0:3])):
                        if cle_heure[l] or cle_heure == "NULL":
                            texte += cle_heure[l] + "\n"
                    x_debut = 2*(tab/3) + i*taille_un_jour
                    x_fin = 2*(tab/3) + (i+1)*taille_un_jour
                    y_debut = 2*(tab2/3)+ k*taille_une_heure
                    y_double_fin = 2*(tab2/3)+ (k+1)*(taille_une_heure) + taille_une_heure
                    taille_pour_moyenne = self.im.multiline_textbbox((0, 0), texte, font = ImageFont.truetype(self.chemin_ecriture, j))
                    petit_tab = ((x_fin - x_debut) - (taille_pour_moyenne[2] - taille_pour_moyenne[0])) / 2
                    petit_tab_y = (((y_double_fin - y_debut) - (taille_pour_moyenne[3] - taille_pour_moyenne[1])) / 2) - taille_une_heure
                    self.im.multiline_text((x_debut + petit_tab, y_debut + petit_tab_y), texte, font = ImageFont.truetype(self.chemin_ecriture, j), fill = "black", align = "center")
    
    def show(self):
        self.image.show()
    
    def save(self, chemin):
        self.image.save(chemin)
    
    def prof_absent(self, x, y):
        x = 2
        y = 6
        tab = taille[0] / 10
        tab2 = taille[1] / 10
        x_sans_tab = taille[0] - tab
        taille_un_jour = x_sans_tab / len(liste_jours)
        y_sans_tab = taille[1] - tab2
        taille_une_heure = y_sans_tab / len(liste_heures)
        un_huitieme = taille_une_heure / 8
        boucle = True

        o = 1
        while boucle:
            taille_ = self.im.textbbox([0, 0], "Prof Absent", font = ImageFont.truetype(self.chemin_ecriture, o), stroke_width = 1)
            if (taille_[2] - taille_[0]) < taille_un_jour and (taille_[3] - taille_[1]) < un_huitieme:
                o += 1
            else:
                boucle = False

        taille_centre = self.im.textsize("Prof Absent", font = ImageFont.truetype(self.chemin_ecriture, o))
        taille_centre_x = (((2*(tab/3)+ (x+1)*taille_un_jour) - (2*(tab/3) + x*taille_un_jour)) - taille_centre[0])/2
        taille_centre_y = (((2*(tab2/3)+ y*taille_une_heure + un_huitieme) - (2*(tab2/3) + y*taille_une_heure)) - taille_centre[1])/2
        #test = (taille_un_jour - taille_centre)/2
        self.im.rectangle([2*(tab/3)+ x*taille_un_jour, 2*(tab2/3) + y*taille_une_heure, 2*(tab/3) + (x+1)*taille_un_jour, 2*(tab2/3) + y*taille_une_heure + un_huitieme], outline = "black", fill = "white")
        #self.im.text([(2*(tab/3) + (x+1)*taille_un_jour) - (2*(tab/3)+ x*taille_un_jour) + (x)*taille_un_jour, 2*(tab2/3) + y*taille_une_heure + un_huitieme - (2*(tab2/3) + y*taille_une_heure)], "Prof Absent", font = ImageFont.truetype(self.chemin_ecriture, o), fill = "black", align = "center")
        self.im.text([2*(tab/3)+ x*taille_un_jour + taille_centre_x, 2*(tab2/3) + y*taille_une_heure + taille_centre_y], "Prof Absent", font = ImageFont.truetype(self.chemin_ecriture, o), fill = "black", align = "center")


liste_matieres = [{"lundi": [{"8H-9H": []}, \
                             {"9H-10H": []}, \
                             {"10H-11H": ["Maths expertes Option", "Louise Colas", "A209"]}, \
                             {"11H-12H": []}, \
                             {"12H-13H": []}, \
                             {"13H-14H": []}, \
                             {"14H-15H": ["ED. Physique & Sport", "Camille Lombard", "EPS 1"]}, \
                             {"15H-16H": ["ED. Physique & Sport", "Camille Lombard", "EPS 1"]}, \
                             {"16H-17H": ["Mathematiques", "Sylvie Fabre", "Z1"]}, \
                             {"17H-18H": []}]}, \
                  {"mardi": [{"8H-9H": []}, \
                             {"9H-10H": ["Histoire-Geographie", "Augustin Durand", "E314"]}, \
                             {"10H-11H": ["Ensign. Scientifique", "Robert Maillot", "S307"]}, \
                             {"11H-12H": ["Ensign. Scientifique", "Robert Maillot", "S307"]}, \
                             {"12H-13H": []}, \
                             {"13H-14H": []}, \
                             {"14H-15H": ["Numerique Sc. Inform.", "Jules Thierry", "S111"]}, \
                             {"15H-16H": ["Numerique Sc. Inform.", "Jules Thierry", "S111"]}, \
                             {"16H-17H": ["Mathematiques", "Sylvie Fabre", "E317"]}, \
                             {"17H-18H": ["Mathematiques", "Sylvie Fabre", "E317"]}]}, \
                  {"mercredi": [{"8H-9H": ["Numerique Sc. Inform.", "Jules Thierry", "S111"]}, \
                             {"9H-10H": ["Numerique Sc. Inform.", "Jules Thierry", "S111"]}, \
                             {"10H-11H": ["Anglais LV1", "Joséphine Louis", "E312"]}, \
                             {"11H-12H": ["Philosophie", "Marc Baron", "E307"]}, \
                             {"12H-13H": []}, \
                             {"13H-14H": []}, \
                             {"14H-15H": ["Maths expertes Option", "Louise Colas", "E316"]}, \
                             {"15H-16H": ["Maths expertes Option", "Louise Colas", "E316"]}, \
                             {"16H-17H": ["Mathematiques", "Sylvie Fabre", "Z1"]}, \
                             {"17H-18H": []}]}, \
                  {"jeudi": [{"8H-9H": ["Philosophie", "Marc Baron", "E307"]}, \
                             {"9H-10H": ["Espagnol LV2", "Charlotte Lagarde", "Z2"]}, \
                             {"10H-11H": ["Histoire-Geographie", "Augustin Durand", "E314"]}, \
                             {"11H-12H": ["Histoire-Geographie", "Augustin Durand", "E314"]}, \
                             {"12H-13H": []}, \
                             {"13H-14H": []}, \
                             {"14H-15H": ["Philosophie", "Marc Baron", "E307"]}, \
                             {"15H-16H": []}, \
                             {"16H-17H": ["Ens. Moral & Civique", "Augustin Durand", "E314"]}, \
                             {"17H-18H": []}]}, \
                  {"vendredi": [{"8H-9H": ["Mathematiques", "Sylvie Fabre", "Z2"]}, \
                             {"9H-10H": ["Mathematiques", "Sylvie Fabre", "Z2"]}, \
                             {"10H-11H": ["Philosophie", "Marc Baron", "E307"]}, \
                             {"11H-12H": ["Vie De Classe", "Marc Baron"]}, \
                             {"12H-13H": []}, \
                             {"13H-14H": ["Espagnol LV2", "Charlotte Lagarde", "E317", "Prof absent"]}, \
                             {"14H-15H": ["Anglais LV1", "Joséphine Louis", "E312"]}, \
                             {"15H-16H": ["Numerique Sc. Inform.", "Jules Thierry", "S113"]}, \
                             {"16H-17H": ["Numerique Sc. Inform.", "Jules Thierry", "S113"]}, \
                             {"17H-18H": []} ]}]

a = ExportEDT("Geosanslight.ttf")
a.inserer_liste_matiere(taille, liste_jours, liste_heures, liste_matieres)
a.prof_absent(1,1)


#self.image.show()
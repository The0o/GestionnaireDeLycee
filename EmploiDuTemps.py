import sqlite3
import os.path
import datetime

class EmploiDuTemps:
    """Classe qui cree une base de donnee qui peut gerer un emploi du temps d'un etablisement scolaire
    Il est fortement conseillé d'utiliser cette classe avec la classe "InterfaceGraphique".
    """

    def __init__(self, nom_base):
        if os.path.exists(nom_base):
            self.conn = sqlite3.connect(nom_base)
            self.curseur = self.conn.cursor()
        else:
            self.conn = sqlite3.connect(nom_base)
            self.curseur = self.conn.cursor()
            self.curseur.execute("""CREATE TABLE Prof(idProf INTEGER PRIMARY KEY,
                                                      nom TEXT,
                                                      prenom TEXT);""")
            self.curseur.execute("""CREATE TABLE Classe(idc INTEGER PRIMARY KEY,
                                                        nom TEXT,
                                                        idProf INTEGER,
                                                        FOREIGN KEY (idProf) REFERENCES Prof(idProf));""")
            self.curseur.execute("""CREATE TABLE Eleve(idEleve INTEGER PRIMARY KEY,
                                                       nom TEXT,
                                                       prenom TEXT,
                                                       classe TEXT,
                                                       dateNaissance DATE,
                                                       FOREIGN KEY (classe) REFERENCES Classe(idc));""")
            self.curseur.execute("""CREATE TABLE Horaire(idHoraire INTEGER PRIMARY KEY,
                                                        debut TIME,
                                                        fin TIME,
                                                        jour INTEGER,
                                                        libre BOOLEAN);""")
            self.curseur.execute("""CREATE TABLE MatiereProf(idProf INTEGER,
                                                             idMatiere INTEGER,
                                                             FOREIGN KEY(idProf) REFERENCES Prof(idProf),
                                                             FOREIGN KEY(idMatiere) REFERENCES Matiere(idMatiere));""")
            self.curseur.execute("""CREATE TABLE Cours(idProf INTEGER,
                                                       idMatiere INTEGER,
                                                       idClasse INTEGER,
                                                       idSalle INTEGER,
                                                       idHoraire INTEGER,
                                                       idEleve INTEGER,
                                                       FOREIGN KEY(idPRof) REFERENCES Prof(idProf),
                                                       FOREIGN KEY(idMatiere) REFERENCES Matiere(idMatiere)
                                                       FOREIGN KEY(idClasse) REFERENCES Classe(idClasse)
                                                       FOREIGN KEY(idSalle) REFERENCES Salle(idSalle)
                                                       FOREIGN KEY(idHoraire) REFERENCES Horaire(idHoraire)
                                                       FOREIGN KEY(idEleve) REFERENCES Eleve(idEleve));""")
            self.curseur.execute("""CREATE TABLE Matiere(idMatiere INTEGER PRIMARY KEY,
                                                         nom TEXT);""")
            self.curseur.execute("""CREATE TABLE Salle(idSalle INTEGER PRIMARY KEY,
                                                       nom TEXT,
                                                       capacite INTEGER,
                                                       type TEXT);""")
            self.conn.commit()

    # TOUS LES ADD

    def add_prof(self, id_, nom, prenom):
        """Methode qui permet d'ajouter un professeur dans la base de donnnee

        Args:
            id_ (Int): L'id unique du professeur
            nom (String): Le nom du professeur
            prenom (String): Le prenom du professeur
        """
        insertion = "INSERT INTO Prof(idProf, nom, prenom) "
        insertion += "VALUES (?, ?, ?);"
        info_prof = (id_, nom, prenom)
        self.curseur.execute(insertion, info_prof)
        self.conn.commit()

    def add_classe(self, id_, nom_classe, prof_principal):
        """Methode qui permet d'ajouter une classe dans la base de donnnee

        Args:
            id_ (Int): L'id unique de la classe
            nom_classe (String): Le nom de la classe
            prof_principal (Int): L'id du professeur principal
        """
        insertion = "INSERT INTO Classe(idc, nom, idProf) "
        insertion += "VALUES (?, ?, ?);"
        info_classe = (id_, nom_classe, prof_principal)
        self.curseur.execute(insertion, info_classe)
        self.conn.commit()

    def add_eleve(self, id_, nom, prenom, classe, dateNaissance):
        """Methode qui permet d'ajouter un eleve dans la base de donnnee

        Args:
            id_ (Int): L'id unique de l'eleve
            nom (String): Le nom de l'eleve
            prenom (String): Le prenom de l'eleve
            classe (Int): L'id de la classe
            dateNaissance (Date): La date de naissance de l'eleve
        """
        insertion = "INSERT INTO Eleve(idEleve, nom, prenom, classe, dateNaissance) "
        insertion += "VALUES (?, ?, ?, ?, ?);"
        info_eleve = (id_, nom, prenom, classe, dateNaissance)
        self.curseur.execute(insertion, info_eleve)
        self.conn.commit()

    def add_matiere(self, id_matiere, nom):
        """Methode qui permet d'ajouter une matiere dans la base de donnnee

        Args:
            id_matiere (Int): L'id unique de la matiere
            nom (String): Le nom de la matiere
        """
        insertion = "INSERT INTO Matiere(idMatiere, nom)"
        insertion += "VALUES (?, ?);"
        info_matiere = (id_matiere, nom)
        self.curseur.execute(insertion, info_matiere)
        self.conn.commit()

    def add_horaire(self, id_horaire, debut, fin, jour, libre):
        """Methode qui permet d'ajouter une horaire dans la base de donnnee

        Args:
            id_horaire (Int): L'id unique de l'horaire
            debut (???): L'heure du commencement de l'heure
            fin (???): L'heure de la fin de l'heure
            jour (Int): Le jour de la semaine de l'heure
            libre (Boolean): Indique si l'heure est libre
        """
        insertion = "INSERT INTO Horaire(idHoraire, debut, fin, jour, libre)"
        insertion += "VALUES (?, ?, ?, ?, ?);"
        info_horaire = (id_horaire, debut, fin, jour, libre)
        self.curseur.execute(insertion, info_horaire)
        self.conn.commit()

    def add_salle(self, idSalle, nom, capacite, typ):
        """Methode qui permet d'ajouter une salle dans la base de donnnee

        Args:
            idSalle (Int): L'id unique de la salle
            nom (String): Le nom de la salle
            capacite (Int): Le nombre de places possibles dans la salle
            type (String): Le type de la salle
        """
        insertion = "INSERT INTO Salle(idSalle, nom, capacite, type)"
        insertion += "VALUES (?, ?, ?, ?)"
        info_salle = (idSalle, nom, capacite, typ)
        self.curseur.execute(insertion, info_salle)
        self.conn.commit()

    def add_matiere_prof(self, idProf, idMatiere):
        """Methode qui permet d'ajouter un professeur lie a une matiere dans la base de donnnee

        Args:
            idProf (Int): L'id du professeur qui enseigne la matiere
            idMatiere (Int): L'id de la matiere enseignee par le professeur
        """
        insertion = "INSERT INTO MatiereProf(idProf, idMatiere)"
        insertion += "VALUES (?, ?)"
        info_matiere_prof = (idProf, idMatiere)
        self.curseur.execute(insertion, info_matiere_prof)
        self.conn.commit()

    def add_cours(self, idProf, idMatiere, idClasse, idSalle, idHoraire, idEleve):
        """Methode qui permet d'ajouter un cours dans la base de donnnee

        Args:
            idProf (Int): L'id du professeur
            idMatiere (Int): L'id de la matiere
            idClasse (Int): L'id de la classe
            idSalle (Int): L'id de la salle
            idHoraire (Int): L'id de l'horaire
            idEleve (Int): L'id de l'eleve
        """
        insertion = "INSERT INTO Cours(idProf, idMatiere, idClasse, idSalle, idHoraire, idEleve)"
        insertion += "VALUES (?, ?, ?, ?, ?, ?)"
        info_cours = (idProf, idMatiere, idClasse, idSalle, idHoraire, idEleve)
        self.curseur.execute(insertion, info_cours)
        self.conn.commit()

    # TOUS LES VOIR CLASSIQUES

    def voir_matiere_prof(self):
        """Methode qui permet de voir tous les id des professeurs lies aux id de la matiere

        Returns:
            Liste: Liste de tuple contenant un id d'un professeur et un id de la matiere
        """
        liste = []
        insertion = "SELECT idProf, idMatiere FROM MatiereProf"
        for a in self.curseur.execute(insertion):
            liste.append(a)
        return liste

    def voir_matiere(self):
        """Methode qui permet de voir tous les noms de toutes les matieres existantes

        Returns:
            Liste: Liste de tuple contenant tous les noms de toutes les matieres existantes
        """
        liste = []
        insertion = "SELECT nom FROM Matiere;"
        for a in self.curseur.execute(insertion):
            liste.append(a)
        return liste

    def voir_eleve (self):
        """Methode qui permet d'avoir tous les noms et prenoms de tous les eleves

        Returns:
            Liste: Liste de tuple contenant tous les noms et prenoms de tous les eleves
        """
        liste = []
        insertion = "SELECT nom, prenom FROM Eleve;"
        for eleve in self.curseur.execute(insertion):
                liste.append(eleve)
        return liste

    def voir_classe(self):
        """Methode qui permet de voir toutes les noms de toutes les classes existantes

        Returns:
            Liste: Liste de tuple contenant tous les noms de toutes les classes existantes
        """
        liste = []
        insertion = "SELECT nom FROM Classe;"
        for classe in self.curseur.execute(insertion):
            liste.append(classe)
        return liste

    def voir_prof(self):
        """Methode qui permet de voir toutes les noms et prenoms de tous les professeurs existants

        Returns:
            Liste: Liste de tuple contenant tous les noms et prenoms de tous les professeurs existants
        """
        liste = []
        insertion = "SELECT nom, prenom FROM Prof;"
        for prof in self.curseur.execute(insertion):
            liste.append(prof)
        return liste

    def voir_salle(self):
        """Methode qui permet de voir toutes les noms, les capacites et les types de toutes les salles existantes

        Returns:
            Liste: Liste de tuple contenant tous les noms, les capacites et les types de toutes les salles existantes
        """
        liste = []
        insertion = "SELECT nom, capacite, type FROM Salle;"
        for salle in self.curseur.execute(insertion):
            liste.append(salle)
        return liste

    def voir_horaire(self):
        """Methode qui permet de voir tous les attributs debut, fin, jour et libre de toutes les horaires existantes

        Returns:
            Liste: Liste de tuple contenant tous les attributs debut, fin, jour et libre de toutes les horaires existantes
        """
        liste = []
        insertion = "SELECT debut, fin, jour, libre FROM Horaire;"
        for horaire in self.curseur.execute(insertion):
            liste.append(horaire)
        return liste

    def voir_cours(self):
        """Methode qui permet de voir tous les attributs
        (id du professeur, id de la matiere, l'id de la classe, l'id de la salle,
        l'id de l'horaire, l'id de l'eleve) de tous les cours existants

        Returns:
            Liste: Liste de tuple contenant tous les attributs
            (id du professeur, id de la matiere, l'id de la classe, l'id de la salle,
            l'id de l'horaire, l'id de l'eleve) de tous les cours existants
        """
        liste = []
        insertion = "SELECT idPRof, idMatiere, idClasse, idSalle, idHoraire, idEleve FROM Cours;"
        for a in self.curseur.execute(insertion):
            liste.append(a)
        return liste

    # TOUS LES VOIR INFO (TOUS LES ATTRIBUTS)

    def voir_info_professeur(self):
        """Methode qui permet de voir tous les attributs (l'id du professeur, le nom, le prenom) de tous les professeurs existants

        Returns:
            Liste: Liste de tuple contenant tous les attributs (l'id du professeur, le nom, le prenom) de tous les professeurs existants
        """
        liste = []
        insertion = "SELECT * FROM Prof;"
        for a in self.curseur.execute(insertion):
            liste.append(a)
        return liste

    def voir_info_eleve(self):
        """Methode qui permet de voir tous les attributs de tous les eleves

        Returns:
            Liste: Liste de tuple contenant tous les attributs de tous les eleves
        """
        liste = []
        insertion = "SELECT * FROM Eleve;"
        for a in self.curseur.execute(insertion):
            liste.append(a)
        return liste

    def voir_info_classe(self):
        """Methode qui permet de voir tous les attributs (l'id de la classe, le nom,
        l'id du professeur principal) de toutes les classes existantes

        Returns:
            Liste: Liste de tuple contenant tous les attributs (l'id de la classe, le nom,
            l'id du professeur principal) de toutes les classes existantes
        """
        liste = []
        insertion = "SELECT * FROM Classe;"
        for a in self.curseur.execute(insertion):
            liste.append(a)
        return liste

    def voir_info_salle(self):
        """Methode qui permet de voir tous les attributs (l'id de la salle, le nom,
        sa capacite, et le type de la salle) de toutes les salles existantes

        Returns:
            Liste: Liste de tuple contenant tous les attributs (l'id de la salle, le nom,
            sa capacite, et le type de la salle) de toutes les salles existantes
        """
        liste = []
        insertion = "SELECT * FROM Salle;"
        for a in self.curseur.execute(insertion):
            liste.append(a)
        return liste

    def voir_info_horaire(self):
        """Methode qui permet de voir tous les attributs (l'id de l'horaire, le debut,
        la fin, le jour, si l'horaire est libre) de toutes les horaires existantes

        Returns:
            Liste: Liste de tuple contenant tous les attributs (l'id de l'horaire, le debut,
            la fin, le jour, si l'horaire est libre) de toutes les horaires existantes
        """
        liste = []
        insertion = "SELECT * FROM Horaire;"
        for a in self.curseur.execute(insertion):
            liste.append(a)
        return liste

    def voir_info_matiere(self):
        """Methode qui permet de voir tous les attributs
        (l'id de la matiere, le nom) de toutes les matieres existantes

        Returns:
            Liste: Liste de tuple contenant tous les attributs
            (l'id de la matiere, le nom) de toutes les matieres existantes
        """
        liste = []
        insertion = "SELECT * FROM Matiere;"
        for a in self.curseur.execute(insertion):
            liste.append(a)
        return liste

    def voir_info_matiere_prof(self):
        """Methode qui permet de voir tous les attributs (l'id de la matiere,
        l'id du professeur) de toutes les matieres et professeurs relies

        Returns:
            Liste: Liste de tuple contenant tous les attributs (l'id de la matiere,
            l'id du professeur) de toutes les matieres et professeurs relies
        """
        liste = []
        insertion = "SELECT * FROM MatiereProf;"
        for a in self.curseur.execute(insertion):
            liste.append(a)
        return liste

    # TOUS LES MODIFIER

    def modifier_info_eleve__(self, nom_colonne_a_modifier, nouv_donne, _id):
        """Methode qui permet de modfifier un eleve

        Args:
            nom_colonne_a_modifier (String): Le nom de la colonne ou l'on shouaite modifier l'information
            nouv_donne (Depend du type de donnee modifier): La nouvelle donnee a inserer
            _id (Int): L'id de l'eleve que l'on shouaite mmodifier
        """
        insertion = f"UPDATE Eleve SET {nom_colonne_a_modifier}='{nouv_donne}' "\
                    f"WHERE idEleve={_id};"
        self.curseur.execute(insertion)
        self.conn.commit()

    def modifier_info_professeur__(self, nom_colonne_a_modifier, nouv_donne, _id):
        """Methode qui permet de modfifier un professeur

        Args:
            nom_colonne_a_modifier (String): Le nom de la colonne ou l'on shouaite modifier l'information
            nouv_donne (Depend du type de donnee modifier): La nouvelle donnee a inserer
            _id (Int): L'id du professeur que l'on shouaite mmodifier
        """
        insertion = f"UPDATE Professeur SET {nom_colonne_a_modifier}='{nouv_donne}' "\
                    f"WHERE idProf={_id};"
        self.curseur.execute(insertion)
        self.conn.commit()

    def modifier_info_salle__(self, nom_colonne_a_modifier, nouv_donne, _id):
        """Methode qui permet de modfifier une salle

        Args:
            nom_colonne_a_modifier (String): Le nom de la colonne ou l'on shouaite modifier l'information
            nouv_donne (Depend du type de donnee modifier): La nouvelle donnee a inserer
            _id (Int): L'id de la salle que l'on shouaite mmodifier
        """
        insertion = f"UPDATE Salle SET {nom_colonne_a_modifier}='{nouv_donne}' "\
                    f"WHERE idSalle={_id};"
        self.curseur.execute(insertion)
        self.conn.commit()

    def modifier_info_horaire__(self, nom_colonne_a_modifier, nouv_donne, _id):
        """Methode qui permet de modfifier une horaire

        Args:
            nom_colonne_a_modifier (String): Le nom de la colonne ou l'on shouaite modifier l'information
            nouv_donne (Depend du type de donnee modifier): La nouvelle donnee a inserer
            _id (Int): L'id de l'horaire que l'on shouaite mmodifier
        """
        insertion = f"UPDATE Horaire SET {nom_colonne_a_modifier}='{nouv_donne}' "\
                    f"WHERE idHoraire={_id};"
        self.curseur.execute(insertion)
        self.conn.commit()

    def modifier_info_matiere__(self, nom_colonne_a_modifier, nouv_donne, _id):
        """Methode qui permet de modfifier une matiere

        Args:
            nom_colonne_a_modifier (String): Le nom de la colonne ou l'on shouaite modifier l'information
            nouv_donne (Depend du type de donnee modifier): La nouvelle donnee a inserer
            _id (Int): L'id de la matiere que l'on shouaite mmodifier
        """
        insertion = f"UPDATE Matiere SET {nom_colonne_a_modifier}='{nouv_donne}' "\
                    f"WHERE idMatiere={_id};"
        self.curseur.execute(insertion)
        self.conn.commit()

    def modifier_info_classe__(self, nom_colonne_a_modifier, nouv_donne, _id):
        """Methode qui permet de modfifier une classe

        Args:
            nom_colonne_a_modifier (String): Le nom de la colonne ou l'on shouaite modifier l'information
            nouv_donne (Depend du type de donnee modifier): La nouvelle donnee a inserer
            _id (Int): L'id de la classe que l'on shouaite mmodifier
        """
        insertion = f"UPDATE Classe SET {nom_colonne_a_modifier}='{nouv_donne}' "\
                    f"WHERE IDC={_id};"
        self.curseur.execute(insertion)
        self.conn.commit()

    # TOUS LES SUPPRIMER

    def supprimer_eleve(self, _id):
        insertion = f"DELETE FROM Eleve WHERE idEleve={_id}"
        self.curseur.execute(insertion)
        self.conn.commit()

    def supprimer_professeur(self, _id):
        insertion = f"DELETE FROM Prof WHERE idProf={_id}"
        self.curseur.execute(insertion)
        self.conn.commit()

    def supprimer_salle(self, _id):
        insertion = f"DELETE FROM Salle WHERE idSalle={_id}"
        self.curseur.execute(insertion)
        self.conn.commit()

    def supprimer_horaire(self, _id):
        insertion = f"DELETE FROM Horaire WHERE idHoraire={_id}"
        self.curseur.execute(insertion)
        self.conn.commit()

    def supprimer_matiere(self, _id):
        insertion = f"DELETE FROM Matiere WHERE idMatiere={_id}"
        self.curseur.execute(insertion)
        self.conn.commit()

    def supprimer_classe(self, _id):
        insertion = f"DELETE FROM Classe WHERE idc={_id}"
        self.curseur.execute(insertion)
        self.conn.commit()

    def supprimer_matiere_professeur(self, _idProf, _idMatiere):
        insertion = f"DELETE FROM MatiereProf WHERE idProf={_idProf} AND idMatiere = {_idMatiere}"
        self.curseur.execute(insertion)
        self.conn.commit()

    def supprimer_cours(self, idProf, idMatiere, idClasse, idSalle, idHoraire):
        insertion = f"DELETE FROM Cours WHERE idProf={idProf} AND idMatiere={idMatiere} AND idClasse={idClasse} AND idSalle={idSalle} AND idHoraire={idHoraire}"
        self.curseur.execute(insertion)
        self.conn.commit()

    # AUTRES FONCTIONS

    def voir_effectif_classe(self, id_):
        """Methode qui permet de voir le nombre d'eleve dans une classe

        Args:
            id_ (Int): L'id de la classe

        Returns:
            Int: Le nombre d'eleve dans la classe
        """
        insertion = "SELECT COUNT(*) FROM Eleve WHERE classe="
        insertion += "(?);"
        id_classe = str(id_)
        for a in self.curseur.execute(insertion, [id_classe]):
            retour = a[0]
        return retour

    def voir_eleve_classe(self, id_):
        """Methode qui permet de voir le nom et le prenom des eleves d'une classe

        Args:
            id_ (Int): L'id de la classe

        Returns:
            Liste: Liste de tuple contenant les noms et prenoms des eleves de la classe selectionne
        """
        insertion = "SELECT idEleve FROM Eleve WHERE classe="
        insertion += "(?);"
        id_classe = str(id_)
        liste_eleve = []
        for a in self.curseur.execute(insertion, [id_classe]):
            liste_eleve.append(a[0])
        return liste_eleve

    def cours_eleve(self, _id):
        liste_cours = []
        insertion = "SELECT Classe FROM Eleve WHERE idEleve=" + str(_id[0])
        for a in self.curseur.execute(insertion):
            classe = a[0]
        insertion = "SELECT * FROM Cours WHERE idClasse=" + str(classe)
        for a in self.curseur.execute(insertion):
            liste_cours.append(a)
        return liste_cours

    def cours_prof(self, _id):
        liste_cours = []
        insertion = "SELECT * FROM Cours WHERE idProf=" + str(_id[0])
        for a in self.curseur.execute(insertion):
            liste_cours.append(a)
        return liste_cours

    def voir_prof_id(self, _id):
        insertion = "SELECT nom, prenom FROM Prof WHERE idProf=" + str(_id) + ";"
        for a in self.curseur.execute(insertion):
            prof = a[0] + " " + a[1]
        self.conn.commit()
        return prof

    def voir_matiere_id(self, _id):
        insertion = "SELECT nom FROM Matiere WHERE idMatiere=" + str(_id) + ";"
        for a in self.curseur.execute(insertion):
            matiere = a[0]
        self.conn.commit()
        return matiere

    def voir_salle_id(self, _id):
        insertion = "SELECT nom FROM Salle WHERE idSalle=" + str(_id) + ";"
        for a in self.curseur.execute(insertion):
            salle = a[0]
        self.conn.commit()
        return salle

    def voir_horaire_id(self, _id):
        insertion = "SELECT debut, fin, jour FROM horaire WHERE idHoraire=" + str(_id) + ";"
        for a in self.curseur.execute(insertion):
            horaire = [a[0], a[1], a[2]]
        self.conn.commit()
        return horaire

    def voir_classe_id(self, _id):
        insertion = "SELECT nom FROM Classe WHERE idc=" + str(_id) + ";"
        for a in self.curseur.execute(insertion):
            classe = a[0]
        self.conn.commit()
        return classe

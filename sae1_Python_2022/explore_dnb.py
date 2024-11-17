
# -----------------------------------------------------------------------------------------------------
# listes de fonctions à implémenter
# -----------------------------------------------------------------------------------------------------

#   from symbol import dictorsetmaker
from unittest import result
from xmlrpc.client import boolean


def taux_reussite(resultat):
    """calcule le pourcentage de réussite correspondant au résultat

    Args:
        resultat (tuple): le résultat d'un collège pour une session (année)
        
    Returns:
        float: le pourcentage de réussite (nb. admis / nb. présents)
    """
    if resultat != () and len(resultat) == 5 and type(resultat[4])==int and type(resultat[3])==int and resultat[3]!=3 and resultat[3]!=0 :
        return resultat[4]/resultat[3]*100



def meilleur(resultat1, resultat2):
    """vérifie si resultat1 est meilleur que resultat2 au sens des taux de réussites

    Args:
        resultat1 (tuple): un résultat d'un collège pour une session (année)
        resultat2 (tuple): un autre résultat d'un collège pour une session (année)

    Returns:
        bool: True si le taux de réussite de resultat1 est supérieur au taux de réussite de resultat2
    """    
    if resultat1 != () and len(resultat1) == 5 and resultat2 != () and len(resultat2) == 5 :    
        return taux_reussite(resultat1) > taux_reussite(resultat2)


def meilleur_taux_reussite(liste_resultats):
    """recherche le meilleur taux de réussite parmi une liste de résultats

    Args:
        liste_resultats (list): une liste de resultats

    Returns:
        float: le meilleur taux de réussite
    """
    if liste_resultats != []:
        maximum=taux_reussite(liste_resultats[0])
        for element in liste_resultats:
            if maximum < taux_reussite(element):
                maximum=taux_reussite(element)
        return maximum


def pire_taux_reussite(liste_resultats):
    """recherche le pire taux de réussite parmi une liste de résultats

    Args:
        liste_resultats (list): une liste de resultats

    Returns:
        float: le pire taux de réussite
    """
    if liste_resultats != []:
        minimum=taux_reussite(liste_resultats[0])
        for element in liste_resultats:
            if minimum >= taux_reussite(element):
                minimum=taux_reussite(element)
        return minimum
    


def total_admis_presents(liste_resultats):
    """calcule le nombre total de candidats admis et de candidats présents aux épreuves du DNB parmi les résultats de la liste passée en paramètre

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        tuple : un couple d'entiers contenant le nombre total de candidats admis et présents
    """
    if liste_resultats !=[]:
        present=0
        admis=0
        for element in liste_resultats:
               if type(element[4])==int and type(element[3])==int:
                present+=element[4]
                admis+=element[3]
        return present,admis
    


def filtre_session(liste_resultats, session):
    """génère la sous-liste de liste_resultats, restreinte aux résultats de la session demandée

    Args:
        liste_resultats (list): une liste de résultats
        session (int): une session (année)

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats de la session demandée
    """
    liste_renvoye=[]
    for element in liste_resultats:
        if element[0]==session:
            liste_renvoye.append(element)
    return liste_renvoye


def filtre_departement(liste_resultats, departement):
    """génère la sous-liste de liste_resultats, restreinte aux résultats du département demandé

    Args:
        liste_resultats (list): une liste de résultats
        departement (int): un numéro de département

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats du département demandé
    """
    if liste_resultats != [] and type(departement)==int:
        liste_renvoye=[]
        for tuples in liste_resultats:
            if type(tuples[2]) == int and tuples[2]==departement:
                liste_renvoye.append(tuples)
        return liste_renvoye


def filtre_college(liste_resultats, nom, departement):
    """génère la sous-liste de liste_resultats, restreinte aux résultats du département donné et dont le nom du collège contient le nom passé en paramètre (en minuscule ou majuscule)

    Args:
        liste_resultats (list): une liste de résultats
        nom (str): un nom de collège (éventuellement incomplet)
        departement (int) : un numéro de département

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats du collège et du département recherchés
    """
    if liste_resultats != [] and type(departement)==int and type(nom)==str:
        liste_renvoye=[]
        for tuples in liste_resultats:
            if type(tuples[2]) == int and tuples[2]==departement and nom in tuples[1] and type(tuples[1])==str:
                liste_renvoye.append(tuples)
        return liste_renvoye



def taux_reussite_global(liste_resultats, session):
    """calcule le taux (pourcentage) de réussite au DNB sur l'ensemble des collèges pour une session donnée

    Args:
        liste_resultats (list): une liste de résultats
        session (int) : une session (année)
        
    Returns:
        float: taux (pourcentage) de réussite au DNB sur l'ensemble des collèges pour une session données
    """
    if liste_resultats!=[]:
        nb_admis=0
        nb_present=0
        for element in liste_resultats:
            if len(element)==5 and type(element[3])==int and type(element[4]) and type(session)==int and session==element[0] :
                nb_admis+= element[4]
                nb_present+=element[3]
        if nb_present != 0:
            return nb_admis/nb_present*100
        return None



def moyenne_taux_reussite_college(liste_resultats, nom, departement):
    """calcule la moyenne des taux de réussite d'un collège sur l'ensemble des sessions

    Args:
        liste_resultats (list): une liste de résultats
        nom (str): un nom de collège (exact)
        departement (int) : un numéro de département
        
    Returns:
        float: moyenne des taux de réussite d'un collège sur l'ensemble des sessions
    """
    if liste_resultats!=[]:
        taux=0
        cpt=0
        for element in liste_resultats:
            if nom in element[1] and departement == element[2]:
                taux += taux_reussite(element)
                cpt += 1
        if cpt!=0:
            return taux/cpt
        return None

    


def meilleur_college(liste_resultats, session):
    """recherche le collège ayant obtenu le meilleur taux de réussite pour une session donnée

    Args:
        liste_resultats (list): une liste de résultats
        session (int) : une session (année)
        
    Returns:
        tuple: couple contenant le nom du collège et le département
    """
    if liste_resultats != []:
        tuple = liste_resultats[0]
        verify_session=False
        for ind in range(1,len(liste_resultats)):
            if session == liste_resultats[ind][0] :
                verify_session =True
                bool = meilleur(liste_resultats[ind],tuple) 
                if bool:
                    tuple= liste_resultats[ind]
        if not verify_session :
           return None
        return tuple[1],tuple[2]


def tri_selection(liste):
    """trier la liste données en paramétre par ordre croissant
    args:
        liste(liste): une liste d'années
    returns:
        liste: une liste trié dans l'ordre croissant
    """
    for i in range(len(liste)):
        indice_mini=i
        mini=liste[i]
        for j in range(i+1,len(liste)):
            if liste[j] < mini:
                indice_mini=j
                mini=liste[j]
        if indice_mini != i:
            temp=liste[i]
            liste[i]=liste[indice_mini]
            liste[indice_mini]=temp
    return liste



def liste_sessions(liste_resultats):
    """retourne la liste des sessions (années) dont au moins un résultat est reporté dans la liste de résultats.
    ATTENTION : la liste renvoyée doit être sans doublons et triée par ordre chronologique des sessions 

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        list: une liste de session (int) triée (ete) sans doublons
    """    
    if liste_resultats!=[]:
        liste_renvoye=[]
        for element in liste_resultats:
            if element[0] not in liste_renvoye :
                liste_renvoye.append(element[0])

        tri_selection(liste_renvoye)
        return liste_renvoye
    return []

def plus_longe_periode_amelioration(liste_resultats):
    """recherche la plus longue periode d'amélioration du taux de réussite global au DNB

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        tuple: un couple contenant la session (année) de début de la période et la session de fin de la période
    """    
    if liste_resultats != []:
        liste_anne= liste_sessions(liste_resultats)
        dico = {}
        liste=[]
        cpt="1"
        if len(liste_anne) > 1:
            for ind in range(len(liste_anne)-1):
                print(liste_anne[ind])
                taux = taux_reussite_global(liste_resultats, liste_anne[ind])
                
                if taux_reussite_global(liste_resultats,liste_anne[ind +1]) < taux:
                    dico[cpt] = [liste_anne[ind],liste_anne[ind+1]]
                    (print(taux))
                    cpt+="1"
            return dico

    """"
    #if liste_resultats!=[]:       
    #    liste_anne = liste_sessions(liste_resultats)
    #    dico={}
    #    liste=[]
    #    premiere_anne = liste_anne[0]
    #    if len(liste_anne) < 1 :
            return None
        for anne in range(1,len(liste_anne)):
            taux = taux_reussite_global(liste_resultats,anne)
            #if taux_reussite_global(liste_resultats,premiere_anne) < taux:
                #dico[premiere_anne] = [premiere_anne,anne]        

        return dico
    """

def est_bien_triee(liste_resultats):
    """vérifie qu'une liste de résultats est bien triée dans l'ordre chronologique des sessions puis dans l'ordre croissant des départements puis dans l'ordre alphabétique des noms de collèges
    
    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        bool: True si la liste est bien triée et False sinon
    """
    pass


def fusionner_resultats(liste_resultats1, liste_resultats2):
    """Fusionne deux listes de résultats triées sans doublons en une liste triée sans doublon
    sachant qu'un même résultat peut être présent dans les deux listes

    Args:
        liste_resultat1 (list): la première liste de résultats
        liste_resultat2 (list): la seconde liste de résultats

    Returns:
        list: la liste triée sans doublon comportant tous les résultats de liste_resultats1 et liste_resultats2
    """
    pass


def charger_resultats(nom_fichier):
    """charge un fichier de résultats au DNB donné au format CSV en une liste de résultats

    Args:
        nom_fichier (str): nom du fichier CSV contenant les résultats au DNB

    Returns:
        list: la liste des résultats contenus dans le fichier
    """
    liste=[]
    fic=open(nom_fichier,'r')
    fic.readline()
    for elem in fic:
        fic.strip()
        session, patronyme, departement, nombre_de_presents, nombre_total_d_admis = fic.split(',')
        liste.append((int(session), patronyme, int(departement), int(nombre_de_presents), int(nombre_total_d_admis)))
    return liste

# ---------------------------------------------------------------------------------------------
# Exemples de données pour vous aider à faire des tests
# ---------------------------------------------------------------------------------------------

# exemples de résultats
resultat1 = (2008, "JEANNE D'ARC", 45, 71, 67)
resultat2 = (2012, "ALBERT SIDOISNE", 28, 98, 78)
resultat3 = (2016, "JEAN MONNET", 37, 115, 109)

# exemples de listes de résultats
liste1 = [(2020, 'ALBERT SIDOISNE', 28, 134, 118),
          (2020, 'ANATOLE FRANCE', 28, 63, 47),
          (2020, 'DE NERMONT - CHATEAUDUN', 28, 74, 60),
          (2020, 'DE NERMONT - NOGENT', 28, 28, 27),
          (2020, 'EMILE ZOLA', 28, 103, 88),
          (2020, 'GILBERT COURTOIS', 28, 22, 18),
          (2020, 'MATHURIN REGNIER', 28, 152, 118)]


liste2 = [(2020, 'ALBERT SIDOISNE', 28, 134, 118),
          (2020, 'ANATOLE FRANCE', 28, 63, 47),
          (2020, 'DE NERMONT - CHATEAUDUN', 28, 74, 60),
          (2020, 'DE NERMONT - NOGENT', 28, 28, 27),
          (2020, 'EMILE ZOLA', 28, 103, 88),
          (2020, 'GILBERT COURTOIS', 28, 22, 18),
          (2020, 'MATHURIN REGNIER', 28, 152, 118),
          (2021, 'DE BEAUMONT LES AUTELS', 28, 37, 34),
          (2021, 'DE NERMONT - CHATEAUDUN', 28, 71, 60),
          (2021, 'EMILE ZOLA', 28, 96, 85),
          (2021, 'GILBERT COURTOIS', 28, 24, 15),
          (2021, 'JEAN MONNET', 28, 97, 91),
          (2021, 'LA PAJOTTERIE', 28, 91, 72),
          (2021, 'ND - LA LOUPE', 28, 12, 9),
          (2021, 'PIERRE BROSSOLETTE', 28, 93, 70),
          (2021, 'SULLY', 28, 14, 10),
          ]



liste3 = [(2021, 'HENRI POURRAT', 45, 17, 16),
          (2021, 'DU HAUT ALLIER', 45, 54, 49),
          (2021, 'LA PRESENTATION', 45, 26, 24),
          (2021, 'NOTRE DAME DU CHATEAU', 45, 27, 25),
          (2021, 'SAINT JACQUES DE COMPOSTELLE', 45, 83, 82),
          (2021, 'LAURENT EYNAC', 45, 59, 52),
          (2021, 'VAL DE SENOUIRE', 45, 23, 21),
          (2021, 'CHARLES ET ADRIEN DUPUY', 45, 13, 5),
          (2021, 'BORIS VIAN', 45, 55, 45),
          (2021, 'ROGER RUEL', 45, 144, 130),
          (2021, 'LE SACRE COEUR', 45, 79, 75),
          (2021, 'SAINT JOSEPH', 45, 40, 37),
          (2021, 'SAINT DOMINIQUE', 45, 40, 36),
          (2021, "D'YSSINGEAUX", 45, 24, 20),
          (2021, 'DU LIGNON', 45, 43, 39),
          (2021, 'EUGENE J. - YSSINGEAUX', 45, 18, 15),
          (2021, 'LA FAYETTE', 45, 105, 88),
          (2021, 'DE STE FLORINE', 45, 8, 6),
          (2021, 'LA CHARTREUSE', 45, 49, 47),
          (2021, 'ANNE FRANK', 45, 54, 52),
          (2021, 'EMMANUEL CHABRIER', 45, 23, 18),
          (2021, 'JEAN MONNET', 45, 22, 20),
          (2021, 'NOTRE DAME', 45, 22, 21),
          (2021, "JEANNE D'ARC", 45, 90, 88),
          (2021, 'SAINT JOSEPH', 45, 47, 47),
          (2021, 'PARADIS', 45, 11, 8),
          (2021, 'JEAN MONNET', 45, 121, 115),
          (2021, 'SAINT REGIS', 45, 97, 97),
          (2021, 'DE VALS PRES LE PUY', 45, 16, 11),
          (2021, 'LA FAYETTE', 45, 10, 8),
          (2021, 'MARGUERITE THOMAS', 45, 48, 42),
          (2021, 'JOACHIM BARRANDE', 45, 17, 17),
          (2021, 'DE LA LIONCHERE', 45, 39, 38),
          (2021, 'JULES VALLES', 45, 137, 123),
          (2021, 'NOTRE DAME DE LA FAYE', 45, 54, 54),
          (2021, 'SAINTE BERNADETTE', 45, 12, 11),
          (2021, 'SAINT-MARTIN', 45, 41, 38),
          (2021, 'ALEXANDRE VIALATTE', 45, 6, 6),
          (2021, 'DE FONTANNES', 45, 14, 13),
          (2021, 'LE MONTEIL', 45, 167, 148),
          (2021, 'NOTRE DAME DU CHATEAU', 45, 166, 163),
          (2021, 'SAINT-GABRIEL', 45, 72, 72),
          (2021, 'DU MONT BAR', 45, 58, 58),
          (2021, 'DES FONTILLES', 45, 19, 19),
          (2021, "DES HAUTS DE L'ARZON", 45, 48, 46),
          (2021, 'ROBERT LOUIS STEVENSON', 45, 39, 35),
          (2021, 'LA FAYETTE', 45, 98, 81),
          (2021, 'JULES ROMAINS', 45, 92, 90),
          (2021, 'SACRE COEUR', 45, 73, 73),
          (2021, 'ANNE MARIE MARTEL', 45, 17, 13),
          (2021, 'SAINT JULIEN', 45, 98, 92),
          (2021, 'DES GORGES DE LA LOIRE', 45, 72, 65),
          (2021, 'SAINT-LOUIS', 45, 69, 69)]

liste4 = [(2008, "JEANNE D'ARC", 45, 71, 67),
          (2012, "ALBERT SIDOISNE", 28, 98, 78),
          (2016, "JEAN MONNET", 37, 115, 109),
          (2020, 'ALBERT SIDOISNE', 28, 134, 118),
          (2020, 'MATHURIN REGNIER', 28, 152, 118),
          ]

liste5 = [(2006, 'AUGUSTE AYMARD', 45, 24, 12), 
          (2006, 'BONNEFONT', 45, 22, 22), 
          (2006, 'CEVENOL', 45, 46, 33), 
          (2006, 'CHAZOURNES', 45, 19, 15), 
          (2006, 'CLAUDE FAVARD', 45, 22, 19), 
          (2006, 'DE CORSAC', 45, 64, 52), 
          (2006, 'DE LA LIONCHERE', 45, 37, 31), 
          (2006, 'DES FONTILLES', 45, 16, 15), 
          (2006, "DES HAUTS DE L'ARZON", 45, 37, 31), 
          (2006, 'DU HAUT ALLIER', 45, 53, 37), 
          (2006, 'DU LIGNON', 45, 26, 20), 
          (2006, 'DU MONT BAR', 45, 41, 37), 
          (2006, 'DU SACRE COEUR', 45, 31, 25), 
          (2006, 'HENRI POURRAT', 45, 16, 12), 
          (2006, 'ISVT ST DOMINIQUE VALS', 45, 27, 23), 
          (2006, 'JEAN MONNET', 45, 23, 22), 
          (2006, "JEANNE D'ARC", 45, 69, 66), 
          (2006, 'JOACHIM BARRANDE', 45, 24, 18), 
          (2006, 'JULES ROMAINS', 45, 71, 66), 
          (2006, 'JULES VALLES', 45, 142, 126), 
          (2006, 'LA BRUYERE', 45, 39, 26), 
          (2006, 'LA CHARTREUSE', 45, 36, 34), 
          (2006, 'LA FAYETTE', 45, 113, 96), 
          (2006, 'LA PRESENTATION', 45, 24, 23), 
          (2006, 'LAURENT EYNAC', 45, 42, 29), 
          (2006, 'LE MONTEIL', 45, 112, 85), 
          (2006, 'LE SACRE COEUR', 45, 71, 65), 
          (2006, 'LYCEE ANNE-MARIE MARTEL', 45, 23, 22), 
          (2006, 'LYCEE EMMANUEL CHABRIER', 45, 23, 21), 
          (2006, 'NOTRE DAME', 45, 32, 31), 
          (2006, 'NOTRE DAME DE LA FAYE', 45, 43, 40), 
          (2006, 'NOTRE DAME DU CHATEAU', 45, 146, 135), 
          (2006, 'PARADIS', 45, 32, 23), 
          (2006, 'ROBERT LOUIS STEVENSON', 45, 47, 38), 
          (2006, 'ROGER RUEL', 45, 86, 80), 
          (2006, 'SACRE COEUR', 45, 54, 47), 
          (2006, 'SAINT DOMINIQUE', 45, 14, 13), 
          (2006, 'SAINT JOSEPH', 45, 29, 22), 
          (2006, 'SAINT JOSEPH LE ROSAIRE', 45, 103, 102), 
          (2006, 'SAINT JULIEN', 45, 73, 67), 
          (2006, 'SAINT PIERRE - SAINTE ANNE', 45, 121, 111), 
          (2006, 'SAINT REGIS', 45, 67, 66), 
          (2006, 'SAINTE BERNADETTE', 45, 19, 13), 
          (2006, 'ST LOUIS NOTRE DAME DE FRANCE', 45, 111, 94), 
          (2006, 'VAL DE SENOUIRE', 45, 40, 39), 
          (2007, 'AUGUSTE AYMARD', 45, 20, 17), 
          (2007, 'BONNEFONT', 45, 18, 15), 
          (2007, 'CEVENOL', 45, 33, 23), 
          (2007, 'CHARLES ET ADRIEN DUPUY', 45, 22, 21), 
          (2007, 'CHAZOURNES', 45, 13, 12), 
          (2007, 'CLAUDE FAVARD', 45, 22, 20), 
          (2007, 'DE CORSAC', 45, 68, 62), 
          (2007, 'DE LA LIONCHERE', 45, 39, 37), 
          (2007, 'DES FONTILLES', 45, 14, 14), 
          (2007, "DES HAUTS DE L'ARZON", 45, 40, 37), 
          (2007, 'DU HAUT ALLIER', 45, 44, 30), 
          (2007, 'DU LIGNON', 45, 32, 26), 
          (2007, 'DU MONT BAR', 45, 41, 31), 
          (2007, 'DU SACRE COEUR', 45, 31, 21), 
          (2007, 'EMMANUEL CHABRIER', 45, 22, 19), 
          (2007, 'HENRI POURRAT', 45, 12, 9), 
          (2007, 'ISVT ST DOMINIQUE VALS', 45, 18, 13), 
          (2007, 'JEAN MONNET', 45, 25, 21), 
          (2007, "JEANNE D'ARC", 45, 51, 49), 
          (2007, 'JOACHIM BARRANDE', 45, 22, 20), 
          (2007, 'JULES ROMAINS', 45, 71, 59), 
          (2007, 'JULES VALLES', 45, 160, 155), 
          (2007, 'LA BRUYERE', 45, 22, 16), 
          (2007, 'LA CHARTREUSE', 45, 40, 34), 
          (2007, 'LA FAYETTE', 45, 102, 88), 
          (2007, 'LA PRESENTATION', 45, 20, 20), 
          (2007, 'LAURENT EYNAC', 45, 40, 33), 
          (2007, 'LE MONTEIL', 45, 118, 100), 
          (2007, 'LE SACRE COEUR', 45, 66, 65), 
          (2007, 'LYCEE ANNE-MARIE MARTEL', 45, 23, 22), 
          (2007, 'NOTRE DAME', 45, 28, 28), 
          (2007, 'NOTRE DAME DE LA FAYE', 45, 64, 61), 
          (2007, 'NOTRE DAME DU CHATEAU', 45, 148, 140), 
          (2007, 'PARADIS', 45, 22, 14), 
          (2007, 'ROBERT LOUIS STEVENSON', 45, 39, 33), 
          (2007, 'ROGER RUEL', 45, 86, 73), 
          (2007, 'SACRE COEUR', 45, 47, 46), 
          (2007, 'SAINT DOMINIQUE', 45, 36, 31), 
          (2007, 'SAINT JOSEPH', 45, 27, 24), 
          (2007, 'SAINT JOSEPH LE ROSAIRE', 45, 82, 78), 
          (2007, 'SAINT JULIEN', 45, 63, 58), 
          (2007, 'SAINT PIERRE - SAINTE ANNE', 45, 104, 92), 
          (2007, 'SAINT REGIS', 45, 63, 63), 
          (2007, 'SAINTE BERNADETTE', 45, 35, 28), 
          (2007, 'ST LOUIS NOTRE DAME DE FRANCE', 45, 80, 63), 
          (2007, 'VAL DE SENOUIRE', 45, 28, 26), 
          (2008, 'AUGUSTE AYMARD', 45, 19, 17), 
          (2008, 'BONNEFONT', 45, 16, 14), 
          (2008, 'CEVENOL', 45, 28, 19), 
          (2008, 'CHARLES ET ADRIEN DUPUY', 45, 19, 18), 
          (2008, 'CHAZOURNES', 45, 26, 22), 
          (2008, 'CLAUDE FAVARD', 45, 22, 21), 
          (2008, 'DE CORSAC', 45, 71, 60), 
          (2008, 'DE LA LIONCHERE', 45, 45, 41), 
          (2008, 'DES FONTILLES', 45, 17, 15), 
          (2008, "DES HAUTS DE L'ARZON", 45, 33, 32), 
          (2008, 'DU HAUT ALLIER', 45, 50, 44), 
          (2008, 'DU LIGNON', 45, 30, 24), 
          (2008, 'DU MONT BAR', 45, 40, 35), 
          (2008, 'DU SACRE COEUR', 45, 33, 30), 
          (2008, 'EMMANUEL CHABRIER', 45, 23, 20), 
          (2008, 'HENRI POURRAT', 45, 18, 18), 
          (2008, 'ISVT ST DOMINIQUE VALS', 45, 19, 13), 
          (2008, 'JEAN MONNET', 45, 54, 46), 
          (2008, "JEANNE D'ARC", 45, 71, 67), 
          (2008, 'JOACHIM BARRANDE', 45, 15, 14), 
          (2008, 'JULES ROMAINS', 45, 65, 52), 
          (2008, 'JULES VALLES', 45, 180, 159), 
          (2008, 'LA BRUYERE', 45, 29, 17), 
          (2008, 'LA CHARTREUSE', 45, 22, 22), 
          (2008, 'LA FAYETTE', 45, 96, 81), 
          (2008, 'LA PRESENTATION', 45, 17, 17), 
          (2008, 'LAURENT EYNAC', 45, 37, 33), 
          (2008, 'LE MONTEIL', 45, 96, 83), 
          (2008, 'LE SACRE COEUR', 45, 64, 61), 
          (2008, 'LPO ANNE-MARIE MARTEL', 45, 24, 23), 
          (2008, 'NOTRE DAME', 45, 29, 22), 
          (2008, 'NOTRE DAME DE LA FAYE', 45, 48, 47), 
          (2008, 'NOTRE DAME DU CHATEAU', 45, 147, 132), 
          (2008, 'PARADIS', 45, 24, 15), 
          (2008, 'ROBERT LOUIS STEVENSON', 45, 40, 31), 
          (2008, 'ROGER RUEL', 45, 108, 98), 
          (2008, 'SACRE COEUR', 45, 53, 50), 
          (2008, 'SAINT DOMINIQUE', 45, 18, 15), 
          (2008, 'SAINT JOSEPH', 45, 33, 26), 
          (2008, 'SAINT JOSEPH LE ROSAIRE', 45, 82, 79), 
          (2008, 'SAINT JULIEN', 45, 56, 55), 
          (2008, 'SAINT PIERRE - SAINTE ANNE', 45, 116, 101), 
          (2008, 'SAINT REGIS', 45, 70, 70), 
          (2008, 'SAINTE BERNADETTE', 45, 35, 31), 
          (2008, 'ST LOUIS NOTRE DAME DE FRANCE', 45, 57, 47), 
          (2008, 'VAL DE SENOUIRE', 45, 32, 26), 
          (2009, 'AUGUSTE AYMARD', 45, 12, 8), 
          (2009, 'BONNEFONT', 45, 14, 10), 
          (2009, 'BORIS VIAN', 45, 59, 45), 
          (2009, 'CEVENOL', 45, 18, 14), 
          (2009, 'CHARLES ET ADRIEN DUPUY', 45, 19, 14), 
          (2009, 'CHAZOURNES', 45, 21, 18), 
          (2009, 'CLAUDE FAVARD', 45, 22, 21), 
          (2009, 'DE CORSAC', 45, 81, 67), 
          (2009, 'DE LA LIONCHERE', 45, 33, 31), 
          (2009, 'DES FONTILLES', 45, 9, 9), 
          (2009, "DES HAUTS DE L'ARZON", 45, 38, 37), 
          (2009, 'DU HAUT ALLIER', 45, 42, 42), 
          (2009, 'DU LIGNON', 45, 45, 42), 
          (2009, 'DU MONT BAR', 45, 42, 40), 
          (2009, 'DU SACRE COEUR', 45, 34, 34), 
          (2009, 'EMMANUEL CHABRIER', 45, 18, 17), 
          (2009, 'HENRI POURRAT', 45, 14, 14), 
          (2009, 'ISVT ST DOMINIQUE VALS', 45, 22, 15), 
          (2009, 'JEAN MONNET', 45, 21, 19), 
          (2009, "JEANNE D'ARC", 45, 73, 69), 
          (2009, 'JOACHIM BARRANDE', 45, 17, 15), 
          (2009, 'JULES ROMAINS', 45, 66, 56), 
          (2009, 'JULES VALLES', 45, 156, 133), 
          (2009, 'LA CHARTREUSE', 45, 27, 20), 
          (2009, 'LA FAYETTE', 45, 84, 68), 
          (2009, 'LA PRESENTATION', 45, 23, 23), 
          (2009, 'LAURENT EYNAC', 45, 38, 34), 
          (2009, 'LE MONTEIL', 45, 98, 83), 
          (2009, 'LE SACRE COEUR', 45, 69, 67), 
          (2009, 'LPO ANNE-MARIE MARTEL', 45, 21, 19), 
          (2009, 'NOTRE DAME', 45, 27, 25), 
          (2009, 'NOTRE DAME DE LA FAYE', 45, 47, 47), 
          (2009, 'NOTRE DAME DU CHATEAU', 45, 127, 119), 
          (2009, 'PARADIS', 45, 20, 14), 
          (2009, 'ROBERT LOUIS STEVENSON', 45, 38, 34), 
          (2009, 'ROGER RUEL', 45, 92, 80), 
          (2009, 'SACRE COEUR', 45, 63, 60), 
          (2009, 'SAINT DOMINIQUE', 45, 15, 14), 
          (2009, 'SAINT JOSEPH', 45, 20, 19), 
          (2009, 'SAINT JOSEPH LE ROSAIRE', 45, 88, 86), 
          (2009, 'SAINT JULIEN', 45, 69, 62), 
          (2009, 'SAINT PIERRE - SAINTE ANNE', 45, 100, 90), 
          (2009, 'SAINT REGIS', 45, 73, 73), 
          (2009, 'SAINTE BERNADETTE', 45, 25, 20), 
          (2009, 'ST LOUIS NOTRE DAME DE FRANCE', 45, 61, 52), 
          (2009, 'VAL DE SENOUIRE', 45, 30, 26), 
          (2010, 'ANNE MARIE MARTEL', 45, 19, 19), 
          (2010, 'AUGUSTE AYMARD', 45, 15, 12), 
          (2010, 'BONNEFONT', 45, 12, 12), 
          (2010, 'BORIS VIAN', 45, 50, 44), 
          (2010, 'CEVENOL', 45, 20, 15), 
          (2010, 'CHAZOURNES', 45, 28, 24), 
          (2010, 'CLAUDE FAVARD', 45, 22, 22), 
          (2010, 'DE CORSAC', 45, 78, 73), 
          (2010, 'DE LA LIONCHERE', 45, 33, 31), 
          (2010, 'DES FONTILLES', 45, 9, 9), 
          (2010, "DES HAUTS DE L'ARZON", 45, 36, 32), 
          (2010, 'DU HAUT ALLIER', 45, 45, 45), 
          (2010, 'DU LIGNON', 45, 30, 29), 
          (2010, 'DU MONT BAR', 45, 40, 38), 
          (2010, 'DU SACRE COEUR', 45, 27, 26), 
          (2010, 'EMMANUEL CHABRIER', 45, 23, 23), 
          (2010, 'HENRI POURRAT', 45, 15, 13), 
          (2010, 'ISVT ST DOMINIQUE VALS', 45, 18, 13), 
          (2010, 'JEAN MONNET', 45, 24, 24), 
          (2010, "JEANNE D'ARC", 45, 75, 75), 
          (2010, 'JOACHIM BARRANDE', 45, 34, 33), 
          (2010, 'JULES ROMAINS', 45, 75, 72), 
          (2010, 'JULES VALLES', 45, 150, 132), 
          (2010, 'LA CHARTREUSE', 45, 23, 18), 
          (2010, 'LA FAYETTE', 45, 79, 71), 
          (2010, 'LA PRESENTATION', 45, 26, 26), 
          (2010, 'LAURENT EYNAC', 45, 42, 41), 
          (2010, 'LE MONTEIL', 45, 124, 110), 
          (2010, 'LE SACRE COEUR', 45, 67, 64), 
          (2010, 'LPO CHARLES ET ADRIEN DUPUY', 45, 18, 15), 
          (2010, 'MARGUERITE THOMAS', 45, 46, 35), 
          (2010, 'NOTRE DAME', 45, 30, 30), 
          (2010, 'NOTRE DAME DE LA FAYE', 45, 76, 75), 
          (2010, 'NOTRE DAME DU CHATEAU', 45, 132, 128), 
          (2010, 'PARADIS', 45, 21, 19), 
          (2010, 'ROBERT LOUIS STEVENSON', 45, 42, 38), 
          (2010, 'ROGER RUEL', 45, 101, 90), 
          (2010, 'SACRE COEUR', 45, 52, 45), 
          (2010, 'SAINT DOMINIQUE', 45, 22, 22), 
          (2010, 'SAINT JOSEPH', 45, 29, 26), 
          (2010, 'SAINT JOSEPH LE ROSAIRE', 45, 74, 72), 
          (2010, 'SAINT JULIEN', 45, 72, 64), 
          (2010, 'SAINT PIERRE - SAINTE ANNE', 45, 107, 97), 
          (2010, 'SAINT REGIS', 45, 72, 72), 
          (2010, 'SAINTE BERNADETTE', 45, 16, 13), 
          (2010, 'ST LOUIS NOTRE DAME DE FRANCE', 45, 66, 64), 
          (2010, 'VAL DE SENOUIRE', 45, 30, 29), 
          (2011, 'ANNE MARIE MARTEL', 45, 18, 18), 
          (2011, 'AUGUSTE AYMARD', 45, 11, 4), 
          (2011, 'BONNEFONT', 45, 12, 10), 
          (2011, 'BORIS VIAN', 45, 84, 76), 
          (2011, 'CEVENOL', 45, 21, 15), 
          (2011, 'CHARLES ET ADRIEN DUPUY', 45, 20, 18), 
          (2011, 'CLAUDE FAVARD', 45, 23, 19), 
          (2011, 'DE CORSAC', 45, 69, 62), 
          (2011, 'DE LA LIONCHERE', 45, 45, 34), 
          (2011, 'DES FONTILLES', 45, 12, 12), 
          (2011, 'DES GORGES DE LA LOIRE', 45, 38, 30), 
          (2011, "DES HAUTS DE L'ARZON", 45, 36, 30), 
          (2011, 'DU HAUT ALLIER', 45, 48, 46), 
          (2011, 'DU LIGNON', 45, 40, 35), 
          (2011, 'DU MONT BAR', 45, 58, 50), 
          (2011, 'DU SACRE COEUR', 45, 34, 33), 
          (2011, 'EMMANUEL CHABRIER', 45, 22, 21), 
          (2011, 'HENRI POURRAT', 45, 21, 17), 
          (2011, 'ISVT ST DOMINIQUE VALS', 45, 20, 13), 
          (2011, 'JEAN MONNET', 45, 20, 17), 
          (2011, "JEANNE D'ARC", 45, 65, 65), 
          (2011, 'JOACHIM BARRANDE', 45, 18, 16), 
          (2011, 'JULES ROMAINS', 45, 74, 69), 
          (2011, 'JULES VALLES', 45, 163, 149), 
          (2011, 'LA CHARTREUSE', 45, 22, 21), 
          (2011, 'LA FAYETTE', 45, 112, 103), 
          (2011, 'LA PRESENTATION', 45, 20, 20), 
          (2011, 'LAURENT EYNAC', 45, 34, 31), 
          (2011, 'LE MONTEIL', 45, 142, 120), 
          (2011, 'LE SACRE COEUR', 45, 71, 67), 
          (2011, 'MARGUERITE THOMAS', 45, 49, 44), 
          (2011, 'NOTRE DAME', 45, 30, 27), 
          (2011, 'NOTRE DAME DE LA FAYE', 45, 63, 53), 
          (2011, 'NOTRE DAME DU CHATEAU', 45, 121, 114), 
          (2011, 'PARADIS', 45, 14, 12), 
          (2011, 'ROBERT LOUIS STEVENSON', 45, 35, 28), 
          (2011, 'ROGER RUEL', 45, 108, 96), 
          (2011, 'SACRE COEUR', 45, 49, 49), 
          (2011, 'SAINT DOMINIQUE', 45, 20, 19), 
          (2011, 'SAINT JOSEPH', 45, 33, 30), 
          (2011, 'SAINT JOSEPH LE ROSAIRE', 45, 66, 62), 
          (2011, 'SAINT JULIEN', 45, 73, 71), 
          (2011, 'SAINT PIERRE - SAINTE ANNE', 45, 99, 99), 
          (2011, 'SAINT REGIS', 45, 70, 70), 
          (2011, 'SAINT-LOUIS - LES CHARTREUX', 45, 60, 54), 
          (2011, 'SAINTE BERNADETTE', 45, 13, 10), 
          (2011, 'VAL DE SENOUIRE', 45, 29, 27), 
          (2012, 'ANNE MARIE MARTEL', 45, 22, 13), 
          (2012, 'AUGUSTE AYMARD', 45, 16, 14), 
          (2012, 'BONNEFONT', 45, 16, 12), 
          (2012, 'BORIS VIAN', 45, 74, 64), 
          (2012, 'CEVENOL', 45, 16, 10), 
          (2012, 'CHARLES ET ADRIEN DUPUY', 45, 19, 12), 
          (2012, 'CLAUDE FAVARD', 45, 17, 13), 
          (2012, 'DE CORSAC', 45, 67, 62), 
          (2012, 'DE LA LIONCHERE', 45, 42, 41), 
          (2012, 'DES FONTILLES', 45, 18, 18), 
          (2012, 'DES GORGES DE LA LOIRE', 45, 18, 17), 
          (2012, "DES HAUTS DE L'ARZON", 45, 50, 36), 
          (2012, 'DU HAUT ALLIER', 45, 45, 43), 
          (2012, 'DU LIGNON', 45, 35, 32), 
          (2012, 'DU MONT BAR', 45, 45, 40), 
          (2012, 'DU SACRE COEUR', 45, 30, 27), 
          (2012, 'EMMANUEL CHABRIER', 45, 24, 23), 
          (2012, 'HENRI POURRAT', 45, 15, 13), 
          (2012, 'ISVT ST DOMINIQUE VALS', 45, 14, 7), 
          (2012, 'JEAN MONNET', 45, 22, 16), 
          (2012, "JEANNE D'ARC", 45, 57, 52), 
          (2012, 'JOACHIM BARRANDE', 45, 22, 20), 
          (2012, 'JULES ROMAINS', 45, 80, 77), 
          (2012, 'JULES VALLES', 45, 160, 150), 
          (2012, 'LA CHARTREUSE', 45, 28, 25), 
          (2012, 'LA FAYETTE', 45, 115, 101), 
          (2012, 'LA PRESENTATION', 45, 23, 23), 
          (2012, 'LAURENT EYNAC', 45, 35, 35), 
          (2012, 'LE MONTEIL', 45, 134, 121), 
          (2012, 'LE SACRE COEUR', 45, 61, 56), 
          (2012, 'MARGUERITE THOMAS', 45, 64, 54), 
          (2012, 'NOTRE DAME', 45, 25, 22), 
          (2012, 'NOTRE DAME DE LA FAYE', 45, 70, 67), 
          (2012, 'NOTRE DAME DU CHATEAU', 45, 153, 147), 
          (2012, 'PARADIS', 45, 22, 21), 
          (2012, 'ROBERT LOUIS STEVENSON', 45, 37, 30), 
          (2012, 'ROGER RUEL', 45, 125, 116), 
          (2012, 'SACRE COEUR', 45, 54, 53), 
          (2012, 'SAINT DOMINIQUE', 45, 21, 18), 
          (2012, 'SAINT JOSEPH', 45, 31, 29), 
          (2012, 'SAINT JOSEPH LE ROSAIRE', 45, 90, 86), 
          (2012, 'SAINT JULIEN', 45, 67, 66), 
          (2012, 'SAINT PIERRE - SAINTE ANNE', 45, 90, 82), 
          (2012, 'SAINT REGIS', 45, 78, 77), 
          (2012, 'SAINT-LOUIS', 45, 56, 50), 
          (2012, 'SAINTE BERNADETTE', 45, 19, 17), 
          (2012, 'VAL DE SENOUIRE', 45, 32, 25), 
          (2013, 'ANNE MARIE MARTEL', 45, 20, 20), 
          (2013, 'BONNEFONT', 45, 13, 11), 
          (2013, 'BORIS VIAN', 45, 83, 73), 
          (2013, 'CEVENOL', 45, 10, 9), 
          (2013, 'CHARLES ET ADRIEN DUPUY', 45, 21, 19), 
          (2013, 'DE CORSAC', 45, 65, 61), 
          (2013, 'DE LA LIONCHERE', 45, 43, 43), 
          (2013, 'DES FONTILLES', 45, 14, 14), 
          (2013, 'DES GORGES DE LA LOIRE', 45, 30, 25), 
          (2013, "DES HAUTS DE L'ARZON", 45, 36, 35), 
          (2013, 'DU HAUT ALLIER', 45, 55, 50), 
          (2013, 'DU LIGNON', 45, 35, 24), 
          (2013, 'DU MONT BAR', 45, 40, 33), 
          (2013, 'DU SACRE COEUR', 45, 27, 23), 
          (2013, 'EMMANUEL CHABRIER', 45, 24, 20), 
          (2013, 'HENRI POURRAT', 45, 17, 14), 
          (2013, 'JEAN MONNET', 45, 91, 68), 
          (2013, "JEANNE D'ARC", 45, 71, 70), 
          (2013, 'JOACHIM BARRANDE', 45, 22, 20), 
          (2013, 'JULES ROMAINS', 45, 79, 70), 
          (2013, 'JULES VALLES', 45, 145, 129), 
          (2013, 'LA CHARTREUSE', 45, 32, 26), 
          (2013, 'LA FAYETTE', 45, 97, 87), 
          (2013, 'LA PRESENTATION', 45, 28, 28), 
          (2013, 'LAURENT EYNAC', 45, 45, 43), 
          (2013, 'LE MONTEIL', 45, 147, 134), 
          (2013, 'LE SACRE COEUR', 45, 74, 65), 
          (2013, 'MARGUERITE THOMAS', 45, 62, 49), 
          (2013, 'NOTRE DAME', 45, 25, 23), 
          (2013, 'NOTRE DAME DE LA FAYE', 45, 69, 64), 
          (2013, 'NOTRE DAME DU CHATEAU', 45, 152, 146), 
          (2013, 'PARADIS', 45, 19, 19), 
          (2013, 'ROBERT LOUIS STEVENSON', 45, 37, 36), 
          (2013, 'ROGER RUEL', 45, 83, 77), 
          (2013, 'SACRE COEUR', 45, 53, 51), 
          (2013, 'SAINT DOMINIQUE', 45, 18, 17), 
          (2013, 'SAINT JOSEPH', 45, 27, 25), 
          (2013, 'SAINT JOSEPH LE ROSAIRE', 45, 85, 84), 
          (2013, 'SAINT JULIEN', 45, 70, 67), 
          (2013, 'SAINT PIERRE - SAINTE ANNE', 45, 97, 92), 
          (2013, 'SAINT REGIS', 45, 70, 69), 
          (2013, 'SAINT-LOUIS', 45, 50, 44), 
          (2013, 'SAINTE BERNADETTE', 45, 16, 12), 
          (2013, "SITE DE VALS DE L'ISVT", 45, 24, 19), 
          (2013, 'STE FLORINE', 45, 19, 8), 
          (2013, 'VAL DE SENOUIRE', 45, 29, 24), 
          (2014, 'ANNE MARIE MARTEL', 45, 18, 18), 
          (2014, 'BONNEFONT', 45, 14, 14), 
          (2014, 'BORIS VIAN', 45, 58, 46), 
          (2014, 'CEVENOL', 45, 5, 5), 
          (2014, 'CHARLES ET ADRIEN DUPUY', 45, 20, 20), 
          (2014, 'DE CORSAC', 45, 75, 67), 
          (2014, 'DE LA LIONCHERE', 45, 64, 57), 
          (2014, 'DES FONTILLES', 45, 7, 7), 
          (2014, 'DES GORGES DE LA LOIRE', 45, 38, 33), 
          (2014, "DES HAUTS DE L'ARZON", 45, 35, 30), 
          (2014, 'DU HAUT ALLIER', 45, 50, 48), 
          (2014, 'DU LIGNON', 45, 32, 23), 
          (2014, 'DU MONT BAR', 45, 70, 60), 
          (2014, 'DU SACRE COEUR', 45, 26, 26), 
          (2014, 'EMMANUEL CHABRIER', 45, 23, 19), 
          (2014, 'HENRI POURRAT', 45, 13, 11), 
          (2014, 'JEAN MONNET', 45, 21, 19), 
          (2014, "JEANNE D'ARC", 45, 79, 77), 
          (2014, 'JOACHIM BARRANDE', 45, 21, 18), 
          (2014, 'JULES ROMAINS', 45, 94, 85), 
          (2014, 'JULES VALLES', 45, 151, 138), 
          (2014, 'LA CHARTREUSE', 45, 39, 34), 
          (2014, 'LA FAYETTE', 45, 118, 103), 
          (2014, 'LA PRESENTATION', 45, 23, 23), 
          (2014, 'LAURENT EYNAC', 45, 51, 50), 
          (2014, 'LE MONTEIL', 45, 179, 152), 
          (2014, 'LE SACRE COEUR', 45, 70, 69), 
          (2014, 'MARGUERITE THOMAS', 45, 68, 55), 
          (2014, 'NOTRE DAME', 45, 19, 19), 
          (2014, 'NOTRE DAME DE LA FAYE', 45, 54, 50), 
          (2014, 'NOTRE DAME DU CHATEAU', 45, 154, 144), 
          (2014, 'PARADIS', 45, 16, 16), 
          (2014, 'ROBERT LOUIS STEVENSON', 45, 36, 30), 
          (2014, 'ROGER RUEL', 45, 117, 115), 
          (2014, 'SACRE COEUR', 45, 55, 53), 
          (2014, 'SAINT DOMINIQUE', 45, 23, 22), 
          (2014, 'SAINT JOSEPH', 45, 29, 28), 
          (2014, 'SAINT JOSEPH LE ROSAIRE', 45, 82, 76), 
          (2014, 'SAINT JULIEN', 45, 81, 78), 
          (2014, 'SAINT PIERRE - SAINTE ANNE', 45, 88, 84), 
          (2014, 'SAINT REGIS', 45, 108, 108), 
          (2014, 'SAINT-LOUIS', 45, 43, 40), 
          (2014, 'SAINTE BERNADETTE', 45, 24, 21), 
          (2014, "SITE DE VALS DE L'ISVT", 45, 22, 16), 
          (2014, 'STE FLORINE', 45, 16, 11), 
          (2014, 'VAL DE SENOUIRE', 45, 32, 26), 
          (2015, 'ANNE MARIE MARTEL', 45, 19, 18), 
          (2015, 'BONNEFONT', 45, 14, 13), 
          (2015, 'BORIS VIAN', 45, 94, 85), 
          (2015, 'CHARLES ET ADRIEN DUPUY', 45, 23, 21), 
          (2015, 'DE CORSAC', 45, 91, 76), 
          (2015, 'DE LA LIONCHERE', 45, 46, 42), 
          (2015, 'DES FONTILLES', 45, 17, 16), 
          (2015, 'DES GORGES DE LA LOIRE', 45, 58, 57), 
          (2015, "DES HAUTS DE L'ARZON", 45, 33, 28), 
          (2015, 'DU HAUT ALLIER', 45, 63, 51), 
          (2015, 'DU LIGNON', 45, 49, 40), 
          (2015, 'DU MONT BAR', 45, 61, 53), 
          (2015, 'EMMANUEL CHABRIER', 45, 23, 19), 
          (2015, 'HENRI POURRAT', 45, 14, 12), 
          (2015, 'ISVT VALS PRES LE PUY', 45, 21, 16), 
          (2015, 'JEAN MONNET', 45, 102, 93), 
          (2015, "JEANNE D'ARC", 45, 71, 67), 
          (2015, 'JOACHIM BARRANDE', 45, 11, 11), 
          (2015, 'JULES ROMAINS', 45, 120, 113), 
          (2015, 'JULES VALLES', 45, 126, 114), 
          (2015, 'LA CHARTREUSE', 45, 49, 47), 
          (2015, 'LA FAYETTE', 45, 112, 103), 
          (2015, 'LA PRESENTATION', 45, 26, 25), 
          (2015, 'LAURENT EYNAC', 45, 65, 64), 
          (2015, 'LE MONTEIL', 45, 154, 140), 
          (2015, 'LE SACRE COEUR', 45, 56, 54), 
          (2015, 'MARGUERITE THOMAS', 45, 43, 35), 
          (2015, 'NOTRE DAME', 45, 27, 27), 
          (2015, 'NOTRE DAME DE LA FAYE', 45, 66, 65), 
          (2015, 'NOTRE DAME DU CHATEAU', 45, 149, 144), 
          (2015, 'PARADIS', 45, 15, 15), 
          (2015, 'ROBERT LOUIS STEVENSON', 45, 52, 45), 
          (2015, 'ROGER RUEL', 45, 115, 108), 
          (2015, 'SACRE COEUR', 45, 61, 59), 
          (2015, 'SAINT DOMINIQUE', 45, 36, 35), 
          (2015, 'SAINT JOSEPH', 45, 33, 30), 
          (2015, 'SAINT JOSEPH LE ROSAIRE', 45, 73, 67), 
          (2015, 'SAINT JULIEN', 45, 79, 71), 
          (2015, 'SAINT PIERRE - SAINTE ANNE', 45, 87, 84), 
          (2015, 'SAINT REGIS', 45, 97, 97), 
          (2015, 'SAINT-LOUIS', 45, 70, 66), 
          (2015, 'SAINT-MARTIN', 45, 30, 30), 
          (2015, 'SAINTE BERNADETTE', 45, 25, 22), 
          (2015, 'STE FLORINE', 45, 16, 9), 
          (2015, 'VAL DE SENOUIRE', 45, 37, 32), 
          (2016, 'ANNE MARIE MARTEL', 45, 24, 20), 
          (2016, 'BONNEFONT', 45, 16, 15), 
          (2016, 'BORIS VIAN', 45, 67, 60), 
          (2016, 'CHARLES ET ADRIEN DUPUY', 45, 23, 14), 
          (2016, 'DE CORSAC', 45, 67, 61), 
          (2016, 'DE LA LIONCHERE', 45, 42, 36), 
          (2016, 'DES FONTILLES', 45, 16, 16), 
          (2016, 'DES GORGES DE LA LOIRE', 45, 62, 57), 
          (2016, "DES HAUTS DE L'ARZON", 45, 46, 43), 
          (2016, 'DU HAUT ALLIER', 45, 68, 64), 
          (2016, 'DU LIGNON', 45, 46, 41), 
          (2016, 'DU MONT BAR', 45, 44, 40), 
          (2016, 'EMMANUEL CHABRIER', 45, 22, 20), 
          (2016, 'HENRI POURRAT', 45, 18, 18), 
          (2016, 'ISVT VALS PRES LE PUY', 45, 15, 13), 
          (2016, 'JEAN MONNET', 45, 23, 20), 
          (2016, "JEANNE D'ARC", 45, 67, 61), 
          (2016, 'JOACHIM BARRANDE', 45, 18, 16), 
          (2016, 'JULES ROMAINS', 45, 98, 95), 
          (2016, 'JULES VALLES', 45, 150, 139), 
          (2016, 'LA CHARTREUSE', 45, 45, 44), 
          (2016, 'LA FAYETTE', 45, 115, 101), 
          (2016, 'LA PRESENTATION', 45, 33, 33), 
          (2016, 'LAURENT EYNAC', 45, 44, 43), 
          (2016, 'LE MONTEIL', 45, 157, 142), 
          (2016, 'LE SACRE COEUR', 45, 74, 71), 
          (2016, 'MARGUERITE THOMAS', 45, 62, 53), 
          (2016, 'NOTRE DAME', 45, 19, 18), 
          (2016, 'NOTRE DAME DE LA FAYE', 45, 60, 57), 
          (2016, 'NOTRE DAME DU CHATEAU', 45, 151, 150), 
          (2016, 'PARADIS', 45, 22, 22), 
          (2016, 'ROBERT LOUIS STEVENSON', 45, 35, 34), 
          (2016, 'ROGER RUEL', 45, 111, 107), 
          (2016, 'SACRE COEUR', 45, 68, 66), 
          (2016, 'SAINT DOMINIQUE', 45, 20, 20), 
          (2016, 'SAINT JOSEPH', 45, 37, 35), 
          (2016, 'SAINT JOSEPH LE ROSAIRE', 45, 78, 75), 
          (2016, 'SAINT JULIEN', 45, 73, 66), 
          (2016, 'SAINT PIERRE - SAINTE ANNE', 45, 70, 69), 
          (2016, 'SAINT REGIS', 45, 74, 74), 
          (2016, 'SAINT-LOUIS', 45, 68, 63), 
          (2016, 'SAINT-MARTIN', 45, 29, 28), 
          (2016, 'SAINTE BERNADETTE', 45, 20, 18), 
          (2016, 'STE FLORINE', 45, 19, 16), 
          (2016, 'VAL DE SENOUIRE', 45, 43, 43), 
          (2017, 'ANNE MARIE MARTEL', 45, 20, 13), 
          (2017, 'BONNEFONT', 45, 15, 15), 
          (2017, 'BORIS VIAN', 45, 73, 68), 
          (2017, 'CHARLES ET ADRIEN DUPUY', 45, 14, 13), 
          (2017, 'DE CORSAC', 45, 82, 79), 
          (2017, 'DE LA LIONCHERE', 45, 32, 32), 
          (2017, 'DES FONTILLES', 45, 9, 6), 
          (2017, 'DES GORGES DE LA LOIRE', 45, 73, 64), 
          (2017, "DES HAUTS DE L'ARZON", 45, 38, 38), 
          (2017, 'DU HAUT ALLIER', 45, 46, 45), 
          (2017, 'DU LIGNON', 45, 47, 42), 
          (2017, 'DU MONT BAR', 45, 38, 37), 
          (2017, 'EMMANUEL CHABRIER', 45, 21, 19), 
          (2017, 'HENRI POURRAT', 45, 10, 10), 
          (2017, 'ISVT VALS PRES LE PUY', 45, 19, 14), 
          (2017, 'JEAN MONNET', 45, 102, 88), 
          (2017, "JEANNE D'ARC", 45, 73, 73), 
          (2017, 'JOACHIM BARRANDE', 45, 20, 19), 
          (2017, 'JULES ROMAINS', 45, 98, 97), 
          (2017, 'JULES VALLES', 45, 130, 121), 
          (2017, 'LA CHARTREUSE', 45, 45, 45), 
          (2017, 'LA FAYETTE', 45, 111, 108), 
          (2017, 'LA PRESENTATION', 45, 32, 32), 
          (2017, 'LAURENT EYNAC', 45, 70, 69), 
          (2017, 'LE MONTEIL', 45, 156, 154), 
          (2017, 'LE SACRE COEUR', 45, 64, 63), 
          (2017, 'MARGUERITE THOMAS', 45, 67, 51), 
          (2017, 'NOTRE DAME', 45, 24, 24), 
          (2017, 'NOTRE DAME DE LA FAYE', 45, 54, 53), 
          (2017, 'NOTRE DAME DU CHATEAU', 45, 128, 124), 
          (2017, 'PARADIS', 45, 14, 14), 
          (2017, 'ROBERT LOUIS STEVENSON', 45, 47, 46), 
          (2017, 'ROGER RUEL', 45, 127, 116), 
          (2017, 'SACRE COEUR', 45, 64, 64), 
          (2017, 'SAINT DOMINIQUE', 45, 25, 25), 
          (2017, 'SAINT JOSEPH', 45, 31, 30), 
          (2017, 'SAINT JOSEPH LE ROSAIRE', 45, 82, 77), 
          (2017, 'SAINT JULIEN', 45, 79, 74), 
          (2017, 'SAINT PIERRE - SAINTE ANNE', 45, 93, 92), 
          (2017, 'SAINT REGIS', 45, 80, 80), 
          (2017, 'SAINT-LOUIS', 45, 67, 65), 
          (2017, 'SAINT-MARTIN', 45, 32, 31), 
          (2017, 'SAINTE BERNADETTE', 45, 15, 10), 
          (2017, 'STE FLORINE', 45, 13, 10), 
          (2017, 'VAL DE SENOUIRE', 45, 26, 18), 
          (2018, 'ANNE MARIE MARTEL', 45, 24, 20), 
          (2018, 'BONNEFONT', 45, 15, 15), 
          (2018, 'BORIS VIAN', 45, 59, 54), 
          (2018, 'CHARLES ET ADRIEN DUPUY', 45, 17, 17), 
          (2018, 'DE CORSAC', 45, 74, 63), 
          (2018, 'DE LA LIONCHERE', 45, 35, 35), 
          (2018, 'DES FONTILLES', 45, 23, 21), 
          (2018, 'DES GORGES DE LA LOIRE', 45, 52, 44), 
          (2018, "DES HAUTS DE L'ARZON", 45, 38, 35), 
          (2018, 'DU HAUT ALLIER', 45, 54, 52), 
          (2018, 'DU LIGNON', 45, 41, 40), 
          (2018, 'DU MONT BAR', 45, 55, 55), 
          (2018, 'EMMANUEL CHABRIER', 45, 24, 24), 
          (2018, 'HENRI POURRAT', 45, 13, 13), 
          (2018, 'ISVT VALS PRES LE PUY', 45, 22, 18), 
          (2018, 'JEAN MONNET', 45, 22, 20), 
          (2018, "JEANNE D'ARC", 45, 73, 71), 
          (2018, 'JOACHIM BARRANDE', 45, 25, 22), 
          (2018, 'JULES ROMAINS', 45, 91, 90), 
          (2018, 'JULES VALLES', 45, 120, 110), 
          (2018, 'LA CHARTREUSE', 45, 48, 46), 
          (2018, 'LA FAYETTE', 45, 103, 90), 
          (2018, 'LA PRESENTATION', 45, 17, 16), 
          (2018, 'LAURENT EYNAC', 45, 58, 56), 
          (2018, 'LE MONTEIL', 45, 167, 152), 
          (2018, 'LE SACRE COEUR', 45, 86, 82), 
          (2018, 'MARGUERITE THOMAS', 45, 68, 62), 
          (2018, 'NOTRE DAME', 45, 25, 23), 
          (2018, 'NOTRE DAME DE LA FAYE', 45, 53, 51), 
          (2018, 'NOTRE DAME DU CHATEAU', 45, 28, 28), 
          (2018, 'PARADIS', 45, 15, 15), 
          (2018, 'ROBERT LOUIS STEVENSON', 45, 44, 42), 
          (2018, 'ROGER RUEL', 45, 147, 133), 
          (2018, 'SACRE COEUR', 45, 56, 54), 
          (2018, 'SAINT DOMINIQUE', 45, 30, 30), 
          (2018, 'SAINT JOSEPH', 45, 37, 35), 
          (2018, 'SAINT JOSEPH LE ROSAIRE', 45, 71, 60), 
          (2018, 'SAINT JULIEN', 45, 78, 70), 
          (2018, 'SAINT PIERRE - SAINTE ANNE', 45, 85, 84), 
          (2018, 'SAINT REGIS', 45, 120, 120), 
          (2018, 'SAINT-LOUIS', 45, 77, 74), 
          (2018, 'SAINT-MARTIN', 45, 34, 33), 
          (2018, 'SAINTE BERNADETTE', 45, 22, 17), 
          (2018, 'STE FLORINE', 45, 5, 5), 
          (2018, 'VAL DE SENOUIRE', 45, 33, 24), 
          (2018, 'YSSINGEAUX', 45, 24, 23), 
          (2019, 'ALEXANDRE VIALATTE', 45, 3, 3), 
          (2019, 'ANNE MARIE MARTEL', 45, 18, 11), 
          (2019, 'BORIS VIAN', 45, 63, 57), 
          (2019, 'CHARLES ET ADRIEN DUPUY', 45, 21, 14), 
          (2019, "D'YSSINGEAUX", 45, 19, 19), 
          (2019, 'DE CORSAC', 45, 67, 61), 
          (2019, 'DE FONTANNES', 45, 14, 11), 
          (2019, 'DE LA LIONCHERE', 45, 32, 32), 
          (2019, 'DE STE FLORINE', 45, 14, 9), 
          (2019, 'DE VALS PRES LE PUY', 45, 19, 15), 
          (2019, 'DES FONTILLES', 45, 15, 15), 
          (2019, 'DES GORGES DE LA LOIRE', 45, 60, 51), 
          (2019, "DES HAUTS DE L'ARZON", 45, 31, 29), 
          (2019, 'DU HAUT ALLIER', 45, 39, 33), 
          (2019, 'DU LIGNON', 45, 40, 36), 
          (2019, 'DU MONT BAR', 45, 57, 56), 
          (2019, 'EMMANUEL CHABRIER', 45, 22, 22), 
          (2019, 'EUGENE J. - YSSINGEAUX', 45, 25, 21), 
          (2019, 'HENRI POURRAT', 45, 15, 14), 
          (2019, 'JEAN MONNET', 45, 22, 22), 
          (2019, "JEANNE D'ARC", 45, 64, 61), 
          (2019, 'JOACHIM BARRANDE', 45, 22, 20), 
          (2019, 'JULES ROMAINS', 45, 101, 99), 
          (2019, 'JULES VALLES', 45, 108, 93), 
          (2019, 'LA CHARTREUSE', 45, 56, 54), 
          (2019, 'LA FAYETTE', 45, 105, 100), 
          (2019, 'LA PRESENTATION', 45, 29, 27), 
          (2019, 'LAURENT EYNAC', 45, 75, 74), 
          (2019, 'LE MONTEIL', 45, 135, 120), 
          (2019, 'LE SACRE COEUR', 45, 71, 61), 
          (2019, 'MARGUERITE THOMAS', 45, 45, 40), 
          (2019, 'NOTRE DAME', 45, 26, 23), 
          (2019, 'NOTRE DAME DE LA FAYE', 45, 69, 67), 
          (2019, 'NOTRE DAME DU CHATEAU', 45, 28, 26), 
          (2019, 'PARADIS', 45, 18, 18), 
          (2019, 'ROBERT LOUIS STEVENSON', 45, 59, 56), 
          (2019, 'ROGER RUEL', 45, 138, 123), 
          (2019, 'SACRE COEUR', 45, 64, 63), 
          (2019, 'SAINT DOMINIQUE', 45, 25, 24), 
          (2019, 'SAINT JOSEPH', 45, 45, 43), 
          (2019, 'SAINT JOSEPH LE ROSAIRE', 45, 66, 59), 
          (2019, 'SAINT JULIEN', 45, 70, 62), 
          (2019, 'SAINT REGIS', 45, 98, 98), 
          (2019, 'SAINT-GABRIEL', 45, 89, 89), 
          (2019, 'SAINT-LOUIS', 45, 83, 83), 
          (2019, 'SAINT-MARTIN', 45, 34, 32), 
          (2019, 'SAINTE BERNADETTE', 45, 16, 16), 
          (2019, 'VAL DE SENOUIRE', 45, 30, 25), 
          (2020, 'ALEXANDRE VIALATTE', 45, 8, 8), 
          (2020, 'ANNE MARIE MARTEL', 45, 14, 12), 
          (2020, 'BORIS VIAN', 45, 65, 55), 
          (2020, 'CHARLES ET ADRIEN DUPUY', 45, 19, 17), 
          (2020, "D'YSSINGEAUX", 45, 23, 23), 
          (2020, 'DE CORSAC', 45, 78, 73), 
          (2020, 'DE FONTANNES', 45, 15, 15), 
          (2020, 'DE LA LIONCHERE', 45, 45, 39), 
          (2020, 'DE STE FLORINE', 45, 15, 10), 
          (2020, 'DE VALS PRES LE PUY', 45, 19, 16), 
          (2020, 'DES FONTILLES', 45, 10, 9), 
          (2020, 'DES GORGES DE LA LOIRE', 45, 77, 59), 
          (2020, "DES HAUTS DE L'ARZON", 45, 38, 33), 
          (2020, 'DU HAUT ALLIER', 45, 37, 32), 
          (2020, 'DU LIGNON', 45, 41, 33), 
          (2020, 'DU MONT BAR', 45, 38, 36), 
          (2020, 'EMMANUEL CHABRIER', 45, 24, 23), 
          (2020, 'EUGENE J. - YSSINGEAUX', 45, 22, 18), 
          (2020, 'HENRI POURRAT', 45, 13, 12), 
          (2020, 'JEAN MONNET', 45, 20, 20), 
          (2020, "JEANNE D'ARC", 45, 90, 89), 
          (2020, 'JOACHIM BARRANDE', 45, 13, 13), 
          (2020, 'JULES ROMAINS', 45, 90, 90), 
          (2020, 'JULES VALLES', 45, 155, 132), 
          (2020, 'LA CHARTREUSE', 45, 41, 41), 
          (2020, 'LA FAYETTE', 45, 98, 88), 
          (2020, 'LA PRESENTATION', 45, 25, 25), 
          (2020, 'LAURENT EYNAC', 45, 52, 52), 
          (2020, 'LE MONTEIL', 45, 156, 144), 
          (2020, 'LE SACRE COEUR', 45, 68, 64), 
          (2020, 'MARGUERITE THOMAS', 45, 68, 59), 
          (2020, 'NOTRE DAME', 45, 28, 27), 
          (2020, 'NOTRE DAME DE LA FAYE', 45, 55, 54), 
          (2020, 'NOTRE DAME DU CHATEAU', 45, 166, 166), 
          (2020, 'PARADIS', 45, 17, 16), 
          (2020, 'ROBERT LOUIS STEVENSON', 45, 38, 36), 
          (2020, 'ROGER RUEL', 45, 149, 139), 
          (2020, 'SACRE COEUR', 45, 49, 47), 
          (2020, 'SAINT DOMINIQUE', 45, 26, 25), 
          (2020, 'SAINT JACQUES DE COMPOSTELLE', 45, 55, 51), 
          (2020, 'SAINT JOSEPH', 45, 44, 40), 
          (2020, 'SAINT JULIEN', 45, 90, 87), 
          (2020, 'SAINT REGIS', 45, 108, 108), 
          (2020, 'SAINT-GABRIEL', 45, 89, 86), 
          (2020, 'SAINT-LOUIS', 45, 67, 67), 
          (2020, 'SAINT-MARTIN', 45, 31, 29), 
          (2020, 'SAINTE BERNADETTE', 45, 8, 8), 
          (2020, 'VAL DE SENOUIRE', 45, 35, 33), 
          (2021, 'ALEXANDRE VIALATTE', 45, 6, 6), 
          (2021, 'ANNE FRANK', 45, 54, 52), 
          (2021, 'ANNE MARIE MARTEL', 45, 17, 13), 
          (2021, 'BORIS VIAN', 45, 55, 45), 
          (2021, 'CHARLES ET ADRIEN DUPUY', 45, 13, 5), 
          (2021, "D'YSSINGEAUX", 45, 24, 20), 
          (2021, 'DE FONTANNES', 45, 14, 13), 
          (2021, 'DE LA LIONCHERE', 45, 39, 38), 
          (2021, 'DE STE FLORINE', 45, 8, 6), 
          (2021, 'DE VALS PRES LE PUY', 45, 16, 11), 
          (2021, 'DES FONTILLES', 45, 19, 19), 
          (2021, 'DES GORGES DE LA LOIRE', 45, 72, 65), 
          (2021, "DES HAUTS DE L'ARZON", 45, 48, 46), 
          (2021, 'DU HAUT ALLIER', 45, 54, 49), 
          (2021, 'DU LIGNON', 45, 43, 39), 
          (2021, 'DU MONT BAR', 45, 58, 58), 
          (2021, 'EMMANUEL CHABRIER', 45, 23, 18), 
          (2021, 'EUGENE J. - YSSINGEAUX', 45, 18, 15), 
          (2021, 'HENRI POURRAT', 45, 17, 16), 
          (2021, 'JEAN MONNET', 45, 22, 20), 
          (2021, "JEANNE D'ARC", 45, 90, 88), 
          (2021, 'JOACHIM BARRANDE', 45, 17, 17), 
          (2021, 'JULES ROMAINS', 45, 92, 90), 
          (2021, 'JULES VALLES', 45, 137, 123), 
          (2021, 'LA CHARTREUSE', 45, 49, 47), 
          (2021, 'LA FAYETTE', 45, 105, 88), 
          (2021, 'LA PRESENTATION', 45, 26, 24), 
          (2021, 'LAURENT EYNAC', 45, 59, 52), 
          (2021, 'LE MONTEIL', 45, 167, 148), 
          (2021, 'LE SACRE COEUR', 45, 79, 75), 
          (2021, 'MARGUERITE THOMAS', 45, 48, 42), 
          (2021, 'NOTRE DAME', 45, 22, 21), 
          (2021, 'NOTRE DAME DE LA FAYE', 45, 54, 54), 
          (2021, 'NOTRE DAME DU CHATEAU', 45, 27, 25), 
          (2021, 'PARADIS', 45, 11, 8), 
          (2021, 'ROBERT LOUIS STEVENSON', 45, 39, 35), 
          (2021, 'ROGER RUEL', 45, 144, 130), 
          (2021, 'SACRE COEUR', 45, 73, 73), 
          (2021, 'SAINT DOMINIQUE', 45, 40, 36), 
          (2021, 'SAINT JACQUES DE COMPOSTELLE', 45, 83, 82), 
          (2021, 'SAINT JOSEPH', 45, 40, 37), 
          (2021, 'SAINT JULIEN', 45, 98, 92), 
          (2021, 'SAINT REGIS', 45, 97, 97), 
          (2021, 'SAINT-GABRIEL', 45, 72, 72), 
          (2021, 'SAINT-LOUIS', 45, 69, 69), 
          (2021, 'SAINT-MARTIN', 45, 41, 38), 
          (2021, 'SAINTE BERNADETTE', 45, 12, 11)]

print(plus_longe_periode_amelioration(liste5))

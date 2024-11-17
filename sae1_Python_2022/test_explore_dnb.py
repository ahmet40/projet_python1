import explore_dnb as dnb

# -----------------------------------------------------------------------------------------------------
# fonctions de tests à compléter
# -----------------------------------------------------------------------------------------------------

def test_taux_reussite():
    assert dnb.taux_reussite(dnb.resultat1) == 67/71*100
    assert dnb.taux_reussite(dnb.resultat2) == 78/98*100
    assert dnb.taux_reussite(dnb.resultat3) == 109/115*100
    assert dnb.taux_reussite(()) == None
    

test_taux_reussite()
           
           
def test_meilleur():
    assert dnb.meilleur(dnb.resultat1, dnb.resultat2) == True
    assert dnb.meilleur(dnb.resultat1, dnb.resultat3) == False

test_meilleur()


def test_meilleur_taux_reussite():
    assert dnb.meilleur_taux_reussite(dnb.liste2) == 27/28*100
    assert dnb.meilleur_taux_reussite(dnb.liste3) == 1.0*100

test_meilleur_taux_reussite()

def test_pire_taux_reussite():
    assert dnb.pire_taux_reussite(dnb.liste1) == 47/63*100
    assert dnb.pire_taux_reussite(dnb.liste2) == 15/24*100

test_pire_taux_reussite()    


def test_total_admis_presents():
    assert dnb.total_admis_presents(dnb.liste1) == (476,576)
    assert dnb.total_admis_presents(dnb.liste2) == (922, 1111)

test_total_admis_presents()


def test_filtre_session():
    assert dnb.filtre_session(dnb.liste4, 2020) == [(2020, 'ALBERT SIDOISNE', 28, 134, 118),(2020, 'MATHURIN REGNIER', 28, 152, 118)]
    assert dnb.filtre_session(dnb.liste4, 2018) == []
    
test_filtre_session()
    
def test_filtre_departement():
    assert dnb.filtre_departement(dnb.liste1, 45) == []
    assert dnb.filtre_departement(dnb.liste4, 28) == [(2012, "ALBERT SIDOISNE", 28, 98, 78),(2020, 'ALBERT SIDOISNE', 28, 134, 118),(2020, 'MATHURIN REGNIER', 28, 152, 118)]


test_filtre_departement()



def test_filtre_college():
    assert dnb.filtre_college(dnb.liste1, 'EMILE', 45) == []
    assert dnb.filtre_college(dnb.liste1, 'NERMONT', 28) == [(2020, 'DE NERMONT - CHATEAUDUN', 28, 74, 60),(2020, 'DE NERMONT - NOGENT', 28, 28, 27)]


test_filtre_college()
    

def test_taux_reussite_global():
    assert dnb.taux_reussite_global(dnb.liste1, 2018) == None
    assert dnb.taux_reussite_global(dnb.liste1, 2020) == 476/576*100

test_taux_reussite_global()


def test_moyenne_taux_reussite_college():
    assert dnb.moyenne_taux_reussite_college(dnb.liste1, 'ALBERT SIDOISNE', 28) == 118/134*100
    assert dnb.moyenne_taux_reussite_college(dnb.liste2, 'GILBERT COURTOIS', 28) == (18/22*100+15/24*100)/2


test_moyenne_taux_reussite_college()

def test_meilleur_college():
    assert dnb.meilleur_college(dnb.liste1, 2018) == None
    assert dnb.meilleur_college(dnb.liste2, 2021) == ('JEAN MONNET', 28)

test_meilleur_college()


def test_liste_sessions():
    assert dnb.liste_sessions([]) == []
    assert dnb.liste_sessions(dnb.liste2) == [2020, 2021]
    assert dnb.liste_sessions([(2020, 'ALBERT SIDOISNE', 28, 134, 118),(2005, 'ANATOLE FRANCE', 28, 63, 47),(2018, 'DE NERMONT - CHATEAUDUN', 28, 74, 60),
          (2020, 'DE NERMONT - NOGENT', 28, 28, 27),
          (2000, 'EMILE ZOLA', 28, 103, 88)]) == [2000,2005,2018,2020]

test_liste_sessions()

def test_plus_longue_periode_amelioration():
    assert dnb.plus_longe_periode_amelioration(dnb.liste5) == (2013, 2017)
    assert dnb.plus_longe_periode_amelioration(dnb.liste1) == (2020, 2020)

test_plus_longue_periode_amelioration()
def test_est_bien_triee():
    assert dnb.est_bien_triee(dnb.liste1) == True
    assert dnb.est_bien_triee([]) == True


def test_fusionner_resultats():
    assert dnb.fusionner_resultats(dnb.liste1, dnb.liste2) == [(2020, 'ALBERT SIDOISNE', 28, 134, 118), (2020, 'ALBERT SIDOISNE', 28, 134, 118), (2020, 'ANATOLE FRANCE', 28, 63, 47), (2020, 'ANATOLE FRANCE', 28, 63, 47), (2020, 'DE NERMONT - CHATEAUDUN', 28, 74, 60), (2020, 'DE NERMONT - CHATEAUDUN', 28, 74, 60), (2020, 'DE NERMONT - NOGENT', 28, 28, 27), (2020, 'DE NERMONT - NOGENT', 28, 28, 27), (2020, 'EMILE ZOLA', 28, 103, 88), (2020, 'EMILE ZOLA', 28, 103, 88), (2020, 'GILBERT COURTOIS', 28, 22, 18), (2020, 'GILBERT COURTOIS', 28, 22, 18), (2020, 'MATHURIN REGNIER', 28, 152, 118), (2020, 'MATHURIN REGNIER', 28, 152, 118), (2021, 'DE BEAUMONT LES AUTELS', 28, 37, 34), (2021, 'DE NERMONT - CHATEAUDUN', 28, 71, 60), (2021, 'EMILE ZOLA', 28, 96, 85), (2021, 'GILBERT COURTOIS', 28, 24, 15), (2021, 'JEAN MONNET', 28, 97, 91), (2021, 'LA PAJOTTERIE', 28, 91, 72), (2021, 'ND - LA LOUPE', 28, 12, 9), (2021, 'PIERRE BROSSOLETTE', 28, 93, 70), (2021, 'SULLY', 28, 14, 10)]
    assert dnb.fusionner_resultats(dnb.liste1, []) == dnb.liste1


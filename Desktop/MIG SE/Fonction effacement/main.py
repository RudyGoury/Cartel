# -*- coding: utf-8 -*-
import datetime
from Machine_verif import *
import datetime as dt
from Conso import *
from Gene_verif import *


#initialisation du programme général

def main( origine_de_la_simulation, fin_de_la_simulation, liste_ordres ):
    
    #pour chaque date, on dit si elle correspond ou non à une période d'effacement
    liste_dates_simulation = liste_dates_avec_booleens(origine_de_la_simulation,fin_de_la_simulation)
    #renvoyer  la liste des températures réelles ci-dessous, indicée comme liste_dates_simulation
    #liste_temperatures_sans_effacement = 
    Tint = liste_temperatures_sans_effacement[0]
    liste_temperatures_avec_effacement = []
    liste_matrices = []
    
    conso_chauffage = conso("General_Clim", origine_de_la_simulation, fin_de_la_simulation)																													)
    conso_max_chauffage  = max(conso_chauffage)  
    chauffage = Machine( "Chauffage", conso_max_chauffage, conso_chauffage[0]/conso_max_chauffage, 0.5, True, 0 )
    
    conso_bouilleur = conso("Bouilleur_Friteuses_Vaisselle", origine_de_la_simulation, fin_de_la_simulation)																													)
    conso_max_bouilleur  = max(conso_bouilleur)  
    bouilleur = Machine( "Bouilleur", conso_max_bouilleur, conso_bouilleur[0]/conso_max_bouilleur, 0.5, True, 0 )
    
    conso_splash_battle = conso( "Splash_Battle", origine_de_la_simulation, fin_de_la_simulation)
    conso_max_splash_battle = max(conso_splash_battle)
    splash_battle = Machine( "Splash Battle", conso_max_splash_battle, conso_splash_battle[0]/conso_max_splash_battle, 0.5, True, 0 )
    
    conso_creperie = conso( "Crèperie_Gaufrier_Rotisoire",origine_de_la_simulation, fin_de_la_simulation )
    conso_max_creperie = max(conso_creperie)    
    creperie = Machine( "Creperie", conso_max_creperie, conso_creperie[0]/conso_max_creperie, 0.5, False, 0 )
    
    conso_PC_normal = conso( "PC_Normal",origine_de_la_simulation, fin_de_la_simulation )
    conso_max_PC_normal = max(conso_PC_normal) 
    PC_normal = Machine( "PCnormal", conso_max_PC_normal, conso_PC_normal[0]/conso_max_PC_normal, 0.5, False, 0 )

    #indiquer les périodes d'effacement sur la liste de tuples liste_dates_simulation
    l = []
    for ( (date_debut, Puissance_a_effacer) in liste_ordres ) :   
        l += liste_dates(date_debut, date_debut + dt.timedelta(seconds = 3600) )
    for ( (date, booleen) in liste_dates_simulation ):
        booleen = (date in l)
    
    #compléter les listes températures réelles et simulées, y compris en dehors de la période d'effacement
    #et actualiser la gene de chaque machine avant d'appliquer l'algo d'effacement
    
    for ( (date, booleen) in liste_dates_simulation ):
        if booleen :
            #les fonctions ci-dessous doivent être implémentées précisément (inertie, datetimetotemperature...)
            #on prend la température régnant initialement dans la pièce (on suppose qu'elle a la valeur indiquée dans les relevés)            
            Tint = calcul_temp(datetime_to_temperature_sans_effacement(date), datetime_to_temperature_exterieure(date), chauffage.renvoyerEtat() * chauffage.renvoyerConsoMax() )
            for instance_machine in liste_machines :
                calcul_gene(instance_machine, date, Tint)
            
            (liste_dates, liste_temp_int_simul, matrice) = effacement_main( date_debut, Puissance_a_effacer )
            liste_temperatures_avec_effacement += liste_temp_int_simul
            liste_matrices.append(matrice)
        else :
            #en jouant sur la puissance de chauffage/clim, il faut proposer une solution pour que la température rejoigne son niveau d'avant effacement, et l'implémenter ci-dessous
            #...
            #...
            Tint = calcul_temp()
            liste_temperatures_avec_effacement.append(Tint)

    return (liste_date_simulation, liste_temperatures_avec_effacement, liste_matrices)

origine_de_la_simulation = dt.datetime(15,1,1,0,0)
fin_de_la_simulation = dt.datetime(15,1,4,0,0)
conso_bouilleur = conso("Bouilleur_Friteuses_Vaisselle", origine_de_la_simulation, fin_de_la_simulation)
#main(origine_de_la_simulation,fin_de_la_simulation,[])

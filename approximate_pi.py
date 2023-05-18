#!/usr/bin/env python3
"""Calcule une valeur approchée de pi grâce à la méthode de Monte-Carlo"""

import sys
import random

class ArgumentError(BaseException):
    """Crée une classe d'exception
    """

def monte_carlo(nb_points):
    """ Crée un itérateur de points générés au hasard de coordonnées dans [-1,1]
        ainsi que leur appartenance au cercle inscirt

    Args:
        nb_points (int): nombre d'itérations

    Yields:
        tuple: (x,y,appartenance au cercle)
    """
    for _ in range(nb_points):
        pointx=random.random()*2-1
        pointy=random.random()*2-1
        yield pointx,pointy,(pointx*pointx+pointy*pointy)<=1

def calcule_pi(iter_points,nb_points):
    """ Parcourt un itérateur de points et calcule une valeur approchée de pi
        avec la méthode de Monte Carlo

    Args:
        iter_points (iter): tuples (x,y,appartenance au cercle)
        nb_points (int): nb de points

    Returns:
        float: valeur approchée de pi
    """
    compteur=0
    for point in iter_points:
        if point[2]:
            compteur+=1
    return 4*compteur/nb_points

if __name__=="__main__":
    arguments=sys.argv

    #Vérification des arguments
    if len(arguments)!=2:
        raise ArgumentError("nombre d'arguments incorrect")
    if not arguments[1].isdigit():
        raise TypeError("argument non entier")

    #Calcul et affichage de pi
    ARG=int(arguments[1])
    iter_monte_carlo=monte_carlo(ARG)
    print(calcule_pi(iter_monte_carlo,ARG))

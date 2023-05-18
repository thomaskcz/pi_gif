#!/usr/bin/env python3
"""Génération d'images PPM puis d'un GIF"""

import sys
import subprocess
import approximate_pi as app

class ArgumentError(BaseException):
    """Crée l'exception ArgumentError utilisée si les arguments ne sont pas bon"""

def segment(num,pixel_pointeur,points_ecrases,largeur,epaisseur):
    """ Trace un segment sur la matrice_image et modifie points_ecrases en place
        Position des segment:
             77
            5  6
            5  6
             44
            2  3
            2  3
            P11

    Args:
        num (int): numéro du segment
        pixel_pointeur (list): position du pixel en bas à gauche (P sur le schéma)
        points_ecrases (list): liste de tuples (x,y,couleur)
        largeur (int): largeur d'un caractère (hauteur/2)
        epaisseur (int): épaisseur d'un segment
    """
    if num==1:
        cur_x=pixel_pointeur[0]
        cur_y=pixel_pointeur[1]
        for i in range(largeur):
            for j in range(epaisseur):
                #Les segments se chevauchent dans les coins donc le pixel est peut être déja noir
                if matrice_image[cur_y-j][cur_x+i]!=NOIR:
                    points_ecrases.append((cur_x+i,cur_y-j,matrice_image[cur_y-j][cur_x+i]))
                    matrice_image[cur_y-j][cur_x+i]=NOIR
    elif num==2:
        cur_x=pixel_pointeur[0]
        cur_y=pixel_pointeur[1]
        for i in range(largeur):
            for j in range(epaisseur):
                #Les segments se chevauchent dans les coins donc le pixel est peut être déja noir
                if matrice_image[cur_y-i][cur_x+j]!=NOIR:
                    points_ecrases.append((cur_x+j,cur_y-i,matrice_image[cur_y-i][cur_x+j]))
                    matrice_image[cur_y-i][cur_x+j]=NOIR
    elif num==3:
        cur_x=pixel_pointeur[0]+largeur
        cur_y=pixel_pointeur[1]
        for i in range(largeur):
            for j in range(epaisseur):
                #Les segments se chevauchent dans les coins donc le pixel est peut être déja noir
                if matrice_image[cur_y-i][cur_x-j]!=NOIR:
                    points_ecrases.append((cur_x-j,cur_y-i,matrice_image[cur_y-i][cur_x-j]))
                    matrice_image[cur_y-i][cur_x-j]=NOIR
    elif num==4:
        cur_x=pixel_pointeur[0]
        cur_y=pixel_pointeur[1]-largeur
        for i in range(largeur):
            for j in range(epaisseur):
                #Les segments se chevauchent dans les coins donc le pixel est peut être déja noir
                if matrice_image[cur_y-j][cur_x+i]!=NOIR:
                    points_ecrases.append((cur_x+i,cur_y-j,matrice_image[cur_y-j][cur_x+i]))
                    matrice_image[cur_y-j][cur_x+i]=NOIR
    elif num==5:
        cur_x=pixel_pointeur[0]
        cur_y=pixel_pointeur[1]-largeur
        for i in range(largeur):
            for j in range(epaisseur):
                #Les segments se chevauchent dans les coins donc le pixel est peut être déja noir
                if matrice_image[cur_y-i][cur_x+j]!=NOIR:
                    points_ecrases.append((cur_x+j,cur_y-i,matrice_image[cur_y-i][cur_x+j]))
                    matrice_image[cur_y-i][cur_x+j]=NOIR
    elif num==6:
        cur_x=pixel_pointeur[0]+largeur
        cur_y=pixel_pointeur[1]-largeur
        for i in range(largeur):
            for j in range(epaisseur):
                #Les segments se chevauchent dans les coins donc le pixel est peut être déja noir
                if matrice_image[cur_y-i][cur_x-j]!=NOIR:
                    points_ecrases.append((cur_x-j,cur_y-i,matrice_image[cur_y-i][cur_x-j]))
                    matrice_image[cur_y-i][cur_x-j]=NOIR
    elif num==7:
        cur_x=pixel_pointeur[0]
        cur_y=pixel_pointeur[1]-2*largeur
        for i in range(largeur):
            for j in range(epaisseur):
                #Les segments se chevauchent dans les coins donc le pixel est peut être déja noir
                if matrice_image[cur_y-j][cur_x+i]!=NOIR:
                    points_ecrases.append((cur_x+i,cur_y-j,matrice_image[cur_y-j][cur_x+i]))
                    matrice_image[cur_y-j][cur_x+i]=NOIR


def ecrire_pi(texte_pi):
    """Ecrit texte_pi sur matrice_image et renvoie la liste des points qui ont étés écrasés

    Args:
        texte_pi (str): valeur approchée de pi

    Returns:
        list: liste de tuples (x,y,couleur) correspondant aux points écrasés par l'affichage de pi
    """

    #Définition arbitraire des tailles d'écriture
    largeur=int((TAILLE/(NB_CHIFFRES+1))/3)
    epaisseur=int(TAILLE/200)
    espace=largeur//4
    largeur_ecriture=(NB_CHIFFRES+1)*(largeur+espace)
    pixel_pointeur=[int((TAILLE-largeur_ecriture)/2),int((TAILLE+largeur*2)/2)]
    points_ecrases=[]

    #Ecriture des caractère dans la matrice
    for carac in texte_pi:
        if carac=="0":
            segment(1,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(2,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(3,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(5,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(6,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(7,pixel_pointeur,points_ecrases,largeur,epaisseur)
            pixel_pointeur[0]+=largeur+espace
        elif carac=="1":
            segment(3,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(6,pixel_pointeur,points_ecrases,largeur,epaisseur)
            pixel_pointeur[0]+=largeur+espace
        elif carac=="2":
            segment(1,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(2,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(4,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(6,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(7,pixel_pointeur,points_ecrases,largeur,epaisseur)
            pixel_pointeur[0]+=largeur+espace
        elif carac=="3":
            segment(1,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(3,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(4,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(6,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(7,pixel_pointeur,points_ecrases,largeur,epaisseur)
            pixel_pointeur[0]+=largeur+espace
        elif carac=="4":
            segment(3,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(4,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(5,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(6,pixel_pointeur,points_ecrases,largeur,epaisseur)
            pixel_pointeur[0]+=largeur+espace
        elif carac=="5":
            segment(1,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(3,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(4,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(5,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(7,pixel_pointeur,points_ecrases,largeur,epaisseur)
            pixel_pointeur[0]+=largeur+espace
        elif carac=="6":
            segment(1,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(2,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(3,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(4,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(5,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(7,pixel_pointeur,points_ecrases,largeur,epaisseur)
            pixel_pointeur[0]+=largeur+espace
        elif carac=="7":
            segment(3,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(6,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(7,pixel_pointeur,points_ecrases,largeur,epaisseur)
            pixel_pointeur[0]+=largeur+espace
        elif carac=="8":
            segment(1,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(2,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(3,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(4,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(5,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(6,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(7,pixel_pointeur,points_ecrases,largeur,epaisseur)
            pixel_pointeur[0]+=largeur+espace
        elif carac=="9":
            segment(1,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(3,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(4,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(5,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(6,pixel_pointeur,points_ecrases,largeur,epaisseur)
            segment(7,pixel_pointeur,points_ecrases,largeur,epaisseur)
            pixel_pointeur[0]+=largeur+espace
        else:
            segment(1,pixel_pointeur,points_ecrases,2*epaisseur,2*epaisseur)
            pixel_pointeur[0]+=espace

    return points_ecrases

def generate_ppm_file(num_img,compteur_pi):
    """ Génére une image ppm en utilisant une matrice globale modifiée en place
        Ajoute POINTS_PAR_IMAGE points à la matrice
        Ecrit pi, crée le fichier puis efface pi de la matrice

    Args:
        num_img (int): numéro de l'image dans [0,9]
        compteur_pi (int):  compte le nombre de points dans le cercle
                            après num_img*POINTS_PAR_IMAGE itérations
    """

    #Ajout des nouveaux points la matrice
    for _ in range(POINTS_PAR_IMAGE):
        x,y,test=next(POINTS_ITERABLES)
        x,y=int((x+1)*TAILLE/2),int((y+1)*TAILLE/2)
        if test:
            matrice_image[y][x]=BLEU
            compteur_pi+=1
        else:
            matrice_image[y][x]=ROUGE

    #Calcul et écriture de pi sur la matrice
    pi_float=4*compteur_pi/(num_image+1)/POINTS_PAR_IMAGE
    pi_str=f"{pi_float:.{NB_CHIFFRES}f}"
    points_temp=ecrire_pi(pi_str)

    #Création et écriture du fichier ppm en binaire
    with open(f"img{num_img}_{pi_str[0]}-{pi_str[2:]}.ppm","wb") as image:
        image.write(f"P6 {TAILLE} {TAILLE} 1\n".encode("ascii"))
        for ligne in matrice_image:
            for pixel in ligne:
                image.write(pixel)

    #Suppression de pi sur la matrice
    for x,y,couleur in points_temp:
        matrice_image[y][x]=couleur

    return compteur_pi


def genere_gif(images,fichier_gif):
    """Crée un fichier gif qui tourne en boucle avec une pause de 100 ms.

    Args:
        images (str): nom des images
        fichier_gif (str): nom du gif
    """
    commande=f"convert -delay 100 -loop 0 {images} {fichier_gif}"
    subprocess.run(commande,shell=True,check=True)

if __name__ == "__main__":
    arguments=sys.argv

    #Vérification des arguments
    if len(arguments)!=4:
        raise ArgumentError("nombre d'arguments incorrect")
    TAILLE,NB_POINTS,NB_CHIFFRES=arguments[1],arguments[2],arguments[3]
    if not (TAILLE.isdigit() and NB_POINTS.isdigit() and NB_CHIFFRES.isdigit()):
        raise ValueError("arguments non entiers")
    TAILLE,NB_POINTS,NB_CHIFFRES=int(TAILLE),int(NB_POINTS),int(NB_CHIFFRES)
    if not (TAILLE>=100 and NB_POINTS>=100 and 0<NB_CHIFFRES<6):
        raise ValueError("valeur(s) non authorisée(s)")

    #Définition des variables globales
    ROUGE=b'\x01\x00\x00'
    BLEU=b'\x00\x00\x01'
    BLANC=b'\x01\x01\x01'
    NOIR=b'\x00\x00\x00'
    matrice_image=[[BLANC for i in range(TAILLE)] for j in range(TAILLE)]
    POINTS_ITERABLES=app.monte_carlo(NB_POINTS)
    POINTS_PAR_IMAGE=NB_POINTS//10
    COMPTEUR_PI=0

    #Création des 10 images
    for num_image in range(10):
        COMPTEUR_PI = generate_ppm_file(num_image,COMPTEUR_PI)

    #Création du gif
    genere_gif("*.ppm","pi.gif")

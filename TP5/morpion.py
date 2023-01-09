#-----------------MORPION-----------------#

from tkinter import * 
from tkinter.messagebox import *

#code global#
def Clic(event):
    global joueur,A1,A2,A3,B1,B2,B3,C1,C2,C3,D1,D2,D3,E1,E2,E3,F1,F2,F3
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    
    #Si joueur=1 on met une croix
    if joueur==1:
        if X < 100:
            if Y < 100:
                if A1[0]==2:
                    joueur=0
                    A1[0]=1
                    F1[0]=1
                    Croix(50,50)
                else :
                        showinfo(title='Non',message='la case est deja prise !')
            else :
                if Y < 200:
                    if A1[1]==2:
                        joueur=0
                        A1[1]=1
                        F2[0]=1
                        Croix(50,150)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
                else :
                    if A1[2]==2:
                        joueur=0
                        A1[2]=1
                        F3[0]=1
                        Croix(50,250)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
               
        if X < 200 and X > 100:
            if Y < 100:
                if A2[0]==3:
                    joueur=0
                    A2[0]=1
                    F1[1]=1
                    Croix(150,50)
                else :
                        showinfo(title='Non',message='la case est deja prise !')
            else :
                if Y < 200:
                    if A2[1]==3:
                        joueur=0
                        A2[1]=1
                        F2[1]=1
                        Croix(150,150)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
                else :
                    if A2[2]==3:
                        joueur=0
                        A2[2]=1
                        F3[1]=1
                        Croix(150,250)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
               
        if X < 300 and X > 200:
            if Y < 100:
                if A3[0]==4:
                    joueur=0
                    A3[0]=1
                    F1[2]=1
                    Croix(250,50)
                else :
                        showinfo(title='Non',message='la case est deja prise !')
               
            else :
                if Y < 200:
                    if A3[1]==4:
                        joueur=0
                        A3[1]=1
                        F2[2]=1
                        Croix(250,150)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
                   
                else :
                    if A3[2]==4:
                        joueur=0
                        A3[2]=1
                        F3[2]=1
                        Croix(250,250)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
                   
    #Si joueur=0 et on met un rond
    else:
        if X < 100:
            if Y < 100:
                if A1[0]==2:
                    joueur=1
                    A1[0]=0
                    F1[0]=0
                    Rond(50,50)
                else :
                        showinfo(title='Non',message='la case est deja prise !')
                       
            else :
                if Y < 200:
                    if A1[1]==2:
                        joueur=1
                        A1[1]=0
                        F2[0]=0
                        Rond(50,150)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
                   
                else :
                    if A1[2]==2:
                        joueur=1
                        A1[2]=0
                        F3[0]=0
                        Rond(50,250)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
                   
        if X < 200 and X > 100:
            if Y < 100:
                if A2[0]==3:
                    joueur=1
                    A2[0]=0
                    F1[1]=0
                    Rond(150,50)
                else :
                        showinfo(title='Non',message='la case est deja prise !')
               
            else :
                if Y < 200:
                    if A2[1]==3:
                        joueur=1
                        A2[1]=0
                        F2[1]=0
                        Rond(150,150)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
                   
                else :
                    if A2[2]==3:
                        joueur=1
                        A2[2]=0
                        F3[1]=0
                        Rond(150,250)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
                   
        if X < 300 and X > 200:
            if Y < 100:
                if A3[0]==4:
                    joueur=1
                    A3[0]=0
                    F1[2]=0
                    Rond(250,50)
                else :
                        showinfo(title='Non',message='la case est deja prise !')
            else :
                if Y < 200:
                    if A3[1]==4:
                        joueur=1
                        A3[1]=0
                        F2[2]=0
                        Rond(250,150)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
                   
                else :
                    if A3[2]==4:
                        joueur=1
                        A3[2]=0
                        F3[2]=0
                        Rond(250,250)
                    else :
                        showinfo(title='Non',message='la case est deja prise !')
    

#on créer la fonction pour afficher les ronds
def Rond(x1,y1):
    global A1,A2,A3
    Canvas.create_oval(x1-45,y1-45,x1+45,y1+45)
    Verif()
#on créer la fonction pour afficher les croix
def Croix(x1,y1):
    global A1,A2,A3
    Canvas.create_line(x1-45,y1-45,x1+45,y1+45)
    Canvas.create_line(x1+45,y1-45,x1-45,y1+45)
    Verif()
    
#on affiche le joueur qui a gagner
    if B1 == 3:
        showinfo(title='Gagne',message='Joueur 1 a Gagner !')
    if B2 == 3:
        showinfo(title='Gagne',message='Joueur 2 a Gagner !')
    if B3 == 3:
        showinfo(title='Gagne',message='Joueur 1 a Gagner !')
    if C1 == 3:
        showinfo(title='Gagne',message='Joueur 2 a Gagner !')
    if C2 == 3:
        showinfo(title='Gagne',message='Joueur 1 a Gagner !')
    if C3 == 3:
        showinfo(title='Gagne',message='Joueur 2 a Gagner !')
       
    if A1[0]==1 and A2[1]==1 and A3[2]==1:
        showinfo(title='Gagne',message='Joueur 1 a Gagner !')
    if A1[2]==1 and A2[1]==1 and A3[0]==1:
        showinfo(title='Gagne',message='Joueur 1 a Gagner !')    
   
    if A1[0]==0 and A2[1]==0 and A3[2]==0:
        showinfo(title='Gagne',message='Joueur 2 a Gagner !')
    if A1[2]==0 and A2[1]==0 and A3[0]==0:
        showinfo(title='Gagne',message='Joueur 2 a Gagner !')  
       
    if D1 == 3:
        showinfo(title='Gagne',message='Joueur 1 a Gagner !')
    if D2 == 3:
        showinfo(title='Gagne',message='Joueur 2 a Gagner !')
    if D3 == 3:
        showinfo(title='Gagne',message='Joueur 1 a Gagner !')
    if E1 == 3:
        showinfo(title='Gagne',message='Joueur 2 a Gagner !')
    if E2 == 3:
        showinfo(title='Gagne',message='Joueur 1 a Gagner !')
    if E3 == 3:
        showinfo(title='Gagne',message='Joueur 2 a Gagner !')
    
#on initialise les colones et les lignes ( trouver sur internet pour cause de bug )

B1,B2,B3,C1,C2,C3,D1,D2,D3,E1,E2,E3 = 0,0,0,0,0,0,0,0,0,0,0,0

joueur=1

A1=[2,2,2]
F1=[2,2,2]

A2=[3,3,3]
F2=[3,3,3]

A3=[4,4,4]
F3=[4,4,4]

print(C1)

#construction fenetre principale "Fenetre"#

Fenetre = Tk()
Fenetre.title('Morpion')

#creation d'un canvas#
largeur=300
hauteur=300
Canvas = Canvas(Fenetre, width = largeur, height =hauteur, bg ="white")
# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur une case fera appel a la fonction utilisateur Clic()
Canvas.bind("<Button-1>", Clic)
Canvas.pack(padx =5, pady =5)

#delimitation des colones et des cases

Canvas.create_line(0,100,300,100,fill="black",width=6)

Canvas.create_line(0,200,300,200,fill="black",width=6)

Canvas.create_line(100,300,300,-100000,fill="black",width=6)

Canvas.create_line(200,300,300,-100000,fill="black",width=6)

#construction bouton "quitter"#

Button(Fenetre, text ="Quitter", command = Fenetre.destroy).pack(side=RIGHT,padx=5,pady=5)

#lancement boucle principale#
Fenetre.mainloop()


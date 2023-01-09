# Sujet Dev - Game And Protocol

## 0. Sommaire

- [Sujet Dev - Game And Protocol](#sujet-dev---game-and-protocol)
  - [0. Sommaire](#0-sommaire)
  - [I. Présentation](#i-présentation)
  - [II. Game and protocol](#ii-game-and-protocol)


## I. Présentation

Pour ce Tp dev nous avons besoin de 3 VMs (on les clonera sur une vm déja existante), Une Vm serveur qu'on appelera **"serveur"** et de deux Vms client respectivement appelées **"client1"** et **"client2"**.

Nous avons décidé de prendre comme jeux un Morpion codé en python dont on peut retrouver le code original *[ici](morpion.py).



## II. Game and protocol

Pour éviter de réecrire les programmes sur chaque vm nous allons simplement cloner le repo git utilisé en local sur chaque vm afin d'avoir directement chaque fichier important pour la manipulation :

```


```


--------------------------------------------------------------------------------------------------------------------------------------------------------------

Ensuite, en étant dans la VM du serveur et dans le bon dossier, on va lancer la ligne de commande pour lancer le code python du serveur en précisant l'ip et le port sur lequel on doit se connecter (*[multiconn-server](multiconn-server.py))

```py

python multiconn-server.py 127.0.0.1 65432

```

ensuite dans les deux autres vm client nous devons faire la même manipulation avec l'autre code qui sert pour la connexion des clients au serveur (*[multiconn-client](multiconn-client.py))

```py

python multiconn-client.py 127.0.0.1 65432

```

voila nos deux clients sont connecté au serveur et peuvent maintenant communiquer. Pour cela, elles peuvent envoyer de la data au serveur  sous forme d'un tableau de bytes. Le serveur pourra leur répondre de la même manière. Pour le jeu du morpion, tous les calculs pour :
  
- Créer la grille
- La mettre à jour
- Calculer la case jouée par le joueur

seront gérés côté client grâce aux informations reçues du serveur pour plus de sécurité. Quand aux **règles du jeu**, toutes les vérifications de connexion, de placement (autorisé ou pas) seront gérés par le serveur.
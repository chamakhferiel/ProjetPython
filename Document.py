# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:55:29 2023

@author: Chamakh Feriel
"""
import datetime
# =============== 2.1 : La classe Document ===============
class Document:
    # Initialisation des variables de la classe
    def __init__(self, titre="", auteur="", date=datetime.datetime.now(), url="", texte=""):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte

# =============== 2.2 : REPRESENTATIONS ===============
    # Fonction qui renvoie le texte Ã  afficher lorsqu'on tape repr(classe)
    def __repr__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDate : {self.date}\tURL : {self.url}\tTexte : {self.texte}\tType : {self.getType()}"

    # Fonction qui renvoie le texte Ã  afficher lorsqu'on tape str(classe)
    def __str__(self):
        return f"{self.titre}, par {self.auteur}"

    def getType(self):
        pass
    
    def print(self):
        print("titre :" + self.titre +
              "auteur :"+self.auteur +   
              "url : "+self.url+
              "text :"+self.texte
              )
        
    def  getTitre(self):
         return self.titre
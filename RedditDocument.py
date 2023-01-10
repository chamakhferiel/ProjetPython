# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:58:01 2023

@author: Chamakh Feriel
"""

import Document as Document
import datetime
 
# la classe RedditDocument classe fille de la classe Document
# l'attribut ajouter dans cette classe est le nbcommentaire
class RedditDocument (Document.Document) :
    def __init__(self,titre=None, auteur=None, date=datetime.datetime.now(),
                 url=None, texte=None,nbCommantaire=None):
        Document.Document.__init__(self,titre, auteur, date, url, texte)
        self.__nbCommantaire = nbCommantaire
        
    def  getnbCommantaire(self):
        return self.__nbCommantaire
        
    def print(self):
        Document.Document.print(self)
        print("nbCommantaire :"+str(self.__nbCommantaire))
        
    def getType(self):
         return "RedditDocument"
        
    def  getTitre(self):
         return Document.Document.titre
     
    def  getAuteur(self):
         return self.auteur
     
    def  getDate(self):
         return super().date
     
    def  getUrl(self):
         return super().url
     
    def  getTexte(self):
             return super().texte
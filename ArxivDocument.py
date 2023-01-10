# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:23:37 2023

@author: Chamakh Feriel
"""
import Document as d
import datetime
# la classe ArxivDocument classe fille de la classe Document
# l'attribut ajouter dans cette classe est le co_auteur

class ArxivDocument (d.Document) :
   def __init__(self,titre=None, auteur=None, date=datetime.datetime.now(), url=None, texte=None,co_auteur=None):
       d.Document.__init__(self,titre, auteur, date, url, texte )
       self.__co_auteur = co_auteur
       
   def  getco_auteur(self):
       return self.__co_auteur
       
   def print(self):
       d.Document.print(self)
       print("co_auteur :"+str(self.__co_auteur))
   
   def getType(self):
        return "ArxivDocument"
       
   def  getTitre(self):
        return super().titre
    
   def  getAuteur(self):
        return super().__auteur
    
   def  getDate(self):
        return super().__date
    
   def  getUrl(self):
        return super().__url
    
   def  getTexte(self):
            return super().texte
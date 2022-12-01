# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:28:44 2022

@author: fchamakh
"""

class Document:
    def __init__(self,titre,author,date,url,text):
        self.titre=titre
        self.author=author
        self.date=date
        self.url=url
        self.text=text
    
    def afficher(self):
        print ("le document "+ self.titre+
                " de l'author "+self.author
                +" publie le "+ self.date
                +" url "+self.url
                +" text "+self.text
                )
                
    def __str__(self):
        return ("le document "+ self.titre+
                " de l'author "+self.author
                +" publie le "+ self.date
                +" url "+self.url
                +" text "+self.text
            )
    

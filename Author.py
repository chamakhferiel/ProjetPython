# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:55:01 2023

@author: Chamakh Feriel
"""

class Author:
    def __init__(self, name):
        self.name = name
        self.ndoc = 0
        self.production = []
# =============== 2.5 : ADD ===============

#ajouter un auteur
    def add(self, production):
        self.ndoc += 1
        self.production.append(production)

#afficher un auteur
    def __str__(self):
        return f"Auteur : {self.name}\t# productions : {self.ndoc}"
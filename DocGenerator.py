# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 18:31:53 2023

@author: Chamakh Feriel
"""
from RedditDocument import RedditDocument 
from ArxivDocument import ArxivDocument


# creation d'un patron de conception d’usine (factory pattern)

def DocGenerator():
  @staticmethod
  def factory(type,nom):
      if type=="ArXiv": return ArxivDocument(nom)
      if type=="Reddit": return RedditDocument(nom)
      assert 0 ,"Erreur :" + type
      
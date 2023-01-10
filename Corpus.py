# Correction de G. Poux-Médard, 2021-2022

from Author import Author
from string import punctuation
from singleton import singleton
import pandas as pd
import numpy as n
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from collections import OrderedDict
# =============== 2.7 : CLASSE CORPUS ===============
import re
@singleton
class Corpus:
    def __init__(self, nom):
        self.nom = nom
        self.authors = {}
        self.aut2id = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0

# ajouter un doc au corpus
    def add(self, doc):
        if doc.auteur not in self.aut2id:
            self.naut += 1
            self.authors[self.naut] = Author(doc.auteur)
            self.aut2id[doc.auteur] = self.naut
        self.authors[self.aut2id[doc.auteur]].add(doc.texte)

        self.ndoc += 1
        self.id2doc[self.ndoc] = doc

# =============== 2.8 : REPRESENTATION ===============
    def show(self, n_docs=-1, tri="abc"):
        docs = list(self.id2doc.values())
        if tri == "abc":  # Tri alphabétique
            docs = list(sorted(docs, key=lambda x: x.titre.lower()))[:n_docs]
        elif tri == "123":  # Tri temporel
            docs = list(sorted(docs, key=lambda x: x.date))[:n_docs]

        print("\n".join(list(map(repr, docs))))

    def __repr__(self):
        docs = list(self.id2doc.values())
        docs = list(sorted(docs, key=lambda x: x.titre.lower()))

        return "\n".join(list(map(str, docs)))

    def __reduce__(self):
        return (Corpus, (), self.__dict__)


#la fonction search qui retourne les passages des documents contenant le mot dans le doc 
    def search(self,mot , doc): 
        ch=""
        #retrouver si le mot existe dans le doc
        x=bool(re.search(mot,str(doc)))
        #parcourir le string
        for i in range(len(doc)):
            #retrouver le mot et retrouver sont enplacement
            if doc[i:(i+len(mot))] == mot:
                start=i
                finish=i
                while doc[start] != "." and start != 0:
                    start=start-1
                while doc[start] == "." or doc[start]==" ":
                    start=start+1
                while doc[finish] != "." and finish != len(doc)-1:
                    finish=finish+1
                #retrourne  les passages du mots
                print(doc[start:finish])
                ch = ch + " /t " +doc[start:finish]
        return ch
            
#la fonction concorde qui retourne les parties debut et fin du passer de la mot dans les doc
    def concorde(self,text,keyword,length):
        data = []
        #parcourir le doc
        for i in range(len(text)):
            #chercher le mot 
             if text[i:(i+len(keyword))] == keyword:
                 #recupere la partie avant le mot
                  start=max(i-length,0)
                  #recupere la partie apres le mot
                  finish=min(i+len(keyword)+length,len(text))
                  print(text[start:finish])
                  #retrourne  les passages du mots dans data avec la partie avant le mot ,le mot,la partie apres le mot 
                  data .append([[text[start:start+length]],[keyword],[text[finish-length:finish]]])
        
        print(data)   
        return data
    

    def nettoyer_texte(self,txt):
        #couper le texte en mot 
        tokens = word_tokenize(txt)
        #mettre en minuscule tous les mots dans le tokens
        tokens=[w.lower() for w in tokens]
        #preparer le regex des caracteres a filtr� "ponctuation"
        re_punc = re.compile('[%s]'% re.escape(string.punctuation))
        #supprimer la ponctuation pour chaque mot
        stripped =[re_punc.sub(' ',w) for w in tokens]
        #supprimer la token qui ne sont pas des alphabes
        words =[word for word in stripped if word.isalpha()]
        #filtre les stop_words
        stop_words=set(stopwords.words('english'))
        word=[w for w in words if not w in stop_words]
        #m=txt.lower()
        #c=m.replace("\n"," ")       
        #d=re.sub(r"[0-9\t\n\x0B\f\r,.?;:!@#&$*()]", " ", c) 
        #k=re.sub(r"[^{-\}%]/=", " ", d) 
        
               
        #txt=txt.split()
        #convert list to string
        k=' '.join(word)
        return k
                
        
    def split_frequence(self,txt):
        #coupe le text en mots 
        words=txt.split()
        #cree un OrderedDict
        vocab=OrderedDict()
        #parcourir la liste des mots
        for i in words:
            # chercher si le mot exite dans le dict
            #s'il n'existe pas l'ajouter
            if i not in vocab:
                vocab[i]=1
            #exite : ajouter occurence +1    
            else:
                vocab[i]=vocab[i]+1
        return vocab
    
    def split_frequence_titre(self,txt):
        #coupe le text en mots par symbole ?
        words=txt.split("?")
        #cree un dict
        vocab={}
        #parcourir la liste des mots
        for i in words:
            # chercher si le mot exite dans le dict
            #s'il n'existe pas l'ajouter
            if i not in vocab:
                vocab[i]=1
            #exite : ajouter occurence +1  
            else:
                vocab[i]=vocab[i]+1
        return vocab
    
    def countX(self,lst, x):
        count = 0
        #couper texte en mots
        words=lst.split()
        #calculer l'occurence de chaque mot
        for ele in words:
            if (ele == x):
                count = count + 1
        return count
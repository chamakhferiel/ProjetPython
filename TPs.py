# Correction de G. Poux-Médard, 2021-2022

# =============== PARTIE 1 =============
# =============== 1.1 : REDDIT ===============
# Library
import praw
import numpy as n
# Fonction affichage hiérarchie dict
def showDictStruct(d):
    def recursivePrint(d, i):
        for k in d:
            if isinstance(d[k], dict):
                print("-"*i, k)
                recursivePrint(d[k], i+2)
            else:
                print("-"*i, k, ":", d[k])
    recursivePrint(d, 1)

# Identification
reddit = praw.Reddit(client_id='HbrEWdTC5uiwF418u-g-Vw', client_secret='tB5M19gl_AOTOwNxvehY9h5dHP2HRw', user_agent='scarping')   

# Requête
limit = 100
hot_posts = reddit.subreddit('crypto').hot(limit=limit)

# Récupération du texte
docs = []
docs_bruts = []
afficher_cles = False
for i, post in enumerate(hot_posts):
    if i%10==0: print("Reddit:", i, "/", limit)
    if afficher_cles: 
        for k, v in post.__dict__.items():
            pass
            print(k, ":", v)

    if post.selftext != "":  # Osef des posts sans texte
        pass
        #print(post.selftext)
        docs.append(post.selftext.replace("\n", " "))
        docs_bruts.append(("Reddit", post))

#print(docs)

# =============== 1.2 : ArXiv ===============
# Libraries
import urllib, urllib.request, _collections
import xmltodict

# Paramètres
query_terms = "crypto"
max_results = 50

# Requête
url = f'http://export.arxiv.org/api/query?search_query=all:{"+".join(query_terms)}&start=0&max_results={max_results}'
data = urllib.request.urlopen(url)

# Format dict (OrderedDict)
data = xmltodict.parse(data.read().decode('utf-8'))

#showDictStruct(data)

# Ajout résumés à la liste
for i, entry in enumerate(data["feed"]["entry"]):
    if i%10==0: print("ArXiv:", i, "/", limit)
    docs.append(entry["summary"].replace("\n", ""))
    docs_bruts.append(("ArXiv", entry))
    #showDictStruct(entry)

# =============== 1.3 : Exploitation ===============
#print(f"# docs avec doublons : {len(docs)}")
docs = list(set(docs))
#print(f"# docs sans doublons : {len(docs)}")

for i, doc in enumerate(docs):
    #print(f"Document {i}\t# caractères : {len(doc)}\t# mots : {len(doc.split(' '))}\t# phrases : {len(doc.split('.'))}")
    if len(doc)<100:
        docs.remove(doc)

longueChaineDeCaracteres = " ".join(docs)

# =============== PARTIE 2 =============
# =============== 2.1, 2.2 : CLASSE DOCUMENT ===============
from Document import Document
from RedditDocument import RedditDocument 
from ArxivDocument import ArxivDocument
# =============== 2.3 : MANIPS ===============
import datetime
collection = []
x=""
co_auteur =""
for nature, doc in docs_bruts:
    if nature == "ArXiv":  # Les fichiers de ArXiv ou de Reddit sont pas formatés de la même manière à ce stade.
        #showDictStruct(doc)

        titre = doc["title"].replace('\n', '')  # On enlève les retours à la ligne
        try:
            x = ", ".join([a["name"] for a in doc["author"]])  # On fait une liste d'auteurs, séparés par une virgule
            x_split = x.split(",", 1)
            co_auteur=x_split[1]
           
        except:
            authors = doc["author"]["name"]  # Si l'auteur est seul, pas besoin de liste
        
        
        summary = doc["summary"].replace("\n", "")  # On enlève les retours à la ligne
        date = datetime.datetime.strptime(doc["published"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y/%m/%d")  # Formatage de la date en année/mois/jour avec librairie datetime
        #tous les fichiers se trouve dans doc_classe
        #ajouter un fichier arxiv
        doc_classe = ArxivDocument(titre, authors, date, doc["id"], summary,co_auteur) 
        
        collection.append(doc_classe)  # Ajout du Document à la liste.

    elif nature == "Reddit":
        #print("".join([f"{k}: {v}\n" for k, v in doc.__dict__.items()]))
        titre = doc.title.replace("\n", '')
        auteur = str(doc.author)
        commentaire = len(doc.comments)
        date = datetime.datetime.fromtimestamp(doc.created).strftime("%Y/%m/%d")
        url = "https://www.reddit.com/"+doc.permalink
        texte = doc.selftext.replace("\n", "")
        #nb_commentaire = doc.
        #doc_classe = Document(titre, auteur, date, url, texte)
        
        #tous les fichiers se trouve dans doc_classe
        #ajouter un fichier Reddit
        doc_classe = RedditDocument(titre, auteur, date, url, texte,commentaire)
        
        collection.append(doc_classe)

# Création de l'index de documents
id2doc = {}
for i, doc in enumerate(collection):
    id2doc[i] = doc.titre

# =============== 2.4, 2.5 : CLASSE AUTEURS ===============
from Author import Author

# =============== 2.6 : DICT AUTEURS ===============
authors = {}
aut2id = {}
num_auteurs_vus = 0
liste_doc=[]
# Création de la liste+index des Auteurs
for doc in collection:
    if doc.auteur not in aut2id:
        num_auteurs_vus += 1
        authors[num_auteurs_vus] = Author(doc.auteur)
        aut2id[doc.auteur] = num_auteurs_vus
        liste_doc.append(doc.texte)
    authors[aut2id[doc.auteur]].add(doc.texte)


# =============== 2.7, 2.8 : CORPUS ===============
from Corpus import Corpus
corpus = Corpus("Mon corpus")

# Construction du corpus à partir des documents
for doc in collection:
    corpus.add(doc)
#corpus.show(tri="abc")
#print(repr(corpus))


# =============== 2.9 : SAUVEGARDE ===============
import pickle

# Ouverture d'un fichier, puis écriture avec pickle
with open("corpus.pkl", "wb") as f:
    pickle.dump(corpus, f)

# Supression de la variable "corpus"
del corpus

# Ouverture du fichier, puis lecture avec pickle
with open("corpus.pkl", "rb") as f:
    corpus = pickle.load(f)

# La variable est reapparue
print(corpus.id2doc)
  
# docgenerator   
"""
import DocGenerator

for doc in corpus:
    print(doc.id2doc)
    #pers = DocGenerator.build.factory(choice,"a")
    #pers.print()
"""
#m=input("le mot a cherch�") 
#essai methode search
"""m=corpus.search("ECDH" , corpus.__repr__())
print(m)

#essai methode concorde
m=corpus.concorde(corpus.__repr__(), "ECDH" , 12 )
print(m)

#essai methode nettoyer_texte
d=corpus.nettoyer_texte(corpus.__repr__())

#essai methode split_frequence
vocab = corpus.split_frequence(d)
print(vocab)
"""

# convert liste_doc en string
liste_doc_join = " ".join(liste_doc)

# concatene la liste des titres et la liste des textes 
doc_title_text=longueChaineDeCaracteres+" "+liste_doc_join

# convert la liste des titres et des textes en miniscules
doc_title_text_lower=doc_title_text.lower()
#nettoyer la liste des ponctualtion ...
netoyer=corpus.nettoyer_texte(doc_title_text)

#recuperer l'occurence de chaque mot du texte
vocaba=corpus.split_frequence(netoyer)
#print(type(vocab))
#vocab.sort()
#sorted(vocab.items(), key=lambda t: t[0])

#vocaba.sort()
print(vocaba)
#initialiser la liste
vocab = {}

#parcourir la liste des valeurs et les recuperers tous dans une seule dict
for key in vocaba:
  vocab[key] = vocaba[key] 
keys = list(vocab)
# trier la liste des valeurs
keys.sort()

#cree la matrice 
mat_TF=n.eye(len(collection),len(keys))
print(mat_TF)

#parcourir la matrice et calculer nombre d'occurence de chaque mot dans chaque doc
for i in range(len(collection)):
    collection[i].titre=corpus.nettoyer_texte(collection[i].titre)
    for j in range(len(keys)):
        print(collection[i].titre)
        print(keys[j])
        mat_TF[i][j]= corpus.countX(collection[i].titre,keys[j])
        
#parcourir la matrice et calculer l'occurence de chaque mots dans tous les doc
for j in range(len(keys)):   
    n=0
    for i in range(len(collection)):
        n=n+mat_TF[i][j]
    vocab[keys[j]]=n
  
#initialiser la liste
list_t=[] 
    
#programme principale
wordsINT=input("Entre des mots : /n")

# netoyer la liste des mots entrees par l'utilisateur
wordsINT=corpus.nettoyer_texte(wordsINT)
#couper la liste en mots
list_word=wordsINT.split()
#search(self,mot , doc)
#parcourir la liste des mots
for i in (list_word):
    #chercher le mot dans le dict vocab
    if (i in vocab):
        print("le mot existe dans le dict")
        #chercher le nombre d'occurence dans la liste des titres et des textes
        if (vocab[i] != 0 ):
            print(i,' existe dans notre dictionnaire vocab nb fois: ',vocab[i])
            print('Tous les phrases qui comporte le mot',i)
            #chercher le mot dans le corpus
            m=corpus.search(i , doc_title_text_lower)
            print(m)
            
        j=keys.index(i)
        print(j)
        #collecter les doc ou le mot existe
        for m in range(len(collection)):
            if mat_TF[m][j] != 0 :
                list_t.append(collection[m].titre)
            


#print (les_titres_doc)
print("*****************************")
#chercher si les mots existants deja dans le dict
if len(list_t) == 0:
        print(list_word ,' n existent pas dans notre dictionnaire vocab')
else:
        
        #convert list to string
        list_join = "?".join(list_t)
        #calucler la frequence de chaque doc 
        les_titres_doc=corpus.split_frequence_titre(list_join)
        #afficher le resultat
        print(les_titres_doc)
        #les_titres_doc.
        val=[]
        #cree une liste des valeur 
        for valeur in les_titres_doc.values():
            val.append(valeur)
        
        #val.sort(reverse=True)
        #cree une liste des valeur sans doublant
        val_d = list(set(val))
        #trier la liste 
        val_d.sort(reverse=True)
        print(val_d)
        lister_trier=[]
        # afficher les doc par ordre d'accurences decroissante
        for m in val_d:
            print("les documents suivantes admettant un nombre d'occurence ",m)
            print("**********************************************************")
            for cle, valeur in les_titres_doc.items():
                if valeur == m :
                    print("le document :",cle)
                    print("*****************************")
            
            
        













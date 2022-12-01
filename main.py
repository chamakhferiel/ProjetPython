# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:50:43 2022

@author: fchamakh
"""

import Document as d
import praw
import pandas as pd

reddit= praw.Reddit(client_id='HbrEWdTC5uiwF418u-g-Vw', client_secret='tB5M19gl_AOTOwNxvehY9h5dHP2HRw', user_agent='scarping')   

subr = reddit.subreddit('Coronavirus')
posts = []
posts = pd.DataFrame(posts,columns=['article'])
posts['article'] = posts['article'].str.replace('\n',' ')
print (posts)

doc=[]
for post in subr.hot(limit=100):
    doc =d.Document(post.title,post.author.name,"post.date",post.url,"post.texte")
    print(doc)
   
     
print(doc.__sizeof__())
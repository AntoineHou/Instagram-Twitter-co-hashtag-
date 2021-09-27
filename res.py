# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:14:09 2021

@author: antoi
"""

import pandas as pd 
import networkx as nx
from twitter import *
from insta import *

#Instagram

def Instagram_Dic(Account_Intsagram) :
    webdriver=driver()
    headers=session()
    recent_post=scrap_profile(webdriver,Account_Intsagram,50,headers)
    dictionnary_post_hashtag=hashtag_post(recent_post)
    return dictionnary_post_hashtag

#Twitter 

def Twitter_Dic (Account_Twitter) : 
    api_twitter=load_api()
    twitter_ID=get_id(Account_Twitter,api_twitter)
    tweets=tweet_scrap(twitter_ID,200,api_twitter)
    dictionnary_tweets_hashtags=tweet_parsing(tweets)
    return dictionnary_tweets_hashtags

#Network

def res_creation (Account_Twitter,dictionnary_tweets_hashtags,dictionnary_post_hashtag) :
    G=nx.Graph()
    all_post=dictionnary_tweets_hashtags+dictionnary_post_hashtag
    nodes_set_1_i=[]
    nodes_set_1_t=[]
    nodes_set_2=[]
    for dictionary in all_post :
        for key,value in dictionary.items():
            if str(key)[0] == "1" :
                if key not in nodes_set_1_t : 
                    nodes_set_1_t.append(key)
            else : 
                nodes_set_1_i.append(key)
            if len(value) == 0 : 
                pass 
            else : 
                for v in value : 
                    v=v.lower()
                    if v not in nodes_set_2 :
                        nodes_set_2.append(v)
    G.add_nodes_from(nodes_set_1_i, bipartite=0,platform="Instagram")
    G.add_nodes_from(nodes_set_1_t, bipartite=0,platform="Twitter")
    G.add_nodes_from(nodes_set_2, bipartite=1)
    for dictionary in all_post :
        hashtags=[]
        for key,value in dictionary.items():
            if len(value) == 0 : 
                pass 
            else :
                for values in value :
                    values=values.lower()
                    G.add_edge(key,values)
    return nx.write_gml(G, Account_Twitter+"_"+"Graph.gml")




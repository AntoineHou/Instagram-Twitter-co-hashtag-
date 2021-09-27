# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:41:13 2021

@author: antoi
"""
import networkx as nx 
import os 

files=os.listdir()
networks=[]

for f in files : 
    if "gml" in f : 
        networks.append(f)
    else :
        pass

G=nx.Graph()

for n in networks: 
    a=str(n[:-10]) 
    G_mock = nx.read_gml(n)
    Hashtag_Twitter=[]
    Hashtag_Instagram=[]
    for edges in G_mock.edges(data=True) :
        if G_mock.nodes[edges[0]]["platform"] == "Twitter" :
            Hashtag_Twitter.append(edges[1])  
        else :  
            Hashtag_Instagram.append(edges[1])
    G.add_node(a+"_Instagram", bipartite=0,platform="Instagram")
    G.add_node(a+"_Twitter", bipartite=0,platform="Twitter")
    for hashtag in Hashtag_Twitter :
        if hashtag not in G.nodes : 
            G.add_node(hashtag,bipartite=1)
        else :
            pass 
        e=(a+"_Twitter",hashtag)
        if G.get_edge_data (e,hashtag) == None:
            G.add_edge(a+"_Twitter",hashtag, weight = 1)
        else : 
            w=G.get_edge_data(a+"_Twitter",hashtag)["weight"]+1
            G.add_edge(a+"_Twitter",hashtag, weight = w)
    for hashtag in Hashtag_Instagram :
        if hashtag not in G.nodes : 
            G.add_node(hashtag,bipartite=1)
        else :
            pass 
        e=(a+"_Instagram",hashtag)
        if G.get_edge_data (e,hashtag) == None:
            G.add_edge(a+"_Instagram",hashtag, weight = 1)
        else : 
            w=G.get_edge_data(a+"_Instagram",hashtag)["weight"]+1
            G.add_edge(a+"_Instagramr",hashtag, weight = w)

remove = [node for node,degree in dict(G.degree()).items() if degree < 1]
G.remove_nodes_from(remove)
nx.write_gexf(G,"G_Merged.gexf")    

        

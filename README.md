# # PhD-Interview-Proof-of-concept


This script collects recent Tweets and Instagram for a defined individual and return a bipartite network with, on one side, two nodes representing the individual on each platform and on the other the hashtags used on his posts. 

Different network can then be merged and analyzed/visualized using the output files. 

# What does the script do

 - Collect the last 200 tweets and 50 Instagram posts for the specified accounts  
 - Parse the hashtag and post "identifier" for each Tweets and Instagram post 
 - Create a bipartite network for the specified accounts  
 - Generate a combination of all network saved in the folder : Network merging ; Isolated node deletion etc...

# Analysis and visualization 

When the data generation is done the script return both a **gml** and **gefx** file which allow for analysis and visualization using both python (**Networkx**) and **Gephi**

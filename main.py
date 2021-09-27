# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 08:17:53 2021

@author: antoi
"""

from res2 import * 

if __name__ == '__main__': 
    Account_Intsagram=input("Enter instagram account :")
    Account_Twitter=input("Enter Twitter account :")
    dictionnary_tweets_hashtags=Twitter_Dic(Account_Twitter)
    dictionnary_post_hashtag=Instagram_Dic(Account_Intsagram)
    res_creation(Account_Twitter,dictionnary_tweets_hashtags,dictionnary_post_hashtag)
    print("Network created")
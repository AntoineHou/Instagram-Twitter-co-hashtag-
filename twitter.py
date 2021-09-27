# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 13:47:59 2021

@author: antoi
"""
import tweepy
import re

def load_api():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,parser=tweepy.parsers.JSONParser())

def get_id(screen_name,apit) : 
    user = apit.get_user(screen_name)
    ID = str(user["id"])
    return ID

def tweet_scrap(UsersID, NTweet,apit) : 
    Tweet = apit.user_timeline(UsersID,count=NTweet)
    dic={}
    a=0
    while a != len(Tweet) : 
        dic[str(a)]=Tweet[a]
        a=a+1
    return dic

def tweet_parsing (list_tweet) : 
    list_tweet_parsed=[]
    for tweets in list_tweet.items() :
        identifiant=tweets[1]["id"]
        a=tweets[1]["text"]
        hashtag=re.findall(r"#(\w+)", a)
        post_hashtag={identifiant:hashtag}
        list_tweet_parsed.append(post_hashtag)
    return list_tweet_parsed
        
         

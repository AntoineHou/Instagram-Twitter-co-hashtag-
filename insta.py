# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:59:20 2021

@author: antoi
"""
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from instascrape import Profile , scrape_posts
import re  
import time 

def driver () :
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())    
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(10)
    driver.find_element_by_name("username").send_keys('Flurnne')
    driver.find_element_by_name("password").send_keys('9NfHTyYbiTpt3p4') 
    driver.find_element_by_name("password").send_keys(u'\ue007')
    time.sleep(20)
    return driver    

def session () :
    SESSIONID = input("Session_ID_Cookie:")
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
    "cookie":f'sessionid={SESSIONID};'
    }
    return headers

def scrap_profile(webdriver,profile_name,n_post,headers) :
    profile = Profile(profile_name)
    profile.scrape(headers=headers)
    recents = profile.get_posts(amount=n_post,webdriver=webdriver)
    scraped_posts = scrape_posts(recents, headers=headers, pause=10, silent=False)
    return scraped_posts

def hashtag_post (recent_post) : 
    list_dict=[]
    recent_post=recent_post[0]
    for post in recent_post : 
        a=str(post["caption"])
        hashtag=re.findall(r"#(\w+)", a)
        b=str(post["source"])
        post_hashtag={b:hashtag}
        list_dict.append(post_hashtag)
        time.sleep(5)
    return list_dict
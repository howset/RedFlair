#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 09:59:12 2022

@author: howsetya
"""

import praw
import pandas as pd
 
reddit_read_only = praw.Reddit(client_id="YWkL8bPOfQp5a53s2NI5hg",         # your client id
                               client_secret="DxcXVVs-Lp5fW_io_x71nmINYoqgjg",      # your client secret
                               user_agent="Scraper_one")        # your user agent
 
# reddit_authorized = praw.Reddit(client_id="YWkL8bPOfQp5a53s2NI5hg",         # your client id
#                                 client_secret="DxcXVVs-Lp5fW_io_x71nmINYoqgjg",      # your client secret
#                                 user_agent="Scraper_one",        # your user agent
#                                 username="how11",        # your reddit username
#                                 password="forher14")        # your reddit password

subreddit = reddit_read_only.subreddit("indonesia")
 
print("Display Name:", subreddit.display_name)
print("Title:", subreddit.title)
print("Description:", subreddit.description)

# for post in subreddit.hot(limit=50):
#     print(post.link_flair_text)
#     print()
    
posts = subreddit.hot(limit=999)
 
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": [],
              "Flair": []
              }
 
for post in posts:
    posts_dict["Title"].append(post.title)
    posts_dict["Post Text"].append(post.selftext)
    posts_dict["ID"].append(post.id)
    posts_dict["Score"].append(post.score)
    posts_dict["Total Comments"].append(post.num_comments)
    posts_dict["Post URL"].append(post.url)
    posts_dict["Flair"].append(post.link_flair_text)
 
# Saving the data in a pandas dataframe
hot_posts = pd.DataFrame(posts_dict)
hot_posts

hot_posts['Flair'].value_counts()

hot_posts.to_csv("Hot Posts ID.csv", index=True)


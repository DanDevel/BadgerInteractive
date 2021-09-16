
import os
import bson
from bson.objectid import ObjectId
import json
from pymongo import MongoClient, errors
import time
from datetime import date, timedelta, datetime
from decimal import *
from flask import Flask, session, render_template, request, redirect, url_for, jsonify, escape
from werkzeug.exceptions import HTTPException
import sys
import jinja2
#import numpy as np 
import pprint
import socket 
#import pyodbc  
import pprint
import random
from flask_cors import CORS
from werkzeug.utils import secure_filename
from pathlib import Path
import urllib3
import certifi

import tweepy
import random 
from random import randint
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import pytz
from datetime import datetime, timezone
import msgs_lib
from msgs_lib import *

local_template_folder = str(Path(__file__).parent.absolute()) + str('/Templates')
local_imgs_folder = str(Path(__file__).parent.absolute()) + str('/imgs')

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())


'''
Example WOEID locations include: Worldwide: 1 UK: 23424975 Brazil: 23424768 Germany: 23424829 Mexico: 23424900 Canada: 23424775 United States: 23424977 New York: 2459115

'''

msg_DAO_DEFI = ["$DAO will lead DeFi o/ #BadgerDaoMEMES", "#BadgerDAO and Defi will led the future. #BadgerDaoMEMES", "#BadgerDAO and DeFi will change the world! o/ #BadgerDaoMEMES"]
msg_DAO_BTC = ["#BTC and $DAO to DeFi and beyondo/ #BadgerDaoMEMES", "#BTC and Defi will make you shake ;). #BadgerDaoMEMES", "#BTC and $DAO #BadgerDAO will change the world! o/ #BadgerDaoMEMES"]

msg_DAO_DEFI_FR = ["$DAO avec DeFi o/ #BadgerDaoMEMES", "#BadgerDAO et Defi tres bien #BadgerDaoMEMES", "#BadgerDAO et DeFi allez changer nouz future! o/ #BadgerDaoMEMES"]
msg_DAO_BTC_FR = ["#BTC et $DAO trouve le DeFi :D o/ #BadgerDaoMEMES", "#BTC et Defi will allez chantee une bonne musique;). #BadgerDaoMEMES", "#BTC et $DAO #BadgerDAO merci merci! o/ #BadgerDaoMEMES"]

exchanges_list = ["#Binance", "#OKex", "#ZT", "#Huobi"]

msg_DAO_PROMO_USA = ["Buy on  " + str(exchanges_list[randint(0, len(exchanges_list)-1)]) ,"Like Pin and Share #BadgerDaoMEMES","Pls visit our Website #BadgerDAO #BadgerDaoMEMES"]
msg_DAO_PROMO_FRANCE = ["Acheter  " + str(exchanges_list[randint(0, len(exchanges_list)-1)]) + str(" #BadgerDAO #BadgerDaoMEMES")  ,"Suivre mon chaine #BadgerDAO","Pls visit our Website #BadgerDAO #BadgerDaoMEMES"]

general_terms_PEOPLE_TALKING_ABOUT = [] # run time filling. fr and en


# dev api twitter
# https://developer.twitter.com/en/docs/tutorials/explore-a-users-tweets

# https://api.twitter.com/1.1/statuses/update.json?status=hello

# lat lon USA: https://www.latlong.net/category/cities-236-15.html

now = datetime.now()
ts = datetime.timestamp(now)

CONSUMER_KEY=''
CONSUMER_SECRET=''
ACCESS_TOKEN=''
ACCESS_TOKEN_SECRET=''
BEARER_TOKEN=''

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)




def infoAboutUserAndHisFollowers(_user):
    user = api.get_user(_user)

    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)

    print("Last 20 Followers:")
    for follower in user.followers():
        print(follower.name)



def followUser(_user):
    api.create_friendship(str(_user))





def periodOfTheDay_EUROPE():
    #utc_dt = datetime.now(timezone.utc)
    #dt = utc_dt.astimezone()
    #tz = pytz.timezone('Europe/Berlin')
    tz = pytz.timezone('Europe/Paris')
    europe_now = datetime.now(tz)
    europe_now_hour = datetime.now(tz).hour
    #print(europe_now)
    #print(europe_now_hour)
    if ((europe_now_hour >= 4) and (europe_now_hour <= 10)):
        print('Bonjour Paris')
        # meme de la matin, morning meme
    if ((europe_now_hour >15) and (europe_now_hour <= 18)):
        print("bonn'apres midi Paris")
        # apres midi meme # afternoon meme
    if ((europe_now_hour >18) and (europe_now_hour <= 23)):
        print('Bon nuit Paris')
        # niut meme # night meme
    return europe_now_hour


def periodOfTheDay_USA():
    #utc_dt = datetime.now(timezone.utc)
    #dt = utc_dt.astimezone()
    #tz = pytz.timezone('Europe/Berlin')
    tz = pytz.timezone('US/Eastern')
    europe_now = datetime.now(tz)
    europe_now_hour = datetime.now(tz).hour
    #print(europe_now)
    print(europe_now_hour)
    if ((europe_now_hour >= 4) and (europe_now_hour <= 10)):
        print('Good morning  periodOfTheDay_USA()')
        # meme de la matin, morning meme
    if ((europe_now_hour >=13) and (europe_now_hour <= 18)):
        print("good noon  periodOfTheDay_USA()")
        # apres midi meme # afternoon meme
    if ((europe_now_hour >18) and (europe_now_hour <= 23)):
        print('Good evenning periodOfTheDay_USA()')
        # niut meme # night meme
    return europe_now_hour





def searchTweets_EN(_term):
    general_terms_PEOPLE_TALKING_ABOUT.clear()

    for tweet in api.search(q=str(_term), lang="en", rpp=10):
        #print('tweet:::::')
        #print(tweet)
        top_msg_1 = ""
        top_msg_2 = ""
        print('')
        print(f"{tweet.user.name}:{tweet.text}")
        if "DAO" in tweet.text: # 2nd Level TOP TERM to improve accuracy
            print('======>>>>>> OK DAO FOUND on TEXT MESSAGE USA')

            if "DeFi" in tweet.text:
                print('======>>>>>> OK $DAO and DeFi FOUND on TEXT MESSAGE USA')


                top_msg_1 = msg_DAO_DEFI[randint(0, len(msg_DAO_DEFI)-1)]
                general_terms_PEOPLE_TALKING_ABOUT.append(str(top_msg_1))

            if "#Bitcoin" in tweet.text:
                print('======>>>>>> OK DAO FOUND on TEXT MESSAGE USA')
                top_msg_2 = msg_DAO_BTC[randint(0, len(msg_DAO_BTC)-1)]
                general_terms_PEOPLE_TALKING_ABOUT.append(str(top_msg_2))

            

        #user1 = str(tweet.user.name)
        #print('====>>>>>name '+str(user1))
        #print('====>>>>>id '+str(tweet.user.id))
        #followUser(str(tweet.user.id))
        #print('===========')
        #time.sleep(10)





def searchTweets_FR(_mot):
    general_terms_PEOPLE_TALKING_ABOUT.clear()
    for tweet in api.search(q=str(_mot), lang="fr", rpp=10):
        #print('tweet:::::')
        #print(tweet)
        print('')
        print(f"{tweet.user.name}:{tweet.text}")
        if "Bitcoin" in tweet.text: # 2nd Level TOP TERM to improve accuracy
            print('======>>>>>> OK DAO FOUND on TEXT MESSAGE france')

            if "DeFi" in tweet.text:
                print('======>>>>>> OK $DAO and DeFi FOUND on TEXT MESSAGE france')


                top_msg_1 = msg_DAO_DEFI_FR[randint(0, len(msg_DAO_DEFI_FR)-1)]
                general_terms_PEOPLE_TALKING_ABOUT.append(str(top_msg_1))

            if "Bitcoin" in tweet.text:
                print('======>>>>>> OK Bitcoin FOUND on TEXT MESSAGE france')
                top_msg_2 = msg_DAO_BTC_FR[randint(0, len(msg_DAO_BTC_FR)-1)]
                general_terms_PEOPLE_TALKING_ABOUT.append(str(top_msg_2))

            if "bitcoin" in tweet.text:
                print('======>>>>>> OK Bitcoin FOUND on TEXT MESSAGE france')
                top_msg_2 = msg_DAO_BTC_FR[randint(0, len(msg_DAO_BTC_FR)-1)]
                general_terms_PEOPLE_TALKING_ABOUT.append(str(top_msg_2))

            if "BTC" in tweet.text:
                print('======>>>>>> OK BTC FOUND on TEXT MESSAGE france')
                top_msg_2 = msg_DAO_BTC_FR[randint(0, len(msg_DAO_BTC_FR)-1)]
                general_terms_PEOPLE_TALKING_ABOUT.append(str(top_msg_2))

            if "#BTC" in tweet.text:
                print('======>>>>>> OK BTC FOUND on TEXT MESSAGE france')
                top_msg_2 = msg_DAO_BTC_FR[randint(0, len(msg_DAO_BTC_FR)-1)]
                general_terms_PEOPLE_TALKING_ABOUT.append(str(top_msg_2))

            if "#Bitcoin" in tweet.text:
                print('======>>>>>> OK #Bitcoin FOUND on TEXT MESSAGE france')
                top_msg_2 = msg_DAO_BTC_FR[randint(0, len(msg_DAO_BTC_FR)-1)]
                general_terms_PEOPLE_TALKING_ABOUT.append(str(top_msg_2))

        #user1 = str(tweet.user.name)
        #print('====>>>>>name '+str(user1))
        #print('====>>>>>id '+str(tweet.user.id))
        #followUser(str(tweet.user.id))
        #print('===========')
        #time.sleep(10)






def trendingWorldWide():
    trends_result = api.trends_place(23424977)
    for trend in trends_result[0]["trends"]:
        print(trend)
        print(trend["name"])


# trendingWorldWide()



msgsLog = [{"en":0, "fr":0}]
msgOfTheDay = {"period":1, "language":1, "msgnumber":1, "msg":"Hello #Bitcoin #Traders"}
badgerMeme = {"background":1, "face":1, "glass":1, "blunt":1, "cap":1}


gpsLocationsFrance = [{"city":"Dunkirk, Hauts-de-France", "lat":"51.050030", "lon":"2.397766"},
{"city":"Lille, Hauts-de-France", "lat":"50.629250", "lon":"3.057256"},
{"city":"Menton, the Provence-Alpes-Côte d'Azur", "lat":"43.774483", "lon":"7.497540"},
{"city":"Bastia, the Haute-Corse", "lat":"42.697285", "lon":"9.450881"},
{"city":"Le Cannet, Cannes", "lat":"43.552849", "lon":"7.017369"},
{"city":"Beauvais, the Hauts-de-France", "lat":"49.431744", "lon":"2.089773"},
{"city":"Mulhouse, Grand Est", "lat":"47.750839", "lon":"7.335888"},
{"city":"Bordeaux", "lat":"44.836151", "lon":"-0.580816"},
{"city":"Boulogne-Billancourt, Île-de-France", "lat":"48.843933", "lon":"2.247391"}]

gpsLocationsUsa = [{"city":"West Palm Beach, FL", "lat":"26.709723", "lon":"-80.064163"},
{"city":"Miami Gardens, FL", "lat":"25.942122", "lon":"-80.269920"},
{"city":"Murrieta, CA,", "lat":"33.569443", "lon":"-117.202499"},
{"city":"Springfield, IL", "lat":"39.799999", "lon":"-89.650002"},
{"city":"El Monte, CA", "lat":"34.073334", "lon":"-118.027496"},
{"city":"West Jordan, UT", "lat":"40.606388", "lon":"-111.976112"},
{"city":"College Station, TX", "lat":"30.601389", "lon":"-96.314445"},
{"city":"Fairfield, CA", "lat":"38.257778", "lon":"-122.054169"},
{"city":"Evansville, IN", "lat":"37.977222", "lon":"-87.550552"}]

msg_search_terms = ["Badger DAO", "Binance", "Crypto", "Bitcoin", "Ethereum", "Cardano"]
#msg_exchange_terms = ["Binance", "Huobi Global Exchange", "OKEx Exchange", "FTX Exchange", "ZT Exchange"]
#people_termos = [{"term":"Crypto", "people:[]"}, {"term":"Badger", "people:[]"}]

# arrayOfTheDay = [0,0,0,0,0] # msg parameters



# ===================================
# MSG USA
# ===================================

def textMessageToUSA(_hour):
    _res = 0
    if ((_hour >= 4) and (_hour <= 10)):
        _res = randint(1, 5)
        random_object_message = MSG_USA_MORNING[randint(0, len(MSG_USA_MORNING)-1)]['msg']
        return random_object_message

    if ((_hour >15) and (_hour <= 18)):
        _res = randint(1, 5) # 6, 10
        random_object_message = MSG_USA_AFTERNOON[randint(0, len(MSG_USA_AFTERNOON)-1)]['msg']
        return random_object_message

    if ((_hour >18) and (_hour <= 23)):
        _res = randint(1, 5) # 11, 15
        random_object_message = MSG_USA_NIGHT[randint(0, len(MSG_USA_NIGHT)-1)]['msg']

        night_products = ["#Pizza", "#Burguer plus #fries", "#Soup"] # ["#Pizza", "#Macarons", "#Lait aux #chocolat chaud"]
        #night_places = ["@McDonalds", "@BurgerKing", "@Starbucks"] # ["@McDonaldsFrance", "@BurgerKingFR", "@StarbucksFrance"]
        night_expressions = ["Where's the Moon right now?", "Under the moonlight ;)", "someone to share the #night ;)"]
        for _products in night_products:
            if _products in random_object_message:
                random_object_message.replace(_products, night_products[randint(0, len(night_products)-1)], 200)
        
        random_object_message += str(night_expressions[randint(0, len(night_expressions)-1)])
        
        return random_object_message


#txt1 =   textMessageToUSA(10) 
#print('selected message:', txt1)

# ===================================
# MSG FRANCE
# ===================================

def textMessageToFRANCE(_hour):
    _res = 0
    if ((_hour >= 4) and (_hour <= 10)):
        _res = randint(1, 5)
        random_object_message = MSG_FRANCE_MORNING[randint(0, len(MSG_FRANCE_MORNING)-1)]['msg']
        return random_object_message

    if ((_hour >15) and (_hour <= 18)):
        _res = randint(1, 5) # 6, 10
        random_object_message = MSG_FRANCE_APRES_MIDI[randint(0, len(MSG_FRANCE_APRES_MIDI)-1)]['msg']
        return random_object_message

    if ((_hour >18) and (_hour <= 23)):
        _res = randint(1, 5) # 11, 15
        random_object_message = MSG_FRANCE_NUIT[randint(0, len(MSG_FRANCE_NUIT)-1)]['msg']

        night_products = ["#Pizza", "#Macarons", "#Lait aux #chocolat chaud"]
        #night_places = ["@McDonaldsFrance", "@BurgerKingFR", "@StarbucksFrance"]
        night_expressions = ["J'adore la nuit", "Regarde la #nuit mis ami", "Nuit super nuit"]
        for _products in night_products:
            if _products in random_object_message:
                random_object_message.replace(_products, night_products[randint(0, len(night_products)-1)], 200)
        
        random_object_message += str(night_expressions[randint(0, len(night_expressions)-1)])
        
        return random_object_message

# txt2 = extMessageToFRANCE(_hour)
#print('selected message:', txt2)

# ===================================
# MEME
# ===================================

def chooseBackground(_hour):
    if ((_hour >= 4) and (_hour <= 12)):
        _res = randint(1, 5)
        return _res
    if ((_hour >=13) and (_hour <= 18)):
        _res = randint(1, 5) # 6, 10
        return _res
    if ((_hour >18) and (_hour <= 23)):
        _res = randint(1, 5) # 11, 15
        return _res

    return 1

def chooseFace(_hour):
    return 1 # only 1 available by now.
    if ((_hour >= 4) and (_hour <= 12)):
        _res = randint(1, 5)
        return _res
    if ((_hour >=13) and (_hour <= 18)):
        _res = randint(1, 5) # 6, 10
        return _res
    if ((_hour >18) and (_hour <= 23)):
        _res = randint(1, 5) # 11, 15
        return _res

    return 1

def chooseGlass(_hour):
    if ((_hour >= 4) and (_hour <= 12)):
        _res = randint(1, 5)
        return _res
    if ((_hour >=13) and (_hour <= 18)):
        _res = randint(1, 5) # 6, 10
        return _res
    if ((_hour >18) and (_hour <= 23)):
        _res = randint(1, 5) # 11, 15
        return _res

    return 1

def chooseCap(_hour):
    if ((_hour >= 4) and (_hour <= 12)):
        _res = randint(1, 5)
        return _res
    if ((_hour >=13) and (_hour <= 18)):
        _res = randint(1, 5) # 6, 10
        return _res
    if ((_hour >18) and (_hour <= 23)):
        _res = randint(1, 5) # 11, 15
        return _res

    return 1

def chooseBlunt(_hour):
    if ((_hour >= 4) and (_hour <= 12)):
        _res = randint(1, 5)
        return _res
    if ((_hour >=13) and (_hour <= 18)):
        _res = randint(1, 5) # 6, 10
        return _res
    if ((_hour >18) and (_hour <= 23)):
        _res = randint(1, 5) # 11, 15
        return _res

    return 1



def tweetMEME(_filename, _status, _lat, _lon):
    # post the tweet
    api.update_with_media(_filename, _status, lat=_lat, lon=_lon)






def BadgerMEME_IMAGE_PLOT(memeName, backgroundNumber, faceNumber, glassNumber, bluntNumber, capNumber):    
    background = mpimg.imread(local_imgs_folder+'/backgnd/background'+str(backgroundNumber)+str('.png'))
    face = mpimg.imread(local_imgs_folder+'/face/face'+str(faceNumber)+str('.png'))
    glass = mpimg.imread(local_imgs_folder+'/glass/glass'+str(glassNumber)+str('.png'))
    blunt = mpimg.imread(local_imgs_folder+'/blunt/blunt'+str(bluntNumber)+str('.png'))
    cap = mpimg.imread(local_imgs_folder+'/cap/cap'+str(capNumber)+str('.png'))

    plt.imshow(background)
    plt.imshow(face)
    plt.imshow(glass)
    plt.imshow(blunt)
    plt.imshow(cap)
    plt.axis('off')
    
    plt.savefig(local_imgs_folder+'/memes/meme'+str(memeName)+str('.png'), bbox_inches='tight')
    #plt.show()
    
# try a meme:
#BadgerMEME_IMAGE_PLOT(2, 1, 3, 1, 2)


def sendMesageBADGER_Style():
    # language
    language_post = "en"
    if randint(0, 1) == 1:
        print('post to US')
        language_post = "en"
        #period_hour_USA = periodOfTheDay_USA()
    else:
        print('post to France')
        language_post = "fr"
        #period_hour_EUROPE = periodOfTheDay_EUROPE()

    #language_post = "fr" # en fixed by now

    # period of the day
    period_hour_EUROPE = periodOfTheDay_EUROPE()
    print('period_hour_EUROPE: ', period_hour_EUROPE)
    period_hour_USA = periodOfTheDay_USA()
    print('period_hour_USA: ', period_hour_USA)
    # message
    local_object = randint(0, len(gpsLocationsUsa)-1) # choose random place lat lon
    print('local_object: ', local_object)

    badger_meme = []

    MEME_ARRAY_LAST_PARAMETERS = [1,1,1,1,1] # background, face, glass, cap, blunt
    MEME_ARRAY_NEW_PARAMETERS = [1,1,1,1,1] 
    while MEME_ARRAY_NEW_PARAMETERS == MEME_ARRAY_LAST_PARAMETERS:
        MEME_ARRAY_NEW_PARAMETERS = [chooseBackground(period_hour_USA),chooseFace(period_hour_USA),chooseGlass(period_hour_USA),chooseCap(period_hour_USA),chooseBlunt(period_hour_USA)]

    print('-----1')

    if language_post == "en":  
        # txt msg to post
        txt_USA = textMessageToUSA(period_hour_USA)
        lat_post_USA = gpsLocationsUsa[local_object]["lat"]
        lon_post_USA = gpsLocationsUsa[local_object]["lon"]
        lat_lon_city = gpsLocationsUsa[local_object]["city"]

        searchTweets_EN("Badger Dao")
        random_accurate_msg_to_post = general_terms_PEOPLE_TALKING_ABOUT[randint(0, len(general_terms_PEOPLE_TALKING_ABOUT)-1)]
        print('-----2')
        # badger meme parts of the meme according the time of the day: morning, afternoon, night
        badger_meme = [{
            "background": str(MEME_ARRAY_NEW_PARAMETERS[0]),
            "face": str(MEME_ARRAY_NEW_PARAMETERS[1]),
            "glass": str(MEME_ARRAY_NEW_PARAMETERS[2]),
            "cap": str(MEME_ARRAY_NEW_PARAMETERS[3]),
            "blunt": str(MEME_ARRAY_NEW_PARAMETERS[4]),
            "lat_lon_city":str(lat_lon_city),
            "lat": lat_post_USA,
            "lon": lon_post_USA,
            "msg_post_level1":str(txt_USA), # general message to USA according Time of the day
            "msg_post_level2":str(random_accurate_msg_to_post), # message according what people are talking about Badger DAO
            "msg_post_level3":str(msg_DAO_PROMO_USA[randint(0, len(msg_DAO_PROMO_USA)-1)]) # add a promo text on message ? 
        }]
        print('-----3')
        

        # MEME IMAGE PLOT
        meme_name = str(datetime.timestamp(now)).replace('.', '', 900).replace('.', '', 900)
        # BadgerMEME_IMAGE_PLOT(meme_name, randint(1,5), 1, randint(1,5), randint(1,5), randint(1,5))
        # BadgerMEME_IMAGE_PLOT(memeName, backgroundNumber, faceNumber, glassNumber, bluntNumber, capNumber):
        BadgerMEME_IMAGE_PLOT(meme_name, badger_meme[0]['background'], badger_meme[0]['face'], badger_meme[0]['glass'], badger_meme[0]['blunt'], badger_meme[0]['cap'])
        print('-----4')
        # avoid repeat same meme
        MEME_ARRAY_LAST_PARAMETERS = MEME_ARRAY_NEW_PARAMETERS
        
        # ====== POST o/
        myMEME = str(local_imgs_folder+'/memes/meme'+str(meme_name)+str('.png'))
        str_badger_object_msg_name = str('msg_post_level')+str(randint(1,2)) # include promo msg: + msg_DAO_PROMO_USA...
        MEME_MSG = badger_meme[0][str(str_badger_object_msg_name)] + str(' #') + str(badger_meme[0]['lat_lon_city'])

        print('')
        print('meme: ' + str(myMEME))
        print('msg to post: ' + str(MEME_MSG))
        print('city: ' + str(lat_lon_city))

        if len(str(badger_meme[0][str(str_badger_object_msg_name)]))> 8:    
            print('')
            print('meme: ' + str(myMEME))
            print('msg to post: ' + str(MEME_MSG))
            tweetMEME(myMEME, MEME_MSG, badger_meme[0]['lat'], badger_meme[0]['lon'])
            print('====== ***** post to USA ok o/')
        else:
            print('==== <<<><><><> MEME_MSG USA was none')




    if language_post == "fr":  
        print('-----5 fr')
        # txt msg to post
        txt_FRANCE = textMessageToFRANCE(period_hour_EUROPE)
        lat_post_FRANCE = gpsLocationsFrance[local_object]["lat"]
        lon_post_FRANCE = gpsLocationsFrance[local_object]["lon"]
        lat_lon_city = gpsLocationsFrance[local_object]["city"]
        print('-----6 fr')
        searchTweets_FR("Bitcoin")
        print('==>>> general_terms_PEOPLE_TALKING_ABOUT:')
        print(general_terms_PEOPLE_TALKING_ABOUT)
        print('')
        random_accurate_msg_to_post = general_terms_PEOPLE_TALKING_ABOUT[randint(0, len(general_terms_PEOPLE_TALKING_ABOUT)-1)]
        print('-----7 fr')
        # badger meme
        badger_meme = [{
            "background": str(MEME_ARRAY_NEW_PARAMETERS[0]),
            "face": str(MEME_ARRAY_NEW_PARAMETERS[1]),
            "glass": str(MEME_ARRAY_NEW_PARAMETERS[2]),
            "cap": str(MEME_ARRAY_NEW_PARAMETERS[3]),
            "blunt": str(MEME_ARRAY_NEW_PARAMETERS[4]),
            "lat_lon_city":str(lat_lon_city),
            "lat": lat_post_FRANCE,
            "lon": lon_post_FRANCE,
            "msg_post_level1":str(txt_FRANCE), # general message to USA according Time of the day
            "msg_post_level2":str(random_accurate_msg_to_post), # message according what people are talking about Badger DAO
            "msg_post_level3":str(msg_DAO_PROMO_FRANCE[randint(0, len(msg_DAO_PROMO_FRANCE)-1)]) # add a promo text on message ? 
        }]
        print('-----8 fr')
        # MEME IMAGE PLOT
        meme_name = str(datetime.timestamp(now)).replace('.', '', 900).replace('.', '', 900)
        # BadgerMEME_IMAGE_PLOT(meme_name, randint(1,5), 1, randint(1,5), randint(1,5), randint(1,5))
        # BadgerMEME_IMAGE_PLOT(memeName, backgroundNumber, faceNumber, glassNumber, bluntNumber, capNumber):
        BadgerMEME_IMAGE_PLOT(meme_name, badger_meme[0]['background'], badger_meme[0]['face'], badger_meme[0]['glass'], badger_meme[0]['blunt'], badger_meme[0]['cap'])
        print('-----9 fr')

        # ====== POST o/
        myMEME = str(local_imgs_folder+'/memes/meme'+str(meme_name)+str('.png'))
        str_badger_object_msg_name = str('msg_post_level')+str(randint(1,2)) # include promo msg: + msg_DAO_PROMO_USA...
        MEME_MSG = badger_meme[0][str(str_badger_object_msg_name)]+ str(' #') + str(badger_meme[0]['lat_lon_city'])


        
        if len(str(badger_meme[0][str(str_badger_object_msg_name)]))> 8:    
            print('')
            print('meme: ' + str(myMEME))
            print('msg to post: ' + str(MEME_MSG))
            tweetMEME(myMEME, MEME_MSG, badger_meme[0]['lat'], badger_meme[0]['lon'])
            print('====== ***** post to FRANCE ok o/')
        else:
            print('==== <<<><><><> MEME_MSG was none')

'''
searchTweets_FR("Bitcoin")
searchTweets_EN("Bitcoin")
'''

twts = 0
while True:
    try:
            
        sendMesageBADGER_Style()
        print('')
        twts += 1
        print('------>>>> Tweet post ok n :', twts)
        timerWait = randint(300, 900) # 5 ~ 15 minutes
        print('next tweet in: ', timerWait)

        time.sleep(timerWait)

    except Exception as err:
        pass
        print('error : ' + str(err))
















# BadgerInteractive 
Interactive content for BADGER Gitcoin's Hackathon

# Search: #BadgerDaoMEMES on Twitter to see the result.

# BOT for Badger DAO interaction on twitter.

Send a tweet with text and auto generated meme, any place in US or France.
Send text messages in french to France territory and English to US territory.

# Work in 2 languages: ENGLISH and FRENCH. (can be improved more languages for the next versions).

How it works:

# before run this code... >>> insert your twitter credentials:

CONSUMER_KEY=''
CONSUMER_SECRET=''
ACCESS_TOKEN=''
ACCESS_TOKEN_SECRET=''
BEARER_TOKEN=''

# step by step tweet workflow:
this is what the bot will do.

1 - choose a random time between 5 and 15 minutes.
2 - choose a random language 'en' or 'fr'
3 - choose a place according the language... New York, California, Paris, Lyon...
4 - search what people are talking about Badger DAO on US (Bitcoin on France)
5 - search especific terms on search result to accurate our post.
6 - once we find people talking about what we want, we can (optionally follow the users talking) and proceed.
7 - check the time of the day (morning, afternoon or night) to mount a text message according with the time.
8 - according whith time and place select a random pre-configured message.
9 - randomly change a few words on message to improve interaction. pizza/burguer etc...
10 - add some promo text: "Hey buy Badger on Exchange XXX etc.."
11 - randomly choose parts of the meme.
12 - send the MEME tweet with a text message to a selected place with lat and lon gps coordinates to spread Badger memes wherever we want.


Improve memes according with events:

We can create more images for the meme parts and sort by themes, for example, xmas background images: image1 to image20, night: image21 to image30 etc etc etc...

# images used on meme creation:

background images are on backgrnd folder, cap images are on cap folder, glass images are on glass folder  etc ...
add or change images to created more different memes.

# tips
for each part of the meme, we have 5 images, so while searching for a random image our code search on a range between 1 and 5. if you put 10 glasses images on glass folder, change the range on code to 1 and 10. 

# all you need to do is run this script file: twitterBADGER.py . easy and simple.







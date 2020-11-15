import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint

headers = {"Accept-Language": "en-US,en;q=0.5"}

#Defining cards as a class
class Card:
    def __init__(card, name, quantity):
        card.name = name
        card.quantity = quantity

#Data we are getting



#Grab HTML from site
formatPage = requests.get("https://www.mtgtop8.com/format?f=LE", headers=headers)
arshSoup = BeautifulSoup(formatPage.text, 'html.parser')
#print(soup.text)

#Get all of the tables on the format page
allTables = arshSoup.find_all('table')

#print out all archetypes found

#Grab all architypes from the architypes table
archetypes = allTables[3].find_all('tr')
for archetype in archetypes:
    for archLink in archetype.findAll('a'):
        archHref = archLink['href']
        print("name = " + archLink.get_text().strip() + " archLink = " + archHref)
        #sleep for bit before the next page request
        sleep(randint(2,5))
        archLink = "https://www.mtgtop8.com/" + str(archHref)
        decklistsPage = requests.get(archLink, headers=headers)
        decklistsSoup = BeautifulSoup(decklistsPage.text, 'html.parser')
        #print(decklistsSoup.text)
        #Get all of the tables on the decks page
        allTables = decklistsSoup.find_all('table')
        decklists = allTables[3].find_all('tr')
        #for each decklist
        for decklist in decklists:
            for deckLink in decklist.findAll('a'):
                deckHref = deckLink['href']
                print("name = " + deckLink.get_text().strip() + " deckHref = " + deckHref)
        

#Go to format

#For each list in format
#simple wikidata client 
#wikidata query response parsing 

import requests
import urllib.request
import http.client
#https://www.wikidata.org/w/index.php?search=&search=Ingolstadt&title=Special:Search&go=Go&ns0=1&ns120=1

url = "https://www.wikidata.org/w/api.php"


while True:
    query = input("Enter name : ")
    if query == "quit":
        break
    else:
        params = {
        "action" : "wbsearchentities",
        "language" : "en",
        "format" : "json",
        "search" : query 
        }
        try:
            data = requests.get(url,params=params)
            print("short description", data.json()["search"][0]["description"])
            # print(data.json())
            print(data.json()["search"][0]["id"])
            qnumber = data.json()["search"][0]["id"]
            
        except:
            print("Invalid Input try again !!!")


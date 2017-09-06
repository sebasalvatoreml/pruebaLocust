from locust import HttpLocust, TaskSet, task
from random import randint
import json

with open('config.json') as json_data:
    config = json.load(json_data)

def search(l):
    response = l.client.get("site_id=MCO", name="search")
    if response.status_code != 200: print "search: Response status code: " + str(response.status_code)

def searchON(l):
    response = l.client.get("site_id=MCO&marketplace=MELI", name="searchON")
    if response.status_code != 200: print "searchON: Response status code: " + str(response.status_code)

def searchOFF(l):
    url = "site_id=MCO&marketplace=MELI&limit=100&bins="+str(randint(400000, 499999))
    response = l.client.get(url, name="searchOFF")
    if response.status_code != 200: print "searchOFF: Response status code: " + str(response.status_code)

def searchSandbox(l):
    response = l.client.get("site_id=MLA&access_token="+config['testToken'], name="searchSandbox")
    if response.status_code != 200: print "searchSandbox: Response status code: " + str(response.status_code)

class searchBySiteId(TaskSet):
    tasks = {search: 1, searchON: 2, searchOFF: 3, searchSandbox: 4,}

    def on_start(self):
        search(self)

class WebsiteSearch(HttpLocust):
    task_set = searchBySiteId
    host = config['host']
    min_wait = 1000
    max_wait = 2000

from locust import HttpLocust, TaskSet, task
from random import randint

def search(l):
    l.client.get("site_id=MLA")
    if response.status_code != 200: print "search: Response status code: " + str(response.status_code)

def searchWithMarketplaceBins(l):
    url = "site_id=MLA&marketplace=MELI&limit=100&bins="+str(randint(400000, 499999))
    response = l.client.get(url, name="/site_id=MLA&marketplace=MELI&limit=100&bins=randomvisa")
    if response.status_code != 200: print "searchMarketplaceWithBins: Response status code: " + str(response.status_code)
    #print url

def searchTest(l):
    response = l.client.get("site_id=MLA&access_token=TEST-123123")
    json = response.json()
    if response.status_code != 200: print "searchTest: Response status code: " + str(response.status_code)

class searchBySiteId(TaskSet):
    tasks = {search: 1, searchMarketplaceWithBins: 2, searchTest: 3,}

    def on_start(self):
        search(self)

class WebsiteSearch(HttpLocust):
    task_set = searchBySiteId
    host = "https://api.mercadopago.com/fury/payment_methods/search?"
    min_wait = 1000
    max_wait = 2000

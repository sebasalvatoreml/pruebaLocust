from locust import HttpLocust, TaskSet, task
from random import randint

def search(l):
    response = l.client.get("site_id=MLA")
    if response.status_code != 200: print "search: Response status code: " + str(response.status_code)

def searchON(l):
    response = l.client.get("site_id=MCO&marketplace=MELI")
    if response.status_code != 200: print "searchON: Response status code: " + str(response.status_code)

def searchWithMarketplaceBins(l):
    url = "site_id=MLA&marketplace=MELI&limit=100&bins="+str(randint(400000, 499999))
    response = l.client.get(url, name="/site_id=MLA&marketplace=MELI&limit=100&bins=randomvisa")
    if response.status_code != 200: print "searchWithMarketplaceBins: Response status code: " + str(response.status_code)
    #print url

class searchBySiteId(TaskSet):
    tasks = {search: 1, searchWithMarketplaceBins: 2, searchON: 3,}

    def on_start(self):
        search(self)

class WebsiteSearch(HttpLocust):
    task_set = searchBySiteId
    #host = "sandbox-sc.payment-methods.melifrontends.com/v1/payment_methods/search?"
    host = "https://api.mercadopago.com/fury/payment_methods/search?"
    min_wait = 1000
    max_wait = 2000

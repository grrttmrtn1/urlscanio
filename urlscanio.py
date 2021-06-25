import requests
import json


class urlscanio:

    def __init__(self, api_key, visibility=None, base_uri=None):
        self.api_key = api_key
        if visibility = None:
            visibility = 'public'
        else:
            self.visibility = visibility
        if base_uri = None:
            base_uri = 'https://urlscan.io/api/v1/'
        else:
            self.base_uri = self.checkBaseURI(base_uri)
        self.headers = {'API-Key': self.api_key,'Content-Type':'application/json'}
    
    def checkBaseURI(uri):
        if uri(len(uri)-1) != '/':
            return uri + '/'
        else:
            return uri 
    def waitForResults():
        

    def submit(self, uri):
        try:
            data = {"url": uri, "visibility": self.visibility}
            response = requests.post(self.base_uri + 'scan/',headers=self.headers, data=json.dumps(data))
            if response.status_code = requests.codes.ok:
                print(json.dumps(response.contentm indent=2))
            else:
                response.raise_for_status()
        except Exception as e:
            print(e)

    def getDom(self, uuid):

    def getScreenshots(self, uuid):
    
    def getResults(self, uuid):

    def search(self, search):
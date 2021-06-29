import requests
import json


class urlscanio:
    def __init__(self, api_key, visibility=None, base_uri=None):
        self.api_key = api_key
        if visibility == None:
            self.visibility = 'public'
        else:
            self.visibility = visibility
        if base_uri == None:
            self.base_uri = 'https://urlscan.io/api/v1/'
        else:
            self.base_uri = self.checkBaseURI(base_uri)
        self.headers = {'API-Key': self.api_key,'Content-Type':'application/json'}
    def checkBaseURI(uri):
        if uri(len(uri)-1) != '/':
            return uri + '/'
        else:
            return uri 
    def waitForResults(self, process, uuid):
        if process == 'result':
            uri = self.base_uri + 'result/' + uuid
        elif process == 'dom':
            uri = 'https://urlscan.io/dom/' + uuid
        elif process == 'screenshots':
            uri = 'https://urlscan.io/screenshots/' + uuid + '.png'
        i=0
        print(uri)
        while i <= 60:
            try:
                print(i)
                response = requests.get(uri, headers=self.headers)
                print(response)
                if response.status_code == requests.codes.ok:
                    return response.content
                    break
                if i == 60:
                    return response.content
                i+=1
            except Exception as e:
                print(e)
    def submit(self, uri):
        try:
            data = {"url": uri, "visibility": self.visibility}
            response = requests.post(self.base_uri + 'scan/',headers=self.headers, data=json.dumps(data))
            if response.status_code == requests.codes.ok:
                return response.json()
            else:
                response.raise_for_status()
        except Exception as e:
            print(e)
    def getDom(self, uuid):
        return self.waitForResults('dom', uuid)
    def getScreenshots(self, uuid):
        return self.waitForResults('screenshots', uuid)   
    def getResults(self, uuid):
        return self.waitForResults('result', uuid)
    def search(self, search):
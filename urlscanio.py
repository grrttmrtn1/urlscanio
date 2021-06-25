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
            self.base_uri = base_uri

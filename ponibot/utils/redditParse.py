import re
import requests
import json

class RedditParse():
    def __init__(self, url):
        self.finds = []
        self.url = url
        self.nextPage = url
        self.headers = {
        "Upgrade-Insecure-Requests": "1",
        "user-agent" : "hui sobachii",
        }
        self.cookies = {
            "over18":"1"
        }

    def next(self):
        if len(self.finds) > 0 :
            return self.finds.pop(0)
        else: 
            try:
                self.next_page()
            except Exception as e:
                print(e)

            if len(self.finds) <= 0:
                raise NoContent()
            
            return self.next()

    def next_page(self):  
        finds = []

        if self.nextPage == None:
            self.nextPage = self.url

        rpage = requests.get(self.nextPage, cookies = self.cookies, headers=self.headers)

        urlinfo = json.loads(re.findall("window.___r = (.+?);</",rpage.text)[0])
        activeKey = urlinfo["listings"]["activeKey"]
        ids_list = urlinfo["listings"]["postOrder"]['ids'][activeKey]
        models = urlinfo["posts"]["models"]

        for ids in ids_list:
            try:
                finds.append({
                    "title" : models[ids]["title"],
                    "url" : models[ids]["media"]["content"],
                })
            except Exception as er:
                pass

        self.finds.extend(finds)

        try:
            self.nextPage = self.url+'?after='+re.findall(self.url+'\?after\=(.+?)"', rpage.text)[0]
        except IndexError as ie: 
            return
    

class NoContent(Exception):
    def __str__(self):
        return "Хент не найден"



import scrapy
import json


class PromptimagesSpider(scrapy.Spider):
    name = 'promptimages'
    # allowed_domains = ['prompt.com']
    # start_urls = ['http://prompt.com/']
    url = "https://www.prompthunt.com/api/search?page=1&themeId=clfqdumhy0005l808ezqstf72"
    payload={}

    def start_requests(self):
        url = "https://www.prompthunt.com/api/search?page=&themeId=clfqdumhy0005l808ezqstf72"
        headers = {
        'authority': 'www.prompthunt.com',
        'accept-language': 'en-US,en;q=0.9,mr;q=0.8',
        'content-type': 'application/json',
        'Cookie': '__Host-next-auth.csrf-token=3a11783d3817e345dd4c3a3c573d05f733c834bec85682c07ae9eaa9fc6e5f4e%7Ca002b9ec38725f4e5c57b6668b353348b3518909435eace9aba575c23d435f46; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.prompthunt.com'
        }

        yield scrapy.Request(url,method="GET",headers=headers,callback=self.parse)


    def parse(self, response):
        json_data = json.loads(response.text)

    
        for i in json_data["prompts"]:
                 
            try:
                a = i.get("assets")
                src=a[0].get("src")
                
            except:
                src = None

            try :
                b = i.get("assets")
                width = b[0].get("width")
            except:
                width=None

            try:
                c = i.get("assets")
                height = c[0].get("height")
            except:
                height=None

            try :
                d = i.get("meta")
                model = d.get("model")
            except:
                model=None

            try:
                e = i.get("meta")
            
                weight= None
                for we in  e["modifiers"]:
                    if we.get("weight"):
                        weight = we.get("weight")
                        break
                    
            except:
                weight=None
                    
            yield {
                "src" :src,
                "width" :width,
                "height":height,
                "weight":weight,
                "model":model}
            
        next_page = json_data.get("nextPage")
        if len(json_data["prompts"]) == 0:
            pass            
        else:
            link1 =f"https://www.prompthunt.com/api/search{next_page}"                   
            yield scrapy.Request(link1,callback=self.parse)
            

        
            
        


            
        

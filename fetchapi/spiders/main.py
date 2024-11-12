import scrapy
import json

class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["www.firestonecompleteautocare.com"]
    start_urls = ["https://www.firestonecompleteautocare.com/bsro/services/store/location/get-list-by-zip?zipCode=10001"]

    def parse(self, response):
        examples = json.loads(response.body)
        for store in examples['data']['stores']:
            hours = store['hours']
            for hour in hours:
                yield{
                    'WeekDay' : hour['weekDay'],
                    'closeTime': hour['closeTime'],
                    'openTime' : hour['openTime']

                }


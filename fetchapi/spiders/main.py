from ast import Store
from time import strftime
import scrapy
import json
from datetime import datetime

class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["www.firestonecompleteautocare.com"]
    start_urls = ["https://www.firestonecompleteautocare.com/bsro/services/store/location/get-list-by-zip?zipCode=10001"]
    custom_settings = {
        'FEED_EXPORT_IDENT': 4

    }
    
    def parse(self, response):
        examples = json.loads(response.body)
        for store in examples['data']['stores']:
            hour_s = {}
            hours = store['hours']
            for hour in hours:
                hour_s[hour['weekDay']] = {
                    'open' : f"{hour['openTime']} am",
                    'close' : f"{hour['closeTime']} pm",
                }

            hour_s['monday'] = hour_s['MON']
            del hour_s['MON']
            hour_s['tuesday'] = hour_s['TUE']
            del hour_s['TUE']
            hour_s['wednesday'] = hour_s['WED']
            del hour_s['WED']
            hour_s['thursday'] = hour_s['THU']
            del hour_s['THU']
            hour_s['friday'] = hour_s['FRI']
            del hour_s['FRI']
            hour_s['saturday'] = hour_s['SAT']
            del hour_s['SAT']
            hour_s['sunday'] = hour_s['SUN']
            del hour_s['SUN'] 

            yield{
            'hours' : hour_s

            }
        
        
'''        for store in examples['data']['stores']:
            hours = store['hours']
            for hour in hours:
                yield{
                    'WeekDay' : hour['weekDay'],
                    'closeTime': hour['closeTime'],
                    'openTime' : hour['openTime']

                }'''


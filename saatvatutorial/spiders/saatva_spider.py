# import library
import scrapy
# import class from items.py
from saatvatutorial.items import SaatvatutorialItem

# create spider class
class SaatvaSpider(scrapy.Spider):
    # set any number of global variables needed
    # Global variables are needed to for your website link
    url = ['https://www.saatva.com/mattresses/saatva-classic']
    
    
    # Functions are used to extract data from the website
    def start_requests(self):
        for link in self.url:
            yield scrapy.Request(url=link, callback=self.parse)
   
   
    def parse(self,response):
        # pull xpath
        name = response.xpath('//h1[@class="productPanel__headingTitle"]/text()').extract_first()
        size = response.xpath('//div[@class="u-fullWidth u-flexDisplay u-flexJustify--spaceBetween"]/span/text()').extract_first()
        price = response.xpath('//div[@class="strikethroughPrice"]/span/text()').extract_first()
        
        # pull data
        item = SaatvatutorialItem()
        item['name'] = name
        item['size'] = size
        item['price'] = price
        yield item

        # Set up the file pipelines.py
        # Adjust settings.py: turn on download delay
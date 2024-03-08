from scrapy import Spider
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.selector import Selector
from time import sleep

class IetfSpider(Spider):
    name = "ietf"
    allowed_domains = ["subway.com.my"]
    start_urls = ['https://subway.com.my/find-a-subway']

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def parse(self, response):
        self.driver.get(response.url)
        sleep(3)  # Wait for the page to load

        sel = Selector(text=self.driver.page_source)
        
        # Loop through each outlet
        for outlet in sel.xpath('//div[contains(@class, "fp_listitem")]'):
            address = outlet.xpath('.//div[@class="infoboxcontent"]/p[1]/text()').get()
            if 'Kuala Lumpur' in address:  # Filter for Kuala Lumpur addresses
                latitude = outlet.xpath('./@data-latitude').get()
                longitude = outlet.xpath('./@data-longitude').get()

                yield {
                    'name': outlet.xpath('.//h4/text()').get(),
                    'address': address,
                    'operating_hours': outlet.xpath('.//div[@class="infoboxcontent"]/p[3]/text()').get(),
                    'waze_link': outlet.xpath('.//div[contains(@class, "directionButton")]/a[contains(@href, "waze")]/@href').get(),
                    'latitude': latitude,
                    'longitude': longitude,
                }
    
        self.driver.quit()

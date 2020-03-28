import scrapy
from scrapy.selector import Selector
from .form4Parser import Form4Parser
from datetime import datetime
from datetime import timedelta


class Form4Spider(scrapy.Spider):
    name = "form4"
    allowed_domains = ["www.sec.gov"]

    def __init__(self, file_path, start, end):
        self.root_url = "https://www.sec.gov/Archives/"
        self.root_daily_url = 'https://www.sec.gov/Archives/edgar/daily-index/'
        self.file_path = file_path
        self.start = start
        self.end = end
        self.urls = []

    def generate_urls(self):
        start_date = datetime.strptime(self.start, '%Y%m%d')
        end_date = datetime.strptime(self.end, '%Y%m%d')

        while start_date < end_date:
            current_date = start_date
            month = current_date.month
            if 1 <= month <= 3:
                qtr = 'QTR1'
            elif 4 <= month <= 6:
                qtr = 'QTR2'
            elif 7 <= month <= 9:
                qtr = 'QTR3'
            else:
                qtr = 'QTR4'

            year = current_date.year
            date_str = current_date.strftime('%Y%m%d')
            url = f'{self.root_daily_url}{year}/{qtr}/master.{date_str}.idx'
            self.urls.append(url)
            start_date = start_date + timedelta(days=1)

    def start_requests(self):
        self.generate_urls()
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            content = str(response.body)
            lines = content.split('\\n')
            for line in lines:
                line = line.strip()
                if line.endswith('.txt'):
                    vars = line.split('|')
                    type = vars[2]
                    if type == '4':
                        xml_url = self.root_url + vars[-1]
                        yield scrapy.Request(url=xml_url, callback=self.parse_xml_url)

    def parse_xml_url(self, response):
        if response.status == 200:
            form4 = Form4Parser()
            form4.parse(response.body)

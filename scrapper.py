from datetime import date
import requests
import csv
from bs4 import BeautifulSoup

class Scrapper:

    headlines = None
    
    def __init__(self, news_url, base_url, class_name, tag, name="news"):
        self.news_url = news_url 
        self.base_url = base_url
        self.name = name
        self.class_name = class_name
        self.tag = tag
        self.date = date.today().isoformat() 


    def scrape(self, helper=lambda link, scapper: None):
        try:
            respose = requests.get(self.news_url)
            respose.raise_for_status()
            soup = BeautifulSoup(respose.content, 'html.parser')
            headlines = []
            for link in soup.find_all('a', class_=self.class_name):
                headline = helper(link, self)
                if headline is not None:
                    headlines.append(headline)        
            self.headlines = headlines 
        except requests.exceptions.RequestException as e:
            print(f'Error scraping {self.name}: {e}')
    
    def export_news_csv(self):
        if self.headlines:
            with open(f"{self.name}-{self.date}.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.headlines[0].keys())
                writer.writeheader()
                for headline in self.headlines:
                    writer.writerow(headline)


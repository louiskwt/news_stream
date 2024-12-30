from datetime import date
import requests
import csv
from bs4 import BeautifulSoup

class Scrapper:

    headlines = None
    
    def __init__(self, news_url, base_url, class_name, name="news", parent_tag=None):
        self.news_url = news_url 
        self.base_url = base_url
        self.name = name
        self.class_name = class_name
        self.date = date.today().isoformat()
        self.parent_tag = parent_tag 


    def scrape(self, helper=lambda link, scapper: None):
        try:
            respose = requests.get(self.news_url)
            respose.raise_for_status()
            soup = BeautifulSoup(respose.content, 'html.parser')
            links = []
            headlines = []
            if self.parent_tag:
                for link_element in soup.find_all(self.parent_tag, class_=self.class_name):
                    a_tag = link_element.find('a')
                    if a_tag:
                        links.append(a_tag)
            else:
                links = soup.find_all('a', class_=self.class_name)

            for link in links:
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


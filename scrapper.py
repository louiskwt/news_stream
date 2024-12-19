from datetime import date
import requests
import csv
from bs4 import BeautifulSoup

class Scrapper:

    headlines = None
    EXCLUDED_WORDS = ['British Broadcasting Corporation', 'Video', 'Sport', 'Home', 'Audio', 'Weather', 'Newsletters']

    def __init__(self, news_url, base_url, class_name, name="news"):
        self.news_url = news_url 
        self.base_url = base_url
        self.name = name
        self.class_name = class_name
        self.date = date.today().isoformat() 


    def scrape(self):
        try:
            respose = requests.get(self.news_url)
            respose.raise_for_status()
            soup = BeautifulSoup(respose.content, 'html.parser')
            headlines = []
            for link in soup.find_all('a', class_=self.class_name):
                text = link.text.strip()
                if text not in self.EXCLUDED_WORDS:
                    href = self.base_url + link['href']
                    headlines.append({'title': text, 'link': href})        
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


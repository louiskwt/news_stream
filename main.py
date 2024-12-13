import requests
import csv
from bs4 import BeautifulSoup

def bbc_scrapper():
    try:

        url = "https://www.bbc.com/news"

        respose = requests.get(url)
        respose.raise_for_status()
        soup = BeautifulSoup(respose.content, 'html.parser')

        headlines = []
        for link in soup.find_all('a', class_='sc-2e6baa30-0 gILusN'):
            text = link.text.strip()
            if text not in ['British Broadcasting Corporation', 'Video', 'Sport', 'Weather', 'Newsletters']:
                href = 'https://www.bbc.com' + link['href']
                headlines.append({'title': text, 'link': href})
        
        return headlines

    except requests.exceptions.RequestException as e:
        print(f'Error scraping BBC: {e}')
        return []

bbc_headlines = bbc_scrapper()

if bbc_headlines:
    with open("bbc_news.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=bbc_headlines[0].keys())
        writer.writeheader()
        for headline in bbc_headlines:
            writer.writerow(headline)
import requests
import csv
from bs4 import BeautifulSoup
from datetime import date
from scrapper import Scrapper

bbc_scrapper = Scrapper("https://www.bbc.com/news", "https://www.bbc.com", 'sc-2e6baa30-0 gILusN', "bbc_news")


bbc_scrapper.scrape()
bbc_scrapper.export_news_csv()


# def guardian_scrapper():
#     try:
#         url = "https://www.theguardian.com/international"
#         respose = requests.get(url)
#         respose.raise_for_status()
#         soup = BeautifulSoup(respose.content, 'html.parser')
#         headlines = []
#         for link in soup.find_all('a', class_='dcr-ezvrjj'):
#             href = 'https://www.theguardian.com' + link['href']
#             headlines.append({'title': link['aria-label'], 'link': href})
#         return headlines
#     except requests.exceptions.RequestException as e:
#         print(f'Error scraping the guardians: {e}')
#         return []

# bbc_headlines = bbc_scrapper()
# guardian_headlines = guardian_scrapper()

# today = date.today().isoformat()

# if bbc_headlines:
#     with open(f"bbc_news-{today}.csv", "w", newline="") as file:
#         writer = csv.DictWriter(file, fieldnames=bbc_headlines[0].keys())
#         writer.writeheader()
#         for headline in bbc_headlines:
#             writer.writerow(headline)

# if guardian_headlines:
#     with open(f'guardian_news-{today}.csv', 'w', newline="") as file:
#         writer = csv.DictWriter(file, fieldnames=guardian_headlines[0].keys())
#         writer.writeheader()
#         for headline in guardian_headlines:
#             writer.writerow(headline)
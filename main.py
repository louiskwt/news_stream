import sys
from scrapper import Scrapper
from utils import process_bbc_headlines, process_guadian_headlines, remove_csv_files

def scrap_news():
    bbc_scrapper = Scrapper("https://www.bbc.com/news", "https://www.bbc.com", 'sc-2e6baa30-0 gILusN', 'href', "bbc_news")
    guardian_scrapper = Scrapper("https://www.theguardian.com/international", "https://www.theguardian.com", 'dcr-ezvrjj', 'aria-label', 'guardian_news')

    bbc_scrapper.scrape(process_bbc_headlines)
    bbc_scrapper.export_news_csv()

    guardian_scrapper.scrape(process_guadian_headlines)
    guardian_scrapper.export_news_csv()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'clean':
            remove_csv_files()
        else:
            print("Usage: python main.py | python main.py clean (to remove CSV files)")
    else:
        scrap_news()
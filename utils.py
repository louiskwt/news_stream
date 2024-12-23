import os 

def process_bbc_headlines(link, scrapper):
    EXCLUDED_WORDS = ['British Broadcasting Corporation', 'Video', 'Sport', 'Home', 'Audio', 'Weather', 'Newsletters']
    title = link.text.strip()
    if title not in EXCLUDED_WORDS:
        href = scrapper.base_url + link['href']
        return {'title': title, 'link': href}
    else:
        return None

def process_guadian_headlines(link, scrapper):
    title = link['aria-label']
    href = scrapper.base_url + link['href']
    return {'title': title, 'link': href}

def remove_csv_files():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir_path)
    for file in files:
        if file.endswith(".csv"):
            os.remove(os.path.join(dir_path, file))
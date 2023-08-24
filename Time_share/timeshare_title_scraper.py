import requests
from bs4 import BeautifulSoup

def scrape_timeshare_titles(url):
    HEADERS = {
        'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                        'AppleWebKit/537.36 (KHTML, like Gecko)'
                        'Chrome/44.0.2403.157 Safari/537.36'),
        'Accept-Language': 'en-US, en;q=0.5'
    }

    html = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(html.text, 'html.parser')

    # Find all elements that contain the title
    titles = soup.find_all('div', {'class': 'brd-card__tit-innr'})

    # Extract and return the text of each title
    title_texts = [element.text.strip() for element in titles]
    return title_texts

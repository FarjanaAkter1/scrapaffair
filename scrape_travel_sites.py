import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.consumeraffairs.com/travel/travel-sites/"
HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64) '
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0 '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}

response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

company_title_elements = soup.find_all('a', class_='ca-a ca-a--bld-no-undln brd-card__tit-nm js-gadatalayer')

def extract_reviews(company_title):
    company_url = f"https://www.consumeraffairs.com/travel/{company_title}.html"
    company_response = requests.get(company_url, headers=HEADERS)
    company_soup = BeautifulSoup(company_response.content, 'html.parser')
    
    # Find the company name
    company_name_element = company_soup.find('span', class_='last-word-wrapper')
    if company_name_element:
        company_name = company_name_element.get_text(strip=True)
    else:
        company_name = "Company name not found"
    
    reviews = company_soup.find_all('div', class_='rvw__hdr-stat')
    
    results = []  # List to store results for each company
    
    # Find reviews and their rating values
    for review in reviews:
        review_text = review.find_next('div', class_='rvw__top-text').get_text(strip=True)
        rating_value_element = review.find('meta', itemprop='ratingValue')
        print("Rating Value Element:", rating_value_element)
        if rating_value_element and 'content' in rating_value_element.attrs:
            print("Content Attribute:", rating_value_element['content'])
            rating_value = int(rating_value_element['content'])
        else:
            rating_value = None
        results.append((company_name, rating_value, review_text))
    
    return results

# Create and open CSV file for writing
with open('reviews.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Company', 'Rating', 'Review'])
    
    # Loop through company titles and extract reviews
    for element in company_title_elements:
        company_title = element.get_text(strip=True)
        review_data = extract_reviews(company_title)
        
        for company_name, rating_value, review_text in review_data:
            csv_writer.writerow([company_name, rating_value, review_text])

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

def extract_reviews(company_title, page_number):
    company_url = f"https://www.consumeraffairs.com/travel/{company_title}.html?page={page_number}"
    company_response = requests.get(company_url, headers=HEADERS)
    company_soup = BeautifulSoup(company_response.content, 'html.parser')
    
    # Find the company name
    company_name_element = company_soup.find('span', class_='last-word-wrapper')
    if company_name_element:
        company_name = company_name_element.get_text(strip=True)
    else:
        company_name = "Company name not found"
    
    reviews = company_soup.find_all('div', class_='rvw__hdr-stat')
    
    results = []  # List to store results for each page
    
    # Find reviews and respective rating values
    for review in reviews:
        rating_value_element = review.find('meta', itemprop='ratingValue')
        if rating_value_element and 'content' in rating_value_element.attrs:
            rating_value = int(rating_value_element['content'])
        else:
            rating_value = None
        
        review_text = review.find_next('div', class_='rvw__top-text').get_text(strip=True)
        results.append((company_name, rating_value, review_text))
    
    return results

# Loop through company titles and extract reviews
with open('reviews.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Company', 'Rating', 'Review'])
    
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    company_title_elements = soup.find_all('a', class_='ca-a ca-a--bld-no-undln brd-card__tit-nm js-gadatalayer')
    
    for element in company_title_elements:
        company_title = element.get_text(strip=True)
        
        # Extract reviews from all pages for indivdual company (limit to 100)
        all_reviews = []
        page_number = 1
        reviews_fetched = 0
        while reviews_fetched < 100:
            review_data = extract_reviews(company_title, page_number)
            if not review_data:
                break
            all_reviews.extend(review_data)
            reviews_fetched += len(review_data)
            page_number += 1
            if reviews_fetched >= 100:
                break
        
        # Write the reviews to the CSV file
        for company_name, rating_value, review_text in all_reviews:
            csv_writer.writerow([company_name, rating_value, review_text])
    
print("Scraping complete and results saved to 'reviews.csv'.")

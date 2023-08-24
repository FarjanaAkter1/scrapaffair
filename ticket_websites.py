from bs4 import BeautifulSoup
import requests

def get_company_urls(website_url):
    page_to_parse = requests.get(website_url)
    soup = BeautifulSoup(page_to_parse.text, 'html.parser')
    companies = soup.find_all("a", attrs={"data-uapi-link": "company_name_cta"})

    url_array = []
    for each_company in companies:
        url = each_company['href']
        url_array.append(url)
    return url_array

def get_company_info(company_url):
    company_page_to_parse = requests.get(company_url)
    company_soup = BeautifulSoup(company_page_to_parse.text, "html.parser")
    
    line_with_company_name = company_soup.find("span", attrs={"style": "white-space: nowrap;"})
    
    if line_with_company_name:
        company_name = line_with_company_name.get_text() 
    else:
        company_name = "No Company Name"
    
    line_with_company_rating = company_soup.find("strong", attrs={"class": "prf-rtng__rtng-dsc"})
    if line_with_company_rating:
        company_rating = line_with_company_rating.get_text() 
    else: 
        company_rating = "No Company Rating"
    
    return company_name, company_rating

def main():
    website = "https://www.consumeraffairs.com/entertainment/ticket-websites/#highest-rated-all"
    company_urls = get_company_urls(website)

    for company_url in company_urls:
        company_name, company_rating = get_company_info(company_url)
        print(f'Company Name: {company_name}')
        print(f'Company Rating: {company_rating}')

if __name__ == "__main__":
    main()

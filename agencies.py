from bs4 import BeautifulSoup
import requests
import csv 

html = requests.get("https://www.consumeraffairs.com/travel/agencies.html")
soup = BeautifulSoup(html.text, 'html.parser')

companies = soup.findAll('a', attrs = {"data-uapi-link" : "company_name_cta"})

company_list = []
company_url_list = []


for company in companies: 
    company_list.append(company.text.strip())
    company_url_list.append(company.get('href'))



def agencies_info(agency_url):
    html = requests.get(agency_url)
    soup = BeautifulSoup(html.text, "html.parser")
    agency_names = soup.find("span", attrs={"class" : "last-word-wrapper"})
    name = agency_names = agency_names.get_text()
    
    rating = soup.find("strong", attrs = { "class": "prf-rtng__rtng-dsc"})
    agency_rating = rating.get_text()

    reviews = soup.find("div", attrs = {"class": "rvw__top-text"})
    agency_reviews = reviews.get_text()

    return [name, agency_rating, agency_reviews]




print(agencies_info(company_url_list[0]))







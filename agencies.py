from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.consumeraffairs.com/travel/agencies.html")
soup = BeautifulSoup(html.text, 'html.parser')

companies = soup.findAll('a', attrs = {"data-uapi-link" : "company_name_cta"})

for company in companies: 
    print(company.text)
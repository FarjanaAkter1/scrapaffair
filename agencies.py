from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.consumeraffairs.com/travel/agencies.html")
soup = BeautifulSoup(html.text, 'html.parser')

companies = soup.findAll('a', attrs = {"data-uapi-link" : "company_name_cta"})

company_list = []
company_url_list = []



for company in companies: 
    company_list.append(company.text.strip())
    company_url_list.append(company.get('href'))

# for link in companies_links: 
#     print(link.text)
# print(company_url_list)





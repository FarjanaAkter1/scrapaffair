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

    for agency in agency_names:
        print(agency.text)


# print(company_url_list)
# html2 = requests.get(company_url_list[0])
# soup2 = BeautifulSoup(html2.text, 'html.parser')
# reviews_div = soup2.findAll('div', attrs ={"class" : "rvw_top-text"})
# # reviews = reviews_div.find_all('p')

# print(reviews_div)

agencies_info(company_url_list[0])







#works 1///title
import requests
from bs4 import BeautifulSoup

url = "https://www.consumeraffairs.com/travel/timeshares.html"

HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko)'
                    'Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}

html = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(html.text, 'html.parser')

# Find all elements that contain the title
title = soup.find_all('div', {'class': 'brd-card__tit-innr'})

# Extract and print the text of each title of comapany
for element in title:
    text = element.text.strip()
    print(text)

################################################

## works 2//reviews
import requests
from bs4 import BeautifulSoup

url = "https://www.consumeraffairs.com/travel/newton-group-transfers.html"

HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko)'
                    'Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}

html = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(html.text, 'html.parser')

# Find all elements that contain the review text
review_elements = soup.find_all('div', {'class': 'rvw__top-text'}) 

# Extract and print the review text for each element
for review_element in review_elements:
    review_text = review_element.text.strip()
    print(review_text)

####################################################################

##### making csv ####

# import requests
# from bs4 import BeautifulSoup
# import csv

# url = "https://www.consumeraffairs.com/travel/timeshares.html"

# HEADERS = {
#     'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
#                     'AppleWebKit/537.36 (KHTML, like Gecko)'
#                     'Chrome/44.0.2403.157 Safari/537.36'),
#     'Accept-Language': 'en-US, en;q=0.5'
# }

# html = requests.get(url, headers=HEADERS)
# soup = BeautifulSoup(html.text, 'html.parser')

# # Find all div elements with the class 'brd-card__tit-innr'
# title_elements = soup.find_all('div', {'class': 'brd-card__tit-innr'})

# # Extract and store the text of each title in a list
# titles = [title_element.text.strip() for title_element in title_elements]

# # Create and write to a CSV file
# with open('titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Title'])  # Write a header row

#     for title in titles:
#         writer.writerow([title])

# print("CSV file 'titles.csv' has been created.")






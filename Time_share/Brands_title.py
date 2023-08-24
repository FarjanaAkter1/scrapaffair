
###  making  1st csv file with title only  ###############################################

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.consumeraffairs.com/travel/timeshares.html"

HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko)'
                    'Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}

html = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(html.text, 'html.parser')

# Find all div elements with the class 'brd-card__tit-innr'
title_elements = soup.find_all('div', {'class': 'brd-card__tit-innr'})

# Extract and store the text of each title in a list
titles = [title_element.text.strip() for title_element in title_elements]

# Create and write to a CSV file
with open('titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title'])  # Write a header row

    for title in titles:
        writer.writerow([title])

print("CSV file 'titles.csv' has been created.")



################ csv with  title , review and ratings ###########################



import requests
from bs4 import BeautifulSoup
import csv
import os

# Set the working directory to the location of 'titles.csv'
os.chdir(r'C:\Users\FarjanaAkter\Code\groupscrape\scrapaffair\Time_share')

def scrape_ratings(url):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.1234.5678 Safari/537.36'
    }

    # Send a GET request to the URL
    html = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(html.text, 'html.parser')

    # Find elements that contain the rating numbers and review comments
    rating_elements = soup.find_all('strong', {'class': 'prf-rtng__rtng-dsc'})
    rating_review = soup.find_all('div', {'class': 'rvw__top-text'})
    
    # Extract the review numbers from the rating elements
    review_numbers = [element.text.strip() for element in rating_elements]
    review_comments = [element.text.strip() for element in rating_review]

    return review_numbers, review_comments

# List of URLs to scrape
urls = [
    "https://www.consumeraffairs.com/travel/newton-group-transfers.html",
    "https://www.consumeraffairs.com/travel/sell-my-timeshare-now.html",
    "https://www.consumeraffairs.com/travel/consumer-consulting-group.html",
    "https://www.consumeraffairs.com/travel/vida-vacations.html",
    "https://www.consumeraffairs.com/travel/westgate.html",
    "https://www.consumeraffairs.com/travel/bluegreen.html",
    "https://www.consumeraffairs.com/travel/wyndham_vacation_resorts.html",
    "https://www.consumeraffairs.com/travel/rci.html",
    "https://www.consumeraffairs.com/travel/worldmark_travel_share.html",
    "https://www.consumeraffairs.com/travel/welk_resort.html",
    "https://www.consumeraffairs.com/travel/global_exchange_vacation_club.html",
    "https://www.consumeraffairs.com/travel/vacation_village_resorts.html",
    "https://www.consumeraffairs.com/travel/summer-bay-resort.html",
    "https://www.consumeraffairs.com/travel/westin-vacation-club.html",
    "https://www.consumeraffairs.com/travel/timeshares_by_owner.html",
    "https://www.consumeraffairs.com/travel/shell_vacation_club.html?",
    "https://www.consumeraffairs.com/travel/buyatimeshare_com.html?",
    "https://www.consumeraffairs.com/travel/calypso_cay.html?",
    "https://www.consumeraffairs.com/travel/timeshares_only.html?",
    "https://www.consumeraffairs.com/travel/the-manhattan-club.html",
    "https://www.consumeraffairs.com/travel/bluebayclub.html?",
    "https://www.consumeraffairs.com/travel/lost-valley-lake-resort.html"
]

# Create and write to the same CSV file, adding 'Review Comments' and 'Ratings Number' columns
with open('titles.csv', 'r', newline='', encoding='utf-8') as infile:
    with open('titles_with_ratings.csv', 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)  # Read the header row
        header.append('Review Comments')  # Add 'Review Comments' to the header row
        header.append('Ratings Number')  # Add 'Ratings Number' to the header row
        writer.writerow(header)  # Write the updated header row

        # Iterate through the list of URLs and scrape ratings
        for url in urls:
            review_numbers, review_comments = scrape_ratings(url)
            
            # Read the corresponding row from 'titles.csv'
            title_row = next(reader)

            # Add the review comments and rating number to the row
            title_row.append(' | '.join(review_comments))
            title_row.append(' | '.join(review_numbers))

            # Write the updated row to 'titles_with_ratings.csv'
            writer.writerow(title_row)

print("CSV file 'titles_with_ratings.csv' has been created.")

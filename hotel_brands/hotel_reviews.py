from bs4 import BeautifulSoup
import requests
from csv import writer

# HEADERS = {
#     'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64) '
#                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0 '
#                    'AppleWebKit/537.36 (KHTML, like Gecko) '
#                    'Chrome/44.0.2403.157 Safari/537.36'),
#     'Accept-Language': 'en-US, en;q=0.5'
# }

HEADERS = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/115.0.0.0 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.9'
}


response_names = requests.get("https://www.consumeraffairs.com/travel/hotels.html", headers=HEADERS)
soup_names = BeautifulSoup(response_names.text, 'html.parser')
hotel_list = soup_names.findAll(class_="ca-a ca-a--bld-no-undln brd-card__tit-nm js-gadatalayer")
# print("h: ", hotel_list)


def hotel_info():
    for item in hotel_list:
        hotel = item.text.strip()
        url = item["href"]
        response_reviews = requests.get(url)
        soup_reviews = BeautifulSoup(response_reviews.text, 'html.parser')
        ratings_container = soup_reviews.findAll(class_="rvw__dtls")

        result = []

        for rating in ratings_container:
            # Number of stars
            star_rating = int(rating.find_all(attrs={"itemprop": "ratingValue"})[0]['content'])
            # Review date
            review_date = rating.find_all(class_="rvw__rvd-dt")[0].text.lstrip("Reviewed ")
            # Reviews
            written_reviews = rating.select("p")[0].text

            result.append((star_rating, review_date, written_reviews))

    return result


with open("hotel_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["hotel", "star rating", "review date", "reviews"])

    for item in hotel_list:
        hotel = item.text.strip()
        reviews = hotel_info()

        for star_rating, review_date, written_reviews in reviews:
            csv_writer.writerow([hotel, star_rating, review_date, written_reviews])


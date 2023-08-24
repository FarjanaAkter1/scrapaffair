from bs4 import BeautifulSoup
import requests
from csv import writer


response_names = requests.get("https://www.consumeraffairs.com/travel/hotels.html")
soup_names = BeautifulSoup(response_names.text, 'html.parser')
hotel_list = soup_names.findAll(class_="ca-a ca-a--bld-no-undln brd-card__tit-nm js-gadatalayer")
# print(hotel_list)
# hotel_names = []
# hotel_names.append(hotel_list)
# for item in hotel_list:
#     hotel = item.text.strip()
#     hotel_names.append(hotel)
    # url = item["href"]
# print(hotel_names)


def hotel_info(hotel_name):
    response_reviews = requests.get(f"https://www.consumeraffairs.com/travel/{hotel_name}.html")
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
        reviews = hotel_info(hotel)

        for star_rating, review_date, written_reviews in reviews:
            csv_writer.writerow([hotel, star_rating, review_date, written_reviews])
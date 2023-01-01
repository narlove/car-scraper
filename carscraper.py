# car scraper

import requests
from bs4 import BeautifulSoup

def get_cars_from_page(URL):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0' } 
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="row flex-nowrap no-gutters")

    carsInListings = results.find_all("div", class_="listing-item card showcase")

    carNamesList = []

    for car in carsInListings:
        carInfo = car.find("div", class_="card-body")
        carFooter = car.find("div", class_="card-footer")

        carName = carInfo.find("a", class_="js-encode-search").text.strip()
        carPrice = carInfo.find("div", class_="price").find("a", class_="js-encode-search").text.strip()

        carKeyDetails = carInfo.find("ul", class_="key-details").find_all("li", class_="key-details__value")

        carOdom = carKeyDetails[0].text
        carBody = carKeyDetails[1].text
        carEngine = carKeyDetails[3].text

        carSellerType = carFooter.find("div", class_="seller-type").text.strip()
        carLocation = carFooter.find("div", class_="seller-location d-flex").text.strip()

        print(carName)
        carNamesList.append(carName)
        print(carPrice)

        print(carOdom)
        print(carBody)
        print(carEngine)

        print(carSellerType)
        print(carLocation)

        print("\n")


def generate_URL(pageNumber: int):
    offset = str(12 * pageNumber - 12)
    return "https://www.carsales.com.au/cars/?q=(And.Service.carsales._.Year.range(2012..)._.Price.range(..11000)._.Odometer.range(..130000)._.GenericGearType.Automatic.)&offset=" + offset

# for x in range(20):
#     get_cars_from_page(generate_URL(x))
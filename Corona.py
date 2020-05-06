import requests
from bs4 import BeautifulSoup


url = "https://www.worldometers.info/coronavirus/"

# STEP 1. get the HTML.
r = requests.get(url)
html_content = r.content
# print(html_content)

# STEP 2. Parse the HTML.
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())
data = soup.find_all("div", class_="maincounter-number")
# print(data)
print("CORONA'S TERROR ALLOVER THE WORLD")
print(" ")
print("Total Cases: ", data[0].text.strip())
print("Total Deaths: ", data[1].text.strip())
print("Total Recovered: ", data[2].text.strip())


# Live detector cases
# def coronaTracker():
#     url = "https://www.worldometers.info/coronavirus/"
#
#     # STEP 1. get the HTML.
#     r = requests.get(url)
#     html_content = r.content
#     # print(html_content)
#
#     # STEP 2. Parse the HTML.
#     soup = BeautifulSoup(html_content, "html.parser")
#     # print(soup.prettify())
#     data = soup.find_all("div", class_="maincounter-number")
#     d1 = data[0].text.strip()
#     d2 = data[1].text.strip()
#     d3 = data[2].text.strip()
#     return d1, d2, d3


# while True:
#     print(coronaTracker())

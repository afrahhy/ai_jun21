# from selenium import webdriver
# import pandas

# my_driver = "chromedriver.exe"
# driver = webdriver.Chrome(my_driver)

# sfw = "https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996"

# driver.get(sfw)
# sevendaylist = driver.find_element_by_xpath('//*[@id="seven-day-forecast-list"]')

# dayweather = sevendaylist.find_elements_by_class_name("content")

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

dict = {
}
sfwurl = "https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996"
sfwpage = requests.get(sfwurl)
sfwsoup = BeautifulSoup(sfwpage.content, "html.parser")

def convert(x):
    return round(((float(x) - 32) * 5.0/9.0), 2)

highlowtemp = []
boxtemp = sfwsoup.find('ul', id='seven-day-forecast-list')
highlows = boxtemp.find_all('p', class_="temp")
for temp in highlows:
    
    highlowtemp.append(temp.text)

incelsius = []
for temp in highlows:
    temp = temp.text
    temp = temp.split()
    x = (float(temp[1]))
    incelsius.append((convert(x)))

print(incelsius)

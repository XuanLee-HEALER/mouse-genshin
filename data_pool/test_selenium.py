from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os


def getDriver():
    # Instantiate options
    opts = Options()
    # opts.add_argument(" — headless") # Uncomment if the headless version needed
    # opts.binary_location = ""

    # Set the location of the webdriver
    chrome_driver = '/Users/mouselee/Documents/mixture/chrome_exe/chromedriver'

    # Instantiate a webdriver
    driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)

    return driver
    # Load the HTML page
    # driver.get('https://bbs.mihoyo.com/ys/obc/channel/map/189')


# Parse processed webpage with BeautifulSoup
# with open('./pages.html', 'w') as f:
#     f.write(driver.page_source)
# soup = BeautifulSoup(driver.page_source)
# print(soup.find('div', class_="collection-avatar__icon"))
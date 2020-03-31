import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


CHROME_DRIVER_PATH = f"{os.getcwd()}/chromedriver"


def get_chrome_driver():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.wait = WebDriverWait(driver, 5)

    return driver

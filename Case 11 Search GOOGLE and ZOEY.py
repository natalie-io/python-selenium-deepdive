from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import os
import time

chromeDriver = os.getcwd() + "\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriver)

driver.get("https://www.google.co.nz")

searchElement = driver.find_element_by_name("q")
searchElement.send_keys("ZOEY")
searchElement.send_keys(Keys.RETURN)

time.sleep(10)

driver.close()

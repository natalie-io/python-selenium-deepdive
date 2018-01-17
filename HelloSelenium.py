from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chromeDriver = os.getcwd() + "\\chromedriver.exe"

# instantiate web driver
driver = webdriver.Chrome(executable_path=chromeDriver)

# go to url
driver.get("https://www.flipkart.com")

# find element for search and place dell+enter
searchElement = driver.find_element_by_name("q")
searchElement.send_keys("DELL")
searchElement.send_keys(Keys.RETURN)

time.sleep(10)

# close driver
driver.close()

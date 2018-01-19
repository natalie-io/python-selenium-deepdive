from selenium import webdriver
import os
import time

chromeDriver = os.getcwd() + "\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriver)
driver.get("https://en.wikipedia.org")


element = driver.find_element_by_id("mw-headline")
print(element.txt)

time.sleep(10)

driver.close()

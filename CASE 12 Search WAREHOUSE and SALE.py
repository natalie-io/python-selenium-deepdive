from selenium import webdriver
import os
import time

chromeDriver = os.getcwd() + "\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriver)
driver.get("https://www.thewarehouse.co.nz/")

time.sleep(3)
elm = driver.find_element_by_link_text("Specials")
elm.click()
elm.click()

time.sleep(10)

driver.close()

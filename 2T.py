from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://github.com/VISHNUGIT2005/beginer/blob/main/chromedriver-win64/1.py")
driver.implicitly_wait(100)
time.sleep(10)


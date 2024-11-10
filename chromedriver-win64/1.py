from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "file:///C:/Users/vishn/Documents/selenium/main.html"

driver = webdriver.Chrome()
driver.get(url)

username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")

username.send_keys("vishnu")
password.send_keys("aaa111222")

search_box = driver.find_element(By.ID,"loginbtn")

search_box.send_keys(Keys.RETURN)

time.sleep(10)
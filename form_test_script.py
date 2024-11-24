from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import logging
logging.basicConfig(filename="error_log.txt",level=logging.ERROR)
url = "http://127.0.0.1:5500/main.html"
driver = webdriver.Chrome()
driver.get(url)
try:
   driver.find_element(By.ID, "userename")
except NoSuchElementException as e:
    logging.error(f"NoSuchElementException: {e}")

username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")

username.send_keys("vishnu")
password.send_keys("aaa111222")

search_box = driver.find_element(By.ID,"loginbtn")
search_box.send_keys(Keys.RETURN)

time.sleep(10000)



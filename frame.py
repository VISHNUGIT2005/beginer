from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

anchor_element = driver.find_element(By.CSS_SELECTOR, "a[href='/frames']")
anchor_element.click()
anchor_element = driver.find_element(By.CSS_SELECTOR, "a[href='/nested_frames']")
anchor_element.click()
anchor_element = driver.find_element(By.NAME, "frame-top")
anchor_element.click()
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
x=driver.find_element(By.TAG_NAME,  "body").text
print(x)
time.sleep(5)










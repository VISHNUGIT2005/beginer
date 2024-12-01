from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
x=driver.find_element(By.CSS_SELECTOR,  "a[href='/javascript_alerts']")
x.click()
button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
button.click()
alert = driver.switch_to.alert

print(alert.text)
alert.accept()
time.sleep(5)
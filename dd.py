from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

x=driver.find_element(By.CSS_SELECTOR,  "a[href='/dropdown']")
x.click()

dropdown = driver.find_element(By.ID,  "dropdown")
dropdown=Select(dropdown)
dropdown.select_by_visible_text("Option 1")
print("Selected Option 1")


time.sleep(3)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
x=driver.find_element(By.CSS_SELECTOR, "a[href='/upload']")
x.click()
y=driver.find_element(By.ID,  "content")
y.click()
z=driver.find_element(By.ID,  "file-upload")
filepath="C:\\Users\\vishn\\Pictures\\Screenshots\\htmlcode.jpg"
z.send_keys(filepath)
c=driver.find_element(By.ID,  "file-submit")

c.click()
a=driver.find_element(By.ID,"uploaded-files")
print(a.text)

time.sleep(30)
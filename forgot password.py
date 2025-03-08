from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)
x=driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[20]/a')

x.click()
time.sleep(3)
y=driver.find_element(By.ID, "email")
y.send_keys("vishnuraj0905@gmail.com")
time.sleep(3)
z=driver.find_element(By.XPATH,'//*[@id="form_submit"]').click()
time.sleep(5)

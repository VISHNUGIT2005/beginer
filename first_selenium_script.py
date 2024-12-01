from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///path/to/your/frame_example.html")

# Switch to frame
driver.switch_to.frame("frame1")
print("Inside Frame")
driver.switch_to.default_content()  # Switch back to main content
print("Outside Frame")
driver.quit()
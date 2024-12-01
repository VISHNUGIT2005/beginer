from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (Make sure to specify the correct path to your WebDriver)
driver = webdriver.Chrome()  # Or use webdriver.Firefox() for Firefox

try:
    # Navigate to the specified URL
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    # Switch to the main frame
    driver.switch_to.frame("frame-top")

    # Switch to the left frame
    driver.switch_to.frame("frame-left")

    # Get the content of the left frame
    content = driver.find_element(By.TAG_NAME, "body").text

    # Print the content
    print("Content from the left frame:")
    print(content)

    # You can also switch to the right frame if required
    # driver.switch_to.default_content()  # To switch back to the main frame
    # driver.switch_to.frame("frame-right")

finally:
    # Close the browser
    driver.quit()
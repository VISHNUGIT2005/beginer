# Import Selenium WebDriver
from selenium import webdriver

# Specify the path to the ChromeDriver
# If ChromeDriver is not in your system PATH, provide the exact path to the driver
url = "https://www.bing.com/search?q=google+maps&gs_lcrp=EgRlZGdlKgcIABBFGMIDMgcIABBFGMIDMgcIARBFGMIDMgcIAhBFGMIDMgcIAxBFGMIDMgcIBBBFGMIDMgcIBRBFGMID0gEKMTA4OTc5ajBqMagCBrACAQ&FORM=ANSPA1&PC=U531"

# Open Google
driver = webdriver.Chrome()
driver.get(url)
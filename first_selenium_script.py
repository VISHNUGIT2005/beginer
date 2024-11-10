# Import Selenium WebDriver
from selenium import webdriver

# Specify the path to the ChromeDriver
# If ChromeDriver is not in your system PATH, provide the exact path to the driver
url = "https://www.bing.com/search?q=google+maps&gs_lcrp=EgRlZGdlKgcIABBFGMIDMgcIABBFGMIDMgcIARBFGMIDMgcIAhBFGMIDMgcIAxBFGMIDMgcIBBBFGMIDMgcIBRBFGMID0gEKMTA4OTc5ajBqMagCBrACAQ&FORM=ANSPA1&PC=U531"

# Open Google
driver = webdriver.Chrome()
<<<<<<< HEAD
driver.get(url)
=======
driver.get(url)

# Print the title of the current webpage
print("Page Title is: ", driver.title)

# Close the browser
#hi vishnu
>>>>>>> 22972e942fd7b0a042f09de62ad83b2f47819b7d

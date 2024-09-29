from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (using Chrome in this case)
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")

    # Find the search box element on the page
    search_box = driver.find_element(By.NAME, "q")

    # Type "dog" into the search box
    search_box.send_keys("Cats")

    # Press Enter to perform the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(3)

    # Find text elements in the search results
    results = driver.find_elements(By.CLASS_NAME, "sATSHe")

    # Print out the text from each result
    for result in results:
        print(result.text)

finally:
    # Close the browser
    driver.quit()


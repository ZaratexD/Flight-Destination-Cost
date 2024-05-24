from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

# Setup Selenium WebDriver using webdriver_manager
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # Run in headless mode for faster execution
executable_path = '/usr/local/bin/geckodriver'

# Initialize the WebDriver
driver = webdriver.Firefox(executable_path=executable_path, options=options)

# URL of the flight schedule page
url = 'https://www.delta.com/flightstatus/schedule/SEA/FCO/2024-06-03'
driver.get(url)

# Wait for the page to load completely
time.sleep(10)  # Adjust the sleep time as necessary

try:
    # Locate the table element using the specified CSS selector
    table = driver.find_element(By.CSS_SELECTOR, '#maincontent > dl-flightschedule > div > div > div > div.row.main-panel > div.col-xl-9.col-lg-9.col-md-12.col-12.right-panel-holder.ng-star-inserted > div > dl-flightroutes > table')
    table_html = table.get_attribute('outerHTML')
    
    # Print the extracted table HTML
    print(table_html)

except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()

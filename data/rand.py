from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import time

# Setup Selenium WebDriver using webdriver_manager
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # Run in headless mode for faster execution

# Setup the GeckoDriver using Service
service = Service(GeckoDriverManager().install())

# Initialize the WebDriver
driver = webdriver.Firefox(service=service, options=options)

# URL of the flight schedule page
url = 'https://www.delta.com/flightstatus/schedule/SEA/FCO/2024-06-03'
driver.get(url)

# Wait for the page to load completely
time.sleep(10)  # Adjust the sleep time as necessary

try:
    # Locate the table element using the specified CSS selector
    table = driver.find_element(By.CSS_SELECTOR, '#maincontent > dl-flightschedule > div > div > div > div.row.main-panel > div.col-xl-9.col-lg-9.col-md-12.col-12.right-panel-holder.ng-star-inserted > div > dl-flightroutes > table')
    table_html = table.get_attribute('outerHTML')
    
    # Use BeautifulSoup to pretty-print the HTML
    soup = BeautifulSoup(table_html, 'lxml')
    pretty_table_html = soup.prettify()
    
    # Write the prettified HTML to a file
    with open("schedule.txt", "w", encoding="utf-8") as file:
        file.write(pretty_table_html)

    print("The schedule has been written to schedule.txt")

except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()

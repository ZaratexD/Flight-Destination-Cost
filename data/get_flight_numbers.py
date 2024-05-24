import requests
from bs4 import BeautifulSoup

# URL of the flight schedule page
url = 'https://www.delta.com/flightstatus/schedule/SEA/FCO/2024-06-03'

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    flights = soup.find_all(div)
    
    print(flights)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

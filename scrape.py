import requests
from bs4 import BeautifulSoup
import json

# Define a function to extract names and URLs from the given webpage
def extract_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the relevant elements containing names and URLs
    # This is a placeholder and needs to be adjusted based on the actual structure of the webpage
    elements = soup.find_all('a', href=True)
    
    # Extract names and URLs
    data = [{'name': el.get_text(), 'url': el['href']} for el in elements]
    
    # Return the extracted data
    return data

# URL of the webpage to extract data from
url = 'https://ypc.am/who-is-who/'

# Extract data and store it as JSON
extracted_data = extract_data(url)
json_data = json.dumps(extracted_data, indent=4)

# Save the JSON data to a file
with open('extracted_data.json', 'w') as file:
    file.write(json_data)

# Print a success message
print("Data has been extracted and stored as JSON in 'extracted_data.json'.")

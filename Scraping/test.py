import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP request to the website
url = "http://dcihrm.dci.daikin.co.jp/PSNWEB/Attendance/Employee.aspx"  # Replace with the website URL you want to read
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
inp = soup.find('input',id='ctl00_ContentPlaceHolder1_TextBox1')
print(inp)

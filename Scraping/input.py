
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys 
import pandas as pd
# Step 1: Set up the Edge WebDriver
import time

# driver_path = "C:/path/to/msedgedriver.exe"  # Update with the path to your msedgedriver.exe
driver_path ='C:/Users/peerapong.k.ITNB17_41256/Downloads/edgedriver_win64/msedgedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)

# Step 2: Open a website
url = "http://dcihrm.dci.daikin.co.jp/PSNWEB/Attendance/Employee.aspx"  # Replace with the URL you want to visit
driver.get(url)
input_element = driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_TextBox1')
input_element.send_keys("41179")
input_element.send_keys(Keys.RETURN)
# ctl00_ContentPlaceHolder1_Table1
# Optional: Wait for a few seconds to see the result
time.sleep(3)
table_element = driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_Table1')
table_data = []
tbody = table_element.find_element(By.TAG_NAME,'tbody')
rows = tbody.find_elements(By.TAG_NAME,'tr')
for row in rows:
        # Find all cells in the row
        cells = row.find_elements(By.TAG_NAME, "td")
        # Extract text from each cell and store in a list
        row_data = [cell.text for cell in cells]
        # Add row data to the table_data list
        if row_data[5] != '-':
            table_data.append(row_data)

    # Print or process the extracted table data
for row in table_data:
    time_period = row[2]
    time_period = time_period.split(' ')
    print(time_period[len(time_period)-1])

# # Read an Excel file into a DataFrame
# df = pd.read_excel('path/to/your/excel_file.xlsx', sheet_name='Sheet1')  # Specify the sheet name or index
# print(df)

# time.sleep(5)
# # Step 3: Close the browser
# driver.quit()
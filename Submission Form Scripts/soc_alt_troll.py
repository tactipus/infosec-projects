from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import csv
import random


path = '/Users/pnalzate/Desktop/InfoSec/Projects'  # your path goes here
service = Service(executable_path=path)
website =  "https://www.socialistalternative.org/join/"
driver = webdriver.Chrome(service=service)

driver.get(website)
time.sleep(5)

with open('info.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    count = 1

    for row in csv_reader:
        input_email = driver.find_element(by='xpath',
                                        value=f"//input[contains(@name, 'rsvp[email]')]")
        input_email.send_keys(row[1])

        input_zip = driver.find_element(by='xpath',
                                        value=f"//input[contains(@name, 'rsvp[zip_code]')]")
        input_zip.send_keys("10002")

        submit_button = driver.find_element(by='xpath', value="//input[contains(@type, 'submit')]")
        submit_button.click()
    
        print(f"Payload {count} has been sent!")
        count += 1

        driver.get(website)
        time.sleep(5)

time.sleep(5)
driver.quit()
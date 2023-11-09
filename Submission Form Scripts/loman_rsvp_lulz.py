from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import csv
import random


path = '/Users/pnalzate/Desktop/InfoSec/Projects/Submission\ Form\ Scripts/'  # your path goes here
service = Service(executable_path=path)
website =  "https://actionnetwork.org/events/lowman-july-branch-meeting-3?clear_id=true&source=email-feeling-fomo-we-can-fix-that-the-next-lowman-dsa-meeting-is-on-june-1st"
driver = webdriver.Chrome(service=service)

random_seconds = random.randrange(1, 720, 7)
time_to_wait = 720 - random_seconds

driver.get(website)

with open('list_of_emails.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    count = 1
    # process = []

    for row in csv_reader:
        time.sleep(random_seconds)
        
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
        time.sleep(time_to_wait)

time.sleep(5)
driver.quit()
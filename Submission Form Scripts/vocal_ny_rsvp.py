from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import csv


path = '/Users/pnalzate/Desktop/InfoSec/Projects'  # your path goes here
service = Service(executable_path=path)
website =  "https://vocal.ourpowerbase.net/civicrm/profile/create?gid=49&reset=1"
driver = webdriver.Chrome(service=service)

driver.get(website)
time.sleep(3)

with open('info.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    count = 1
    process = []


    for row in csv_reader:
        input_fname = driver.find_element(by='xpath',
                                        value=f"//input[contains(@name, 'first_name')]")
        input_fname.send_keys("NYC-DSA")

        input_lname = driver.find_element(by='xpath',
                                        value=f"//input[contains(@name, 'last_name')]")
        input_lname.send_keys("Red Rabbits Cyberwarfare Division")


        input_email = driver.find_element(by='xpath',
                                       value=f"//input[contains(@name, 'email-Primary')]")
        input_email.send_keys(row[1])

        submit_button = driver.find_element(by='xpath', value="//button[contains(@type, 'submit')]")
        submit_button.click()
        
        print(f"Payload {count} has been sent!")
        count += 1

        driver.get(website)
        time.sleep(3)

time.sleep(1)
driver.quit()
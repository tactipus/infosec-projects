from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import csv
import random


path = '/Users/pnalzate/Desktop/InfoSec/Projects/Submission\ Form\ Scripts/'  # your path goes here
service = Service(executable_path=path)
website =  "https://suffolkdsa.org/#contact"
driver = webdriver.Chrome(service=service)

driver.get(website)
time.sleep(5)

with open('info.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    count = 0

    for row in csv_reader:        
        if count == 5:
            print("All payloads delivered!")
            break
        
        input_email = driver.find_element(by='xpath',
                                        value=f"//input[contains(@name, 'Name')]")
        input_email.send_keys("Bull Meecham")
        
        input_email = driver.find_element(by='xpath',
                                        value=f"//input[contains(@name, 'Email')]")
        input_email.send_keys("red.rabbits.cyberwarfare@socialists.nyc")

        input_message = driver.find_element(by='xpath',
                                        value=f"//textarea[contains(@name, 'Message')]")
        input_message.send_keys("Keep on talking shit. We know what your co-chairs been saying about us. We're gonna come out & throw lobsters at you!.")

        submit_button = driver.find_element(by='xpath', value="//button[contains(@type, 'submit')]")
        driver.execute_script("arguments[0].click();", submit_button)
    
        print(f"Payload {count + 1} has been sent!")
        count += 1

        driver.get(website)
        time.sleep(2)

time.sleep(5)
driver.quit()
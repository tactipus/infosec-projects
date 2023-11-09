from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from fake_useragent import UserAgent
import time
import csv


path = '/Users/pnalzate/Desktop/BBH/Projects'  # your path goes here
service = Service(executable_path=path)
website =  "https://www.nyc.gov/site/nypd/about/about-nypd/email-the-commissioner.page"
driver = webdriver.Chrome(service=service)

count = 1

options = Options()
ua = UserAgent()


for x in range(500):
    driver.get(website)
    time.sleep(3)
    
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')

    wait = WebDriverWait(driver, 10)
    
    if wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "span6 about-description")]'))):
        driver.back()
    
    # code for finding the input fields and filling them out
    select_type = Select(driver.find_element(by='xpath',
                                    value=f"//select[contains(@name, 'Message Type')]"))
    select_type.select_by_value("Compliment")

    select_topic = Select(driver.find_element(by='xpath',
                                    value=f"//select[contains(@name, 'Topic')]"))
    select_topic.select_by_value("Complaints")

    input_message = driver.find_element(by='xpath',
                                    value=f"//textarea[contains(@name, 'Message')]")
    input_message.send_keys("Abolish the NYPD!")

    # code for sending the form
    submit_button = driver.find_element(by='xpath', value="//button[contains(@type, 'button')]")
    submit_button.click()
    
    print(f"Payload {count} has been sent!")
    count += 1

    driver.get(website)

time.sleep(1)
driver.quit()
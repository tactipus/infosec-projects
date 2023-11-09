import pandas as pd
import numpy as np
import os
import random
from faker import Faker
import csv

fake = Faker()

def faker_categorical(num=1000, seed=None):
    np.random.seed(seed)
    fake.seed_instance(seed)
    output = []
    for x in range(num):
        gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
        first_name = fake.first_name_male() if gender =="M" else fake.first_name_female()
        last_name = fake.last_name()
        
        output.append(
            {
                "Name": first_name + " " + last_name,
                "Email": f"{first_name}.{last_name}@{fake.domain_name()}"
            }
       )
    return output

info = faker_categorical()

myFile = open('list_of_emails.csv', 'w')
writer = csv.DictWriter(myFile, fieldnames=['Name', 'Email', 'Message'])
writer.writeheader()
writer.writerows(info)
myFile.close()
import pandas as pd
import numpy as np
import os
import random
from faker import Faker
import csv

fake = Faker()

def faker_categorical(num=500, seed=None):
    np.random.seed(seed)
    fake.seed_instance(seed)
    output = []
    for x in range(num):
        gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
        first_name = fake.first_name_male() if gender =="M" else fake.first_name_female()
        last_name = fake.last_name()
        
        output.append(
            {
                "Message": "Bueller?"
            }
       )
    return output

info = faker_categorical()

myFile = open('info.csv', 'w')
writer = csv.DictWriter(myFile, fieldnames=['Message'])
writer.writeheader()
writer.writerows(info)
myFile.close()
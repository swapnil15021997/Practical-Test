import csv
import pandas as pd
from datetime import date

with open("./csvfile.csv",'r') as file:
    reader = csv.reader(file, delimiter = '-')
    for row in reader:
        print("Output of CSV Data: ")
        print(row)

data = pd.read_csv("./csvfile.csv", parse_dates=['Birthdate'])
def calculateAge(bd: pd.Series)->pd.Series:
    today = pd.to_datetime(date.today())
    return (today-bd)/pd.Timedelta(days=365.25)

data['age'] = calculateAge(data.Birthdate)
print("Data After calculating Date of Birth ")
print(data)

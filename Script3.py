from csv import DictReader
import csv
import datetime
from datetime import datetime

with open('Python_exercises_QA_Engr (5) (1)/Updated_Python_exercises_QA_Engr/Jmeter_log1.jtl', 'r') as logfile, open(
        'response.csv', 'w') as csvfile:
    readlog = csv.reader(logfile)
    writecsv = csv.writer(csvfile)
    writecsv.writerows(readlog)
with open('response.csv', 'r') as read:
    readcsv = DictReader(read)
    for row in readcsv:
        if row['responseCode'] != '200':
            if row['timeStamp']:
                errorTime = datetime.fromtimestamp(float(row['timeStamp']) / 1000.0)
            print(errorTime, row['responseCode'], row['responseMessage'], row['failureMessage'])




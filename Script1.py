import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

testTree = ET.parse('Python_exercises_QA_Engr (5) (1)/Updated_Python_exercises_QA_Engr/test_payload1.xml')
testRoot = testTree.getroot()
x = input("X Value:")
y = input("Y Value:")
CurrentDate = datetime.today().strftime("%y%m%d")
for dep in testRoot.iter('DEPART'):
    dep.text = str(float(CurrentDate) + float(x))
for re in testRoot.iter('RETURN'):
    re.text = str(float(CurrentDate) + float(y))

testTree.write('Python_exercises_QA_Engr (5) (1)/Updated_Python_exercises_QA_Engr/test_payload1_update.xml')

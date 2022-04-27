import json

with open('Python_exercises_QA_Engr (5) (1)/Updated_Python_exercises_QA_Engr/test_payload.json', 'r') as file:
    data = json.load(file)
    x = input("Enter x value:")
    y = input("Enter y value:")
    for e in data:
        if x in data:
            data.pop(x, None)
            break
    for f in data:
        print(f)
        if y in data[f]:
            data[f].pop(y, None)
            break
        else:
            continue
with open('Python_exercises_QA_Engr (5) (1)/Updated_Python_exercises_QA_Engr/test_payload_update.json', 'w') as Ufile:
    data = json.dump(data, Ufile)

import json

with open(r'C:\Users\tharu\OneDrive\Desktop\penv prac\task 1\village-1.json') as f1, \
     open(r'C:\Users\tharu\OneDrive\Desktop\penv prac\task 1\village-2.json') as f2:
    village1 = json.load(f1)
    village2 = json.load(f2)

data1= {person['UUID']: person for person in village1}
data2= {person['UUID']: person for person in village2}

bothvillages = []
onlyvillage1 = []
onlyvillage2 = []


for uuid, person in data1.items():
    if uuid in data2:
        bothvillages.append(person)
    else:
        onlyvillage1.append(person)

for uuid, person in data2.items():
    if uuid not in data1:
        onlyvillage2.append(person)

result = {
    "Both Villages": bothvillages
}
result1 = {
    "Only Village-1": onlyvillage1
}
result2 = {
    "Only Village-2": onlyvillage2
}

with open('result.json', 'w') as fout:
    json.dump(result, fout)
    
with open('result1.json', 'w') as fout:
    json.dump(result1, fout)
    
with open('result2.json', 'w') as fout:
    json.dump(result2, fout)



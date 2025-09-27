
with open('notes.txt', 'w') as n:
    n.write('Привет, пидрила \n')
    n.write('Извинись \n')

with open ('notes.txt', 'r') as n:
    print(n.read())


import json

users = {'name': 'Salavat', 'role': 'QA Automation'}

with open('users.json', 'w') as u:
    json.dump(users, u)

with open('users.json', 'r') as u:
    loaded = json.load(u)
    print(loaded['name'])

import csv

with open('guys.csv', 'w') as g:
    write = csv.writer(g)
    write.writerow(['name', 'age'])
    write.writerow(['Salavat', '23'])
    write.writerow(['Alina', '23'])
    write.writerow(['Daniil', '21'])

with open('guys.csv', "r") as g:
    reader = csv.reader(g)
    for read in reader:
        print(read)
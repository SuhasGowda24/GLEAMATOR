#
# import csv
# with open('students.csv','w',newline='') as file:
#     writer=csv.writer(file)
#     writer.writerow(['Name','Age','Place'])
#     writer.writerow(['Ram',22,'Bengaluru'])
#     writer.writerow(['Shyam',21,'Mysore'])
# print('csv file created')

# with open('students.csv','r') as file:
#     reader=csv.reader(file)
# for row in reader:
#     print(row)


import json
# data={
#     'name':"ABC",
#     'Age':22,
#     'Place':"Bengaluru"
# }
# with open('students.json','w') as file:
#     json.dump(data,file)
# print('json file created')

with open('students.json','r') as file:
    data=json.load(file)
print(data['name'])
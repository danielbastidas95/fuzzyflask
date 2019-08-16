import csv

n = 1
data = [['Objetivo', 'Valor'], 
['Objetivo 1', 0], 
['Objetivo 2', 0],
['Objetivo 3', 0],
['Objetivo 4', 0],
['Objetivo 5', 0],
['Objetivo 6', 0],
['Objetivo 7', 0]]

with open('static/data/datamain.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data[n] = ['Objetivo', row['Valor']]
        n=n+1

data[2][1] = 17
print(data)


"""
#create and write csv file
 csvData = [['Objetivo', 'Valor'], 
 ['Objetivo 1', 1], 
 ['Objetivo 2', 2],
 ['Objetivo 3', 3],
 ['Objetivo 4', 4],
 ['Objetivo 5', 5],
 ['Objetivo 6', 6],
 ['Objetivo 7', 7]]

with open('static/data/datamain.csv', 'w') as csvFile:
writer = csv.writer(csvFile)
writer.writerows(csvData)
"""
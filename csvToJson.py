import csv
import json

csvFilePath = 'cases-19-05.csv'
jsonFilePath = 'cases.json'

data = []
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        data.append(csvRow)

root = {}
root['cases'] = data

with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(root, indent=4))

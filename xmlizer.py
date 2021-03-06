#ECON435 HW1 Q2(a)
#Author: Xiao FU
#UID:305448673

import csv

csvFile = 'FoodServiceData.csv'
xmlFile = 'FoodServiceData.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<FoodServiceData>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else: 
        xmlData.write('<foodservice>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</foodservice>' + "\n")
            
    rowNum +=1

xmlData.write('</FoodServiceData>' + "\n")
xmlData.close()

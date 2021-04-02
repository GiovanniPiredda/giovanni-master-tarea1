import requests
import csv
import os
import prepend

#Download daily updated source file from the  internet
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
dataSet = requests.get(url)

#Save source file in local
open(r"../tarea1/sourceFiles/owid-covid-data.csv", "wb").write(dataSet.content)

#Open source file for splitting info per country
with open(r"../tarea1/sourceFiles/owid-covid-data.csv") as sourceData:
    linesReader = csv.reader(sourceData)

    header = next(linesReader)

    for line in linesReader:
        lineStr = ','.join(line)

        with open(r"dataPerCountry/" + line[2] + ".csv", "a") as targetData:
            targetData.write(lineStr + "\n")

#Add header to the generated files
headerStr = ','.join(header) + "\n"

basePath = "dataPerCountry/"
for entry in os.listdir(basePath):
    if os.path.isfile(os.path.join(basePath, entry)):
        prepend.prepend_line(basePath + entry, headerStr)
import requests
import csv
import os

######################
# AUXILIARY FUNCTION #
######################

def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line)
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)


#################
# MAIN FUNCTION #
#################

def updateData():

    #Creation store directories
    if not os.path.exists("sourceFiles"):
        os.mkdir("sourceFiles")

    if not os.path.exists("dataPerCountry"):
        os.mkdir("dataPerCountry")

    #Download daily updated source file from the  internet
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    dataSet = requests.get(url)

    #Save source file in local
    open(r"sourceFiles/owid-covid-data.csv", "wb").write(dataSet.content)

    #Open source file for splitting info per country
    with open(r"sourceFiles/owid-covid-data.csv") as sourceData:
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
            prepend_line(basePath + entry, headerStr)
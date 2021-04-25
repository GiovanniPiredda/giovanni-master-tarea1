#######################################
# Documentation
#
# This function presents the basic global information for the user to get a
# fast glance of the global coronavirus situation
# In particular, displays the following info:
# - Country with the highest coronavirus incidence today ----------------> OK
# - Country with the lowest coronavirus incidence today -----------------> OK
# - Country with the highest coronavirus historical incidence -----------> OK
# - Country with the lowest coronavirus historical incidence ------------> OK
# - Country with the highest coronavirus increase over the last month
# - Country with the highest coronavirus decrease over the last month
#######################################

from datetime import datetime, timedelta
import os
import errno
import csv

def getSyntheticData():
    path = os.path.realpath('.') + '/dataPerCountry'

    files = os.listdir(path)

    today = datetime.date(datetime.now())
    oneMonthAgo = today - timedelta(days = 30)

    syntheticData = {
        "highestTodayValue": 0,
        "highestTodayCountry": "",
        "lowestTodayValue": 999999999999999,
        "lowestTodayCountry": "",
        "highestHistoricalValue": 0,
        "highestHistoricalCountry": "",
        "lowestHistoricalValue": 999999999999999,
        "lowestHistoricalCountry": "",
        "highestIncreaseOverLastMonthValue": 0,
        "highestIncreaseOverLastMonthCountry": "",
        "highestDecreaseOverLastMonthValue": 999999999999999,
        "highestDecreaseOverLastMonthCountry": "",
    }

    for countryData in files:
        try:
            path2Country = os.path.realpath('.') + "/dataPerCountry/" + countryData
            with open(path2Country, 'r') as f:

                reversedRows = reversed(list(csv.reader(f)))

                lastRow = next(reversedRows)

                # Getting the highest coronavirus incidence today
                if (lastRow[4] and float(lastRow[5]) > syntheticData.get("highestTodayValue")):
                    syntheticData["highestTodayValue"] = float(lastRow[4])
                    syntheticData["highestTodayCountry"] = lastRow[2]

                #Getting the lowest coronavirus incidence today
                if (lastRow[4] and float(lastRow[4]) < syntheticData.get("lowestTodayValue")):
                    syntheticData["lowestTodayValue"] = float(lastRow[4])
                    syntheticData["lowestTodayCountry"] = lastRow[2]

            f.close()

            with open(path2Country, 'r') as f:

                fileRows = list(csv.reader(f))

                totalHistoricCasesInCountry = 0.0
                monthyIncrease = 0.0

                for row in fileRows[1:]:
                    if (row[4]):
                        totalHistoricCasesInCountry += float(row[4])

                    if oneMonthAgo <= datetime.strptime(row[3], '%Y-%m-%d').date() <= today and row[5]:
                        monthyIncrease += float(row[5])

                if totalHistoricCasesInCountry > syntheticData.get("highestHistoricalValue"):
                    syntheticData["highestHistoricalValue"] = totalHistoricCasesInCountry
                    syntheticData["highestHistoricalCountry"] = countryData[:-3]

                if totalHistoricCasesInCountry < syntheticData.get("lowestHistoricalValue"):
                    syntheticData["lowestHistoricalValue"] = totalHistoricCasesInCountry
                    syntheticData["lowestHistoricalCountry"] = countryData[:-3]

                if monthyIncrease > syntheticData.get("highestIncreaseOverLastMonthValue"):
                    syntheticData["highestIncreaseOverLastMonthValue"] = monthyIncrease
                    syntheticData["highestIncreaseOverLastMonthCountry"] = countryData[:-3]

                if monthyIncrease < syntheticData.get("highestDecreaseOverLastMonthValue"):
                    syntheticData["highestDecreaseOverLastMonthValue"] = monthyIncrease
                    syntheticData["highestDecreaseOverLastMonthCountry"] = countryData[:-3]

            f.close()

        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise

    print ("-------------------------------------------------------------------------------------")
    print ("Results:")
    print()
    print(syntheticData.get("highestTodayCountry") +
          " is the country with the HIGHEST coronavirus" +
          " cases today with " + str(syntheticData.get("highestTodayValue")) +
          " cases")
    print()
    print(syntheticData.get("lowestTodayCountry") +
          " is the country with the LOWEST coronavirus" +
          " cases today with " + str(syntheticData.get("lowestTodayValue")) +
          " cases")
    print()
    print(syntheticData.get("highestHistoricalCountry") +
          " is the country with the HIGHEST coronavirus" +
          " cases IN HISTORY with " + str(syntheticData.get("highestHistoricalValue")) +
          " cases")
    print()
    print(syntheticData.get("lowestHistoricalCountry") +
          " is the country with the LOWEST coronavirus" +
          " cases IN HISTORY with " + str(syntheticData.get("lowestHistoricalValue")) +
          " cases")
    print()
    print(syntheticData.get("highestIncreaseOverLastMonthCountry") +
          " is the country with the HIGHEST coronavirus INCREASE over the last month" +
          " with " + str(syntheticData.get("highestIncreaseOverLastMonthValue")) +
          " new cases")
    print()
    print(syntheticData.get("highestDecreaseOverLastMonthCountry") +
          " is the country with the HIGHEST coronavirus DECREASE over the las month" +
          " with " + str(syntheticData.get("highestDecreaseOverLastMonthValue")) +
          " new cases")
    print("-------------------------------------------------------------------------------------")
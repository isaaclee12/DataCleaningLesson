#Hello


def main():

    # Provisional_Death_Counts_for_Coronavirus_Disease__COVID-19_.csv
    # COVID-19_Confirmed_Cases_and_Deaths_by_Race_Ethnicity.csv
    inputFileName = 'COVID-19_Confirmed_Cases_and_Deaths_by_Race_Ethnicity.csv'
    outputFileName = "clean.csv"

    try:

        inputFile = open(inputFileName,'r') #read

        outputFile = open(outputFileName,'w') #write



    except:

        print("ERROR: " + inputFileName + "could not be opened.")

    finally:

        inputLine = inputFile.readline()

        while inputLine != '':  # The EOF char is an empty string

            outputLine = inputLine #set outputline to be same by default

            for i in range(0,len(outputLine)):  #cleaner loop

                if outputLine[i] == ',' and outputLine[i+1] == ',': # if two ,, in a row, empty cell, new line is appended.
                    #print("OLD:",outputLine)
                    outputLine = outputLine[:i+1] + '0' + outputLine[i+1:] #insert 0 into outputLine
                    #print("NEW:",outputLine)
            #print(outputLine) #Print for debug

            outputFile.write(outputLine) #After cleaning, insert new line

            inputLine = inputFile.readline() #Go to the next inputLine

        print("done")
main()
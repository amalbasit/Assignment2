

# CHECK VALIDITY OF FILE AND OPEN IN READ MODE !!!

# MAKE SURE OUTPY IS BEING MADE IN ASSIGNMENT 2 FOLDER !!

class Preprocessor:

    def __init__(self, inputFile):

        self.inputFile = inputFile
        self.outputFile = 'out1.txt'


    def eliminateBlankLines(self):

        cleanLines = []

        with open(self.inputFile, 'r') as file:

            fileLines = file.readlines()

            for line in fileLines:

                if line.strip() == "":

                    pass

                else:

                    cleanLines.append(line)

            return cleanLines


    def eliminateHash(self, lines): 

        cleanLines = []

        for line in lines:

            if "#" in line:

                beforeHash = line.split("#", 1)[0]

                cleanLines.append(beforeHash)

            else:

                cleanLines.append(line)

        return cleanLines
    

    # def eliminateTripleQuotes(self, lines):  # should remove triple quote but also everything in between

    #     cleanLines = []
    #     insideQuotes = False

    #     for line in lines:

    #         while not insideQuotes:

    #             if "'''" in line or '"""' in line:
                
    #                 insideQuotes = True

    #                 continue

    #             else:

    #                 cleanLines.append(line)

    #     return cleanLines


    def eliminateTabsSpaces(self, lines): # UNNECESSARY TABS AND SPACES !!!!

        cleanLines = []

        for line in lines:

            newLine = line.strip()
            cleanLines.append("\n")
            cleanLines.append(newLine)

        return cleanLines


    def removeImportAnnotations(self, lines):

        cleanLines = []

        for line in lines:

            if "import" in line: 

                pass

            elif line.startswith("@"):

                pass

            else:

                cleanLines.append(line)

        return cleanLines
    

    def writeToFile(self, lines):

        with open(self.outputFile, 'w') as file:

           file.writelines(lines)


    def getFile(self):

        return self.outputFile
    

    def displayOutput(self):

        with open(self.outputFile, 'r') as file:

            print(file.read())


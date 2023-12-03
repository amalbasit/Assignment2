

class Processor:

    def __init__(self, inputFile):
        
        self.inputFile = inputFile 
        self.outputFile = 'out2.txt'

    
    def processFile(self):

        buffer = []

        with open(self.inputFile.getFile(), 'r') as file:

            while True: 

                char = file.read(1)

                if not char:

                    break

                elif char == "\n":

                    pass

                else:

                    buffer.append(char)

        buffer.append('$')

        return buffer


    def writeToFile(self, buffer):

        with open(self.outputFile, 'w') as file:

           file.write(str(buffer))


    def getFile(self):

        return self.outputFile
    
    
    def displayOutput(self, buffer):
        
        print("".join(buffer))
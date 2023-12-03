from preprocessorClass import Preprocessor
from processorClass import Processor
from lexicalAnalyzerClass import lexicalAnalyzer

FILE = r'C:\Users\amalb\Desktop\University !\Semesters\2023FALL\COMP111\Assignment 2\in1.txt'

preprocessorObj = Preprocessor(FILE)
blankLinesRemoved = preprocessorObj.eliminateBlankLines()
hashRemoved = preprocessorObj.eliminateHash(blankLinesRemoved)
spacesRemoved = preprocessorObj.eliminateTabsSpaces(hashRemoved)
allRemoved = preprocessorObj.removeImportAnnotations(spacesRemoved)
preprocessorObj.writeToFile(allRemoved)
preprocessorObj.displayOutput()
print()
processorObj = Processor(preprocessorObj)
processedFile = processorObj.processFile()
processorObj.writeToFile(processedFile)
processorObj.displayOutput(processedFile)
print()
lexemeAnalyzerObj = lexicalAnalyzer(processorObj)
buffer = lexemeAnalyzerObj.retrieveBuffer()
lexemeAnalyzerObj.lexemeBreakdown(buffer)
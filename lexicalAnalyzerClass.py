

class lexicalAnalyzer:

    def __init__(self, inputFile):
        
        self.inputFile = inputFile
        self.keywords = ["and", "as", "assert", "break", "class", "continue", 
                         "def", "del", "elif", "else", "except", "False", "finally", 
                         "for", "from", "global", "if", "import", "in", "is", "lambda", 
                         "None", "nonlocal", "not", "or", "pass", "raise", "return", 
                         "True", "try", "while", "with", "yield"]
        self.operators = ["+", "-", "*", "/", "%", "=", "+=", "-=", "*=", "/=", "==", "!=", "<", ">", "<=", ">="]
        self.punctuators = ["{", "}", "[", "]", "(", ")", ",", ";", ":", "."]

    def retrieveBuffer(self):

        with open(self.inputFile.getFile(), 'r') as file:

            content = file.read()

            buffer = eval(content)

            buffer.remove("$")

        return buffer
    

    def lexemeBreakdown(self, buffer):

        emptyStr = ""

        for character in buffer:

            if character.isalpha() or '_' in character:

                emptyStr += character 

            else:
                self.lexemeCheck(emptyStr)
                self.lexemeCheck(character)
                emptyStr = ""
  
        self.lexemeCheck(emptyStr)


    def lexemeCheck(self, lexeme): 

        if lexeme == ' ': # is this even working??

            pass

        elif lexeme in self.keywords:

            print(f"Lexeme: {lexeme}")


        elif lexeme.isalpha() or '_' in lexeme:

            print(f"Lexeme: {lexeme}")


        elif lexeme in self.operators:

            print(f"Lexeme: {lexeme}")


        elif lexeme in self.punctuators:

            print(f"Lexeme: {lexeme}")


        elif lexeme.isdigit(): # fix literals check

            print(f"Lexeme: {lexeme}")
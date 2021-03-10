import json
import sys

# HOW THE PROGRAM SHOULD BE CALLED
#
# You should have 3 files ready:
# 1.  Transition matrix file
# 2.  Input string file
# 3.  The output file
#
# Call
# py main.py <transition-matrix-file> <input-string-file> <output-file-name>

def parse(transitionMatrix, inputStr):
    index = 0
    state = transitionMatrix["startingState"]
    tokens = []

    while index < len(inputStr):
        value = ""

        # poor man's 'do-while'
        char = inputStr[index]
        index += 1

        if char in transitionMatrix["transitions"][state]:
            state = transitionMatrix["transitions"][state][char]
            if int(state) > 0:
                value += char
        else:
            state = transitionMatrix["errorState"]
            raise Exception("Reached error state at index " + str(index - 1) + ".")

        while index < len(inputStr) and int(state) < int(transitionMatrix["acceptingStateTreshold"]):
            char = inputStr[index]
            index += 1

            if char in transitionMatrix["transitions"][state]:
                state = transitionMatrix["transitions"][state][char]
                if int(state) > 0:
                    value += char
            else:
                state = transitionMatrix["errorState"]
                raise Exception("Reached error state at index " + str(index - 1) + ".")

        if int(state) > int(transitionMatrix["specialAcceptingStateTreshold"]) and not (int(state) == int(transitionMatrix["errorState"])):
            index -= 1
            value = value[:-1]

        if int(state) < int(transitionMatrix["acceptingStateTreshold"]):
            raise Exception("Finished without accepting state.")
        
        tokens.append({ "type": transitionMatrix["acceptingStates"][state], "value": value })
        state = transitionMatrix["startingState"]
    
    return tokens

def readTransMatrix():
    with open(sys.argv[1]) as transitionMatrixFile:
        return json.load(transitionMatrixFile)

def readInputString():
    with open(sys.argv[2]) as inStrFile:
        return inStrFile.read()

def writeOutput(tokens):
    with open(sys.argv[3], 'w') as outFile:
        json.dump(tokens, outFile, sort_keys=True, indent=4)

def main():
    transMatrix = readTransMatrix()
    inStr = readInputString()
    tokens = parse(transMatrix, inStr)
    writeOutput(tokens)

main()

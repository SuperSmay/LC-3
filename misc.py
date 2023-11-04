def isValid16BitBinary(input: str) ->  bool:
    return len(input) == 16 and len(input.replace('0', '').replace('1', '')) == 0

def isValidBinary(input: str) -> bool:
    return len(input.replace('0', '').replace('1', '')) == 0


def binaryStringToInt(input: str) -> int:
    total = 0
    value = 1
    isNegative = input[0] == '1'
    for char in input[1:][::-1]:  # Reverse string excluding first character
        if char == '0':
            if isNegative:
                total -= value
        elif char == '1':
            if not isNegative:
                total += value
        else:
            raise ValueError
        
        value *= 2

    if input[0] == '1':
        total -= 1

        
    return total

def fullAdder(inputOne: str, inputTwo: str):
    # This is the shittiest code ever btw

    result = []

    if len(inputOne) != len(inputTwo):
        raise ValueError("Inputs must be the same length")
    if not isValidBinary(inputOne) or not isValidBinary(inputTwo):
        raise ValueError("Inputs must be binary strings")
    
    carry = 0
    # Iterate through string in reverse and add each digit together
    for i in range(0, len(inputOne))[::-1]:

        add = int(inputOne[i]) + int(inputTwo[i]) + int(carry)

        if add == 3:
            carry = 1
            add = 1
        elif add == 2:
            carry = 1
            add = 0
        else:
            carry = 0

        result.insert(0, str(add))

    return ''.join(result)

def fullAnder(inputOne: str, inputTwo: str):
    # Lol

    result = []

    if len(inputOne) != len(inputTwo):
        raise ValueError("Inputs must be the same length")
    if not isValidBinary(inputOne) or not isValidBinary(inputTwo):
        raise ValueError("Inputs must be binary strings")
    
    # Iterate through string in reverse and add each digit together
    for i in range(0, len(inputOne))[::-1]:

        # I cannot believe this works lmfao
        result.insert(0, inputOne[i] and inputTwo[i])

    return ''.join(result)

def fullNotter(inputOne: str):
    # Lol

    result = []

    if not isValidBinary(inputOne):
        raise ValueError("Input must be a binary string")
    
    # Iterate through string in reverse and add each digit together
    for i in range(0, len(inputOne))[::-1]:

        opposite = not int(inputOne[i])
        result.insert(0, str(int(opposite)))

    return ''.join(result)

def sext5(input: str):
    if len(input) != 5:
        raise ValueError
    if not isValidBinary(input):
        raise ValueError
    
    sign = input[0]
    
    return sign*11 + input

def sext6(input: str):
    if len(input) != 6:
        raise ValueError
    if not isValidBinary(input):
        raise ValueError
    
    sign = input[0]
    
    return sign*10 + input

def sext9(input: str):
    if len(input) != 9:
        raise ValueError
    if not isValidBinary(input):
        raise ValueError
    
    sign = input[0]
    
    return sign*7 + input
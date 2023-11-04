def isValid16BitBinary(input: str):
    return len(input) == 16 and len(input.replace('0', '').replace('1', '')) == 0
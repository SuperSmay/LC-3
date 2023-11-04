from pathlib import Path

# This is gonna be jank but oh well
FILE_PATH = Path('memory')



def loadFileIntoList(filePath: Path) -> list[str]:
    
    loadedMemory: list[str] = []

    with open(filePath, 'r') as file:
        lines = file.readlines()
        for i in range(0, 2**16):
            if len(lines) > i:
                currentLine = lines[i]
                # Remove comments
                if '#' in currentLine:
                    commentIndex = currentLine.find('#')
                    currentLine = currentLine[:commentIndex]
                # Remove linebreaks and spaces
                currentLine = currentLine.replace('\n', '').replace(' ', '') 
                loadedMemory.append(get16BitFromInput(currentLine))
            else:
                loadedMemory.append('0000000000000000')
    
    return loadedMemory

def get16BitFromInput(inputData: str) -> str:
    if inputData == '':
        return '0000000000000000'
    elif inputData.startswith('0x'):
        return getBinaryFromHex(inputData.removeprefix('0x'))
    elif len(inputData) == 16 and len(inputData.replace('0', '').replace('1', '')) == 0:  # If the string is 16 bits long and only 0 and 1
        return inputData
    
    raise ValueError(f"Line {inputData} is malformed!")


def getBinaryFromHex(inputData: str) -> str:

    output = ''

    for char in inputData:
        match char:
            case '0':
                output += '0000'
            case '1':
                output += '0001'
            case '2':
                output += '0010'
            case '3':
                output += '0011'
            case '4':
                output += '0100'
            case '5':
                output += '0101'
            case '6':
                output += '0110'
            case '7':
                output += '0111'
            case '8':
                output += '1000'
            case '9':
                output += '1001'
            case 'A':
                output += '1010'
            case 'B':
                output += '1011'
            case 'C':
                output += '1100'
            case 'D':
                output += '1101'
            case 'E':
                output += '1110'
            case 'F':
                output += '1111'
            case _:
                raise ValueError(f"{char} is not valid hex")

    return output


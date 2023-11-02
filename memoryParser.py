from pathlib import Path

# This is gonna be jank but oh well
FILE_PATH = Path('memory')



def loadFileIntoList(filePath: Path) -> list[str]:
    
    loadedMemory: list[str] = []

    with open(filePath, 'r') as file:
        lines = file.readlines()
        for i in range(0, 2**16):
            if len(lines) > i:
                currentLine = lines[i].replace('\n', '')  # Remove linebreaks
                loadedMemory.append(get16BitFromInput(currentLine))
            else:
                loadedMemory.append('0000000000000000')
    
    return loadedMemory

def get16BitFromInput(inputData: str):
    if inputData == '':
        return '0000000000000000'
    elif inputData.startswith('0x'):
        return getBinaryFromHex(inputData)
    elif len(inputData) == 16 and len(inputData.replace('0', '').replace('1', '')) == 0:  # If the string is 16 bits long and only 0 and 1
        return inputData
    
    raise ValueError(f"Line {inputData} is malformed!")

def getBinaryFromHex(inputData: str):
    return '0000000000000000' # Placeholder



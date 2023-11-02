import unittest
import memoryParser
from pathlib import Path

class MemoryParserTests(unittest.TestCase):

    def testGetBinaryFromHex(self):
        self.assertEquals(memoryParser.getBinaryFromHex('0x0000'), '0000000000000000')
        self.assertEquals(memoryParser.getBinaryFromHex('0x123F'), '0001001000111111')
        with self.assertRaises(ValueError):
            memoryParser.getBinaryFromHex('hello')

    def testLoadFileIntoList(self):
        path = Path('testData')
        loadedList = memoryParser.loadFileIntoList(path)

        self.assertEquals(len(loadedList), 2**16, "Loaded List is wrong size")
        self.assertEquals(loadedList[0], '0000000000000000', "First line is loaded from file wrong")
        self.assertEquals(loadedList[1], '0000000000000000', "Second line is loaded from hex wrong")
        self.assertEquals(loadedList[2], '1111000011110000', "Third line is loaded from file wrong")
        self.assertEquals(loadedList[3], '0000000000000000', "Implicit zeros from blank line in file loaded incorrectly")
        self.assertEquals(loadedList[6], '1111111100000000', "Line after gaps loaded wrong")

if __name__ == '__main__':
    unittest.main()
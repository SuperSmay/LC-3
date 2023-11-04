import unittest
import misc

class MiscTests(unittest.TestCase):

    def testBinaryStringToInt(self):
        self.assertEqual(misc.binaryStringToInt('0000'), 0)
        self.assertEqual(misc.binaryStringToInt('1010'), 10)
        self.assertEqual(misc.binaryStringToInt('111000111'), 455)

    def testBinaryFullAdder(self):
        self.assertEquals(misc.fullAdder('0011', '1100'), '1111')
        self.assertEquals(misc.fullAdder('0101', '1100'), '0001')
        self.assertEquals(misc.fullAdder('1001', '1100'), '0101')

        with self.assertRaises(ValueError):
            misc.fullAdder('1111', '0')

        with self.assertRaises(ValueError):
            misc.fullAdder('1111', 'help')

    def testSexting(self):
        self.assertEquals(misc.sext5('01010'), '0000000000001010')
        self.assertEquals(misc.sext5('11010'), '1111111111111010')

        self.assertEquals(misc.sext9('010101010'), '0000000010101010')
        self.assertEquals(misc.sext9('110101010'), '1111111110101010')



if __name__ == '__main__':
    unittest.main()
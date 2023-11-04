import unittest
import decodeInstruction

class DecodeTests (unittest.TestCase):

    def testGetOpCode(self):
        self.assertEquals(decodeInstruction.getOpCode('10101111111111111111'), decodeInstruction.OpCode.LDI)

        with self.assertRaises(ValueError):
            decodeInstruction.getOpCode("hello")
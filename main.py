import memoryParser
import decodeInstruction
from pathlib import Path
from decodeInstruction import OpCode
import misc

class Processor:
    pc = '0000000000000000'
    memory = memoryParser.loadFileIntoList(Path('data'))
    instructionRegister = '0000000000000000'
    registerFile = ['0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000', '0000000000000000']

    conditionP = False
    conditionZ = False
    conditionN = False

    def runToHalt(self):
        pass

    def step(self):
        self.processInstruction()

    def stepOnKey(self):
        while True:
            self.step()
            print(f"After execution state:\n\tPC: {self.pc}\n\tIR:{self.instructionRegister}\n\tRegisters:{self.registerFile}")
            userInput = input()
            if userInput == 'q' or userInput == 'quit':
                break

    def processInstruction(self):
        # Fetch Instruction
        self.instructionRegister = self.memory[misc.binaryStringToInt(self.pc)]
        self.pc = misc.fullAdder(self.pc, '0000000000000001')
        # Decode
        opCode = decodeInstruction.getOpCode(self.instructionRegister)
        # Go wild
        match opCode:
            case OpCode.NOT:
                srcIndex = misc.binaryStringToInt(self.instructionRegister[7:10])
                dstIndex = misc.binaryStringToInt(self.instructionRegister[4:7])
                result = ''
                src = self.registerFile[srcIndex]

                result = misc.fullNotter(src)

                self.setRegister(dstIndex, result)
                
            case OpCode.ADD:
                src1Index = misc.binaryStringToInt(self.instructionRegister[7:10])
                dstIndex = misc.binaryStringToInt(self.instructionRegister[4:7])
                result = ''
                src1 = self.registerFile[src1Index]
                if self.instructionRegister[10] == '1':  # Immediate mode
                    immediate = self.instructionRegister[11:]
                    sextImmediate = misc.sext5(immediate)
                    result = misc.fullAdder(src1, sextImmediate)
                else:
                    src2Index = misc.binaryStringToInt(self.instructionRegister[13:])
                    src2 = self.registerFile[src2Index]
                    result = misc.fullAdder(src1, src2)

                self.setRegister(dstIndex, result)

            case OpCode.AND: # Copied from above but with and instead of add
                src1Index = misc.binaryStringToInt(self.instructionRegister[7:10])
                dstIndex = misc.binaryStringToInt(self.instructionRegister[4:7])
                result = ''
                src1 = self.registerFile[src1Index]
                if self.instructionRegister[10] == '1':  # Immediate mode
                    immediate = self.instructionRegister[11:]
                    sextImmediate = misc.sext5(immediate)
                    result = misc.fullAnder(src1, sextImmediate)
                else:
                    src2Index = misc.binaryStringToInt(self.instructionRegister[13:])
                    src2 = self.registerFile[src2Index]
                    result = misc.fullAnder(src1, src2)

                self.setRegister(dstIndex, result)

            case OpCode.LDR:
                srcIndex = misc.binaryStringToInt(self.instructionRegister[7:10])
                dstIndex = misc.binaryStringToInt(self.instructionRegister[4:7])
                sextOffset = misc.sext6(self.instructionRegister[10:])

                src = self.registerFile[srcIndex]

                memAddress = misc.fullAdder(sextOffset, src)

                result = self.memory[misc.binaryStringToInt(memAddress)]

                self.setRegister(dstIndex, result)

            case OpCode.STR:
                baseIndex = misc.binaryStringToInt(self.instructionRegister[7:10])
                srcIndex = misc.binaryStringToInt(self.instructionRegister[4:7])
                sextOffset = misc.sext6(self.instructionRegister[10:])

                base = self.registerFile[baseIndex]
                src = self.registerFile[srcIndex]

                memAddress = misc.fullAdder(sextOffset, base)

                self.memory[misc.binaryStringToInt(memAddress)] = src


                
            case OpCode.LD:
                sextOffset = misc.sext9(self.instructionRegister[7:])
                dstIndex = misc.binaryStringToInt(self.instructionRegister[4:7])
                memAddress = misc.fullAdder(sextOffset, self.pc)
                result = self.memory[misc.binaryStringToInt(memAddress)]

                self.setRegister(dstIndex, result)

            case OpCode.ST:
                sextOffset = misc.sext9(self.instructionRegister[7:])
                srcIndex = misc.binaryStringToInt(self.instructionRegister[4:7])
                memAddress = misc.fullAdder(sextOffset, self.pc)
                src = self.registerFile[srcIndex]

                self.memory[misc.binaryStringToInt(memAddress)] = src

            case OpCode.LDI:
                sextOffset = misc.sext9(self.instructionRegister[7:])
                dstIndex = misc.binaryStringToInt(self.instructionRegister[4:7])
                memAddress = misc.fullAdder(sextOffset, self.pc)
                effectiveAddress = self.memory[misc.binaryStringToInt(memAddress)]
                result = self.memory[misc.binaryStringToInt(effectiveAddress)]

                self.setRegister(dstIndex, result)

            case OpCode.STI:
                sextOffset = misc.sext9(self.instructionRegister[7:])
                srcIndex = misc.binaryStringToInt(self.instructionRegister[4:7])
                memAddress = misc.fullAdder(sextOffset, self.pc)
                effectiveAddress = self.memory[misc.binaryStringToInt(memAddress)]

                src = self.registerFile[srcIndex]

                self.memory[misc.binaryStringToInt(effectiveAddress)] = src

            case OpCode.LEA:
                sextOffset = misc.sext9(self.instructionRegister[7:])
                dstIndex = misc.binaryStringToInt(self.instructionRegister[4:7])
                result = misc.fullAdder(self.pc, sextOffset)

                self.setRegister(dstIndex, result)

            case OpCode.BR:
                if ((int(self.instructionRegister[4]) and self.conditionN) or
                    (int(self.instructionRegister[5]) and self.conditionZ) or
                    (int(self.instructionRegister[6]) and self.conditionP)):
                    sextOffset = misc.sext9(self.instructionRegister[7:])
                    self.pc = misc.fullAdder(self.pc, sextOffset)
                
            case OpCode.JMP:
                srcIndex = misc.binaryStringToInt(self.instructionRegister[7:10])
                src = self.registerFile[srcIndex]

                self.pc = src

            case OpCode.TRAP:
                pass

    def setRegister(self, registerIndex: int, value: str):
        self.registerFile[registerIndex] = value

        intValue = misc.binaryStringToInt(value)

        if intValue > 0:
            self.conditionN = False
            self.conditionZ = False
            self.conditionP = True
        elif intValue < 0:
            self.conditionN = True
            self.conditionZ = False
            self.conditionP = False
        else:
            self.conditionN = False
            self.conditionZ = True
            self.conditionP = False



if __name__ == '__main__':
    Processor().stepOnKey()

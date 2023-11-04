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

                self.registerFile[dstIndex] = result
                
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

                self.registerFile[dstIndex] = result

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

                self.registerFile[dstIndex] = result

            case OpCode.LDR:
                pass
            case OpCode.STR:
                pass
            case OpCode.LD:
                pass
            case OpCode.ST:
                pass
            case OpCode.LDI:
                pass
            case OpCode.STI:
                pass
            case OpCode.LEA:
                pass
            case OpCode.BR:
                pass
            case OpCode.JMP:
                pass
            case OpCode.TRAP:
                pass

    def NOT(self):
        pass

    def ADD(self):
        pass




if __name__ == '__main__':
    Processor().stepOnKey()

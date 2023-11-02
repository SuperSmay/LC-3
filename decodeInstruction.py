import enum

class OpCodes(enum.Enum):
    NOT = '1001'
    ADD = '0001'
    AND = '0101'
    LDR = '0110'
    STR = '0111'
    LD  = '0010'
    ST  = '0011'
    LDI = '1010'
    STI = '1011'
    LEA = '1110'
    BR  = '0000'
    JMP = '1100'
    TRAP= '1111'


from enum import Enum

class TokenType(Enum):
    NUM = 1
    ID = 2
    SLASH = 3
    COMMENT = 4
    COMMENT = 5
    COMMENT = 6
    COMMENT = 7
    ASTERISC = 8
    SMALLER = 9
    BIGGER = 11
    EQUALS = 13
    EXC = 15
    O_CURLY = 18
    C_CURLY = 17
    O_BRACKET = 20
    C_BRACKET = 19
    O_PAR = 22
    C_PAR = 21
    SEMICOLON = 24
    COMA = 23
    MINUS = 25
    PLUS = 26
    ENDFILE = 100
    SPACE = 0
    ELSE = 101
    IF = 102
    INT = 103
    RETURN = 104
    VOID = 105
    WHILE = 106
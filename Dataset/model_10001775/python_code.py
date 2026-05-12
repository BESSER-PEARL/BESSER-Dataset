from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Interpreter_ByteCodeLoader:

    def __init__(self, byteSource: str, program: str, byteCodeList: str):
        self.byteSource = byteSource
        self.program = program
        self.byteCodeList = byteCodeList
        
        pass
    @property
    def program(self):
        return self.__program
    @program.setter
    def program(self, program: str):
        self.__program = program

    @property
    def byteSource(self):
        return self.__byteSource
    @byteSource.setter
    def byteSource(self, byteSource: str):
        self.__byteSource = byteSource

    @property
    def byteCodeList(self):
        return self.__byteCodeList
    @byteCodeList.setter
    def byteCodeList(self, byteCodeList: str):
        self.__byteCodeList = byteCodeList



class Interpreter_ByteCode_Write:

    pass


class Interpreter_ByteCode_Store:

    def __init__(self, id: str, offset: int, value: int):
        self.id = id
        self.offset = offset
        self.value = value
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def offset(self):
        return self.__offset
    @offset.setter
    def offset(self, offset: int):
        self.__offset = offset



class Interpreter_ByteCode_Return:

    def __init__(self, funcname: str):
        self.funcname = funcname
        
        pass
    @property
    def funcname(self):
        return self.__funcname
    @funcname.setter
    def funcname(self, funcname: str):
        self.__funcname = funcname



class Interpreter_ByteCode_Read:

    pass


class Interpreter_ByteCode_Pop:

    def __init__(self, count: int):
        self.count = count
        
        pass
    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self, count: int):
        self.__count = count



class Interpreter_ByteCode_Load:

    def __init__(self, id: str, offset: int):
        self.id = id
        self.offset = offset
        
        pass
    @property
    def offset(self):
        return self.__offset
    @offset.setter
    def offset(self, offset: int):
        self.__offset = offset

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id



class Interpreter_ByteCode_Lit:

    def __init__(self, var: str, value: int):
        self.var = var
        self.value = value
        
        pass
    @property
    def var(self):
        return self.__var
    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value



class Interpreter_ByteCode_Label:

    def __init__(self, label: str):
        self.label = label
        
        pass
    @property
    def label(self):
        return self.__label
    @label.setter
    def label(self, label: str):
        self.__label = label



class Interpreter_ByteCode_Halt:

    pass


class Interpreter_ByteCode_GoTo:

    def __init__(self, address: int, label: str):
        self.address = address
        self.label = label
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: int):
        self.__address = address

    @property
    def label(self):
        return self.__label
    @label.setter
    def label(self, label: str):
        self.__label = label



class Interpreter_ByteCode_FalseBranch:

    def __init__(self, address: int, label: str):
        self.address = address
        self.label = label
        
        pass
    @property
    def label(self):
        return self.__label
    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: int):
        self.__address = address



class Interpreter_ByteCode_Dump:

    def __init__(self, stats: str):
        self.stats = stats
        
        pass
    @property
    def stats(self):
        return self.__stats
    @stats.setter
    def stats(self, stats: str):
        self.__stats = stats



class Interpreter_ByteCode_Call:

    def __init__(self, funcname: str, address: int):
        self.funcname = funcname
        self.address = address
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: int):
        self.__address = address

    @property
    def funcname(self):
        return self.__funcname
    @funcname.setter
    def funcname(self, funcname: str):
        self.__funcname = funcname



class Interpreter_ByteCode_BOP:

    def __init__(self, binaryOp: str):
        self.binaryOp = binaryOp
        
        pass
    @property
    def binaryOp(self):
        return self.__binaryOp
    @binaryOp.setter
    def binaryOp(self, binaryOp: str):
        self.__binaryOp = binaryOp



class Interpreter_ByteCode_Args:

    def __init__(self, nArgs: int):
        self.nArgs = nArgs
        
        pass
    @property
    def nArgs(self):
        return self.__nArgs
    @nArgs.setter
    def nArgs(self, nArgs: int):
        self.__nArgs = nArgs



class Interpreter_ByteCode_ByteCode:

    pass

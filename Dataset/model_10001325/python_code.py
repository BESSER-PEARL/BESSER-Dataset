from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class genmymodelreverse_C21:

    pass


class genmymodelreverse_C12:

    pass


class genmymodelreverse_java_util_Map_Interface(ABC):

    pass


class genmymodelreverse_C11:

    pass


class genmymodelreverse_java_util_Vector:

    pass


class genmymodelreverse_C2:

    pass


class genmymodelreverse_C1:

    pass


class genmymodelreverse_java_util_HashMap:

    pass


class genmymodelreverse_java_io_IOException:

    pass


class genmymodelreverse_java_util_Scanner:

    pass


class interpreter_VirtualMachine:

    def __init__(self, pc: int, isRunning: bool, dumpState: bool, returnAddrs: int, newProgram3: "interpreter_Program" = None, newRunStack5: "interpreter_RunTimeStack" = None):
        self.pc = pc
        self.isRunning = isRunning
        self.dumpState = dumpState
        self.returnAddrs = returnAddrs
        self.newProgram3 = newProgram3
        self.newRunStack5 = newRunStack5
        
        pass
    @property
    def pc(self):
        return self.__pc
    @pc.setter
    def pc(self, pc: int):
        self.__pc = pc

    @property
    def isRunning(self):
        return self.__isRunning
    @isRunning.setter
    def isRunning(self, isRunning: bool):
        self.__isRunning = isRunning

    @property
    def returnAddrs(self):
        return self.__returnAddrs
    @returnAddrs.setter
    def returnAddrs(self, returnAddrs: int):
        self.__returnAddrs = returnAddrs

    @property
    def dumpState(self):
        return self.__dumpState
    @dumpState.setter
    def dumpState(self, dumpState: bool):
        self.__dumpState = dumpState

    @property
    def newRunStack5(self):
        return self.__newRunStack5
    @newRunStack5.setter
    def newRunStack5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interpreter_VirtualMachine__newRunStack5", None)
        self.__newRunStack5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "virtualmachine4"):
                opp_val = getattr(old_value, "virtualmachine4", None)
                if opp_val == self:
                    setattr(old_value, "virtualmachine4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "virtualmachine4"):
                opp_val = getattr(value, "virtualmachine4", None)
                setattr(value, "virtualmachine4", self)

    @property
    def newProgram3(self):
        return self.__newProgram3
    @newProgram3.setter
    def newProgram3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interpreter_VirtualMachine__newProgram3", None)
        self.__newProgram3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "virtualmachine2"):
                opp_val = getattr(old_value, "virtualmachine2", None)
                if opp_val == self:
                    setattr(old_value, "virtualmachine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "virtualmachine2"):
                opp_val = getattr(value, "virtualmachine2", None)
                setattr(value, "virtualmachine2", self)



class interpreter_RunTimeStack:

    def __init__(self, runStack: str, framePointers: int, virtualmachine4: "interpreter_VirtualMachine" = None):
        self.runStack = runStack
        self.framePointers = framePointers
        self.virtualmachine4 = virtualmachine4
        
        pass
    @property
    def runStack(self):
        return self.__runStack
    @runStack.setter
    def runStack(self, runStack: str):
        self.__runStack = runStack

    @property
    def framePointers(self):
        return self.__framePointers
    @framePointers.setter
    def framePointers(self, framePointers: int):
        self.__framePointers = framePointers

    @property
    def virtualmachine4(self):
        return self.__virtualmachine4
    @virtualmachine4.setter
    def virtualmachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interpreter_RunTimeStack__virtualmachine4", None)
        self.__virtualmachine4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newRunStack5"):
                opp_val = getattr(old_value, "newRunStack5", None)
                if opp_val == self:
                    setattr(old_value, "newRunStack5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newRunStack5"):
                opp_val = getattr(value, "newRunStack5", None)
                setattr(value, "newRunStack5", self)



class interpreter_Program:

    def __init__(self, programMap: str, byteCodeVector: str, virtualmachine2: "interpreter_VirtualMachine" = None):
        self.programMap = programMap
        self.byteCodeVector = byteCodeVector
        self.virtualmachine2 = virtualmachine2
        
        pass
    @property
    def programMap(self):
        return self.__programMap
    @programMap.setter
    def programMap(self, programMap: str):
        self.__programMap = programMap

    @property
    def byteCodeVector(self):
        return self.__byteCodeVector
    @byteCodeVector.setter
    def byteCodeVector(self, byteCodeVector: str):
        self.__byteCodeVector = byteCodeVector

    @property
    def virtualmachine2(self):
        return self.__virtualmachine2
    @virtualmachine2.setter
    def virtualmachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interpreter_Program__virtualmachine2", None)
        self.__virtualmachine2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "newProgram3"):
                opp_val = getattr(old_value, "newProgram3", None)
                if opp_val == self:
                    setattr(old_value, "newProgram3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "newProgram3"):
                opp_val = getattr(value, "newProgram3", None)
                setattr(value, "newProgram3", self)



class interpreter_Interpreter:

    pass


class interpreter_CodeTable:

    def __init__(self, codeMap: str, byteCodesTXT: str):
        self.codeMap = codeMap
        self.byteCodesTXT = byteCodesTXT
        
        pass
    @property
    def byteCodesTXT(self):
        return self.__byteCodesTXT
    @byteCodesTXT.setter
    def byteCodesTXT(self, byteCodesTXT: str):
        self.__byteCodesTXT = byteCodesTXT

    @property
    def codeMap(self):
        return self.__codeMap
    @codeMap.setter
    def codeMap(self, codeMap: str):
        self.__codeMap = codeMap



class interpreter_ByteCodeLoader:

    def __init__(self, input: genmymodelreverse_java_util_Scanner, programMap: str, lineCount: int, interpreter0: "interpreter_Interpreter" = None):
        self.input = input
        self.programMap = programMap
        self.lineCount = lineCount
        self.interpreter0 = interpreter0
        
        pass
    @property
    def input(self):
        return self.__input
    @input.setter
    def input(self, input: genmymodelreverse_java_util_Scanner):
        self.__input = input

    @property
    def programMap(self):
        return self.__programMap
    @programMap.setter
    def programMap(self, programMap: str):
        self.__programMap = programMap

    @property
    def lineCount(self):
        return self.__lineCount
    @lineCount.setter
    def lineCount(self, lineCount: int):
        self.__lineCount = lineCount

    @property
    def interpreter0(self):
        return self.__interpreter0
    @interpreter0.setter
    def interpreter0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_interpreter_ByteCodeLoader__interpreter0", None)
        self.__interpreter0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bcl1"):
                opp_val = getattr(old_value, "bcl1", None)
                if opp_val == self:
                    setattr(old_value, "bcl1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bcl1"):
                opp_val = getattr(value, "bcl1", None)
                setattr(value, "bcl1", self)



class bytecode_WriteByteCode:

    def __init__(self, byteCode: str):
        self.byteCode = byteCode
        
        pass
    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode



class bytecode_StoreByteCode:

    def __init__(self, storeValue: int, storeID: str, byteCode: str, theArg: str):
        self.storeValue = storeValue
        self.storeID = storeID
        self.byteCode = byteCode
        self.theArg = theArg
        
        pass
    @property
    def theArg(self):
        return self.__theArg
    @theArg.setter
    def theArg(self, theArg: str):
        self.__theArg = theArg

    @property
    def storeID(self):
        return self.__storeID
    @storeID.setter
    def storeID(self, storeID: str):
        self.__storeID = storeID

    @property
    def storeValue(self):
        return self.__storeValue
    @storeValue.setter
    def storeValue(self, storeValue: int):
        self.__storeValue = storeValue

    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode



class bytecode_ReturnByteCode:

    def __init__(self, byteCode: str):
        self.byteCode = byteCode
        
        pass
    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode



class bytecode_ReadByteCode:

    def __init__(self, byteCode: str):
        self.byteCode = byteCode
        
        pass
    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode



class bytecode_PopByteCode:

    def __init__(self, byteCode: str, theArg: str, count: int):
        self.byteCode = byteCode
        self.theArg = theArg
        self.count = count
        
        pass
    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode

    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def theArg(self):
        return self.__theArg
    @theArg.setter
    def theArg(self, theArg: str):
        self.__theArg = theArg



class bytecode_LoadByteCode:

    def __init__(self, byteCode: str, loadOffset: int, loadID: str):
        self.byteCode = byteCode
        self.loadOffset = loadOffset
        self.loadID = loadID
        
        pass
    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode

    @property
    def loadID(self):
        return self.__loadID
    @loadID.setter
    def loadID(self, loadID: str):
        self.__loadID = loadID

    @property
    def loadOffset(self):
        return self.__loadOffset
    @loadOffset.setter
    def loadOffset(self, loadOffset: int):
        self.__loadOffset = loadOffset



class bytecode_LitByteCode:

    def __init__(self, byteCode: str, litValue: int, litID: str):
        self.byteCode = byteCode
        self.litValue = litValue
        self.litID = litID
        
        pass
    @property
    def litValue(self):
        return self.__litValue
    @litValue.setter
    def litValue(self, litValue: int):
        self.__litValue = litValue

    @property
    def litID(self):
        return self.__litID
    @litID.setter
    def litID(self, litID: str):
        self.__litID = litID

    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode



class bytecode_LabelByteCode:

    def __init__(self, lineNO: int, byteCode: str, theArg: str):
        self.lineNO = lineNO
        self.byteCode = byteCode
        self.theArg = theArg
        
        pass
    @property
    def theArg(self):
        return self.__theArg
    @theArg.setter
    def theArg(self, theArg: str):
        self.__theArg = theArg

    @property
    def lineNO(self):
        return self.__lineNO
    @lineNO.setter
    def lineNO(self, lineNO: int):
        self.__lineNO = lineNO

    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode



class bytecode_HaltByteCode:

    def __init__(self, byteCode: str):
        self.byteCode = byteCode
        
        pass
    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode



class bytecode_GoToByteCode:

    def __init__(self, byteCode: str, theArg: str, lineNO: int):
        self.byteCode = byteCode
        self.theArg = theArg
        self.lineNO = lineNO
        
        pass
    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode

    @property
    def lineNO(self):
        return self.__lineNO
    @lineNO.setter
    def lineNO(self, lineNO: int):
        self.__lineNO = lineNO

    @property
    def theArg(self):
        return self.__theArg
    @theArg.setter
    def theArg(self, theArg: str):
        self.__theArg = theArg



class bytecode_FalseBranchByteCode:

    def __init__(self, byteCode: str, theArg: str, lineNO: int):
        self.byteCode = byteCode
        self.theArg = theArg
        self.lineNO = lineNO
        
        pass
    @property
    def lineNO(self):
        return self.__lineNO
    @lineNO.setter
    def lineNO(self, lineNO: int):
        self.__lineNO = lineNO

    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode

    @property
    def theArg(self):
        return self.__theArg
    @theArg.setter
    def theArg(self, theArg: str):
        self.__theArg = theArg



class bytecode_DumpByteCode:

    def __init__(self, byteCode: str, theArg: str):
        self.byteCode = byteCode
        self.theArg = theArg
        
        pass
    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode

    @property
    def theArg(self):
        return self.__theArg
    @theArg.setter
    def theArg(self, theArg: str):
        self.__theArg = theArg



class bytecode_CallByteCode:

    def __init__(self, byteCode: str, theArg: str, lineNO: int):
        self.byteCode = byteCode
        self.theArg = theArg
        self.lineNO = lineNO
        
        pass
    @property
    def lineNO(self):
        return self.__lineNO
    @lineNO.setter
    def lineNO(self, lineNO: int):
        self.__lineNO = lineNO

    @property
    def theArg(self):
        return self.__theArg
    @theArg.setter
    def theArg(self, theArg: str):
        self.__theArg = theArg

    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode



class bytecode_ByteCode(ABC):

    pass


class bytecode_BopByteCode:

    def __init__(self, byteCode: str, theOperator: str):
        self.byteCode = byteCode
        self.theOperator = theOperator
        
        pass
    @property
    def theOperator(self):
        return self.__theOperator
    @theOperator.setter
    def theOperator(self, theOperator: str):
        self.__theOperator = theOperator

    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode



class bytecode_ArgsByteCode:

    def __init__(self, argCount: int, byteCode: str):
        self.argCount = argCount
        self.byteCode = byteCode
        
        pass
    @property
    def argCount(self):
        return self.__argCount
    @argCount.setter
    def argCount(self, argCount: int):
        self.__argCount = argCount

    @property
    def byteCode(self):
        return self.__byteCode
    @byteCode.setter
    def byteCode(self, byteCode: str):
        self.__byteCode = byteCode


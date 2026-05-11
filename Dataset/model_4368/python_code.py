from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Cardinals(Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"


############################################
# Definition of Classes
############################################

class BinaryOperation:

    pass
class minilang_Modulo(BinaryOperation):

    def __init__(self):
        
        pass
    def valueK3(self):
        # TODO: Implement valueK3 method
        pass

class minilang_Sum(BinaryOperation):

    def __init__(self):
        
        pass
    def valueK3(self):
        # TODO: Implement valueK3 method
        pass

class minilang_Value(ABC):

    def __init__(self, minilang_Value: "minilang_GreaterThan" = None, minilang_Value21: "minilang_GreaterThan" = None, minilang_Value28: "minilang_VariableAffect" = None, minilang_Value30: "minilang_BinaryOperation" = None, minilang_Value33: "minilang_BinaryOperation" = None):
        self.minilang_Value = minilang_Value
        self.minilang_Value21 = minilang_Value21
        self.minilang_Value28 = minilang_Value28
        self.minilang_Value30 = minilang_Value30
        self.minilang_Value33 = minilang_Value33
        
        pass
    @property
    def minilang_Value30(self):
        return self.__minilang_Value30

    @minilang_Value30.setter
    def minilang_Value30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Value__minilang_Value30", None)
        self.__minilang_Value30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_BinaryOperation"):
                opp_val = getattr(old_value, "minilang_BinaryOperation", None)
                if opp_val == self:
                    setattr(old_value, "minilang_BinaryOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_BinaryOperation"):
                opp_val = getattr(value, "minilang_BinaryOperation", None)
                setattr(value, "minilang_BinaryOperation", self)

    @property
    def minilang_Value21(self):
        return self.__minilang_Value21

    @minilang_Value21.setter
    def minilang_Value21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Value__minilang_Value21", None)
        self.__minilang_Value21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_GreaterThan20"):
                opp_val = getattr(old_value, "minilang_GreaterThan20", None)
                if opp_val == self:
                    setattr(old_value, "minilang_GreaterThan20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_GreaterThan20"):
                opp_val = getattr(value, "minilang_GreaterThan20", None)
                setattr(value, "minilang_GreaterThan20", self)

    @property
    def minilang_Value28(self):
        return self.__minilang_Value28

    @minilang_Value28.setter
    def minilang_Value28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Value__minilang_Value28", None)
        self.__minilang_Value28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_VariableAffect27"):
                opp_val = getattr(old_value, "minilang_VariableAffect27", None)
                if opp_val == self:
                    setattr(old_value, "minilang_VariableAffect27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_VariableAffect27"):
                opp_val = getattr(value, "minilang_VariableAffect27", None)
                setattr(value, "minilang_VariableAffect27", self)

    @property
    def minilang_Value33(self):
        return self.__minilang_Value33

    @minilang_Value33.setter
    def minilang_Value33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Value__minilang_Value33", None)
        self.__minilang_Value33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_BinaryOperation32"):
                opp_val = getattr(old_value, "minilang_BinaryOperation32", None)
                if opp_val == self:
                    setattr(old_value, "minilang_BinaryOperation32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_BinaryOperation32"):
                opp_val = getattr(value, "minilang_BinaryOperation32", None)
                setattr(value, "minilang_BinaryOperation32", self)

    @property
    def minilang_Value(self):
        return self.__minilang_Value

    @minilang_Value.setter
    def minilang_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Value__minilang_Value", None)
        self.__minilang_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_GreaterThan"):
                opp_val = getattr(old_value, "minilang_GreaterThan", None)
                if opp_val == self:
                    setattr(old_value, "minilang_GreaterThan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_GreaterThan"):
                opp_val = getattr(value, "minilang_GreaterThan", None)
                setattr(value, "minilang_GreaterThan", self)

    def valueK3(self):
        # TODO: Implement valueK3 method
        pass

class Condition:

    pass
class minilang_GreaterThan(Condition):

    def __init__(self, minilang_GreaterThan: "minilang_Value" = None, minilang_GreaterThan20: "minilang_Value" = None):
        self.minilang_GreaterThan = minilang_GreaterThan
        self.minilang_GreaterThan20 = minilang_GreaterThan20
        
        pass
    @property
    def minilang_GreaterThan20(self):
        return self.__minilang_GreaterThan20

    @minilang_GreaterThan20.setter
    def minilang_GreaterThan20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_GreaterThan__minilang_GreaterThan20", None)
        self.__minilang_GreaterThan20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Value21"):
                opp_val = getattr(old_value, "minilang_Value21", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Value21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Value21"):
                opp_val = getattr(value, "minilang_Value21", None)
                setattr(value, "minilang_Value21", self)

    @property
    def minilang_GreaterThan(self):
        return self.__minilang_GreaterThan

    @minilang_GreaterThan.setter
    def minilang_GreaterThan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_GreaterThan__minilang_GreaterThan", None)
        self.__minilang_GreaterThan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Value"):
                opp_val = getattr(old_value, "minilang_Value", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Value"):
                opp_val = getattr(value, "minilang_Value", None)
                setattr(value, "minilang_Value", self)

    def evalK3(self):
        # TODO: Implement evalK3 method
        pass

class minilang_Condition(ABC):

    def __init__(self, minilang_Condition: "minilang_IfStmt" = None):
        self.minilang_Condition = minilang_Condition
        
        pass
    @property
    def minilang_Condition(self):
        return self.__minilang_Condition

    @minilang_Condition.setter
    def minilang_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Condition__minilang_Condition", None)
        self.__minilang_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_IfStmt17"):
                opp_val = getattr(old_value, "minilang_IfStmt17", None)
                if opp_val == self:
                    setattr(old_value, "minilang_IfStmt17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_IfStmt17"):
                opp_val = getattr(value, "minilang_IfStmt17", None)
                setattr(value, "minilang_IfStmt17", self)

    def evalK3(self):
        # TODO: Implement evalK3 method
        pass

class Statement:

    pass
class minilang_CallMethod(Statement):

    def __init__(self, minilang_CallMethod: "minilang_Method" = None):
        self.minilang_CallMethod = minilang_CallMethod
        
        pass
    @property
    def minilang_CallMethod(self):
        return self.__minilang_CallMethod

    @minilang_CallMethod.setter
    def minilang_CallMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_CallMethod__minilang_CallMethod", None)
        self.__minilang_CallMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Method35"):
                opp_val = getattr(old_value, "minilang_Method35", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Method35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Method35"):
                opp_val = getattr(value, "minilang_Method35", None)
                setattr(value, "minilang_Method35", self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_VariableAffect(Statement):

    def __init__(self, minilang_VariableAffect: "minilang_Variable" = None, minilang_VariableAffect27: "minilang_Value" = None):
        self.minilang_VariableAffect = minilang_VariableAffect
        self.minilang_VariableAffect27 = minilang_VariableAffect27
        
        pass
    @property
    def minilang_VariableAffect27(self):
        return self.__minilang_VariableAffect27

    @minilang_VariableAffect27.setter
    def minilang_VariableAffect27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_VariableAffect__minilang_VariableAffect27", None)
        self.__minilang_VariableAffect27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Value28"):
                opp_val = getattr(old_value, "minilang_Value28", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Value28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Value28"):
                opp_val = getattr(value, "minilang_Value28", None)
                setattr(value, "minilang_Value28", self)

    @property
    def minilang_VariableAffect(self):
        return self.__minilang_VariableAffect

    @minilang_VariableAffect.setter
    def minilang_VariableAffect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_VariableAffect__minilang_VariableAffect", None)
        self.__minilang_VariableAffect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Variable25"):
                opp_val = getattr(old_value, "minilang_Variable25", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Variable25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Variable25"):
                opp_val = getattr(value, "minilang_Variable25", None)
                setattr(value, "minilang_Variable25", self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_RotateLeft(Statement):

    def __init__(self):
        
        pass
    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_RotateRight(Statement):

    def __init__(self):
        
        pass
    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_Move(Statement):

    def __init__(self):
        
        pass
    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_IfStmt(Statement):

    def __init__(self, minilang_IfStmt: "minilang_Block" = None, minilang_IfStmt14: "minilang_Block" = None, minilang_IfStmt17: "minilang_Condition" = None):
        self.minilang_IfStmt = minilang_IfStmt
        self.minilang_IfStmt14 = minilang_IfStmt14
        self.minilang_IfStmt17 = minilang_IfStmt17
        
        pass
    @property
    def minilang_IfStmt(self):
        return self.__minilang_IfStmt

    @minilang_IfStmt.setter
    def minilang_IfStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_IfStmt__minilang_IfStmt", None)
        self.__minilang_IfStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Block12"):
                opp_val = getattr(old_value, "minilang_Block12", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Block12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Block12"):
                opp_val = getattr(value, "minilang_Block12", None)
                setattr(value, "minilang_Block12", self)

    @property
    def minilang_IfStmt17(self):
        return self.__minilang_IfStmt17

    @minilang_IfStmt17.setter
    def minilang_IfStmt17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_IfStmt__minilang_IfStmt17", None)
        self.__minilang_IfStmt17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Condition"):
                opp_val = getattr(old_value, "minilang_Condition", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Condition"):
                opp_val = getattr(value, "minilang_Condition", None)
                setattr(value, "minilang_Condition", self)

    @property
    def minilang_IfStmt14(self):
        return self.__minilang_IfStmt14

    @minilang_IfStmt14.setter
    def minilang_IfStmt14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_IfStmt__minilang_IfStmt14", None)
        self.__minilang_IfStmt14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Block15"):
                opp_val = getattr(old_value, "minilang_Block15", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Block15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Block15"):
                opp_val = getattr(value, "minilang_Block15", None)
                setattr(value, "minilang_Block15", self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_Statement(ABC):

    def __init__(self, minilang_Statement: "minilang_Block" = None):
        self.minilang_Statement = minilang_Statement
        
        pass
    @property
    def minilang_Statement(self):
        return self.__minilang_Statement

    @minilang_Statement.setter
    def minilang_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Statement__minilang_Statement", None)
        self.__minilang_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Block10"):
                opp_val = getattr(old_value, "minilang_Block10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Block10"):
                opp_val = getattr(value, "minilang_Block10", None)
                if opp_val is None:
                    setattr(value, "minilang_Block10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_Block:

    def __init__(self, minilang_Block: "minilang_Method" = None, minilang_Block10: set["minilang_Statement"] = None, minilang_Block12: "minilang_IfStmt" = None, minilang_Block15: "minilang_IfStmt" = None):
        self.minilang_Block = minilang_Block
        self.minilang_Block10 = minilang_Block10 if minilang_Block10 is not None else set()
        self.minilang_Block12 = minilang_Block12
        self.minilang_Block15 = minilang_Block15
        
        pass
    @property
    def minilang_Block12(self):
        return self.__minilang_Block12

    @minilang_Block12.setter
    def minilang_Block12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Block__minilang_Block12", None)
        self.__minilang_Block12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_IfStmt"):
                opp_val = getattr(old_value, "minilang_IfStmt", None)
                if opp_val == self:
                    setattr(old_value, "minilang_IfStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_IfStmt"):
                opp_val = getattr(value, "minilang_IfStmt", None)
                setattr(value, "minilang_IfStmt", self)

    @property
    def minilang_Block10(self):
        return self.__minilang_Block10

    @minilang_Block10.setter
    def minilang_Block10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Block__minilang_Block10", None)
        self.__minilang_Block10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minilang_Statement"):
                    opp_val = getattr(item, "minilang_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "minilang_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minilang_Statement"):
                    opp_val = getattr(item, "minilang_Statement", None)
                    
                    setattr(item, "minilang_Statement", self)
                    

    @property
    def minilang_Block15(self):
        return self.__minilang_Block15

    @minilang_Block15.setter
    def minilang_Block15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Block__minilang_Block15", None)
        self.__minilang_Block15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_IfStmt14"):
                opp_val = getattr(old_value, "minilang_IfStmt14", None)
                if opp_val == self:
                    setattr(old_value, "minilang_IfStmt14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_IfStmt14"):
                opp_val = getattr(value, "minilang_IfStmt14", None)
                setattr(value, "minilang_IfStmt14", self)

    @property
    def minilang_Block(self):
        return self.__minilang_Block

    @minilang_Block.setter
    def minilang_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Block__minilang_Block", None)
        self.__minilang_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Method8"):
                opp_val = getattr(old_value, "minilang_Method8", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Method8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Method8"):
                opp_val = getattr(value, "minilang_Method8", None)
                setattr(value, "minilang_Method8", self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class Value:

    pass
class minilang_VariableRef(Value):

    def __init__(self, minilang_VariableRef: "minilang_Variable" = None):
        self.minilang_VariableRef = minilang_VariableRef
        
        pass
    @property
    def minilang_VariableRef(self):
        return self.__minilang_VariableRef

    @minilang_VariableRef.setter
    def minilang_VariableRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_VariableRef__minilang_VariableRef", None)
        self.__minilang_VariableRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Variable23"):
                opp_val = getattr(old_value, "minilang_Variable23", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Variable23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Variable23"):
                opp_val = getattr(value, "minilang_Variable23", None)
                setattr(value, "minilang_Variable23", self)

    def valueK3(self):
        # TODO: Implement valueK3 method
        pass

class minilang_BinaryOperation(Value):

    pass
class minilang_Constant(Value):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


    def valueK3(self):
        # TODO: Implement valueK3 method
        pass

class minilang_Variable:

    def __init__(self, name: str, value: float, minilang_Variable: "minilang_Program" = None, minilang_Variable23: "minilang_VariableRef" = None, minilang_Variable25: "minilang_VariableAffect" = None):
        self.name = name
        self.value = value
        self.minilang_Variable = minilang_Variable
        self.minilang_Variable23 = minilang_Variable23
        self.minilang_Variable25 = minilang_Variable25
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


    @property
    def minilang_Variable23(self):
        return self.__minilang_Variable23

    @minilang_Variable23.setter
    def minilang_Variable23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Variable__minilang_Variable23", None)
        self.__minilang_Variable23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_VariableRef"):
                opp_val = getattr(old_value, "minilang_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "minilang_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_VariableRef"):
                opp_val = getattr(value, "minilang_VariableRef", None)
                setattr(value, "minilang_VariableRef", self)

    @property
    def minilang_Variable25(self):
        return self.__minilang_Variable25

    @minilang_Variable25.setter
    def minilang_Variable25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Variable__minilang_Variable25", None)
        self.__minilang_Variable25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_VariableAffect"):
                opp_val = getattr(old_value, "minilang_VariableAffect", None)
                if opp_val == self:
                    setattr(old_value, "minilang_VariableAffect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_VariableAffect"):
                opp_val = getattr(value, "minilang_VariableAffect", None)
                setattr(value, "minilang_VariableAffect", self)

    @property
    def minilang_Variable(self):
        return self.__minilang_Variable

    @minilang_Variable.setter
    def minilang_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Variable__minilang_Variable", None)
        self.__minilang_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Program3"):
                opp_val = getattr(old_value, "minilang_Program3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Program3"):
                opp_val = getattr(value, "minilang_Program3", None)
                if opp_val is None:
                    setattr(value, "minilang_Program3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class minilang_Method:

    def __init__(self, name: str, Method: "minilang_Program" = None, minilang_Method: "minilang_Program" = None, methods: "minilang_Program" = None, minilang_Method8: "minilang_Block" = None, minilang_Method35: "minilang_CallMethod" = None):
        self.name = name
        self.Method = Method
        self.minilang_Method = minilang_Method
        self.methods = methods
        self.minilang_Method8 = minilang_Method8
        self.minilang_Method35 = minilang_Method35
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def minilang_Method8(self):
        return self.__minilang_Method8

    @minilang_Method8.setter
    def minilang_Method8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Method__minilang_Method8", None)
        self.__minilang_Method8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Block"):
                opp_val = getattr(old_value, "minilang_Block", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Block"):
                opp_val = getattr(value, "minilang_Block", None)
                setattr(value, "minilang_Block", self)

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Method__Method", None)
        self.__Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "program"):
                opp_val = getattr(old_value, "program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "program"):
                opp_val = getattr(value, "program", None)
                if opp_val is None:
                    setattr(value, "program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def minilang_Method35(self):
        return self.__minilang_Method35

    @minilang_Method35.setter
    def minilang_Method35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Method__minilang_Method35", None)
        self.__minilang_Method35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_CallMethod"):
                opp_val = getattr(old_value, "minilang_CallMethod", None)
                if opp_val == self:
                    setattr(old_value, "minilang_CallMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_CallMethod"):
                opp_val = getattr(value, "minilang_CallMethod", None)
                setattr(value, "minilang_CallMethod", self)

    @property
    def minilang_Method(self):
        return self.__minilang_Method

    @minilang_Method.setter
    def minilang_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Method__minilang_Method", None)
        self.__minilang_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Program"):
                opp_val = getattr(old_value, "minilang_Program", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Program"):
                opp_val = getattr(value, "minilang_Program", None)
                setattr(value, "minilang_Program", self)

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Method__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program"):
                opp_val = getattr(old_value, "Program", None)
                if opp_val == self:
                    setattr(old_value, "Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program"):
                opp_val = getattr(value, "Program", None)
                setattr(value, "Program", self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_Program:

    def __init__(self, distance: float, x: float, y: float, angle: str, minilang_Program5: set["minilang_Line"] = None, program: set["minilang_Method"] = None, minilang_Program: "minilang_Method" = None, minilang_Program3: set["minilang_Variable"] = None, Program: "minilang_Method" = None):
        self.distance = distance
        self.x = x
        self.y = y
        self.angle = angle
        self.minilang_Program5 = minilang_Program5 if minilang_Program5 is not None else set()
        self.program = program if program is not None else set()
        self.minilang_Program = minilang_Program
        self.minilang_Program3 = minilang_Program3 if minilang_Program3 is not None else set()
        self.Program = Program
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x


    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle


    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance: float):
        self.__distance = distance


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y


    @property
    def minilang_Program(self):
        return self.__minilang_Program

    @minilang_Program.setter
    def minilang_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Program__minilang_Program", None)
        self.__minilang_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Method"):
                opp_val = getattr(old_value, "minilang_Method", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Method"):
                opp_val = getattr(value, "minilang_Method", None)
                setattr(value, "minilang_Method", self)

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Program__program", None)
        self.__program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

    @property
    def minilang_Program3(self):
        return self.__minilang_Program3

    @minilang_Program3.setter
    def minilang_Program3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Program__minilang_Program3", None)
        self.__minilang_Program3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minilang_Variable"):
                    opp_val = getattr(item, "minilang_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "minilang_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minilang_Variable"):
                    opp_val = getattr(item, "minilang_Variable", None)
                    
                    setattr(item, "minilang_Variable", self)
                    

    @property
    def Program(self):
        return self.__Program

    @Program.setter
    def Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Program__Program", None)
        self.__Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methods"):
                opp_val = getattr(old_value, "methods", None)
                if opp_val == self:
                    setattr(old_value, "methods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methods"):
                opp_val = getattr(value, "methods", None)
                setattr(value, "methods", self)

    @property
    def minilang_Program5(self):
        return self.__minilang_Program5

    @minilang_Program5.setter
    def minilang_Program5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Program__minilang_Program5", None)
        self.__minilang_Program5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minilang_Line"):
                    opp_val = getattr(item, "minilang_Line", None)
                    
                    if opp_val == self:
                        setattr(item, "minilang_Line", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minilang_Line"):
                    opp_val = getattr(item, "minilang_Line", None)
                    
                    setattr(item, "minilang_Line", self)
                    

    def mainK3(self):
        # TODO: Implement mainK3 method
        pass

class minilang_Line:

    def __init__(self, x1: float, y1: float, x2: float, y2: float, minilang_Line: "minilang_Program" = None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.minilang_Line = minilang_Line
        
        pass
    @property
    def x1(self):
        return self.__x1

    @x1.setter
    def x1(self, x1: float):
        self.__x1 = x1


    @property
    def y1(self):
        return self.__y1

    @y1.setter
    def y1(self, y1: float):
        self.__y1 = y1


    @property
    def y2(self):
        return self.__y2

    @y2.setter
    def y2(self, y2: float):
        self.__y2 = y2


    @property
    def x2(self):
        return self.__x2

    @x2.setter
    def x2(self, x2: float):
        self.__x2 = x2


    @property
    def minilang_Line(self):
        return self.__minilang_Line

    @minilang_Line.setter
    def minilang_Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Line__minilang_Line", None)
        self.__minilang_Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Program5"):
                opp_val = getattr(old_value, "minilang_Program5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Program5"):
                opp_val = getattr(value, "minilang_Program5", None)
                if opp_val is None:
                    setattr(value, "minilang_Program5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

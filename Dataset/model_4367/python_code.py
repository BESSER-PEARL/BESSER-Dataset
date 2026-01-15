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

class Value:

    pass
class minilang_VariableRef(Value):

    def __init__(self, minilang_VariableRef: "minilang_Variable" = None):
        self.minilang_VariableRef = minilang_VariableRef
        
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
            if hasattr(old_value, "minilang_Variable26"):
                opp_val = getattr(old_value, "minilang_Variable26", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Variable26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Variable26"):
                opp_val = getattr(value, "minilang_Variable26", None)
                setattr(value, "minilang_Variable26", self)

    def valueK3(self):
        # TODO: Implement valueK3 method
        pass

class minilang_Constant(Value):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    def valueK3(self):
        # TODO: Implement valueK3 method
        pass

class minilang_BinaryOperation(Value):

    pass
class BinaryOperation:

    pass
class minilang_Modulo(BinaryOperation):

    def __init__(self):
        
    def valueK3(self):
        # TODO: Implement valueK3 method
        pass

class minilang_Sum(BinaryOperation):

    def __init__(self):
        
    def valueK3(self):
        # TODO: Implement valueK3 method
        pass

class minilang_Statement(ABC):

    def __init__(self, minilang_Statement: "minilang_Block" = None):
        self.minilang_Statement = minilang_Statement
        
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
            if hasattr(old_value, "minilang_Block13"):
                opp_val = getattr(old_value, "minilang_Block13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Block13"):
                opp_val = getattr(value, "minilang_Block13", None)
                if opp_val is None:
                    setattr(value, "minilang_Block13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_Value(ABC):

    def __init__(self, minilang_Value: "minilang_GreaterThan" = None, minilang_Value24: "minilang_GreaterThan" = None, minilang_Value31: "minilang_VariableAffect" = None, minilang_Value33: "minilang_BinaryOperation" = None, minilang_Value36: "minilang_BinaryOperation" = None):
        self.minilang_Value = minilang_Value
        self.minilang_Value24 = minilang_Value24
        self.minilang_Value31 = minilang_Value31
        self.minilang_Value33 = minilang_Value33
        self.minilang_Value36 = minilang_Value36
        
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
    def minilang_Value24(self):
        return self.__minilang_Value24

    @minilang_Value24.setter
    def minilang_Value24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Value__minilang_Value24", None)
        self.__minilang_Value24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_GreaterThan23"):
                opp_val = getattr(old_value, "minilang_GreaterThan23", None)
                if opp_val == self:
                    setattr(old_value, "minilang_GreaterThan23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_GreaterThan23"):
                opp_val = getattr(value, "minilang_GreaterThan23", None)
                setattr(value, "minilang_GreaterThan23", self)

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

    @property
    def minilang_Value36(self):
        return self.__minilang_Value36

    @minilang_Value36.setter
    def minilang_Value36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Value__minilang_Value36", None)
        self.__minilang_Value36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_BinaryOperation35"):
                opp_val = getattr(old_value, "minilang_BinaryOperation35", None)
                if opp_val == self:
                    setattr(old_value, "minilang_BinaryOperation35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_BinaryOperation35"):
                opp_val = getattr(value, "minilang_BinaryOperation35", None)
                setattr(value, "minilang_BinaryOperation35", self)

    @property
    def minilang_Value31(self):
        return self.__minilang_Value31

    @minilang_Value31.setter
    def minilang_Value31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Value__minilang_Value31", None)
        self.__minilang_Value31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_VariableAffect30"):
                opp_val = getattr(old_value, "minilang_VariableAffect30", None)
                if opp_val == self:
                    setattr(old_value, "minilang_VariableAffect30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_VariableAffect30"):
                opp_val = getattr(value, "minilang_VariableAffect30", None)
                setattr(value, "minilang_VariableAffect30", self)

    def valueK3(self):
        # TODO: Implement valueK3 method
        pass

class Condition:

    pass
class minilang_GreaterThan(Condition):

    def __init__(self, minilang_GreaterThan: "minilang_Value" = None, minilang_GreaterThan23: "minilang_Value" = None):
        self.minilang_GreaterThan = minilang_GreaterThan
        self.minilang_GreaterThan23 = minilang_GreaterThan23
        
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

    @property
    def minilang_GreaterThan23(self):
        return self.__minilang_GreaterThan23

    @minilang_GreaterThan23.setter
    def minilang_GreaterThan23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_GreaterThan__minilang_GreaterThan23", None)
        self.__minilang_GreaterThan23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Value24"):
                opp_val = getattr(old_value, "minilang_Value24", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Value24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Value24"):
                opp_val = getattr(value, "minilang_Value24", None)
                setattr(value, "minilang_Value24", self)

    def evalK3(self):
        # TODO: Implement evalK3 method
        pass

class minilang_Condition(ABC):

    def __init__(self, minilang_Condition: "minilang_IfStmt" = None):
        self.minilang_Condition = minilang_Condition
        
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
            if hasattr(old_value, "minilang_IfStmt20"):
                opp_val = getattr(old_value, "minilang_IfStmt20", None)
                if opp_val == self:
                    setattr(old_value, "minilang_IfStmt20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_IfStmt20"):
                opp_val = getattr(value, "minilang_IfStmt20", None)
                setattr(value, "minilang_IfStmt20", self)

    def evalK3(self):
        # TODO: Implement evalK3 method
        pass

class Statement:

    pass
class minilang_RotateLeft(Statement):

    def __init__(self):
        
    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_VariableAffect(Statement):

    def __init__(self, minilang_VariableAffect30: "minilang_Value" = None, minilang_VariableAffect: "minilang_Variable" = None):
        self.minilang_VariableAffect30 = minilang_VariableAffect30
        self.minilang_VariableAffect = minilang_VariableAffect
        
    @property
    def minilang_VariableAffect30(self):
        return self.__minilang_VariableAffect30

    @minilang_VariableAffect30.setter
    def minilang_VariableAffect30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_VariableAffect__minilang_VariableAffect30", None)
        self.__minilang_VariableAffect30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Value31"):
                opp_val = getattr(old_value, "minilang_Value31", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Value31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Value31"):
                opp_val = getattr(value, "minilang_Value31", None)
                setattr(value, "minilang_Value31", self)

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
            if hasattr(old_value, "minilang_Variable28"):
                opp_val = getattr(old_value, "minilang_Variable28", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Variable28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Variable28"):
                opp_val = getattr(value, "minilang_Variable28", None)
                setattr(value, "minilang_Variable28", self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_RotateRight(Statement):

    def __init__(self):
        
    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_Move(Statement):

    def __init__(self):
        
    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_CallMethod(Statement):

    def __init__(self, minilang_CallMethod: "minilang_Method" = None):
        self.minilang_CallMethod = minilang_CallMethod
        
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
            if hasattr(old_value, "minilang_Method38"):
                opp_val = getattr(old_value, "minilang_Method38", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Method38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Method38"):
                opp_val = getattr(value, "minilang_Method38", None)
                setattr(value, "minilang_Method38", self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_IfStmt(Statement):

    def __init__(self, minilang_IfStmt: "minilang_Block" = None, minilang_IfStmt17: "minilang_Block" = None, minilang_IfStmt20: "minilang_Condition" = None):
        self.minilang_IfStmt = minilang_IfStmt
        self.minilang_IfStmt17 = minilang_IfStmt17
        self.minilang_IfStmt20 = minilang_IfStmt20
        
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
            if hasattr(old_value, "minilang_Block18"):
                opp_val = getattr(old_value, "minilang_Block18", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Block18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Block18"):
                opp_val = getattr(value, "minilang_Block18", None)
                setattr(value, "minilang_Block18", self)

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
            if hasattr(old_value, "minilang_Block15"):
                opp_val = getattr(old_value, "minilang_Block15", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Block15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Block15"):
                opp_val = getattr(value, "minilang_Block15", None)
                setattr(value, "minilang_Block15", self)

    @property
    def minilang_IfStmt20(self):
        return self.__minilang_IfStmt20

    @minilang_IfStmt20.setter
    def minilang_IfStmt20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_IfStmt__minilang_IfStmt20", None)
        self.__minilang_IfStmt20 = value
        
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

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_Method:

    def __init__(self, name: str, minilang_Method: "minilang_Program" = None, 8: "minilang_Program" = None, minilang_Method11: "minilang_Block" = None, 1: "minilang_Program" = None, minilang_Method38: "minilang_CallMethod" = None):
        self.name = name
        self.minilang_Method = minilang_Method
        self.8 = 8
        self.minilang_Method11 = minilang_Method11
        self.1 = 1
        self.minilang_Method38 = minilang_Method38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Method__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def minilang_Method38(self):
        return self.__minilang_Method38

    @minilang_Method38.setter
    def minilang_Method38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Method__minilang_Method38", None)
        self.__minilang_Method38 = value
        
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
    def minilang_Method11(self):
        return self.__minilang_Method11

    @minilang_Method11.setter
    def minilang_Method11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Method__minilang_Method11", None)
        self.__minilang_Method11 = value
        
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
    def 8(self):
        return self.__8

    @8.setter
    def 8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Method__8", None)
        self.__8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if opp_val == self:
                    setattr(old_value, "9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                setattr(value, "9", self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_Program:

    def __init__(self, x: float, y: float, angle: str, distance: float, minilang_Program: "minilang_Method" = None, minilang_Program4: set["minilang_Variable"] = None, minilang_Program6: set["minilang_Line"] = None, 9: "minilang_Method" = None, : set["minilang_Method"] = None):
        self.x = x
        self.y = y
        self.angle = angle
        self.distance = distance
        self.minilang_Program = minilang_Program
        self.minilang_Program4 = minilang_Program4 if minilang_Program4 is not None else set()
        self.minilang_Program6 = minilang_Program6 if minilang_Program6 is not None else set()
        self.9 = 9
        self. =  if  is not None else set()
        
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def distance(self) -> float:
        return self.__distance

    @distance.setter
    def distance(self, distance: float):
        self.__distance = distance

    @property
    def angle(self) -> str:
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Program__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    if opp_val == self:
                        setattr(item, "1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    setattr(item, "1", self)
                    

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
    def minilang_Program6(self):
        return self.__minilang_Program6

    @minilang_Program6.setter
    def minilang_Program6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Program__minilang_Program6", None)
        self.__minilang_Program6 = value if value is not None else set()
        
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
                    

    @property
    def minilang_Program4(self):
        return self.__minilang_Program4

    @minilang_Program4.setter
    def minilang_Program4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Program__minilang_Program4", None)
        self.__minilang_Program4 = value if value is not None else set()
        
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
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Program__9", None)
        self.__9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "8"):
                opp_val = getattr(old_value, "8", None)
                if opp_val == self:
                    setattr(old_value, "8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "8"):
                opp_val = getattr(value, "8", None)
                setattr(value, "8", self)

    def mainK3(self):
        # TODO: Implement mainK3 method
        pass

class minilang_Block:

    def __init__(self, minilang_Block: "minilang_Method" = None, minilang_Block15: "minilang_IfStmt" = None, minilang_Block18: "minilang_IfStmt" = None, minilang_Block13: set["minilang_Statement"] = None):
        self.minilang_Block = minilang_Block
        self.minilang_Block15 = minilang_Block15
        self.minilang_Block18 = minilang_Block18
        self.minilang_Block13 = minilang_Block13 if minilang_Block13 is not None else set()
        
    @property
    def minilang_Block18(self):
        return self.__minilang_Block18

    @minilang_Block18.setter
    def minilang_Block18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Block__minilang_Block18", None)
        self.__minilang_Block18 = value
        
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

    @property
    def minilang_Block13(self):
        return self.__minilang_Block13

    @minilang_Block13.setter
    def minilang_Block13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Block__minilang_Block13", None)
        self.__minilang_Block13 = value if value is not None else set()
        
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
    def minilang_Block(self):
        return self.__minilang_Block

    @minilang_Block.setter
    def minilang_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Block__minilang_Block", None)
        self.__minilang_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minilang_Method11"):
                opp_val = getattr(old_value, "minilang_Method11", None)
                if opp_val == self:
                    setattr(old_value, "minilang_Method11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Method11"):
                opp_val = getattr(value, "minilang_Method11", None)
                setattr(value, "minilang_Method11", self)

    def executeK3(self):
        # TODO: Implement executeK3 method
        pass

class minilang_Line:

    def __init__(self, x1: float, y1: float, x2: float, y2: float, minilang_Line: "minilang_Program" = None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.minilang_Line = minilang_Line
        
    @property
    def y2(self) -> float:
        return self.__y2

    @y2.setter
    def y2(self, y2: float):
        self.__y2 = y2

    @property
    def x1(self) -> float:
        return self.__x1

    @x1.setter
    def x1(self, x1: float):
        self.__x1 = x1

    @property
    def y1(self) -> float:
        return self.__y1

    @y1.setter
    def y1(self, y1: float):
        self.__y1 = y1

    @property
    def x2(self) -> float:
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
            if hasattr(old_value, "minilang_Program6"):
                opp_val = getattr(old_value, "minilang_Program6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Program6"):
                opp_val = getattr(value, "minilang_Program6", None)
                if opp_val is None:
                    setattr(value, "minilang_Program6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class minilang_Variable:

    def __init__(self, name: str, value: float, minilang_Variable: "minilang_Program" = None, minilang_Variable26: "minilang_VariableRef" = None, minilang_Variable28: "minilang_VariableAffect" = None):
        self.name = name
        self.value = value
        self.minilang_Variable = minilang_Variable
        self.minilang_Variable26 = minilang_Variable26
        self.minilang_Variable28 = minilang_Variable28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

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
            if hasattr(old_value, "minilang_Program4"):
                opp_val = getattr(old_value, "minilang_Program4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minilang_Program4"):
                opp_val = getattr(value, "minilang_Program4", None)
                if opp_val is None:
                    setattr(value, "minilang_Program4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def minilang_Variable28(self):
        return self.__minilang_Variable28

    @minilang_Variable28.setter
    def minilang_Variable28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Variable__minilang_Variable28", None)
        self.__minilang_Variable28 = value
        
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
    def minilang_Variable26(self):
        return self.__minilang_Variable26

    @minilang_Variable26.setter
    def minilang_Variable26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minilang_Variable__minilang_Variable26", None)
        self.__minilang_Variable26 = value
        
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

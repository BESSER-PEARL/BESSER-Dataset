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

class Statement:

    pass
class minilang_RotateRight(Statement):

    pass
class minilang_RotateLeft(Statement):

    pass
class minilang_Move(Statement):

    pass
class minilang_CallMethod(Statement):

    pass
class minilang_IfStmt(Statement):

    pass
class minilang_Statement(ABC):

    pass
class minilang_Block:

    pass
class BinaryOperation:

    pass
class minilang_Modulo(BinaryOperation):

    pass
class minilang_Sum(BinaryOperation):

    pass
class minilang_VariableAffect(Statement):

    pass
class Value:

    pass
class minilang_VariableRef(Value):

    pass
class minilang_BinaryOperation(Value):

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

class minilang_Value(ABC):

    pass
class Condition:

    pass
class minilang_GreaterThan(Condition):

    pass
class minilang_Condition(ABC):

    pass
class minilang_Line:

    def __init__(self, y2: float, x1: float, y1: float, x2: float, minilang_Line: "minilang_Program" = None):
        self.y2 = y2
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.minilang_Line = minilang_Line
        
    @property
    def x1(self) -> float:
        return self.__x1

    @x1.setter
    def x1(self, x1: float):
        self.__x1 = x1

    @property
    def y2(self) -> float:
        return self.__y2

    @y2.setter
    def y2(self, y2: float):
        self.__y2 = y2

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

class minilang_Method:

    def __init__(self, name: str, 1: "minilang_Program" = None, minilang_Method: "minilang_Program" = None, 8: "minilang_Program" = None, minilang_Method11: "minilang_Block" = None, minilang_Method38: "minilang_CallMethod" = None):
        self.name = name
        self.1 = 1
        self.minilang_Method = minilang_Method
        self.8 = 8
        self.minilang_Method11 = minilang_Method11
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

class minilang_Program:

    def __init__(self, x: float, y: float, angle: str, distance: float, : set["minilang_Method"] = None, minilang_Program: "minilang_Method" = None, minilang_Program4: set["minilang_Variable"] = None, minilang_Program6: set["minilang_Line"] = None, 9: "minilang_Method" = None):
        self.x = x
        self.y = y
        self.angle = angle
        self.distance = distance
        self. =  if  is not None else set()
        self.minilang_Program = minilang_Program
        self.minilang_Program4 = minilang_Program4 if minilang_Program4 is not None else set()
        self.minilang_Program6 = minilang_Program6 if minilang_Program6 is not None else set()
        self.9 = 9
        
    @property
    def angle(self) -> str:
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def distance(self) -> float:
        return self.__distance

    @distance.setter
    def distance(self, distance: float):
        self.__distance = distance

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

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
class minilang_IfStmt(Statement):

    pass
class minilang_Statement(ABC):

    pass
class minilang_RotateLeft(Statement):

    pass
class minilang_RotateRight(Statement):

    pass
class minilang_Move(Statement):

    pass
class minilang_CallMethod(Statement):

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
        
        pass
    @property
    def value(self):
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
class minilang_Block:

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
    def y1(self):
        return self.__y1

    @y1.setter
    def y1(self, y1: float):
        self.__y1 = y1


    @property
    def x1(self):
        return self.__x1

    @x1.setter
    def x1(self, x1: float):
        self.__x1 = x1


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

class minilang_Method:

    def __init__(self, name: str, Method: "minilang_Program" = None, minilang_Method: "minilang_Program" = None, methods: "minilang_Program" = None, minilang_Method35: "minilang_CallMethod" = None, minilang_Method8: "minilang_Block" = None):
        self.name = name
        self.Method = Method
        self.minilang_Method = minilang_Method
        self.methods = methods
        self.minilang_Method35 = minilang_Method35
        self.minilang_Method8 = minilang_Method8
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

class minilang_Program:

    def __init__(self, x: float, y: float, angle: str, distance: float, program: set["minilang_Method"] = None, minilang_Program: "minilang_Method" = None, minilang_Program3: set["minilang_Variable"] = None, minilang_Program5: set["minilang_Line"] = None, Program: "minilang_Method" = None):
        self.x = x
        self.y = y
        self.angle = angle
        self.distance = distance
        self.program = program if program is not None else set()
        self.minilang_Program = minilang_Program
        self.minilang_Program3 = minilang_Program3 if minilang_Program3 is not None else set()
        self.minilang_Program5 = minilang_Program5 if minilang_Program5 is not None else set()
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

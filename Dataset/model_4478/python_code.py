from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class kmLogo_CallStack:

    pass
class kmLogo_Segment:

    pass
class kmLogo_Point:

    def __init__(self, x: float, y: float, kmLogo_Point48: "kmLogo_Segment" = None, kmLogo_Point51: "kmLogo_Segment" = None, kmLogo_Point: "kmLogo_Turtle" = None):
        self.x = x
        self.y = y
        self.kmLogo_Point48 = kmLogo_Point48
        self.kmLogo_Point51 = kmLogo_Point51
        self.kmLogo_Point = kmLogo_Point
        
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
    def kmLogo_Point51(self):
        return self.__kmLogo_Point51

    @kmLogo_Point51.setter
    def kmLogo_Point51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Point__kmLogo_Point51", None)
        self.__kmLogo_Point51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_Segment50"):
                opp_val = getattr(old_value, "kmLogo_Segment50", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_Segment50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_Segment50"):
                opp_val = getattr(value, "kmLogo_Segment50", None)
                setattr(value, "kmLogo_Segment50", self)

    @property
    def kmLogo_Point(self):
        return self.__kmLogo_Point

    @kmLogo_Point.setter
    def kmLogo_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Point__kmLogo_Point", None)
        self.__kmLogo_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_Turtle"):
                opp_val = getattr(old_value, "kmLogo_Turtle", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_Turtle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_Turtle"):
                opp_val = getattr(value, "kmLogo_Turtle", None)
                setattr(value, "kmLogo_Turtle", self)

    @property
    def kmLogo_Point48(self):
        return self.__kmLogo_Point48

    @kmLogo_Point48.setter
    def kmLogo_Point48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Point__kmLogo_Point48", None)
        self.__kmLogo_Point48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_Segment47"):
                opp_val = getattr(old_value, "kmLogo_Segment47", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_Segment47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_Segment47"):
                opp_val = getattr(value, "kmLogo_Segment47", None)
                setattr(value, "kmLogo_Segment47", self)

class kmLogo_Turtle:

    def __init__(self, heading: float, penUp: bool, kmLogo_Turtle: "kmLogo_Point" = None, kmLogo_Turtle43: set["kmLogo_Segment"] = None, kmLogo_Turtle45: "kmLogo_CallStack" = None):
        self.heading = heading
        self.penUp = penUp
        self.kmLogo_Turtle = kmLogo_Turtle
        self.kmLogo_Turtle43 = kmLogo_Turtle43 if kmLogo_Turtle43 is not None else set()
        self.kmLogo_Turtle45 = kmLogo_Turtle45
        
    @property
    def penUp(self) -> bool:
        return self.__penUp

    @penUp.setter
    def penUp(self, penUp: bool):
        self.__penUp = penUp

    @property
    def heading(self) -> float:
        return self.__heading

    @heading.setter
    def heading(self, heading: float):
        self.__heading = heading

    @property
    def kmLogo_Turtle43(self):
        return self.__kmLogo_Turtle43

    @kmLogo_Turtle43.setter
    def kmLogo_Turtle43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Turtle__kmLogo_Turtle43", None)
        self.__kmLogo_Turtle43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kmLogo_Segment"):
                    opp_val = getattr(item, "kmLogo_Segment", None)
                    
                    if opp_val == self:
                        setattr(item, "kmLogo_Segment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kmLogo_Segment"):
                    opp_val = getattr(item, "kmLogo_Segment", None)
                    
                    setattr(item, "kmLogo_Segment", self)
                    

    @property
    def kmLogo_Turtle(self):
        return self.__kmLogo_Turtle

    @kmLogo_Turtle.setter
    def kmLogo_Turtle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Turtle__kmLogo_Turtle", None)
        self.__kmLogo_Turtle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_Point"):
                opp_val = getattr(old_value, "kmLogo_Point", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_Point"):
                opp_val = getattr(value, "kmLogo_Point", None)
                setattr(value, "kmLogo_Point", self)

    @property
    def kmLogo_Turtle45(self):
        return self.__kmLogo_Turtle45

    @kmLogo_Turtle45.setter
    def kmLogo_Turtle45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Turtle__kmLogo_Turtle45", None)
        self.__kmLogo_Turtle45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_CallStack"):
                opp_val = getattr(old_value, "kmLogo_CallStack", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_CallStack", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_CallStack"):
                opp_val = getattr(value, "kmLogo_CallStack", None)
                setattr(value, "kmLogo_CallStack", self)

class kmLogo_LogoProgram:

    pass
class kmLogo_Variable:

    def __init__(self, name: str, value: float, kmLogo_Variable: "kmLogo_StackFrame" = None):
        self.name = name
        self.value = value
        self.kmLogo_Variable = kmLogo_Variable
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kmLogo_Variable(self):
        return self.__kmLogo_Variable

    @kmLogo_Variable.setter
    def kmLogo_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Variable__kmLogo_Variable", None)
        self.__kmLogo_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_StackFrame55"):
                opp_val = getattr(old_value, "kmLogo_StackFrame55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_StackFrame55"):
                opp_val = getattr(value, "kmLogo_StackFrame55", None)
                if opp_val is None:
                    setattr(value, "kmLogo_StackFrame55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kmLogo_StackFrame:

    pass
class ControlStructure:

    pass
class kmLogo_If(ControlStructure):

    pass
class UnaryExpression:

    pass
class kmLogo_Sin(UnaryExpression):

    pass
class kmLogo_Tan(UnaryExpression):

    pass
class kmLogo_Cos(UnaryExpression):

    pass
class BinaryExp:

    pass
class kmLogo_Greater(BinaryExp):

    pass
class kmLogo_Equals(BinaryExp):

    pass
class kmLogo_Minus(BinaryExp):

    pass
class kmLogo_Lower(BinaryExp):

    pass
class kmLogo_Div(BinaryExp):

    pass
class kmLogo_Mult(BinaryExp):

    pass
class kmLogo_Plus(BinaryExp):

    pass
class kmLogo_While(ControlStructure):

    pass
class kmLogo_Repeat(ControlStructure):

    pass
class Expression:

    pass
class kmLogo_ParameterCall(Expression):

    pass
class kmLogo_BinaryExp(Expression):

    pass
class kmLogo_Parameter:

    def __init__(self, name: str, kmLogo_Parameter38: "kmLogo_ParameterCall" = None, kmLogo_Parameter: "kmLogo_ProcDeclaration" = None):
        self.name = name
        self.kmLogo_Parameter38 = kmLogo_Parameter38
        self.kmLogo_Parameter = kmLogo_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kmLogo_Parameter38(self):
        return self.__kmLogo_Parameter38

    @kmLogo_Parameter38.setter
    def kmLogo_Parameter38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Parameter__kmLogo_Parameter38", None)
        self.__kmLogo_Parameter38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_ParameterCall"):
                opp_val = getattr(old_value, "kmLogo_ParameterCall", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_ParameterCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_ParameterCall"):
                opp_val = getattr(value, "kmLogo_ParameterCall", None)
                setattr(value, "kmLogo_ParameterCall", self)

    @property
    def kmLogo_Parameter(self):
        return self.__kmLogo_Parameter

    @kmLogo_Parameter.setter
    def kmLogo_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Parameter__kmLogo_Parameter", None)
        self.__kmLogo_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_ProcDeclaration"):
                opp_val = getattr(old_value, "kmLogo_ProcDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_ProcDeclaration"):
                opp_val = getattr(value, "kmLogo_ProcDeclaration", None)
                if opp_val is None:
                    setattr(value, "kmLogo_ProcDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kmLogo_ProcCall(Expression):

    pass
class kmLogo_Constant(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class kmLogo_UnaryExpression(Expression):

    pass
class Primitive:

    pass
class kmLogo_PenDown(Primitive):

    pass
class kmLogo_Right(Primitive):

    pass
class kmLogo_Clear(Primitive):

    pass
class kmLogo_Left(Primitive):

    pass
class kmLogo_PenUp(Primitive):

    pass
class kmLogo_Forward(Primitive):

    pass
class kmLogo_Back(Primitive):

    pass
class Instruction:

    pass
class kmLogo_ControlStructure(Instruction):

    pass
class kmLogo_ProcDeclaration(Instruction):

    def __init__(self, name: str, 17: "kmLogo_ProcCall" = None, kmLogo_ProcDeclaration: set["kmLogo_Parameter"] = None, 20: set["kmLogo_ProcCall"] = None, kmLogo_ProcDeclaration23: set["kmLogo_Instruction"] = None):
        self.name = name
        self.17 = 17
        self.kmLogo_ProcDeclaration = kmLogo_ProcDeclaration if kmLogo_ProcDeclaration is not None else set()
        self.20 = 20 if 20 is not None else set()
        self.kmLogo_ProcDeclaration23 = kmLogo_ProcDeclaration23 if kmLogo_ProcDeclaration23 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    @property
    def kmLogo_ProcDeclaration23(self):
        return self.__kmLogo_ProcDeclaration23

    @kmLogo_ProcDeclaration23.setter
    def kmLogo_ProcDeclaration23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__kmLogo_ProcDeclaration23", None)
        self.__kmLogo_ProcDeclaration23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kmLogo_Instruction"):
                    opp_val = getattr(item, "kmLogo_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "kmLogo_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kmLogo_Instruction"):
                    opp_val = getattr(item, "kmLogo_Instruction", None)
                    
                    setattr(item, "kmLogo_Instruction", self)
                    

    @property
    def kmLogo_ProcDeclaration(self):
        return self.__kmLogo_ProcDeclaration

    @kmLogo_ProcDeclaration.setter
    def kmLogo_ProcDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__kmLogo_ProcDeclaration", None)
        self.__kmLogo_ProcDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kmLogo_Parameter"):
                    opp_val = getattr(item, "kmLogo_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "kmLogo_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kmLogo_Parameter"):
                    opp_val = getattr(item, "kmLogo_Parameter", None)
                    
                    setattr(item, "kmLogo_Parameter", self)
                    

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__20", None)
        self.__20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "21"):
                    opp_val = getattr(item, "21", None)
                    
                    if opp_val == self:
                        setattr(item, "21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "21"):
                    opp_val = getattr(item, "21", None)
                    
                    setattr(item, "21", self)
                    

class kmLogo_Block(Instruction):

    pass
class kmLogo_Expression(Instruction):

    pass
class kmLogo_Primitive(Instruction):

    pass
class kmLogo_Instruction(ABC):

    pass
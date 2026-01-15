from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TYPE(Enum):
    ANALOG = "ANALOG"
    DIGITAL = "DIGITAL"
class IO(Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"


############################################
# Definition of Classes
############################################

class ardlers_Smoothing:

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class ardlers_ComponentBody:

    def __init__(self, io: str, type: str, pinned: str, pin: int, ardlers_ComponentBody45: "ardlers_Rate" = None, ardlers_ComponentBody47: "ardlers_Map" = None, ardlers_ComponentBody: "ardlers_Component" = None):
        self.io = io
        self.type = type
        self.pinned = pinned
        self.pin = pin
        self.ardlers_ComponentBody45 = ardlers_ComponentBody45
        self.ardlers_ComponentBody47 = ardlers_ComponentBody47
        self.ardlers_ComponentBody = ardlers_ComponentBody
        
    @property
    def pinned(self) -> str:
        return self.__pinned

    @pinned.setter
    def pinned(self, pinned: str):
        self.__pinned = pinned

    @property
    def pin(self) -> int:
        return self.__pin

    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

    @property
    def io(self) -> str:
        return self.__io

    @io.setter
    def io(self, io: str):
        self.__io = io

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ardlers_ComponentBody47(self):
        return self.__ardlers_ComponentBody47

    @ardlers_ComponentBody47.setter
    def ardlers_ComponentBody47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_ComponentBody__ardlers_ComponentBody47", None)
        self.__ardlers_ComponentBody47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Map"):
                opp_val = getattr(old_value, "ardlers_Map", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Map", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Map"):
                opp_val = getattr(value, "ardlers_Map", None)
                setattr(value, "ardlers_Map", self)

    @property
    def ardlers_ComponentBody45(self):
        return self.__ardlers_ComponentBody45

    @ardlers_ComponentBody45.setter
    def ardlers_ComponentBody45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_ComponentBody__ardlers_ComponentBody45", None)
        self.__ardlers_ComponentBody45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Rate"):
                opp_val = getattr(old_value, "ardlers_Rate", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Rate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Rate"):
                opp_val = getattr(value, "ardlers_Rate", None)
                setattr(value, "ardlers_Rate", self)

    @property
    def ardlers_ComponentBody(self):
        return self.__ardlers_ComponentBody

    @ardlers_ComponentBody.setter
    def ardlers_ComponentBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_ComponentBody__ardlers_ComponentBody", None)
        self.__ardlers_ComponentBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Component43"):
                opp_val = getattr(old_value, "ardlers_Component43", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Component43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Component43"):
                opp_val = getattr(value, "ardlers_Component43", None)
                setattr(value, "ardlers_Component43", self)

class ardlers_Assignment:

    pass
class ardlers_Range:

    def __init__(self, low: float, high: float, ardlers_Range: "ardlers_Map" = None, ardlers_Range52: "ardlers_Map" = None):
        self.low = low
        self.high = high
        self.ardlers_Range = ardlers_Range
        self.ardlers_Range52 = ardlers_Range52
        
    @property
    def high(self) -> float:
        return self.__high

    @high.setter
    def high(self, high: float):
        self.__high = high

    @property
    def low(self) -> float:
        return self.__low

    @low.setter
    def low(self, low: float):
        self.__low = low

    @property
    def ardlers_Range52(self):
        return self.__ardlers_Range52

    @ardlers_Range52.setter
    def ardlers_Range52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Range__ardlers_Range52", None)
        self.__ardlers_Range52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Map51"):
                opp_val = getattr(old_value, "ardlers_Map51", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Map51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Map51"):
                opp_val = getattr(value, "ardlers_Map51", None)
                setattr(value, "ardlers_Map51", self)

    @property
    def ardlers_Range(self):
        return self.__ardlers_Range

    @ardlers_Range.setter
    def ardlers_Range(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Range__ardlers_Range", None)
        self.__ardlers_Range = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Map49"):
                opp_val = getattr(old_value, "ardlers_Map49", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Map49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Map49"):
                opp_val = getattr(value, "ardlers_Map49", None)
                setattr(value, "ardlers_Map49", self)

class ardlers_Map:

    pass
class ardlers_Rate:

    def __init__(self, value: int, ardlers_Rate: "ardlers_ComponentBody" = None):
        self.value = value
        self.ardlers_Rate = ardlers_Rate
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def ardlers_Rate(self):
        return self.__ardlers_Rate

    @ardlers_Rate.setter
    def ardlers_Rate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Rate__ardlers_Rate", None)
        self.__ardlers_Rate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_ComponentBody45"):
                opp_val = getattr(old_value, "ardlers_ComponentBody45", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_ComponentBody45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_ComponentBody45"):
                opp_val = getattr(value, "ardlers_ComponentBody45", None)
                setattr(value, "ardlers_ComponentBody45", self)

class Or:

    pass
class ardlers_Expression(Or):

    pass
class ardlers_RuleBody:

    pass
class ardlers_Or:

    def __init__(self, operator: str, ardlers_Or19: "ardlers_Parenthesis" = None, ardlers_Or: "ardlers_Rule" = None, ardlers_Or15: "ardlers_Or" = None, ardlers_Or13: "ardlers_Or" = None, ardlers_Or17: "ardlers_Expression" = None):
        self.operator = operator
        self.ardlers_Or19 = ardlers_Or19
        self.ardlers_Or = ardlers_Or
        self.ardlers_Or15 = ardlers_Or15
        self.ardlers_Or13 = ardlers_Or13
        self.ardlers_Or17 = ardlers_Or17
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ardlers_Or(self):
        return self.__ardlers_Or

    @ardlers_Or.setter
    def ardlers_Or(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Or__ardlers_Or", None)
        self.__ardlers_Or = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Rule"):
                opp_val = getattr(old_value, "ardlers_Rule", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Rule"):
                opp_val = getattr(value, "ardlers_Rule", None)
                setattr(value, "ardlers_Rule", self)

    @property
    def ardlers_Or15(self):
        return self.__ardlers_Or15

    @ardlers_Or15.setter
    def ardlers_Or15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Or__ardlers_Or15", None)
        self.__ardlers_Or15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Or13"):
                opp_val = getattr(old_value, "ardlers_Or13", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Or13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Or13"):
                opp_val = getattr(value, "ardlers_Or13", None)
                setattr(value, "ardlers_Or13", self)

    @property
    def ardlers_Or17(self):
        return self.__ardlers_Or17

    @ardlers_Or17.setter
    def ardlers_Or17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Or__ardlers_Or17", None)
        self.__ardlers_Or17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Expression"):
                opp_val = getattr(old_value, "ardlers_Expression", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Expression"):
                opp_val = getattr(value, "ardlers_Expression", None)
                setattr(value, "ardlers_Expression", self)

    @property
    def ardlers_Or13(self):
        return self.__ardlers_Or13

    @ardlers_Or13.setter
    def ardlers_Or13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Or__ardlers_Or13", None)
        self.__ardlers_Or13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Or15"):
                opp_val = getattr(old_value, "ardlers_Or15", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Or15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Or15"):
                opp_val = getattr(value, "ardlers_Or15", None)
                setattr(value, "ardlers_Or15", self)

    @property
    def ardlers_Or19(self):
        return self.__ardlers_Or19

    @ardlers_Or19.setter
    def ardlers_Or19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Or__ardlers_Or19", None)
        self.__ardlers_Or19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Parenthesis"):
                opp_val = getattr(old_value, "ardlers_Parenthesis", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Parenthesis", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Parenthesis"):
                opp_val = getattr(value, "ardlers_Parenthesis", None)
                setattr(value, "ardlers_Parenthesis", self)

class ardlers_Rule:

    def __init__(self, type: str, ardlers_Rule: "ardlers_Or" = None, ardlers_Rule12: "ardlers_RuleBody" = None):
        self.type = type
        self.ardlers_Rule = ardlers_Rule
        self.ardlers_Rule12 = ardlers_Rule12
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ardlers_Rule12(self):
        return self.__ardlers_Rule12

    @ardlers_Rule12.setter
    def ardlers_Rule12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Rule__ardlers_Rule12", None)
        self.__ardlers_Rule12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_RuleBody"):
                opp_val = getattr(old_value, "ardlers_RuleBody", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_RuleBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_RuleBody"):
                opp_val = getattr(value, "ardlers_RuleBody", None)
                setattr(value, "ardlers_RuleBody", self)

    @property
    def ardlers_Rule(self):
        return self.__ardlers_Rule

    @ardlers_Rule.setter
    def ardlers_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Rule__ardlers_Rule", None)
        self.__ardlers_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Or"):
                opp_val = getattr(old_value, "ardlers_Or", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Or", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Or"):
                opp_val = getattr(value, "ardlers_Or", None)
                setattr(value, "ardlers_Or", self)

class ardlers_State:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ardlers_Component:

    def __init__(self, name: str, ardlers_Component: "ardlers_Attribute" = None, ardlers_Component38: "ardlers_Node" = None, ardlers_Component40: "ardlers_SensorImport" = None, ardlers_Component43: "ardlers_ComponentBody" = None):
        self.name = name
        self.ardlers_Component = ardlers_Component
        self.ardlers_Component38 = ardlers_Component38
        self.ardlers_Component40 = ardlers_Component40
        self.ardlers_Component43 = ardlers_Component43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ardlers_Component38(self):
        return self.__ardlers_Component38

    @ardlers_Component38.setter
    def ardlers_Component38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Component__ardlers_Component38", None)
        self.__ardlers_Component38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Node37"):
                opp_val = getattr(old_value, "ardlers_Node37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Node37"):
                opp_val = getattr(value, "ardlers_Node37", None)
                if opp_val is None:
                    setattr(value, "ardlers_Node37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ardlers_Component43(self):
        return self.__ardlers_Component43

    @ardlers_Component43.setter
    def ardlers_Component43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Component__ardlers_Component43", None)
        self.__ardlers_Component43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_ComponentBody"):
                opp_val = getattr(old_value, "ardlers_ComponentBody", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_ComponentBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_ComponentBody"):
                opp_val = getattr(value, "ardlers_ComponentBody", None)
                setattr(value, "ardlers_ComponentBody", self)

    @property
    def ardlers_Component40(self):
        return self.__ardlers_Component40

    @ardlers_Component40.setter
    def ardlers_Component40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Component__ardlers_Component40", None)
        self.__ardlers_Component40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_SensorImport41"):
                opp_val = getattr(old_value, "ardlers_SensorImport41", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_SensorImport41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_SensorImport41"):
                opp_val = getattr(value, "ardlers_SensorImport41", None)
                setattr(value, "ardlers_SensorImport41", self)

    @property
    def ardlers_Component(self):
        return self.__ardlers_Component

    @ardlers_Component.setter
    def ardlers_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Component__ardlers_Component", None)
        self.__ardlers_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Attribute22"):
                opp_val = getattr(old_value, "ardlers_Attribute22", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Attribute22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Attribute22"):
                opp_val = getattr(value, "ardlers_Attribute22", None)
                setattr(value, "ardlers_Attribute22", self)

class ardlers_Node:

    def __init__(self, name: str, ardlers_Node: "ardlers_Attribute" = None, ardlers_Node34: "ardlers_BoardDefinition" = None, ardlers_Node37: set["ardlers_Component"] = None):
        self.name = name
        self.ardlers_Node = ardlers_Node
        self.ardlers_Node34 = ardlers_Node34
        self.ardlers_Node37 = ardlers_Node37 if ardlers_Node37 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ardlers_Node37(self):
        return self.__ardlers_Node37

    @ardlers_Node37.setter
    def ardlers_Node37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Node__ardlers_Node37", None)
        self.__ardlers_Node37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ardlers_Component38"):
                    opp_val = getattr(item, "ardlers_Component38", None)
                    
                    if opp_val == self:
                        setattr(item, "ardlers_Component38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ardlers_Component38"):
                    opp_val = getattr(item, "ardlers_Component38", None)
                    
                    setattr(item, "ardlers_Component38", self)
                    

    @property
    def ardlers_Node34(self):
        return self.__ardlers_Node34

    @ardlers_Node34.setter
    def ardlers_Node34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Node__ardlers_Node34", None)
        self.__ardlers_Node34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_BoardDefinition35"):
                opp_val = getattr(old_value, "ardlers_BoardDefinition35", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_BoardDefinition35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_BoardDefinition35"):
                opp_val = getattr(value, "ardlers_BoardDefinition35", None)
                setattr(value, "ardlers_BoardDefinition35", self)

    @property
    def ardlers_Node(self):
        return self.__ardlers_Node

    @ardlers_Node.setter
    def ardlers_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_Node__ardlers_Node", None)
        self.__ardlers_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Attribute"):
                opp_val = getattr(old_value, "ardlers_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Attribute"):
                opp_val = getattr(value, "ardlers_Attribute", None)
                setattr(value, "ardlers_Attribute", self)

class Value:

    pass
class ardlers_NumberLiteral(Value):

    def __init__(self, float: str, int: int):
        self.float = float
        self.int = int
        
    @property
    def int(self) -> int:
        return self.__int

    @int.setter
    def int(self, int: int):
        self.__int = int

    @property
    def float(self) -> str:
        return self.__float

    @float.setter
    def float(self, float: str):
        self.__float = float

class ardlers_Delta(Value):

    pass
class ardlers_Attribute(Value):

    pass
class Parenthesis:

    pass
class ardlers_Value(Parenthesis):

    pass
class Expression:

    pass
class ardlers_Factor(Expression):

    pass
class ardlers_Exp(Expression):

    pass
class ardlers_Comparison(Expression):

    pass
class ardlers_And(Expression):

    pass
class ardlers_Parenthesis(Expression):

    pass
class ardlers_BoardDefinition:

    def __init__(self, name: str, di: int, do: int, ain: int, aout: int, ardlers_BoardDefinition: "ardlers_Program" = None, ardlers_BoardDefinition9: "ardlers_Library" = None, ardlers_BoardDefinition35: "ardlers_Node" = None):
        self.name = name
        self.di = di
        self.do = do
        self.ain = ain
        self.aout = aout
        self.ardlers_BoardDefinition = ardlers_BoardDefinition
        self.ardlers_BoardDefinition9 = ardlers_BoardDefinition9
        self.ardlers_BoardDefinition35 = ardlers_BoardDefinition35
        
    @property
    def aout(self) -> int:
        return self.__aout

    @aout.setter
    def aout(self, aout: int):
        self.__aout = aout

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ain(self) -> int:
        return self.__ain

    @ain.setter
    def ain(self, ain: int):
        self.__ain = ain

    @property
    def do(self) -> int:
        return self.__do

    @do.setter
    def do(self, do: int):
        self.__do = do

    @property
    def di(self) -> int:
        return self.__di

    @di.setter
    def di(self, di: int):
        self.__di = di

    @property
    def ardlers_BoardDefinition35(self):
        return self.__ardlers_BoardDefinition35

    @ardlers_BoardDefinition35.setter
    def ardlers_BoardDefinition35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_BoardDefinition__ardlers_BoardDefinition35", None)
        self.__ardlers_BoardDefinition35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Node34"):
                opp_val = getattr(old_value, "ardlers_Node34", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Node34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Node34"):
                opp_val = getattr(value, "ardlers_Node34", None)
                setattr(value, "ardlers_Node34", self)

    @property
    def ardlers_BoardDefinition9(self):
        return self.__ardlers_BoardDefinition9

    @ardlers_BoardDefinition9.setter
    def ardlers_BoardDefinition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_BoardDefinition__ardlers_BoardDefinition9", None)
        self.__ardlers_BoardDefinition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Library8"):
                opp_val = getattr(old_value, "ardlers_Library8", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Library8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Library8"):
                opp_val = getattr(value, "ardlers_Library8", None)
                setattr(value, "ardlers_Library8", self)

    @property
    def ardlers_BoardDefinition(self):
        return self.__ardlers_BoardDefinition

    @ardlers_BoardDefinition.setter
    def ardlers_BoardDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_BoardDefinition__ardlers_BoardDefinition", None)
        self.__ardlers_BoardDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Program6"):
                opp_val = getattr(old_value, "ardlers_Program6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Program6"):
                opp_val = getattr(value, "ardlers_Program6", None)
                if opp_val is None:
                    setattr(value, "ardlers_Program6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ardlers_EObject:

    pass
class ardlers_SensorImport:

    def __init__(self, name: str, ardlers_SensorImport: "ardlers_Program" = None, ardlers_SensorImport41: "ardlers_Component" = None):
        self.name = name
        self.ardlers_SensorImport = ardlers_SensorImport
        self.ardlers_SensorImport41 = ardlers_SensorImport41
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ardlers_SensorImport(self):
        return self.__ardlers_SensorImport

    @ardlers_SensorImport.setter
    def ardlers_SensorImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_SensorImport__ardlers_SensorImport", None)
        self.__ardlers_SensorImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Program2"):
                opp_val = getattr(old_value, "ardlers_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Program2"):
                opp_val = getattr(value, "ardlers_Program2", None)
                if opp_val is None:
                    setattr(value, "ardlers_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ardlers_SensorImport41(self):
        return self.__ardlers_SensorImport41

    @ardlers_SensorImport41.setter
    def ardlers_SensorImport41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ardlers_SensorImport__ardlers_SensorImport41", None)
        self.__ardlers_SensorImport41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ardlers_Component40"):
                opp_val = getattr(old_value, "ardlers_Component40", None)
                if opp_val == self:
                    setattr(old_value, "ardlers_Component40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ardlers_Component40"):
                opp_val = getattr(value, "ardlers_Component40", None)
                setattr(value, "ardlers_Component40", self)

class ardlers_Library:

    pass
class ardlers_Program:

    pass
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RelationalOperator(Enum):
    greater = "greater"
    equal = "equal"
    less = "less"
    greaterEqual = "greaterEqual"
    lessEqual = "lessEqual"
    and_ = "and_"
class ArithmeticOperator(Enum):
    plus = "plus"
    minus = "minus"
    mult = "mult"
    div = "div"


############################################
# Definition of Classes
############################################

class Literal:

    pass
class fmpl_Field(Literal):

    pass
class fmpl_StringLit(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class fmpl_IntegerLit(Literal):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class Expression:

    pass
class fmpl_Relational(Expression):

    def __init__(self, operator: str, fmpl_Relational: "fmpl_Cond" = None, fmpl_Relational26: "fmpl_Expression" = None, fmpl_Relational29: "fmpl_Expression" = None):
        self.operator = operator
        self.fmpl_Relational = fmpl_Relational
        self.fmpl_Relational26 = fmpl_Relational26
        self.fmpl_Relational29 = fmpl_Relational29
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def fmpl_Relational(self):
        return self.__fmpl_Relational

    @fmpl_Relational.setter
    def fmpl_Relational(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Relational__fmpl_Relational", None)
        self.__fmpl_Relational = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Cond"):
                opp_val = getattr(old_value, "fmpl_Cond", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Cond", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Cond"):
                opp_val = getattr(value, "fmpl_Cond", None)
                setattr(value, "fmpl_Cond", self)

    @property
    def fmpl_Relational29(self):
        return self.__fmpl_Relational29

    @fmpl_Relational29.setter
    def fmpl_Relational29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Relational__fmpl_Relational29", None)
        self.__fmpl_Relational29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Expression30"):
                opp_val = getattr(old_value, "fmpl_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Expression30"):
                opp_val = getattr(value, "fmpl_Expression30", None)
                setattr(value, "fmpl_Expression30", self)

    @property
    def fmpl_Relational26(self):
        return self.__fmpl_Relational26

    @fmpl_Relational26.setter
    def fmpl_Relational26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Relational__fmpl_Relational26", None)
        self.__fmpl_Relational26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Expression27"):
                opp_val = getattr(old_value, "fmpl_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Expression27"):
                opp_val = getattr(value, "fmpl_Expression27", None)
                setattr(value, "fmpl_Expression27", self)

class fmpl_Init(Expression):

    pass
class fmpl_VarReference(Expression):

    pass
class fmpl_ArithmeticExpression(Expression):

    def __init__(self, operator: str, fmpl_ArithmeticExpression: "fmpl_Expression" = None, fmpl_ArithmeticExpression34: "fmpl_Expression" = None):
        self.operator = operator
        self.fmpl_ArithmeticExpression = fmpl_ArithmeticExpression
        self.fmpl_ArithmeticExpression34 = fmpl_ArithmeticExpression34
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def fmpl_ArithmeticExpression34(self):
        return self.__fmpl_ArithmeticExpression34

    @fmpl_ArithmeticExpression34.setter
    def fmpl_ArithmeticExpression34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_ArithmeticExpression__fmpl_ArithmeticExpression34", None)
        self.__fmpl_ArithmeticExpression34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Expression35"):
                opp_val = getattr(old_value, "fmpl_Expression35", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Expression35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Expression35"):
                opp_val = getattr(value, "fmpl_Expression35", None)
                setattr(value, "fmpl_Expression35", self)

    @property
    def fmpl_ArithmeticExpression(self):
        return self.__fmpl_ArithmeticExpression

    @fmpl_ArithmeticExpression.setter
    def fmpl_ArithmeticExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_ArithmeticExpression__fmpl_ArithmeticExpression", None)
        self.__fmpl_ArithmeticExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Expression32"):
                opp_val = getattr(old_value, "fmpl_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Expression32"):
                opp_val = getattr(value, "fmpl_Expression32", None)
                setattr(value, "fmpl_Expression32", self)

class fmpl_Literal(Expression):

    pass
class fmpl_VarDeclaration(Expression):

    def __init__(self, name: str, fmpl_VarDeclaration: "fmpl_Expression" = None, fmpl_VarDeclaration40: "fmpl_VarReference" = None):
        self.name = name
        self.fmpl_VarDeclaration = fmpl_VarDeclaration
        self.fmpl_VarDeclaration40 = fmpl_VarDeclaration40
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def fmpl_VarDeclaration40(self):
        return self.__fmpl_VarDeclaration40

    @fmpl_VarDeclaration40.setter
    def fmpl_VarDeclaration40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_VarDeclaration__fmpl_VarDeclaration40", None)
        self.__fmpl_VarDeclaration40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_VarReference39"):
                opp_val = getattr(old_value, "fmpl_VarReference39", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_VarReference39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_VarReference39"):
                opp_val = getattr(value, "fmpl_VarReference39", None)
                setattr(value, "fmpl_VarReference39", self)

    @property
    def fmpl_VarDeclaration(self):
        return self.__fmpl_VarDeclaration

    @fmpl_VarDeclaration.setter
    def fmpl_VarDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_VarDeclaration__fmpl_VarDeclaration", None)
        self.__fmpl_VarDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Expression37"):
                opp_val = getattr(old_value, "fmpl_Expression37", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Expression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Expression37"):
                opp_val = getattr(value, "fmpl_Expression37", None)
                setattr(value, "fmpl_Expression37", self)

class fmpl_Read(Expression):

    def __init__(self, initBit: int, length: int):
        self.initBit = initBit
        self.length = length
        
        pass
    @property
    def initBit(self):
        return self.__initBit

    @initBit.setter
    def initBit(self, initBit: int):
        self.__initBit = initBit


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


class fmpl_Write(Expression):

    def __init__(self, initBit: int, length: int, fmpl_Write: "fmpl_VarReference" = None):
        self.initBit = initBit
        self.length = length
        self.fmpl_Write = fmpl_Write
        
        pass
    @property
    def initBit(self):
        return self.__initBit

    @initBit.setter
    def initBit(self, initBit: int):
        self.__initBit = initBit


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    @property
    def fmpl_Write(self):
        return self.__fmpl_Write

    @fmpl_Write.setter
    def fmpl_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Write__fmpl_Write", None)
        self.__fmpl_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_VarReference"):
                opp_val = getattr(old_value, "fmpl_VarReference", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_VarReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_VarReference"):
                opp_val = getattr(value, "fmpl_VarReference", None)
                setattr(value, "fmpl_VarReference", self)

class fmpl_Cond(Expression):

    pass
class fmpl_Exec(Expression):

    pass
class fmpl_Transition:

    def __init__(self, name: str, fmpl_Transition: "fmpl_Automata" = None, fmpl_Transition14: "fmpl_State" = None, fmpl_Transition17: "fmpl_Exec" = None, fmpl_Transition11: "fmpl_State" = None):
        self.name = name
        self.fmpl_Transition = fmpl_Transition
        self.fmpl_Transition14 = fmpl_Transition14
        self.fmpl_Transition17 = fmpl_Transition17
        self.fmpl_Transition11 = fmpl_Transition11
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def fmpl_Transition11(self):
        return self.__fmpl_Transition11

    @fmpl_Transition11.setter
    def fmpl_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Transition__fmpl_Transition11", None)
        self.__fmpl_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_State12"):
                opp_val = getattr(old_value, "fmpl_State12", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_State12"):
                opp_val = getattr(value, "fmpl_State12", None)
                setattr(value, "fmpl_State12", self)

    @property
    def fmpl_Transition(self):
        return self.__fmpl_Transition

    @fmpl_Transition.setter
    def fmpl_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Transition__fmpl_Transition", None)
        self.__fmpl_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Automata6"):
                opp_val = getattr(old_value, "fmpl_Automata6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Automata6"):
                opp_val = getattr(value, "fmpl_Automata6", None)
                if opp_val is None:
                    setattr(value, "fmpl_Automata6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fmpl_Transition14(self):
        return self.__fmpl_Transition14

    @fmpl_Transition14.setter
    def fmpl_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Transition__fmpl_Transition14", None)
        self.__fmpl_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_State15"):
                opp_val = getattr(old_value, "fmpl_State15", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_State15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_State15"):
                opp_val = getattr(value, "fmpl_State15", None)
                setattr(value, "fmpl_State15", self)

    @property
    def fmpl_Transition17(self):
        return self.__fmpl_Transition17

    @fmpl_Transition17.setter
    def fmpl_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Transition__fmpl_Transition17", None)
        self.__fmpl_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Exec"):
                opp_val = getattr(old_value, "fmpl_Exec", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Exec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Exec"):
                opp_val = getattr(value, "fmpl_Exec", None)
                setattr(value, "fmpl_Exec", self)

class fmpl_State:

    def __init__(self, name: str, fmpl_State: "fmpl_Automata" = None, fmpl_State9: "fmpl_Automata" = None, fmpl_State15: "fmpl_Transition" = None, fmpl_State12: "fmpl_Transition" = None):
        self.name = name
        self.fmpl_State = fmpl_State
        self.fmpl_State9 = fmpl_State9
        self.fmpl_State15 = fmpl_State15
        self.fmpl_State12 = fmpl_State12
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def fmpl_State(self):
        return self.__fmpl_State

    @fmpl_State.setter
    def fmpl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_State__fmpl_State", None)
        self.__fmpl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Automata4"):
                opp_val = getattr(old_value, "fmpl_Automata4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Automata4"):
                opp_val = getattr(value, "fmpl_Automata4", None)
                if opp_val is None:
                    setattr(value, "fmpl_Automata4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fmpl_State12(self):
        return self.__fmpl_State12

    @fmpl_State12.setter
    def fmpl_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_State__fmpl_State12", None)
        self.__fmpl_State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Transition11"):
                opp_val = getattr(old_value, "fmpl_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Transition11"):
                opp_val = getattr(value, "fmpl_Transition11", None)
                setattr(value, "fmpl_Transition11", self)

    @property
    def fmpl_State9(self):
        return self.__fmpl_State9

    @fmpl_State9.setter
    def fmpl_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_State__fmpl_State9", None)
        self.__fmpl_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Automata8"):
                opp_val = getattr(old_value, "fmpl_Automata8", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Automata8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Automata8"):
                opp_val = getattr(value, "fmpl_Automata8", None)
                setattr(value, "fmpl_Automata8", self)

    @property
    def fmpl_State15(self):
        return self.__fmpl_State15

    @fmpl_State15.setter
    def fmpl_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_State__fmpl_State15", None)
        self.__fmpl_State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Transition14"):
                opp_val = getattr(old_value, "fmpl_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Transition14"):
                opp_val = getattr(value, "fmpl_Transition14", None)
                setattr(value, "fmpl_Transition14", self)

class fmpl_Expression(ABC):

    pass
class fmpl_Automata:

    def __init__(self, name: str, fmpl_Automata4: set["fmpl_State"] = None, fmpl_Automata6: set["fmpl_Transition"] = None, fmpl_Automata8: "fmpl_State" = None, fmpl_Automata: "fmpl_Policy" = None, fmpl_Automata24: "fmpl_Init" = None):
        self.name = name
        self.fmpl_Automata4 = fmpl_Automata4 if fmpl_Automata4 is not None else set()
        self.fmpl_Automata6 = fmpl_Automata6 if fmpl_Automata6 is not None else set()
        self.fmpl_Automata8 = fmpl_Automata8
        self.fmpl_Automata = fmpl_Automata
        self.fmpl_Automata24 = fmpl_Automata24
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def fmpl_Automata24(self):
        return self.__fmpl_Automata24

    @fmpl_Automata24.setter
    def fmpl_Automata24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Automata__fmpl_Automata24", None)
        self.__fmpl_Automata24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Init"):
                opp_val = getattr(old_value, "fmpl_Init", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_Init", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Init"):
                opp_val = getattr(value, "fmpl_Init", None)
                setattr(value, "fmpl_Init", self)

    @property
    def fmpl_Automata6(self):
        return self.__fmpl_Automata6

    @fmpl_Automata6.setter
    def fmpl_Automata6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Automata__fmpl_Automata6", None)
        self.__fmpl_Automata6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fmpl_Transition"):
                    opp_val = getattr(item, "fmpl_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fmpl_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fmpl_Transition"):
                    opp_val = getattr(item, "fmpl_Transition", None)
                    
                    setattr(item, "fmpl_Transition", self)
                    

    @property
    def fmpl_Automata(self):
        return self.__fmpl_Automata

    @fmpl_Automata.setter
    def fmpl_Automata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Automata__fmpl_Automata", None)
        self.__fmpl_Automata = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_Policy"):
                opp_val = getattr(old_value, "fmpl_Policy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_Policy"):
                opp_val = getattr(value, "fmpl_Policy", None)
                if opp_val is None:
                    setattr(value, "fmpl_Policy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fmpl_Automata8(self):
        return self.__fmpl_Automata8

    @fmpl_Automata8.setter
    def fmpl_Automata8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Automata__fmpl_Automata8", None)
        self.__fmpl_Automata8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmpl_State9"):
                opp_val = getattr(old_value, "fmpl_State9", None)
                if opp_val == self:
                    setattr(old_value, "fmpl_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmpl_State9"):
                opp_val = getattr(value, "fmpl_State9", None)
                setattr(value, "fmpl_State9", self)

    @property
    def fmpl_Automata4(self):
        return self.__fmpl_Automata4

    @fmpl_Automata4.setter
    def fmpl_Automata4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Automata__fmpl_Automata4", None)
        self.__fmpl_Automata4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fmpl_State"):
                    opp_val = getattr(item, "fmpl_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fmpl_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fmpl_State"):
                    opp_val = getattr(item, "fmpl_State", None)
                    
                    setattr(item, "fmpl_State", self)
                    

class fmpl_Policy:

    def __init__(self, name: str, parserURI: str, fmpl_Policy2: set["fmpl_Expression"] = None, fmpl_Policy: set["fmpl_Automata"] = None):
        self.name = name
        self.parserURI = parserURI
        self.fmpl_Policy2 = fmpl_Policy2 if fmpl_Policy2 is not None else set()
        self.fmpl_Policy = fmpl_Policy if fmpl_Policy is not None else set()
        
        pass
    @property
    def parserURI(self):
        return self.__parserURI

    @parserURI.setter
    def parserURI(self, parserURI: str):
        self.__parserURI = parserURI


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def fmpl_Policy(self):
        return self.__fmpl_Policy

    @fmpl_Policy.setter
    def fmpl_Policy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Policy__fmpl_Policy", None)
        self.__fmpl_Policy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fmpl_Automata"):
                    opp_val = getattr(item, "fmpl_Automata", None)
                    
                    if opp_val == self:
                        setattr(item, "fmpl_Automata", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fmpl_Automata"):
                    opp_val = getattr(item, "fmpl_Automata", None)
                    
                    setattr(item, "fmpl_Automata", self)
                    

    @property
    def fmpl_Policy2(self):
        return self.__fmpl_Policy2

    @fmpl_Policy2.setter
    def fmpl_Policy2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmpl_Policy__fmpl_Policy2", None)
        self.__fmpl_Policy2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fmpl_Expression"):
                    opp_val = getattr(item, "fmpl_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "fmpl_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fmpl_Expression"):
                    opp_val = getattr(item, "fmpl_Expression", None)
                    
                    setattr(item, "fmpl_Expression", self)
                    

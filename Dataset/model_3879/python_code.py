from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EBoolTwoOp(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"
class EIntTwoOp(Enum):
    SUB = "SUB"
    ADD = "ADD"
    MUL = "MUL"
    DIV = "DIV"
class EIntOneOp(Enum):
    MIN = "MIN"
class EBoolVal(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
class ECompOp(Enum):
    EQ = "EQ"
    LE = "LE"
    GT = "GT"
    NE = "NE"
    GE = "GE"
    LT = "LT"
class EBoolOneOp(Enum):
    NOT = "NOT"


############################################
# Definition of Classes
############################################

class BoolExpr:

    pass
class flinkie2_Comparison(BoolExpr):

    def __init__(self, operator: str, flinkie2_Comparison: "flinkie2_IntExpr" = None, flinkie2_Comparison62: "flinkie2_IntExpr" = None):
        self.operator = operator
        self.flinkie2_Comparison = flinkie2_Comparison
        self.flinkie2_Comparison62 = flinkie2_Comparison62
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def flinkie2_Comparison62(self):
        return self.__flinkie2_Comparison62

    @flinkie2_Comparison62.setter
    def flinkie2_Comparison62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Comparison__flinkie2_Comparison62", None)
        self.__flinkie2_Comparison62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_IntExpr63"):
                opp_val = getattr(old_value, "flinkie2_IntExpr63", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_IntExpr63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_IntExpr63"):
                opp_val = getattr(value, "flinkie2_IntExpr63", None)
                setattr(value, "flinkie2_IntExpr63", self)

    @property
    def flinkie2_Comparison(self):
        return self.__flinkie2_Comparison

    @flinkie2_Comparison.setter
    def flinkie2_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Comparison__flinkie2_Comparison", None)
        self.__flinkie2_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_IntExpr60"):
                opp_val = getattr(old_value, "flinkie2_IntExpr60", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_IntExpr60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_IntExpr60"):
                opp_val = getattr(value, "flinkie2_IntExpr60", None)
                setattr(value, "flinkie2_IntExpr60", self)

class flinkie2_TwoOpBool(BoolExpr):

    def __init__(self, operator: str, flinkie2_TwoOpBool: "flinkie2_BoolExpr" = None, flinkie2_TwoOpBool55: "flinkie2_BoolExpr" = None):
        self.operator = operator
        self.flinkie2_TwoOpBool = flinkie2_TwoOpBool
        self.flinkie2_TwoOpBool55 = flinkie2_TwoOpBool55
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def flinkie2_TwoOpBool55(self):
        return self.__flinkie2_TwoOpBool55

    @flinkie2_TwoOpBool55.setter
    def flinkie2_TwoOpBool55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_TwoOpBool__flinkie2_TwoOpBool55", None)
        self.__flinkie2_TwoOpBool55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_BoolExpr56"):
                opp_val = getattr(old_value, "flinkie2_BoolExpr56", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_BoolExpr56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_BoolExpr56"):
                opp_val = getattr(value, "flinkie2_BoolExpr56", None)
                setattr(value, "flinkie2_BoolExpr56", self)

    @property
    def flinkie2_TwoOpBool(self):
        return self.__flinkie2_TwoOpBool

    @flinkie2_TwoOpBool.setter
    def flinkie2_TwoOpBool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_TwoOpBool__flinkie2_TwoOpBool", None)
        self.__flinkie2_TwoOpBool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_BoolExpr53"):
                opp_val = getattr(old_value, "flinkie2_BoolExpr53", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_BoolExpr53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_BoolExpr53"):
                opp_val = getattr(value, "flinkie2_BoolExpr53", None)
                setattr(value, "flinkie2_BoolExpr53", self)

class flinkie2_BoolVal(BoolExpr):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class flinkie2_BracExprBool(BoolExpr):

    pass
class flinkie2_OneOpBool(BoolExpr):

    def __init__(self, operator: str, flinkie2_OneOpBool: "flinkie2_BoolExpr" = None):
        self.operator = operator
        self.flinkie2_OneOpBool = flinkie2_OneOpBool
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def flinkie2_OneOpBool(self):
        return self.__flinkie2_OneOpBool

    @flinkie2_OneOpBool.setter
    def flinkie2_OneOpBool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_OneOpBool__flinkie2_OneOpBool", None)
        self.__flinkie2_OneOpBool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_BoolExpr51"):
                opp_val = getattr(old_value, "flinkie2_BoolExpr51", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_BoolExpr51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_BoolExpr51"):
                opp_val = getattr(value, "flinkie2_BoolExpr51", None)
                setattr(value, "flinkie2_BoolExpr51", self)

class flinkie2_FlowChart:

    pass
class IntExpr:

    pass
class flinkie2_VariableExpr(IntExpr):

    pass
class flinkie2_BracExprInt(IntExpr):

    pass
class flinkie2_Number(IntExpr):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class flinkie2_OneOpInt(IntExpr):

    def __init__(self, operator: str, flinkie2_OneOpInt: "flinkie2_IntExpr" = None):
        self.operator = operator
        self.flinkie2_OneOpInt = flinkie2_OneOpInt
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def flinkie2_OneOpInt(self):
        return self.__flinkie2_OneOpInt

    @flinkie2_OneOpInt.setter
    def flinkie2_OneOpInt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_OneOpInt__flinkie2_OneOpInt", None)
        self.__flinkie2_OneOpInt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_IntExpr"):
                opp_val = getattr(old_value, "flinkie2_IntExpr", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_IntExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_IntExpr"):
                opp_val = getattr(value, "flinkie2_IntExpr", None)
                setattr(value, "flinkie2_IntExpr", self)

class flinkie2_IntExpr(ABC):

    pass
class flinkie2_Option:

    def __init__(self, text: str, flinkie2_Option: "flinkie2_Question" = None, flinkie2_Option24: set["flinkie2_AssignStat"] = None, flinkie2_Option27: "flinkie2_Node" = None):
        self.text = text
        self.flinkie2_Option = flinkie2_Option
        self.flinkie2_Option24 = flinkie2_Option24 if flinkie2_Option24 is not None else set()
        self.flinkie2_Option27 = flinkie2_Option27
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def flinkie2_Option24(self):
        return self.__flinkie2_Option24

    @flinkie2_Option24.setter
    def flinkie2_Option24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Option__flinkie2_Option24", None)
        self.__flinkie2_Option24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flinkie2_AssignStat25"):
                    opp_val = getattr(item, "flinkie2_AssignStat25", None)
                    
                    if opp_val == self:
                        setattr(item, "flinkie2_AssignStat25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flinkie2_AssignStat25"):
                    opp_val = getattr(item, "flinkie2_AssignStat25", None)
                    
                    setattr(item, "flinkie2_AssignStat25", self)
                    

    @property
    def flinkie2_Option(self):
        return self.__flinkie2_Option

    @flinkie2_Option.setter
    def flinkie2_Option(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Option__flinkie2_Option", None)
        self.__flinkie2_Option = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_Question"):
                opp_val = getattr(old_value, "flinkie2_Question", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_Question"):
                opp_val = getattr(value, "flinkie2_Question", None)
                if opp_val is None:
                    setattr(value, "flinkie2_Question", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flinkie2_Option27(self):
        return self.__flinkie2_Option27

    @flinkie2_Option27.setter
    def flinkie2_Option27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Option__flinkie2_Option27", None)
        self.__flinkie2_Option27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_Node28"):
                opp_val = getattr(old_value, "flinkie2_Node28", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_Node28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_Node28"):
                opp_val = getattr(value, "flinkie2_Node28", None)
                setattr(value, "flinkie2_Node28", self)

class flinkie2_BoolExpr(ABC):

    pass
class flinkie2_TwoOpInt(IntExpr):

    def __init__(self, operator: str, flinkie2_TwoOpInt: "flinkie2_IntExpr" = None, flinkie2_TwoOpInt33: "flinkie2_IntExpr" = None):
        self.operator = operator
        self.flinkie2_TwoOpInt = flinkie2_TwoOpInt
        self.flinkie2_TwoOpInt33 = flinkie2_TwoOpInt33
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def flinkie2_TwoOpInt33(self):
        return self.__flinkie2_TwoOpInt33

    @flinkie2_TwoOpInt33.setter
    def flinkie2_TwoOpInt33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_TwoOpInt__flinkie2_TwoOpInt33", None)
        self.__flinkie2_TwoOpInt33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_IntExpr34"):
                opp_val = getattr(old_value, "flinkie2_IntExpr34", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_IntExpr34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_IntExpr34"):
                opp_val = getattr(value, "flinkie2_IntExpr34", None)
                setattr(value, "flinkie2_IntExpr34", self)

    @property
    def flinkie2_TwoOpInt(self):
        return self.__flinkie2_TwoOpInt

    @flinkie2_TwoOpInt.setter
    def flinkie2_TwoOpInt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_TwoOpInt__flinkie2_TwoOpInt", None)
        self.__flinkie2_TwoOpInt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_IntExpr31"):
                opp_val = getattr(old_value, "flinkie2_IntExpr31", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_IntExpr31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_IntExpr31"):
                opp_val = getattr(value, "flinkie2_IntExpr31", None)
                setattr(value, "flinkie2_IntExpr31", self)

class flinkie2_DeclStat:

    pass
class flinkie2_Init:

    pass
class flinkie2_Node(ABC):

    pass
class flinkie2_AssignStat:

    pass
class Node:

    pass
class flinkie2_Message(Node):

    def __init__(self, text: str, flinkie2_Message: set["flinkie2_AssignStat"] = None, flinkie2_Message21: "flinkie2_Node" = None):
        self.text = text
        self.flinkie2_Message = flinkie2_Message if flinkie2_Message is not None else set()
        self.flinkie2_Message21 = flinkie2_Message21
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def flinkie2_Message21(self):
        return self.__flinkie2_Message21

    @flinkie2_Message21.setter
    def flinkie2_Message21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Message__flinkie2_Message21", None)
        self.__flinkie2_Message21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_Node22"):
                opp_val = getattr(old_value, "flinkie2_Node22", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_Node22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_Node22"):
                opp_val = getattr(value, "flinkie2_Node22", None)
                setattr(value, "flinkie2_Node22", self)

    @property
    def flinkie2_Message(self):
        return self.__flinkie2_Message

    @flinkie2_Message.setter
    def flinkie2_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Message__flinkie2_Message", None)
        self.__flinkie2_Message = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flinkie2_AssignStat19"):
                    opp_val = getattr(item, "flinkie2_AssignStat19", None)
                    
                    if opp_val == self:
                        setattr(item, "flinkie2_AssignStat19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flinkie2_AssignStat19"):
                    opp_val = getattr(item, "flinkie2_AssignStat19", None)
                    
                    setattr(item, "flinkie2_AssignStat19", self)
                    

class flinkie2_Question(Node):

    def __init__(self, text: str, flinkie2_Question: set["flinkie2_Option"] = None, flinkie2_Question16: set["flinkie2_AssignStat"] = None):
        self.text = text
        self.flinkie2_Question = flinkie2_Question if flinkie2_Question is not None else set()
        self.flinkie2_Question16 = flinkie2_Question16 if flinkie2_Question16 is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def flinkie2_Question(self):
        return self.__flinkie2_Question

    @flinkie2_Question.setter
    def flinkie2_Question(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Question__flinkie2_Question", None)
        self.__flinkie2_Question = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flinkie2_Option"):
                    opp_val = getattr(item, "flinkie2_Option", None)
                    
                    if opp_val == self:
                        setattr(item, "flinkie2_Option", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flinkie2_Option"):
                    opp_val = getattr(item, "flinkie2_Option", None)
                    
                    setattr(item, "flinkie2_Option", self)
                    

    @property
    def flinkie2_Question16(self):
        return self.__flinkie2_Question16

    @flinkie2_Question16.setter
    def flinkie2_Question16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Question__flinkie2_Question16", None)
        self.__flinkie2_Question16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flinkie2_AssignStat17"):
                    opp_val = getattr(item, "flinkie2_AssignStat17", None)
                    
                    if opp_val == self:
                        setattr(item, "flinkie2_AssignStat17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flinkie2_AssignStat17"):
                    opp_val = getattr(item, "flinkie2_AssignStat17", None)
                    
                    setattr(item, "flinkie2_AssignStat17", self)
                    

class flinkie2_BooleanEvaluation(Node):

    pass
class flinkie2_Variable:

    def __init__(self, name: str, flinkie2_Variable: "flinkie2_DeclStat" = None, flinkie2_Variable49: "flinkie2_VariableExpr" = None):
        self.name = name
        self.flinkie2_Variable = flinkie2_Variable
        self.flinkie2_Variable49 = flinkie2_Variable49
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def flinkie2_Variable49(self):
        return self.__flinkie2_Variable49

    @flinkie2_Variable49.setter
    def flinkie2_Variable49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Variable__flinkie2_Variable49", None)
        self.__flinkie2_Variable49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_VariableExpr48"):
                opp_val = getattr(old_value, "flinkie2_VariableExpr48", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_VariableExpr48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_VariableExpr48"):
                opp_val = getattr(value, "flinkie2_VariableExpr48", None)
                setattr(value, "flinkie2_VariableExpr48", self)

    @property
    def flinkie2_Variable(self):
        return self.__flinkie2_Variable

    @flinkie2_Variable.setter
    def flinkie2_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flinkie2_Variable__flinkie2_Variable", None)
        self.__flinkie2_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flinkie2_DeclStat4"):
                opp_val = getattr(old_value, "flinkie2_DeclStat4", None)
                if opp_val == self:
                    setattr(old_value, "flinkie2_DeclStat4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flinkie2_DeclStat4"):
                opp_val = getattr(value, "flinkie2_DeclStat4", None)
                setattr(value, "flinkie2_DeclStat4", self)

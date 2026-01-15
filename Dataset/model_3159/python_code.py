from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BaseTypeEnum(Enum):
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
class Severity(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"


############################################
# Definition of Classes
############################################

class Instruction:

    pass
class altarica_Block(Instruction):

    pass
class altarica_Assignment(Instruction):

    pass
class altarica_Conditional(Instruction):

    pass
class altarica_Skip(Instruction):

    pass
class TransitionExpression:

    pass
class altarica_Transition(TransitionExpression):

    pass
class altarica_TransitionOr(TransitionExpression):

    pass
class altarica_TransitionAnd(TransitionExpression):

    pass
class NamedElement:

    pass
class altarica_Attribute(NamedElement):

    pass
class altarica_Parameter(NamedElement):

    pass
class altarica_Event(NamedElement):

    pass
class altarica_SymbolicConstant(NamedElement):

    pass
class altarica_Observer(NamedElement):

    pass
class altarica_Domain(NamedElement):

    pass
class altarica_Variable(NamedElement):

    pass
class altarica_Node(NamedElement):

    pass
class Expression:

    pass
class altarica_Equal(Expression):

    def __init__(self, op: str, altarica_Equal: "altarica_Expression" = None, altarica_Equal93: "altarica_Expression" = None):
        self.op = op
        self.altarica_Equal = altarica_Equal
        self.altarica_Equal93 = altarica_Equal93
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def altarica_Equal93(self):
        return self.__altarica_Equal93

    @altarica_Equal93.setter
    def altarica_Equal93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Equal__altarica_Equal93", None)
        self.__altarica_Equal93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Expression94"):
                opp_val = getattr(old_value, "altarica_Expression94", None)
                if opp_val == self:
                    setattr(old_value, "altarica_Expression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Expression94"):
                opp_val = getattr(value, "altarica_Expression94", None)
                setattr(value, "altarica_Expression94", self)

    @property
    def altarica_Equal(self):
        return self.__altarica_Equal

    @altarica_Equal.setter
    def altarica_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Equal__altarica_Equal", None)
        self.__altarica_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Expression91"):
                opp_val = getattr(old_value, "altarica_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "altarica_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Expression91"):
                opp_val = getattr(value, "altarica_Expression91", None)
                setattr(value, "altarica_Expression91", self)

class altarica_LogicalAnd(Expression):

    def __init__(self, op: str, altarica_LogicalAnd: "altarica_Expression" = None, altarica_LogicalAnd88: "altarica_Expression" = None):
        self.op = op
        self.altarica_LogicalAnd = altarica_LogicalAnd
        self.altarica_LogicalAnd88 = altarica_LogicalAnd88
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def altarica_LogicalAnd(self):
        return self.__altarica_LogicalAnd

    @altarica_LogicalAnd.setter
    def altarica_LogicalAnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_LogicalAnd__altarica_LogicalAnd", None)
        self.__altarica_LogicalAnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Expression86"):
                opp_val = getattr(old_value, "altarica_Expression86", None)
                if opp_val == self:
                    setattr(old_value, "altarica_Expression86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Expression86"):
                opp_val = getattr(value, "altarica_Expression86", None)
                setattr(value, "altarica_Expression86", self)

    @property
    def altarica_LogicalAnd88(self):
        return self.__altarica_LogicalAnd88

    @altarica_LogicalAnd88.setter
    def altarica_LogicalAnd88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_LogicalAnd__altarica_LogicalAnd88", None)
        self.__altarica_LogicalAnd88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Expression89"):
                opp_val = getattr(old_value, "altarica_Expression89", None)
                if opp_val == self:
                    setattr(old_value, "altarica_Expression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Expression89"):
                opp_val = getattr(value, "altarica_Expression89", None)
                setattr(value, "altarica_Expression89", self)

class altarica_ARNumber(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class altarica_LogicalOr(Expression):

    def __init__(self, op: str, altarica_LogicalOr: "altarica_Expression" = None, altarica_LogicalOr83: "altarica_Expression" = None):
        self.op = op
        self.altarica_LogicalOr = altarica_LogicalOr
        self.altarica_LogicalOr83 = altarica_LogicalOr83
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def altarica_LogicalOr83(self):
        return self.__altarica_LogicalOr83

    @altarica_LogicalOr83.setter
    def altarica_LogicalOr83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_LogicalOr__altarica_LogicalOr83", None)
        self.__altarica_LogicalOr83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Expression84"):
                opp_val = getattr(old_value, "altarica_Expression84", None)
                if opp_val == self:
                    setattr(old_value, "altarica_Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Expression84"):
                opp_val = getattr(value, "altarica_Expression84", None)
                setattr(value, "altarica_Expression84", self)

    @property
    def altarica_LogicalOr(self):
        return self.__altarica_LogicalOr

    @altarica_LogicalOr.setter
    def altarica_LogicalOr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_LogicalOr__altarica_LogicalOr", None)
        self.__altarica_LogicalOr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Expression81"):
                opp_val = getattr(old_value, "altarica_Expression81", None)
                if opp_val == self:
                    setattr(old_value, "altarica_Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Expression81"):
                opp_val = getattr(value, "altarica_Expression81", None)
                setattr(value, "altarica_Expression81", self)

class altarica_Multiplication(Expression):

    def __init__(self, op: str, altarica_Multiplication103: "altarica_Expression" = None, altarica_Multiplication: "altarica_Expression" = None):
        self.op = op
        self.altarica_Multiplication103 = altarica_Multiplication103
        self.altarica_Multiplication = altarica_Multiplication
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def altarica_Multiplication(self):
        return self.__altarica_Multiplication

    @altarica_Multiplication.setter
    def altarica_Multiplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Multiplication__altarica_Multiplication", None)
        self.__altarica_Multiplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Expression101"):
                opp_val = getattr(old_value, "altarica_Expression101", None)
                if opp_val == self:
                    setattr(old_value, "altarica_Expression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Expression101"):
                opp_val = getattr(value, "altarica_Expression101", None)
                setattr(value, "altarica_Expression101", self)

    @property
    def altarica_Multiplication103(self):
        return self.__altarica_Multiplication103

    @altarica_Multiplication103.setter
    def altarica_Multiplication103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Multiplication__altarica_Multiplication103", None)
        self.__altarica_Multiplication103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Expression104"):
                opp_val = getattr(old_value, "altarica_Expression104", None)
                if opp_val == self:
                    setattr(old_value, "altarica_Expression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Expression104"):
                opp_val = getattr(value, "altarica_Expression104", None)
                setattr(value, "altarica_Expression104", self)

class altarica_FunctionCall(Expression):

    def __init__(self, name: str, altarica_FunctionCall: set["altarica_Expression"] = None):
        self.name = name
        self.altarica_FunctionCall = altarica_FunctionCall if altarica_FunctionCall is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def altarica_FunctionCall(self):
        return self.__altarica_FunctionCall

    @altarica_FunctionCall.setter
    def altarica_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_FunctionCall__altarica_FunctionCall", None)
        self.__altarica_FunctionCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "altarica_Expression110"):
                    opp_val = getattr(item, "altarica_Expression110", None)
                    
                    if opp_val == self:
                        setattr(item, "altarica_Expression110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "altarica_Expression110"):
                    opp_val = getattr(item, "altarica_Expression110", None)
                    
                    setattr(item, "altarica_Expression110", self)
                    

class altarica_Minus(Expression):

    pass
class altarica_Addition(Expression):

    def __init__(self, op: str, altarica_Addition: "altarica_Expression" = None, altarica_Addition98: "altarica_Expression" = None):
        self.op = op
        self.altarica_Addition = altarica_Addition
        self.altarica_Addition98 = altarica_Addition98
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def altarica_Addition98(self):
        return self.__altarica_Addition98

    @altarica_Addition98.setter
    def altarica_Addition98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Addition__altarica_Addition98", None)
        self.__altarica_Addition98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Expression99"):
                opp_val = getattr(old_value, "altarica_Expression99", None)
                if opp_val == self:
                    setattr(old_value, "altarica_Expression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Expression99"):
                opp_val = getattr(value, "altarica_Expression99", None)
                setattr(value, "altarica_Expression99", self)

    @property
    def altarica_Addition(self):
        return self.__altarica_Addition

    @altarica_Addition.setter
    def altarica_Addition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Addition__altarica_Addition", None)
        self.__altarica_Addition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Expression96"):
                opp_val = getattr(old_value, "altarica_Expression96", None)
                if opp_val == self:
                    setattr(old_value, "altarica_Expression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Expression96"):
                opp_val = getattr(value, "altarica_Expression96", None)
                setattr(value, "altarica_Expression96", self)

class altarica_ARString(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class altarica_Not(Expression):

    pass
class altarica_ARBoolean(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class altarica_Expression:

    pass
class altarica_EObject:

    pass
class altarica_SwitchExpression(Expression):

    pass
class Type:

    pass
class altarica_NamedType(Type):

    pass
class altarica_BaseType(Type):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class altarica_Type:

    pass
class Declaration:

    pass
class AbstractDeclaration:

    pass
class altarica_CaseExpression:

    pass
class altarica_Instruction:

    pass
class altarica_TransitionExpression:

    pass
class altarica_NameRef(Expression):

    pass
class altarica_LabeledTransition:

    pass
class altarica_Declaration:

    pass
class altarica_NamedElement(AbstractDeclaration, Declaration):

    def __init__(self, name: str, altarica_NamedElement: "altarica_NamedType" = None, altarica_NamedElement12: "altarica_NameRef" = None, altarica_NamedElement27: "altarica_Domain" = None, altarica_NamedElement38: "altarica_Variable" = None, altarica_NamedElement42: "altarica_Event" = None):
        self.name = name
        self.altarica_NamedElement = altarica_NamedElement
        self.altarica_NamedElement12 = altarica_NamedElement12
        self.altarica_NamedElement27 = altarica_NamedElement27
        self.altarica_NamedElement38 = altarica_NamedElement38
        self.altarica_NamedElement42 = altarica_NamedElement42
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def altarica_NamedElement38(self):
        return self.__altarica_NamedElement38

    @altarica_NamedElement38.setter
    def altarica_NamedElement38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_NamedElement__altarica_NamedElement38", None)
        self.__altarica_NamedElement38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Variable37"):
                opp_val = getattr(old_value, "altarica_Variable37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Variable37"):
                opp_val = getattr(value, "altarica_Variable37", None)
                if opp_val is None:
                    setattr(value, "altarica_Variable37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def altarica_NamedElement27(self):
        return self.__altarica_NamedElement27

    @altarica_NamedElement27.setter
    def altarica_NamedElement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_NamedElement__altarica_NamedElement27", None)
        self.__altarica_NamedElement27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Domain"):
                opp_val = getattr(old_value, "altarica_Domain", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Domain"):
                opp_val = getattr(value, "altarica_Domain", None)
                if opp_val is None:
                    setattr(value, "altarica_Domain", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def altarica_NamedElement42(self):
        return self.__altarica_NamedElement42

    @altarica_NamedElement42.setter
    def altarica_NamedElement42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_NamedElement__altarica_NamedElement42", None)
        self.__altarica_NamedElement42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Event"):
                opp_val = getattr(old_value, "altarica_Event", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Event"):
                opp_val = getattr(value, "altarica_Event", None)
                if opp_val is None:
                    setattr(value, "altarica_Event", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def altarica_NamedElement(self):
        return self.__altarica_NamedElement

    @altarica_NamedElement.setter
    def altarica_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_NamedElement__altarica_NamedElement", None)
        self.__altarica_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_NamedType"):
                opp_val = getattr(old_value, "altarica_NamedType", None)
                if opp_val == self:
                    setattr(old_value, "altarica_NamedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_NamedType"):
                opp_val = getattr(value, "altarica_NamedType", None)
                setattr(value, "altarica_NamedType", self)

    @property
    def altarica_NamedElement12(self):
        return self.__altarica_NamedElement12

    @altarica_NamedElement12.setter
    def altarica_NamedElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_NamedElement__altarica_NamedElement12", None)
        self.__altarica_NamedElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_NameRef11"):
                opp_val = getattr(old_value, "altarica_NameRef11", None)
                if opp_val == self:
                    setattr(old_value, "altarica_NameRef11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_NameRef11"):
                opp_val = getattr(value, "altarica_NameRef11", None)
                setattr(value, "altarica_NameRef11", self)

class altarica_AbstractDeclaration:

    pass
class altarica_Error:

    def __init__(self, severity: str, message: str, altarica_Error: "altarica_Model" = None):
        self.severity = severity
        self.message = message
        self.altarica_Error = altarica_Error
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def altarica_Error(self):
        return self.__altarica_Error

    @altarica_Error.setter
    def altarica_Error(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Error__altarica_Error", None)
        self.__altarica_Error = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Model"):
                opp_val = getattr(old_value, "altarica_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Model"):
                opp_val = getattr(value, "altarica_Model", None)
                if opp_val is None:
                    setattr(value, "altarica_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class altarica_Model:

    pass
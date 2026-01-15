from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AddOper(Enum):
    ADD = "ADD"
    MINUS = "MINUS"
class DataTypes(Enum):
    double = "double"
    long = "long"
    String = "String"
    int = "int"
    number = "number"
    Date = "Date"
class Cardinality(Enum):
    CEROTOMANY = "CEROTOMANY"
    CEROTOONE = "CEROTOONE"
class MultOper(Enum):
    MULT = "MULT"
    DIV = "DIV"
class RelationType(Enum):
    COMPOSITION = "COMPOSITION"
    REFERENCE = "REFERENCE"
class LogicalCononnector(Enum):
    AND = "AND"
    OR = "OR"
class LogicalOperator(Enum):
    LESSTHAN = "LESSTHAN"
    EQUALTO = "EQUALTO"
    DIFFERENT = "DIFFERENT"


############################################
# Definition of Classes
############################################

class Relation:

    pass
class PagosPim_NewEClass21:

    pass
class Expression:

    pass
class PagosPim_Mult(Expression):

    def __init__(self, operator: str, PagosPim_Mult: "PagosPim_Expression" = None, PagosPim_Mult95: "PagosPim_Expression" = None):
        self.operator = operator
        self.PagosPim_Mult = PagosPim_Mult
        self.PagosPim_Mult95 = PagosPim_Mult95
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def PagosPim_Mult95(self):
        return self.__PagosPim_Mult95

    @PagosPim_Mult95.setter
    def PagosPim_Mult95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Mult__PagosPim_Mult95", None)
        self.__PagosPim_Mult95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Expression96"):
                opp_val = getattr(old_value, "PagosPim_Expression96", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Expression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Expression96"):
                opp_val = getattr(value, "PagosPim_Expression96", None)
                setattr(value, "PagosPim_Expression96", self)

    @property
    def PagosPim_Mult(self):
        return self.__PagosPim_Mult

    @PagosPim_Mult.setter
    def PagosPim_Mult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Mult__PagosPim_Mult", None)
        self.__PagosPim_Mult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Expression93"):
                opp_val = getattr(old_value, "PagosPim_Expression93", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Expression93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Expression93"):
                opp_val = getattr(value, "PagosPim_Expression93", None)
                setattr(value, "PagosPim_Expression93", self)

class PagosPim_Add(Expression):

    def __init__(self, operator: str, PagosPim_Add: "PagosPim_Expression" = None, PagosPim_Add90: "PagosPim_Expression" = None):
        self.operator = operator
        self.PagosPim_Add = PagosPim_Add
        self.PagosPim_Add90 = PagosPim_Add90
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def PagosPim_Add90(self):
        return self.__PagosPim_Add90

    @PagosPim_Add90.setter
    def PagosPim_Add90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Add__PagosPim_Add90", None)
        self.__PagosPim_Add90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Expression91"):
                opp_val = getattr(old_value, "PagosPim_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Expression91"):
                opp_val = getattr(value, "PagosPim_Expression91", None)
                setattr(value, "PagosPim_Expression91", self)

    @property
    def PagosPim_Add(self):
        return self.__PagosPim_Add

    @PagosPim_Add.setter
    def PagosPim_Add(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Add__PagosPim_Add", None)
        self.__PagosPim_Add = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Expression88"):
                opp_val = getattr(old_value, "PagosPim_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Expression88"):
                opp_val = getattr(value, "PagosPim_Expression88", None)
                setattr(value, "PagosPim_Expression88", self)

class PagosPim_TerminalValue(Expression):

    def __init__(self, method: str, value: str, PagosPim_TerminalValue: "PagosPim_LogicalExpression" = None, PagosPim_TerminalValue74: "PagosPim_LogicalExpression" = None, PagosPim_TerminalValue82: "PagosPim_EObject" = None, PagosPim_TerminalValue85: "PagosPim_Attribute" = None):
        self.method = method
        self.value = value
        self.PagosPim_TerminalValue = PagosPim_TerminalValue
        self.PagosPim_TerminalValue74 = PagosPim_TerminalValue74
        self.PagosPim_TerminalValue82 = PagosPim_TerminalValue82
        self.PagosPim_TerminalValue85 = PagosPim_TerminalValue85
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def PagosPim_TerminalValue74(self):
        return self.__PagosPim_TerminalValue74

    @PagosPim_TerminalValue74.setter
    def PagosPim_TerminalValue74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_TerminalValue__PagosPim_TerminalValue74", None)
        self.__PagosPim_TerminalValue74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_LogicalExpression73"):
                opp_val = getattr(old_value, "PagosPim_LogicalExpression73", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_LogicalExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_LogicalExpression73"):
                opp_val = getattr(value, "PagosPim_LogicalExpression73", None)
                setattr(value, "PagosPim_LogicalExpression73", self)

    @property
    def PagosPim_TerminalValue85(self):
        return self.__PagosPim_TerminalValue85

    @PagosPim_TerminalValue85.setter
    def PagosPim_TerminalValue85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_TerminalValue__PagosPim_TerminalValue85", None)
        self.__PagosPim_TerminalValue85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Attribute86"):
                opp_val = getattr(old_value, "PagosPim_Attribute86", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Attribute86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Attribute86"):
                opp_val = getattr(value, "PagosPim_Attribute86", None)
                setattr(value, "PagosPim_Attribute86", self)

    @property
    def PagosPim_TerminalValue(self):
        return self.__PagosPim_TerminalValue

    @PagosPim_TerminalValue.setter
    def PagosPim_TerminalValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_TerminalValue__PagosPim_TerminalValue", None)
        self.__PagosPim_TerminalValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_LogicalExpression71"):
                opp_val = getattr(old_value, "PagosPim_LogicalExpression71", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_LogicalExpression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_LogicalExpression71"):
                opp_val = getattr(value, "PagosPim_LogicalExpression71", None)
                setattr(value, "PagosPim_LogicalExpression71", self)

    @property
    def PagosPim_TerminalValue82(self):
        return self.__PagosPim_TerminalValue82

    @PagosPim_TerminalValue82.setter
    def PagosPim_TerminalValue82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_TerminalValue__PagosPim_TerminalValue82", None)
        self.__PagosPim_TerminalValue82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_EObject83"):
                opp_val = getattr(old_value, "PagosPim_EObject83", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_EObject83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_EObject83"):
                opp_val = getattr(value, "PagosPim_EObject83", None)
                setattr(value, "PagosPim_EObject83", self)

class PagosPim_IfBlock:

    pass
class PagosPim_LogicalExpression:

    def __init__(self, logicalOperator: str, literal: str, conOper: str, PagosPim_LogicalExpression: "PagosPim_IfCondition" = None, PagosPim_LogicalExpression71: "PagosPim_TerminalValue" = None, PagosPim_LogicalExpression73: "PagosPim_TerminalValue" = None, PagosPim_LogicalExpression77: "PagosPim_LogicalExpression" = None, PagosPim_LogicalExpression75: "PagosPim_LogicalExpression" = None):
        self.logicalOperator = logicalOperator
        self.literal = literal
        self.conOper = conOper
        self.PagosPim_LogicalExpression = PagosPim_LogicalExpression
        self.PagosPim_LogicalExpression71 = PagosPim_LogicalExpression71
        self.PagosPim_LogicalExpression73 = PagosPim_LogicalExpression73
        self.PagosPim_LogicalExpression77 = PagosPim_LogicalExpression77
        self.PagosPim_LogicalExpression75 = PagosPim_LogicalExpression75
        
    @property
    def conOper(self) -> str:
        return self.__conOper

    @conOper.setter
    def conOper(self, conOper: str):
        self.__conOper = conOper

    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def logicalOperator(self) -> str:
        return self.__logicalOperator

    @logicalOperator.setter
    def logicalOperator(self, logicalOperator: str):
        self.__logicalOperator = logicalOperator

    @property
    def PagosPim_LogicalExpression77(self):
        return self.__PagosPim_LogicalExpression77

    @PagosPim_LogicalExpression77.setter
    def PagosPim_LogicalExpression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_LogicalExpression__PagosPim_LogicalExpression77", None)
        self.__PagosPim_LogicalExpression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_LogicalExpression75"):
                opp_val = getattr(old_value, "PagosPim_LogicalExpression75", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_LogicalExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_LogicalExpression75"):
                opp_val = getattr(value, "PagosPim_LogicalExpression75", None)
                setattr(value, "PagosPim_LogicalExpression75", self)

    @property
    def PagosPim_LogicalExpression75(self):
        return self.__PagosPim_LogicalExpression75

    @PagosPim_LogicalExpression75.setter
    def PagosPim_LogicalExpression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_LogicalExpression__PagosPim_LogicalExpression75", None)
        self.__PagosPim_LogicalExpression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_LogicalExpression77"):
                opp_val = getattr(old_value, "PagosPim_LogicalExpression77", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_LogicalExpression77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_LogicalExpression77"):
                opp_val = getattr(value, "PagosPim_LogicalExpression77", None)
                setattr(value, "PagosPim_LogicalExpression77", self)

    @property
    def PagosPim_LogicalExpression(self):
        return self.__PagosPim_LogicalExpression

    @PagosPim_LogicalExpression.setter
    def PagosPim_LogicalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_LogicalExpression__PagosPim_LogicalExpression", None)
        self.__PagosPim_LogicalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_IfCondition57"):
                opp_val = getattr(old_value, "PagosPim_IfCondition57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_IfCondition57"):
                opp_val = getattr(value, "PagosPim_IfCondition57", None)
                if opp_val is None:
                    setattr(value, "PagosPim_IfCondition57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PagosPim_LogicalExpression73(self):
        return self.__PagosPim_LogicalExpression73

    @PagosPim_LogicalExpression73.setter
    def PagosPim_LogicalExpression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_LogicalExpression__PagosPim_LogicalExpression73", None)
        self.__PagosPim_LogicalExpression73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_TerminalValue74"):
                opp_val = getattr(old_value, "PagosPim_TerminalValue74", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_TerminalValue74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_TerminalValue74"):
                opp_val = getattr(value, "PagosPim_TerminalValue74", None)
                setattr(value, "PagosPim_TerminalValue74", self)

    @property
    def PagosPim_LogicalExpression71(self):
        return self.__PagosPim_LogicalExpression71

    @PagosPim_LogicalExpression71.setter
    def PagosPim_LogicalExpression71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_LogicalExpression__PagosPim_LogicalExpression71", None)
        self.__PagosPim_LogicalExpression71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_TerminalValue"):
                opp_val = getattr(old_value, "PagosPim_TerminalValue", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_TerminalValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_TerminalValue"):
                opp_val = getattr(value, "PagosPim_TerminalValue", None)
                setattr(value, "PagosPim_TerminalValue", self)

class PagosPim_ProgramIfExpression:

    pass
class PagosPim_ElseSegment:

    pass
class PagosPim_IfCondition:

    pass
class PagosPim_Return:

    def __init__(self, type: str, PagosPim_Return49: "PagosPim_Body" = None, PagosPim_Return60: "PagosPim_IfCondition" = None, PagosPim_Return: set["PagosPim_Expression"] = None, PagosPim_Return69: "PagosPim_ElseSegment" = None):
        self.type = type
        self.PagosPim_Return49 = PagosPim_Return49
        self.PagosPim_Return60 = PagosPim_Return60
        self.PagosPim_Return = PagosPim_Return if PagosPim_Return is not None else set()
        self.PagosPim_Return69 = PagosPim_Return69
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def PagosPim_Return(self):
        return self.__PagosPim_Return

    @PagosPim_Return.setter
    def PagosPim_Return(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Return__PagosPim_Return", None)
        self.__PagosPim_Return = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_Expression44"):
                    opp_val = getattr(item, "PagosPim_Expression44", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_Expression44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_Expression44"):
                    opp_val = getattr(item, "PagosPim_Expression44", None)
                    
                    setattr(item, "PagosPim_Expression44", self)
                    

    @property
    def PagosPim_Return60(self):
        return self.__PagosPim_Return60

    @PagosPim_Return60.setter
    def PagosPim_Return60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Return__PagosPim_Return60", None)
        self.__PagosPim_Return60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_IfCondition59"):
                opp_val = getattr(old_value, "PagosPim_IfCondition59", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_IfCondition59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_IfCondition59"):
                opp_val = getattr(value, "PagosPim_IfCondition59", None)
                setattr(value, "PagosPim_IfCondition59", self)

    @property
    def PagosPim_Return49(self):
        return self.__PagosPim_Return49

    @PagosPim_Return49.setter
    def PagosPim_Return49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Return__PagosPim_Return49", None)
        self.__PagosPim_Return49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Body48"):
                opp_val = getattr(old_value, "PagosPim_Body48", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Body48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Body48"):
                opp_val = getattr(value, "PagosPim_Body48", None)
                setattr(value, "PagosPim_Body48", self)

    @property
    def PagosPim_Return69(self):
        return self.__PagosPim_Return69

    @PagosPim_Return69.setter
    def PagosPim_Return69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Return__PagosPim_Return69", None)
        self.__PagosPim_Return69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_ElseSegment68"):
                opp_val = getattr(old_value, "PagosPim_ElseSegment68", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_ElseSegment68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_ElseSegment68"):
                opp_val = getattr(value, "PagosPim_ElseSegment68", None)
                setattr(value, "PagosPim_ElseSegment68", self)

class PagosPim_EObject:

    pass
class PagosPim_AttributeDefinition(ABC):

    def __init__(self, name: str, type: str, PagosPim_AttributeDefinition: "PagosPim_EObject" = None):
        self.name = name
        self.type = type
        self.PagosPim_AttributeDefinition = PagosPim_AttributeDefinition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def PagosPim_AttributeDefinition(self):
        return self.__PagosPim_AttributeDefinition

    @PagosPim_AttributeDefinition.setter
    def PagosPim_AttributeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_AttributeDefinition__PagosPim_AttributeDefinition", None)
        self.__PagosPim_AttributeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_EObject"):
                opp_val = getattr(old_value, "PagosPim_EObject", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_EObject"):
                opp_val = getattr(value, "PagosPim_EObject", None)
                setattr(value, "PagosPim_EObject", self)

class PagosPim_GenericComponent:

    def __init__(self, name: str, PagosPim_GenericComponent25: set["PagosPim_Relation"] = None, PagosPim_GenericComponent27: set["PagosPim_Operation"] = None, PagosPim_GenericComponent: set["PagosPim_Attribute"] = None, PagosPim_GenericComponent41: "PagosPim_Relation" = None):
        self.name = name
        self.PagosPim_GenericComponent25 = PagosPim_GenericComponent25 if PagosPim_GenericComponent25 is not None else set()
        self.PagosPim_GenericComponent27 = PagosPim_GenericComponent27 if PagosPim_GenericComponent27 is not None else set()
        self.PagosPim_GenericComponent = PagosPim_GenericComponent if PagosPim_GenericComponent is not None else set()
        self.PagosPim_GenericComponent41 = PagosPim_GenericComponent41
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PagosPim_GenericComponent(self):
        return self.__PagosPim_GenericComponent

    @PagosPim_GenericComponent.setter
    def PagosPim_GenericComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_GenericComponent__PagosPim_GenericComponent", None)
        self.__PagosPim_GenericComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_Attribute"):
                    opp_val = getattr(item, "PagosPim_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_Attribute"):
                    opp_val = getattr(item, "PagosPim_Attribute", None)
                    
                    setattr(item, "PagosPim_Attribute", self)
                    

    @property
    def PagosPim_GenericComponent25(self):
        return self.__PagosPim_GenericComponent25

    @PagosPim_GenericComponent25.setter
    def PagosPim_GenericComponent25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_GenericComponent__PagosPim_GenericComponent25", None)
        self.__PagosPim_GenericComponent25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_Relation"):
                    opp_val = getattr(item, "PagosPim_Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_Relation"):
                    opp_val = getattr(item, "PagosPim_Relation", None)
                    
                    setattr(item, "PagosPim_Relation", self)
                    

    @property
    def PagosPim_GenericComponent27(self):
        return self.__PagosPim_GenericComponent27

    @PagosPim_GenericComponent27.setter
    def PagosPim_GenericComponent27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_GenericComponent__PagosPim_GenericComponent27", None)
        self.__PagosPim_GenericComponent27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_Operation"):
                    opp_val = getattr(item, "PagosPim_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_Operation"):
                    opp_val = getattr(item, "PagosPim_Operation", None)
                    
                    setattr(item, "PagosPim_Operation", self)
                    

    @property
    def PagosPim_GenericComponent41(self):
        return self.__PagosPim_GenericComponent41

    @PagosPim_GenericComponent41.setter
    def PagosPim_GenericComponent41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_GenericComponent__PagosPim_GenericComponent41", None)
        self.__PagosPim_GenericComponent41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Relation40"):
                opp_val = getattr(old_value, "PagosPim_Relation40", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Relation40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Relation40"):
                opp_val = getattr(value, "PagosPim_Relation40", None)
                setattr(value, "PagosPim_Relation40", self)

class PagosPim_Body:

    pass
class PagosPim_ParameterList:

    pass
class PagosPim_Expression:

    pass
class AttributeDefinition:

    pass
class PagosPim_Parameter(AttributeDefinition):

    pass
class PagosPim_Attribute(AttributeDefinition):

    def __init__(self, isIndex: str, PagosPim_Attribute29: "PagosPim_Expression" = None, PagosPim_Attribute36: "PagosPim_Operation" = None, PagosPim_Attribute: "PagosPim_GenericComponent" = None, PagosPim_Attribute86: "PagosPim_TerminalValue" = None):
        self.isIndex = isIndex
        self.PagosPim_Attribute29 = PagosPim_Attribute29
        self.PagosPim_Attribute36 = PagosPim_Attribute36
        self.PagosPim_Attribute = PagosPim_Attribute
        self.PagosPim_Attribute86 = PagosPim_Attribute86
        
    @property
    def isIndex(self) -> str:
        return self.__isIndex

    @isIndex.setter
    def isIndex(self, isIndex: str):
        self.__isIndex = isIndex

    @property
    def PagosPim_Attribute86(self):
        return self.__PagosPim_Attribute86

    @PagosPim_Attribute86.setter
    def PagosPim_Attribute86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Attribute__PagosPim_Attribute86", None)
        self.__PagosPim_Attribute86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_TerminalValue85"):
                opp_val = getattr(old_value, "PagosPim_TerminalValue85", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_TerminalValue85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_TerminalValue85"):
                opp_val = getattr(value, "PagosPim_TerminalValue85", None)
                setattr(value, "PagosPim_TerminalValue85", self)

    @property
    def PagosPim_Attribute29(self):
        return self.__PagosPim_Attribute29

    @PagosPim_Attribute29.setter
    def PagosPim_Attribute29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Attribute__PagosPim_Attribute29", None)
        self.__PagosPim_Attribute29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Expression"):
                opp_val = getattr(old_value, "PagosPim_Expression", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Expression"):
                opp_val = getattr(value, "PagosPim_Expression", None)
                setattr(value, "PagosPim_Expression", self)

    @property
    def PagosPim_Attribute(self):
        return self.__PagosPim_Attribute

    @PagosPim_Attribute.setter
    def PagosPim_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Attribute__PagosPim_Attribute", None)
        self.__PagosPim_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_GenericComponent"):
                opp_val = getattr(old_value, "PagosPim_GenericComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_GenericComponent"):
                opp_val = getattr(value, "PagosPim_GenericComponent", None)
                if opp_val is None:
                    setattr(value, "PagosPim_GenericComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PagosPim_Attribute36(self):
        return self.__PagosPim_Attribute36

    @PagosPim_Attribute36.setter
    def PagosPim_Attribute36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Attribute__PagosPim_Attribute36", None)
        self.__PagosPim_Attribute36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Operation35"):
                opp_val = getattr(old_value, "PagosPim_Operation35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Operation35"):
                opp_val = getattr(value, "PagosPim_Operation35", None)
                if opp_val is None:
                    setattr(value, "PagosPim_Operation35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PagosPim_Operation:

    def __init__(self, name: str, PagosPim_Operation: "PagosPim_GenericComponent" = None, PagosPim_Operation31: "PagosPim_ParameterList" = None, PagosPim_Operation33: "PagosPim_Body" = None, PagosPim_Operation35: set["PagosPim_Attribute"] = None):
        self.name = name
        self.PagosPim_Operation = PagosPim_Operation
        self.PagosPim_Operation31 = PagosPim_Operation31
        self.PagosPim_Operation33 = PagosPim_Operation33
        self.PagosPim_Operation35 = PagosPim_Operation35 if PagosPim_Operation35 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PagosPim_Operation(self):
        return self.__PagosPim_Operation

    @PagosPim_Operation.setter
    def PagosPim_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Operation__PagosPim_Operation", None)
        self.__PagosPim_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_GenericComponent27"):
                opp_val = getattr(old_value, "PagosPim_GenericComponent27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_GenericComponent27"):
                opp_val = getattr(value, "PagosPim_GenericComponent27", None)
                if opp_val is None:
                    setattr(value, "PagosPim_GenericComponent27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PagosPim_Operation33(self):
        return self.__PagosPim_Operation33

    @PagosPim_Operation33.setter
    def PagosPim_Operation33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Operation__PagosPim_Operation33", None)
        self.__PagosPim_Operation33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Body"):
                opp_val = getattr(old_value, "PagosPim_Body", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Body", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Body"):
                opp_val = getattr(value, "PagosPim_Body", None)
                setattr(value, "PagosPim_Body", self)

    @property
    def PagosPim_Operation31(self):
        return self.__PagosPim_Operation31

    @PagosPim_Operation31.setter
    def PagosPim_Operation31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Operation__PagosPim_Operation31", None)
        self.__PagosPim_Operation31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_ParameterList"):
                opp_val = getattr(old_value, "PagosPim_ParameterList", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_ParameterList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_ParameterList"):
                opp_val = getattr(value, "PagosPim_ParameterList", None)
                setattr(value, "PagosPim_ParameterList", self)

    @property
    def PagosPim_Operation35(self):
        return self.__PagosPim_Operation35

    @PagosPim_Operation35.setter
    def PagosPim_Operation35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Operation__PagosPim_Operation35", None)
        self.__PagosPim_Operation35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_Attribute36"):
                    opp_val = getattr(item, "PagosPim_Attribute36", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_Attribute36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_Attribute36"):
                    opp_val = getattr(item, "PagosPim_Attribute36", None)
                    
                    setattr(item, "PagosPim_Attribute36", self)
                    

class PagosPim_Relation:

    def __init__(self, type: str, name: str, cardinality: str, PagosPim_Relation: "PagosPim_GenericComponent" = None, PagosPim_Relation40: "PagosPim_GenericComponent" = None):
        self.type = type
        self.name = name
        self.cardinality = cardinality
        self.PagosPim_Relation = PagosPim_Relation
        self.PagosPim_Relation40 = PagosPim_Relation40
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def PagosPim_Relation40(self):
        return self.__PagosPim_Relation40

    @PagosPim_Relation40.setter
    def PagosPim_Relation40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Relation__PagosPim_Relation40", None)
        self.__PagosPim_Relation40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_GenericComponent41"):
                opp_val = getattr(old_value, "PagosPim_GenericComponent41", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_GenericComponent41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_GenericComponent41"):
                opp_val = getattr(value, "PagosPim_GenericComponent41", None)
                setattr(value, "PagosPim_GenericComponent41", self)

    @property
    def PagosPim_Relation(self):
        return self.__PagosPim_Relation

    @PagosPim_Relation.setter
    def PagosPim_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Relation__PagosPim_Relation", None)
        self.__PagosPim_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_GenericComponent25"):
                opp_val = getattr(old_value, "PagosPim_GenericComponent25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_GenericComponent25"):
                opp_val = getattr(value, "PagosPim_GenericComponent25", None)
                if opp_val is None:
                    setattr(value, "PagosPim_GenericComponent25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PagosPim_SubComponent(Relation):

    pass
class GenericComponent:

    pass
class Operation:

    pass
class PagosPim_ServerService(GenericComponent):

    pass
class PagosPim_LogicComponent(GenericComponent):

    def __init__(self, persistible: bool, PagosPim_LogicComponent: "PagosPim_Application" = None, PagosPim_LogicComponent99: "PagosPim_ServerService" = None, PagosPim_LogicComponent101: "PagosPim_DataLayerComponent" = None):
        self.persistible = persistible
        self.PagosPim_LogicComponent = PagosPim_LogicComponent
        self.PagosPim_LogicComponent99 = PagosPim_LogicComponent99
        self.PagosPim_LogicComponent101 = PagosPim_LogicComponent101
        
    @property
    def persistible(self) -> bool:
        return self.__persistible

    @persistible.setter
    def persistible(self, persistible: bool):
        self.__persistible = persistible

    @property
    def PagosPim_LogicComponent99(self):
        return self.__PagosPim_LogicComponent99

    @PagosPim_LogicComponent99.setter
    def PagosPim_LogicComponent99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_LogicComponent__PagosPim_LogicComponent99", None)
        self.__PagosPim_LogicComponent99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_ServerService98"):
                opp_val = getattr(old_value, "PagosPim_ServerService98", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_ServerService98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_ServerService98"):
                opp_val = getattr(value, "PagosPim_ServerService98", None)
                setattr(value, "PagosPim_ServerService98", self)

    @property
    def PagosPim_LogicComponent(self):
        return self.__PagosPim_LogicComponent

    @PagosPim_LogicComponent.setter
    def PagosPim_LogicComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_LogicComponent__PagosPim_LogicComponent", None)
        self.__PagosPim_LogicComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Application"):
                opp_val = getattr(old_value, "PagosPim_Application", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Application"):
                opp_val = getattr(value, "PagosPim_Application", None)
                if opp_val is None:
                    setattr(value, "PagosPim_Application", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PagosPim_LogicComponent101(self):
        return self.__PagosPim_LogicComponent101

    @PagosPim_LogicComponent101.setter
    def PagosPim_LogicComponent101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_LogicComponent__PagosPim_LogicComponent101", None)
        self.__PagosPim_LogicComponent101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_DataLayerComponent102"):
                opp_val = getattr(old_value, "PagosPim_DataLayerComponent102", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_DataLayerComponent102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_DataLayerComponent102"):
                opp_val = getattr(value, "PagosPim_DataLayerComponent102", None)
                setattr(value, "PagosPim_DataLayerComponent102", self)

class PagosPim_FrontService(Operation):

    def __init__(self, fullName: str, PagosPim_FrontService: "PagosPim_Input" = None, PagosPim_FrontService12: "PagosPim_FrontService" = None, PagosPim_FrontService10: set["PagosPim_FrontService"] = None, PagosPim_FrontService14: "PagosPim_ServerService" = None, PagosPim_FrontService22: "PagosPim_ViewComponent" = None, PagosPim_FrontService109: "PagosPim_Action" = None):
        self.fullName = fullName
        self.PagosPim_FrontService = PagosPim_FrontService
        self.PagosPim_FrontService12 = PagosPim_FrontService12
        self.PagosPim_FrontService10 = PagosPim_FrontService10 if PagosPim_FrontService10 is not None else set()
        self.PagosPim_FrontService14 = PagosPim_FrontService14
        self.PagosPim_FrontService22 = PagosPim_FrontService22
        self.PagosPim_FrontService109 = PagosPim_FrontService109
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def PagosPim_FrontService109(self):
        return self.__PagosPim_FrontService109

    @PagosPim_FrontService109.setter
    def PagosPim_FrontService109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_FrontService__PagosPim_FrontService109", None)
        self.__PagosPim_FrontService109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Action"):
                opp_val = getattr(old_value, "PagosPim_Action", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Action"):
                opp_val = getattr(value, "PagosPim_Action", None)
                setattr(value, "PagosPim_Action", self)

    @property
    def PagosPim_FrontService22(self):
        return self.__PagosPim_FrontService22

    @PagosPim_FrontService22.setter
    def PagosPim_FrontService22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_FrontService__PagosPim_FrontService22", None)
        self.__PagosPim_FrontService22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_ViewComponent21"):
                opp_val = getattr(old_value, "PagosPim_ViewComponent21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_ViewComponent21"):
                opp_val = getattr(value, "PagosPim_ViewComponent21", None)
                if opp_val is None:
                    setattr(value, "PagosPim_ViewComponent21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PagosPim_FrontService(self):
        return self.__PagosPim_FrontService

    @PagosPim_FrontService.setter
    def PagosPim_FrontService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_FrontService__PagosPim_FrontService", None)
        self.__PagosPim_FrontService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Input"):
                opp_val = getattr(old_value, "PagosPim_Input", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_Input", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Input"):
                opp_val = getattr(value, "PagosPim_Input", None)
                setattr(value, "PagosPim_Input", self)

    @property
    def PagosPim_FrontService10(self):
        return self.__PagosPim_FrontService10

    @PagosPim_FrontService10.setter
    def PagosPim_FrontService10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_FrontService__PagosPim_FrontService10", None)
        self.__PagosPim_FrontService10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_FrontService12"):
                    opp_val = getattr(item, "PagosPim_FrontService12", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_FrontService12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_FrontService12"):
                    opp_val = getattr(item, "PagosPim_FrontService12", None)
                    
                    setattr(item, "PagosPim_FrontService12", self)
                    

    @property
    def PagosPim_FrontService14(self):
        return self.__PagosPim_FrontService14

    @PagosPim_FrontService14.setter
    def PagosPim_FrontService14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_FrontService__PagosPim_FrontService14", None)
        self.__PagosPim_FrontService14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_ServerService15"):
                opp_val = getattr(old_value, "PagosPim_ServerService15", None)
                if opp_val == self:
                    setattr(old_value, "PagosPim_ServerService15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_ServerService15"):
                opp_val = getattr(value, "PagosPim_ServerService15", None)
                setattr(value, "PagosPim_ServerService15", self)

    @property
    def PagosPim_FrontService12(self):
        return self.__PagosPim_FrontService12

    @PagosPim_FrontService12.setter
    def PagosPim_FrontService12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_FrontService__PagosPim_FrontService12", None)
        self.__PagosPim_FrontService12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_FrontService10"):
                opp_val = getattr(old_value, "PagosPim_FrontService10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_FrontService10"):
                opp_val = getattr(value, "PagosPim_FrontService10", None)
                if opp_val is None:
                    setattr(value, "PagosPim_FrontService10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Attribute:

    pass
class PagosPim_Field(Attribute):

    pass
class Control:

    pass
class PagosPim_Output(Control, Attribute):

    pass
class PagosPim_Action(Control, Operation):

    pass
class PagosPim_Input(Control, Attribute):

    pass
class PagosPim_Control:

    def __init__(self, label: str, PagosPim_Control: "PagosPim_ViewComponent" = None):
        self.label = label
        self.PagosPim_Control = PagosPim_Control
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def PagosPim_Control(self):
        return self.__PagosPim_Control

    @PagosPim_Control.setter
    def PagosPim_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Control__PagosPim_Control", None)
        self.__PagosPim_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_ViewComponent19"):
                opp_val = getattr(old_value, "PagosPim_ViewComponent19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_ViewComponent19"):
                opp_val = getattr(value, "PagosPim_ViewComponent19", None)
                if opp_val is None:
                    setattr(value, "PagosPim_ViewComponent19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PagosPim_ViewComponent(GenericComponent):

    def __init__(self, title: str, PagosPim_ViewComponent: "PagosPim_Application" = None, PagosPim_ViewComponent17: set["PagosPim_SubComponent"] = None, PagosPim_ViewComponent19: set["PagosPim_Control"] = None, PagosPim_ViewComponent21: set["PagosPim_FrontService"] = None):
        self.title = title
        self.PagosPim_ViewComponent = PagosPim_ViewComponent
        self.PagosPim_ViewComponent17 = PagosPim_ViewComponent17 if PagosPim_ViewComponent17 is not None else set()
        self.PagosPim_ViewComponent19 = PagosPim_ViewComponent19 if PagosPim_ViewComponent19 is not None else set()
        self.PagosPim_ViewComponent21 = PagosPim_ViewComponent21 if PagosPim_ViewComponent21 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def PagosPim_ViewComponent21(self):
        return self.__PagosPim_ViewComponent21

    @PagosPim_ViewComponent21.setter
    def PagosPim_ViewComponent21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_ViewComponent__PagosPim_ViewComponent21", None)
        self.__PagosPim_ViewComponent21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_FrontService22"):
                    opp_val = getattr(item, "PagosPim_FrontService22", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_FrontService22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_FrontService22"):
                    opp_val = getattr(item, "PagosPim_FrontService22", None)
                    
                    setattr(item, "PagosPim_FrontService22", self)
                    

    @property
    def PagosPim_ViewComponent19(self):
        return self.__PagosPim_ViewComponent19

    @PagosPim_ViewComponent19.setter
    def PagosPim_ViewComponent19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_ViewComponent__PagosPim_ViewComponent19", None)
        self.__PagosPim_ViewComponent19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_Control"):
                    opp_val = getattr(item, "PagosPim_Control", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_Control", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_Control"):
                    opp_val = getattr(item, "PagosPim_Control", None)
                    
                    setattr(item, "PagosPim_Control", self)
                    

    @property
    def PagosPim_ViewComponent(self):
        return self.__PagosPim_ViewComponent

    @PagosPim_ViewComponent.setter
    def PagosPim_ViewComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_ViewComponent__PagosPim_ViewComponent", None)
        self.__PagosPim_ViewComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagosPim_Application8"):
                opp_val = getattr(old_value, "PagosPim_Application8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagosPim_Application8"):
                opp_val = getattr(value, "PagosPim_Application8", None)
                if opp_val is None:
                    setattr(value, "PagosPim_Application8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PagosPim_ViewComponent17(self):
        return self.__PagosPim_ViewComponent17

    @PagosPim_ViewComponent17.setter
    def PagosPim_ViewComponent17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_ViewComponent__PagosPim_ViewComponent17", None)
        self.__PagosPim_ViewComponent17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_SubComponent"):
                    opp_val = getattr(item, "PagosPim_SubComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_SubComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_SubComponent"):
                    opp_val = getattr(item, "PagosPim_SubComponent", None)
                    
                    setattr(item, "PagosPim_SubComponent", self)
                    

class PagosPim_DaoComponent(GenericComponent):

    pass
class PagosPim_DataLayerComponent(GenericComponent):

    pass
class PagosPim_Application:

    def __init__(self, name: str, PagosPim_Application2: set["PagosPim_ServerService"] = None, PagosPim_Application4: set["PagosPim_DataLayerComponent"] = None, PagosPim_Application6: set["PagosPim_DaoComponent"] = None, PagosPim_Application8: set["PagosPim_ViewComponent"] = None, PagosPim_Application: set["PagosPim_LogicComponent"] = None):
        self.name = name
        self.PagosPim_Application2 = PagosPim_Application2 if PagosPim_Application2 is not None else set()
        self.PagosPim_Application4 = PagosPim_Application4 if PagosPim_Application4 is not None else set()
        self.PagosPim_Application6 = PagosPim_Application6 if PagosPim_Application6 is not None else set()
        self.PagosPim_Application8 = PagosPim_Application8 if PagosPim_Application8 is not None else set()
        self.PagosPim_Application = PagosPim_Application if PagosPim_Application is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PagosPim_Application8(self):
        return self.__PagosPim_Application8

    @PagosPim_Application8.setter
    def PagosPim_Application8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Application__PagosPim_Application8", None)
        self.__PagosPim_Application8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_ViewComponent"):
                    opp_val = getattr(item, "PagosPim_ViewComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_ViewComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_ViewComponent"):
                    opp_val = getattr(item, "PagosPim_ViewComponent", None)
                    
                    setattr(item, "PagosPim_ViewComponent", self)
                    

    @property
    def PagosPim_Application(self):
        return self.__PagosPim_Application

    @PagosPim_Application.setter
    def PagosPim_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Application__PagosPim_Application", None)
        self.__PagosPim_Application = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_LogicComponent"):
                    opp_val = getattr(item, "PagosPim_LogicComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_LogicComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_LogicComponent"):
                    opp_val = getattr(item, "PagosPim_LogicComponent", None)
                    
                    setattr(item, "PagosPim_LogicComponent", self)
                    

    @property
    def PagosPim_Application4(self):
        return self.__PagosPim_Application4

    @PagosPim_Application4.setter
    def PagosPim_Application4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Application__PagosPim_Application4", None)
        self.__PagosPim_Application4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_DataLayerComponent"):
                    opp_val = getattr(item, "PagosPim_DataLayerComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_DataLayerComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_DataLayerComponent"):
                    opp_val = getattr(item, "PagosPim_DataLayerComponent", None)
                    
                    setattr(item, "PagosPim_DataLayerComponent", self)
                    

    @property
    def PagosPim_Application6(self):
        return self.__PagosPim_Application6

    @PagosPim_Application6.setter
    def PagosPim_Application6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Application__PagosPim_Application6", None)
        self.__PagosPim_Application6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_DaoComponent"):
                    opp_val = getattr(item, "PagosPim_DaoComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_DaoComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_DaoComponent"):
                    opp_val = getattr(item, "PagosPim_DaoComponent", None)
                    
                    setattr(item, "PagosPim_DaoComponent", self)
                    

    @property
    def PagosPim_Application2(self):
        return self.__PagosPim_Application2

    @PagosPim_Application2.setter
    def PagosPim_Application2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PagosPim_Application__PagosPim_Application2", None)
        self.__PagosPim_Application2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PagosPim_ServerService"):
                    opp_val = getattr(item, "PagosPim_ServerService", None)
                    
                    if opp_val == self:
                        setattr(item, "PagosPim_ServerService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PagosPim_ServerService"):
                    opp_val = getattr(item, "PagosPim_ServerService", None)
                    
                    setattr(item, "PagosPim_ServerService", self)
                    

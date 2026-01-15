from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinaryOperator(Enum):
    Equals = "Equals"
    Higher = "Higher"
    Lower = "Lower"
    And = "And"
    Add = "Add"
    Subtract = "Subtract"
    Divide = "Divide"
    Multiply = "Multiply"
    Or = "Or"
class SimpleType(Enum):
    boolean = "boolean"
    int = "int"
    double = "double"
    String = "String"
    nulltype = "nulltype"
class UnaryOperator(Enum):
    Not = "Not"
    Minus = "Minus"
class SolitaryType(Enum):
    Mandatory = "Mandatory"
    Optional = "Optional"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class featureModel_UnaryOperation(Expression):

    def __init__(self, operator: str, featureModel_UnaryOperation: "featureModel_Expression" = None):
        self.operator = operator
        self.featureModel_UnaryOperation = featureModel_UnaryOperation
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def featureModel_UnaryOperation(self):
        return self.__featureModel_UnaryOperation

    @featureModel_UnaryOperation.setter
    def featureModel_UnaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_UnaryOperation__featureModel_UnaryOperation", None)
        self.__featureModel_UnaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Expression15"):
                opp_val = getattr(old_value, "featureModel_Expression15", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Expression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Expression15"):
                opp_val = getattr(value, "featureModel_Expression15", None)
                setattr(value, "featureModel_Expression15", self)

class featureModel_BinaryOperation(Expression):

    def __init__(self, operator: str, featureModel_BinaryOperation: "featureModel_Expression" = None, featureModel_BinaryOperation12: "featureModel_Expression" = None):
        self.operator = operator
        self.featureModel_BinaryOperation = featureModel_BinaryOperation
        self.featureModel_BinaryOperation12 = featureModel_BinaryOperation12
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def featureModel_BinaryOperation12(self):
        return self.__featureModel_BinaryOperation12

    @featureModel_BinaryOperation12.setter
    def featureModel_BinaryOperation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_BinaryOperation__featureModel_BinaryOperation12", None)
        self.__featureModel_BinaryOperation12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Expression13"):
                opp_val = getattr(old_value, "featureModel_Expression13", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Expression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Expression13"):
                opp_val = getattr(value, "featureModel_Expression13", None)
                setattr(value, "featureModel_Expression13", self)

    @property
    def featureModel_BinaryOperation(self):
        return self.__featureModel_BinaryOperation

    @featureModel_BinaryOperation.setter
    def featureModel_BinaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_BinaryOperation__featureModel_BinaryOperation", None)
        self.__featureModel_BinaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Expression10"):
                opp_val = getattr(old_value, "featureModel_Expression10", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Expression10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Expression10"):
                opp_val = getattr(value, "featureModel_Expression10", None)
                setattr(value, "featureModel_Expression10", self)

class featureModel_Identifier(Expression):

    def __init__(self, name: str, featureModel_Identifier: set["featureModel_Feature"] = None):
        self.name = name
        self.featureModel_Identifier = featureModel_Identifier if featureModel_Identifier is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featureModel_Identifier(self):
        return self.__featureModel_Identifier

    @featureModel_Identifier.setter
    def featureModel_Identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Identifier__featureModel_Identifier", None)
        self.__featureModel_Identifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Feature17"):
                    opp_val = getattr(item, "featureModel_Feature17", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Feature17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Feature17"):
                    opp_val = getattr(item, "featureModel_Feature17", None)
                    
                    setattr(item, "featureModel_Feature17", self)
                    

class Constant:

    pass
class featureModel_Number(Constant):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class featureModel_NULL(Constant):

    pass
class featureModel_Constant(Expression):

    pass
class featureModel_Model:

    pass
class featureModel_Expression(ABC):

    pass
class featureModel_Group:

    def __init__(self, inclusive: bool, featureModel_Group: "featureModel_Feature" = None, featureModel_Group8: set["featureModel_GroupedFeature"] = None):
        self.inclusive = inclusive
        self.featureModel_Group = featureModel_Group
        self.featureModel_Group8 = featureModel_Group8 if featureModel_Group8 is not None else set()
        
    @property
    def inclusive(self) -> bool:
        return self.__inclusive

    @inclusive.setter
    def inclusive(self, inclusive: bool):
        self.__inclusive = inclusive

    @property
    def featureModel_Group(self):
        return self.__featureModel_Group

    @featureModel_Group.setter
    def featureModel_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Group__featureModel_Group", None)
        self.__featureModel_Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature"):
                opp_val = getattr(old_value, "featureModel_Feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature"):
                opp_val = getattr(value, "featureModel_Feature", None)
                if opp_val is None:
                    setattr(value, "featureModel_Feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModel_Group8(self):
        return self.__featureModel_Group8

    @featureModel_Group8.setter
    def featureModel_Group8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Group__featureModel_Group8", None)
        self.__featureModel_Group8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_GroupedFeature"):
                    opp_val = getattr(item, "featureModel_GroupedFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_GroupedFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_GroupedFeature"):
                    opp_val = getattr(item, "featureModel_GroupedFeature", None)
                    
                    setattr(item, "featureModel_GroupedFeature", self)
                    

class featureModel_Feature(ABC):

    def __init__(self, name: str, type: str, featureModel_Feature: set["featureModel_Group"] = None, featureModel_Feature2: set["featureModel_SolitaryFeature"] = None, featureModel_Feature4: set["featureModel_Expression"] = None, featureModel_Feature6: "featureModel_Model" = None, featureModel_Feature17: "featureModel_Identifier" = None):
        self.name = name
        self.type = type
        self.featureModel_Feature = featureModel_Feature if featureModel_Feature is not None else set()
        self.featureModel_Feature2 = featureModel_Feature2 if featureModel_Feature2 is not None else set()
        self.featureModel_Feature4 = featureModel_Feature4 if featureModel_Feature4 is not None else set()
        self.featureModel_Feature6 = featureModel_Feature6
        self.featureModel_Feature17 = featureModel_Feature17
        
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
    def featureModel_Feature2(self):
        return self.__featureModel_Feature2

    @featureModel_Feature2.setter
    def featureModel_Feature2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature2", None)
        self.__featureModel_Feature2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_SolitaryFeature"):
                    opp_val = getattr(item, "featureModel_SolitaryFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_SolitaryFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_SolitaryFeature"):
                    opp_val = getattr(item, "featureModel_SolitaryFeature", None)
                    
                    setattr(item, "featureModel_SolitaryFeature", self)
                    

    @property
    def featureModel_Feature(self):
        return self.__featureModel_Feature

    @featureModel_Feature.setter
    def featureModel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature", None)
        self.__featureModel_Feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Group"):
                    opp_val = getattr(item, "featureModel_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Group"):
                    opp_val = getattr(item, "featureModel_Group", None)
                    
                    setattr(item, "featureModel_Group", self)
                    

    @property
    def featureModel_Feature6(self):
        return self.__featureModel_Feature6

    @featureModel_Feature6.setter
    def featureModel_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature6", None)
        self.__featureModel_Feature6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Model"):
                opp_val = getattr(old_value, "featureModel_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Model"):
                opp_val = getattr(value, "featureModel_Model", None)
                if opp_val is None:
                    setattr(value, "featureModel_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModel_Feature17(self):
        return self.__featureModel_Feature17

    @featureModel_Feature17.setter
    def featureModel_Feature17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature17", None)
        self.__featureModel_Feature17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Identifier"):
                opp_val = getattr(old_value, "featureModel_Identifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Identifier"):
                opp_val = getattr(value, "featureModel_Identifier", None)
                if opp_val is None:
                    setattr(value, "featureModel_Identifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModel_Feature4(self):
        return self.__featureModel_Feature4

    @featureModel_Feature4.setter
    def featureModel_Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature4", None)
        self.__featureModel_Feature4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Expression"):
                    opp_val = getattr(item, "featureModel_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Expression"):
                    opp_val = getattr(item, "featureModel_Expression", None)
                    
                    setattr(item, "featureModel_Expression", self)
                    

class Feature:

    pass
class featureModel_GroupedFeature(Feature):

    pass
class featureModel_SolitaryFeature(Feature):

    def __init__(self, required: str, featureModel_SolitaryFeature: "featureModel_Feature" = None):
        self.required = required
        self.featureModel_SolitaryFeature = featureModel_SolitaryFeature
        
    @property
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def featureModel_SolitaryFeature(self):
        return self.__featureModel_SolitaryFeature

    @featureModel_SolitaryFeature.setter
    def featureModel_SolitaryFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_SolitaryFeature__featureModel_SolitaryFeature", None)
        self.__featureModel_SolitaryFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature2"):
                opp_val = getattr(old_value, "featureModel_Feature2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature2"):
                opp_val = getattr(value, "featureModel_Feature2", None)
                if opp_val is None:
                    setattr(value, "featureModel_Feature2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssocKind(Enum):
    Association = "Association"
    Composition = "Composition"
    Aggregation = "Aggregation"
class SimpleTypes(Enum):
    Integer = "Integer"
    Real = "Real"
    Boolean = "Boolean"
    String = "String"
class CollectionTypes(Enum):
    Set = "Set"
    Bag = "Bag"
    Sequence = "Sequence"


############################################
# Definition of Classes
############################################

class USE_Role:

    def __init__(self, lowerBound: int, name: str, ordered: bool, upperBound: int, USE_Role44: "USE_Class" = None, USE_Role: "USE_Association" = None):
        self.lowerBound = lowerBound
        self.name = name
        self.ordered = ordered
        self.upperBound = upperBound
        self.USE_Role44 = USE_Role44
        self.USE_Role = USE_Role
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def USE_Role44(self):
        return self.__USE_Role44

    @USE_Role44.setter
    def USE_Role44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Role__USE_Role44", None)
        self.__USE_Role44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Class45"):
                opp_val = getattr(old_value, "USE_Class45", None)
                if opp_val == self:
                    setattr(old_value, "USE_Class45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Class45"):
                opp_val = getattr(value, "USE_Class45", None)
                setattr(value, "USE_Class45", self)

    @property
    def USE_Role(self):
        return self.__USE_Role

    @USE_Role.setter
    def USE_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Role__USE_Role", None)
        self.__USE_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Association42"):
                opp_val = getattr(old_value, "USE_Association42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Association42"):
                opp_val = getattr(value, "USE_Association42", None)
                if opp_val is None:
                    setattr(value, "USE_Association42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class USE_Literal:

    def __init__(self, name: str, USE_Literal: "USE_Enumeration" = None):
        self.name = name
        self.USE_Literal = USE_Literal
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def USE_Literal(self):
        return self.__USE_Literal

    @USE_Literal.setter
    def USE_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Literal__USE_Literal", None)
        self.__USE_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Enumeration40"):
                opp_val = getattr(old_value, "USE_Enumeration40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Enumeration40"):
                opp_val = getattr(value, "USE_Enumeration40", None)
                if opp_val is None:
                    setattr(value, "USE_Enumeration40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class USE_Parameter:

    def __init__(self, name: str, USE_Parameter31: "USE_Type" = None, USE_Parameter: "USE_Operation" = None):
        self.name = name
        self.USE_Parameter31 = USE_Parameter31
        self.USE_Parameter = USE_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def USE_Parameter31(self):
        return self.__USE_Parameter31

    @USE_Parameter31.setter
    def USE_Parameter31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Parameter__USE_Parameter31", None)
        self.__USE_Parameter31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Type32"):
                opp_val = getattr(old_value, "USE_Type32", None)
                if opp_val == self:
                    setattr(old_value, "USE_Type32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Type32"):
                opp_val = getattr(value, "USE_Type32", None)
                setattr(value, "USE_Type32", self)

    @property
    def USE_Parameter(self):
        return self.__USE_Parameter

    @USE_Parameter.setter
    def USE_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Parameter__USE_Parameter", None)
        self.__USE_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Operation17"):
                opp_val = getattr(old_value, "USE_Operation17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Operation17"):
                opp_val = getattr(value, "USE_Operation17", None)
                if opp_val is None:
                    setattr(value, "USE_Operation17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class USE_Type(ABC):

    pass
class Type:

    pass
class USE_CollectionType(Type):

    def __init__(self, type: str, USE_CollectionType: "USE_Type" = None):
        self.type = type
        self.USE_CollectionType = USE_CollectionType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def USE_CollectionType(self):
        return self.__USE_CollectionType

    @USE_CollectionType.setter
    def USE_CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_CollectionType__USE_CollectionType", None)
        self.__USE_CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Type36"):
                opp_val = getattr(old_value, "USE_Type36", None)
                if opp_val == self:
                    setattr(old_value, "USE_Type36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Type36"):
                opp_val = getattr(value, "USE_Type36", None)
                setattr(value, "USE_Type36", self)

class USE_ReferenceType(Type):

    pass
class USE_SimpleType(Type):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class USE_EnumerationType(Type):

    pass
class USE_Class:

    def __init__(self, name: str, abstract: bool, USE_Class: "USE_Class" = None, USE_Class0: set["USE_Class"] = None, USE_Class3: set["USE_Attribute"] = None, USE_Class5: set["USE_Operation"] = None, USE_Class7: set["USE_OCLExpression"] = None, USE_Class9: "USE_Model" = None, USE_Class38: "USE_ReferenceType" = None, USE_Class45: "USE_Role" = None):
        self.name = name
        self.abstract = abstract
        self.USE_Class = USE_Class
        self.USE_Class0 = USE_Class0 if USE_Class0 is not None else set()
        self.USE_Class3 = USE_Class3 if USE_Class3 is not None else set()
        self.USE_Class5 = USE_Class5 if USE_Class5 is not None else set()
        self.USE_Class7 = USE_Class7 if USE_Class7 is not None else set()
        self.USE_Class9 = USE_Class9
        self.USE_Class38 = USE_Class38
        self.USE_Class45 = USE_Class45
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def USE_Class7(self):
        return self.__USE_Class7

    @USE_Class7.setter
    def USE_Class7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Class__USE_Class7", None)
        self.__USE_Class7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_OCLExpression"):
                    opp_val = getattr(item, "USE_OCLExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_OCLExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_OCLExpression"):
                    opp_val = getattr(item, "USE_OCLExpression", None)
                    
                    setattr(item, "USE_OCLExpression", self)
                    

    @property
    def USE_Class0(self):
        return self.__USE_Class0

    @USE_Class0.setter
    def USE_Class0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Class__USE_Class0", None)
        self.__USE_Class0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_Class"):
                    opp_val = getattr(item, "USE_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_Class"):
                    opp_val = getattr(item, "USE_Class", None)
                    
                    setattr(item, "USE_Class", self)
                    

    @property
    def USE_Class45(self):
        return self.__USE_Class45

    @USE_Class45.setter
    def USE_Class45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Class__USE_Class45", None)
        self.__USE_Class45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Role44"):
                opp_val = getattr(old_value, "USE_Role44", None)
                if opp_val == self:
                    setattr(old_value, "USE_Role44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Role44"):
                opp_val = getattr(value, "USE_Role44", None)
                setattr(value, "USE_Role44", self)

    @property
    def USE_Class9(self):
        return self.__USE_Class9

    @USE_Class9.setter
    def USE_Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Class__USE_Class9", None)
        self.__USE_Class9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Model"):
                opp_val = getattr(old_value, "USE_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Model"):
                opp_val = getattr(value, "USE_Model", None)
                if opp_val is None:
                    setattr(value, "USE_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def USE_Class5(self):
        return self.__USE_Class5

    @USE_Class5.setter
    def USE_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Class__USE_Class5", None)
        self.__USE_Class5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_Operation"):
                    opp_val = getattr(item, "USE_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_Operation"):
                    opp_val = getattr(item, "USE_Operation", None)
                    
                    setattr(item, "USE_Operation", self)
                    

    @property
    def USE_Class(self):
        return self.__USE_Class

    @USE_Class.setter
    def USE_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Class__USE_Class", None)
        self.__USE_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Class0"):
                opp_val = getattr(old_value, "USE_Class0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Class0"):
                opp_val = getattr(value, "USE_Class0", None)
                if opp_val is None:
                    setattr(value, "USE_Class0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def USE_Class38(self):
        return self.__USE_Class38

    @USE_Class38.setter
    def USE_Class38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Class__USE_Class38", None)
        self.__USE_Class38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_ReferenceType"):
                opp_val = getattr(old_value, "USE_ReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "USE_ReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_ReferenceType"):
                opp_val = getattr(value, "USE_ReferenceType", None)
                setattr(value, "USE_ReferenceType", self)

    @property
    def USE_Class3(self):
        return self.__USE_Class3

    @USE_Class3.setter
    def USE_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Class__USE_Class3", None)
        self.__USE_Class3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_Attribute"):
                    opp_val = getattr(item, "USE_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_Attribute"):
                    opp_val = getattr(item, "USE_Attribute", None)
                    
                    setattr(item, "USE_Attribute", self)
                    

class USE_Association:

    def __init__(self, name: str, kind: str, USE_Association: "USE_Model" = None, USE_Association42: set["USE_Role"] = None):
        self.name = name
        self.kind = kind
        self.USE_Association = USE_Association
        self.USE_Association42 = USE_Association42 if USE_Association42 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def USE_Association(self):
        return self.__USE_Association

    @USE_Association.setter
    def USE_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Association__USE_Association", None)
        self.__USE_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Model13"):
                opp_val = getattr(old_value, "USE_Model13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Model13"):
                opp_val = getattr(value, "USE_Model13", None)
                if opp_val is None:
                    setattr(value, "USE_Model13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def USE_Association42(self):
        return self.__USE_Association42

    @USE_Association42.setter
    def USE_Association42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Association__USE_Association42", None)
        self.__USE_Association42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_Role"):
                    opp_val = getattr(item, "USE_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_Role"):
                    opp_val = getattr(item, "USE_Role", None)
                    
                    setattr(item, "USE_Role", self)
                    

class USE_Enumeration:

    def __init__(self, name: str, USE_Enumeration: "USE_Model" = None, USE_Enumeration40: set["USE_Literal"] = None, USE_Enumeration34: "USE_EnumerationType" = None):
        self.name = name
        self.USE_Enumeration = USE_Enumeration
        self.USE_Enumeration40 = USE_Enumeration40 if USE_Enumeration40 is not None else set()
        self.USE_Enumeration34 = USE_Enumeration34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def USE_Enumeration34(self):
        return self.__USE_Enumeration34

    @USE_Enumeration34.setter
    def USE_Enumeration34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Enumeration__USE_Enumeration34", None)
        self.__USE_Enumeration34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_EnumerationType"):
                opp_val = getattr(old_value, "USE_EnumerationType", None)
                if opp_val == self:
                    setattr(old_value, "USE_EnumerationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_EnumerationType"):
                opp_val = getattr(value, "USE_EnumerationType", None)
                setattr(value, "USE_EnumerationType", self)

    @property
    def USE_Enumeration40(self):
        return self.__USE_Enumeration40

    @USE_Enumeration40.setter
    def USE_Enumeration40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Enumeration__USE_Enumeration40", None)
        self.__USE_Enumeration40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_Literal"):
                    opp_val = getattr(item, "USE_Literal", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_Literal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_Literal"):
                    opp_val = getattr(item, "USE_Literal", None)
                    
                    setattr(item, "USE_Literal", self)
                    

    @property
    def USE_Enumeration(self):
        return self.__USE_Enumeration

    @USE_Enumeration.setter
    def USE_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Enumeration__USE_Enumeration", None)
        self.__USE_Enumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Model11"):
                opp_val = getattr(old_value, "USE_Model11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Model11"):
                opp_val = getattr(value, "USE_Model11", None)
                if opp_val is None:
                    setattr(value, "USE_Model11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class USE_Model:

    def __init__(self, name: str, USE_Model: set["USE_Class"] = None, USE_Model11: set["USE_Enumeration"] = None, USE_Model13: set["USE_Association"] = None):
        self.name = name
        self.USE_Model = USE_Model if USE_Model is not None else set()
        self.USE_Model11 = USE_Model11 if USE_Model11 is not None else set()
        self.USE_Model13 = USE_Model13 if USE_Model13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def USE_Model(self):
        return self.__USE_Model

    @USE_Model.setter
    def USE_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Model__USE_Model", None)
        self.__USE_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_Class9"):
                    opp_val = getattr(item, "USE_Class9", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_Class9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_Class9"):
                    opp_val = getattr(item, "USE_Class9", None)
                    
                    setattr(item, "USE_Class9", self)
                    

    @property
    def USE_Model11(self):
        return self.__USE_Model11

    @USE_Model11.setter
    def USE_Model11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Model__USE_Model11", None)
        self.__USE_Model11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_Enumeration"):
                    opp_val = getattr(item, "USE_Enumeration", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_Enumeration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_Enumeration"):
                    opp_val = getattr(item, "USE_Enumeration", None)
                    
                    setattr(item, "USE_Enumeration", self)
                    

    @property
    def USE_Model13(self):
        return self.__USE_Model13

    @USE_Model13.setter
    def USE_Model13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Model__USE_Model13", None)
        self.__USE_Model13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_Association"):
                    opp_val = getattr(item, "USE_Association", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_Association"):
                    opp_val = getattr(item, "USE_Association", None)
                    
                    setattr(item, "USE_Association", self)
                    

class USE_OCLExpression:

    def __init__(self, expr: str, USE_OCLExpression: "USE_Class" = None, USE_OCLExpression20: "USE_Operation" = None, USE_OCLExpression26: "USE_Operation" = None, USE_OCLExpression29: "USE_Operation" = None):
        self.expr = expr
        self.USE_OCLExpression = USE_OCLExpression
        self.USE_OCLExpression20 = USE_OCLExpression20
        self.USE_OCLExpression26 = USE_OCLExpression26
        self.USE_OCLExpression29 = USE_OCLExpression29
        
    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def USE_OCLExpression(self):
        return self.__USE_OCLExpression

    @USE_OCLExpression.setter
    def USE_OCLExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_OCLExpression__USE_OCLExpression", None)
        self.__USE_OCLExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Class7"):
                opp_val = getattr(old_value, "USE_Class7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Class7"):
                opp_val = getattr(value, "USE_Class7", None)
                if opp_val is None:
                    setattr(value, "USE_Class7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def USE_OCLExpression20(self):
        return self.__USE_OCLExpression20

    @USE_OCLExpression20.setter
    def USE_OCLExpression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_OCLExpression__USE_OCLExpression20", None)
        self.__USE_OCLExpression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Operation19"):
                opp_val = getattr(old_value, "USE_Operation19", None)
                if opp_val == self:
                    setattr(old_value, "USE_Operation19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Operation19"):
                opp_val = getattr(value, "USE_Operation19", None)
                setattr(value, "USE_Operation19", self)

    @property
    def USE_OCLExpression26(self):
        return self.__USE_OCLExpression26

    @USE_OCLExpression26.setter
    def USE_OCLExpression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_OCLExpression__USE_OCLExpression26", None)
        self.__USE_OCLExpression26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Operation25"):
                opp_val = getattr(old_value, "USE_Operation25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Operation25"):
                opp_val = getattr(value, "USE_Operation25", None)
                if opp_val is None:
                    setattr(value, "USE_Operation25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def USE_OCLExpression29(self):
        return self.__USE_OCLExpression29

    @USE_OCLExpression29.setter
    def USE_OCLExpression29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_OCLExpression__USE_OCLExpression29", None)
        self.__USE_OCLExpression29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Operation28"):
                opp_val = getattr(old_value, "USE_Operation28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Operation28"):
                opp_val = getattr(value, "USE_Operation28", None)
                if opp_val is None:
                    setattr(value, "USE_Operation28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class USE_Operation:

    def __init__(self, name: str, USE_Operation: "USE_Class" = None, USE_Operation17: set["USE_Parameter"] = None, USE_Operation19: "USE_OCLExpression" = None, USE_Operation22: "USE_Type" = None, USE_Operation25: set["USE_OCLExpression"] = None, USE_Operation28: set["USE_OCLExpression"] = None):
        self.name = name
        self.USE_Operation = USE_Operation
        self.USE_Operation17 = USE_Operation17 if USE_Operation17 is not None else set()
        self.USE_Operation19 = USE_Operation19
        self.USE_Operation22 = USE_Operation22
        self.USE_Operation25 = USE_Operation25 if USE_Operation25 is not None else set()
        self.USE_Operation28 = USE_Operation28 if USE_Operation28 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def USE_Operation28(self):
        return self.__USE_Operation28

    @USE_Operation28.setter
    def USE_Operation28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Operation__USE_Operation28", None)
        self.__USE_Operation28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_OCLExpression29"):
                    opp_val = getattr(item, "USE_OCLExpression29", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_OCLExpression29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_OCLExpression29"):
                    opp_val = getattr(item, "USE_OCLExpression29", None)
                    
                    setattr(item, "USE_OCLExpression29", self)
                    

    @property
    def USE_Operation(self):
        return self.__USE_Operation

    @USE_Operation.setter
    def USE_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Operation__USE_Operation", None)
        self.__USE_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Class5"):
                opp_val = getattr(old_value, "USE_Class5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Class5"):
                opp_val = getattr(value, "USE_Class5", None)
                if opp_val is None:
                    setattr(value, "USE_Class5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def USE_Operation19(self):
        return self.__USE_Operation19

    @USE_Operation19.setter
    def USE_Operation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Operation__USE_Operation19", None)
        self.__USE_Operation19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_OCLExpression20"):
                opp_val = getattr(old_value, "USE_OCLExpression20", None)
                if opp_val == self:
                    setattr(old_value, "USE_OCLExpression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_OCLExpression20"):
                opp_val = getattr(value, "USE_OCLExpression20", None)
                setattr(value, "USE_OCLExpression20", self)

    @property
    def USE_Operation22(self):
        return self.__USE_Operation22

    @USE_Operation22.setter
    def USE_Operation22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Operation__USE_Operation22", None)
        self.__USE_Operation22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Type23"):
                opp_val = getattr(old_value, "USE_Type23", None)
                if opp_val == self:
                    setattr(old_value, "USE_Type23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Type23"):
                opp_val = getattr(value, "USE_Type23", None)
                setattr(value, "USE_Type23", self)

    @property
    def USE_Operation17(self):
        return self.__USE_Operation17

    @USE_Operation17.setter
    def USE_Operation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Operation__USE_Operation17", None)
        self.__USE_Operation17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_Parameter"):
                    opp_val = getattr(item, "USE_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_Parameter"):
                    opp_val = getattr(item, "USE_Parameter", None)
                    
                    setattr(item, "USE_Parameter", self)
                    

    @property
    def USE_Operation25(self):
        return self.__USE_Operation25

    @USE_Operation25.setter
    def USE_Operation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Operation__USE_Operation25", None)
        self.__USE_Operation25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "USE_OCLExpression26"):
                    opp_val = getattr(item, "USE_OCLExpression26", None)
                    
                    if opp_val == self:
                        setattr(item, "USE_OCLExpression26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "USE_OCLExpression26"):
                    opp_val = getattr(item, "USE_OCLExpression26", None)
                    
                    setattr(item, "USE_OCLExpression26", self)
                    

class USE_Attribute:

    def __init__(self, name: str, USE_Attribute: "USE_Class" = None, USE_Attribute15: "USE_Type" = None):
        self.name = name
        self.USE_Attribute = USE_Attribute
        self.USE_Attribute15 = USE_Attribute15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def USE_Attribute15(self):
        return self.__USE_Attribute15

    @USE_Attribute15.setter
    def USE_Attribute15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Attribute__USE_Attribute15", None)
        self.__USE_Attribute15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Type"):
                opp_val = getattr(old_value, "USE_Type", None)
                if opp_val == self:
                    setattr(old_value, "USE_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Type"):
                opp_val = getattr(value, "USE_Type", None)
                setattr(value, "USE_Type", self)

    @property
    def USE_Attribute(self):
        return self.__USE_Attribute

    @USE_Attribute.setter
    def USE_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USE_Attribute__USE_Attribute", None)
        self.__USE_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "USE_Class3"):
                opp_val = getattr(old_value, "USE_Class3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "USE_Class3"):
                opp_val = getattr(value, "USE_Class3", None)
                if opp_val is None:
                    setattr(value, "USE_Class3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class LiteralType(Enum):
    BOOL = "BOOL"
    INT = "INT"
    REAL = "REAL"
    CHAR = "CHAR"


############################################
# Definition of Classes
############################################

class NumberLiteral:

    pass
class base_IntLiteral(NumberLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class base_RealLiteral(NumberLiteral):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class Literal:

    pass
class base_NumberLiteral(Literal):

    pass
class base_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class base_BooleanLiteral(Literal):

    def __init__(self, isTrue: bool):
        self.isTrue = isTrue
        
    @property
    def isTrue(self) -> bool:
        return self.__isTrue

    @isTrue.setter
    def isTrue(self, isTrue: bool):
        self.__isTrue = isTrue

class base_LiteralArray:

    pass
class base_Literal:

    pass
class base_Import:

    def __init__(self, importedNamespace: str, importURI: str):
        self.importedNamespace = importedNamespace
        self.importURI = importURI
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

class AnnotationAttribute:

    pass
class base_EnumAnnotationAttribute(AnnotationAttribute):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class base_SimpleAnnotationAttribute(AnnotationAttribute):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class base_AnnotationAttribute:

    def __init__(self, optional: bool, name: str, base_AnnotationAttribute: "base_AnnotationType" = None):
        self.optional = optional
        self.name = name
        self.base_AnnotationAttribute = base_AnnotationAttribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def base_AnnotationAttribute(self):
        return self.__base_AnnotationAttribute

    @base_AnnotationAttribute.setter
    def base_AnnotationAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_AnnotationAttribute__base_AnnotationAttribute", None)
        self.__base_AnnotationAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_AnnotationType8"):
                opp_val = getattr(old_value, "base_AnnotationType8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_AnnotationType8"):
                opp_val = getattr(value, "base_AnnotationType8", None)
                if opp_val is None:
                    setattr(value, "base_AnnotationType8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class base_Documentation:

    def __init__(self, lines: str, base_Documentation: "base_AnnotationType" = None):
        self.lines = lines
        self.base_Documentation = base_Documentation
        
    @property
    def lines(self) -> str:
        return self.__lines

    @lines.setter
    def lines(self, lines: str):
        self.__lines = lines

    @property
    def base_Documentation(self):
        return self.__base_Documentation

    @base_Documentation.setter
    def base_Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_Documentation__base_Documentation", None)
        self.__base_Documentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_AnnotationType6"):
                opp_val = getattr(old_value, "base_AnnotationType6", None)
                if opp_val == self:
                    setattr(old_value, "base_AnnotationType6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_AnnotationType6"):
                opp_val = getattr(value, "base_AnnotationType6", None)
                setattr(value, "base_AnnotationType6", self)

class base_KeyValue:

    def __init__(self, key: str, base_KeyValue: "base_Annotation" = None, base_KeyValue4: "base_Literal" = None):
        self.key = key
        self.base_KeyValue = base_KeyValue
        self.base_KeyValue4 = base_KeyValue4
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def base_KeyValue(self):
        return self.__base_KeyValue

    @base_KeyValue.setter
    def base_KeyValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_KeyValue__base_KeyValue", None)
        self.__base_KeyValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_Annotation2"):
                opp_val = getattr(old_value, "base_Annotation2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_Annotation2"):
                opp_val = getattr(value, "base_Annotation2", None)
                if opp_val is None:
                    setattr(value, "base_Annotation2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def base_KeyValue4(self):
        return self.__base_KeyValue4

    @base_KeyValue4.setter
    def base_KeyValue4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_KeyValue__base_KeyValue4", None)
        self.__base_KeyValue4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_Literal"):
                opp_val = getattr(old_value, "base_Literal", None)
                if opp_val == self:
                    setattr(old_value, "base_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_Literal"):
                opp_val = getattr(value, "base_Literal", None)
                setattr(value, "base_Literal", self)

class base_AnnotationType:

    def __init__(self, name: str, targets: str, base_AnnotationType: "base_Annotation" = None, base_AnnotationType6: "base_Documentation" = None, base_AnnotationType8: set["base_AnnotationAttribute"] = None):
        self.name = name
        self.targets = targets
        self.base_AnnotationType = base_AnnotationType
        self.base_AnnotationType6 = base_AnnotationType6
        self.base_AnnotationType8 = base_AnnotationType8 if base_AnnotationType8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def targets(self) -> str:
        return self.__targets

    @targets.setter
    def targets(self, targets: str):
        self.__targets = targets

    @property
    def base_AnnotationType(self):
        return self.__base_AnnotationType

    @base_AnnotationType.setter
    def base_AnnotationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_AnnotationType__base_AnnotationType", None)
        self.__base_AnnotationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_Annotation"):
                opp_val = getattr(old_value, "base_Annotation", None)
                if opp_val == self:
                    setattr(old_value, "base_Annotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_Annotation"):
                opp_val = getattr(value, "base_Annotation", None)
                setattr(value, "base_Annotation", self)

    @property
    def base_AnnotationType8(self):
        return self.__base_AnnotationType8

    @base_AnnotationType8.setter
    def base_AnnotationType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_AnnotationType__base_AnnotationType8", None)
        self.__base_AnnotationType8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "base_AnnotationAttribute"):
                    opp_val = getattr(item, "base_AnnotationAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "base_AnnotationAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "base_AnnotationAttribute"):
                    opp_val = getattr(item, "base_AnnotationAttribute", None)
                    
                    setattr(item, "base_AnnotationAttribute", self)
                    

    @property
    def base_AnnotationType6(self):
        return self.__base_AnnotationType6

    @base_AnnotationType6.setter
    def base_AnnotationType6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_AnnotationType__base_AnnotationType6", None)
        self.__base_AnnotationType6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_Documentation"):
                opp_val = getattr(old_value, "base_Documentation", None)
                if opp_val == self:
                    setattr(old_value, "base_Documentation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_Documentation"):
                opp_val = getattr(value, "base_Documentation", None)
                setattr(value, "base_Documentation", self)

class base_Annotation:

    pass
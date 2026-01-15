from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Extent:

    pass
class emof_URIExtent(Extent):

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class emof_Property(MultiplicityElement, TypedElement):

    def __init__(self, default: str, isComposite: str, isDerived: str, isId: str, isReadOnly: str, emof_Property: "Class" = None, emof_Property26: "Property" = None):
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isId = isId
        self.isReadOnly = isReadOnly
        self.emof_Property = emof_Property
        self.emof_Property26 = emof_Property26
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def isId(self) -> str:
        return self.__isId

    @isId.setter
    def isId(self, isId: str):
        self.__isId = isId

    @property
    def emof_Property26(self):
        return self.__emof_Property26

    @emof_Property26.setter
    def emof_Property26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Property__emof_Property26", None)
        self.__emof_Property26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property27"):
                opp_val = getattr(old_value, "Property27", None)
                if opp_val == self:
                    setattr(old_value, "Property27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property27"):
                opp_val = getattr(value, "Property27", None)
                setattr(value, "Property27", self)

    @property
    def emof_Property(self):
        return self.__emof_Property

    @emof_Property.setter
    def emof_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Property__emof_Property", None)
        self.__emof_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class24"):
                opp_val = getattr(old_value, "Class24", None)
                if opp_val == self:
                    setattr(old_value, "Class24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class24"):
                opp_val = getattr(value, "Class24", None)
                setattr(value, "Class24", self)

class emof_Parameter(MultiplicityElement, TypedElement):

    pass
class emof_Operation(MultiplicityElement, TypedElement):

    pass
class emof_Object:

    pass
class Package:

    pass
class Parameter:

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class emof_PrimitiveType(DataType):

    pass
class emof_Enumeration(DataType):

    pass
class emof_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

class Enumeration:

    pass
class Operation:

    pass
class Tag:

    pass
class Comment:

    pass
class Object:

    pass
class emof_Extent(Object):

    pass
class emof_Element(Object):

    pass
class NamedElement:

    pass
class emof_TypedElement(NamedElement):

    pass
class emof_Type(NamedElement):

    pass
class emof_EnumerationLiteral(NamedElement):

    pass
class emof_Package(NamedElement):

    def __init__(self, uri: str, emof_Package: set["Package"] = None, emof_Package19: set["Type"] = None, NamedElement: "emof_Comment"):
        self.uri = uri
        self.emof_Package = emof_Package if emof_Package is not None else set()
        self.emof_Package19 = emof_Package19 if emof_Package19 is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def emof_Package(self):
        return self.__emof_Package

    @emof_Package.setter
    def emof_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Package__emof_Package", None)
        self.__emof_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def emof_Package19(self):
        return self.__emof_Package19

    @emof_Package19.setter
    def emof_Package19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Package__emof_Package19", None)
        self.__emof_Package19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type20"):
                    opp_val = getattr(item, "Type20", None)
                    
                    if opp_val == self:
                        setattr(item, "Type20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type20"):
                    opp_val = getattr(item, "Type20", None)
                    
                    setattr(item, "Type20", self)
                    

class Element:

    pass
class emof_Tag(Element):

    def __init__(self, value: str, name: str, emof_Tag: set["Element"] = None, Element: "emof_Tag"):
        self.value = value
        self.name = name
        self.emof_Tag = emof_Tag if emof_Tag is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emof_Tag(self):
        return self.__emof_Tag

    @emof_Tag.setter
    def emof_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Tag__emof_Tag", None)
        self.__emof_Tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

class emof_NamedElement(Element):

    def __init__(self, name: str, Element: "emof_Tag"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class emof_Comment(Element):

    pass
class Class:

    pass
class Property:

    pass
class Type:

    pass
class emof_DataType(Type):

    pass
class emof_Class(Type):

    def __init__(self, isAbstract: str, emof_Class4: set["Class"] = None, emof_Class: set["Property"] = None, emof_Class2: set["Operation"] = None, Type32: "emof_TypedElement", Type20: "emof_Package", Type: "emof_Operation"):
        self.isAbstract = isAbstract
        self.emof_Class4 = emof_Class4 if emof_Class4 is not None else set()
        self.emof_Class = emof_Class if emof_Class is not None else set()
        self.emof_Class2 = emof_Class2 if emof_Class2 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def emof_Class4(self):
        return self.__emof_Class4

    @emof_Class4.setter
    def emof_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__emof_Class4", None)
        self.__emof_Class4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    if opp_val == self:
                        setattr(item, "Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    setattr(item, "Class", self)
                    

    @property
    def emof_Class2(self):
        return self.__emof_Class2

    @emof_Class2.setter
    def emof_Class2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__emof_Class2", None)
        self.__emof_Class2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def emof_Class(self):
        return self.__emof_Class

    @emof_Class.setter
    def emof_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__emof_Class", None)
        self.__emof_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

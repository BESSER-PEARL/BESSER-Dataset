from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Extent:

    pass
class emof_URIExtent(Extent):

    pass
class Package:

    pass
class Parameter:

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class emof_Parameter(TypedElement, MultiplicityElement):

    pass
class emof_Property(TypedElement, MultiplicityElement):

    def __init__(self, isDerived: str, isId: str, isReadOnly: str, default: str, isComposite: str, emof_Property26: "Property" = None, emof_Property: "Class" = None):
        self.isDerived = isDerived
        self.isId = isId
        self.isReadOnly = isReadOnly
        self.default = default
        self.isComposite = isComposite
        self.emof_Property26 = emof_Property26
        self.emof_Property = emof_Property
        
        pass
    @property
    def isId(self):
        return self.__isId

    @isId.setter
    def isId(self, isId: str):
        self.__isId = isId


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived


    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


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

class emof_Operation(TypedElement, MultiplicityElement):

    pass
class emof_Object:

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class emof_PrimitiveType(DataType):

    pass
class emof_Enumeration(DataType):

    pass
class Tag:

    pass
class Comment:

    pass
class Object:

    pass
class emof_Element(Object):

    pass
class NamedElement:

    pass
class emof_TypedElement(NamedElement):

    pass
class emof_EnumerationLiteral(NamedElement):

    pass
class emof_Package(NamedElement):

    def __init__(self, uri: str, emof_Package: set["Package"] = None, emof_Package19: set["Type"] = None, NamedElement: "emof_Comment" = None):
        self.uri = uri
        self.emof_Package = emof_Package if emof_Package is not None else set()
        self.emof_Package19 = emof_Package19 if emof_Package19 is not None else set()
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


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
                    

class emof_Type(NamedElement):

    pass
class Element:

    pass
class emof_NamedElement(Element):

    def __init__(self, name: str, Element: "emof_Tag" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class emof_Tag(Element):

    def __init__(self, name: str, value: str, emof_Tag: set["Element"] = None, Element: "emof_Tag" = None):
        self.name = name
        self.value = value
        self.emof_Tag = emof_Tag if emof_Tag is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


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
                    

class emof_Comment(Element):

    pass
class Class:

    pass
class Operation:

    pass
class Property:

    pass
class Type:

    pass
class emof_DataType(Type):

    pass
class emof_Class(Type):

    def __init__(self, isAbstract: str, emof_Class: set["Property"] = None, emof_Class2: set["Operation"] = None, emof_Class4: set["Class"] = None, Type32: "emof_TypedElement" = None, Type: "emof_Operation" = None, Type20: "emof_Package" = None):
        self.isAbstract = isAbstract
        self.emof_Class = emof_Class if emof_Class is not None else set()
        self.emof_Class2 = emof_Class2 if emof_Class2 is not None else set()
        self.emof_Class4 = emof_Class4 if emof_Class4 is not None else set()
        
        pass
    @property
    def isAbstract(self):
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
                    

class emof_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
        pass
    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered


    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


class emof_Extent(Object):

    pass
class Enumeration:

    pass
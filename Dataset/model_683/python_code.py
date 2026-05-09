from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Extent:

    pass
class EMOF_URIExtent(Extent):

    def __init__(self):
        
        pass
    def element(self, EMOF_uri) :
        # TODO: Implement element method
        pass

    def uri(self, EMOF_element) :
        # TODO: Implement uri method
        pass

    def contextURI(self) :
        # TODO: Implement contextURI method
        pass

class ReflectiveCollection:

    pass
class EMOF_ReflectiveSequence(ReflectiveCollection):

    def __init__(self):
        
        pass
    def set(self, EMOF_object, EMOF_index) :
        # TODO: Implement set method
        pass

    def remove(self, EMOF_index) :
        # TODO: Implement remove method
        pass

    def add(self, EMOF_index, EMOF_object):
        # TODO: Implement add method
        pass

    def get(self, EMOF_index) :
        # TODO: Implement get method
        pass

class Parameter:

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class EMOF_Parameter(MultiplicityElement, TypedElement):

    pass
class EMOF_Operation(MultiplicityElement, TypedElement):

    pass
class EMOF_Object:

    pass
class Enumeration:

    pass
class EMOF_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
        pass
    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered


class Package:

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class EMOF_PrimitiveType(DataType):

    pass
class EMOF_Enumeration(DataType):

    pass
class Comment:

    pass
class EMOF_Property(MultiplicityElement, TypedElement):

    def __init__(self, default: str, isComposite: str, isDerived: str, isID: str, isReadOnly: str, EMOF_Property: "Class" = None, EMOF_Property29: "Property" = None):
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.isReadOnly = isReadOnly
        self.EMOF_Property = EMOF_Property
        self.EMOF_Property29 = EMOF_Property29
        
        pass
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
    def isID(self):
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


    @property
    def EMOF_Property(self):
        return self.__EMOF_Property

    @EMOF_Property.setter
    def EMOF_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Property__EMOF_Property", None)
        self.__EMOF_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class27"):
                opp_val = getattr(old_value, "Class27", None)
                if opp_val == self:
                    setattr(old_value, "Class27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class27"):
                opp_val = getattr(value, "Class27", None)
                setattr(value, "Class27", self)

    @property
    def EMOF_Property29(self):
        return self.__EMOF_Property29

    @EMOF_Property29.setter
    def EMOF_Property29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Property__EMOF_Property29", None)
        self.__EMOF_Property29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property30"):
                opp_val = getattr(old_value, "Property30", None)
                if opp_val == self:
                    setattr(old_value, "Property30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property30"):
                opp_val = getattr(value, "Property30", None)
                setattr(value, "Property30", self)

class Object:

    pass
class EMOF_Extent(Object):

    def __init__(self):
        
        pass
    def elements(self) :
        # TODO: Implement elements method
        pass

    def useContainment(self) :
        # TODO: Implement useContainment method
        pass

class EMOF_ReflectiveCollection(Object):

    def __init__(self):
        
        pass
    def size(self) :
        # TODO: Implement size method
        pass

    def addAll(self, EMOF_objects) :
        # TODO: Implement addAll method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def add(self, EMOF_object) :
        # TODO: Implement add method
        pass

    def remove(self, EMOF_object) :
        # TODO: Implement remove method
        pass

class EMOF_Element(Object):

    def __init__(self, EMOF_Element: set["Comment"] = None):
        self.EMOF_Element = EMOF_Element if EMOF_Element is not None else set()
        
        pass
    @property
    def EMOF_Element(self):
        return self.__EMOF_Element

    @EMOF_Element.setter
    def EMOF_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Element__EMOF_Element", None)
        self.__EMOF_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

    def equals(self, EMOF_object) :
        # TODO: Implement equals method
        pass

    def unset(self, EMOF_property):
        # TODO: Implement unset method
        pass

    def set(self, EMOF_object, EMOF_property):
        # TODO: Implement set method
        pass

    def isSet(self, EMOF_property) :
        # TODO: Implement isSet method
        pass

    def container(self) :
        # TODO: Implement container method
        pass

    def getMetaClass(self) :
        # TODO: Implement getMetaClass method
        pass

    def get(self, EMOF_property) :
        # TODO: Implement get method
        pass

class Property:

    pass
class Type:

    pass
class EMOF_DataType(Type):

    pass
class EMOF_Class(Type):

    def __init__(self, isAbstract: str, EMOF_Class2: set["Operation"] = None, EMOF_Class4: set["Class"] = None, EMOF_Class: set["Property"] = None, Type: "EMOF_Operation" = None, Type35: "EMOF_TypedElement" = None, Type23: "EMOF_Package" = None):
        self.isAbstract = isAbstract
        self.EMOF_Class2 = EMOF_Class2 if EMOF_Class2 is not None else set()
        self.EMOF_Class4 = EMOF_Class4 if EMOF_Class4 is not None else set()
        self.EMOF_Class = EMOF_Class if EMOF_Class is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def EMOF_Class4(self):
        return self.__EMOF_Class4

    @EMOF_Class4.setter
    def EMOF_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Class__EMOF_Class4", None)
        self.__EMOF_Class4 = value if value is not None else set()
        
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
    def EMOF_Class2(self):
        return self.__EMOF_Class2

    @EMOF_Class2.setter
    def EMOF_Class2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Class__EMOF_Class2", None)
        self.__EMOF_Class2 = value if value is not None else set()
        
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
    def EMOF_Class(self):
        return self.__EMOF_Class

    @EMOF_Class.setter
    def EMOF_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Class__EMOF_Class", None)
        self.__EMOF_Class = value if value is not None else set()
        
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
                    

class NamedElement:

    pass
class EMOF_EnumerationLiteral(NamedElement):

    pass
class EMOF_Type(NamedElement):

    def __init__(self, EMOF_Type: "Package" = None, NamedElement: "EMOF_Comment" = None):
        self.EMOF_Type = EMOF_Type
        
        pass
    @property
    def EMOF_Type(self):
        return self.__EMOF_Type

    @EMOF_Type.setter
    def EMOF_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Type__EMOF_Type", None)
        self.__EMOF_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package33"):
                opp_val = getattr(old_value, "Package33", None)
                if opp_val == self:
                    setattr(old_value, "Package33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package33"):
                opp_val = getattr(value, "Package33", None)
                setattr(value, "Package33", self)

    def isInstance(self, EMOF_object) :
        # TODO: Implement isInstance method
        pass

class EMOF_Package(NamedElement):

    def __init__(self, uri: str, EMOF_Package: set["Package"] = None, EMOF_Package19: "Package" = None, EMOF_Package22: set["Type"] = None, NamedElement: "EMOF_Comment" = None):
        self.uri = uri
        self.EMOF_Package = EMOF_Package if EMOF_Package is not None else set()
        self.EMOF_Package19 = EMOF_Package19
        self.EMOF_Package22 = EMOF_Package22 if EMOF_Package22 is not None else set()
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def EMOF_Package(self):
        return self.__EMOF_Package

    @EMOF_Package.setter
    def EMOF_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__EMOF_Package", None)
        self.__EMOF_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package17"):
                    opp_val = getattr(item, "Package17", None)
                    
                    if opp_val == self:
                        setattr(item, "Package17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package17"):
                    opp_val = getattr(item, "Package17", None)
                    
                    setattr(item, "Package17", self)
                    

    @property
    def EMOF_Package22(self):
        return self.__EMOF_Package22

    @EMOF_Package22.setter
    def EMOF_Package22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__EMOF_Package22", None)
        self.__EMOF_Package22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type23"):
                    opp_val = getattr(item, "Type23", None)
                    
                    if opp_val == self:
                        setattr(item, "Type23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type23"):
                    opp_val = getattr(item, "Type23", None)
                    
                    setattr(item, "Type23", self)
                    

    @property
    def EMOF_Package19(self):
        return self.__EMOF_Package19

    @EMOF_Package19.setter
    def EMOF_Package19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__EMOF_Package19", None)
        self.__EMOF_Package19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package20"):
                opp_val = getattr(old_value, "Package20", None)
                if opp_val == self:
                    setattr(old_value, "Package20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package20"):
                opp_val = getattr(value, "Package20", None)
                setattr(value, "Package20", self)

class EMOF_TypedElement(NamedElement):

    pass
class Element:

    pass
class EMOF_Tag(Element):

    def __init__(self, value: str, name: str, EMOF_Tag: set["Element"] = None, Element: "EMOF_Tag" = None):
        self.value = value
        self.name = name
        self.EMOF_Tag = EMOF_Tag if EMOF_Tag is not None else set()
        
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
    def EMOF_Tag(self):
        return self.__EMOF_Tag

    @EMOF_Tag.setter
    def EMOF_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Tag__EMOF_Tag", None)
        self.__EMOF_Tag = value if value is not None else set()
        
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
                    

class EMOF_Factory(Element):

    def __init__(self, EMOF_Factory: "Package" = None, Element: "EMOF_Tag" = None):
        self.EMOF_Factory = EMOF_Factory
        
        pass
    @property
    def EMOF_Factory(self):
        return self.__EMOF_Factory

    @EMOF_Factory.setter
    def EMOF_Factory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Factory__EMOF_Factory", None)
        self.__EMOF_Factory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package"):
                opp_val = getattr(old_value, "Package", None)
                if opp_val == self:
                    setattr(old_value, "Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package"):
                opp_val = getattr(value, "Package", None)
                setattr(value, "Package", self)

    def createFromString(self, EMOF_string, EMOF_dataType) :
        # TODO: Implement createFromString method
        pass

    def create(self, EMOF_metaClass) :
        # TODO: Implement create method
        pass

    def convertToString(self, EMOF_object, EMOF_dataType) :
        # TODO: Implement convertToString method
        pass

class EMOF_NamedElement(Element):

    def __init__(self, name: str, Element: "EMOF_Tag" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class EMOF_Comment(Element):

    def __init__(self, body: str, EMOF_Comment: set["NamedElement"] = None, Element: "EMOF_Tag" = None):
        self.body = body
        self.EMOF_Comment = EMOF_Comment if EMOF_Comment is not None else set()
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def EMOF_Comment(self):
        return self.__EMOF_Comment

    @EMOF_Comment.setter
    def EMOF_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Comment__EMOF_Comment", None)
        self.__EMOF_Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedElement"):
                    opp_val = getattr(item, "NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedElement"):
                    opp_val = getattr(item, "NamedElement", None)
                    
                    setattr(item, "NamedElement", self)
                    

class Class:

    pass
class Operation:

    pass
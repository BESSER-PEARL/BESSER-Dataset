from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Extent:

    pass
class emof_URIExtent(Extent):

    pass
class NamedElement:

    pass
class emof_TypedElement(NamedElement):

    pass
class emof_Package(NamedElement):

    def __init__(self, uri: str, package: set["emof_Type"] = None, emof_Package: "emof_Package" = None, emof_Package13: set["emof_Package"] = None, Package: "emof_Type" = None):
        self.uri = uri
        self.package = package if package is not None else set()
        self.emof_Package = emof_Package
        self.emof_Package13 = emof_Package13 if emof_Package13 is not None else set()
        self.Package = Package
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedType"):
                opp_val = getattr(old_value, "ownedType", None)
                if opp_val == self:
                    setattr(old_value, "ownedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedType"):
                opp_val = getattr(value, "ownedType", None)
                setattr(value, "ownedType", self)

    @property
    def emof_Package(self):
        return self.__emof_Package

    @emof_Package.setter
    def emof_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Package__emof_Package", None)
        self.__emof_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emof_Package13"):
                opp_val = getattr(old_value, "emof_Package13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emof_Package13"):
                opp_val = getattr(value, "emof_Package13", None)
                if opp_val is None:
                    setattr(value, "emof_Package13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def emof_Package13(self):
        return self.__emof_Package13

    @emof_Package13.setter
    def emof_Package13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Package__emof_Package13", None)
        self.__emof_Package13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emof_Package"):
                    opp_val = getattr(item, "emof_Package", None)
                    
                    if opp_val == self:
                        setattr(item, "emof_Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emof_Package"):
                    opp_val = getattr(item, "emof_Package", None)
                    
                    setattr(item, "emof_Package", self)
                    

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Package__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    if opp_val == self:
                        setattr(item, "Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    setattr(item, "Type", self)
                    

class emof_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
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

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

class emof_Type(NamedElement):

    pass
class emof_EnumerationLiteral(NamedElement):

    pass
class DataType:

    pass
class emof_PrimitiveType(DataType):

    pass
class emof_Enumeration(DataType):

    pass
class Element:

    pass
class emof_Comment(Element):

    pass
class emof_Tag(Element):

    def __init__(self, value: str, name: str, Tag: "emof_Element" = None, tag: set["emof_Element"] = None):
        self.value = value
        self.name = name
        self.Tag = Tag
        self.tag = tag if tag is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Tag__tag", None)
        self.__tag = value if value is not None else set()
        
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
                    

    @property
    def Tag(self):
        return self.__Tag

    @Tag.setter
    def Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Tag__Tag", None)
        self.__Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "element"):
                opp_val = getattr(old_value, "element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "element"):
                opp_val = getattr(value, "element", None)
                if opp_val is None:
                    setattr(value, "element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypedElement:

    pass
class MultiplicityElement:

    pass
class emof_Parameter(MultiplicityElement, TypedElement):

    pass
class emof_Object:

    pass
class emof_NamedElement(Element):

    def __init__(self, name: str, emof_NamedElement: "emof_Comment" = None):
        self.name = name
        self.emof_NamedElement = emof_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emof_NamedElement(self):
        return self.__emof_NamedElement

    @emof_NamedElement.setter
    def emof_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_NamedElement__emof_NamedElement", None)
        self.__emof_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emof_Comment26"):
                opp_val = getattr(old_value, "emof_Comment26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emof_Comment26"):
                opp_val = getattr(value, "emof_Comment26", None)
                if opp_val is None:
                    setattr(value, "emof_Comment26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emof_Operation(TypedElement, MultiplicityElement):

    pass
class emof_Property(MultiplicityElement, TypedElement):

    def __init__(self, isDerived: str, isComposite: str, isId: str, default: str, isReadOnly: str, Property: "emof_Class" = None, ownedAttribute: "emof_Class" = None, emof_Property: "emof_Property" = None, emof_Property21: "emof_Property" = None):
        self.isDerived = isDerived
        self.isComposite = isComposite
        self.isId = isId
        self.default = default
        self.isReadOnly = isReadOnly
        self.Property = Property
        self.ownedAttribute = ownedAttribute
        self.emof_Property = emof_Property
        self.emof_Property21 = emof_Property21
        
    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isId(self) -> str:
        return self.__isId

    @isId.setter
    def isId(self, isId: str):
        self.__isId = isId

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class"):
                opp_val = getattr(old_value, "class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class"):
                opp_val = getattr(value, "class", None)
                if opp_val is None:
                    setattr(value, "class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def emof_Property21(self):
        return self.__emof_Property21

    @emof_Property21.setter
    def emof_Property21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Property__emof_Property21", None)
        self.__emof_Property21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emof_Property"):
                opp_val = getattr(old_value, "emof_Property", None)
                if opp_val == self:
                    setattr(old_value, "emof_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emof_Property"):
                opp_val = getattr(value, "emof_Property", None)
                setattr(value, "emof_Property", self)

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
            if hasattr(old_value, "emof_Property21"):
                opp_val = getattr(old_value, "emof_Property21", None)
                if opp_val == self:
                    setattr(old_value, "emof_Property21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emof_Property21"):
                opp_val = getattr(value, "emof_Property21", None)
                setattr(value, "emof_Property21", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class20"):
                opp_val = getattr(old_value, "Class20", None)
                if opp_val == self:
                    setattr(old_value, "Class20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class20"):
                opp_val = getattr(value, "Class20", None)
                setattr(value, "Class20", self)

class Type:

    pass
class emof_Class(Type):

    def __init__(self, isAbstract: str, class2: set["emof_Operation"] = None, emof_Class: "emof_Class" = None, emof_Class3: set["emof_Class"] = None, class: set["emof_Property"] = None, Class: "emof_Operation" = None, Class20: "emof_Property" = None):
        self.isAbstract = isAbstract
        self.class2 = class2 if class2 is not None else set()
        self.emof_Class = emof_Class
        self.emof_Class3 = emof_Class3 if emof_Class3 is not None else set()
        self.class = class if class is not None else set()
        self.Class = Class
        self.Class20 = Class20
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedOperation"):
                opp_val = getattr(old_value, "ownedOperation", None)
                if opp_val == self:
                    setattr(old_value, "ownedOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedOperation"):
                opp_val = getattr(value, "ownedOperation", None)
                setattr(value, "ownedOperation", self)

    @property
    def emof_Class3(self):
        return self.__emof_Class3

    @emof_Class3.setter
    def emof_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__emof_Class3", None)
        self.__emof_Class3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emof_Class"):
                    opp_val = getattr(item, "emof_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "emof_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emof_Class"):
                    opp_val = getattr(item, "emof_Class", None)
                    
                    setattr(item, "emof_Class", self)
                    

    @property
    def Class20(self):
        return self.__Class20

    @Class20.setter
    def Class20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__Class20", None)
        self.__Class20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedAttribute"):
                opp_val = getattr(old_value, "ownedAttribute", None)
                if opp_val == self:
                    setattr(old_value, "ownedAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedAttribute"):
                opp_val = getattr(value, "ownedAttribute", None)
                setattr(value, "ownedAttribute", self)

    @property
    def emof_Class(self):
        return self.__emof_Class

    @emof_Class.setter
    def emof_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__emof_Class", None)
        self.__emof_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emof_Class3"):
                opp_val = getattr(old_value, "emof_Class3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emof_Class3"):
                opp_val = getattr(value, "emof_Class3", None)
                if opp_val is None:
                    setattr(value, "emof_Class3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def class2(self):
        return self.__class2

    @class2.setter
    def class2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__class2", None)
        self.__class2 = value if value is not None else set()
        
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
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__class", None)
        self.__class = value if value is not None else set()
        
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
                    

class Object:

    pass
class emof_Extent(Object):

    pass
class emof_Element(Object):

    pass
class emof_DataType(Type):

    pass
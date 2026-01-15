from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class KragsteinPackage_Link:

    pass
class KragsteinPackage_Parameter:

    def __init__(self, name: str, type: str, value: str, KragsteinPackage_Parameter: "KragsteinPackage_Method" = None):
        self.name = name
        self.type = type
        self.value = value
        self.KragsteinPackage_Parameter = KragsteinPackage_Parameter
        
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
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def KragsteinPackage_Parameter(self):
        return self.__KragsteinPackage_Parameter

    @KragsteinPackage_Parameter.setter
    def KragsteinPackage_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Parameter__KragsteinPackage_Parameter", None)
        self.__KragsteinPackage_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KragsteinPackage_Method15"):
                opp_val = getattr(old_value, "KragsteinPackage_Method15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KragsteinPackage_Method15"):
                opp_val = getattr(value, "KragsteinPackage_Method15", None)
                if opp_val is None:
                    setattr(value, "KragsteinPackage_Method15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class KragsteinPackage_ImportedClass:

    def __init__(self, name: str, path: str, isInternal: bool, KragsteinPackage_ImportedClass: "KragsteinPackage_Class" = None):
        self.name = name
        self.path = path
        self.isInternal = isInternal
        self.KragsteinPackage_ImportedClass = KragsteinPackage_ImportedClass
        
    @property
    def isInternal(self) -> bool:
        return self.__isInternal

    @isInternal.setter
    def isInternal(self, isInternal: bool):
        self.__isInternal = isInternal

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def KragsteinPackage_ImportedClass(self):
        return self.__KragsteinPackage_ImportedClass

    @KragsteinPackage_ImportedClass.setter
    def KragsteinPackage_ImportedClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_ImportedClass__KragsteinPackage_ImportedClass", None)
        self.__KragsteinPackage_ImportedClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KragsteinPackage_Class13"):
                opp_val = getattr(old_value, "KragsteinPackage_Class13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KragsteinPackage_Class13"):
                opp_val = getattr(value, "KragsteinPackage_Class13", None)
                if opp_val is None:
                    setattr(value, "KragsteinPackage_Class13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class KragsteinPackage_Method:

    def __init__(self, name: str, type: str, visibility: str, isConst: bool, isVirtual: bool, isStatic: bool, KragsteinPackage_Method: "KragsteinPackage_Class" = None, KragsteinPackage_Method15: set["KragsteinPackage_Parameter"] = None):
        self.name = name
        self.type = type
        self.visibility = visibility
        self.isConst = isConst
        self.isVirtual = isVirtual
        self.isStatic = isStatic
        self.KragsteinPackage_Method = KragsteinPackage_Method
        self.KragsteinPackage_Method15 = KragsteinPackage_Method15 if KragsteinPackage_Method15 is not None else set()
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def isConst(self) -> bool:
        return self.__isConst

    @isConst.setter
    def isConst(self, isConst: bool):
        self.__isConst = isConst

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isVirtual(self) -> bool:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: bool):
        self.__isVirtual = isVirtual

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def KragsteinPackage_Method(self):
        return self.__KragsteinPackage_Method

    @KragsteinPackage_Method.setter
    def KragsteinPackage_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Method__KragsteinPackage_Method", None)
        self.__KragsteinPackage_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KragsteinPackage_Class8"):
                opp_val = getattr(old_value, "KragsteinPackage_Class8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KragsteinPackage_Class8"):
                opp_val = getattr(value, "KragsteinPackage_Class8", None)
                if opp_val is None:
                    setattr(value, "KragsteinPackage_Class8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def KragsteinPackage_Method15(self):
        return self.__KragsteinPackage_Method15

    @KragsteinPackage_Method15.setter
    def KragsteinPackage_Method15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Method__KragsteinPackage_Method15", None)
        self.__KragsteinPackage_Method15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "KragsteinPackage_Parameter"):
                    opp_val = getattr(item, "KragsteinPackage_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "KragsteinPackage_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "KragsteinPackage_Parameter"):
                    opp_val = getattr(item, "KragsteinPackage_Parameter", None)
                    
                    setattr(item, "KragsteinPackage_Parameter", self)
                    

class KragsteinPackage_Attribute:

    def __init__(self, name: str, type: str, visibility: str, isConst: bool, isStatic: bool, value: str, KragsteinPackage_Attribute: "KragsteinPackage_Class" = None):
        self.name = name
        self.type = type
        self.visibility = visibility
        self.isConst = isConst
        self.isStatic = isStatic
        self.value = value
        self.KragsteinPackage_Attribute = KragsteinPackage_Attribute
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

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
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def isConst(self) -> bool:
        return self.__isConst

    @isConst.setter
    def isConst(self, isConst: bool):
        self.__isConst = isConst

    @property
    def KragsteinPackage_Attribute(self):
        return self.__KragsteinPackage_Attribute

    @KragsteinPackage_Attribute.setter
    def KragsteinPackage_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Attribute__KragsteinPackage_Attribute", None)
        self.__KragsteinPackage_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KragsteinPackage_Class6"):
                opp_val = getattr(old_value, "KragsteinPackage_Class6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KragsteinPackage_Class6"):
                opp_val = getattr(value, "KragsteinPackage_Class6", None)
                if opp_val is None:
                    setattr(value, "KragsteinPackage_Class6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Unit:

    pass
class KragsteinPackage_Note(Unit):

    def __init__(self, name: str, text: str):
        self.name = name
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Relationship:

    pass
class KragsteinPackage_Realization(Relationship):

    pass
class KragsteinPackage_Composition(Relationship):

    pass
class KragsteinPackage_Association(Relationship):

    pass
class KragsteinPackage_Aggregation(Relationship):

    pass
class KragsteinPackage_Generalization(Relationship):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class KragsteinPackage_Class(Unit):

    def __init__(self, name: str, visibility: str, isSingletone: bool, isInterface: bool, superClass: str, supplierElement: str, KragsteinPackage_Class: "KragsteinPackage_Relationship" = None, KragsteinPackage_Class4: "KragsteinPackage_Relationship" = None, KragsteinPackage_Class6: set["KragsteinPackage_Attribute"] = None, KragsteinPackage_Class8: set["KragsteinPackage_Method"] = None, KragsteinPackage_Class10: set["KragsteinPackage_Relationship"] = None, KragsteinPackage_Class13: set["KragsteinPackage_ImportedClass"] = None):
        self.name = name
        self.visibility = visibility
        self.isSingletone = isSingletone
        self.isInterface = isInterface
        self.superClass = superClass
        self.supplierElement = supplierElement
        self.KragsteinPackage_Class = KragsteinPackage_Class
        self.KragsteinPackage_Class4 = KragsteinPackage_Class4
        self.KragsteinPackage_Class6 = KragsteinPackage_Class6 if KragsteinPackage_Class6 is not None else set()
        self.KragsteinPackage_Class8 = KragsteinPackage_Class8 if KragsteinPackage_Class8 is not None else set()
        self.KragsteinPackage_Class10 = KragsteinPackage_Class10 if KragsteinPackage_Class10 is not None else set()
        self.KragsteinPackage_Class13 = KragsteinPackage_Class13 if KragsteinPackage_Class13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def supplierElement(self) -> str:
        return self.__supplierElement

    @supplierElement.setter
    def supplierElement(self, supplierElement: str):
        self.__supplierElement = supplierElement

    @property
    def isSingletone(self) -> bool:
        return self.__isSingletone

    @isSingletone.setter
    def isSingletone(self, isSingletone: bool):
        self.__isSingletone = isSingletone

    @property
    def superClass(self) -> str:
        return self.__superClass

    @superClass.setter
    def superClass(self, superClass: str):
        self.__superClass = superClass

    @property
    def isInterface(self) -> bool:
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: bool):
        self.__isInterface = isInterface

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def KragsteinPackage_Class6(self):
        return self.__KragsteinPackage_Class6

    @KragsteinPackage_Class6.setter
    def KragsteinPackage_Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Class__KragsteinPackage_Class6", None)
        self.__KragsteinPackage_Class6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "KragsteinPackage_Attribute"):
                    opp_val = getattr(item, "KragsteinPackage_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "KragsteinPackage_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "KragsteinPackage_Attribute"):
                    opp_val = getattr(item, "KragsteinPackage_Attribute", None)
                    
                    setattr(item, "KragsteinPackage_Attribute", self)
                    

    @property
    def KragsteinPackage_Class(self):
        return self.__KragsteinPackage_Class

    @KragsteinPackage_Class.setter
    def KragsteinPackage_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Class__KragsteinPackage_Class", None)
        self.__KragsteinPackage_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KragsteinPackage_Relationship"):
                opp_val = getattr(old_value, "KragsteinPackage_Relationship", None)
                if opp_val == self:
                    setattr(old_value, "KragsteinPackage_Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KragsteinPackage_Relationship"):
                opp_val = getattr(value, "KragsteinPackage_Relationship", None)
                setattr(value, "KragsteinPackage_Relationship", self)

    @property
    def KragsteinPackage_Class4(self):
        return self.__KragsteinPackage_Class4

    @KragsteinPackage_Class4.setter
    def KragsteinPackage_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Class__KragsteinPackage_Class4", None)
        self.__KragsteinPackage_Class4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KragsteinPackage_Relationship3"):
                opp_val = getattr(old_value, "KragsteinPackage_Relationship3", None)
                if opp_val == self:
                    setattr(old_value, "KragsteinPackage_Relationship3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KragsteinPackage_Relationship3"):
                opp_val = getattr(value, "KragsteinPackage_Relationship3", None)
                setattr(value, "KragsteinPackage_Relationship3", self)

    @property
    def KragsteinPackage_Class10(self):
        return self.__KragsteinPackage_Class10

    @KragsteinPackage_Class10.setter
    def KragsteinPackage_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Class__KragsteinPackage_Class10", None)
        self.__KragsteinPackage_Class10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "KragsteinPackage_Relationship11"):
                    opp_val = getattr(item, "KragsteinPackage_Relationship11", None)
                    
                    if opp_val == self:
                        setattr(item, "KragsteinPackage_Relationship11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "KragsteinPackage_Relationship11"):
                    opp_val = getattr(item, "KragsteinPackage_Relationship11", None)
                    
                    setattr(item, "KragsteinPackage_Relationship11", self)
                    

    @property
    def KragsteinPackage_Class8(self):
        return self.__KragsteinPackage_Class8

    @KragsteinPackage_Class8.setter
    def KragsteinPackage_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Class__KragsteinPackage_Class8", None)
        self.__KragsteinPackage_Class8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "KragsteinPackage_Method"):
                    opp_val = getattr(item, "KragsteinPackage_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "KragsteinPackage_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "KragsteinPackage_Method"):
                    opp_val = getattr(item, "KragsteinPackage_Method", None)
                    
                    setattr(item, "KragsteinPackage_Method", self)
                    

    @property
    def KragsteinPackage_Class13(self):
        return self.__KragsteinPackage_Class13

    @KragsteinPackage_Class13.setter
    def KragsteinPackage_Class13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Class__KragsteinPackage_Class13", None)
        self.__KragsteinPackage_Class13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "KragsteinPackage_ImportedClass"):
                    opp_val = getattr(item, "KragsteinPackage_ImportedClass", None)
                    
                    if opp_val == self:
                        setattr(item, "KragsteinPackage_ImportedClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "KragsteinPackage_ImportedClass"):
                    opp_val = getattr(item, "KragsteinPackage_ImportedClass", None)
                    
                    setattr(item, "KragsteinPackage_ImportedClass", self)
                    

class KragsteinPackage_Relationship(ABC):

    def __init__(self, name: str, lowerBound: int, upperBound: int, KragsteinPackage_Relationship: "KragsteinPackage_Class" = None, KragsteinPackage_Relationship3: "KragsteinPackage_Class" = None, KragsteinPackage_Relationship11: "KragsteinPackage_Class" = None):
        self.name = name
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.KragsteinPackage_Relationship = KragsteinPackage_Relationship
        self.KragsteinPackage_Relationship3 = KragsteinPackage_Relationship3
        self.KragsteinPackage_Relationship11 = KragsteinPackage_Relationship11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def KragsteinPackage_Relationship11(self):
        return self.__KragsteinPackage_Relationship11

    @KragsteinPackage_Relationship11.setter
    def KragsteinPackage_Relationship11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Relationship__KragsteinPackage_Relationship11", None)
        self.__KragsteinPackage_Relationship11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KragsteinPackage_Class10"):
                opp_val = getattr(old_value, "KragsteinPackage_Class10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KragsteinPackage_Class10"):
                opp_val = getattr(value, "KragsteinPackage_Class10", None)
                if opp_val is None:
                    setattr(value, "KragsteinPackage_Class10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def KragsteinPackage_Relationship(self):
        return self.__KragsteinPackage_Relationship

    @KragsteinPackage_Relationship.setter
    def KragsteinPackage_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Relationship__KragsteinPackage_Relationship", None)
        self.__KragsteinPackage_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KragsteinPackage_Class"):
                opp_val = getattr(old_value, "KragsteinPackage_Class", None)
                if opp_val == self:
                    setattr(old_value, "KragsteinPackage_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KragsteinPackage_Class"):
                opp_val = getattr(value, "KragsteinPackage_Class", None)
                setattr(value, "KragsteinPackage_Class", self)

    @property
    def KragsteinPackage_Relationship3(self):
        return self.__KragsteinPackage_Relationship3

    @KragsteinPackage_Relationship3.setter
    def KragsteinPackage_Relationship3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Relationship__KragsteinPackage_Relationship3", None)
        self.__KragsteinPackage_Relationship3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "KragsteinPackage_Class4"):
                opp_val = getattr(old_value, "KragsteinPackage_Class4", None)
                if opp_val == self:
                    setattr(old_value, "KragsteinPackage_Class4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "KragsteinPackage_Class4"):
                opp_val = getattr(value, "KragsteinPackage_Class4", None)
                setattr(value, "KragsteinPackage_Class4", self)

class KragsteinPackage_Unit(ABC):

    pass
class KragsteinPackage_Package:

    def __init__(self, name: str, path: str, KragsteinPackage_Package: set["KragsteinPackage_Unit"] = None):
        self.name = name
        self.path = path
        self.KragsteinPackage_Package = KragsteinPackage_Package if KragsteinPackage_Package is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def KragsteinPackage_Package(self):
        return self.__KragsteinPackage_Package

    @KragsteinPackage_Package.setter
    def KragsteinPackage_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KragsteinPackage_Package__KragsteinPackage_Package", None)
        self.__KragsteinPackage_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "KragsteinPackage_Unit"):
                    opp_val = getattr(item, "KragsteinPackage_Unit", None)
                    
                    if opp_val == self:
                        setattr(item, "KragsteinPackage_Unit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "KragsteinPackage_Unit"):
                    opp_val = getattr(item, "KragsteinPackage_Unit", None)
                    
                    setattr(item, "KragsteinPackage_Unit", self)
                    

class KragsteinPackage_Dependency(Relationship):

    pass
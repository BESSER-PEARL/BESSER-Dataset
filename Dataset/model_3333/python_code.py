from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Vis(Enum):
    public = "public"
    private = "private"
    protected = "protected"
class ReferenceType(Enum):
    JClassType = "JClassType"
    JInterfaceType = "JInterfaceType"
    JArrayType = "JArrayType"
class PrimitiveType(Enum):
    JByte = "JByte"
    JShort = "JShort"
    JInt = "JInt"
    JLong = "JLong"
    JChar = "JChar"
    JFloat = "JFloat"
    JDouble = "JDouble"
    JBoolean = "JBoolean"
class Direction(Enum):
    input = "input"
    return = "return"


############################################
# Definition of Classes
############################################

class JParameter:

    pass
class javaMetaModel_JPrimitiveTypePar(JParameter):

    def __init__(self, primitiveType: str):
        self.primitiveType = primitiveType
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

class JField:

    pass
class javaMetaModel_JReference(JField):

    def __init__(self, refType: str):
        self.refType = refType
        
    @property
    def refType(self) -> str:
        return self.__refType

    @refType.setter
    def refType(self, refType: str):
        self.__refType = refType

class javaMetaModel_JAttribute(JField):

    def __init__(self, primitiveType: str):
        self.primitiveType = primitiveType
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

class javaMetaModel_JReferenceTypePar(JParameter):

    def __init__(self, refType: str):
        self.refType = refType
        
    @property
    def refType(self) -> str:
        return self.__refType

    @refType.setter
    def refType(self, refType: str):
        self.__refType = refType

class JElement:

    pass
class javaMetaModel_JFeature(JElement):

    def __init__(self, visibility: str, isStatic: bool, JFeature: "javaMetaModel_JClass" = None, jfeature: "javaMetaModel_JClass" = None):
        self.visibility = visibility
        self.isStatic = isStatic
        self.JFeature = JFeature
        self.jfeature = jfeature
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def JFeature(self):
        return self.__JFeature

    @JFeature.setter
    def JFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JFeature__JFeature", None)
        self.__JFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner2"):
                opp_val = getattr(old_value, "owner2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner2"):
                opp_val = getattr(value, "owner2", None)
                if opp_val is None:
                    setattr(value, "owner2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jfeature(self):
        return self.__jfeature

    @jfeature.setter
    def jfeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JFeature__jfeature", None)
        self.__jfeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JClass14"):
                opp_val = getattr(old_value, "JClass14", None)
                if opp_val == self:
                    setattr(old_value, "JClass14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JClass14"):
                opp_val = getattr(value, "JClass14", None)
                setattr(value, "JClass14", self)

class javaMetaModel_JClass(JElement):

    def __init__(self, isAbstract: bool, isFinal: bool, jclass: "javaMetaModel_JPackage" = None, JClass: "javaMetaModel_JClass" = None, jsuperClass: set["javaMetaModel_JClass"] = None, owner2: set["javaMetaModel_JFeature"] = None, JClass8: "javaMetaModel_JClass" = None, jsubClass: "javaMetaModel_JClass" = None, JClass11: "javaMetaModel_JPackage" = None, JClass14: "javaMetaModel_JFeature" = None):
        self.isAbstract = isAbstract
        self.isFinal = isFinal
        self.jclass = jclass
        self.JClass = JClass
        self.jsuperClass = jsuperClass if jsuperClass is not None else set()
        self.owner2 = owner2 if owner2 is not None else set()
        self.JClass8 = JClass8
        self.jsubClass = jsubClass
        self.JClass11 = JClass11
        self.JClass14 = JClass14
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def JClass8(self):
        return self.__JClass8

    @JClass8.setter
    def JClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JClass__JClass8", None)
        self.__JClass8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jsubClass"):
                opp_val = getattr(old_value, "jsubClass", None)
                if opp_val == self:
                    setattr(old_value, "jsubClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jsubClass"):
                opp_val = getattr(value, "jsubClass", None)
                setattr(value, "jsubClass", self)

    @property
    def jsuperClass(self):
        return self.__jsuperClass

    @jsuperClass.setter
    def jsuperClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JClass__jsuperClass", None)
        self.__jsuperClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JClass"):
                    opp_val = getattr(item, "JClass", None)
                    
                    if opp_val == self:
                        setattr(item, "JClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JClass"):
                    opp_val = getattr(item, "JClass", None)
                    
                    setattr(item, "JClass", self)
                    

    @property
    def jsubClass(self):
        return self.__jsubClass

    @jsubClass.setter
    def jsubClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JClass__jsubClass", None)
        self.__jsubClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JClass8"):
                opp_val = getattr(old_value, "JClass8", None)
                if opp_val == self:
                    setattr(old_value, "JClass8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JClass8"):
                opp_val = getattr(value, "JClass8", None)
                setattr(value, "JClass8", self)

    @property
    def JClass(self):
        return self.__JClass

    @JClass.setter
    def JClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JClass__JClass", None)
        self.__JClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jsuperClass"):
                opp_val = getattr(old_value, "jsuperClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jsuperClass"):
                opp_val = getattr(value, "jsuperClass", None)
                if opp_val is None:
                    setattr(value, "jsuperClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JClass14(self):
        return self.__JClass14

    @JClass14.setter
    def JClass14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JClass__JClass14", None)
        self.__JClass14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jfeature"):
                opp_val = getattr(old_value, "jfeature", None)
                if opp_val == self:
                    setattr(old_value, "jfeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jfeature"):
                opp_val = getattr(value, "jfeature", None)
                setattr(value, "jfeature", self)

    @property
    def owner2(self):
        return self.__owner2

    @owner2.setter
    def owner2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JClass__owner2", None)
        self.__owner2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JFeature"):
                    opp_val = getattr(item, "JFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "JFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JFeature"):
                    opp_val = getattr(item, "JFeature", None)
                    
                    setattr(item, "JFeature", self)
                    

    @property
    def jclass(self):
        return self.__jclass

    @jclass.setter
    def jclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JClass__jclass", None)
        self.__jclass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JPackage"):
                opp_val = getattr(old_value, "JPackage", None)
                if opp_val == self:
                    setattr(old_value, "JPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JPackage"):
                opp_val = getattr(value, "JPackage", None)
                setattr(value, "JPackage", self)

    @property
    def JClass11(self):
        return self.__JClass11

    @JClass11.setter
    def JClass11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JClass__JClass11", None)
        self.__JClass11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner10"):
                opp_val = getattr(old_value, "owner10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner10"):
                opp_val = getattr(value, "owner10", None)
                if opp_val is None:
                    setattr(value, "owner10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaMetaModel_JPackage(JElement):

    pass
class JFeature:

    pass
class javaMetaModel_JField(JFeature):

    pass
class javaMetaModel_JMethod(JFeature):

    pass
class javaMetaModel_JElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class javaMetaModel_JParameter(JElement):

    def __init__(self, direction: str, JParameter: "javaMetaModel_JMethod" = None, jparameter: "javaMetaModel_JMethod" = None):
        self.direction = direction
        self.JParameter = JParameter
        self.jparameter = jparameter
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def jparameter(self):
        return self.__jparameter

    @jparameter.setter
    def jparameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JParameter__jparameter", None)
        self.__jparameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JMethod"):
                opp_val = getattr(old_value, "JMethod", None)
                if opp_val == self:
                    setattr(old_value, "JMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JMethod"):
                opp_val = getattr(value, "JMethod", None)
                setattr(value, "JMethod", self)

    @property
    def JParameter(self):
        return self.__JParameter

    @JParameter.setter
    def JParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaMetaModel_JParameter__JParameter", None)
        self.__JParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

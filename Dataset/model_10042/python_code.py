from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class JvmVisibility(Enum):
    DEFAULT = "DEFAULT"
    PRIVATE = "PRIVATE"
    PROTECTED = "PROTECTED"
    PUBLIC = "PUBLIC"


############################################
# Definition of Classes
############################################

class xtend_CreateExtensionInfo:

    def __init__(self, name: str, xtend_CreateExtensionInfo: "xtend_XtendFunction" = None, xtend_CreateExtensionInfo46: "xtend_XExpression" = None):
        self.name = name
        self.xtend_CreateExtensionInfo = xtend_CreateExtensionInfo
        self.xtend_CreateExtensionInfo46 = xtend_CreateExtensionInfo46
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xtend_CreateExtensionInfo(self):
        return self.__xtend_CreateExtensionInfo

    @xtend_CreateExtensionInfo.setter
    def xtend_CreateExtensionInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_CreateExtensionInfo__xtend_CreateExtensionInfo", None)
        self.__xtend_CreateExtensionInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendFunction14"):
                opp_val = getattr(old_value, "xtend_XtendFunction14", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XtendFunction14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendFunction14"):
                opp_val = getattr(value, "xtend_XtendFunction14", None)
                setattr(value, "xtend_XtendFunction14", self)

    @property
    def xtend_CreateExtensionInfo46(self):
        return self.__xtend_CreateExtensionInfo46

    @xtend_CreateExtensionInfo46.setter
    def xtend_CreateExtensionInfo46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_CreateExtensionInfo__xtend_CreateExtensionInfo46", None)
        self.__xtend_CreateExtensionInfo46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XExpression47"):
                opp_val = getattr(old_value, "xtend_XExpression47", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XExpression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XExpression47"):
                opp_val = getattr(value, "xtend_XExpression47", None)
                setattr(value, "xtend_XExpression47", self)

class XtendExecutable:

    pass
class xtend_XtendFunction(XtendExecutable):

    def __init__(self, name: str, xtend_XtendFunction14: "xtend_CreateExtensionInfo" = None, xtend_XtendFunction: "xtend_JvmTypeReference" = None):
        self.name = name
        self.xtend_XtendFunction14 = xtend_XtendFunction14
        self.xtend_XtendFunction = xtend_XtendFunction
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xtend_XtendFunction(self):
        return self.__xtend_XtendFunction

    @xtend_XtendFunction.setter
    def xtend_XtendFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendFunction__xtend_XtendFunction", None)
        self.__xtend_XtendFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeReference12"):
                opp_val = getattr(old_value, "xtend_JvmTypeReference12", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeReference12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeReference12"):
                opp_val = getattr(value, "xtend_JvmTypeReference12", None)
                setattr(value, "xtend_JvmTypeReference12", self)

    @property
    def xtend_XtendFunction14(self):
        return self.__xtend_XtendFunction14

    @xtend_XtendFunction14.setter
    def xtend_XtendFunction14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendFunction__xtend_XtendFunction14", None)
        self.__xtend_XtendFunction14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_CreateExtensionInfo"):
                opp_val = getattr(old_value, "xtend_CreateExtensionInfo", None)
                if opp_val == self:
                    setattr(old_value, "xtend_CreateExtensionInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_CreateExtensionInfo"):
                opp_val = getattr(value, "xtend_CreateExtensionInfo", None)
                setattr(value, "xtend_CreateExtensionInfo", self)

    def isDispatch(self) :
        # TODO: Implement isDispatch method
        pass

    def isOverride(self) :
        # TODO: Implement isOverride method
        pass

    def isStrictFloatingPoint(self) :
        # TODO: Implement isStrictFloatingPoint method
        pass

    def isSynchonized(self) :
        # TODO: Implement isSynchonized method
        pass

    def isAbstract(self) :
        # TODO: Implement isAbstract method
        pass

    def isNative(self) :
        # TODO: Implement isNative method
        pass

class XtendAnnotationTarget:

    pass
class xtend_XtendMember(XtendAnnotationTarget):

    def __init__(self, modifiers: str, XtendMember: "xtend_XtendTypeDeclaration" = None, xtend_XtendMember: "xtend_XtendAnnotationTarget" = None, members: "xtend_XtendTypeDeclaration" = None):
        self.modifiers = modifiers
        self.XtendMember = XtendMember
        self.xtend_XtendMember = xtend_XtendMember
        self.members = members
        
        pass
    @property
    def modifiers(self):
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers


    @property
    def xtend_XtendMember(self):
        return self.__xtend_XtendMember

    @xtend_XtendMember.setter
    def xtend_XtendMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendMember__xtend_XtendMember", None)
        self.__xtend_XtendMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendAnnotationTarget9"):
                opp_val = getattr(old_value, "xtend_XtendAnnotationTarget9", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XtendAnnotationTarget9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendAnnotationTarget9"):
                opp_val = getattr(value, "xtend_XtendAnnotationTarget9", None)
                setattr(value, "xtend_XtendAnnotationTarget9", self)

    @property
    def XtendMember(self):
        return self.__XtendMember

    @XtendMember.setter
    def XtendMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendMember__XtendMember", None)
        self.__XtendMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declaringType"):
                opp_val = getattr(old_value, "declaringType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declaringType"):
                opp_val = getattr(value, "declaringType", None)
                if opp_val is None:
                    setattr(value, "declaringType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendMember__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XtendTypeDeclaration"):
                opp_val = getattr(old_value, "XtendTypeDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "XtendTypeDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XtendTypeDeclaration"):
                opp_val = getattr(value, "XtendTypeDeclaration", None)
                setattr(value, "XtendTypeDeclaration", self)

    def getVisibility(self) :
        # TODO: Implement getVisibility method
        pass

    def isStatic(self) :
        # TODO: Implement isStatic method
        pass

    def isFinal(self) :
        # TODO: Implement isFinal method
        pass

    def getDeclaredVisibility(self) :
        # TODO: Implement getDeclaredVisibility method
        pass

class xtend_XtendParameter(XtendAnnotationTarget):

    def __init__(self, name: str, varArg: bool, extension: bool, xtend_XtendParameter: "xtend_JvmTypeReference" = None, xtend_XtendParameter184: "xtend_XtendExecutable" = None):
        self.name = name
        self.varArg = varArg
        self.extension = extension
        self.xtend_XtendParameter = xtend_XtendParameter
        self.xtend_XtendParameter184 = xtend_XtendParameter184
        
        pass
    @property
    def varArg(self):
        return self.__varArg

    @varArg.setter
    def varArg(self, varArg: bool):
        self.__varArg = varArg


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension


    @property
    def xtend_XtendParameter184(self):
        return self.__xtend_XtendParameter184

    @xtend_XtendParameter184.setter
    def xtend_XtendParameter184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendParameter__xtend_XtendParameter184", None)
        self.__xtend_XtendParameter184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendExecutable183"):
                opp_val = getattr(old_value, "xtend_XtendExecutable183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendExecutable183"):
                opp_val = getattr(value, "xtend_XtendExecutable183", None)
                if opp_val is None:
                    setattr(value, "xtend_XtendExecutable183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_XtendParameter(self):
        return self.__xtend_XtendParameter

    @xtend_XtendParameter.setter
    def xtend_XtendParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendParameter__xtend_XtendParameter", None)
        self.__xtend_XtendParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeReference20"):
                opp_val = getattr(old_value, "xtend_JvmTypeReference20", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeReference20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeReference20"):
                opp_val = getattr(value, "xtend_JvmTypeReference20", None)
                setattr(value, "xtend_JvmTypeReference20", self)

class xtend_XAnnotation:

    pass
class xtend_XtendAnnotationTarget(ABC):

    pass
class xtend_XExpression(ABC):

    pass
class xtend_XtendFile:

    def __init__(self, package: str, xtend_XtendFile: set["xtend_XtendTypeDeclaration"] = None):
        self.package = package
        self.xtend_XtendFile = xtend_XtendFile if xtend_XtendFile is not None else set()
        
        pass
    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package


    @property
    def xtend_XtendFile(self):
        return self.__xtend_XtendFile

    @xtend_XtendFile.setter
    def xtend_XtendFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendFile__xtend_XtendFile", None)
        self.__xtend_XtendFile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_XtendTypeDeclaration"):
                    opp_val = getattr(item, "xtend_XtendTypeDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_XtendTypeDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_XtendTypeDeclaration"):
                    opp_val = getattr(item, "xtend_XtendTypeDeclaration", None)
                    
                    setattr(item, "xtend_XtendTypeDeclaration", self)
                    

class JvmAnnotationValue:

    pass
class xtend_JvmLongAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class xtend_JvmShortAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class xtend_JvmStringAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class xtend_JvmEnumAnnotationValue(JvmAnnotationValue):

    pass
class xtend_JvmDoubleAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: float):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: float):
        self.__values = values


class xtend_JvmCharAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class xtend_JvmTypeAnnotationValue(JvmAnnotationValue):

    pass
class xtend_JvmFloatAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: float):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: float):
        self.__values = values


class xtend_JvmByteAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class xtend_JvmBooleanAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: bool):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: bool):
        self.__values = values


class xtend_JvmCustomAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class xtend_JvmIntAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: int):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: int):
        self.__values = values


class xtend_JvmAnnotationReference:

    pass
class xtend_JvmAnnotationTarget(ABC):

    pass
class xtend_JvmAnnotationValue(ABC):

    def __init__(self, xtend_JvmAnnotationValue: "xtend_JvmOperation" = None, xtend_JvmAnnotationValue231: "xtend_JvmAnnotationReference" = None, xtend_JvmAnnotationValue233: "xtend_JvmOperation" = None):
        self.xtend_JvmAnnotationValue = xtend_JvmAnnotationValue
        self.xtend_JvmAnnotationValue231 = xtend_JvmAnnotationValue231
        self.xtend_JvmAnnotationValue233 = xtend_JvmAnnotationValue233
        
        pass
    @property
    def xtend_JvmAnnotationValue231(self):
        return self.__xtend_JvmAnnotationValue231

    @xtend_JvmAnnotationValue231.setter
    def xtend_JvmAnnotationValue231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmAnnotationValue__xtend_JvmAnnotationValue231", None)
        self.__xtend_JvmAnnotationValue231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmAnnotationReference230"):
                opp_val = getattr(old_value, "xtend_JvmAnnotationReference230", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmAnnotationReference230"):
                opp_val = getattr(value, "xtend_JvmAnnotationReference230", None)
                if opp_val is None:
                    setattr(value, "xtend_JvmAnnotationReference230", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmAnnotationValue(self):
        return self.__xtend_JvmAnnotationValue

    @xtend_JvmAnnotationValue.setter
    def xtend_JvmAnnotationValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmAnnotationValue__xtend_JvmAnnotationValue", None)
        self.__xtend_JvmAnnotationValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmOperation222"):
                opp_val = getattr(old_value, "xtend_JvmOperation222", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmOperation222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmOperation222"):
                opp_val = getattr(value, "xtend_JvmOperation222", None)
                setattr(value, "xtend_JvmOperation222", self)

    @property
    def xtend_JvmAnnotationValue233(self):
        return self.__xtend_JvmAnnotationValue233

    @xtend_JvmAnnotationValue233.setter
    def xtend_JvmAnnotationValue233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmAnnotationValue__xtend_JvmAnnotationValue233", None)
        self.__xtend_JvmAnnotationValue233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmOperation234"):
                opp_val = getattr(old_value, "xtend_JvmOperation234", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmOperation234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmOperation234"):
                opp_val = getattr(value, "xtend_JvmOperation234", None)
                setattr(value, "xtend_JvmOperation234", self)

    def getValueName(self) :
        # TODO: Implement getValueName method
        pass

class JvmExecutable:

    pass
class xtend_JvmOperation(JvmExecutable):

    def __init__(self, static: bool, final: bool, abstract: bool, xtend_JvmOperation: "xtend_JvmTypeReference" = None, xtend_JvmOperation222: "xtend_JvmAnnotationValue" = None, xtend_JvmOperation234: "xtend_JvmAnnotationValue" = None):
        self.static = static
        self.final = final
        self.abstract = abstract
        self.xtend_JvmOperation = xtend_JvmOperation
        self.xtend_JvmOperation222 = xtend_JvmOperation222
        self.xtend_JvmOperation234 = xtend_JvmOperation234
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def xtend_JvmOperation234(self):
        return self.__xtend_JvmOperation234

    @xtend_JvmOperation234.setter
    def xtend_JvmOperation234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmOperation__xtend_JvmOperation234", None)
        self.__xtend_JvmOperation234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmAnnotationValue233"):
                opp_val = getattr(old_value, "xtend_JvmAnnotationValue233", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmAnnotationValue233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmAnnotationValue233"):
                opp_val = getattr(value, "xtend_JvmAnnotationValue233", None)
                setattr(value, "xtend_JvmAnnotationValue233", self)

    @property
    def xtend_JvmOperation222(self):
        return self.__xtend_JvmOperation222

    @xtend_JvmOperation222.setter
    def xtend_JvmOperation222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmOperation__xtend_JvmOperation222", None)
        self.__xtend_JvmOperation222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmAnnotationValue"):
                opp_val = getattr(old_value, "xtend_JvmAnnotationValue", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmAnnotationValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmAnnotationValue"):
                opp_val = getattr(value, "xtend_JvmAnnotationValue", None)
                setattr(value, "xtend_JvmAnnotationValue", self)

    @property
    def xtend_JvmOperation(self):
        return self.__xtend_JvmOperation

    @xtend_JvmOperation.setter
    def xtend_JvmOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmOperation__xtend_JvmOperation", None)
        self.__xtend_JvmOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeReference220"):
                opp_val = getattr(old_value, "xtend_JvmTypeReference220", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeReference220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeReference220"):
                opp_val = getattr(value, "xtend_JvmTypeReference220", None)
                setattr(value, "xtend_JvmTypeReference220", self)

class JvmFeature:

    pass
class xtend_JvmField(JvmFeature):

    def __init__(self, static: bool, final: bool, xtend_JvmField: "xtend_JvmTypeReference" = None):
        self.static = static
        self.final = final
        self.xtend_JvmField = xtend_JvmField
        
        pass
    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def xtend_JvmField(self):
        return self.__xtend_JvmField

    @xtend_JvmField.setter
    def xtend_JvmField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmField__xtend_JvmField", None)
        self.__xtend_JvmField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeReference213"):
                opp_val = getattr(old_value, "xtend_JvmTypeReference213", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeReference213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeReference213"):
                opp_val = getattr(value, "xtend_JvmTypeReference213", None)
                setattr(value, "xtend_JvmTypeReference213", self)

class JvmAnnotationTarget:

    pass
class xtend_JvmAnnotationAnnotationValue(JvmAnnotationValue, JvmAnnotationTarget):

    pass
class JvmCompoundTypeReference:

    pass
class xtend_JvmSynonymTypeReference(JvmCompoundTypeReference):

    pass
class xtend_JvmMultiTypeReference(JvmCompoundTypeReference):

    pass
class JvmTypeReference:

    pass
class xtend_JvmAnyTypeReference(JvmTypeReference):

    pass
class xtend_JvmSpecializedTypeReference(JvmTypeReference):

    pass
class xtend_JvmUnknownTypeReference(JvmTypeReference):

    def __init__(self, exception: str):
        self.exception = exception
        
        pass
    @property
    def exception(self):
        return self.__exception

    @exception.setter
    def exception(self, exception: str):
        self.__exception = exception


class xtend_JvmGenericArrayTypeReference(JvmTypeReference):

    def __init__(self, xtend_JvmGenericArrayTypeReference: "xtend_JvmTypeReference" = None):
        self.xtend_JvmGenericArrayTypeReference = xtend_JvmGenericArrayTypeReference
        
        pass
    @property
    def xtend_JvmGenericArrayTypeReference(self):
        return self.__xtend_JvmGenericArrayTypeReference

    @xtend_JvmGenericArrayTypeReference.setter
    def xtend_JvmGenericArrayTypeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmGenericArrayTypeReference__xtend_JvmGenericArrayTypeReference", None)
        self.__xtend_JvmGenericArrayTypeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeReference207"):
                opp_val = getattr(old_value, "xtend_JvmTypeReference207", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeReference207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeReference207"):
                opp_val = getattr(value, "xtend_JvmTypeReference207", None)
                setattr(value, "xtend_JvmTypeReference207", self)

    def getType(self) :
        # TODO: Implement getType method
        pass

    def getDimensions(self) :
        # TODO: Implement getDimensions method
        pass

class xtend_JvmDelegateTypeReference(JvmTypeReference):

    pass
class xtend_JvmCompoundTypeReference(JvmTypeReference):

    pass
class xtend_JvmParameterizedTypeReference(JvmTypeReference):

    pass
class JvmTypeParameterDeclarator:

    pass
class xtend_JvmExecutable(JvmTypeParameterDeclarator, JvmFeature):

    def __init__(self, varArgs: bool, xtend_JvmExecutable: set["xtend_JvmFormalParameter"] = None, xtend_JvmExecutable217: set["xtend_JvmTypeReference"] = None):
        self.varArgs = varArgs
        self.xtend_JvmExecutable = xtend_JvmExecutable if xtend_JvmExecutable is not None else set()
        self.xtend_JvmExecutable217 = xtend_JvmExecutable217 if xtend_JvmExecutable217 is not None else set()
        
        pass
    @property
    def varArgs(self):
        return self.__varArgs

    @varArgs.setter
    def varArgs(self, varArgs: bool):
        self.__varArgs = varArgs


    @property
    def xtend_JvmExecutable217(self):
        return self.__xtend_JvmExecutable217

    @xtend_JvmExecutable217.setter
    def xtend_JvmExecutable217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmExecutable__xtend_JvmExecutable217", None)
        self.__xtend_JvmExecutable217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmTypeReference218"):
                    opp_val = getattr(item, "xtend_JvmTypeReference218", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmTypeReference218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmTypeReference218"):
                    opp_val = getattr(item, "xtend_JvmTypeReference218", None)
                    
                    setattr(item, "xtend_JvmTypeReference218", self)
                    

    @property
    def xtend_JvmExecutable(self):
        return self.__xtend_JvmExecutable

    @xtend_JvmExecutable.setter
    def xtend_JvmExecutable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmExecutable__xtend_JvmExecutable", None)
        self.__xtend_JvmExecutable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmFormalParameter215"):
                    opp_val = getattr(item, "xtend_JvmFormalParameter215", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmFormalParameter215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmFormalParameter215"):
                    opp_val = getattr(item, "xtend_JvmFormalParameter215", None)
                    
                    setattr(item, "xtend_JvmFormalParameter215", self)
                    

class JvmField:

    pass
class xtend_JvmEnumerationLiteral(JvmField):

    def __init__(self, xtend_JvmEnumerationLiteral240: "xtend_JvmEnumAnnotationValue" = None, xtend_JvmEnumerationLiteral: "xtend_JvmEnumerationType" = None):
        self.xtend_JvmEnumerationLiteral240 = xtend_JvmEnumerationLiteral240
        self.xtend_JvmEnumerationLiteral = xtend_JvmEnumerationLiteral
        
        pass
    @property
    def xtend_JvmEnumerationLiteral(self):
        return self.__xtend_JvmEnumerationLiteral

    @xtend_JvmEnumerationLiteral.setter
    def xtend_JvmEnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmEnumerationLiteral__xtend_JvmEnumerationLiteral", None)
        self.__xtend_JvmEnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmEnumerationType"):
                opp_val = getattr(old_value, "xtend_JvmEnumerationType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmEnumerationType"):
                opp_val = getattr(value, "xtend_JvmEnumerationType", None)
                if opp_val is None:
                    setattr(value, "xtend_JvmEnumerationType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmEnumerationLiteral240(self):
        return self.__xtend_JvmEnumerationLiteral240

    @xtend_JvmEnumerationLiteral240.setter
    def xtend_JvmEnumerationLiteral240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmEnumerationLiteral__xtend_JvmEnumerationLiteral240", None)
        self.__xtend_JvmEnumerationLiteral240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmEnumAnnotationValue"):
                opp_val = getattr(old_value, "xtend_JvmEnumAnnotationValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmEnumAnnotationValue"):
                opp_val = getattr(value, "xtend_JvmEnumAnnotationValue", None)
                if opp_val is None:
                    setattr(value, "xtend_JvmEnumAnnotationValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getEnumType(self) :
        # TODO: Implement getEnumType method
        pass

class JvmDeclaredType:

    pass
class xtend_JvmGenericType(JvmTypeParameterDeclarator, JvmDeclaredType):

    def __init__(self, interface: bool):
        self.interface = interface
        
        pass
    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface


    def isInstantiateable(self) :
        # TODO: Implement isInstantiateable method
        pass

    def getDeclaredConstructors(self):
        # TODO: Implement getDeclaredConstructors method
        pass

    def getExtendedClass(self) :
        # TODO: Implement getExtendedClass method
        pass

    def getExtendedInterfaces(self):
        # TODO: Implement getExtendedInterfaces method
        pass

class xtend_JvmEnumerationType(JvmDeclaredType):

    pass
class xtend_JvmAnnotationType(JvmDeclaredType):

    pass
class JvmTypeConstraint:

    pass
class xtend_JvmLowerBound(JvmTypeConstraint):

    pass
class xtend_JvmUpperBound(JvmTypeConstraint):

    pass
class xtend_JvmTypeConstraint(ABC):

    def __init__(self, xtend_JvmTypeConstraint: "xtend_JvmTypeReference" = None, constraints: "xtend_JvmConstraintOwner" = None, JvmTypeConstraint: "xtend_JvmConstraintOwner" = None):
        self.xtend_JvmTypeConstraint = xtend_JvmTypeConstraint
        self.constraints = constraints
        self.JvmTypeConstraint = JvmTypeConstraint
        
        pass
    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeConstraint__constraints", None)
        self.__constraints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmConstraintOwner"):
                opp_val = getattr(old_value, "JvmConstraintOwner", None)
                if opp_val == self:
                    setattr(old_value, "JvmConstraintOwner", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmConstraintOwner"):
                opp_val = getattr(value, "JvmConstraintOwner", None)
                setattr(value, "JvmConstraintOwner", self)

    @property
    def xtend_JvmTypeConstraint(self):
        return self.__xtend_JvmTypeConstraint

    @xtend_JvmTypeConstraint.setter
    def xtend_JvmTypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeConstraint__xtend_JvmTypeConstraint", None)
        self.__xtend_JvmTypeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeReference198"):
                opp_val = getattr(old_value, "xtend_JvmTypeReference198", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeReference198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeReference198"):
                opp_val = getattr(value, "xtend_JvmTypeReference198", None)
                setattr(value, "xtend_JvmTypeReference198", self)

    @property
    def JvmTypeConstraint(self):
        return self.__JvmTypeConstraint

    @JvmTypeConstraint.setter
    def JvmTypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeConstraint__JvmTypeConstraint", None)
        self.__JvmTypeConstraint = value
        
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

    def getSimpleName(self) :
        # TODO: Implement getSimpleName method
        pass

    def getIdentifier(self) :
        # TODO: Implement getIdentifier method
        pass

    def getQualifiedName(self, xtend_innerClassDelimiter) :
        # TODO: Implement getQualifiedName method
        pass

class xtend_JvmConstraintOwner(ABC):

    pass
class xtend_JvmTypeParameterDeclarator(ABC):

    pass
class JvmConstraintOwner:

    pass
class xtend_JvmWildcardTypeReference(JvmConstraintOwner, JvmTypeReference):

    pass
class JvmMember:

    pass
class xtend_JvmFeature(JvmMember):

    pass
class JvmComponentType:

    pass
class xtend_JvmTypeParameter(JvmConstraintOwner, JvmComponentType):

    def __init__(self, name: str, xtend_JvmTypeParameter: "xtend_XtendClass" = None, xtend_JvmTypeParameter53: "xtend_XtendInterface" = None, xtend_JvmTypeParameter178: "xtend_XtendExecutable" = None, typeParameters: "xtend_JvmTypeParameterDeclarator" = None, JvmTypeParameter: "xtend_JvmTypeParameterDeclarator" = None):
        self.name = name
        self.xtend_JvmTypeParameter = xtend_JvmTypeParameter
        self.xtend_JvmTypeParameter53 = xtend_JvmTypeParameter53
        self.xtend_JvmTypeParameter178 = xtend_JvmTypeParameter178
        self.typeParameters = typeParameters
        self.JvmTypeParameter = JvmTypeParameter
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xtend_JvmTypeParameter178(self):
        return self.__xtend_JvmTypeParameter178

    @xtend_JvmTypeParameter178.setter
    def xtend_JvmTypeParameter178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeParameter__xtend_JvmTypeParameter178", None)
        self.__xtend_JvmTypeParameter178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendExecutable177"):
                opp_val = getattr(old_value, "xtend_XtendExecutable177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendExecutable177"):
                opp_val = getattr(value, "xtend_XtendExecutable177", None)
                if opp_val is None:
                    setattr(value, "xtend_XtendExecutable177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeParameter(self):
        return self.__xtend_JvmTypeParameter

    @xtend_JvmTypeParameter.setter
    def xtend_JvmTypeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeParameter__xtend_JvmTypeParameter", None)
        self.__xtend_JvmTypeParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendClass6"):
                opp_val = getattr(old_value, "xtend_XtendClass6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendClass6"):
                opp_val = getattr(value, "xtend_XtendClass6", None)
                if opp_val is None:
                    setattr(value, "xtend_XtendClass6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeParameter53(self):
        return self.__xtend_JvmTypeParameter53

    @xtend_JvmTypeParameter53.setter
    def xtend_JvmTypeParameter53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeParameter__xtend_JvmTypeParameter53", None)
        self.__xtend_JvmTypeParameter53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendInterface52"):
                opp_val = getattr(old_value, "xtend_XtendInterface52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendInterface52"):
                opp_val = getattr(value, "xtend_XtendInterface52", None)
                if opp_val is None:
                    setattr(value, "xtend_XtendInterface52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JvmTypeParameter(self):
        return self.__JvmTypeParameter

    @JvmTypeParameter.setter
    def JvmTypeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeParameter__JvmTypeParameter", None)
        self.__JvmTypeParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declarator"):
                opp_val = getattr(old_value, "declarator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declarator"):
                opp_val = getattr(value, "declarator", None)
                if opp_val is None:
                    setattr(value, "declarator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def typeParameters(self):
        return self.__typeParameters

    @typeParameters.setter
    def typeParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeParameter__typeParameters", None)
        self.__typeParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeParameterDeclarator"):
                opp_val = getattr(old_value, "JvmTypeParameterDeclarator", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeParameterDeclarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeParameterDeclarator"):
                opp_val = getattr(value, "JvmTypeParameterDeclarator", None)
                setattr(value, "JvmTypeParameterDeclarator", self)

class xtend_JvmPrimitiveType(JvmComponentType):

    def __init__(self, simpleName: str):
        self.simpleName = simpleName
        
        pass
    @property
    def simpleName(self):
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName


class xtend_JvmArrayType(JvmComponentType):

    def __init__(self, JvmArrayType: "xtend_JvmComponentType" = None, arrayType: "xtend_JvmComponentType" = None):
        self.JvmArrayType = JvmArrayType
        self.arrayType = arrayType
        
        pass
    @property
    def arrayType(self):
        return self.__arrayType

    @arrayType.setter
    def arrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmArrayType__arrayType", None)
        self.__arrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmComponentType"):
                opp_val = getattr(old_value, "JvmComponentType", None)
                if opp_val == self:
                    setattr(old_value, "JvmComponentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmComponentType"):
                opp_val = getattr(value, "JvmComponentType", None)
                setattr(value, "JvmComponentType", self)

    @property
    def JvmArrayType(self):
        return self.__JvmArrayType

    @JvmArrayType.setter
    def JvmArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmArrayType__JvmArrayType", None)
        self.__JvmArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentType"):
                opp_val = getattr(old_value, "componentType", None)
                if opp_val == self:
                    setattr(old_value, "componentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentType"):
                opp_val = getattr(value, "componentType", None)
                setattr(value, "componentType", self)

    def getDimensions(self) :
        # TODO: Implement getDimensions method
        pass

class JvmType:

    pass
class xtend_JvmComponentType(JvmType):

    pass
class xtend_JvmVoid(JvmType):

    pass
class xtend_XCatchClause:

    pass
class XAbstractWhileExpression:

    pass
class xtend_XWhileExpression(XAbstractWhileExpression):

    pass
class xtend_XDoWhileExpression(XAbstractWhileExpression):

    pass
class xtend_JvmConstructor(JvmExecutable):

    pass
class xtend_JvmDeclaredType(JvmComponentType, JvmMember):

    def __init__(self, abstract: bool, static: bool, final: bool, packageName: str, xtend_JvmDeclaredType190: set["xtend_JvmTypeReference"] = None, declaringType193: set["xtend_JvmMember"] = None, xtend_JvmDeclaredType: "xtend_XFeatureCall" = None, JvmDeclaredType: "xtend_JvmMember" = None):
        self.abstract = abstract
        self.static = static
        self.final = final
        self.packageName = packageName
        self.xtend_JvmDeclaredType190 = xtend_JvmDeclaredType190 if xtend_JvmDeclaredType190 is not None else set()
        self.declaringType193 = declaringType193 if declaringType193 is not None else set()
        self.xtend_JvmDeclaredType = xtend_JvmDeclaredType
        self.JvmDeclaredType = JvmDeclaredType
        
        pass
    @property
    def packageName(self):
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def declaringType193(self):
        return self.__declaringType193

    @declaringType193.setter
    def declaringType193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmDeclaredType__declaringType193", None)
        self.__declaringType193 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmMember"):
                    opp_val = getattr(item, "JvmMember", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmMember"):
                    opp_val = getattr(item, "JvmMember", None)
                    
                    setattr(item, "JvmMember", self)
                    

    @property
    def xtend_JvmDeclaredType(self):
        return self.__xtend_JvmDeclaredType

    @xtend_JvmDeclaredType.setter
    def xtend_JvmDeclaredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmDeclaredType__xtend_JvmDeclaredType", None)
        self.__xtend_JvmDeclaredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XFeatureCall106"):
                opp_val = getattr(old_value, "xtend_XFeatureCall106", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XFeatureCall106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XFeatureCall106"):
                opp_val = getattr(value, "xtend_XFeatureCall106", None)
                setattr(value, "xtend_XFeatureCall106", self)

    @property
    def xtend_JvmDeclaredType190(self):
        return self.__xtend_JvmDeclaredType190

    @xtend_JvmDeclaredType190.setter
    def xtend_JvmDeclaredType190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmDeclaredType__xtend_JvmDeclaredType190", None)
        self.__xtend_JvmDeclaredType190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmTypeReference191"):
                    opp_val = getattr(item, "xtend_JvmTypeReference191", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmTypeReference191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmTypeReference191"):
                    opp_val = getattr(item, "xtend_JvmTypeReference191", None)
                    
                    setattr(item, "xtend_JvmTypeReference191", self)
                    

    @property
    def JvmDeclaredType(self):
        return self.__JvmDeclaredType

    @JvmDeclaredType.setter
    def JvmDeclaredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmDeclaredType__JvmDeclaredType", None)
        self.__JvmDeclaredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "members211"):
                opp_val = getattr(old_value, "members211", None)
                if opp_val == self:
                    setattr(old_value, "members211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "members211"):
                opp_val = getattr(value, "members211", None)
                setattr(value, "members211", self)

    def findAllFeaturesByName(self, xtend_simpleName):
        # TODO: Implement findAllFeaturesByName method
        pass

    def getAllFeatures(self):
        # TODO: Implement getAllFeatures method
        pass

    def getDeclaredFields(self):
        # TODO: Implement getDeclaredFields method
        pass

    def getDeclaredOperations(self):
        # TODO: Implement getDeclaredOperations method
        pass

class XAbstractFeatureCall:

    pass
class xtend_XAssignment(XAbstractFeatureCall):

    pass
class xtend_XBinaryOperation(XAbstractFeatureCall):

    pass
class xtend_XUnaryOperation(XAbstractFeatureCall):

    pass
class xtend_XFeatureCall(XAbstractFeatureCall):

    def __init__(self, explicitOperationCall: bool, xtend_XFeatureCall: set["xtend_XExpression"] = None, xtend_XFeatureCall106: "xtend_JvmDeclaredType" = None):
        self.explicitOperationCall = explicitOperationCall
        self.xtend_XFeatureCall = xtend_XFeatureCall if xtend_XFeatureCall is not None else set()
        self.xtend_XFeatureCall106 = xtend_XFeatureCall106
        
        pass
    @property
    def explicitOperationCall(self):
        return self.__explicitOperationCall

    @explicitOperationCall.setter
    def explicitOperationCall(self, explicitOperationCall: bool):
        self.__explicitOperationCall = explicitOperationCall


    @property
    def xtend_XFeatureCall(self):
        return self.__xtend_XFeatureCall

    @xtend_XFeatureCall.setter
    def xtend_XFeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XFeatureCall__xtend_XFeatureCall", None)
        self.__xtend_XFeatureCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_XExpression104"):
                    opp_val = getattr(item, "xtend_XExpression104", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_XExpression104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_XExpression104"):
                    opp_val = getattr(item, "xtend_XExpression104", None)
                    
                    setattr(item, "xtend_XExpression104", self)
                    

    @property
    def xtend_XFeatureCall106(self):
        return self.__xtend_XFeatureCall106

    @xtend_XFeatureCall106.setter
    def xtend_XFeatureCall106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XFeatureCall__xtend_XFeatureCall106", None)
        self.__xtend_XFeatureCall106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmDeclaredType"):
                opp_val = getattr(old_value, "xtend_JvmDeclaredType", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmDeclaredType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmDeclaredType"):
                opp_val = getattr(value, "xtend_JvmDeclaredType", None)
                setattr(value, "xtend_JvmDeclaredType", self)

class xtend_XMemberFeatureCall(XAbstractFeatureCall):

    def __init__(self, nullSafe: bool, explicitOperationCall: bool, spreading: bool, xtend_XMemberFeatureCall: "xtend_XExpression" = None, xtend_XMemberFeatureCall101: set["xtend_XExpression"] = None):
        self.nullSafe = nullSafe
        self.explicitOperationCall = explicitOperationCall
        self.spreading = spreading
        self.xtend_XMemberFeatureCall = xtend_XMemberFeatureCall
        self.xtend_XMemberFeatureCall101 = xtend_XMemberFeatureCall101 if xtend_XMemberFeatureCall101 is not None else set()
        
        pass
    @property
    def nullSafe(self):
        return self.__nullSafe

    @nullSafe.setter
    def nullSafe(self, nullSafe: bool):
        self.__nullSafe = nullSafe


    @property
    def spreading(self):
        return self.__spreading

    @spreading.setter
    def spreading(self, spreading: bool):
        self.__spreading = spreading


    @property
    def explicitOperationCall(self):
        return self.__explicitOperationCall

    @explicitOperationCall.setter
    def explicitOperationCall(self, explicitOperationCall: bool):
        self.__explicitOperationCall = explicitOperationCall


    @property
    def xtend_XMemberFeatureCall101(self):
        return self.__xtend_XMemberFeatureCall101

    @xtend_XMemberFeatureCall101.setter
    def xtend_XMemberFeatureCall101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XMemberFeatureCall__xtend_XMemberFeatureCall101", None)
        self.__xtend_XMemberFeatureCall101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_XExpression102"):
                    opp_val = getattr(item, "xtend_XExpression102", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_XExpression102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_XExpression102"):
                    opp_val = getattr(item, "xtend_XExpression102", None)
                    
                    setattr(item, "xtend_XExpression102", self)
                    

    @property
    def xtend_XMemberFeatureCall(self):
        return self.__xtend_XMemberFeatureCall

    @xtend_XMemberFeatureCall.setter
    def xtend_XMemberFeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XMemberFeatureCall__xtend_XMemberFeatureCall", None)
        self.__xtend_XMemberFeatureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XExpression99"):
                opp_val = getattr(old_value, "xtend_XExpression99", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XExpression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XExpression99"):
                opp_val = getattr(value, "xtend_XExpression99", None)
                setattr(value, "xtend_XExpression99", self)

class xtend_JvmIdentifiableElement(ABC):

    def __init__(self, xtend_JvmIdentifiableElement: "xtend_XAbstractFeatureCall" = None):
        self.xtend_JvmIdentifiableElement = xtend_JvmIdentifiableElement
        
        pass
    @property
    def xtend_JvmIdentifiableElement(self):
        return self.__xtend_JvmIdentifiableElement

    @xtend_JvmIdentifiableElement.setter
    def xtend_JvmIdentifiableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmIdentifiableElement__xtend_JvmIdentifiableElement", None)
        self.__xtend_JvmIdentifiableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XAbstractFeatureCall"):
                opp_val = getattr(old_value, "xtend_XAbstractFeatureCall", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XAbstractFeatureCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XAbstractFeatureCall"):
                opp_val = getattr(value, "xtend_XAbstractFeatureCall", None)
                setattr(value, "xtend_XAbstractFeatureCall", self)

    def getQualifiedName(self, xtend_innerClassDelimiter) :
        # TODO: Implement getQualifiedName method
        pass

    def getIdentifier(self) :
        # TODO: Implement getIdentifier method
        pass

    def getSimpleName(self) :
        # TODO: Implement getSimpleName method
        pass

class JvmIdentifiableElement:

    pass
class xtend_JvmFormalParameter(JvmIdentifiableElement, JvmAnnotationTarget):

    def __init__(self, name: str, xtend_JvmFormalParameter140: "xtend_XForLoopExpression" = None, xtend_JvmFormalParameter166: "xtend_XCatchClause" = None, xtend_JvmFormalParameter: "xtend_XClosure" = None, xtend_JvmFormalParameter120: "xtend_XClosure" = None, xtend_JvmFormalParameter224: "xtend_JvmTypeReference" = None, xtend_JvmFormalParameter215: "xtend_JvmExecutable" = None):
        self.name = name
        self.xtend_JvmFormalParameter140 = xtend_JvmFormalParameter140
        self.xtend_JvmFormalParameter166 = xtend_JvmFormalParameter166
        self.xtend_JvmFormalParameter = xtend_JvmFormalParameter
        self.xtend_JvmFormalParameter120 = xtend_JvmFormalParameter120
        self.xtend_JvmFormalParameter224 = xtend_JvmFormalParameter224
        self.xtend_JvmFormalParameter215 = xtend_JvmFormalParameter215
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xtend_JvmFormalParameter215(self):
        return self.__xtend_JvmFormalParameter215

    @xtend_JvmFormalParameter215.setter
    def xtend_JvmFormalParameter215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmFormalParameter__xtend_JvmFormalParameter215", None)
        self.__xtend_JvmFormalParameter215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmExecutable"):
                opp_val = getattr(old_value, "xtend_JvmExecutable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmExecutable"):
                opp_val = getattr(value, "xtend_JvmExecutable", None)
                if opp_val is None:
                    setattr(value, "xtend_JvmExecutable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmFormalParameter224(self):
        return self.__xtend_JvmFormalParameter224

    @xtend_JvmFormalParameter224.setter
    def xtend_JvmFormalParameter224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmFormalParameter__xtend_JvmFormalParameter224", None)
        self.__xtend_JvmFormalParameter224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeReference225"):
                opp_val = getattr(old_value, "xtend_JvmTypeReference225", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeReference225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeReference225"):
                opp_val = getattr(value, "xtend_JvmTypeReference225", None)
                setattr(value, "xtend_JvmTypeReference225", self)

    @property
    def xtend_JvmFormalParameter166(self):
        return self.__xtend_JvmFormalParameter166

    @xtend_JvmFormalParameter166.setter
    def xtend_JvmFormalParameter166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmFormalParameter__xtend_JvmFormalParameter166", None)
        self.__xtend_JvmFormalParameter166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XCatchClause165"):
                opp_val = getattr(old_value, "xtend_XCatchClause165", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XCatchClause165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XCatchClause165"):
                opp_val = getattr(value, "xtend_XCatchClause165", None)
                setattr(value, "xtend_XCatchClause165", self)

    @property
    def xtend_JvmFormalParameter(self):
        return self.__xtend_JvmFormalParameter

    @xtend_JvmFormalParameter.setter
    def xtend_JvmFormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmFormalParameter__xtend_JvmFormalParameter", None)
        self.__xtend_JvmFormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XClosure"):
                opp_val = getattr(old_value, "xtend_XClosure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XClosure"):
                opp_val = getattr(value, "xtend_XClosure", None)
                if opp_val is None:
                    setattr(value, "xtend_XClosure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmFormalParameter120(self):
        return self.__xtend_JvmFormalParameter120

    @xtend_JvmFormalParameter120.setter
    def xtend_JvmFormalParameter120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmFormalParameter__xtend_JvmFormalParameter120", None)
        self.__xtend_JvmFormalParameter120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XClosure119"):
                opp_val = getattr(old_value, "xtend_XClosure119", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XClosure119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XClosure119"):
                opp_val = getattr(value, "xtend_XClosure119", None)
                setattr(value, "xtend_XClosure119", self)

    @property
    def xtend_JvmFormalParameter140(self):
        return self.__xtend_JvmFormalParameter140

    @xtend_JvmFormalParameter140.setter
    def xtend_JvmFormalParameter140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmFormalParameter__xtend_JvmFormalParameter140", None)
        self.__xtend_JvmFormalParameter140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XForLoopExpression139"):
                opp_val = getattr(old_value, "xtend_XForLoopExpression139", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XForLoopExpression139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XForLoopExpression139"):
                opp_val = getattr(value, "xtend_XForLoopExpression139", None)
                setattr(value, "xtend_XForLoopExpression139", self)

class xtend_XCasePart(JvmIdentifiableElement):

    pass
class xtend_JvmType(JvmIdentifiableElement):

    pass
class xtend_JvmMember(JvmIdentifiableElement, JvmAnnotationTarget):

    def __init__(self, visibility: str, simpleName: str, identifier: str, JvmMember: "xtend_JvmDeclaredType" = None, members211: "xtend_JvmDeclaredType" = None):
        self.visibility = visibility
        self.simpleName = simpleName
        self.identifier = identifier
        self.JvmMember = JvmMember
        self.members211 = members211
        
        pass
    @property
    def simpleName(self):
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName


    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def JvmMember(self):
        return self.__JvmMember

    @JvmMember.setter
    def JvmMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmMember__JvmMember", None)
        self.__JvmMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declaringType193"):
                opp_val = getattr(old_value, "declaringType193", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declaringType193"):
                opp_val = getattr(value, "declaringType193", None)
                if opp_val is None:
                    setattr(value, "declaringType193", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def members211(self):
        return self.__members211

    @members211.setter
    def members211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmMember__members211", None)
        self.__members211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmDeclaredType"):
                opp_val = getattr(old_value, "JvmDeclaredType", None)
                if opp_val == self:
                    setattr(old_value, "JvmDeclaredType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmDeclaredType"):
                opp_val = getattr(value, "JvmDeclaredType", None)
                setattr(value, "JvmDeclaredType", self)

    def internalSetIdentifier(self, xtend_identifier):
        # TODO: Implement internalSetIdentifier method
        pass

class xtend_RichStringElseIf:

    pass
class XExpression:

    pass
class xtend_XConstructorCall(XExpression):

    def __init__(self, invalidFeatureIssueCode: str, validFeature: bool, xtend_XConstructorCall186: "xtend_AnonymousClass" = None, xtend_XConstructorCall: "xtend_JvmConstructor" = None, xtend_XConstructorCall109: set["xtend_XExpression"] = None, xtend_XConstructorCall112: set["xtend_JvmTypeReference"] = None):
        self.invalidFeatureIssueCode = invalidFeatureIssueCode
        self.validFeature = validFeature
        self.xtend_XConstructorCall186 = xtend_XConstructorCall186
        self.xtend_XConstructorCall = xtend_XConstructorCall
        self.xtend_XConstructorCall109 = xtend_XConstructorCall109 if xtend_XConstructorCall109 is not None else set()
        self.xtend_XConstructorCall112 = xtend_XConstructorCall112 if xtend_XConstructorCall112 is not None else set()
        
        pass
    @property
    def validFeature(self):
        return self.__validFeature

    @validFeature.setter
    def validFeature(self, validFeature: bool):
        self.__validFeature = validFeature


    @property
    def invalidFeatureIssueCode(self):
        return self.__invalidFeatureIssueCode

    @invalidFeatureIssueCode.setter
    def invalidFeatureIssueCode(self, invalidFeatureIssueCode: str):
        self.__invalidFeatureIssueCode = invalidFeatureIssueCode


    @property
    def xtend_XConstructorCall(self):
        return self.__xtend_XConstructorCall

    @xtend_XConstructorCall.setter
    def xtend_XConstructorCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XConstructorCall__xtend_XConstructorCall", None)
        self.__xtend_XConstructorCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmConstructor"):
                opp_val = getattr(old_value, "xtend_JvmConstructor", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmConstructor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmConstructor"):
                opp_val = getattr(value, "xtend_JvmConstructor", None)
                setattr(value, "xtend_JvmConstructor", self)

    @property
    def xtend_XConstructorCall109(self):
        return self.__xtend_XConstructorCall109

    @xtend_XConstructorCall109.setter
    def xtend_XConstructorCall109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XConstructorCall__xtend_XConstructorCall109", None)
        self.__xtend_XConstructorCall109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_XExpression110"):
                    opp_val = getattr(item, "xtend_XExpression110", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_XExpression110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_XExpression110"):
                    opp_val = getattr(item, "xtend_XExpression110", None)
                    
                    setattr(item, "xtend_XExpression110", self)
                    

    @property
    def xtend_XConstructorCall186(self):
        return self.__xtend_XConstructorCall186

    @xtend_XConstructorCall186.setter
    def xtend_XConstructorCall186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XConstructorCall__xtend_XConstructorCall186", None)
        self.__xtend_XConstructorCall186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_AnonymousClass"):
                opp_val = getattr(old_value, "xtend_AnonymousClass", None)
                if opp_val == self:
                    setattr(old_value, "xtend_AnonymousClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_AnonymousClass"):
                opp_val = getattr(value, "xtend_AnonymousClass", None)
                setattr(value, "xtend_AnonymousClass", self)

    @property
    def xtend_XConstructorCall112(self):
        return self.__xtend_XConstructorCall112

    @xtend_XConstructorCall112.setter
    def xtend_XConstructorCall112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XConstructorCall__xtend_XConstructorCall112", None)
        self.__xtend_XConstructorCall112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmTypeReference113"):
                    opp_val = getattr(item, "xtend_JvmTypeReference113", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmTypeReference113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmTypeReference113"):
                    opp_val = getattr(item, "xtend_JvmTypeReference113", None)
                    
                    setattr(item, "xtend_JvmTypeReference113", self)
                    

class xtend_XReturnExpression(XExpression):

    pass
class xtend_XThrowExpression(XExpression):

    pass
class xtend_XTypeLiteral(XExpression):

    pass
class xtend_XAbstractFeatureCall(XExpression):

    def __init__(self, invalidFeatureIssueCode: str, validFeature: bool, xtend_XAbstractFeatureCall93: "xtend_XExpression" = None, xtend_XAbstractFeatureCall96: set["xtend_JvmTypeReference"] = None, xtend_XAbstractFeatureCall: "xtend_JvmIdentifiableElement" = None, xtend_XAbstractFeatureCall87: set["xtend_JvmTypeReference"] = None, xtend_XAbstractFeatureCall90: "xtend_XExpression" = None):
        self.invalidFeatureIssueCode = invalidFeatureIssueCode
        self.validFeature = validFeature
        self.xtend_XAbstractFeatureCall93 = xtend_XAbstractFeatureCall93
        self.xtend_XAbstractFeatureCall96 = xtend_XAbstractFeatureCall96 if xtend_XAbstractFeatureCall96 is not None else set()
        self.xtend_XAbstractFeatureCall = xtend_XAbstractFeatureCall
        self.xtend_XAbstractFeatureCall87 = xtend_XAbstractFeatureCall87 if xtend_XAbstractFeatureCall87 is not None else set()
        self.xtend_XAbstractFeatureCall90 = xtend_XAbstractFeatureCall90
        
        pass
    @property
    def validFeature(self):
        return self.__validFeature

    @validFeature.setter
    def validFeature(self, validFeature: bool):
        self.__validFeature = validFeature


    @property
    def invalidFeatureIssueCode(self):
        return self.__invalidFeatureIssueCode

    @invalidFeatureIssueCode.setter
    def invalidFeatureIssueCode(self, invalidFeatureIssueCode: str):
        self.__invalidFeatureIssueCode = invalidFeatureIssueCode


    @property
    def xtend_XAbstractFeatureCall93(self):
        return self.__xtend_XAbstractFeatureCall93

    @xtend_XAbstractFeatureCall93.setter
    def xtend_XAbstractFeatureCall93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XAbstractFeatureCall__xtend_XAbstractFeatureCall93", None)
        self.__xtend_XAbstractFeatureCall93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XExpression94"):
                opp_val = getattr(old_value, "xtend_XExpression94", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XExpression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XExpression94"):
                opp_val = getattr(value, "xtend_XExpression94", None)
                setattr(value, "xtend_XExpression94", self)

    @property
    def xtend_XAbstractFeatureCall90(self):
        return self.__xtend_XAbstractFeatureCall90

    @xtend_XAbstractFeatureCall90.setter
    def xtend_XAbstractFeatureCall90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XAbstractFeatureCall__xtend_XAbstractFeatureCall90", None)
        self.__xtend_XAbstractFeatureCall90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XExpression91"):
                opp_val = getattr(old_value, "xtend_XExpression91", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XExpression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XExpression91"):
                opp_val = getattr(value, "xtend_XExpression91", None)
                setattr(value, "xtend_XExpression91", self)

    @property
    def xtend_XAbstractFeatureCall87(self):
        return self.__xtend_XAbstractFeatureCall87

    @xtend_XAbstractFeatureCall87.setter
    def xtend_XAbstractFeatureCall87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XAbstractFeatureCall__xtend_XAbstractFeatureCall87", None)
        self.__xtend_XAbstractFeatureCall87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmTypeReference88"):
                    opp_val = getattr(item, "xtend_JvmTypeReference88", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmTypeReference88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmTypeReference88"):
                    opp_val = getattr(item, "xtend_JvmTypeReference88", None)
                    
                    setattr(item, "xtend_JvmTypeReference88", self)
                    

    @property
    def xtend_XAbstractFeatureCall(self):
        return self.__xtend_XAbstractFeatureCall

    @xtend_XAbstractFeatureCall.setter
    def xtend_XAbstractFeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XAbstractFeatureCall__xtend_XAbstractFeatureCall", None)
        self.__xtend_XAbstractFeatureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmIdentifiableElement"):
                opp_val = getattr(old_value, "xtend_JvmIdentifiableElement", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmIdentifiableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmIdentifiableElement"):
                opp_val = getattr(value, "xtend_JvmIdentifiableElement", None)
                setattr(value, "xtend_JvmIdentifiableElement", self)

    @property
    def xtend_XAbstractFeatureCall96(self):
        return self.__xtend_XAbstractFeatureCall96

    @xtend_XAbstractFeatureCall96.setter
    def xtend_XAbstractFeatureCall96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XAbstractFeatureCall__xtend_XAbstractFeatureCall96", None)
        self.__xtend_XAbstractFeatureCall96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmTypeReference97"):
                    opp_val = getattr(item, "xtend_JvmTypeReference97", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmTypeReference97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmTypeReference97"):
                    opp_val = getattr(item, "xtend_JvmTypeReference97", None)
                    
                    setattr(item, "xtend_JvmTypeReference97", self)
                    

    def getConcreteSyntaxFeatureName(self) :
        # TODO: Implement getConcreteSyntaxFeatureName method
        pass

    def getExplicitArguments(self) :
        # TODO: Implement getExplicitArguments method
        pass

    def isExplicitOperationCallOrBuilderSyntax(self) :
        # TODO: Implement isExplicitOperationCallOrBuilderSyntax method
        pass

class xtend_XAbstractWhileExpression(XExpression):

    pass
class xtend_XSwitchExpression(JvmIdentifiableElement, XExpression):

    def __init__(self, localVarName: str, xtend_XSwitchExpression65: set["xtend_XCasePart"] = None, xtend_XSwitchExpression67: "xtend_XExpression" = None, xtend_XSwitchExpression: "xtend_XExpression" = None):
        self.localVarName = localVarName
        self.xtend_XSwitchExpression65 = xtend_XSwitchExpression65 if xtend_XSwitchExpression65 is not None else set()
        self.xtend_XSwitchExpression67 = xtend_XSwitchExpression67
        self.xtend_XSwitchExpression = xtend_XSwitchExpression
        
        pass
    @property
    def localVarName(self):
        return self.__localVarName

    @localVarName.setter
    def localVarName(self, localVarName: str):
        self.__localVarName = localVarName


    @property
    def xtend_XSwitchExpression(self):
        return self.__xtend_XSwitchExpression

    @xtend_XSwitchExpression.setter
    def xtend_XSwitchExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XSwitchExpression__xtend_XSwitchExpression", None)
        self.__xtend_XSwitchExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XExpression63"):
                opp_val = getattr(old_value, "xtend_XExpression63", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XExpression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XExpression63"):
                opp_val = getattr(value, "xtend_XExpression63", None)
                setattr(value, "xtend_XExpression63", self)

    @property
    def xtend_XSwitchExpression65(self):
        return self.__xtend_XSwitchExpression65

    @xtend_XSwitchExpression65.setter
    def xtend_XSwitchExpression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XSwitchExpression__xtend_XSwitchExpression65", None)
        self.__xtend_XSwitchExpression65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_XCasePart"):
                    opp_val = getattr(item, "xtend_XCasePart", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_XCasePart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_XCasePart"):
                    opp_val = getattr(item, "xtend_XCasePart", None)
                    
                    setattr(item, "xtend_XCasePart", self)
                    

    @property
    def xtend_XSwitchExpression67(self):
        return self.__xtend_XSwitchExpression67

    @xtend_XSwitchExpression67.setter
    def xtend_XSwitchExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XSwitchExpression__xtend_XSwitchExpression67", None)
        self.__xtend_XSwitchExpression67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XExpression68"):
                opp_val = getattr(old_value, "xtend_XExpression68", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XExpression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XExpression68"):
                opp_val = getattr(value, "xtend_XExpression68", None)
                setattr(value, "xtend_XExpression68", self)

class xtend_XNumberLiteral(XExpression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class xtend_XNullLiteral(XExpression):

    pass
class xtend_XInstanceOfExpression(XExpression):

    pass
class xtend_XForLoopExpression(XExpression):

    pass
class xtend_XBlockExpression(XExpression):

    pass
class xtend_XStringLiteral(XExpression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class xtend_XIfExpression(XExpression):

    pass
class xtend_XCastedExpression(XExpression):

    pass
class xtend_XVariableDeclaration(JvmIdentifiableElement, XExpression):

    def __init__(self, name: str, writeable: bool, xtend_XVariableDeclaration: "xtend_JvmTypeReference" = None, xtend_XVariableDeclaration83: "xtend_XExpression" = None):
        self.name = name
        self.writeable = writeable
        self.xtend_XVariableDeclaration = xtend_XVariableDeclaration
        self.xtend_XVariableDeclaration83 = xtend_XVariableDeclaration83
        
        pass
    @property
    def writeable(self):
        return self.__writeable

    @writeable.setter
    def writeable(self, writeable: bool):
        self.__writeable = writeable


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xtend_XVariableDeclaration83(self):
        return self.__xtend_XVariableDeclaration83

    @xtend_XVariableDeclaration83.setter
    def xtend_XVariableDeclaration83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XVariableDeclaration__xtend_XVariableDeclaration83", None)
        self.__xtend_XVariableDeclaration83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XExpression84"):
                opp_val = getattr(old_value, "xtend_XExpression84", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XExpression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XExpression84"):
                opp_val = getattr(value, "xtend_XExpression84", None)
                setattr(value, "xtend_XExpression84", self)

    @property
    def xtend_XVariableDeclaration(self):
        return self.__xtend_XVariableDeclaration

    @xtend_XVariableDeclaration.setter
    def xtend_XVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XVariableDeclaration__xtend_XVariableDeclaration", None)
        self.__xtend_XVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeReference81"):
                opp_val = getattr(old_value, "xtend_JvmTypeReference81", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeReference81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeReference81"):
                opp_val = getattr(value, "xtend_JvmTypeReference81", None)
                setattr(value, "xtend_JvmTypeReference81", self)

class xtend_XClosure(XExpression):

    def __init__(self, explicitSyntax: bool, xtend_XClosure119: "xtend_JvmFormalParameter" = None, xtend_XClosure: set["xtend_JvmFormalParameter"] = None, xtend_XClosure116: "xtend_XExpression" = None):
        self.explicitSyntax = explicitSyntax
        self.xtend_XClosure119 = xtend_XClosure119
        self.xtend_XClosure = xtend_XClosure if xtend_XClosure is not None else set()
        self.xtend_XClosure116 = xtend_XClosure116
        
        pass
    @property
    def explicitSyntax(self):
        return self.__explicitSyntax

    @explicitSyntax.setter
    def explicitSyntax(self, explicitSyntax: bool):
        self.__explicitSyntax = explicitSyntax


    @property
    def xtend_XClosure116(self):
        return self.__xtend_XClosure116

    @xtend_XClosure116.setter
    def xtend_XClosure116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XClosure__xtend_XClosure116", None)
        self.__xtend_XClosure116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XExpression117"):
                opp_val = getattr(old_value, "xtend_XExpression117", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XExpression117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XExpression117"):
                opp_val = getattr(value, "xtend_XExpression117", None)
                setattr(value, "xtend_XExpression117", self)

    @property
    def xtend_XClosure(self):
        return self.__xtend_XClosure

    @xtend_XClosure.setter
    def xtend_XClosure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XClosure__xtend_XClosure", None)
        self.__xtend_XClosure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmFormalParameter"):
                    opp_val = getattr(item, "xtend_JvmFormalParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmFormalParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmFormalParameter"):
                    opp_val = getattr(item, "xtend_JvmFormalParameter", None)
                    
                    setattr(item, "xtend_JvmFormalParameter", self)
                    

    @property
    def xtend_XClosure119(self):
        return self.__xtend_XClosure119

    @xtend_XClosure119.setter
    def xtend_XClosure119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XClosure__xtend_XClosure119", None)
        self.__xtend_XClosure119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmFormalParameter120"):
                opp_val = getattr(old_value, "xtend_JvmFormalParameter120", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmFormalParameter120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmFormalParameter120"):
                opp_val = getattr(value, "xtend_JvmFormalParameter120", None)
                setattr(value, "xtend_JvmFormalParameter120", self)

    def getFormalParameters(self) :
        # TODO: Implement getFormalParameters method
        pass

class xtend_XTryCatchFinallyExpression(XExpression):

    pass
class xtend_XBooleanLiteral(XExpression):

    def __init__(self, isTrue: bool):
        self.isTrue = isTrue
        
        pass
    @property
    def isTrue(self):
        return self.__isTrue

    @isTrue.setter
    def isTrue(self, isTrue: bool):
        self.__isTrue = isTrue


class xtend_RichStringIf(XExpression):

    pass
class JvmFormalParameter:

    pass
class xtend_XtendFormalParameter(JvmFormalParameter):

    def __init__(self, extension: bool):
        self.extension = extension
        
        pass
    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension


class XVariableDeclaration:

    pass
class xtend_XtendVariableDeclaration(XVariableDeclaration):

    def __init__(self, extension: bool):
        self.extension = extension
        
        pass
    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension


class XForLoopExpression:

    pass
class xtend_RichStringForLoop(XForLoopExpression):

    pass
class XStringLiteral:

    pass
class xtend_RichStringLiteral(XStringLiteral):

    pass
class XBlockExpression:

    pass
class xtend_RichString(XBlockExpression):

    pass
class xtend_XtendConstructor(XtendExecutable):

    pass
class xtend_JvmTypeReference(ABC):

    def __init__(self, xtend_JvmTypeReference4: "xtend_XtendClass" = None, xtend_JvmTypeReference16: "xtend_XtendField" = None, xtend_JvmTypeReference: "xtend_XtendClass" = None, xtend_JvmTypeReference20: "xtend_XtendParameter" = None, xtend_JvmTypeReference50: "xtend_XtendInterface" = None, xtend_JvmTypeReference81: "xtend_XVariableDeclaration" = None, xtend_JvmTypeReference77: "xtend_XCasePart" = None, xtend_JvmTypeReference97: "xtend_XAbstractFeatureCall" = None, xtend_JvmTypeReference88: "xtend_XAbstractFeatureCall" = None, xtend_JvmTypeReference12: "xtend_XtendFunction" = None, xtend_JvmTypeReference122: "xtend_XCastedExpression" = None, xtend_JvmTypeReference148: "xtend_XInstanceOfExpression" = None, xtend_JvmTypeReference175: "xtend_XtendExecutable" = None, xtend_JvmTypeReference191: "xtend_JvmDeclaredType" = None, xtend_JvmTypeReference198: "xtend_JvmTypeConstraint" = None, xtend_JvmTypeReference113: "xtend_XConstructorCall" = None, xtend_JvmTypeReference220: "xtend_JvmOperation" = None, xtend_JvmTypeReference225: "xtend_JvmFormalParameter" = None, xtend_JvmTypeReference236: "xtend_JvmTypeAnnotationValue" = None, xtend_JvmTypeReference242: "xtend_JvmDelegateTypeReference" = None, xtend_JvmTypeReference244: "xtend_JvmSpecializedTypeReference" = None, xtend_JvmTypeReference249: "xtend_JvmCompoundTypeReference" = None, xtend_JvmTypeReference202: "xtend_JvmParameterizedTypeReference" = None, xtend_JvmTypeReference207: "xtend_JvmGenericArrayTypeReference" = None, xtend_JvmTypeReference213: "xtend_JvmField" = None, xtend_JvmTypeReference218: "xtend_JvmExecutable" = None):
        self.xtend_JvmTypeReference4 = xtend_JvmTypeReference4
        self.xtend_JvmTypeReference16 = xtend_JvmTypeReference16
        self.xtend_JvmTypeReference = xtend_JvmTypeReference
        self.xtend_JvmTypeReference20 = xtend_JvmTypeReference20
        self.xtend_JvmTypeReference50 = xtend_JvmTypeReference50
        self.xtend_JvmTypeReference81 = xtend_JvmTypeReference81
        self.xtend_JvmTypeReference77 = xtend_JvmTypeReference77
        self.xtend_JvmTypeReference97 = xtend_JvmTypeReference97
        self.xtend_JvmTypeReference88 = xtend_JvmTypeReference88
        self.xtend_JvmTypeReference12 = xtend_JvmTypeReference12
        self.xtend_JvmTypeReference122 = xtend_JvmTypeReference122
        self.xtend_JvmTypeReference148 = xtend_JvmTypeReference148
        self.xtend_JvmTypeReference175 = xtend_JvmTypeReference175
        self.xtend_JvmTypeReference191 = xtend_JvmTypeReference191
        self.xtend_JvmTypeReference198 = xtend_JvmTypeReference198
        self.xtend_JvmTypeReference113 = xtend_JvmTypeReference113
        self.xtend_JvmTypeReference220 = xtend_JvmTypeReference220
        self.xtend_JvmTypeReference225 = xtend_JvmTypeReference225
        self.xtend_JvmTypeReference236 = xtend_JvmTypeReference236
        self.xtend_JvmTypeReference242 = xtend_JvmTypeReference242
        self.xtend_JvmTypeReference244 = xtend_JvmTypeReference244
        self.xtend_JvmTypeReference249 = xtend_JvmTypeReference249
        self.xtend_JvmTypeReference202 = xtend_JvmTypeReference202
        self.xtend_JvmTypeReference207 = xtend_JvmTypeReference207
        self.xtend_JvmTypeReference213 = xtend_JvmTypeReference213
        self.xtend_JvmTypeReference218 = xtend_JvmTypeReference218
        
        pass
    @property
    def xtend_JvmTypeReference148(self):
        return self.__xtend_JvmTypeReference148

    @xtend_JvmTypeReference148.setter
    def xtend_JvmTypeReference148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference148", None)
        self.__xtend_JvmTypeReference148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XInstanceOfExpression"):
                opp_val = getattr(old_value, "xtend_XInstanceOfExpression", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XInstanceOfExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XInstanceOfExpression"):
                opp_val = getattr(value, "xtend_XInstanceOfExpression", None)
                setattr(value, "xtend_XInstanceOfExpression", self)

    @property
    def xtend_JvmTypeReference244(self):
        return self.__xtend_JvmTypeReference244

    @xtend_JvmTypeReference244.setter
    def xtend_JvmTypeReference244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference244", None)
        self.__xtend_JvmTypeReference244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmSpecializedTypeReference"):
                opp_val = getattr(old_value, "xtend_JvmSpecializedTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmSpecializedTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmSpecializedTypeReference"):
                opp_val = getattr(value, "xtend_JvmSpecializedTypeReference", None)
                setattr(value, "xtend_JvmSpecializedTypeReference", self)

    @property
    def xtend_JvmTypeReference220(self):
        return self.__xtend_JvmTypeReference220

    @xtend_JvmTypeReference220.setter
    def xtend_JvmTypeReference220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference220", None)
        self.__xtend_JvmTypeReference220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmOperation"):
                opp_val = getattr(old_value, "xtend_JvmOperation", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmOperation"):
                opp_val = getattr(value, "xtend_JvmOperation", None)
                setattr(value, "xtend_JvmOperation", self)

    @property
    def xtend_JvmTypeReference191(self):
        return self.__xtend_JvmTypeReference191

    @xtend_JvmTypeReference191.setter
    def xtend_JvmTypeReference191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference191", None)
        self.__xtend_JvmTypeReference191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmDeclaredType190"):
                opp_val = getattr(old_value, "xtend_JvmDeclaredType190", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmDeclaredType190"):
                opp_val = getattr(value, "xtend_JvmDeclaredType190", None)
                if opp_val is None:
                    setattr(value, "xtend_JvmDeclaredType190", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference225(self):
        return self.__xtend_JvmTypeReference225

    @xtend_JvmTypeReference225.setter
    def xtend_JvmTypeReference225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference225", None)
        self.__xtend_JvmTypeReference225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmFormalParameter224"):
                opp_val = getattr(old_value, "xtend_JvmFormalParameter224", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmFormalParameter224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmFormalParameter224"):
                opp_val = getattr(value, "xtend_JvmFormalParameter224", None)
                setattr(value, "xtend_JvmFormalParameter224", self)

    @property
    def xtend_JvmTypeReference97(self):
        return self.__xtend_JvmTypeReference97

    @xtend_JvmTypeReference97.setter
    def xtend_JvmTypeReference97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference97", None)
        self.__xtend_JvmTypeReference97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XAbstractFeatureCall96"):
                opp_val = getattr(old_value, "xtend_XAbstractFeatureCall96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XAbstractFeatureCall96"):
                opp_val = getattr(value, "xtend_XAbstractFeatureCall96", None)
                if opp_val is None:
                    setattr(value, "xtend_XAbstractFeatureCall96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference242(self):
        return self.__xtend_JvmTypeReference242

    @xtend_JvmTypeReference242.setter
    def xtend_JvmTypeReference242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference242", None)
        self.__xtend_JvmTypeReference242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmDelegateTypeReference"):
                opp_val = getattr(old_value, "xtend_JvmDelegateTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmDelegateTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmDelegateTypeReference"):
                opp_val = getattr(value, "xtend_JvmDelegateTypeReference", None)
                setattr(value, "xtend_JvmDelegateTypeReference", self)

    @property
    def xtend_JvmTypeReference249(self):
        return self.__xtend_JvmTypeReference249

    @xtend_JvmTypeReference249.setter
    def xtend_JvmTypeReference249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference249", None)
        self.__xtend_JvmTypeReference249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmCompoundTypeReference248"):
                opp_val = getattr(old_value, "xtend_JvmCompoundTypeReference248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmCompoundTypeReference248"):
                opp_val = getattr(value, "xtend_JvmCompoundTypeReference248", None)
                if opp_val is None:
                    setattr(value, "xtend_JvmCompoundTypeReference248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference88(self):
        return self.__xtend_JvmTypeReference88

    @xtend_JvmTypeReference88.setter
    def xtend_JvmTypeReference88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference88", None)
        self.__xtend_JvmTypeReference88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XAbstractFeatureCall87"):
                opp_val = getattr(old_value, "xtend_XAbstractFeatureCall87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XAbstractFeatureCall87"):
                opp_val = getattr(value, "xtend_XAbstractFeatureCall87", None)
                if opp_val is None:
                    setattr(value, "xtend_XAbstractFeatureCall87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference218(self):
        return self.__xtend_JvmTypeReference218

    @xtend_JvmTypeReference218.setter
    def xtend_JvmTypeReference218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference218", None)
        self.__xtend_JvmTypeReference218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmExecutable217"):
                opp_val = getattr(old_value, "xtend_JvmExecutable217", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmExecutable217"):
                opp_val = getattr(value, "xtend_JvmExecutable217", None)
                if opp_val is None:
                    setattr(value, "xtend_JvmExecutable217", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference16(self):
        return self.__xtend_JvmTypeReference16

    @xtend_JvmTypeReference16.setter
    def xtend_JvmTypeReference16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference16", None)
        self.__xtend_JvmTypeReference16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendField"):
                opp_val = getattr(old_value, "xtend_XtendField", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XtendField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendField"):
                opp_val = getattr(value, "xtend_XtendField", None)
                setattr(value, "xtend_XtendField", self)

    @property
    def xtend_JvmTypeReference12(self):
        return self.__xtend_JvmTypeReference12

    @xtend_JvmTypeReference12.setter
    def xtend_JvmTypeReference12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference12", None)
        self.__xtend_JvmTypeReference12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendFunction"):
                opp_val = getattr(old_value, "xtend_XtendFunction", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XtendFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendFunction"):
                opp_val = getattr(value, "xtend_XtendFunction", None)
                setattr(value, "xtend_XtendFunction", self)

    @property
    def xtend_JvmTypeReference(self):
        return self.__xtend_JvmTypeReference

    @xtend_JvmTypeReference.setter
    def xtend_JvmTypeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference", None)
        self.__xtend_JvmTypeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendClass"):
                opp_val = getattr(old_value, "xtend_XtendClass", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XtendClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendClass"):
                opp_val = getattr(value, "xtend_XtendClass", None)
                setattr(value, "xtend_XtendClass", self)

    @property
    def xtend_JvmTypeReference113(self):
        return self.__xtend_JvmTypeReference113

    @xtend_JvmTypeReference113.setter
    def xtend_JvmTypeReference113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference113", None)
        self.__xtend_JvmTypeReference113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XConstructorCall112"):
                opp_val = getattr(old_value, "xtend_XConstructorCall112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XConstructorCall112"):
                opp_val = getattr(value, "xtend_XConstructorCall112", None)
                if opp_val is None:
                    setattr(value, "xtend_XConstructorCall112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference122(self):
        return self.__xtend_JvmTypeReference122

    @xtend_JvmTypeReference122.setter
    def xtend_JvmTypeReference122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference122", None)
        self.__xtend_JvmTypeReference122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XCastedExpression"):
                opp_val = getattr(old_value, "xtend_XCastedExpression", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XCastedExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XCastedExpression"):
                opp_val = getattr(value, "xtend_XCastedExpression", None)
                setattr(value, "xtend_XCastedExpression", self)

    @property
    def xtend_JvmTypeReference77(self):
        return self.__xtend_JvmTypeReference77

    @xtend_JvmTypeReference77.setter
    def xtend_JvmTypeReference77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference77", None)
        self.__xtend_JvmTypeReference77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XCasePart76"):
                opp_val = getattr(old_value, "xtend_XCasePart76", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XCasePart76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XCasePart76"):
                opp_val = getattr(value, "xtend_XCasePart76", None)
                setattr(value, "xtend_XCasePart76", self)

    @property
    def xtend_JvmTypeReference207(self):
        return self.__xtend_JvmTypeReference207

    @xtend_JvmTypeReference207.setter
    def xtend_JvmTypeReference207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference207", None)
        self.__xtend_JvmTypeReference207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmGenericArrayTypeReference"):
                opp_val = getattr(old_value, "xtend_JvmGenericArrayTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmGenericArrayTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmGenericArrayTypeReference"):
                opp_val = getattr(value, "xtend_JvmGenericArrayTypeReference", None)
                setattr(value, "xtend_JvmGenericArrayTypeReference", self)

    @property
    def xtend_JvmTypeReference50(self):
        return self.__xtend_JvmTypeReference50

    @xtend_JvmTypeReference50.setter
    def xtend_JvmTypeReference50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference50", None)
        self.__xtend_JvmTypeReference50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendInterface"):
                opp_val = getattr(old_value, "xtend_XtendInterface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendInterface"):
                opp_val = getattr(value, "xtend_XtendInterface", None)
                if opp_val is None:
                    setattr(value, "xtend_XtendInterface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference236(self):
        return self.__xtend_JvmTypeReference236

    @xtend_JvmTypeReference236.setter
    def xtend_JvmTypeReference236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference236", None)
        self.__xtend_JvmTypeReference236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeAnnotationValue"):
                opp_val = getattr(old_value, "xtend_JvmTypeAnnotationValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeAnnotationValue"):
                opp_val = getattr(value, "xtend_JvmTypeAnnotationValue", None)
                if opp_val is None:
                    setattr(value, "xtend_JvmTypeAnnotationValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference198(self):
        return self.__xtend_JvmTypeReference198

    @xtend_JvmTypeReference198.setter
    def xtend_JvmTypeReference198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference198", None)
        self.__xtend_JvmTypeReference198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeConstraint"):
                opp_val = getattr(old_value, "xtend_JvmTypeConstraint", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeConstraint"):
                opp_val = getattr(value, "xtend_JvmTypeConstraint", None)
                setattr(value, "xtend_JvmTypeConstraint", self)

    @property
    def xtend_JvmTypeReference202(self):
        return self.__xtend_JvmTypeReference202

    @xtend_JvmTypeReference202.setter
    def xtend_JvmTypeReference202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference202", None)
        self.__xtend_JvmTypeReference202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmParameterizedTypeReference"):
                opp_val = getattr(old_value, "xtend_JvmParameterizedTypeReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmParameterizedTypeReference"):
                opp_val = getattr(value, "xtend_JvmParameterizedTypeReference", None)
                if opp_val is None:
                    setattr(value, "xtend_JvmParameterizedTypeReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference213(self):
        return self.__xtend_JvmTypeReference213

    @xtend_JvmTypeReference213.setter
    def xtend_JvmTypeReference213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference213", None)
        self.__xtend_JvmTypeReference213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmField"):
                opp_val = getattr(old_value, "xtend_JvmField", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmField"):
                opp_val = getattr(value, "xtend_JvmField", None)
                setattr(value, "xtend_JvmField", self)

    @property
    def xtend_JvmTypeReference175(self):
        return self.__xtend_JvmTypeReference175

    @xtend_JvmTypeReference175.setter
    def xtend_JvmTypeReference175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference175", None)
        self.__xtend_JvmTypeReference175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendExecutable"):
                opp_val = getattr(old_value, "xtend_XtendExecutable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendExecutable"):
                opp_val = getattr(value, "xtend_XtendExecutable", None)
                if opp_val is None:
                    setattr(value, "xtend_XtendExecutable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference81(self):
        return self.__xtend_JvmTypeReference81

    @xtend_JvmTypeReference81.setter
    def xtend_JvmTypeReference81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference81", None)
        self.__xtend_JvmTypeReference81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XVariableDeclaration"):
                opp_val = getattr(old_value, "xtend_XVariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XVariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XVariableDeclaration"):
                opp_val = getattr(value, "xtend_XVariableDeclaration", None)
                setattr(value, "xtend_XVariableDeclaration", self)

    @property
    def xtend_JvmTypeReference4(self):
        return self.__xtend_JvmTypeReference4

    @xtend_JvmTypeReference4.setter
    def xtend_JvmTypeReference4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference4", None)
        self.__xtend_JvmTypeReference4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendClass3"):
                opp_val = getattr(old_value, "xtend_XtendClass3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendClass3"):
                opp_val = getattr(value, "xtend_XtendClass3", None)
                if opp_val is None:
                    setattr(value, "xtend_XtendClass3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xtend_JvmTypeReference20(self):
        return self.__xtend_JvmTypeReference20

    @xtend_JvmTypeReference20.setter
    def xtend_JvmTypeReference20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_JvmTypeReference__xtend_JvmTypeReference20", None)
        self.__xtend_JvmTypeReference20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendParameter"):
                opp_val = getattr(old_value, "xtend_XtendParameter", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XtendParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendParameter"):
                opp_val = getattr(value, "xtend_XtendParameter", None)
                setattr(value, "xtend_XtendParameter", self)

    def getIdentifier(self) :
        # TODO: Implement getIdentifier method
        pass

    def getType(self) :
        # TODO: Implement getType method
        pass

    def getSimpleName(self) :
        # TODO: Implement getSimpleName method
        pass

    def accept1(self, xtend_visitor):
        # TODO: Implement accept1 method
        pass

    def accept2(self, xtend_visitor, xtend_parameter):
        # TODO: Implement accept2 method
        pass

    def getQualifiedName(self, xtend_innerClassDelimiter) :
        # TODO: Implement getQualifiedName method
        pass

class XtendMember:

    pass
class xtend_XtendExecutable(XtendMember):

    pass
class xtend_XtendTypeDeclaration(XtendMember):

    def __init__(self, name: str, xtend_XtendTypeDeclaration: "xtend_XtendFile" = None, declaringType: set["xtend_XtendMember"] = None, XtendTypeDeclaration: "xtend_XtendMember" = None):
        self.name = name
        self.xtend_XtendTypeDeclaration = xtend_XtendTypeDeclaration
        self.declaringType = declaringType if declaringType is not None else set()
        self.XtendTypeDeclaration = XtendTypeDeclaration
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def declaringType(self):
        return self.__declaringType

    @declaringType.setter
    def declaringType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendTypeDeclaration__declaringType", None)
        self.__declaringType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XtendMember"):
                    opp_val = getattr(item, "XtendMember", None)
                    
                    if opp_val == self:
                        setattr(item, "XtendMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XtendMember"):
                    opp_val = getattr(item, "XtendMember", None)
                    
                    setattr(item, "XtendMember", self)
                    

    @property
    def xtend_XtendTypeDeclaration(self):
        return self.__xtend_XtendTypeDeclaration

    @xtend_XtendTypeDeclaration.setter
    def xtend_XtendTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendTypeDeclaration__xtend_XtendTypeDeclaration", None)
        self.__xtend_XtendTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XtendFile"):
                opp_val = getattr(old_value, "xtend_XtendFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XtendFile"):
                opp_val = getattr(value, "xtend_XtendFile", None)
                if opp_val is None:
                    setattr(value, "xtend_XtendFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def XtendTypeDeclaration(self):
        return self.__XtendTypeDeclaration

    @XtendTypeDeclaration.setter
    def XtendTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendTypeDeclaration__XtendTypeDeclaration", None)
        self.__XtendTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "members"):
                opp_val = getattr(old_value, "members", None)
                if opp_val == self:
                    setattr(old_value, "members", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "members"):
                opp_val = getattr(value, "members", None)
                setattr(value, "members", self)

    def isLocal(self) :
        # TODO: Implement isLocal method
        pass

    def isAnonymous(self) :
        # TODO: Implement isAnonymous method
        pass

class xtend_XtendEnumLiteral(XtendMember):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class xtend_XtendField(XtendMember):

    def __init__(self, name: str, xtend_XtendField: "xtend_JvmTypeReference" = None, xtend_XtendField18: "xtend_XExpression" = None):
        self.name = name
        self.xtend_XtendField = xtend_XtendField
        self.xtend_XtendField18 = xtend_XtendField18
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def xtend_XtendField(self):
        return self.__xtend_XtendField

    @xtend_XtendField.setter
    def xtend_XtendField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendField__xtend_XtendField", None)
        self.__xtend_XtendField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeReference16"):
                opp_val = getattr(old_value, "xtend_JvmTypeReference16", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeReference16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeReference16"):
                opp_val = getattr(value, "xtend_JvmTypeReference16", None)
                setattr(value, "xtend_JvmTypeReference16", self)

    @property
    def xtend_XtendField18(self):
        return self.__xtend_XtendField18

    @xtend_XtendField18.setter
    def xtend_XtendField18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendField__xtend_XtendField18", None)
        self.__xtend_XtendField18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_XExpression"):
                opp_val = getattr(old_value, "xtend_XExpression", None)
                if opp_val == self:
                    setattr(old_value, "xtend_XExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_XExpression"):
                opp_val = getattr(value, "xtend_XExpression", None)
                setattr(value, "xtend_XExpression", self)

    def isExtension(self) :
        # TODO: Implement isExtension method
        pass

    def isVolatile(self) :
        # TODO: Implement isVolatile method
        pass

    def isTransient(self) :
        # TODO: Implement isTransient method
        pass

class XtendTypeDeclaration:

    pass
class xtend_XtendInterface(XtendTypeDeclaration):

    def __init__(self, xtend_XtendInterface: set["xtend_JvmTypeReference"] = None, xtend_XtendInterface52: set["xtend_JvmTypeParameter"] = None):
        self.xtend_XtendInterface = xtend_XtendInterface if xtend_XtendInterface is not None else set()
        self.xtend_XtendInterface52 = xtend_XtendInterface52 if xtend_XtendInterface52 is not None else set()
        
        pass
    @property
    def xtend_XtendInterface(self):
        return self.__xtend_XtendInterface

    @xtend_XtendInterface.setter
    def xtend_XtendInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendInterface__xtend_XtendInterface", None)
        self.__xtend_XtendInterface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmTypeReference50"):
                    opp_val = getattr(item, "xtend_JvmTypeReference50", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmTypeReference50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmTypeReference50"):
                    opp_val = getattr(item, "xtend_JvmTypeReference50", None)
                    
                    setattr(item, "xtend_JvmTypeReference50", self)
                    

    @property
    def xtend_XtendInterface52(self):
        return self.__xtend_XtendInterface52

    @xtend_XtendInterface52.setter
    def xtend_XtendInterface52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendInterface__xtend_XtendInterface52", None)
        self.__xtend_XtendInterface52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmTypeParameter53"):
                    opp_val = getattr(item, "xtend_JvmTypeParameter53", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmTypeParameter53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmTypeParameter53"):
                    opp_val = getattr(item, "xtend_JvmTypeParameter53", None)
                    
                    setattr(item, "xtend_JvmTypeParameter53", self)
                    

    def isStrictFloatingPoint(self) :
        # TODO: Implement isStrictFloatingPoint method
        pass

class xtend_AnonymousClass(XtendTypeDeclaration, XExpression):

    pass
class xtend_XtendEnum(XtendTypeDeclaration):

    pass
class xtend_XtendAnnotationType(XtendTypeDeclaration):

    pass
class xtend_XtendClass(XtendTypeDeclaration):

    def __init__(self, xtend_XtendClass3: set["xtend_JvmTypeReference"] = None, xtend_XtendClass6: set["xtend_JvmTypeParameter"] = None, xtend_XtendClass: "xtend_JvmTypeReference" = None):
        self.xtend_XtendClass3 = xtend_XtendClass3 if xtend_XtendClass3 is not None else set()
        self.xtend_XtendClass6 = xtend_XtendClass6 if xtend_XtendClass6 is not None else set()
        self.xtend_XtendClass = xtend_XtendClass
        
        pass
    @property
    def xtend_XtendClass6(self):
        return self.__xtend_XtendClass6

    @xtend_XtendClass6.setter
    def xtend_XtendClass6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendClass__xtend_XtendClass6", None)
        self.__xtend_XtendClass6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmTypeParameter"):
                    opp_val = getattr(item, "xtend_JvmTypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmTypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmTypeParameter"):
                    opp_val = getattr(item, "xtend_JvmTypeParameter", None)
                    
                    setattr(item, "xtend_JvmTypeParameter", self)
                    

    @property
    def xtend_XtendClass3(self):
        return self.__xtend_XtendClass3

    @xtend_XtendClass3.setter
    def xtend_XtendClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendClass__xtend_XtendClass3", None)
        self.__xtend_XtendClass3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xtend_JvmTypeReference4"):
                    opp_val = getattr(item, "xtend_JvmTypeReference4", None)
                    
                    if opp_val == self:
                        setattr(item, "xtend_JvmTypeReference4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xtend_JvmTypeReference4"):
                    opp_val = getattr(item, "xtend_JvmTypeReference4", None)
                    
                    setattr(item, "xtend_JvmTypeReference4", self)
                    

    @property
    def xtend_XtendClass(self):
        return self.__xtend_XtendClass

    @xtend_XtendClass.setter
    def xtend_XtendClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xtend_XtendClass__xtend_XtendClass", None)
        self.__xtend_XtendClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xtend_JvmTypeReference"):
                opp_val = getattr(old_value, "xtend_JvmTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "xtend_JvmTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xtend_JvmTypeReference"):
                opp_val = getattr(value, "xtend_JvmTypeReference", None)
                setattr(value, "xtend_JvmTypeReference", self)

    def isAbstract(self) :
        # TODO: Implement isAbstract method
        pass

    def isStrictFloatingPoint(self) :
        # TODO: Implement isStrictFloatingPoint method
        pass

from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CSIDatatypeCodes(Enum):
    CSIInteger = "CSIInteger"
    CSIString = "CSIString"
    CSIFloat = "CSIFloat"
    CSIDouble = "CSIDouble"
    CSIBoolean = "CSIBoolean"
    CSIDate = "CSIDate"
    CSIByte = "CSIByte"
    CSILong = "CSILong"
class CSIExceptionTypes(Enum):
    USER = "USER"
    SYSTEM = "SYSTEM"
    UNRECOVERABLE = "UNRECOVERABLE"


############################################
# Definition of Classes
############################################

class typedef_EnumLiteral:

    def __init__(self, name: str, value: str, typedef_EnumLiteral: "typedef_EnumVal" = None, typedef_EnumLiteral22: "typedef_TDDocumentation" = None):
        self.name = name
        self.value = value
        self.typedef_EnumLiteral = typedef_EnumLiteral
        self.typedef_EnumLiteral22 = typedef_EnumLiteral22
        
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
    def typedef_EnumLiteral(self):
        return self.__typedef_EnumLiteral

    @typedef_EnumLiteral.setter
    def typedef_EnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_EnumLiteral__typedef_EnumLiteral", None)
        self.__typedef_EnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_EnumVal20"):
                opp_val = getattr(old_value, "typedef_EnumVal20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_EnumVal20"):
                opp_val = getattr(value, "typedef_EnumVal20", None)
                if opp_val is None:
                    setattr(value, "typedef_EnumVal20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def typedef_EnumLiteral22(self):
        return self.__typedef_EnumLiteral22

    @typedef_EnumLiteral22.setter
    def typedef_EnumLiteral22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_EnumLiteral__typedef_EnumLiteral22", None)
        self.__typedef_EnumLiteral22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_TDDocumentation23"):
                opp_val = getattr(old_value, "typedef_TDDocumentation23", None)
                if opp_val == self:
                    setattr(old_value, "typedef_TDDocumentation23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_TDDocumentation23"):
                opp_val = getattr(value, "typedef_TDDocumentation23", None)
                setattr(value, "typedef_TDDocumentation23", self)

class typedef_TDAnnotationDetail:

    def __init__(self, key: str, value: str, typedef_TDAnnotationDetail: "typedef_TypeAnnotation" = None):
        self.key = key
        self.value = value
        self.typedef_TDAnnotationDetail = typedef_TDAnnotationDetail
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def typedef_TDAnnotationDetail(self):
        return self.__typedef_TDAnnotationDetail

    @typedef_TDAnnotationDetail.setter
    def typedef_TDAnnotationDetail(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_TDAnnotationDetail__typedef_TDAnnotationDetail", None)
        self.__typedef_TDAnnotationDetail = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_TypeAnnotation15"):
                opp_val = getattr(old_value, "typedef_TypeAnnotation15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_TypeAnnotation15"):
                opp_val = getattr(value, "typedef_TypeAnnotation15", None)
                if opp_val is None:
                    setattr(value, "typedef_TypeAnnotation15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class typedef_TypeLanguageBinding:

    def __init__(self, lang: str, langSpecificType: str, langSpecificNS: str, defaultInitValue: str, nullValueLiteral: str, typedef_TypeLanguageBinding: "typedef_PrimitiveType" = None):
        self.lang = lang
        self.langSpecificType = langSpecificType
        self.langSpecificNS = langSpecificNS
        self.defaultInitValue = defaultInitValue
        self.nullValueLiteral = nullValueLiteral
        self.typedef_TypeLanguageBinding = typedef_TypeLanguageBinding
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def defaultInitValue(self) -> str:
        return self.__defaultInitValue

    @defaultInitValue.setter
    def defaultInitValue(self, defaultInitValue: str):
        self.__defaultInitValue = defaultInitValue

    @property
    def nullValueLiteral(self) -> str:
        return self.__nullValueLiteral

    @nullValueLiteral.setter
    def nullValueLiteral(self, nullValueLiteral: str):
        self.__nullValueLiteral = nullValueLiteral

    @property
    def langSpecificType(self) -> str:
        return self.__langSpecificType

    @langSpecificType.setter
    def langSpecificType(self, langSpecificType: str):
        self.__langSpecificType = langSpecificType

    @property
    def langSpecificNS(self) -> str:
        return self.__langSpecificNS

    @langSpecificNS.setter
    def langSpecificNS(self, langSpecificNS: str):
        self.__langSpecificNS = langSpecificNS

    @property
    def typedef_TypeLanguageBinding(self):
        return self.__typedef_TypeLanguageBinding

    @typedef_TypeLanguageBinding.setter
    def typedef_TypeLanguageBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_TypeLanguageBinding__typedef_TypeLanguageBinding", None)
        self.__typedef_TypeLanguageBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_PrimitiveType"):
                opp_val = getattr(old_value, "typedef_PrimitiveType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_PrimitiveType"):
                opp_val = getattr(value, "typedef_PrimitiveType", None)
                if opp_val is None:
                    setattr(value, "typedef_PrimitiveType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class typedef_Feature:

    def __init__(self, name: str, typedef_Feature7: "typedef_Type" = None, typedef_Feature10: "typedef_TDDocumentation" = None, typedef_Feature: "typedef_Entity" = None):
        self.name = name
        self.typedef_Feature7 = typedef_Feature7
        self.typedef_Feature10 = typedef_Feature10
        self.typedef_Feature = typedef_Feature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typedef_Feature10(self):
        return self.__typedef_Feature10

    @typedef_Feature10.setter
    def typedef_Feature10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_Feature__typedef_Feature10", None)
        self.__typedef_Feature10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_TDDocumentation11"):
                opp_val = getattr(old_value, "typedef_TDDocumentation11", None)
                if opp_val == self:
                    setattr(old_value, "typedef_TDDocumentation11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_TDDocumentation11"):
                opp_val = getattr(value, "typedef_TDDocumentation11", None)
                setattr(value, "typedef_TDDocumentation11", self)

    @property
    def typedef_Feature7(self):
        return self.__typedef_Feature7

    @typedef_Feature7.setter
    def typedef_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_Feature__typedef_Feature7", None)
        self.__typedef_Feature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_Type8"):
                opp_val = getattr(old_value, "typedef_Type8", None)
                if opp_val == self:
                    setattr(old_value, "typedef_Type8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_Type8"):
                opp_val = getattr(value, "typedef_Type8", None)
                setattr(value, "typedef_Type8", self)

    @property
    def typedef_Feature(self):
        return self.__typedef_Feature

    @typedef_Feature.setter
    def typedef_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_Feature__typedef_Feature", None)
        self.__typedef_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_Entity"):
                opp_val = getattr(old_value, "typedef_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_Entity"):
                opp_val = getattr(value, "typedef_Entity", None)
                if opp_val is None:
                    setattr(value, "typedef_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class typedef_TypeAnnotation:

    def __init__(self, source: str, typedef_TypeAnnotation: "typedef_Type" = None, typedef_TypeAnnotation15: set["typedef_TDAnnotationDetail"] = None):
        self.source = source
        self.typedef_TypeAnnotation = typedef_TypeAnnotation
        self.typedef_TypeAnnotation15 = typedef_TypeAnnotation15 if typedef_TypeAnnotation15 is not None else set()
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def typedef_TypeAnnotation(self):
        return self.__typedef_TypeAnnotation

    @typedef_TypeAnnotation.setter
    def typedef_TypeAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_TypeAnnotation__typedef_TypeAnnotation", None)
        self.__typedef_TypeAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_Type2"):
                opp_val = getattr(old_value, "typedef_Type2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_Type2"):
                opp_val = getattr(value, "typedef_Type2", None)
                if opp_val is None:
                    setattr(value, "typedef_Type2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def typedef_TypeAnnotation15(self):
        return self.__typedef_TypeAnnotation15

    @typedef_TypeAnnotation15.setter
    def typedef_TypeAnnotation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_TypeAnnotation__typedef_TypeAnnotation15", None)
        self.__typedef_TypeAnnotation15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typedef_TDAnnotationDetail"):
                    opp_val = getattr(item, "typedef_TDAnnotationDetail", None)
                    
                    if opp_val == self:
                        setattr(item, "typedef_TDAnnotationDetail", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typedef_TDAnnotationDetail"):
                    opp_val = getattr(item, "typedef_TDAnnotationDetail", None)
                    
                    setattr(item, "typedef_TDAnnotationDetail", self)
                    

class typedef_Type(ABC):

    def __init__(self, name: str, typedef_Type2: set["typedef_TypeAnnotation"] = None, typedef_Type4: "typedef_TDDocumentation" = None, typedef_Type: "typedef_DocumentRoot" = None, typedef_Type8: "typedef_Feature" = None, typedef_Type13: "typedef_TypedArray" = None, typedef_Type18: "typedef_EnumVal" = None):
        self.name = name
        self.typedef_Type2 = typedef_Type2 if typedef_Type2 is not None else set()
        self.typedef_Type4 = typedef_Type4
        self.typedef_Type = typedef_Type
        self.typedef_Type8 = typedef_Type8
        self.typedef_Type13 = typedef_Type13
        self.typedef_Type18 = typedef_Type18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typedef_Type18(self):
        return self.__typedef_Type18

    @typedef_Type18.setter
    def typedef_Type18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_Type__typedef_Type18", None)
        self.__typedef_Type18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_EnumVal"):
                opp_val = getattr(old_value, "typedef_EnumVal", None)
                if opp_val == self:
                    setattr(old_value, "typedef_EnumVal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_EnumVal"):
                opp_val = getattr(value, "typedef_EnumVal", None)
                setattr(value, "typedef_EnumVal", self)

    @property
    def typedef_Type8(self):
        return self.__typedef_Type8

    @typedef_Type8.setter
    def typedef_Type8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_Type__typedef_Type8", None)
        self.__typedef_Type8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_Feature7"):
                opp_val = getattr(old_value, "typedef_Feature7", None)
                if opp_val == self:
                    setattr(old_value, "typedef_Feature7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_Feature7"):
                opp_val = getattr(value, "typedef_Feature7", None)
                setattr(value, "typedef_Feature7", self)

    @property
    def typedef_Type(self):
        return self.__typedef_Type

    @typedef_Type.setter
    def typedef_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_Type__typedef_Type", None)
        self.__typedef_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_DocumentRoot"):
                opp_val = getattr(old_value, "typedef_DocumentRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_DocumentRoot"):
                opp_val = getattr(value, "typedef_DocumentRoot", None)
                if opp_val is None:
                    setattr(value, "typedef_DocumentRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def typedef_Type13(self):
        return self.__typedef_Type13

    @typedef_Type13.setter
    def typedef_Type13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_Type__typedef_Type13", None)
        self.__typedef_Type13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_TypedArray"):
                opp_val = getattr(old_value, "typedef_TypedArray", None)
                if opp_val == self:
                    setattr(old_value, "typedef_TypedArray", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_TypedArray"):
                opp_val = getattr(value, "typedef_TypedArray", None)
                setattr(value, "typedef_TypedArray", self)

    @property
    def typedef_Type4(self):
        return self.__typedef_Type4

    @typedef_Type4.setter
    def typedef_Type4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_Type__typedef_Type4", None)
        self.__typedef_Type4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_TDDocumentation"):
                opp_val = getattr(old_value, "typedef_TDDocumentation", None)
                if opp_val == self:
                    setattr(old_value, "typedef_TDDocumentation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_TDDocumentation"):
                opp_val = getattr(value, "typedef_TDDocumentation", None)
                setattr(value, "typedef_TDDocumentation", self)

    @property
    def typedef_Type2(self):
        return self.__typedef_Type2

    @typedef_Type2.setter
    def typedef_Type2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_Type__typedef_Type2", None)
        self.__typedef_Type2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typedef_TypeAnnotation"):
                    opp_val = getattr(item, "typedef_TypeAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "typedef_TypeAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typedef_TypeAnnotation"):
                    opp_val = getattr(item, "typedef_TypeAnnotation", None)
                    
                    setattr(item, "typedef_TypeAnnotation", self)
                    

class typedef_DocumentRoot:

    pass
class Type:

    pass
class typedef_EnumVal(Type):

    pass
class typedef_PrimitiveType(Type):

    def __init__(self, typesetName: str, nillable: bool, typedef_PrimitiveType: set["typedef_TypeLanguageBinding"] = None):
        self.typesetName = typesetName
        self.nillable = nillable
        self.typedef_PrimitiveType = typedef_PrimitiveType if typedef_PrimitiveType is not None else set()
        
    @property
    def typesetName(self) -> str:
        return self.__typesetName

    @typesetName.setter
    def typesetName(self, typesetName: str):
        self.__typesetName = typesetName

    @property
    def nillable(self) -> bool:
        return self.__nillable

    @nillable.setter
    def nillable(self, nillable: bool):
        self.__nillable = nillable

    @property
    def typedef_PrimitiveType(self):
        return self.__typedef_PrimitiveType

    @typedef_PrimitiveType.setter
    def typedef_PrimitiveType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_PrimitiveType__typedef_PrimitiveType", None)
        self.__typedef_PrimitiveType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typedef_TypeLanguageBinding"):
                    opp_val = getattr(item, "typedef_TypeLanguageBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "typedef_TypeLanguageBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typedef_TypeLanguageBinding"):
                    opp_val = getattr(item, "typedef_TypeLanguageBinding", None)
                    
                    setattr(item, "typedef_TypeLanguageBinding", self)
                    

class typedef_Entity(Type):

    def __init__(self, versionuid: int, typedef_Entity: set["typedef_Feature"] = None):
        self.versionuid = versionuid
        self.typedef_Entity = typedef_Entity if typedef_Entity is not None else set()
        
    @property
    def versionuid(self) -> int:
        return self.__versionuid

    @versionuid.setter
    def versionuid(self, versionuid: int):
        self.__versionuid = versionuid

    @property
    def typedef_Entity(self):
        return self.__typedef_Entity

    @typedef_Entity.setter
    def typedef_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_Entity__typedef_Entity", None)
        self.__typedef_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typedef_Feature"):
                    opp_val = getattr(item, "typedef_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "typedef_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typedef_Feature"):
                    opp_val = getattr(item, "typedef_Feature", None)
                    
                    setattr(item, "typedef_Feature", self)
                    

class typedef_Exception(Type):

    def __init__(self, exceptionType: str):
        self.exceptionType = exceptionType
        
    @property
    def exceptionType(self) -> str:
        return self.__exceptionType

    @exceptionType.setter
    def exceptionType(self, exceptionType: str):
        self.__exceptionType = exceptionType

class typedef_TypedArray(Type):

    pass
class typedef_CSIDatatype(Type):

    def __init__(self, code: str, nillable: bool):
        self.code = code
        self.nillable = nillable
        
    @property
    def nillable(self) -> bool:
        return self.__nillable

    @nillable.setter
    def nillable(self, nillable: bool):
        self.__nillable = nillable

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class typedef_TDDocumentation:

    def __init__(self, doc: str, typedef_TDDocumentation: "typedef_Type" = None, typedef_TDDocumentation11: "typedef_Feature" = None, typedef_TDDocumentation23: "typedef_EnumLiteral" = None):
        self.doc = doc
        self.typedef_TDDocumentation = typedef_TDDocumentation
        self.typedef_TDDocumentation11 = typedef_TDDocumentation11
        self.typedef_TDDocumentation23 = typedef_TDDocumentation23
        
    @property
    def doc(self) -> str:
        return self.__doc

    @doc.setter
    def doc(self, doc: str):
        self.__doc = doc

    @property
    def typedef_TDDocumentation11(self):
        return self.__typedef_TDDocumentation11

    @typedef_TDDocumentation11.setter
    def typedef_TDDocumentation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_TDDocumentation__typedef_TDDocumentation11", None)
        self.__typedef_TDDocumentation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_Feature10"):
                opp_val = getattr(old_value, "typedef_Feature10", None)
                if opp_val == self:
                    setattr(old_value, "typedef_Feature10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_Feature10"):
                opp_val = getattr(value, "typedef_Feature10", None)
                setattr(value, "typedef_Feature10", self)

    @property
    def typedef_TDDocumentation(self):
        return self.__typedef_TDDocumentation

    @typedef_TDDocumentation.setter
    def typedef_TDDocumentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_TDDocumentation__typedef_TDDocumentation", None)
        self.__typedef_TDDocumentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_Type4"):
                opp_val = getattr(old_value, "typedef_Type4", None)
                if opp_val == self:
                    setattr(old_value, "typedef_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_Type4"):
                opp_val = getattr(value, "typedef_Type4", None)
                setattr(value, "typedef_Type4", self)

    @property
    def typedef_TDDocumentation23(self):
        return self.__typedef_TDDocumentation23

    @typedef_TDDocumentation23.setter
    def typedef_TDDocumentation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typedef_TDDocumentation__typedef_TDDocumentation23", None)
        self.__typedef_TDDocumentation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typedef_EnumLiteral22"):
                opp_val = getattr(old_value, "typedef_EnumLiteral22", None)
                if opp_val == self:
                    setattr(old_value, "typedef_EnumLiteral22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typedef_EnumLiteral22"):
                opp_val = getattr(value, "typedef_EnumLiteral22", None)
                setattr(value, "typedef_EnumLiteral22", self)

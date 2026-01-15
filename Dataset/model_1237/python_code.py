from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DotOrArrowEnum(Enum):
    none = "none"
    dot = "dot"
    arrow = "arrow"
class CollectionTypeIdentifierEnum(Enum):
    Set = "Set"
    Bag = "Bag"
    Sequence = "Sequence"
    Collection = "Collection"
    OrderedSet = "OrderedSet"
class MessageExpKind(Enum):
    hasSent = "hasSent"
    sent = "sent"
class SimpleTypeEnum(Enum):
    identifier = "identifier"
    self = "self"
    Integer = "Integer"
    String = "String"
    Real = "Real"
    Boolean = "Boolean"
    OclAny = "OclAny"
    OclVoid = "OclVoid"
    OclInvalid = "OclInvalid"
    OclMessage = "OclMessage"
    keyword = "keyword"
    UnlimitedNatural = "UnlimitedNatural"
class PrePostOrBodyEnum(Enum):
    pre = "pre"
    post = "post"
    body = "body"


############################################
# Definition of Classes
############################################

class FeatureCallExpCS:

    pass
class ocl_cst_OperationCallExpCS(FeatureCallExpCS):

    def __init__(self, isAtomic: str):
        self.isAtomic = isAtomic
        
    @property
    def isAtomic(self) -> str:
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic

class LoopExpCS:

    pass
class ocl_cst_IterateExpCS(LoopExpCS):

    pass
class ocl_cst_IteratorExpCS(LoopExpCS):

    pass
class CallExpCS:

    pass
class ocl_cst_FeatureCallExpCS(CallExpCS):

    pass
class ocl_cst_LoopExpCS(CallExpCS):

    pass
class cst_LiteralExpCS:

    pass
class cst_PrimitiveLiteralExpCS:

    pass
class PrimitiveLiteralExpCS:

    pass
class ocl_cst_StringLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, stringSymbol: str, unescapedStringSymbol: str):
        self.stringSymbol = stringSymbol
        self.unescapedStringSymbol = unescapedStringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

    @property
    def unescapedStringSymbol(self) -> str:
        return self.__unescapedStringSymbol

    @unescapedStringSymbol.setter
    def unescapedStringSymbol(self, unescapedStringSymbol: str):
        self.__unescapedStringSymbol = unescapedStringSymbol

class ocl_cst_RealLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class ocl_cst_UnlimitedNaturalLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, integerSymbol: str, extendedIntegerSymbol: str, longSymbol: str):
        self.integerSymbol = integerSymbol
        self.extendedIntegerSymbol = extendedIntegerSymbol
        self.longSymbol = longSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

    @property
    def extendedIntegerSymbol(self) -> str:
        return self.__extendedIntegerSymbol

    @extendedIntegerSymbol.setter
    def extendedIntegerSymbol(self, extendedIntegerSymbol: str):
        self.__extendedIntegerSymbol = extendedIntegerSymbol

    @property
    def longSymbol(self) -> str:
        return self.__longSymbol

    @longSymbol.setter
    def longSymbol(self, longSymbol: str):
        self.__longSymbol = longSymbol

class ocl_cst_IntegerLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, integerSymbol: str, extendedIntegerSymbol: str, longSymbol: str):
        self.integerSymbol = integerSymbol
        self.extendedIntegerSymbol = extendedIntegerSymbol
        self.longSymbol = longSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

    @property
    def extendedIntegerSymbol(self) -> str:
        return self.__extendedIntegerSymbol

    @extendedIntegerSymbol.setter
    def extendedIntegerSymbol(self, extendedIntegerSymbol: str):
        self.__extendedIntegerSymbol = extendedIntegerSymbol

    @property
    def longSymbol(self) -> str:
        return self.__longSymbol

    @longSymbol.setter
    def longSymbol(self, longSymbol: str):
        self.__longSymbol = longSymbol

class CollectionLiteralPartCS:

    pass
class ocl_cst_CollectionRangeCS(CollectionLiteralPartCS):

    pass
class LiteralExpCS:

    pass
class ocl_cst_TupleLiteralExpCS(LiteralExpCS):

    pass
class ocl_cst_PrimitiveLiteralExpCS(LiteralExpCS):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class ocl_cst_CollectionLiteralExpCS(LiteralExpCS):

    def __init__(self, collectionType: str, ocl_cst_CollectionLiteralExpCS: set["CollectionLiteralPartCS"] = None):
        self.collectionType = collectionType
        self.ocl_cst_CollectionLiteralExpCS = ocl_cst_CollectionLiteralExpCS if ocl_cst_CollectionLiteralExpCS is not None else set()
        
    @property
    def collectionType(self) -> str:
        return self.__collectionType

    @collectionType.setter
    def collectionType(self, collectionType: str):
        self.__collectionType = collectionType

    @property
    def ocl_cst_CollectionLiteralExpCS(self):
        return self.__ocl_cst_CollectionLiteralExpCS

    @ocl_cst_CollectionLiteralExpCS.setter
    def ocl_cst_CollectionLiteralExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_CollectionLiteralExpCS__ocl_cst_CollectionLiteralExpCS", None)
        self.__ocl_cst_CollectionLiteralExpCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CollectionLiteralPartCS"):
                    opp_val = getattr(item, "CollectionLiteralPartCS", None)
                    
                    if opp_val == self:
                        setattr(item, "CollectionLiteralPartCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CollectionLiteralPartCS"):
                    opp_val = getattr(item, "CollectionLiteralPartCS", None)
                    
                    setattr(item, "CollectionLiteralPartCS", self)
                    

class OCLMessageArgCS:

    pass
class cst_TypeCS:

    pass
class cst_SimpleNameCS:

    pass
class ocl_cst_BooleanLiteralExpCS(cst_PrimitiveLiteralExpCS, cst_SimpleNameCS):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class ocl_cst_InvalidLiteralExpCS(cst_LiteralExpCS, cst_SimpleNameCS):

    pass
class ocl_cst_NullLiteralExpCS(cst_LiteralExpCS, cst_SimpleNameCS):

    pass
class ocl_cst_CollectionTypeCS(cst_SimpleNameCS, cst_TypeCS):

    def __init__(self, collectionTypeIdentifier: str, ocl_cst_CollectionTypeCS: "TypeCS" = None):
        self.collectionTypeIdentifier = collectionTypeIdentifier
        self.ocl_cst_CollectionTypeCS = ocl_cst_CollectionTypeCS
        
    @property
    def collectionTypeIdentifier(self) -> str:
        return self.__collectionTypeIdentifier

    @collectionTypeIdentifier.setter
    def collectionTypeIdentifier(self, collectionTypeIdentifier: str):
        self.__collectionTypeIdentifier = collectionTypeIdentifier

    @property
    def ocl_cst_CollectionTypeCS(self):
        return self.__ocl_cst_CollectionTypeCS

    @ocl_cst_CollectionTypeCS.setter
    def ocl_cst_CollectionTypeCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_CollectionTypeCS__ocl_cst_CollectionTypeCS", None)
        self.__ocl_cst_CollectionTypeCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeCS69"):
                opp_val = getattr(old_value, "TypeCS69", None)
                if opp_val == self:
                    setattr(old_value, "TypeCS69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeCS69"):
                opp_val = getattr(value, "TypeCS69", None)
                setattr(value, "TypeCS69", self)

class ocl_cst_PrimitiveTypeCS(cst_SimpleNameCS, cst_TypeCS):

    pass
class DefExpressionCS:

    pass
class IsMarkedPreCS:

    pass
class VariableCS:

    pass
class PrePostOrBodyDeclCS:

    pass
class OperationCS:

    pass
class InvOrDefCS:

    pass
class ocl_cst_InvCS(InvOrDefCS):

    pass
class ocl_cst_DefCS(InvOrDefCS):

    def __init__(self, static: bool, ocl_cst_DefCS: "DefExpressionCS" = None, InvOrDefCS: "ocl_cst_ClassifierContextDeclCS"):
        self.static = static
        self.ocl_cst_DefCS = ocl_cst_DefCS
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def ocl_cst_DefCS(self):
        return self.__ocl_cst_DefCS

    @ocl_cst_DefCS.setter
    def ocl_cst_DefCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_DefCS__ocl_cst_DefCS", None)
        self.__ocl_cst_DefCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DefExpressionCS"):
                opp_val = getattr(old_value, "DefExpressionCS", None)
                if opp_val == self:
                    setattr(old_value, "DefExpressionCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DefExpressionCS"):
                opp_val = getattr(value, "DefExpressionCS", None)
                setattr(value, "DefExpressionCS", self)

class InitOrDerValueCS:

    pass
class ocl_cst_InitValueCS(InitOrDerValueCS):

    pass
class ocl_cst_DerValueCS(InitOrDerValueCS):

    pass
class OCLExpressionCS:

    pass
class ocl_cst_IfExpCS(OCLExpressionCS):

    pass
class ocl_cst_VariableExpCS(OCLExpressionCS):

    pass
class ocl_cst_MessageExpCS(OCLExpressionCS):

    def __init__(self, kind: str, ocl_cst_MessageExpCS: "OCLExpressionCS" = None, ocl_cst_MessageExpCS86: "SimpleNameCS" = None, ocl_cst_MessageExpCS89: set["OCLMessageArgCS"] = None, OCLExpressionCS49: "ocl_cst_InvCS", OCLExpressionCS101: "ocl_cst_CollectionRangeCS", OCLExpressionCS58: "ocl_cst_DefExpressionCS", OCLExpressionCS79: "ocl_cst_IfExpCS", OCLExpressionCS74: "ocl_cst_LetExpCS", OCLExpressionCS60: "ocl_cst_VariableExpCS", OCLExpressionCS114: "ocl_cst_LoopExpCS", OCLExpressionCS: "ocl_cst_InitOrDerValueCS", OCLExpressionCS97: "ocl_cst_CollectionLiteralPartCS", OCLExpressionCS76: "ocl_cst_IfExpCS", OCLExpressionCS103: "ocl_cst_CallExpCS", OCLExpressionCS84: "ocl_cst_MessageExpCS", OCLExpressionCS47: "ocl_cst_PrePostOrBodyDeclCS", OCLExpressionCS119: "ocl_cst_FeatureCallExpCS", OCLExpressionCS42: "ocl_cst_VariableCS", OCLExpressionCS82: "ocl_cst_IfExpCS", OCLExpressionCS94: "ocl_cst_OCLMessageArgCS"):
        self.kind = kind
        self.ocl_cst_MessageExpCS = ocl_cst_MessageExpCS
        self.ocl_cst_MessageExpCS86 = ocl_cst_MessageExpCS86
        self.ocl_cst_MessageExpCS89 = ocl_cst_MessageExpCS89 if ocl_cst_MessageExpCS89 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ocl_cst_MessageExpCS86(self):
        return self.__ocl_cst_MessageExpCS86

    @ocl_cst_MessageExpCS86.setter
    def ocl_cst_MessageExpCS86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_MessageExpCS__ocl_cst_MessageExpCS86", None)
        self.__ocl_cst_MessageExpCS86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS87"):
                opp_val = getattr(old_value, "SimpleNameCS87", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS87"):
                opp_val = getattr(value, "SimpleNameCS87", None)
                setattr(value, "SimpleNameCS87", self)

    @property
    def ocl_cst_MessageExpCS(self):
        return self.__ocl_cst_MessageExpCS

    @ocl_cst_MessageExpCS.setter
    def ocl_cst_MessageExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_MessageExpCS__ocl_cst_MessageExpCS", None)
        self.__ocl_cst_MessageExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS84"):
                opp_val = getattr(old_value, "OCLExpressionCS84", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS84"):
                opp_val = getattr(value, "OCLExpressionCS84", None)
                setattr(value, "OCLExpressionCS84", self)

    @property
    def ocl_cst_MessageExpCS89(self):
        return self.__ocl_cst_MessageExpCS89

    @ocl_cst_MessageExpCS89.setter
    def ocl_cst_MessageExpCS89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_MessageExpCS__ocl_cst_MessageExpCS89", None)
        self.__ocl_cst_MessageExpCS89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCLMessageArgCS"):
                    opp_val = getattr(item, "OCLMessageArgCS", None)
                    
                    if opp_val == self:
                        setattr(item, "OCLMessageArgCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCLMessageArgCS"):
                    opp_val = getattr(item, "OCLMessageArgCS", None)
                    
                    setattr(item, "OCLMessageArgCS", self)
                    

class ocl_cst_CallExpCS(OCLExpressionCS):

    def __init__(self, accessor: str, ocl_cst_CallExpCS: "OCLExpressionCS" = None, ocl_cst_CallExpCS105: "SimpleNameCS" = None, OCLExpressionCS49: "ocl_cst_InvCS", OCLExpressionCS101: "ocl_cst_CollectionRangeCS", OCLExpressionCS58: "ocl_cst_DefExpressionCS", OCLExpressionCS79: "ocl_cst_IfExpCS", OCLExpressionCS74: "ocl_cst_LetExpCS", OCLExpressionCS60: "ocl_cst_VariableExpCS", OCLExpressionCS114: "ocl_cst_LoopExpCS", OCLExpressionCS: "ocl_cst_InitOrDerValueCS", OCLExpressionCS97: "ocl_cst_CollectionLiteralPartCS", OCLExpressionCS76: "ocl_cst_IfExpCS", OCLExpressionCS103: "ocl_cst_CallExpCS", OCLExpressionCS84: "ocl_cst_MessageExpCS", OCLExpressionCS47: "ocl_cst_PrePostOrBodyDeclCS", OCLExpressionCS119: "ocl_cst_FeatureCallExpCS", OCLExpressionCS42: "ocl_cst_VariableCS", OCLExpressionCS82: "ocl_cst_IfExpCS", OCLExpressionCS94: "ocl_cst_OCLMessageArgCS"):
        self.accessor = accessor
        self.ocl_cst_CallExpCS = ocl_cst_CallExpCS
        self.ocl_cst_CallExpCS105 = ocl_cst_CallExpCS105
        
    @property
    def accessor(self) -> str:
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: str):
        self.__accessor = accessor

    @property
    def ocl_cst_CallExpCS(self):
        return self.__ocl_cst_CallExpCS

    @ocl_cst_CallExpCS.setter
    def ocl_cst_CallExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_CallExpCS__ocl_cst_CallExpCS", None)
        self.__ocl_cst_CallExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS103"):
                opp_val = getattr(old_value, "OCLExpressionCS103", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS103"):
                opp_val = getattr(value, "OCLExpressionCS103", None)
                setattr(value, "OCLExpressionCS103", self)

    @property
    def ocl_cst_CallExpCS105(self):
        return self.__ocl_cst_CallExpCS105

    @ocl_cst_CallExpCS105.setter
    def ocl_cst_CallExpCS105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_CallExpCS__ocl_cst_CallExpCS105", None)
        self.__ocl_cst_CallExpCS105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS106"):
                opp_val = getattr(old_value, "SimpleNameCS106", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS106"):
                opp_val = getattr(value, "SimpleNameCS106", None)
                setattr(value, "SimpleNameCS106", self)

class ocl_cst_LiteralExpCS(OCLExpressionCS):

    pass
class ocl_cst_LetExpCS(OCLExpressionCS):

    pass
class ocl_cst_SimpleNameCS(OCLExpressionCS):

    def __init__(self, value: str, type: str, OCLExpressionCS49: "ocl_cst_InvCS", OCLExpressionCS101: "ocl_cst_CollectionRangeCS", OCLExpressionCS58: "ocl_cst_DefExpressionCS", OCLExpressionCS79: "ocl_cst_IfExpCS", OCLExpressionCS74: "ocl_cst_LetExpCS", OCLExpressionCS60: "ocl_cst_VariableExpCS", OCLExpressionCS114: "ocl_cst_LoopExpCS", OCLExpressionCS: "ocl_cst_InitOrDerValueCS", OCLExpressionCS97: "ocl_cst_CollectionLiteralPartCS", OCLExpressionCS76: "ocl_cst_IfExpCS", OCLExpressionCS103: "ocl_cst_CallExpCS", OCLExpressionCS84: "ocl_cst_MessageExpCS", OCLExpressionCS47: "ocl_cst_PrePostOrBodyDeclCS", OCLExpressionCS119: "ocl_cst_FeatureCallExpCS", OCLExpressionCS42: "ocl_cst_VariableCS", OCLExpressionCS82: "ocl_cst_IfExpCS", OCLExpressionCS94: "ocl_cst_OCLMessageArgCS"):
        self.value = value
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ocl_cst_TypeCS(OCLExpressionCS):

    pass
class SimpleNameCS:

    pass
class TypeCS:

    pass
class ocl_cst_TupleTypeCS(TypeCS):

    pass
class ocl_cst_PathNameCS(TypeCS):

    pass
class PackageDeclarationCS:

    pass
class ContextDeclCS:

    pass
class ocl_cst_PropertyContextCS(ContextDeclCS):

    pass
class ocl_cst_OperationContextDeclCS(ContextDeclCS):

    pass
class ocl_cst_ClassifierContextDeclCS(ContextDeclCS):

    pass
class PathNameCS:

    pass
class CSTNode:

    pass
class ocl_cst_VariableCS(CSTNode):

    def __init__(self, name: str, ocl_cst_VariableCS41: "OCLExpressionCS" = None, ocl_cst_VariableCS: "TypeCS" = None):
        self.name = name
        self.ocl_cst_VariableCS41 = ocl_cst_VariableCS41
        self.ocl_cst_VariableCS = ocl_cst_VariableCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ocl_cst_VariableCS41(self):
        return self.__ocl_cst_VariableCS41

    @ocl_cst_VariableCS41.setter
    def ocl_cst_VariableCS41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_VariableCS__ocl_cst_VariableCS41", None)
        self.__ocl_cst_VariableCS41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS42"):
                opp_val = getattr(old_value, "OCLExpressionCS42", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS42"):
                opp_val = getattr(value, "OCLExpressionCS42", None)
                setattr(value, "OCLExpressionCS42", self)

    @property
    def ocl_cst_VariableCS(self):
        return self.__ocl_cst_VariableCS

    @ocl_cst_VariableCS.setter
    def ocl_cst_VariableCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_VariableCS__ocl_cst_VariableCS", None)
        self.__ocl_cst_VariableCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeCS39"):
                opp_val = getattr(old_value, "TypeCS39", None)
                if opp_val == self:
                    setattr(old_value, "TypeCS39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeCS39"):
                opp_val = getattr(value, "TypeCS39", None)
                setattr(value, "TypeCS39", self)

class ocl_cst_OCLMessageArgCS(CSTNode):

    pass
class ocl_cst_InvOrDefCS(CSTNode):

    pass
class ocl_cst_InitOrDerValueCS(CSTNode):

    pass
class ocl_cst_ContextDeclCS(CSTNode):

    pass
class ocl_cst_IsMarkedPreCS(CSTNode):

    pass
class ocl_cst_OperationCS(CSTNode):

    pass
class ocl_cst_PrePostOrBodyDeclCS(CSTNode):

    def __init__(self, kind: str, ocl_cst_PrePostOrBodyDeclCS: "SimpleNameCS" = None, ocl_cst_PrePostOrBodyDeclCS46: "OCLExpressionCS" = None):
        self.kind = kind
        self.ocl_cst_PrePostOrBodyDeclCS = ocl_cst_PrePostOrBodyDeclCS
        self.ocl_cst_PrePostOrBodyDeclCS46 = ocl_cst_PrePostOrBodyDeclCS46
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ocl_cst_PrePostOrBodyDeclCS(self):
        return self.__ocl_cst_PrePostOrBodyDeclCS

    @ocl_cst_PrePostOrBodyDeclCS.setter
    def ocl_cst_PrePostOrBodyDeclCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_PrePostOrBodyDeclCS__ocl_cst_PrePostOrBodyDeclCS", None)
        self.__ocl_cst_PrePostOrBodyDeclCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS44"):
                opp_val = getattr(old_value, "SimpleNameCS44", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS44"):
                opp_val = getattr(value, "SimpleNameCS44", None)
                setattr(value, "SimpleNameCS44", self)

    @property
    def ocl_cst_PrePostOrBodyDeclCS46(self):
        return self.__ocl_cst_PrePostOrBodyDeclCS46

    @ocl_cst_PrePostOrBodyDeclCS46.setter
    def ocl_cst_PrePostOrBodyDeclCS46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_PrePostOrBodyDeclCS__ocl_cst_PrePostOrBodyDeclCS46", None)
        self.__ocl_cst_PrePostOrBodyDeclCS46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS47"):
                opp_val = getattr(old_value, "OCLExpressionCS47", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS47"):
                opp_val = getattr(value, "OCLExpressionCS47", None)
                setattr(value, "OCLExpressionCS47", self)

class ocl_cst_DefExpressionCS(CSTNode):

    pass
class ocl_cst_OCLDocumentCS(CSTNode):

    pass
class ocl_cst_CollectionLiteralPartCS(CSTNode):

    pass
class ocl_cst_OCLExpressionCS(CSTNode):

    pass
class ocl_cst_PackageDeclarationCS(CSTNode):

    pass
class ocl_cst_CSTNode(ABC):

    def __init__(self, startOffset: int, endOffset: int, startToken: str, endToken: str, ast: str):
        self.startOffset = startOffset
        self.endOffset = endOffset
        self.startToken = startToken
        self.endToken = endToken
        self.ast = ast
        
    @property
    def ast(self) -> str:
        return self.__ast

    @ast.setter
    def ast(self, ast: str):
        self.__ast = ast

    @property
    def endOffset(self) -> int:
        return self.__endOffset

    @endOffset.setter
    def endOffset(self, endOffset: int):
        self.__endOffset = endOffset

    @property
    def startOffset(self) -> int:
        return self.__startOffset

    @startOffset.setter
    def startOffset(self, startOffset: int):
        self.__startOffset = startOffset

    @property
    def endToken(self) -> str:
        return self.__endToken

    @endToken.setter
    def endToken(self, endToken: str):
        self.__endToken = endToken

    @property
    def startToken(self) -> str:
        return self.__startToken

    @startToken.setter
    def startToken(self, startToken: str):
        self.__startToken = startToken

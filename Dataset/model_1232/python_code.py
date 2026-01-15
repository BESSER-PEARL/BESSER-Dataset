from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionTypeIdentifierEnum(Enum):
    Set = "Set"
    Bag = "Bag"
    Sequence = "Sequence"
    Collection = "Collection"
    OrderedSet = "OrderedSet"
class DotOrArrowEnum(Enum):
    none = "none"
    dot = "dot"
    arrow = "arrow"
class MessageExpKind(Enum):
    hasSent = "hasSent"
    sent = "sent"
class SimpleTypeEnum(Enum):
    keyword = "keyword"
    UnlimitedNatural = "UnlimitedNatural"
    identifier = "identifier"
    self = "self"
    Integer = "Integer"
    String = "String"
    Real = "Real"
    Boolean = "Boolean"
    OclAny = "OclAny"
    OclVoid = "OclVoid"
    Invalid = "Invalid"
    OclMessage = "OclMessage"
class PrePostOrBodyEnum(Enum):
    pre = "pre"
    post = "post"
    body = "body"


############################################
# Definition of Classes
############################################

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
class FeatureCallExpCS:

    pass
class ocl_cst_OperationCallExpCS(FeatureCallExpCS):

    pass
class PrimitiveLiteralExpCS:

    pass
class ocl_cst_BooleanLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

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

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

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

class ocl_cst_IntegerLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class LiteralExpCS:

    pass
class ocl_cst_NullLiteralExpCS(LiteralExpCS):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class ocl_cst_PrimitiveLiteralExpCS(LiteralExpCS):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class ocl_cst_InvalidLiteralExpCS(LiteralExpCS):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class ocl_cst_EnumLiteralExpCS(LiteralExpCS):

    pass
class OCLMessageArgCS:

    pass
class ocl_cst_TupleLiteralExpCS(LiteralExpCS):

    pass
class CollectionLiteralPartCS:

    pass
class ocl_cst_CollectionRangeCS(CollectionLiteralPartCS):

    pass
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
                    

class cst_SimpleNameCS:

    pass
class IsMarkedPreCS:

    pass
class cst_TypeCS:

    pass
class ocl_cst_PrimitiveTypeCS(cst_TypeCS, cst_SimpleNameCS):

    pass
class DefExpressionCS:

    pass
class PrePostOrBodyDeclCS:

    pass
class OperationCS:

    pass
class VariableCS:

    pass
class InvOrDefCS:

    pass
class ocl_cst_DefCS(InvOrDefCS):

    pass
class ocl_cst_InvCS(InvOrDefCS):

    pass
class TypeCS:

    pass
class ocl_cst_StateExpCS(TypeCS):

    def __init__(self, sequenceOfNames: str, TypeCS73: "ocl_cst_CollectionTypeCS", TypeCS43: "ocl_cst_VariableCS", TypeCS41: "ocl_cst_OperationCS", TypeCS95: "ocl_cst_OCLMessageArgCS", TypeCS: "ocl_cst_PropertyContextCS"):
        self.sequenceOfNames = sequenceOfNames
        
    @property
    def sequenceOfNames(self) -> str:
        return self.__sequenceOfNames

    @sequenceOfNames.setter
    def sequenceOfNames(self, sequenceOfNames: str):
        self.__sequenceOfNames = sequenceOfNames

class ocl_cst_CollectionTypeCS(TypeCS):

    def __init__(self, collectionTypeIdentifier: str, ocl_cst_CollectionTypeCS: "TypeCS" = None, TypeCS73: "ocl_cst_CollectionTypeCS", TypeCS43: "ocl_cst_VariableCS", TypeCS41: "ocl_cst_OperationCS", TypeCS95: "ocl_cst_OCLMessageArgCS", TypeCS: "ocl_cst_PropertyContextCS"):
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
            if hasattr(old_value, "TypeCS73"):
                opp_val = getattr(old_value, "TypeCS73", None)
                if opp_val == self:
                    setattr(old_value, "TypeCS73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeCS73"):
                opp_val = getattr(value, "TypeCS73", None)
                setattr(value, "TypeCS73", self)

class ocl_cst_TupleTypeCS(TypeCS):

    pass
class ocl_cst_PathNameCS(TypeCS):

    def __init__(self, sequenceOfNames: str, TypeCS73: "ocl_cst_CollectionTypeCS", TypeCS43: "ocl_cst_VariableCS", TypeCS41: "ocl_cst_OperationCS", TypeCS95: "ocl_cst_OCLMessageArgCS", TypeCS: "ocl_cst_PropertyContextCS"):
        self.sequenceOfNames = sequenceOfNames
        
    @property
    def sequenceOfNames(self) -> str:
        return self.__sequenceOfNames

    @sequenceOfNames.setter
    def sequenceOfNames(self, sequenceOfNames: str):
        self.__sequenceOfNames = sequenceOfNames

class PackageDeclarationCS:

    pass
class ContextDeclCS:

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

    def __init__(self, name: str, ocl_cst_VariableCS: "TypeCS" = None, ocl_cst_VariableCS45: "OCLExpressionCS" = None):
        self.name = name
        self.ocl_cst_VariableCS = ocl_cst_VariableCS
        self.ocl_cst_VariableCS45 = ocl_cst_VariableCS45
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ocl_cst_VariableCS45(self):
        return self.__ocl_cst_VariableCS45

    @ocl_cst_VariableCS45.setter
    def ocl_cst_VariableCS45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_VariableCS__ocl_cst_VariableCS45", None)
        self.__ocl_cst_VariableCS45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS46"):
                opp_val = getattr(old_value, "OCLExpressionCS46", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS46"):
                opp_val = getattr(value, "OCLExpressionCS46", None)
                setattr(value, "OCLExpressionCS46", self)

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
            if hasattr(old_value, "TypeCS43"):
                opp_val = getattr(old_value, "TypeCS43", None)
                if opp_val == self:
                    setattr(old_value, "TypeCS43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeCS43"):
                opp_val = getattr(value, "TypeCS43", None)
                setattr(value, "TypeCS43", self)

class ocl_cst_CollectionLiteralPartCS(CSTNode):

    pass
class ocl_cst_OCLDocumentCS(CSTNode):

    pass
class ocl_cst_IsMarkedPreCS(CSTNode):

    def __init__(self, pre: bool):
        self.pre = pre
        
    @property
    def pre(self) -> bool:
        return self.__pre

    @pre.setter
    def pre(self, pre: bool):
        self.__pre = pre

class ocl_cst_PrePostOrBodyDeclCS(CSTNode):

    def __init__(self, kind: str, ocl_cst_PrePostOrBodyDeclCS: "SimpleNameCS" = None, ocl_cst_PrePostOrBodyDeclCS50: "OCLExpressionCS" = None):
        self.kind = kind
        self.ocl_cst_PrePostOrBodyDeclCS = ocl_cst_PrePostOrBodyDeclCS
        self.ocl_cst_PrePostOrBodyDeclCS50 = ocl_cst_PrePostOrBodyDeclCS50
        
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
            if hasattr(old_value, "SimpleNameCS48"):
                opp_val = getattr(old_value, "SimpleNameCS48", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS48"):
                opp_val = getattr(value, "SimpleNameCS48", None)
                setattr(value, "SimpleNameCS48", self)

    @property
    def ocl_cst_PrePostOrBodyDeclCS50(self):
        return self.__ocl_cst_PrePostOrBodyDeclCS50

    @ocl_cst_PrePostOrBodyDeclCS50.setter
    def ocl_cst_PrePostOrBodyDeclCS50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_PrePostOrBodyDeclCS__ocl_cst_PrePostOrBodyDeclCS50", None)
        self.__ocl_cst_PrePostOrBodyDeclCS50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS51"):
                opp_val = getattr(old_value, "OCLExpressionCS51", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS51"):
                opp_val = getattr(value, "OCLExpressionCS51", None)
                setattr(value, "OCLExpressionCS51", self)

class ocl_cst_DefExpressionCS(CSTNode):

    pass
class ocl_cst_OCLMessageArgCS(CSTNode):

    pass
class ocl_cst_InvOrDefCS(CSTNode):

    pass
class ocl_cst_OperationCS(CSTNode):

    pass
class ocl_cst_InitOrDerValueCS(CSTNode):

    pass
class ocl_cst_PackageDeclarationCS(CSTNode):

    pass
class InitOrDerValueCS:

    pass
class ocl_cst_DerValueCS(InitOrDerValueCS):

    pass
class ocl_cst_InitValueCS(InitOrDerValueCS):

    pass
class SimpleNameCS:

    pass
class ocl_cst_PropertyContextCS(ContextDeclCS):

    pass
class ocl_cst_ContextDeclCS(CSTNode):

    pass
class ocl_cst_OCLExpressionCS(CSTNode):

    pass
class OCLExpressionCS:

    pass
class ocl_cst_SimpleNameCS(OCLExpressionCS):

    def __init__(self, value: str, type: str, OCLExpressionCS125: "ocl_cst_FeatureCallExpCS", OCLExpressionCS51: "ocl_cst_PrePostOrBodyDeclCS", OCLExpressionCS83: "ocl_cst_IfExpCS", OCLExpressionCS112: "ocl_cst_CallExpCS", OCLExpressionCS88: "ocl_cst_MessageExpCS", OCLExpressionCS62: "ocl_cst_DefExpressionCS", OCLExpressionCS86: "ocl_cst_IfExpCS", OCLExpressionCS64: "ocl_cst_VariableExpCS", OCLExpressionCS46: "ocl_cst_VariableCS", OCLExpressionCS106: "ocl_cst_CollectionLiteralPartCS", OCLExpressionCS: "ocl_cst_InitOrDerValueCS", OCLExpressionCS80: "ocl_cst_IfExpCS", OCLExpressionCS78: "ocl_cst_LetExpCS", OCLExpressionCS98: "ocl_cst_OCLMessageArgCS", OCLExpressionCS110: "ocl_cst_CollectionRangeCS", OCLExpressionCS53: "ocl_cst_InvCS", OCLExpressionCS123: "ocl_cst_LoopExpCS"):
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
class ocl_cst_MessageExpCS(OCLExpressionCS):

    def __init__(self, kind: str, ocl_cst_MessageExpCS: "OCLExpressionCS" = None, ocl_cst_MessageExpCS90: "SimpleNameCS" = None, ocl_cst_MessageExpCS93: set["OCLMessageArgCS"] = None, OCLExpressionCS125: "ocl_cst_FeatureCallExpCS", OCLExpressionCS51: "ocl_cst_PrePostOrBodyDeclCS", OCLExpressionCS83: "ocl_cst_IfExpCS", OCLExpressionCS112: "ocl_cst_CallExpCS", OCLExpressionCS88: "ocl_cst_MessageExpCS", OCLExpressionCS62: "ocl_cst_DefExpressionCS", OCLExpressionCS86: "ocl_cst_IfExpCS", OCLExpressionCS64: "ocl_cst_VariableExpCS", OCLExpressionCS46: "ocl_cst_VariableCS", OCLExpressionCS106: "ocl_cst_CollectionLiteralPartCS", OCLExpressionCS: "ocl_cst_InitOrDerValueCS", OCLExpressionCS80: "ocl_cst_IfExpCS", OCLExpressionCS78: "ocl_cst_LetExpCS", OCLExpressionCS98: "ocl_cst_OCLMessageArgCS", OCLExpressionCS110: "ocl_cst_CollectionRangeCS", OCLExpressionCS53: "ocl_cst_InvCS", OCLExpressionCS123: "ocl_cst_LoopExpCS"):
        self.kind = kind
        self.ocl_cst_MessageExpCS = ocl_cst_MessageExpCS
        self.ocl_cst_MessageExpCS90 = ocl_cst_MessageExpCS90
        self.ocl_cst_MessageExpCS93 = ocl_cst_MessageExpCS93 if ocl_cst_MessageExpCS93 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ocl_cst_MessageExpCS90(self):
        return self.__ocl_cst_MessageExpCS90

    @ocl_cst_MessageExpCS90.setter
    def ocl_cst_MessageExpCS90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_MessageExpCS__ocl_cst_MessageExpCS90", None)
        self.__ocl_cst_MessageExpCS90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS91"):
                opp_val = getattr(old_value, "SimpleNameCS91", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS91"):
                opp_val = getattr(value, "SimpleNameCS91", None)
                setattr(value, "SimpleNameCS91", self)

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
            if hasattr(old_value, "OCLExpressionCS88"):
                opp_val = getattr(old_value, "OCLExpressionCS88", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS88"):
                opp_val = getattr(value, "OCLExpressionCS88", None)
                setattr(value, "OCLExpressionCS88", self)

    @property
    def ocl_cst_MessageExpCS93(self):
        return self.__ocl_cst_MessageExpCS93

    @ocl_cst_MessageExpCS93.setter
    def ocl_cst_MessageExpCS93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_MessageExpCS__ocl_cst_MessageExpCS93", None)
        self.__ocl_cst_MessageExpCS93 = value if value is not None else set()
        
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
                    

class ocl_cst_LetExpCS(OCLExpressionCS):

    pass
class ocl_cst_IfExpCS(OCLExpressionCS):

    pass
class ocl_cst_VariableExpCS(OCLExpressionCS):

    pass
class ocl_cst_CallExpCS(OCLExpressionCS):

    def __init__(self, accessor: str, ocl_cst_CallExpCS: "OCLExpressionCS" = None, ocl_cst_CallExpCS114: "SimpleNameCS" = None, OCLExpressionCS125: "ocl_cst_FeatureCallExpCS", OCLExpressionCS51: "ocl_cst_PrePostOrBodyDeclCS", OCLExpressionCS83: "ocl_cst_IfExpCS", OCLExpressionCS112: "ocl_cst_CallExpCS", OCLExpressionCS88: "ocl_cst_MessageExpCS", OCLExpressionCS62: "ocl_cst_DefExpressionCS", OCLExpressionCS86: "ocl_cst_IfExpCS", OCLExpressionCS64: "ocl_cst_VariableExpCS", OCLExpressionCS46: "ocl_cst_VariableCS", OCLExpressionCS106: "ocl_cst_CollectionLiteralPartCS", OCLExpressionCS: "ocl_cst_InitOrDerValueCS", OCLExpressionCS80: "ocl_cst_IfExpCS", OCLExpressionCS78: "ocl_cst_LetExpCS", OCLExpressionCS98: "ocl_cst_OCLMessageArgCS", OCLExpressionCS110: "ocl_cst_CollectionRangeCS", OCLExpressionCS53: "ocl_cst_InvCS", OCLExpressionCS123: "ocl_cst_LoopExpCS"):
        self.accessor = accessor
        self.ocl_cst_CallExpCS = ocl_cst_CallExpCS
        self.ocl_cst_CallExpCS114 = ocl_cst_CallExpCS114
        
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
            if hasattr(old_value, "OCLExpressionCS112"):
                opp_val = getattr(old_value, "OCLExpressionCS112", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS112"):
                opp_val = getattr(value, "OCLExpressionCS112", None)
                setattr(value, "OCLExpressionCS112", self)

    @property
    def ocl_cst_CallExpCS114(self):
        return self.__ocl_cst_CallExpCS114

    @ocl_cst_CallExpCS114.setter
    def ocl_cst_CallExpCS114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_CallExpCS__ocl_cst_CallExpCS114", None)
        self.__ocl_cst_CallExpCS114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS115"):
                opp_val = getattr(old_value, "SimpleNameCS115", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS115"):
                opp_val = getattr(value, "SimpleNameCS115", None)
                setattr(value, "SimpleNameCS115", self)

class ocl_cst_LiteralExpCS(OCLExpressionCS):

    pass
class ocl_cst_CSTNode(ABC):

    def __init__(self, startOffset: int, endOffset: int, startToken: str, endToken: str, ast: str):
        self.startOffset = startOffset
        self.endOffset = endOffset
        self.startToken = startToken
        self.endToken = endToken
        self.ast = ast
        
    @property
    def endToken(self) -> str:
        return self.__endToken

    @endToken.setter
    def endToken(self, endToken: str):
        self.__endToken = endToken

    @property
    def startOffset(self) -> int:
        return self.__startOffset

    @startOffset.setter
    def startOffset(self, startOffset: int):
        self.__startOffset = startOffset

    @property
    def ast(self) -> str:
        return self.__ast

    @ast.setter
    def ast(self, ast: str):
        self.__ast = ast

    @property
    def startToken(self) -> str:
        return self.__startToken

    @startToken.setter
    def startToken(self, startToken: str):
        self.__startToken = startToken

    @property
    def endOffset(self) -> int:
        return self.__endOffset

    @endOffset.setter
    def endOffset(self, endOffset: int):
        self.__endOffset = endOffset

from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrePostOrBodyEnum(Enum):
    pre = "pre"
    post = "post"
    body = "body"
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
class SimpleTypeEnum(Enum):
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
    keyword = "keyword"
class MessageExpKind(Enum):
    hasSent = "hasSent"
    sent = "sent"


############################################
# Definition of Classes
############################################

class FeatureCallExpCS:

    pass
class ocl_cst_OperationCallExpCS(FeatureCallExpCS):

    pass
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
class PrimitiveLiteralExpCS:

    pass
class ocl_cst_StringLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

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
                    

class ocl_cst_PrimitiveLiteralExpCS(LiteralExpCS):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class ocl_cst_TupleLiteralExpCS(LiteralExpCS):

    pass
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
class CollectionLiteralPartCS:

    pass
class ocl_cst_CollectionRangeCS(CollectionLiteralPartCS):

    pass
class IsMarkedPreCS:

    pass
class cst_TypeCS:

    pass
class cst_SimpleNameCS:

    pass
class ocl_cst_PrimitiveTypeCS(cst_SimpleNameCS, cst_TypeCS):

    pass
class VariableCS:

    pass
class OCLExpressionCS:

    pass
class ocl_cst_MessageExpCS(OCLExpressionCS):

    def __init__(self, kind: str, ocl_cst_MessageExpCS: "OCLExpressionCS" = None, ocl_cst_MessageExpCS80: "SimpleNameCS" = None, ocl_cst_MessageExpCS83: set["OCLMessageArgCS"] = None, OCLExpressionCS76: "ocl_cst_IfExpCS", OCLExpressionCS107: "ocl_cst_CallExpCS", OCLExpressionCS93: "ocl_cst_VariableCS", OCLExpressionCS103: "ocl_cst_CollectionLiteralPartCS", OCLExpressionCS105: "ocl_cst_CollectionRangeCS", OCLExpressionCS: "ocl_cst_PrePostOrBodyDeclCS", OCLExpressionCS52: "ocl_cst_DefExpressionCS", OCLExpressionCS73: "ocl_cst_IfExpCS", OCLExpressionCS70: "ocl_cst_IfExpCS", OCLExpressionCS54: "ocl_cst_VariableExpCS", OCLExpressionCS36: "ocl_cst_InitOrDerValueCS", OCLExpressionCS68: "ocl_cst_LetExpCS", OCLExpressionCS88: "ocl_cst_OCLMessageArgCS", OCLExpressionCS118: "ocl_cst_LoopExpCS", OCLExpressionCS120: "ocl_cst_FeatureCallExpCS", OCLExpressionCS78: "ocl_cst_MessageExpCS", OCLExpressionCS43: "ocl_cst_InvCS"):
        self.kind = kind
        self.ocl_cst_MessageExpCS = ocl_cst_MessageExpCS
        self.ocl_cst_MessageExpCS80 = ocl_cst_MessageExpCS80
        self.ocl_cst_MessageExpCS83 = ocl_cst_MessageExpCS83 if ocl_cst_MessageExpCS83 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ocl_cst_MessageExpCS83(self):
        return self.__ocl_cst_MessageExpCS83

    @ocl_cst_MessageExpCS83.setter
    def ocl_cst_MessageExpCS83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_MessageExpCS__ocl_cst_MessageExpCS83", None)
        self.__ocl_cst_MessageExpCS83 = value if value is not None else set()
        
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
                    

    @property
    def ocl_cst_MessageExpCS80(self):
        return self.__ocl_cst_MessageExpCS80

    @ocl_cst_MessageExpCS80.setter
    def ocl_cst_MessageExpCS80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_MessageExpCS__ocl_cst_MessageExpCS80", None)
        self.__ocl_cst_MessageExpCS80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS81"):
                opp_val = getattr(old_value, "SimpleNameCS81", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS81"):
                opp_val = getattr(value, "SimpleNameCS81", None)
                setattr(value, "SimpleNameCS81", self)

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
            if hasattr(old_value, "OCLExpressionCS78"):
                opp_val = getattr(old_value, "OCLExpressionCS78", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS78"):
                opp_val = getattr(value, "OCLExpressionCS78", None)
                setattr(value, "OCLExpressionCS78", self)

class ocl_cst_LetExpCS(OCLExpressionCS):

    pass
class ocl_cst_SimpleNameCS(OCLExpressionCS):

    def __init__(self, value: str, type: str, OCLExpressionCS76: "ocl_cst_IfExpCS", OCLExpressionCS107: "ocl_cst_CallExpCS", OCLExpressionCS93: "ocl_cst_VariableCS", OCLExpressionCS103: "ocl_cst_CollectionLiteralPartCS", OCLExpressionCS105: "ocl_cst_CollectionRangeCS", OCLExpressionCS: "ocl_cst_PrePostOrBodyDeclCS", OCLExpressionCS52: "ocl_cst_DefExpressionCS", OCLExpressionCS73: "ocl_cst_IfExpCS", OCLExpressionCS70: "ocl_cst_IfExpCS", OCLExpressionCS54: "ocl_cst_VariableExpCS", OCLExpressionCS36: "ocl_cst_InitOrDerValueCS", OCLExpressionCS68: "ocl_cst_LetExpCS", OCLExpressionCS88: "ocl_cst_OCLMessageArgCS", OCLExpressionCS118: "ocl_cst_LoopExpCS", OCLExpressionCS120: "ocl_cst_FeatureCallExpCS", OCLExpressionCS78: "ocl_cst_MessageExpCS", OCLExpressionCS43: "ocl_cst_InvCS"):
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

class ocl_cst_CallExpCS(OCLExpressionCS):

    def __init__(self, accessor: str, ocl_cst_CallExpCS109: "SimpleNameCS" = None, ocl_cst_CallExpCS: "OCLExpressionCS" = None, OCLExpressionCS76: "ocl_cst_IfExpCS", OCLExpressionCS107: "ocl_cst_CallExpCS", OCLExpressionCS93: "ocl_cst_VariableCS", OCLExpressionCS103: "ocl_cst_CollectionLiteralPartCS", OCLExpressionCS105: "ocl_cst_CollectionRangeCS", OCLExpressionCS: "ocl_cst_PrePostOrBodyDeclCS", OCLExpressionCS52: "ocl_cst_DefExpressionCS", OCLExpressionCS73: "ocl_cst_IfExpCS", OCLExpressionCS70: "ocl_cst_IfExpCS", OCLExpressionCS54: "ocl_cst_VariableExpCS", OCLExpressionCS36: "ocl_cst_InitOrDerValueCS", OCLExpressionCS68: "ocl_cst_LetExpCS", OCLExpressionCS88: "ocl_cst_OCLMessageArgCS", OCLExpressionCS118: "ocl_cst_LoopExpCS", OCLExpressionCS120: "ocl_cst_FeatureCallExpCS", OCLExpressionCS78: "ocl_cst_MessageExpCS", OCLExpressionCS43: "ocl_cst_InvCS"):
        self.accessor = accessor
        self.ocl_cst_CallExpCS109 = ocl_cst_CallExpCS109
        self.ocl_cst_CallExpCS = ocl_cst_CallExpCS
        
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
            if hasattr(old_value, "OCLExpressionCS107"):
                opp_val = getattr(old_value, "OCLExpressionCS107", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS107"):
                opp_val = getattr(value, "OCLExpressionCS107", None)
                setattr(value, "OCLExpressionCS107", self)

    @property
    def ocl_cst_CallExpCS109(self):
        return self.__ocl_cst_CallExpCS109

    @ocl_cst_CallExpCS109.setter
    def ocl_cst_CallExpCS109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_CallExpCS__ocl_cst_CallExpCS109", None)
        self.__ocl_cst_CallExpCS109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS110"):
                opp_val = getattr(old_value, "SimpleNameCS110", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS110"):
                opp_val = getattr(value, "SimpleNameCS110", None)
                setattr(value, "SimpleNameCS110", self)

class ocl_cst_LiteralExpCS(OCLExpressionCS):

    pass
class ocl_cst_TypeCS(OCLExpressionCS):

    pass
class ocl_cst_VariableExpCS(OCLExpressionCS):

    pass
class ocl_cst_IfExpCS(OCLExpressionCS):

    pass
class PrePostOrBodyDeclCS:

    pass
class DefExpressionCS:

    pass
class OperationCS:

    pass
class InvOrDefCS:

    pass
class ocl_cst_DefCS(InvOrDefCS):

    pass
class ocl_cst_InvCS(InvOrDefCS):

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
class ocl_cst_DefExpressionCS(CSTNode):

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

class ocl_cst_OperationCS(CSTNode):

    pass
class ocl_cst_OCLExpressionCS(CSTNode):

    pass
class ocl_cst_CollectionLiteralPartCS(CSTNode):

    pass
class ocl_cst_InitOrDerValueCS(CSTNode):

    pass
class ocl_cst_InvOrDefCS(CSTNode):

    pass
class ocl_cst_OCLMessageArgCS(CSTNode):

    pass
class ocl_cst_VariableCS(CSTNode):

    def __init__(self, name: str, ocl_cst_VariableCS: "TypeCS" = None, ocl_cst_VariableCS92: "OCLExpressionCS" = None):
        self.name = name
        self.ocl_cst_VariableCS = ocl_cst_VariableCS
        self.ocl_cst_VariableCS92 = ocl_cst_VariableCS92
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ocl_cst_VariableCS92(self):
        return self.__ocl_cst_VariableCS92

    @ocl_cst_VariableCS92.setter
    def ocl_cst_VariableCS92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_VariableCS__ocl_cst_VariableCS92", None)
        self.__ocl_cst_VariableCS92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS93"):
                opp_val = getattr(old_value, "OCLExpressionCS93", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS93"):
                opp_val = getattr(value, "OCLExpressionCS93", None)
                setattr(value, "OCLExpressionCS93", self)

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
            if hasattr(old_value, "TypeCS90"):
                opp_val = getattr(old_value, "TypeCS90", None)
                if opp_val == self:
                    setattr(old_value, "TypeCS90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeCS90"):
                opp_val = getattr(value, "TypeCS90", None)
                setattr(value, "TypeCS90", self)

class ocl_cst_PrePostOrBodyDeclCS(CSTNode):

    def __init__(self, kind: str, ocl_cst_PrePostOrBodyDeclCS: "SimpleNameCS" = None, ocl_cst_PrePostOrBodyDeclCS21: "OCLExpressionCS" = None):
        self.kind = kind
        self.ocl_cst_PrePostOrBodyDeclCS = ocl_cst_PrePostOrBodyDeclCS
        self.ocl_cst_PrePostOrBodyDeclCS21 = ocl_cst_PrePostOrBodyDeclCS21
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ocl_cst_PrePostOrBodyDeclCS21(self):
        return self.__ocl_cst_PrePostOrBodyDeclCS21

    @ocl_cst_PrePostOrBodyDeclCS21.setter
    def ocl_cst_PrePostOrBodyDeclCS21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_cst_PrePostOrBodyDeclCS__ocl_cst_PrePostOrBodyDeclCS21", None)
        self.__ocl_cst_PrePostOrBodyDeclCS21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS"):
                opp_val = getattr(old_value, "OCLExpressionCS", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS"):
                opp_val = getattr(value, "OCLExpressionCS", None)
                setattr(value, "OCLExpressionCS", self)

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
            if hasattr(old_value, "SimpleNameCS19"):
                opp_val = getattr(old_value, "SimpleNameCS19", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS19"):
                opp_val = getattr(value, "SimpleNameCS19", None)
                setattr(value, "SimpleNameCS19", self)

class ocl_cst_PackageDeclarationCS(CSTNode):

    pass
class ocl_cst_CSTNode(ABC):

    def __init__(self, startOffset: int, endOffset: int):
        self.startOffset = startOffset
        self.endOffset = endOffset
        
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

class InitOrDerValueCS:

    pass
class ocl_cst_DerValueCS(InitOrDerValueCS):

    pass
class ocl_cst_InitValueCS(InitOrDerValueCS):

    pass
class TypeCS:

    pass
class ocl_cst_CollectionTypeCS(TypeCS):

    def __init__(self, collectionTypeIdentifier: str, ocl_cst_CollectionTypeCS: "TypeCS" = None, TypeCS90: "ocl_cst_VariableCS", TypeCS85: "ocl_cst_OCLMessageArgCS", TypeCS63: "ocl_cst_CollectionTypeCS", TypeCS: "ocl_cst_PropertyContextCS", TypeCS31: "ocl_cst_OperationCS"):
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
            if hasattr(old_value, "TypeCS63"):
                opp_val = getattr(old_value, "TypeCS63", None)
                if opp_val == self:
                    setattr(old_value, "TypeCS63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeCS63"):
                opp_val = getattr(value, "TypeCS63", None)
                setattr(value, "TypeCS63", self)

class ocl_cst_StateExpCS(TypeCS):

    def __init__(self, sequenceOfNames: str, TypeCS90: "ocl_cst_VariableCS", TypeCS85: "ocl_cst_OCLMessageArgCS", TypeCS63: "ocl_cst_CollectionTypeCS", TypeCS: "ocl_cst_PropertyContextCS", TypeCS31: "ocl_cst_OperationCS"):
        self.sequenceOfNames = sequenceOfNames
        
    @property
    def sequenceOfNames(self) -> str:
        return self.__sequenceOfNames

    @sequenceOfNames.setter
    def sequenceOfNames(self, sequenceOfNames: str):
        self.__sequenceOfNames = sequenceOfNames

class ocl_cst_TupleTypeCS(TypeCS):

    pass
class ocl_cst_PathNameCS(TypeCS):

    def __init__(self, sequenceOfNames: str, TypeCS90: "ocl_cst_VariableCS", TypeCS85: "ocl_cst_OCLMessageArgCS", TypeCS63: "ocl_cst_CollectionTypeCS", TypeCS: "ocl_cst_PropertyContextCS", TypeCS31: "ocl_cst_OperationCS"):
        self.sequenceOfNames = sequenceOfNames
        
    @property
    def sequenceOfNames(self) -> str:
        return self.__sequenceOfNames

    @sequenceOfNames.setter
    def sequenceOfNames(self, sequenceOfNames: str):
        self.__sequenceOfNames = sequenceOfNames

class SimpleNameCS:

    pass
class ocl_cst_PropertyContextCS(ContextDeclCS):

    pass
class ocl_cst_ContextDeclCS(CSTNode):

    pass
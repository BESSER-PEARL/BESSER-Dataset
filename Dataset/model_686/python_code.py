from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionKind(Enum):
    OrderedSet = "OrderedSet"
    Set = "Set"
    Bag = "Bag"
    Sequence = "Sequence"
class SeverityKind(Enum):
    error = "error"
    fatal = "fatal"
    warning = "warning"


############################################
# Definition of Classes
############################################

class AnonymousTupleLiteralPart:

    pass
class LogExp:

    pass
class essentialocl_LoopExp:

    pass
class DictLiteralPart:

    pass
class ImperativeLoopExp:

    pass
class JTLMM_imperativeocl_ForExp(ImperativeLoopExp):

    pass
class JTLMM_imperativeocl_CollectorExp(ImperativeLoopExp):

    pass
class JTLMM_imperativeocl_ImperativeIterateExp(ImperativeLoopExp):

    pass
class ObjectTemplateExp:

    pass
class AltExp:

    pass
class imperativeocl_ImperativeExpression:

    pass
class JTLMM_imperativeocl_ImperativeLoopExp(essentialocl_LoopExp, imperativeocl_ImperativeExpression):

    pass
class ImperativeExpression:

    pass
class JTLMM_imperativeocl_WhileExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, JTLMM_imperativeocl_AssertExp256: "OclExpression" = None, JTLMM_imperativeocl_AssertExp: "LogExp" = None):
        self.severity = severity
        self.JTLMM_imperativeocl_AssertExp256 = JTLMM_imperativeocl_AssertExp256
        self.JTLMM_imperativeocl_AssertExp = JTLMM_imperativeocl_AssertExp
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def JTLMM_imperativeocl_AssertExp256(self):
        return self.__JTLMM_imperativeocl_AssertExp256

    @JTLMM_imperativeocl_AssertExp256.setter
    def JTLMM_imperativeocl_AssertExp256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_AssertExp__JTLMM_imperativeocl_AssertExp256", None)
        self.__JTLMM_imperativeocl_AssertExp256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression257"):
                opp_val = getattr(old_value, "OclExpression257", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression257"):
                opp_val = getattr(value, "OclExpression257", None)
                setattr(value, "OclExpression257", self)

    @property
    def JTLMM_imperativeocl_AssertExp(self):
        return self.__JTLMM_imperativeocl_AssertExp

    @JTLMM_imperativeocl_AssertExp.setter
    def JTLMM_imperativeocl_AssertExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_AssertExp__JTLMM_imperativeocl_AssertExp", None)
        self.__JTLMM_imperativeocl_AssertExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogExp"):
                opp_val = getattr(old_value, "LogExp", None)
                if opp_val == self:
                    setattr(old_value, "LogExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogExp"):
                opp_val = getattr(value, "LogExp", None)
                setattr(value, "LogExp", self)

class JTLMM_imperativeocl_TupleExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_ContinueExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_LogExp(ImperativeExpression):

    def __init__(self, text: str, level: int, JTLMM_imperativeocl_LogExp: "OclExpression" = None, JTLMM_imperativeocl_LogExp252: "Element" = None):
        self.text = text
        self.level = level
        self.JTLMM_imperativeocl_LogExp = JTLMM_imperativeocl_LogExp
        self.JTLMM_imperativeocl_LogExp252 = JTLMM_imperativeocl_LogExp252
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def JTLMM_imperativeocl_LogExp(self):
        return self.__JTLMM_imperativeocl_LogExp

    @JTLMM_imperativeocl_LogExp.setter
    def JTLMM_imperativeocl_LogExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_LogExp__JTLMM_imperativeocl_LogExp", None)
        self.__JTLMM_imperativeocl_LogExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression250"):
                opp_val = getattr(old_value, "OclExpression250", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression250"):
                opp_val = getattr(value, "OclExpression250", None)
                setattr(value, "OclExpression250", self)

    @property
    def JTLMM_imperativeocl_LogExp252(self):
        return self.__JTLMM_imperativeocl_LogExp252

    @JTLMM_imperativeocl_LogExp252.setter
    def JTLMM_imperativeocl_LogExp252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_LogExp__JTLMM_imperativeocl_LogExp252", None)
        self.__JTLMM_imperativeocl_LogExp252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element253"):
                opp_val = getattr(old_value, "Element253", None)
                if opp_val == self:
                    setattr(old_value, "Element253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element253"):
                opp_val = getattr(value, "Element253", None)
                setattr(value, "Element253", self)

class JTLMM_imperativeocl_BlockExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_AltExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_InstantiationExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_TryExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_ReturnExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: bool, JTLMM_imperativeocl_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.JTLMM_imperativeocl_VariableInitExp = JTLMM_imperativeocl_VariableInitExp
        
    @property
    def withResult(self) -> bool:
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: bool):
        self.__withResult = withResult

    @property
    def JTLMM_imperativeocl_VariableInitExp(self):
        return self.__JTLMM_imperativeocl_VariableInitExp

    @JTLMM_imperativeocl_VariableInitExp.setter
    def JTLMM_imperativeocl_VariableInitExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_VariableInitExp__JTLMM_imperativeocl_VariableInitExp", None)
        self.__JTLMM_imperativeocl_VariableInitExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable193"):
                opp_val = getattr(old_value, "Variable193", None)
                if opp_val == self:
                    setattr(old_value, "Variable193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable193"):
                opp_val = getattr(value, "Variable193", None)
                setattr(value, "Variable193", self)

class JTLMM_imperativeocl_ComputeExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_UnpackExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_BreakExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_UnlinkExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_RaiseExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_AssignExp(ImperativeExpression):

    def __init__(self, isReset: bool, JTLMM_imperativeocl_AssignExp: set["OclExpression"] = None, JTLMM_imperativeocl_AssignExp181: "OclExpression" = None, JTLMM_imperativeocl_AssignExp184: "OclExpression" = None):
        self.isReset = isReset
        self.JTLMM_imperativeocl_AssignExp = JTLMM_imperativeocl_AssignExp if JTLMM_imperativeocl_AssignExp is not None else set()
        self.JTLMM_imperativeocl_AssignExp181 = JTLMM_imperativeocl_AssignExp181
        self.JTLMM_imperativeocl_AssignExp184 = JTLMM_imperativeocl_AssignExp184
        
    @property
    def isReset(self) -> bool:
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: bool):
        self.__isReset = isReset

    @property
    def JTLMM_imperativeocl_AssignExp(self):
        return self.__JTLMM_imperativeocl_AssignExp

    @JTLMM_imperativeocl_AssignExp.setter
    def JTLMM_imperativeocl_AssignExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_AssignExp__JTLMM_imperativeocl_AssignExp", None)
        self.__JTLMM_imperativeocl_AssignExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression179"):
                    opp_val = getattr(item, "OclExpression179", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression179"):
                    opp_val = getattr(item, "OclExpression179", None)
                    
                    setattr(item, "OclExpression179", self)
                    

    @property
    def JTLMM_imperativeocl_AssignExp181(self):
        return self.__JTLMM_imperativeocl_AssignExp181

    @JTLMM_imperativeocl_AssignExp181.setter
    def JTLMM_imperativeocl_AssignExp181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_AssignExp__JTLMM_imperativeocl_AssignExp181", None)
        self.__JTLMM_imperativeocl_AssignExp181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression182"):
                opp_val = getattr(old_value, "OclExpression182", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression182"):
                opp_val = getattr(value, "OclExpression182", None)
                setattr(value, "OclExpression182", self)

    @property
    def JTLMM_imperativeocl_AssignExp184(self):
        return self.__JTLMM_imperativeocl_AssignExp184

    @JTLMM_imperativeocl_AssignExp184.setter
    def JTLMM_imperativeocl_AssignExp184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_AssignExp__JTLMM_imperativeocl_AssignExp184", None)
        self.__JTLMM_imperativeocl_AssignExp184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression185"):
                opp_val = getattr(old_value, "OclExpression185", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression185"):
                opp_val = getattr(value, "OclExpression185", None)
                setattr(value, "OclExpression185", self)

class emof_Type:

    pass
class emof_DataType:

    pass
class AssignExp:

    pass
class PropertyTemplateItem:

    pass
class CollectionType:

    pass
class JTLMM_imperativeocl_ListType(CollectionType):

    pass
class JTLMM_imperativeocl_DictionaryType(CollectionType):

    pass
class JTLMM_essentialocl_BagType(CollectionType):

    pass
class TupleLiteralExp:

    pass
class CallExp:

    pass
class JTLMM_essentialocl_FeaturePropertyCall(CallExp):

    pass
class JTLMM_essentialocl_SetType(CollectionType):

    pass
class JTLMM_essentialocl_SequenceType(CollectionType):

    pass
class JTLMM_essentialocl_OrderedSetType(CollectionType):

    pass
class TupleLiteralPart:

    pass
class JTLMM_essentialocl_OpaqueExpression:

    pass
class OpaqueExpression:

    pass
class JTLMM_essentialocl_ExpressionInOcl(OpaqueExpression):

    pass
class CollectionLiteralExp:

    pass
class CollectionLiteralPart:

    pass
class JTLMM_essentialocl_CollectionItem(CollectionLiteralPart):

    pass
class JTLMM_essentialocl_CollectionRange(CollectionLiteralPart):

    pass
class LiteralExp:

    pass
class JTLMM_essentialocl_InvalidLiteralExp(LiteralExp):

    pass
class JTLMM_essentialocl_EnumLiteralExp(LiteralExp):

    pass
class JTLMM_template_TemplateExp(LiteralExp):

    pass
class JTLMM_essentialocl_NullLiteralExp(LiteralExp):

    pass
class JTLMM_essentialocl_TupleLiteralExp(LiteralExp):

    pass
class JTLMM_essentialocl_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, CollectionLiteralPart: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.CollectionLiteralPart = CollectionLiteralPart if CollectionLiteralPart is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def CollectionLiteralPart(self):
        return self.__CollectionLiteralPart

    @CollectionLiteralPart.setter
    def CollectionLiteralPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_essentialocl_CollectionLiteralExp__CollectionLiteralPart", None)
        self.__CollectionLiteralPart = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialocl126"):
                    opp_val = getattr(item, "essentialocl126", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialocl126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialocl126"):
                    opp_val = getattr(item, "essentialocl126", None)
                    
                    setattr(item, "essentialocl126", self)
                    

class JTLMM_imperativeocl_DictLiteralExp(LiteralExp):

    pass
class JTLMM_imperativeocl_AnonymousTupleLiteralExp(LiteralExp):

    pass
class JTLMM_essentialocl_PrimitiveLiteralExp(LiteralExp):

    pass
class FeaturePropertyCall:

    pass
class JTLMM_essentialocl_OperationCallExp(FeaturePropertyCall):

    pass
class JTLMM_essentialocl_PropertyCallExp(FeaturePropertyCall):

    pass
class ComputeExp:

    pass
class LetExp:

    pass
class LoopExp:

    pass
class JTLMM_essentialocl_IterateExp(LoopExp):

    pass
class JTLMM_essentialocl_IteratorExp(LoopExp):

    pass
class essentialocl_OclExpression:

    pass
class essentialocl_CallExp:

    pass
class JTLMM_imperativeocl_SwitchExp(imperativeocl_ImperativeExpression, essentialocl_CallExp):

    pass
class JTLMM_essentialocl_LoopExp(essentialocl_CallExp, essentialocl_OclExpression):

    pass
class NumericLiteralExp:

    pass
class JTLMM_essentialocl_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: float):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> float:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: float):
        self.__realSymbol = realSymbol

class JTLMM_essentialocl_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: int):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> int:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: int):
        self.__integerSymbol = integerSymbol

class JTLMM_essentialocl_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class TryExp:

    pass
class TypedElement:

    pass
class JTLMM_essentialocl_CollectionLiteralPart(TypedElement):

    pass
class JTLMM_essentialocl_TupleLiteralPart(TypedElement):

    pass
class JTLMM_essentialocl_OclExpression(TypedElement):

    pass
class JTLMM_essentialocl_Variable(TypedElement):

    pass
class PrimitiveLiteralExp:

    pass
class JTLMM_essentialocl_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class JTLMM_essentialocl_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class JTLMM_essentialocl_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: bool):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> bool:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: bool):
        self.__booleanSymbol = booleanSymbol

class OclExpression:

    pass
class JTLMM_essentialocl_VariableExp(OclExpression):

    pass
class JTLMM_essentialocl_TypeExp(OclExpression):

    pass
class JTLMM_essentialocl_IfExp(OclExpression):

    pass
class JTLMM_imperativeocl_ImperativeExpression(OclExpression):

    pass
class JTLMM_essentialocl_CallExp(OclExpression):

    pass
class JTLMM_essentialocl_LiteralExp(OclExpression):

    pass
class JTLMM_essentialocl_LetExp(OclExpression):

    pass
class TemplateExp:

    pass
class JTLMM_template_ObjectTemplateExp(TemplateExp):

    def __init__(self, referredClass: str, PropertyTemplateItem: set["PropertyTemplateItem"] = None, JTLMM_template_ObjectTemplateExp: set["AssignExp"] = None, TemplateExp: "JTLMM_JTL_Pattern"):
        self.referredClass = referredClass
        self.PropertyTemplateItem = PropertyTemplateItem if PropertyTemplateItem is not None else set()
        self.JTLMM_template_ObjectTemplateExp = JTLMM_template_ObjectTemplateExp if JTLMM_template_ObjectTemplateExp is not None else set()
        
    @property
    def referredClass(self) -> str:
        return self.__referredClass

    @referredClass.setter
    def referredClass(self, referredClass: str):
        self.__referredClass = referredClass

    @property
    def JTLMM_template_ObjectTemplateExp(self):
        return self.__JTLMM_template_ObjectTemplateExp

    @JTLMM_template_ObjectTemplateExp.setter
    def JTLMM_template_ObjectTemplateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_template_ObjectTemplateExp__JTLMM_template_ObjectTemplateExp", None)
        self.__JTLMM_template_ObjectTemplateExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssignExp"):
                    opp_val = getattr(item, "AssignExp", None)
                    
                    if opp_val == self:
                        setattr(item, "AssignExp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssignExp"):
                    opp_val = getattr(item, "AssignExp", None)
                    
                    setattr(item, "AssignExp", self)
                    

    @property
    def PropertyTemplateItem(self):
        return self.__PropertyTemplateItem

    @PropertyTemplateItem.setter
    def PropertyTemplateItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_template_ObjectTemplateExp__PropertyTemplateItem", None)
        self.__PropertyTemplateItem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "template"):
                    opp_val = getattr(item, "template", None)
                    
                    if opp_val == self:
                        setattr(item, "template", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "template"):
                    opp_val = getattr(item, "template", None)
                    
                    setattr(item, "template", self)
                    

class JTLMM_template_CollectionTemplateExp(TemplateExp):

    def __init__(self, kind: str, JTLMM_template_CollectionTemplateExp: set["OclExpression"] = None, JTLMM_template_CollectionTemplateExp165: "CollectionType" = None, JTLMM_template_CollectionTemplateExp167: "OclExpression" = None, TemplateExp: "JTLMM_JTL_Pattern"):
        self.kind = kind
        self.JTLMM_template_CollectionTemplateExp = JTLMM_template_CollectionTemplateExp if JTLMM_template_CollectionTemplateExp is not None else set()
        self.JTLMM_template_CollectionTemplateExp165 = JTLMM_template_CollectionTemplateExp165
        self.JTLMM_template_CollectionTemplateExp167 = JTLMM_template_CollectionTemplateExp167
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def JTLMM_template_CollectionTemplateExp167(self):
        return self.__JTLMM_template_CollectionTemplateExp167

    @JTLMM_template_CollectionTemplateExp167.setter
    def JTLMM_template_CollectionTemplateExp167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_template_CollectionTemplateExp__JTLMM_template_CollectionTemplateExp167", None)
        self.__JTLMM_template_CollectionTemplateExp167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression168"):
                opp_val = getattr(old_value, "OclExpression168", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression168"):
                opp_val = getattr(value, "OclExpression168", None)
                setattr(value, "OclExpression168", self)

    @property
    def JTLMM_template_CollectionTemplateExp(self):
        return self.__JTLMM_template_CollectionTemplateExp

    @JTLMM_template_CollectionTemplateExp.setter
    def JTLMM_template_CollectionTemplateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_template_CollectionTemplateExp__JTLMM_template_CollectionTemplateExp", None)
        self.__JTLMM_template_CollectionTemplateExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression163"):
                    opp_val = getattr(item, "OclExpression163", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression163"):
                    opp_val = getattr(item, "OclExpression163", None)
                    
                    setattr(item, "OclExpression163", self)
                    

    @property
    def JTLMM_template_CollectionTemplateExp165(self):
        return self.__JTLMM_template_CollectionTemplateExp165

    @JTLMM_template_CollectionTemplateExp165.setter
    def JTLMM_template_CollectionTemplateExp165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_template_CollectionTemplateExp__JTLMM_template_CollectionTemplateExp165", None)
        self.__JTLMM_template_CollectionTemplateExp165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CollectionType"):
                opp_val = getattr(old_value, "CollectionType", None)
                if opp_val == self:
                    setattr(old_value, "CollectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CollectionType"):
                opp_val = getattr(value, "CollectionType", None)
                setattr(value, "CollectionType", self)

class Predicate:

    pass
class Domain:

    pass
class Transformation:

    pass
class Relation:

    pass
class Model:

    pass
class Variable:

    pass
class Pattern:

    pass
class emof_Package:

    pass
class emof_Class:

    pass
class JTLMM_essentialocl_AnyType(emof_Class, emof_Type):

    pass
class JTLMM_essentialocl_TupleType(emof_Class, emof_DataType):

    pass
class JTLMM_JTL_Transformation(emof_Class, emof_Package):

    pass
class Extent:

    pass
class JTLMM_emof_URIExtent(Extent):

    pass
class JTLMM_emof_MultiplicityElement(ABC):

    def __init__(self, lower: int, upper: str, isOrdered: str, isUnique: str):
        self.lower = lower
        self.upper = upper
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

class Parameter:

    pass
class emof_TypedElement:

    pass
class Enumeration:

    pass
class Package:

    pass
class NamedElement:

    pass
class JTLMM_JTL_Relation(NamedElement):

    def __init__(self, isTopLevel: bool, Pattern: "Pattern" = None, Pattern45: "Pattern" = None, JTLMM_JTL_Relation: set["Variable"] = None, Transformation: "Transformation" = None, Domain: set["Domain"] = None, NamedElement: "JTLMM_emof_Comment"):
        self.isTopLevel = isTopLevel
        self.Pattern = Pattern
        self.Pattern45 = Pattern45
        self.JTLMM_JTL_Relation = JTLMM_JTL_Relation if JTLMM_JTL_Relation is not None else set()
        self.Transformation = Transformation
        self.Domain = Domain if Domain is not None else set()
        
    @property
    def isTopLevel(self) -> bool:
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: bool):
        self.__isTopLevel = isTopLevel

    @property
    def Pattern45(self):
        return self.__Pattern45

    @Pattern45.setter
    def Pattern45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Relation__Pattern45", None)
        self.__Pattern45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL46"):
                opp_val = getattr(old_value, "JTL46", None)
                if opp_val == self:
                    setattr(old_value, "JTL46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL46"):
                opp_val = getattr(value, "JTL46", None)
                setattr(value, "JTL46", self)

    @property
    def Transformation(self):
        return self.__Transformation

    @Transformation.setter
    def Transformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Relation__Transformation", None)
        self.__Transformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL39"):
                opp_val = getattr(old_value, "JTL39", None)
                if opp_val == self:
                    setattr(old_value, "JTL39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL39"):
                opp_val = getattr(value, "JTL39", None)
                setattr(value, "JTL39", self)

    @property
    def JTLMM_JTL_Relation(self):
        return self.__JTLMM_JTL_Relation

    @JTLMM_JTL_Relation.setter
    def JTLMM_JTL_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Relation__JTLMM_JTL_Relation", None)
        self.__JTLMM_JTL_Relation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    setattr(item, "Variable", self)
                    

    @property
    def Domain(self):
        return self.__Domain

    @Domain.setter
    def Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Relation__Domain", None)
        self.__Domain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JTL41"):
                    opp_val = getattr(item, "JTL41", None)
                    
                    if opp_val == self:
                        setattr(item, "JTL41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JTL41"):
                    opp_val = getattr(item, "JTL41", None)
                    
                    setattr(item, "JTL41", self)
                    

    @property
    def Pattern(self):
        return self.__Pattern

    @Pattern.setter
    def Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Relation__Pattern", None)
        self.__Pattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL43"):
                opp_val = getattr(old_value, "JTL43", None)
                if opp_val == self:
                    setattr(old_value, "JTL43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL43"):
                opp_val = getattr(value, "JTL43", None)
                setattr(value, "JTL43", self)

class JTLMM_JTL_Domain(NamedElement):

    def __init__(self, isCheckable: bool, isEnforceable: bool, Relation49: "Relation" = None, JTLMM_JTL_Domain: "Pattern" = None, JTLMM_JTL_Domain54: "Model" = None, JTLMM_JTL_Domain57: "Variable" = None, NamedElement: "JTLMM_emof_Comment"):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.Relation49 = Relation49
        self.JTLMM_JTL_Domain = JTLMM_JTL_Domain
        self.JTLMM_JTL_Domain54 = JTLMM_JTL_Domain54
        self.JTLMM_JTL_Domain57 = JTLMM_JTL_Domain57
        
    @property
    def isCheckable(self) -> bool:
        return self.__isCheckable

    @isCheckable.setter
    def isCheckable(self, isCheckable: bool):
        self.__isCheckable = isCheckable

    @property
    def isEnforceable(self) -> bool:
        return self.__isEnforceable

    @isEnforceable.setter
    def isEnforceable(self, isEnforceable: bool):
        self.__isEnforceable = isEnforceable

    @property
    def JTLMM_JTL_Domain57(self):
        return self.__JTLMM_JTL_Domain57

    @JTLMM_JTL_Domain57.setter
    def JTLMM_JTL_Domain57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Domain__JTLMM_JTL_Domain57", None)
        self.__JTLMM_JTL_Domain57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable58"):
                opp_val = getattr(old_value, "Variable58", None)
                if opp_val == self:
                    setattr(old_value, "Variable58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable58"):
                opp_val = getattr(value, "Variable58", None)
                setattr(value, "Variable58", self)

    @property
    def JTLMM_JTL_Domain54(self):
        return self.__JTLMM_JTL_Domain54

    @JTLMM_JTL_Domain54.setter
    def JTLMM_JTL_Domain54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Domain__JTLMM_JTL_Domain54", None)
        self.__JTLMM_JTL_Domain54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model55"):
                opp_val = getattr(old_value, "Model55", None)
                if opp_val == self:
                    setattr(old_value, "Model55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model55"):
                opp_val = getattr(value, "Model55", None)
                setattr(value, "Model55", self)

    @property
    def JTLMM_JTL_Domain(self):
        return self.__JTLMM_JTL_Domain

    @JTLMM_JTL_Domain.setter
    def JTLMM_JTL_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Domain__JTLMM_JTL_Domain", None)
        self.__JTLMM_JTL_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern52"):
                opp_val = getattr(old_value, "Pattern52", None)
                if opp_val == self:
                    setattr(old_value, "Pattern52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern52"):
                opp_val = getattr(value, "Pattern52", None)
                setattr(value, "Pattern52", self)

    @property
    def Relation49(self):
        return self.__Relation49

    @Relation49.setter
    def Relation49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Domain__Relation49", None)
        self.__Relation49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL50"):
                opp_val = getattr(old_value, "JTL50", None)
                if opp_val == self:
                    setattr(old_value, "JTL50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL50"):
                opp_val = getattr(value, "JTL50", None)
                setattr(value, "JTL50", self)

class JTLMM_emof_TypedElement(NamedElement):

    def __init__(self, type: str, NamedElement: "JTLMM_emof_Comment"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class JTLMM_JTL_Model(NamedElement):

    def __init__(self, usedPackage: str, Transformation60: "Transformation" = None, JTLMM_JTL_Model: set["Model"] = None, NamedElement: "JTLMM_emof_Comment"):
        self.usedPackage = usedPackage
        self.Transformation60 = Transformation60
        self.JTLMM_JTL_Model = JTLMM_JTL_Model if JTLMM_JTL_Model is not None else set()
        
    @property
    def usedPackage(self) -> str:
        return self.__usedPackage

    @usedPackage.setter
    def usedPackage(self, usedPackage: str):
        self.__usedPackage = usedPackage

    @property
    def JTLMM_JTL_Model(self):
        return self.__JTLMM_JTL_Model

    @JTLMM_JTL_Model.setter
    def JTLMM_JTL_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Model__JTLMM_JTL_Model", None)
        self.__JTLMM_JTL_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Model63"):
                    opp_val = getattr(item, "Model63", None)
                    
                    if opp_val == self:
                        setattr(item, "Model63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model63"):
                    opp_val = getattr(item, "Model63", None)
                    
                    setattr(item, "Model63", self)
                    

    @property
    def Transformation60(self):
        return self.__Transformation60

    @Transformation60.setter
    def Transformation60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Model__Transformation60", None)
        self.__Transformation60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL61"):
                opp_val = getattr(old_value, "JTL61", None)
                if opp_val == self:
                    setattr(old_value, "JTL61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL61"):
                opp_val = getattr(value, "JTL61", None)
                setattr(value, "JTL61", self)

class JTLMM_emof_Type(NamedElement):

    pass
class JTLMM_emof_EnumerationLiteral(NamedElement):

    pass
class JTLMM_emof_Package(NamedElement):

    def __init__(self, uri: str, Type18: set["Type"] = None, JTLMM_emof_Package: set["Package"] = None, NamedElement: "JTLMM_emof_Comment"):
        self.uri = uri
        self.Type18 = Type18 if Type18 is not None else set()
        self.JTLMM_emof_Package = JTLMM_emof_Package if JTLMM_emof_Package is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def JTLMM_emof_Package(self):
        return self.__JTLMM_emof_Package

    @JTLMM_emof_Package.setter
    def JTLMM_emof_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Package__JTLMM_emof_Package", None)
        self.__JTLMM_emof_Package = value if value is not None else set()
        
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
                    

    @property
    def Type18(self):
        return self.__Type18

    @Type18.setter
    def Type18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Package__Type18", None)
        self.__Type18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emof19"):
                    opp_val = getattr(item, "emof19", None)
                    
                    if opp_val == self:
                        setattr(item, "emof19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emof19"):
                    opp_val = getattr(item, "emof19", None)
                    
                    setattr(item, "emof19", self)
                    

class Object:

    pass
class JTLMM_emof_Element(Object):

    pass
class Class:

    pass
class JTLMM_imperativeocl_AnonymousTupleType(Class):

    pass
class JTLMM_imperativeocl_Typedef(Class):

    pass
class Operation:

    pass
class emof_MultiplicityElement:

    pass
class JTLMM_emof_Property(emof_MultiplicityElement, emof_TypedElement):

    def __init__(self, default: str, isReadOnly: bool, isDerived: bool, isComposite: bool, isId: bool, Class30: "Class" = None, JTLMM_emof_Property: "Property" = None):
        self.default = default
        self.isReadOnly = isReadOnly
        self.isDerived = isDerived
        self.isComposite = isComposite
        self.isId = isId
        self.Class30 = Class30
        self.JTLMM_emof_Property = JTLMM_emof_Property
        
    @property
    def isId(self) -> bool:
        return self.__isId

    @isId.setter
    def isId(self, isId: bool):
        self.__isId = isId

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def JTLMM_emof_Property(self):
        return self.__JTLMM_emof_Property

    @JTLMM_emof_Property.setter
    def JTLMM_emof_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Property__JTLMM_emof_Property", None)
        self.__JTLMM_emof_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property33"):
                opp_val = getattr(old_value, "Property33", None)
                if opp_val == self:
                    setattr(old_value, "Property33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property33"):
                opp_val = getattr(value, "Property33", None)
                setattr(value, "Property33", self)

    @property
    def Class30(self):
        return self.__Class30

    @Class30.setter
    def Class30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Property__Class30", None)
        self.__Class30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emof31"):
                opp_val = getattr(old_value, "emof31", None)
                if opp_val == self:
                    setattr(old_value, "emof31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emof31"):
                opp_val = getattr(value, "emof31", None)
                setattr(value, "emof31", self)

class JTLMM_emof_Parameter(emof_MultiplicityElement, emof_TypedElement):

    pass
class JTLMM_emof_Operation(emof_MultiplicityElement, emof_TypedElement):

    pass
class JTLMM_emof_Object:

    pass
class JTLMM_emof_Extent(Object):

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class JTLMM_emof_PrimitiveType(DataType):

    pass
class JTLMM_essentialocl_CollectionType(DataType):

    pass
class JTLMM_emof_Enumeration(DataType):

    pass
class Element:

    pass
class JTLMM_template_PropertyTemplateItem(Element):

    pass
class JTLMM_JTL_Pattern(Element):

    pass
class JTLMM_imperativeocl_DictLiteralPart(Element):

    pass
class JTLMM_emof_NamedElement(Element):

    def __init__(self, name: str, emof8: "JTLMM_emof_Tag", Element253: "JTLMM_imperativeocl_LogExp"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class JTLMM_emof_Comment(Element):

    pass
class JTLMM_imperativeocl_AnonymousTupleLiteralPart(Element):

    pass
class JTLMM_JTL_Predicate(Element):

    pass
class JTLMM_emof_Tag(Element):

    def __init__(self, value: str, name: str, Element: set["Element"] = None, emof8: "JTLMM_emof_Tag", Element253: "JTLMM_imperativeocl_LogExp"):
        self.value = value
        self.name = name
        self.Element = Element if Element is not None else set()
        
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
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Tag__Element", None)
        self.__Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emof8"):
                    opp_val = getattr(item, "emof8", None)
                    
                    if opp_val == self:
                        setattr(item, "emof8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emof8"):
                    opp_val = getattr(item, "emof8", None)
                    
                    setattr(item, "emof8", self)
                    

class Comment:

    pass
class Tag:

    pass
class Property:

    pass
class Type:

    pass
class JTLMM_imperativeocl_TemplateParameterType(Type):

    def __init__(self, specification: str, Type: "JTLMM_emof_Operation", Type225: "JTLMM_imperativeocl_RaiseExp", Type242: "JTLMM_imperativeocl_DictionaryType", Type229: "JTLMM_imperativeocl_Typedef", Type112: "JTLMM_essentialocl_TypeExp", Type265: "JTLMM_imperativeocl_AnonymousTupleType", Type220: "JTLMM_imperativeocl_TryExp", Type152: "JTLMM_essentialocl_CollectionType", emof19: "JTLMM_emof_Package"):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class JTLMM_emof_DataType(Type):

    pass
class JTLMM_essentialocl_VoidType(Type):

    pass
class JTLMM_essentialocl_InvalidType(Type):

    pass
class JTLMM_emof_Class(Type):

    def __init__(self, isAbstract: bool, Property: set["Property"] = None, Operation: set["Operation"] = None, JTLMM_emof_Class: set["Class"] = None, Type: "JTLMM_emof_Operation", Type225: "JTLMM_imperativeocl_RaiseExp", Type242: "JTLMM_imperativeocl_DictionaryType", Type229: "JTLMM_imperativeocl_Typedef", Type112: "JTLMM_essentialocl_TypeExp", Type265: "JTLMM_imperativeocl_AnonymousTupleType", Type220: "JTLMM_imperativeocl_TryExp", Type152: "JTLMM_essentialocl_CollectionType", emof19: "JTLMM_emof_Package"):
        self.isAbstract = isAbstract
        self.Property = Property if Property is not None else set()
        self.Operation = Operation if Operation is not None else set()
        self.JTLMM_emof_Class = JTLMM_emof_Class if JTLMM_emof_Class is not None else set()
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Class__Operation", None)
        self.__Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emof2"):
                    opp_val = getattr(item, "emof2", None)
                    
                    if opp_val == self:
                        setattr(item, "emof2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emof2"):
                    opp_val = getattr(item, "emof2", None)
                    
                    setattr(item, "emof2", self)
                    

    @property
    def JTLMM_emof_Class(self):
        return self.__JTLMM_emof_Class

    @JTLMM_emof_Class.setter
    def JTLMM_emof_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Class__JTLMM_emof_Class", None)
        self.__JTLMM_emof_Class = value if value is not None else set()
        
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
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Class__Property", None)
        self.__Property = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emof"):
                    opp_val = getattr(item, "emof", None)
                    
                    if opp_val == self:
                        setattr(item, "emof", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emof"):
                    opp_val = getattr(item, "emof", None)
                    
                    setattr(item, "emof", self)
                    

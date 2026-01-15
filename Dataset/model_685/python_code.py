from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SeverityKind(Enum):
    error = "error"
    fatal = "fatal"
    warning = "warning"
class CollectionKind(Enum):
    OrderedSet = "OrderedSet"
    Set = "Set"
    Bag = "Bag"
    Sequence = "Sequence"


############################################
# Definition of Classes
############################################

class AnonymousTupleLiteralPart:

    pass
class essentialocl_LoopExp:

    pass
class LogExp:

    pass
class DictLiteralPart:

    pass
class AltExp:

    pass
class imperativeocl_ImperativeExpression:

    pass
class JTL_imperativeocl_ImperativeLoopExp(imperativeocl_ImperativeExpression, essentialocl_LoopExp):

    pass
class ImperativeExpression:

    pass
class JTL_imperativeocl_WhileExp(ImperativeExpression):

    pass
class JTL_imperativeocl_BreakExp(ImperativeExpression):

    pass
class JTL_imperativeocl_AltExp(ImperativeExpression):

    pass
class JTL_imperativeocl_LogExp(ImperativeExpression):

    def __init__(self, text: str, level: int, JTL_imperativeocl_LogExp: "OclExpression" = None, JTL_imperativeocl_LogExp250: "Element" = None):
        self.text = text
        self.level = level
        self.JTL_imperativeocl_LogExp = JTL_imperativeocl_LogExp
        self.JTL_imperativeocl_LogExp250 = JTL_imperativeocl_LogExp250
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def JTL_imperativeocl_LogExp(self):
        return self.__JTL_imperativeocl_LogExp

    @JTL_imperativeocl_LogExp.setter
    def JTL_imperativeocl_LogExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_LogExp__JTL_imperativeocl_LogExp", None)
        self.__JTL_imperativeocl_LogExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression248"):
                opp_val = getattr(old_value, "OclExpression248", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression248"):
                opp_val = getattr(value, "OclExpression248", None)
                setattr(value, "OclExpression248", self)

    @property
    def JTL_imperativeocl_LogExp250(self):
        return self.__JTL_imperativeocl_LogExp250

    @JTL_imperativeocl_LogExp250.setter
    def JTL_imperativeocl_LogExp250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_LogExp__JTL_imperativeocl_LogExp250", None)
        self.__JTL_imperativeocl_LogExp250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element251"):
                opp_val = getattr(old_value, "Element251", None)
                if opp_val == self:
                    setattr(old_value, "Element251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element251"):
                opp_val = getattr(value, "Element251", None)
                setattr(value, "Element251", self)

class JTL_imperativeocl_InstantiationExp(ImperativeExpression):

    pass
class JTL_imperativeocl_TupleExp(ImperativeExpression):

    pass
class JTL_imperativeocl_ContinueExp(ImperativeExpression):

    pass
class JTL_imperativeocl_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: bool, JTL_imperativeocl_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.JTL_imperativeocl_VariableInitExp = JTL_imperativeocl_VariableInitExp
        
    @property
    def withResult(self) -> bool:
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: bool):
        self.__withResult = withResult

    @property
    def JTL_imperativeocl_VariableInitExp(self):
        return self.__JTL_imperativeocl_VariableInitExp

    @JTL_imperativeocl_VariableInitExp.setter
    def JTL_imperativeocl_VariableInitExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_VariableInitExp__JTL_imperativeocl_VariableInitExp", None)
        self.__JTL_imperativeocl_VariableInitExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable191"):
                opp_val = getattr(old_value, "Variable191", None)
                if opp_val == self:
                    setattr(old_value, "Variable191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable191"):
                opp_val = getattr(value, "Variable191", None)
                setattr(value, "Variable191", self)

class JTL_imperativeocl_ComputeExp(ImperativeExpression):

    pass
class JTL_imperativeocl_RaiseExp(ImperativeExpression):

    pass
class JTL_imperativeocl_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, JTL_imperativeocl_AssertExp: "LogExp" = None, JTL_imperativeocl_AssertExp254: "OclExpression" = None):
        self.severity = severity
        self.JTL_imperativeocl_AssertExp = JTL_imperativeocl_AssertExp
        self.JTL_imperativeocl_AssertExp254 = JTL_imperativeocl_AssertExp254
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def JTL_imperativeocl_AssertExp(self):
        return self.__JTL_imperativeocl_AssertExp

    @JTL_imperativeocl_AssertExp.setter
    def JTL_imperativeocl_AssertExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_AssertExp__JTL_imperativeocl_AssertExp", None)
        self.__JTL_imperativeocl_AssertExp = value
        
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

    @property
    def JTL_imperativeocl_AssertExp254(self):
        return self.__JTL_imperativeocl_AssertExp254

    @JTL_imperativeocl_AssertExp254.setter
    def JTL_imperativeocl_AssertExp254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_AssertExp__JTL_imperativeocl_AssertExp254", None)
        self.__JTL_imperativeocl_AssertExp254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression255"):
                opp_val = getattr(old_value, "OclExpression255", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression255"):
                opp_val = getattr(value, "OclExpression255", None)
                setattr(value, "OclExpression255", self)

class JTL_imperativeocl_TryExp(ImperativeExpression):

    pass
class JTL_imperativeocl_UnlinkExp(ImperativeExpression):

    pass
class JTL_imperativeocl_ReturnExp(ImperativeExpression):

    pass
class JTL_imperativeocl_UnpackExp(ImperativeExpression):

    pass
class JTL_imperativeocl_AssignExp(ImperativeExpression):

    def __init__(self, isReset: bool, JTL_imperativeocl_AssignExp179: "OclExpression" = None, JTL_imperativeocl_AssignExp182: "OclExpression" = None, JTL_imperativeocl_AssignExp: set["OclExpression"] = None):
        self.isReset = isReset
        self.JTL_imperativeocl_AssignExp179 = JTL_imperativeocl_AssignExp179
        self.JTL_imperativeocl_AssignExp182 = JTL_imperativeocl_AssignExp182
        self.JTL_imperativeocl_AssignExp = JTL_imperativeocl_AssignExp if JTL_imperativeocl_AssignExp is not None else set()
        
    @property
    def isReset(self) -> bool:
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: bool):
        self.__isReset = isReset

    @property
    def JTL_imperativeocl_AssignExp179(self):
        return self.__JTL_imperativeocl_AssignExp179

    @JTL_imperativeocl_AssignExp179.setter
    def JTL_imperativeocl_AssignExp179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_AssignExp__JTL_imperativeocl_AssignExp179", None)
        self.__JTL_imperativeocl_AssignExp179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression180"):
                opp_val = getattr(old_value, "OclExpression180", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression180"):
                opp_val = getattr(value, "OclExpression180", None)
                setattr(value, "OclExpression180", self)

    @property
    def JTL_imperativeocl_AssignExp(self):
        return self.__JTL_imperativeocl_AssignExp

    @JTL_imperativeocl_AssignExp.setter
    def JTL_imperativeocl_AssignExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_AssignExp__JTL_imperativeocl_AssignExp", None)
        self.__JTL_imperativeocl_AssignExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression177"):
                    opp_val = getattr(item, "OclExpression177", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression177"):
                    opp_val = getattr(item, "OclExpression177", None)
                    
                    setattr(item, "OclExpression177", self)
                    

    @property
    def JTL_imperativeocl_AssignExp182(self):
        return self.__JTL_imperativeocl_AssignExp182

    @JTL_imperativeocl_AssignExp182.setter
    def JTL_imperativeocl_AssignExp182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_AssignExp__JTL_imperativeocl_AssignExp182", None)
        self.__JTL_imperativeocl_AssignExp182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression183"):
                opp_val = getattr(old_value, "OclExpression183", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression183"):
                opp_val = getattr(value, "OclExpression183", None)
                setattr(value, "OclExpression183", self)

class JTL_imperativeocl_BlockExp(ImperativeExpression):

    pass
class ObjectTemplateExp:

    pass
class ImperativeLoopExp:

    pass
class JTL_imperativeocl_CollectorExp(ImperativeLoopExp):

    pass
class JTL_imperativeocl_ForExp(ImperativeLoopExp):

    pass
class JTL_imperativeocl_ImperativeIterateExp(ImperativeLoopExp):

    pass
class AssignExp:

    pass
class PropertyTemplateItem:

    pass
class emof_Type:

    pass
class emof_DataType:

    pass
class CollectionType:

    pass
class JTL_imperativeocl_ListType(CollectionType):

    pass
class JTL_imperativeocl_DictionaryType(CollectionType):

    pass
class JTL_essentialocl_BagType(CollectionType):

    pass
class TupleLiteralExp:

    pass
class JTL_essentialocl_SetType(CollectionType):

    pass
class JTL_essentialocl_SequenceType(CollectionType):

    pass
class JTL_essentialocl_OrderedSetType(CollectionType):

    pass
class OpaqueExpression:

    pass
class JTL_essentialocl_ExpressionInOcl(OpaqueExpression):

    pass
class CallExp:

    pass
class JTL_essentialocl_FeaturePropertyCall(CallExp):

    pass
class JTL_essentialocl_OpaqueExpression:

    pass
class TupleLiteralPart:

    pass
class LiteralExp:

    pass
class JTL_imperativeocl_DictLiteralExp(LiteralExp):

    pass
class JTL_imperativeocl_AnonymousTupleLiteralExp(LiteralExp):

    pass
class JTL_essentialocl_TupleLiteralExp(LiteralExp):

    pass
class JTL_essentialocl_InvalidLiteralExp(LiteralExp):

    pass
class JTL_essentialocl_NullLiteralExp(LiteralExp):

    pass
class JTL_essentialocl_CollectionLiteralExp(LiteralExp):

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
        old_value = getattr(self, f"_JTL_essentialocl_CollectionLiteralExp__CollectionLiteralPart", None)
        self.__CollectionLiteralPart = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialocl124"):
                    opp_val = getattr(item, "essentialocl124", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialocl124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialocl124"):
                    opp_val = getattr(item, "essentialocl124", None)
                    
                    setattr(item, "essentialocl124", self)
                    

class JTL_essentialocl_EnumLiteralExp(LiteralExp):

    pass
class JTL_template_TemplateExp(LiteralExp):

    pass
class JTL_essentialocl_PrimitiveLiteralExp(LiteralExp):

    pass
class CollectionLiteralExp:

    pass
class CollectionLiteralPart:

    pass
class JTL_essentialocl_CollectionRange(CollectionLiteralPart):

    pass
class JTL_essentialocl_CollectionItem(CollectionLiteralPart):

    pass
class LoopExp:

    pass
class JTL_essentialocl_IterateExp(LoopExp):

    pass
class JTL_essentialocl_IteratorExp(LoopExp):

    pass
class essentialocl_OclExpression:

    pass
class essentialocl_CallExp:

    pass
class JTL_imperativeocl_SwitchExp(imperativeocl_ImperativeExpression, essentialocl_CallExp):

    pass
class JTL_essentialocl_LoopExp(essentialocl_OclExpression, essentialocl_CallExp):

    pass
class LetExp:

    pass
class FeaturePropertyCall:

    pass
class JTL_essentialocl_OperationCallExp(FeaturePropertyCall):

    pass
class JTL_essentialocl_PropertyCallExp(FeaturePropertyCall):

    pass
class ComputeExp:

    pass
class NumericLiteralExp:

    pass
class JTL_essentialocl_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: float):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> float:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: float):
        self.__realSymbol = realSymbol

class JTL_essentialocl_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: int):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> int:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: int):
        self.__integerSymbol = integerSymbol

class JTL_essentialocl_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class PrimitiveLiteralExp:

    pass
class JTL_essentialocl_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class JTL_essentialocl_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class JTL_essentialocl_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: bool):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> bool:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: bool):
        self.__booleanSymbol = booleanSymbol

class TryExp:

    pass
class TypedElement:

    pass
class JTL_essentialocl_TupleLiteralPart(TypedElement):

    pass
class JTL_essentialocl_CollectionLiteralPart(TypedElement):

    pass
class JTL_essentialocl_Variable(TypedElement):

    pass
class JTL_essentialocl_OclExpression(TypedElement):

    pass
class OclExpression:

    pass
class JTL_essentialocl_TypeExp(OclExpression):

    pass
class JTL_essentialocl_IfExp(OclExpression):

    pass
class JTL_essentialocl_CallExp(OclExpression):

    pass
class JTL_essentialocl_LiteralExp(OclExpression):

    pass
class JTL_essentialocl_LetExp(OclExpression):

    pass
class JTL_imperativeocl_ImperativeExpression(OclExpression):

    pass
class JTL_essentialocl_VariableExp(OclExpression):

    pass
class TemplateExp:

    pass
class JTL_template_CollectionTemplateExp(TemplateExp):

    def __init__(self, kind: str, JTL_template_CollectionTemplateExp: set["OclExpression"] = None, JTL_template_CollectionTemplateExp163: "CollectionType" = None, JTL_template_CollectionTemplateExp165: "OclExpression" = None, TemplateExp: "JTL_JTL_Pattern"):
        self.kind = kind
        self.JTL_template_CollectionTemplateExp = JTL_template_CollectionTemplateExp if JTL_template_CollectionTemplateExp is not None else set()
        self.JTL_template_CollectionTemplateExp163 = JTL_template_CollectionTemplateExp163
        self.JTL_template_CollectionTemplateExp165 = JTL_template_CollectionTemplateExp165
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def JTL_template_CollectionTemplateExp(self):
        return self.__JTL_template_CollectionTemplateExp

    @JTL_template_CollectionTemplateExp.setter
    def JTL_template_CollectionTemplateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_template_CollectionTemplateExp__JTL_template_CollectionTemplateExp", None)
        self.__JTL_template_CollectionTemplateExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression161"):
                    opp_val = getattr(item, "OclExpression161", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression161"):
                    opp_val = getattr(item, "OclExpression161", None)
                    
                    setattr(item, "OclExpression161", self)
                    

    @property
    def JTL_template_CollectionTemplateExp163(self):
        return self.__JTL_template_CollectionTemplateExp163

    @JTL_template_CollectionTemplateExp163.setter
    def JTL_template_CollectionTemplateExp163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_template_CollectionTemplateExp__JTL_template_CollectionTemplateExp163", None)
        self.__JTL_template_CollectionTemplateExp163 = value
        
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

    @property
    def JTL_template_CollectionTemplateExp165(self):
        return self.__JTL_template_CollectionTemplateExp165

    @JTL_template_CollectionTemplateExp165.setter
    def JTL_template_CollectionTemplateExp165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_template_CollectionTemplateExp__JTL_template_CollectionTemplateExp165", None)
        self.__JTL_template_CollectionTemplateExp165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression166"):
                opp_val = getattr(old_value, "OclExpression166", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression166"):
                opp_val = getattr(value, "OclExpression166", None)
                setattr(value, "OclExpression166", self)

class JTL_template_ObjectTemplateExp(TemplateExp):

    def __init__(self, referredClass: str, PropertyTemplateItem: set["PropertyTemplateItem"] = None, JTL_template_ObjectTemplateExp: set["AssignExp"] = None, TemplateExp: "JTL_JTL_Pattern"):
        self.referredClass = referredClass
        self.PropertyTemplateItem = PropertyTemplateItem if PropertyTemplateItem is not None else set()
        self.JTL_template_ObjectTemplateExp = JTL_template_ObjectTemplateExp if JTL_template_ObjectTemplateExp is not None else set()
        
    @property
    def referredClass(self) -> str:
        return self.__referredClass

    @referredClass.setter
    def referredClass(self, referredClass: str):
        self.__referredClass = referredClass

    @property
    def PropertyTemplateItem(self):
        return self.__PropertyTemplateItem

    @PropertyTemplateItem.setter
    def PropertyTemplateItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_template_ObjectTemplateExp__PropertyTemplateItem", None)
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
                    

    @property
    def JTL_template_ObjectTemplateExp(self):
        return self.__JTL_template_ObjectTemplateExp

    @JTL_template_ObjectTemplateExp.setter
    def JTL_template_ObjectTemplateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_template_ObjectTemplateExp__JTL_template_ObjectTemplateExp", None)
        self.__JTL_template_ObjectTemplateExp = value if value is not None else set()
        
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
                    

class Predicate:

    pass
class Pattern:

    pass
class JTL_JTL_Where(Pattern):

    pass
class JTL_JTL_When(Pattern):

    pass
class Transformation:

    pass
class Variable:

    pass
class When:

    pass
class Where:

    pass
class Domain:

    pass
class Extent:

    pass
class Relation:

    pass
class Model:

    pass
class emof_Package:

    pass
class emof_Class:

    pass
class JTL_essentialocl_AnyType(emof_Class, emof_Type):

    pass
class JTL_essentialocl_TupleType(emof_DataType, emof_Class):

    pass
class JTL_JTL_Transformation(emof_Class, emof_Package):

    pass
class JTL_emof_URIExtent(Extent):

    pass
class Package:

    pass
class Enumeration:

    pass
class NamedElement:

    pass
class JTL_JTL_Domain(NamedElement):

    def __init__(self, isCheckable: bool, isEnforceable: bool, Relation48: "Relation" = None, JTL_JTL_Domain: "Pattern" = None, JTL_JTL_Domain52: "Model" = None, JTL_JTL_Domain55: "Variable" = None, NamedElement: "JTL_emof_Comment"):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.Relation48 = Relation48
        self.JTL_JTL_Domain = JTL_JTL_Domain
        self.JTL_JTL_Domain52 = JTL_JTL_Domain52
        self.JTL_JTL_Domain55 = JTL_JTL_Domain55
        
    @property
    def isEnforceable(self) -> bool:
        return self.__isEnforceable

    @isEnforceable.setter
    def isEnforceable(self, isEnforceable: bool):
        self.__isEnforceable = isEnforceable

    @property
    def isCheckable(self) -> bool:
        return self.__isCheckable

    @isCheckable.setter
    def isCheckable(self, isCheckable: bool):
        self.__isCheckable = isCheckable

    @property
    def JTL_JTL_Domain55(self):
        return self.__JTL_JTL_Domain55

    @JTL_JTL_Domain55.setter
    def JTL_JTL_Domain55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Domain__JTL_JTL_Domain55", None)
        self.__JTL_JTL_Domain55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable56"):
                opp_val = getattr(old_value, "Variable56", None)
                if opp_val == self:
                    setattr(old_value, "Variable56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable56"):
                opp_val = getattr(value, "Variable56", None)
                setattr(value, "Variable56", self)

    @property
    def JTL_JTL_Domain52(self):
        return self.__JTL_JTL_Domain52

    @JTL_JTL_Domain52.setter
    def JTL_JTL_Domain52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Domain__JTL_JTL_Domain52", None)
        self.__JTL_JTL_Domain52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model53"):
                opp_val = getattr(old_value, "Model53", None)
                if opp_val == self:
                    setattr(old_value, "Model53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model53"):
                opp_val = getattr(value, "Model53", None)
                setattr(value, "Model53", self)

    @property
    def Relation48(self):
        return self.__Relation48

    @Relation48.setter
    def Relation48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Domain__Relation48", None)
        self.__Relation48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL49"):
                opp_val = getattr(old_value, "JTL49", None)
                if opp_val == self:
                    setattr(old_value, "JTL49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL49"):
                opp_val = getattr(value, "JTL49", None)
                setattr(value, "JTL49", self)

    @property
    def JTL_JTL_Domain(self):
        return self.__JTL_JTL_Domain

    @JTL_JTL_Domain.setter
    def JTL_JTL_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Domain__JTL_JTL_Domain", None)
        self.__JTL_JTL_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern"):
                opp_val = getattr(old_value, "Pattern", None)
                if opp_val == self:
                    setattr(old_value, "Pattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern"):
                opp_val = getattr(value, "Pattern", None)
                setattr(value, "Pattern", self)

class JTL_emof_EnumerationLiteral(NamedElement):

    pass
class JTL_JTL_Model(NamedElement):

    def __init__(self, usedPackage: str, Transformation58: "Transformation" = None, JTL_JTL_Model: set["Model"] = None, NamedElement: "JTL_emof_Comment"):
        self.usedPackage = usedPackage
        self.Transformation58 = Transformation58
        self.JTL_JTL_Model = JTL_JTL_Model if JTL_JTL_Model is not None else set()
        
    @property
    def usedPackage(self) -> str:
        return self.__usedPackage

    @usedPackage.setter
    def usedPackage(self, usedPackage: str):
        self.__usedPackage = usedPackage

    @property
    def Transformation58(self):
        return self.__Transformation58

    @Transformation58.setter
    def Transformation58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Model__Transformation58", None)
        self.__Transformation58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL59"):
                opp_val = getattr(old_value, "JTL59", None)
                if opp_val == self:
                    setattr(old_value, "JTL59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL59"):
                opp_val = getattr(value, "JTL59", None)
                setattr(value, "JTL59", self)

    @property
    def JTL_JTL_Model(self):
        return self.__JTL_JTL_Model

    @JTL_JTL_Model.setter
    def JTL_JTL_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Model__JTL_JTL_Model", None)
        self.__JTL_JTL_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Model61"):
                    opp_val = getattr(item, "Model61", None)
                    
                    if opp_val == self:
                        setattr(item, "Model61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model61"):
                    opp_val = getattr(item, "Model61", None)
                    
                    setattr(item, "Model61", self)
                    

class JTL_emof_Type(NamedElement):

    pass
class JTL_JTL_Relation(NamedElement):

    def __init__(self, isTopLevel: bool, Domain: set["Domain"] = None, Where: "Where" = None, When: "When" = None, JTL_JTL_Relation: set["Variable"] = None, Transformation: "Transformation" = None, NamedElement: "JTL_emof_Comment"):
        self.isTopLevel = isTopLevel
        self.Domain = Domain if Domain is not None else set()
        self.Where = Where
        self.When = When
        self.JTL_JTL_Relation = JTL_JTL_Relation if JTL_JTL_Relation is not None else set()
        self.Transformation = Transformation
        
    @property
    def isTopLevel(self) -> bool:
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: bool):
        self.__isTopLevel = isTopLevel

    @property
    def When(self):
        return self.__When

    @When.setter
    def When(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Relation__When", None)
        self.__When = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL45"):
                opp_val = getattr(old_value, "JTL45", None)
                if opp_val == self:
                    setattr(old_value, "JTL45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL45"):
                opp_val = getattr(value, "JTL45", None)
                setattr(value, "JTL45", self)

    @property
    def Domain(self):
        return self.__Domain

    @Domain.setter
    def Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Relation__Domain", None)
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
    def Where(self):
        return self.__Where

    @Where.setter
    def Where(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Relation__Where", None)
        self.__Where = value
        
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

    @property
    def JTL_JTL_Relation(self):
        return self.__JTL_JTL_Relation

    @JTL_JTL_Relation.setter
    def JTL_JTL_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Relation__JTL_JTL_Relation", None)
        self.__JTL_JTL_Relation = value if value is not None else set()
        
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
    def Transformation(self):
        return self.__Transformation

    @Transformation.setter
    def Transformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Relation__Transformation", None)
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

class JTL_emof_TypedElement(NamedElement):

    def __init__(self, type: str, NamedElement: "JTL_emof_Comment"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class JTL_emof_Package(NamedElement):

    def __init__(self, uri: str, Type18: set["Type"] = None, JTL_emof_Package: set["Package"] = None, NamedElement: "JTL_emof_Comment"):
        self.uri = uri
        self.Type18 = Type18 if Type18 is not None else set()
        self.JTL_emof_Package = JTL_emof_Package if JTL_emof_Package is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def JTL_emof_Package(self):
        return self.__JTL_emof_Package

    @JTL_emof_Package.setter
    def JTL_emof_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Package__JTL_emof_Package", None)
        self.__JTL_emof_Package = value if value is not None else set()
        
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
        old_value = getattr(self, f"_JTL_emof_Package__Type18", None)
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
                    

class JTL_emof_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: int, upper: str):
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

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

class Parameter:

    pass
class emof_TypedElement:

    pass
class emof_MultiplicityElement:

    pass
class JTL_emof_Parameter(emof_MultiplicityElement, emof_TypedElement):

    pass
class JTL_emof_Property(emof_MultiplicityElement, emof_TypedElement):

    def __init__(self, isReadOnly: bool, isDerived: bool, isComposite: bool, isId: bool, default: str, Class30: "Class" = None, JTL_emof_Property: "Property" = None):
        self.isReadOnly = isReadOnly
        self.isDerived = isDerived
        self.isComposite = isComposite
        self.isId = isId
        self.default = default
        self.Class30 = Class30
        self.JTL_emof_Property = JTL_emof_Property
        
    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def isId(self) -> bool:
        return self.__isId

    @isId.setter
    def isId(self, isId: bool):
        self.__isId = isId

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def Class30(self):
        return self.__Class30

    @Class30.setter
    def Class30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Property__Class30", None)
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

    @property
    def JTL_emof_Property(self):
        return self.__JTL_emof_Property

    @JTL_emof_Property.setter
    def JTL_emof_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Property__JTL_emof_Property", None)
        self.__JTL_emof_Property = value
        
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

class JTL_emof_Operation(emof_MultiplicityElement, emof_TypedElement):

    pass
class JTL_emof_Object:

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class JTL_emof_PrimitiveType(DataType):

    pass
class JTL_essentialocl_CollectionType(DataType):

    pass
class JTL_emof_Enumeration(DataType):

    pass
class Operation:

    pass
class Element:

    pass
class JTL_emof_Comment(Element):

    pass
class JTL_JTL_Pattern(Element):

    pass
class JTL_JTL_Predicate(Element):

    pass
class JTL_imperativeocl_DictLiteralPart(Element):

    pass
class JTL_emof_NamedElement(Element):

    def __init__(self, name: str, emof8: "JTL_emof_Tag", Element251: "JTL_imperativeocl_LogExp"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class JTL_template_PropertyTemplateItem(Element):

    pass
class JTL_imperativeocl_AnonymousTupleLiteralPart(Element):

    pass
class JTL_emof_Tag(Element):

    def __init__(self, value: str, name: str, Element: set["Element"] = None, emof8: "JTL_emof_Tag", Element251: "JTL_imperativeocl_LogExp"):
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
        old_value = getattr(self, f"_JTL_emof_Tag__Element", None)
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
class Object:

    pass
class JTL_emof_Extent(Object):

    pass
class JTL_emof_Element(Object):

    pass
class Class:

    pass
class JTL_imperativeocl_Typedef(Class):

    pass
class JTL_imperativeocl_AnonymousTupleType(Class):

    pass
class Property:

    pass
class Type:

    pass
class JTL_essentialocl_InvalidType(Type):

    pass
class JTL_emof_DataType(Type):

    pass
class JTL_imperativeocl_TemplateParameterType(Type):

    def __init__(self, specification: str, Type110: "JTL_essentialocl_TypeExp", Type240: "JTL_imperativeocl_DictionaryType", Type218: "JTL_imperativeocl_TryExp", Type150: "JTL_essentialocl_CollectionType", Type223: "JTL_imperativeocl_RaiseExp", emof19: "JTL_emof_Package", Type263: "JTL_imperativeocl_AnonymousTupleType", Type227: "JTL_imperativeocl_Typedef", Type: "JTL_emof_Operation"):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class JTL_essentialocl_VoidType(Type):

    pass
class JTL_emof_Class(Type):

    def __init__(self, isAbstract: bool, Property: set["Property"] = None, JTL_emof_Class: set["Class"] = None, Operation: set["Operation"] = None, Type110: "JTL_essentialocl_TypeExp", Type240: "JTL_imperativeocl_DictionaryType", Type218: "JTL_imperativeocl_TryExp", Type150: "JTL_essentialocl_CollectionType", Type223: "JTL_imperativeocl_RaiseExp", emof19: "JTL_emof_Package", Type263: "JTL_imperativeocl_AnonymousTupleType", Type227: "JTL_imperativeocl_Typedef", Type: "JTL_emof_Operation"):
        self.isAbstract = isAbstract
        self.Property = Property if Property is not None else set()
        self.JTL_emof_Class = JTL_emof_Class if JTL_emof_Class is not None else set()
        self.Operation = Operation if Operation is not None else set()
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def JTL_emof_Class(self):
        return self.__JTL_emof_Class

    @JTL_emof_Class.setter
    def JTL_emof_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Class__JTL_emof_Class", None)
        self.__JTL_emof_Class = value if value is not None else set()
        
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
        old_value = getattr(self, f"_JTL_emof_Class__Property", None)
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
                    

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Class__Operation", None)
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
                    

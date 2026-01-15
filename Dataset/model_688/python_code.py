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
class AltExp:

    pass
class imperativeocl_ImperativeExpression:

    pass
class Janus_imperativeocl_ImperativeLoopExp(essentialocl_LoopExp, imperativeocl_ImperativeExpression):

    pass
class ImperativeLoopExp:

    pass
class Janus_imperativeocl_ForExp(ImperativeLoopExp):

    pass
class Janus_imperativeocl_CollectorExp(ImperativeLoopExp):

    pass
class Janus_imperativeocl_ImperativeIterateExp(ImperativeLoopExp):

    pass
class ObjectTemplateExp:

    pass
class ImperativeExpression:

    pass
class Janus_imperativeocl_BreakExp(ImperativeExpression):

    pass
class Janus_imperativeocl_UnlinkExp(ImperativeExpression):

    pass
class Janus_imperativeocl_WhileExp(ImperativeExpression):

    pass
class Janus_imperativeocl_ComputeExp(ImperativeExpression):

    pass
class Janus_imperativeocl_UnpackExp(ImperativeExpression):

    pass
class Janus_imperativeocl_LogExp(ImperativeExpression):

    def __init__(self, text: str, level: int, Janus_imperativeocl_LogExp: "OclExpression" = None, Janus_imperativeocl_LogExp258: "Element" = None):
        self.text = text
        self.level = level
        self.Janus_imperativeocl_LogExp = Janus_imperativeocl_LogExp
        self.Janus_imperativeocl_LogExp258 = Janus_imperativeocl_LogExp258
        
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
    def Janus_imperativeocl_LogExp258(self):
        return self.__Janus_imperativeocl_LogExp258

    @Janus_imperativeocl_LogExp258.setter
    def Janus_imperativeocl_LogExp258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_LogExp__Janus_imperativeocl_LogExp258", None)
        self.__Janus_imperativeocl_LogExp258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element259"):
                opp_val = getattr(old_value, "Element259", None)
                if opp_val == self:
                    setattr(old_value, "Element259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element259"):
                opp_val = getattr(value, "Element259", None)
                setattr(value, "Element259", self)

    @property
    def Janus_imperativeocl_LogExp(self):
        return self.__Janus_imperativeocl_LogExp

    @Janus_imperativeocl_LogExp.setter
    def Janus_imperativeocl_LogExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_LogExp__Janus_imperativeocl_LogExp", None)
        self.__Janus_imperativeocl_LogExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression256"):
                opp_val = getattr(old_value, "OclExpression256", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression256"):
                opp_val = getattr(value, "OclExpression256", None)
                setattr(value, "OclExpression256", self)

class Janus_imperativeocl_AltExp(ImperativeExpression):

    pass
class Janus_imperativeocl_InstantiationExp(ImperativeExpression):

    pass
class Janus_imperativeocl_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: bool, Janus_imperativeocl_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.Janus_imperativeocl_VariableInitExp = Janus_imperativeocl_VariableInitExp
        
    @property
    def withResult(self) -> bool:
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: bool):
        self.__withResult = withResult

    @property
    def Janus_imperativeocl_VariableInitExp(self):
        return self.__Janus_imperativeocl_VariableInitExp

    @Janus_imperativeocl_VariableInitExp.setter
    def Janus_imperativeocl_VariableInitExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_VariableInitExp__Janus_imperativeocl_VariableInitExp", None)
        self.__Janus_imperativeocl_VariableInitExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable199"):
                opp_val = getattr(old_value, "Variable199", None)
                if opp_val == self:
                    setattr(old_value, "Variable199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable199"):
                opp_val = getattr(value, "Variable199", None)
                setattr(value, "Variable199", self)

class Janus_imperativeocl_ContinueExp(ImperativeExpression):

    pass
class Janus_imperativeocl_RaiseExp(ImperativeExpression):

    pass
class Janus_imperativeocl_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, Janus_imperativeocl_AssertExp: "LogExp" = None, Janus_imperativeocl_AssertExp262: "OclExpression" = None):
        self.severity = severity
        self.Janus_imperativeocl_AssertExp = Janus_imperativeocl_AssertExp
        self.Janus_imperativeocl_AssertExp262 = Janus_imperativeocl_AssertExp262
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def Janus_imperativeocl_AssertExp262(self):
        return self.__Janus_imperativeocl_AssertExp262

    @Janus_imperativeocl_AssertExp262.setter
    def Janus_imperativeocl_AssertExp262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_AssertExp__Janus_imperativeocl_AssertExp262", None)
        self.__Janus_imperativeocl_AssertExp262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression263"):
                opp_val = getattr(old_value, "OclExpression263", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression263"):
                opp_val = getattr(value, "OclExpression263", None)
                setattr(value, "OclExpression263", self)

    @property
    def Janus_imperativeocl_AssertExp(self):
        return self.__Janus_imperativeocl_AssertExp

    @Janus_imperativeocl_AssertExp.setter
    def Janus_imperativeocl_AssertExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_AssertExp__Janus_imperativeocl_AssertExp", None)
        self.__Janus_imperativeocl_AssertExp = value
        
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

class Janus_imperativeocl_TupleExp(ImperativeExpression):

    pass
class Janus_imperativeocl_BlockExp(ImperativeExpression):

    pass
class Janus_imperativeocl_TryExp(ImperativeExpression):

    pass
class Janus_imperativeocl_ReturnExp(ImperativeExpression):

    pass
class Janus_imperativeocl_AssignExp(ImperativeExpression):

    def __init__(self, isReset: bool, Janus_imperativeocl_AssignExp: set["OclExpression"] = None, Janus_imperativeocl_AssignExp187: "OclExpression" = None, Janus_imperativeocl_AssignExp190: "OclExpression" = None):
        self.isReset = isReset
        self.Janus_imperativeocl_AssignExp = Janus_imperativeocl_AssignExp if Janus_imperativeocl_AssignExp is not None else set()
        self.Janus_imperativeocl_AssignExp187 = Janus_imperativeocl_AssignExp187
        self.Janus_imperativeocl_AssignExp190 = Janus_imperativeocl_AssignExp190
        
    @property
    def isReset(self) -> bool:
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: bool):
        self.__isReset = isReset

    @property
    def Janus_imperativeocl_AssignExp(self):
        return self.__Janus_imperativeocl_AssignExp

    @Janus_imperativeocl_AssignExp.setter
    def Janus_imperativeocl_AssignExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_AssignExp__Janus_imperativeocl_AssignExp", None)
        self.__Janus_imperativeocl_AssignExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression185"):
                    opp_val = getattr(item, "OclExpression185", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression185"):
                    opp_val = getattr(item, "OclExpression185", None)
                    
                    setattr(item, "OclExpression185", self)
                    

    @property
    def Janus_imperativeocl_AssignExp190(self):
        return self.__Janus_imperativeocl_AssignExp190

    @Janus_imperativeocl_AssignExp190.setter
    def Janus_imperativeocl_AssignExp190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_AssignExp__Janus_imperativeocl_AssignExp190", None)
        self.__Janus_imperativeocl_AssignExp190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression191"):
                opp_val = getattr(old_value, "OclExpression191", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression191"):
                opp_val = getattr(value, "OclExpression191", None)
                setattr(value, "OclExpression191", self)

    @property
    def Janus_imperativeocl_AssignExp187(self):
        return self.__Janus_imperativeocl_AssignExp187

    @Janus_imperativeocl_AssignExp187.setter
    def Janus_imperativeocl_AssignExp187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_AssignExp__Janus_imperativeocl_AssignExp187", None)
        self.__Janus_imperativeocl_AssignExp187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression188"):
                opp_val = getattr(old_value, "OclExpression188", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression188"):
                opp_val = getattr(value, "OclExpression188", None)
                setattr(value, "OclExpression188", self)

class PropertyTemplateItem:

    pass
class CollectionType:

    pass
class Janus_essentialocl_SequenceType(CollectionType):

    pass
class Janus_essentialocl_OrderedSetType(CollectionType):

    pass
class Janus_imperativeocl_ListType(CollectionType):

    pass
class Janus_imperativeocl_DictionaryType(CollectionType):

    pass
class emof_Type:

    pass
class emof_DataType:

    pass
class Janus_essentialocl_SetType(CollectionType):

    pass
class CallExp:

    pass
class Janus_essentialocl_FeaturePropertyCall(CallExp):

    pass
class Janus_essentialocl_OpaqueExpression:

    pass
class Janus_essentialocl_BagType(CollectionType):

    pass
class TupleLiteralExp:

    pass
class TupleLiteralPart:

    pass
class OpaqueExpression:

    pass
class Janus_essentialocl_ExpressionInOcl(OpaqueExpression):

    pass
class CollectionLiteralPart:

    pass
class Janus_essentialocl_CollectionItem(CollectionLiteralPart):

    pass
class Janus_essentialocl_CollectionRange(CollectionLiteralPart):

    pass
class LiteralExp:

    pass
class Janus_template_TemplateExp(LiteralExp):

    pass
class Janus_essentialocl_NullLiteralExp(LiteralExp):

    pass
class Janus_imperativeocl_DictLiteralExp(LiteralExp):

    pass
class Janus_imperativeocl_AnonymousTupleLiteralExp(LiteralExp):

    pass
class Janus_essentialocl_EnumLiteralExp(LiteralExp):

    pass
class Janus_essentialocl_CollectionLiteralExp(LiteralExp):

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
        old_value = getattr(self, f"_Janus_essentialocl_CollectionLiteralExp__CollectionLiteralPart", None)
        self.__CollectionLiteralPart = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialocl131"):
                    opp_val = getattr(item, "essentialocl131", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialocl131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialocl131"):
                    opp_val = getattr(item, "essentialocl131", None)
                    
                    setattr(item, "essentialocl131", self)
                    

class Janus_essentialocl_InvalidLiteralExp(LiteralExp):

    pass
class Janus_essentialocl_TupleLiteralExp(LiteralExp):

    pass
class Janus_essentialocl_PrimitiveLiteralExp(LiteralExp):

    pass
class CollectionLiteralExp:

    pass
class LoopExp:

    pass
class Janus_essentialocl_IterateExp(LoopExp):

    pass
class Janus_essentialocl_IteratorExp(LoopExp):

    pass
class essentialocl_OclExpression:

    pass
class essentialocl_CallExp:

    pass
class Janus_imperativeocl_SwitchExp(essentialocl_CallExp, imperativeocl_ImperativeExpression):

    pass
class Janus_essentialocl_LoopExp(essentialocl_OclExpression, essentialocl_CallExp):

    pass
class ComputeExp:

    pass
class LetExp:

    pass
class FeaturePropertyCall:

    pass
class Janus_essentialocl_OperationCallExp(FeaturePropertyCall):

    pass
class Janus_essentialocl_PropertyCallExp(FeaturePropertyCall):

    pass
class NumericLiteralExp:

    pass
class Janus_essentialocl_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: float):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> float:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: float):
        self.__realSymbol = realSymbol

class Janus_essentialocl_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: int):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> int:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: int):
        self.__integerSymbol = integerSymbol

class Janus_essentialocl_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class TypedElement:

    pass
class Janus_essentialocl_CollectionLiteralPart(TypedElement):

    pass
class Janus_essentialocl_TupleLiteralPart(TypedElement):

    pass
class Janus_essentialocl_Variable(TypedElement):

    pass
class Janus_essentialocl_OclExpression(TypedElement):

    pass
class TryExp:

    pass
class PrimitiveLiteralExp:

    pass
class Janus_essentialocl_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class Janus_essentialocl_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class Janus_essentialocl_BooleanLiteralExp(PrimitiveLiteralExp):

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
class Janus_essentialocl_LiteralExp(OclExpression):

    pass
class Janus_essentialocl_IfExp(OclExpression):

    pass
class Janus_essentialocl_LetExp(OclExpression):

    pass
class Janus_essentialocl_VariableExp(OclExpression):

    pass
class Janus_imperativeocl_ImperativeExpression(OclExpression):

    pass
class Janus_essentialocl_TypeExp(OclExpression):

    pass
class Janus_essentialocl_CallExp(OclExpression):

    pass
class TemplateExp:

    pass
class Janus_template_ObjectTemplateExp(TemplateExp):

    def __init__(self, referredClass: str, PropertyTemplateItem: set["PropertyTemplateItem"] = None, TemplateExp: "Janus_JTL_Pattern"):
        self.referredClass = referredClass
        self.PropertyTemplateItem = PropertyTemplateItem if PropertyTemplateItem is not None else set()
        
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
        old_value = getattr(self, f"_Janus_template_ObjectTemplateExp__PropertyTemplateItem", None)
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
                    

class Janus_template_CollectionTemplateExp(TemplateExp):

    def __init__(self, kind: str, Janus_template_CollectionTemplateExp: set["OclExpression"] = None, Janus_template_CollectionTemplateExp171: "CollectionType" = None, Janus_template_CollectionTemplateExp173: "OclExpression" = None, TemplateExp: "Janus_JTL_Pattern"):
        self.kind = kind
        self.Janus_template_CollectionTemplateExp = Janus_template_CollectionTemplateExp if Janus_template_CollectionTemplateExp is not None else set()
        self.Janus_template_CollectionTemplateExp171 = Janus_template_CollectionTemplateExp171
        self.Janus_template_CollectionTemplateExp173 = Janus_template_CollectionTemplateExp173
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Janus_template_CollectionTemplateExp(self):
        return self.__Janus_template_CollectionTemplateExp

    @Janus_template_CollectionTemplateExp.setter
    def Janus_template_CollectionTemplateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_template_CollectionTemplateExp__Janus_template_CollectionTemplateExp", None)
        self.__Janus_template_CollectionTemplateExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression169"):
                    opp_val = getattr(item, "OclExpression169", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression169"):
                    opp_val = getattr(item, "OclExpression169", None)
                    
                    setattr(item, "OclExpression169", self)
                    

    @property
    def Janus_template_CollectionTemplateExp171(self):
        return self.__Janus_template_CollectionTemplateExp171

    @Janus_template_CollectionTemplateExp171.setter
    def Janus_template_CollectionTemplateExp171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_template_CollectionTemplateExp__Janus_template_CollectionTemplateExp171", None)
        self.__Janus_template_CollectionTemplateExp171 = value
        
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
    def Janus_template_CollectionTemplateExp173(self):
        return self.__Janus_template_CollectionTemplateExp173

    @Janus_template_CollectionTemplateExp173.setter
    def Janus_template_CollectionTemplateExp173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_template_CollectionTemplateExp__Janus_template_CollectionTemplateExp173", None)
        self.__Janus_template_CollectionTemplateExp173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression174"):
                opp_val = getattr(old_value, "OclExpression174", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression174"):
                opp_val = getattr(value, "OclExpression174", None)
                setattr(value, "OclExpression174", self)

class Predicate:

    pass
class Variable:

    pass
class Domain:

    pass
class Transformation:

    pass
class Relation:

    pass
class Pattern:

    pass
class Model:

    pass
class emof_Package:

    pass
class emof_Class:

    pass
class Janus_essentialocl_AnyType(emof_Type, emof_Class):

    pass
class Janus_essentialocl_TupleType(emof_DataType, emof_Class):

    pass
class Janus_JTL_Transformation(emof_Package, emof_Class):

    pass
class Extent:

    pass
class Janus_emof_URIExtent(Extent):

    pass
class Package:

    pass
class NamedElement:

    pass
class Janus_emof_TypedElement(NamedElement):

    pass
class Janus_JTL_Model(NamedElement):

    pass
class Janus_JTL_Relation(NamedElement):

    def __init__(self, isTopLevel: bool, Pattern: "Pattern" = None, Transformation: "Transformation" = None, Domain: set["Domain"] = None, Pattern47: "Pattern" = None, Janus_JTL_Relation: set["Variable"] = None, NamedElement: "Janus_emof_Comment"):
        self.isTopLevel = isTopLevel
        self.Pattern = Pattern
        self.Transformation = Transformation
        self.Domain = Domain if Domain is not None else set()
        self.Pattern47 = Pattern47
        self.Janus_JTL_Relation = Janus_JTL_Relation if Janus_JTL_Relation is not None else set()
        
    @property
    def isTopLevel(self) -> bool:
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: bool):
        self.__isTopLevel = isTopLevel

    @property
    def Domain(self):
        return self.__Domain

    @Domain.setter
    def Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Relation__Domain", None)
        self.__Domain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JTL43"):
                    opp_val = getattr(item, "JTL43", None)
                    
                    if opp_val == self:
                        setattr(item, "JTL43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JTL43"):
                    opp_val = getattr(item, "JTL43", None)
                    
                    setattr(item, "JTL43", self)
                    

    @property
    def Pattern47(self):
        return self.__Pattern47

    @Pattern47.setter
    def Pattern47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Relation__Pattern47", None)
        self.__Pattern47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL48"):
                opp_val = getattr(old_value, "JTL48", None)
                if opp_val == self:
                    setattr(old_value, "JTL48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL48"):
                opp_val = getattr(value, "JTL48", None)
                setattr(value, "JTL48", self)

    @property
    def Transformation(self):
        return self.__Transformation

    @Transformation.setter
    def Transformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Relation__Transformation", None)
        self.__Transformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL41"):
                opp_val = getattr(old_value, "JTL41", None)
                if opp_val == self:
                    setattr(old_value, "JTL41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL41"):
                opp_val = getattr(value, "JTL41", None)
                setattr(value, "JTL41", self)

    @property
    def Janus_JTL_Relation(self):
        return self.__Janus_JTL_Relation

    @Janus_JTL_Relation.setter
    def Janus_JTL_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Relation__Janus_JTL_Relation", None)
        self.__Janus_JTL_Relation = value if value is not None else set()
        
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
    def Pattern(self):
        return self.__Pattern

    @Pattern.setter
    def Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Relation__Pattern", None)
        self.__Pattern = value
        
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

class Janus_JTL_Domain(NamedElement):

    def __init__(self, isEnforceable: bool, isCheckable: bool, Relation51: "Relation" = None, Janus_JTL_Domain: "Pattern" = None, Janus_JTL_Domain56: "Model" = None, Janus_JTL_Domain59: "Variable" = None, NamedElement: "Janus_emof_Comment"):
        self.isEnforceable = isEnforceable
        self.isCheckable = isCheckable
        self.Relation51 = Relation51
        self.Janus_JTL_Domain = Janus_JTL_Domain
        self.Janus_JTL_Domain56 = Janus_JTL_Domain56
        self.Janus_JTL_Domain59 = Janus_JTL_Domain59
        
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
    def Relation51(self):
        return self.__Relation51

    @Relation51.setter
    def Relation51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Domain__Relation51", None)
        self.__Relation51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JTL52"):
                opp_val = getattr(old_value, "JTL52", None)
                if opp_val == self:
                    setattr(old_value, "JTL52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JTL52"):
                opp_val = getattr(value, "JTL52", None)
                setattr(value, "JTL52", self)

    @property
    def Janus_JTL_Domain(self):
        return self.__Janus_JTL_Domain

    @Janus_JTL_Domain.setter
    def Janus_JTL_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Domain__Janus_JTL_Domain", None)
        self.__Janus_JTL_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern54"):
                opp_val = getattr(old_value, "Pattern54", None)
                if opp_val == self:
                    setattr(old_value, "Pattern54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern54"):
                opp_val = getattr(value, "Pattern54", None)
                setattr(value, "Pattern54", self)

    @property
    def Janus_JTL_Domain56(self):
        return self.__Janus_JTL_Domain56

    @Janus_JTL_Domain56.setter
    def Janus_JTL_Domain56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Domain__Janus_JTL_Domain56", None)
        self.__Janus_JTL_Domain56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model57"):
                opp_val = getattr(old_value, "Model57", None)
                if opp_val == self:
                    setattr(old_value, "Model57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model57"):
                opp_val = getattr(value, "Model57", None)
                setattr(value, "Model57", self)

    @property
    def Janus_JTL_Domain59(self):
        return self.__Janus_JTL_Domain59

    @Janus_JTL_Domain59.setter
    def Janus_JTL_Domain59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Domain__Janus_JTL_Domain59", None)
        self.__Janus_JTL_Domain59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable60"):
                opp_val = getattr(old_value, "Variable60", None)
                if opp_val == self:
                    setattr(old_value, "Variable60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable60"):
                opp_val = getattr(value, "Variable60", None)
                setattr(value, "Variable60", self)

class Janus_emof_Type(NamedElement):

    pass
class Janus_emof_Package(NamedElement):

    def __init__(self, uri: str, Type18: set["Type"] = None, Janus_emof_Package: set["Package"] = None, NamedElement: "Janus_emof_Comment"):
        self.uri = uri
        self.Type18 = Type18 if Type18 is not None else set()
        self.Janus_emof_Package = Janus_emof_Package if Janus_emof_Package is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def Type18(self):
        return self.__Type18

    @Type18.setter
    def Type18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Package__Type18", None)
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
                    

    @property
    def Janus_emof_Package(self):
        return self.__Janus_emof_Package

    @Janus_emof_Package.setter
    def Janus_emof_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Package__Janus_emof_Package", None)
        self.__Janus_emof_Package = value if value is not None else set()
        
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
                    

class Enumeration:

    pass
class Janus_emof_EnumerationLiteral(NamedElement):

    pass
class Parameter:

    pass
class emof_TypedElement:

    pass
class emof_MultiplicityElement:

    pass
class Janus_emof_Property(emof_TypedElement, emof_MultiplicityElement):

    def __init__(self, isReadOnly: bool, isDerived: bool, isComposite: bool, isId: bool, default: str, Class30: "Class" = None, Janus_emof_Property: "Property" = None):
        self.isReadOnly = isReadOnly
        self.isDerived = isDerived
        self.isComposite = isComposite
        self.isId = isId
        self.default = default
        self.Class30 = Class30
        self.Janus_emof_Property = Janus_emof_Property
        
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
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

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
        old_value = getattr(self, f"_Janus_emof_Property__Class30", None)
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
    def Janus_emof_Property(self):
        return self.__Janus_emof_Property

    @Janus_emof_Property.setter
    def Janus_emof_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Property__Janus_emof_Property", None)
        self.__Janus_emof_Property = value
        
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

class Janus_emof_Parameter(emof_TypedElement, emof_MultiplicityElement):

    pass
class Janus_emof_Operation(emof_TypedElement, emof_MultiplicityElement):

    pass
class Janus_emof_Object:

    pass
class EnumerationLiteral:

    pass
class Janus_emof_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: int, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

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

class Element:

    pass
class Janus_imperativeocl_AnonymousTupleLiteralPart(Element):

    pass
class Janus_template_PropertyTemplateItem(Element):

    pass
class Janus_JTL_Pattern(Element):

    pass
class Janus_emof_NamedElement(Element):

    def __init__(self, name: str, Element259: "Janus_imperativeocl_LogExp", emof8: "Janus_emof_Tag"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Janus_JTL_Predicate(Element):

    pass
class Janus_imperativeocl_DictLiteralPart(Element):

    pass
class Janus_emof_Comment(Element):

    pass
class Janus_emof_Tag(Element):

    def __init__(self, name: str, value: str, Element: set["Element"] = None, Element259: "Janus_imperativeocl_LogExp", emof8: "Janus_emof_Tag"):
        self.name = name
        self.value = value
        self.Element = Element if Element is not None else set()
        
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
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Tag__Element", None)
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
class Janus_emof_Extent(Object):

    pass
class Janus_emof_Element(Object):

    pass
class Class:

    pass
class Janus_imperativeocl_Typedef(Class):

    pass
class Janus_imperativeocl_AnonymousTupleType(Class):

    pass
class DataType:

    pass
class Janus_essentialocl_CollectionType(DataType):

    pass
class Janus_emof_PrimitiveType(DataType):

    pass
class Janus_emof_Enumeration(DataType):

    pass
class Property:

    pass
class Type:

    pass
class Janus_essentialocl_VoidType(Type):

    pass
class Janus_imperativeocl_TemplateParameterType(Type):

    def __init__(self, specification: str, Type235: "Janus_imperativeocl_Typedef", emof19: "Janus_emof_Package", Type231: "Janus_imperativeocl_RaiseExp", Type: "Janus_emof_Operation", Type159: "Janus_essentialocl_CollectionType", Type117: "Janus_essentialocl_TypeExp", Type271: "Janus_imperativeocl_AnonymousTupleType", Type35: "Janus_emof_TypedElement", Type248: "Janus_imperativeocl_DictionaryType", Type226: "Janus_imperativeocl_TryExp"):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class Janus_emof_DataType(Type):

    pass
class Janus_essentialocl_InvalidType(Type):

    pass
class Janus_emof_Class(Type):

    def __init__(self, isAbstract: bool, Operation: set["Operation"] = None, Property: set["Property"] = None, Janus_emof_Class: set["Class"] = None, Type235: "Janus_imperativeocl_Typedef", emof19: "Janus_emof_Package", Type231: "Janus_imperativeocl_RaiseExp", Type: "Janus_emof_Operation", Type159: "Janus_essentialocl_CollectionType", Type117: "Janus_essentialocl_TypeExp", Type271: "Janus_imperativeocl_AnonymousTupleType", Type35: "Janus_emof_TypedElement", Type248: "Janus_imperativeocl_DictionaryType", Type226: "Janus_imperativeocl_TryExp"):
        self.isAbstract = isAbstract
        self.Operation = Operation if Operation is not None else set()
        self.Property = Property if Property is not None else set()
        self.Janus_emof_Class = Janus_emof_Class if Janus_emof_Class is not None else set()
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Class__Property", None)
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
    def Janus_emof_Class(self):
        return self.__Janus_emof_Class

    @Janus_emof_Class.setter
    def Janus_emof_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Class__Janus_emof_Class", None)
        self.__Janus_emof_Class = value if value is not None else set()
        
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
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Class__Operation", None)
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
                    

class Operation:

    pass
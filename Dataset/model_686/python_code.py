from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SeverityKind(Enum):
    fatal = "fatal"
    warning = "warning"
    error = "error"
class CollectionKind(Enum):
    OrderedSet = "OrderedSet"
    Set = "Set"
    Bag = "Bag"
    Sequence = "Sequence"


############################################
# Definition of Classes
############################################

class emof_MultiplicityElement:

    pass
class JTLMM_emof_Object:

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class JTLMM_emof_Enumeration(DataType):

    pass
class Enumeration:

    pass
class Element:

    pass
class JTLMM_emof_NamedElement(Element):

    def __init__(self, name: str, Element230: "JTLMM_imperativeocl_LogExp" = None, Element: "JTLMM_emof_Tag" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class JTLMM_emof_Tag(Element):

    def __init__(self, value: str, name: str, tag: set["Element"] = None, Element230: "JTLMM_imperativeocl_LogExp" = None, Element: "JTLMM_emof_Tag" = None):
        self.value = value
        self.name = name
        self.tag = tag if tag is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Tag__tag", None)
        self.__tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

class Comment:

    pass
class Tag:

    pass
class Object:

    pass
class JTLMM_emof_Extent(Object):

    pass
class JTLMM_emof_Element(Object):

    pass
class LogExp:

    pass
class JTLMM_imperativeocl_AnonymousTupleLiteralPart(Element):

    pass
class AnonymousTupleLiteralPart:

    pass
class essentialocl_LoopExp:

    pass
class JTLMM_imperativeocl_DictLiteralPart(Element):

    pass
class DictLiteralPart:

    pass
class ImperativeLoopExp:

    pass
class JTLMM_imperativeocl_CollectorExp(ImperativeLoopExp):

    pass
class JTLMM_imperativeocl_ForExp(ImperativeLoopExp):

    pass
class JTLMM_imperativeocl_ImperativeIterateExp(ImperativeLoopExp):

    pass
class ObjectTemplateExp:

    pass
class JTLMM_template_PropertyTemplateItem(Element):

    pass
class AltExp:

    pass
class imperativeocl_ImperativeExpression:

    pass
class JTLMM_imperativeocl_ImperativeLoopExp(essentialocl_LoopExp, imperativeocl_ImperativeExpression):

    pass
class ImperativeExpression:

    pass
class JTLMM_imperativeocl_InstantiationExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_WhileExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_UnpackExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_AltExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_RaiseExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, JTLMM_imperativeocl_AssertExp: "LogExp" = None, JTLMM_imperativeocl_AssertExp233: "OclExpression" = None):
        self.severity = severity
        self.JTLMM_imperativeocl_AssertExp = JTLMM_imperativeocl_AssertExp
        self.JTLMM_imperativeocl_AssertExp233 = JTLMM_imperativeocl_AssertExp233
        
        pass
    @property
    def severity(self):
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity


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

    @property
    def JTLMM_imperativeocl_AssertExp233(self):
        return self.__JTLMM_imperativeocl_AssertExp233

    @JTLMM_imperativeocl_AssertExp233.setter
    def JTLMM_imperativeocl_AssertExp233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_AssertExp__JTLMM_imperativeocl_AssertExp233", None)
        self.__JTLMM_imperativeocl_AssertExp233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression234"):
                opp_val = getattr(old_value, "OclExpression234", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression234"):
                opp_val = getattr(value, "OclExpression234", None)
                setattr(value, "OclExpression234", self)

class JTLMM_imperativeocl_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: bool, JTLMM_imperativeocl_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.JTLMM_imperativeocl_VariableInitExp = JTLMM_imperativeocl_VariableInitExp
        
        pass
    @property
    def withResult(self):
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
            if hasattr(old_value, "Variable172"):
                opp_val = getattr(old_value, "Variable172", None)
                if opp_val == self:
                    setattr(old_value, "Variable172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable172"):
                opp_val = getattr(value, "Variable172", None)
                setattr(value, "Variable172", self)

class JTLMM_imperativeocl_BlockExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_LogExp(ImperativeExpression):

    def __init__(self, text: str, level: int, JTLMM_imperativeocl_LogExp: "OclExpression" = None, JTLMM_imperativeocl_LogExp229: "Element" = None):
        self.text = text
        self.level = level
        self.JTLMM_imperativeocl_LogExp = JTLMM_imperativeocl_LogExp
        self.JTLMM_imperativeocl_LogExp229 = JTLMM_imperativeocl_LogExp229
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def level(self):
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
            if hasattr(old_value, "OclExpression227"):
                opp_val = getattr(old_value, "OclExpression227", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression227"):
                opp_val = getattr(value, "OclExpression227", None)
                setattr(value, "OclExpression227", self)

    @property
    def JTLMM_imperativeocl_LogExp229(self):
        return self.__JTLMM_imperativeocl_LogExp229

    @JTLMM_imperativeocl_LogExp229.setter
    def JTLMM_imperativeocl_LogExp229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_LogExp__JTLMM_imperativeocl_LogExp229", None)
        self.__JTLMM_imperativeocl_LogExp229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element230"):
                opp_val = getattr(old_value, "Element230", None)
                if opp_val == self:
                    setattr(old_value, "Element230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element230"):
                opp_val = getattr(value, "Element230", None)
                setattr(value, "Element230", self)

class JTLMM_imperativeocl_ComputeExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_TupleExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_BreakExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_ContinueExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_ReturnExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_UnlinkExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_TryExp(ImperativeExpression):

    pass
class JTLMM_imperativeocl_AssignExp(ImperativeExpression):

    def __init__(self, isReset: bool, JTLMM_imperativeocl_AssignExp: set["OclExpression"] = None, JTLMM_imperativeocl_AssignExp160: "OclExpression" = None, JTLMM_imperativeocl_AssignExp163: "OclExpression" = None):
        self.isReset = isReset
        self.JTLMM_imperativeocl_AssignExp = JTLMM_imperativeocl_AssignExp if JTLMM_imperativeocl_AssignExp is not None else set()
        self.JTLMM_imperativeocl_AssignExp160 = JTLMM_imperativeocl_AssignExp160
        self.JTLMM_imperativeocl_AssignExp163 = JTLMM_imperativeocl_AssignExp163
        
        pass
    @property
    def isReset(self):
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: bool):
        self.__isReset = isReset


    @property
    def JTLMM_imperativeocl_AssignExp163(self):
        return self.__JTLMM_imperativeocl_AssignExp163

    @JTLMM_imperativeocl_AssignExp163.setter
    def JTLMM_imperativeocl_AssignExp163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_AssignExp__JTLMM_imperativeocl_AssignExp163", None)
        self.__JTLMM_imperativeocl_AssignExp163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression164"):
                opp_val = getattr(old_value, "OclExpression164", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression164"):
                opp_val = getattr(value, "OclExpression164", None)
                setattr(value, "OclExpression164", self)

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
                if hasattr(item, "OclExpression158"):
                    opp_val = getattr(item, "OclExpression158", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression158"):
                    opp_val = getattr(item, "OclExpression158", None)
                    
                    setattr(item, "OclExpression158", self)
                    

    @property
    def JTLMM_imperativeocl_AssignExp160(self):
        return self.__JTLMM_imperativeocl_AssignExp160

    @JTLMM_imperativeocl_AssignExp160.setter
    def JTLMM_imperativeocl_AssignExp160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_imperativeocl_AssignExp__JTLMM_imperativeocl_AssignExp160", None)
        self.__JTLMM_imperativeocl_AssignExp160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression161"):
                opp_val = getattr(old_value, "OclExpression161", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression161"):
                opp_val = getattr(value, "OclExpression161", None)
                setattr(value, "OclExpression161", self)

class JTLMM_essentialocl_CollectionType(DataType):

    pass
class CollectionType:

    pass
class JTLMM_imperativeocl_DictionaryType(CollectionType):

    pass
class JTLMM_imperativeocl_ListType(CollectionType):

    pass
class JTLMM_essentialocl_BagType(CollectionType):

    pass
class TupleLiteralExp:

    pass
class CallExp:

    pass
class JTLMM_essentialocl_FeaturePropertyCall(CallExp):

    pass
class JTLMM_essentialocl_OpaqueExpression:

    pass
class AssignExp:

    pass
class PropertyTemplateItem:

    pass
class emof_Type:

    pass
class emof_DataType:

    pass
class JTLMM_essentialocl_SetType(CollectionType):

    pass
class JTLMM_essentialocl_SequenceType(CollectionType):

    pass
class JTLMM_essentialocl_OrderedSetType(CollectionType):

    pass
class OpaqueExpression:

    pass
class JTLMM_essentialocl_ExpressionInOcl(OpaqueExpression):

    pass
class TupleLiteralPart:

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
class JTLMM_essentialocl_NullLiteralExp(LiteralExp):

    pass
class JTLMM_essentialocl_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, CollectionLiteralExp: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.CollectionLiteralExp = CollectionLiteralExp if CollectionLiteralExp is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def CollectionLiteralExp(self):
        return self.__CollectionLiteralExp

    @CollectionLiteralExp.setter
    def CollectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_essentialocl_CollectionLiteralExp__CollectionLiteralExp", None)
        self.__CollectionLiteralExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CollectionLiteralPart"):
                    opp_val = getattr(item, "CollectionLiteralPart", None)
                    
                    if opp_val == self:
                        setattr(item, "CollectionLiteralPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CollectionLiteralPart"):
                    opp_val = getattr(item, "CollectionLiteralPart", None)
                    
                    setattr(item, "CollectionLiteralPart", self)
                    

class JTLMM_essentialocl_EnumLiteralExp(LiteralExp):

    pass
class JTLMM_imperativeocl_AnonymousTupleLiteralExp(LiteralExp):

    pass
class JTLMM_template_TemplateExp(LiteralExp):

    pass
class JTLMM_imperativeocl_DictLiteralExp(LiteralExp):

    pass
class JTLMM_essentialocl_InvalidLiteralExp(LiteralExp):

    pass
class JTLMM_essentialocl_TupleLiteralExp(LiteralExp):

    pass
class JTLMM_essentialocl_PrimitiveLiteralExp(LiteralExp):

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
class JTLMM_imperativeocl_SwitchExp(essentialocl_CallExp, imperativeocl_ImperativeExpression):

    pass
class JTLMM_essentialocl_LoopExp(essentialocl_CallExp, essentialocl_OclExpression):

    pass
class FeaturePropertyCall:

    pass
class JTLMM_essentialocl_OperationCallExp(FeaturePropertyCall):

    pass
class JTLMM_essentialocl_PropertyCallExp(FeaturePropertyCall):

    pass
class PrimitiveLiteralExp:

    pass
class JTLMM_essentialocl_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class JTLMM_essentialocl_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class JTLMM_essentialocl_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: bool):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: bool):
        self.__booleanSymbol = booleanSymbol


class OclExpression:

    pass
class JTLMM_essentialocl_LiteralExp(OclExpression):

    pass
class JTLMM_essentialocl_TypeExp(OclExpression):

    pass
class JTLMM_essentialocl_VariableExp(OclExpression):

    pass
class JTLMM_essentialocl_LetExp(OclExpression):

    pass
class JTLMM_imperativeocl_ImperativeExpression(OclExpression):

    pass
class JTLMM_essentialocl_CallExp(OclExpression):

    pass
class JTLMM_JTL_Predicate(Element):

    pass
class TemplateExp:

    pass
class JTLMM_template_ObjectTemplateExp(TemplateExp):

    def __init__(self, referredClass: str, objContainer: set["PropertyTemplateItem"] = None, JTLMM_template_ObjectTemplateExp: set["AssignExp"] = None, TemplateExp: "JTLMM_JTL_Pattern" = None):
        self.referredClass = referredClass
        self.objContainer = objContainer if objContainer is not None else set()
        self.JTLMM_template_ObjectTemplateExp = JTLMM_template_ObjectTemplateExp if JTLMM_template_ObjectTemplateExp is not None else set()
        
        pass
    @property
    def referredClass(self):
        return self.__referredClass

    @referredClass.setter
    def referredClass(self, referredClass: str):
        self.__referredClass = referredClass


    @property
    def objContainer(self):
        return self.__objContainer

    @objContainer.setter
    def objContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_template_ObjectTemplateExp__objContainer", None)
        self.__objContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PropertyTemplateItem"):
                    opp_val = getattr(item, "PropertyTemplateItem", None)
                    
                    if opp_val == self:
                        setattr(item, "PropertyTemplateItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PropertyTemplateItem"):
                    opp_val = getattr(item, "PropertyTemplateItem", None)
                    
                    setattr(item, "PropertyTemplateItem", self)
                    

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
                    

class JTLMM_template_CollectionTemplateExp(TemplateExp):

    def __init__(self, kind: str, JTLMM_template_CollectionTemplateExp: set["OclExpression"] = None, JTLMM_template_CollectionTemplateExp144: "CollectionType" = None, JTLMM_template_CollectionTemplateExp146: "OclExpression" = None, TemplateExp: "JTLMM_JTL_Pattern" = None):
        self.kind = kind
        self.JTLMM_template_CollectionTemplateExp = JTLMM_template_CollectionTemplateExp if JTLMM_template_CollectionTemplateExp is not None else set()
        self.JTLMM_template_CollectionTemplateExp144 = JTLMM_template_CollectionTemplateExp144
        self.JTLMM_template_CollectionTemplateExp146 = JTLMM_template_CollectionTemplateExp146
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


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
                if hasattr(item, "OclExpression142"):
                    opp_val = getattr(item, "OclExpression142", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression142"):
                    opp_val = getattr(item, "OclExpression142", None)
                    
                    setattr(item, "OclExpression142", self)
                    

    @property
    def JTLMM_template_CollectionTemplateExp144(self):
        return self.__JTLMM_template_CollectionTemplateExp144

    @JTLMM_template_CollectionTemplateExp144.setter
    def JTLMM_template_CollectionTemplateExp144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_template_CollectionTemplateExp__JTLMM_template_CollectionTemplateExp144", None)
        self.__JTLMM_template_CollectionTemplateExp144 = value
        
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
    def JTLMM_template_CollectionTemplateExp146(self):
        return self.__JTLMM_template_CollectionTemplateExp146

    @JTLMM_template_CollectionTemplateExp146.setter
    def JTLMM_template_CollectionTemplateExp146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_template_CollectionTemplateExp__JTLMM_template_CollectionTemplateExp146", None)
        self.__JTLMM_template_CollectionTemplateExp146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression147"):
                opp_val = getattr(old_value, "OclExpression147", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression147"):
                opp_val = getattr(value, "OclExpression147", None)
                setattr(value, "OclExpression147", self)

class Predicate:

    pass
class JTLMM_essentialocl_IfExp(OclExpression):

    pass
class NumericLiteralExp:

    pass
class JTLMM_essentialocl_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: int):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: int):
        self.__integerSymbol = integerSymbol


class JTLMM_essentialocl_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: float):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: float):
        self.__realSymbol = realSymbol


class JTLMM_essentialocl_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


class TryExp:

    pass
class TypedElement:

    pass
class JTLMM_essentialocl_TupleLiteralPart(TypedElement):

    pass
class JTLMM_essentialocl_Variable(TypedElement):

    pass
class JTLMM_essentialocl_CollectionLiteralPart(TypedElement):

    pass
class JTLMM_essentialocl_OclExpression(TypedElement):

    pass
class Pattern:

    pass
class Domain:

    pass
class Transformation:

    pass
class Relation:

    pass
class Model:

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
class JTLMM_emof_Comment(Element):

    pass
class Extent:

    pass
class JTLMM_emof_URIExtent(Extent):

    pass
class JTLMM_emof_PrimitiveType(DataType):

    pass
class JTLMM_JTL_Pattern(Element):

    pass
class Variable:

    pass
class Package:

    pass
class NamedElement:

    pass
class JTLMM_JTL_Model(NamedElement):

    def __init__(self, usedPackage: str, modelParameter: "Transformation" = None, JTLMM_JTL_Model: set["Model"] = None, NamedElement: "JTLMM_emof_Comment" = None):
        self.usedPackage = usedPackage
        self.modelParameter = modelParameter
        self.JTLMM_JTL_Model = JTLMM_JTL_Model if JTLMM_JTL_Model is not None else set()
        
        pass
    @property
    def usedPackage(self):
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
                if hasattr(item, "Model48"):
                    opp_val = getattr(item, "Model48", None)
                    
                    if opp_val == self:
                        setattr(item, "Model48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model48"):
                    opp_val = getattr(item, "Model48", None)
                    
                    setattr(item, "Model48", self)
                    

    @property
    def modelParameter(self):
        return self.__modelParameter

    @modelParameter.setter
    def modelParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Model__modelParameter", None)
        self.__modelParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transformation46"):
                opp_val = getattr(old_value, "Transformation46", None)
                if opp_val == self:
                    setattr(old_value, "Transformation46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transformation46"):
                opp_val = getattr(value, "Transformation46", None)
                setattr(value, "Transformation46", self)

class JTLMM_emof_TypedElement(NamedElement):

    def __init__(self, type: str, NamedElement: "JTLMM_emof_Comment" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class JTLMM_emof_EnumerationLiteral(NamedElement):

    pass
class JTLMM_JTL_Domain(NamedElement):

    def __init__(self, isCheckable: bool, isEnforceable: bool, domain: "Relation" = None, JTLMM_JTL_Domain: "Pattern" = None, JTLMM_JTL_Domain40: "Model" = None, JTLMM_JTL_Domain43: "Variable" = None, NamedElement: "JTLMM_emof_Comment" = None):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.domain = domain
        self.JTLMM_JTL_Domain = JTLMM_JTL_Domain
        self.JTLMM_JTL_Domain40 = JTLMM_JTL_Domain40
        self.JTLMM_JTL_Domain43 = JTLMM_JTL_Domain43
        
        pass
    @property
    def isCheckable(self):
        return self.__isCheckable

    @isCheckable.setter
    def isCheckable(self, isCheckable: bool):
        self.__isCheckable = isCheckable


    @property
    def isEnforceable(self):
        return self.__isEnforceable

    @isEnforceable.setter
    def isEnforceable(self, isEnforceable: bool):
        self.__isEnforceable = isEnforceable


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
            if hasattr(old_value, "Pattern38"):
                opp_val = getattr(old_value, "Pattern38", None)
                if opp_val == self:
                    setattr(old_value, "Pattern38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern38"):
                opp_val = getattr(value, "Pattern38", None)
                setattr(value, "Pattern38", self)

    @property
    def JTLMM_JTL_Domain40(self):
        return self.__JTLMM_JTL_Domain40

    @JTLMM_JTL_Domain40.setter
    def JTLMM_JTL_Domain40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Domain__JTLMM_JTL_Domain40", None)
        self.__JTLMM_JTL_Domain40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model41"):
                opp_val = getattr(old_value, "Model41", None)
                if opp_val == self:
                    setattr(old_value, "Model41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model41"):
                opp_val = getattr(value, "Model41", None)
                setattr(value, "Model41", self)

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Domain__domain", None)
        self.__domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relation36"):
                opp_val = getattr(old_value, "Relation36", None)
                if opp_val == self:
                    setattr(old_value, "Relation36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relation36"):
                opp_val = getattr(value, "Relation36", None)
                setattr(value, "Relation36", self)

    @property
    def JTLMM_JTL_Domain43(self):
        return self.__JTLMM_JTL_Domain43

    @JTLMM_JTL_Domain43.setter
    def JTLMM_JTL_Domain43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Domain__JTLMM_JTL_Domain43", None)
        self.__JTLMM_JTL_Domain43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable44"):
                opp_val = getattr(old_value, "Variable44", None)
                if opp_val == self:
                    setattr(old_value, "Variable44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable44"):
                opp_val = getattr(value, "Variable44", None)
                setattr(value, "Variable44", self)

class JTLMM_JTL_Relation(NamedElement):

    def __init__(self, isTopLevel: bool, JTLMM_JTL_Relation: set["Variable"] = None, relation: "Transformation" = None, relation30: set["Domain"] = None, whereOwner: "Pattern" = None, whenOwner: "Pattern" = None, NamedElement: "JTLMM_emof_Comment" = None):
        self.isTopLevel = isTopLevel
        self.JTLMM_JTL_Relation = JTLMM_JTL_Relation if JTLMM_JTL_Relation is not None else set()
        self.relation = relation
        self.relation30 = relation30 if relation30 is not None else set()
        self.whereOwner = whereOwner
        self.whenOwner = whenOwner
        
        pass
    @property
    def isTopLevel(self):
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: bool):
        self.__isTopLevel = isTopLevel


    @property
    def whenOwner(self):
        return self.__whenOwner

    @whenOwner.setter
    def whenOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Relation__whenOwner", None)
        self.__whenOwner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern33"):
                opp_val = getattr(old_value, "Pattern33", None)
                if opp_val == self:
                    setattr(old_value, "Pattern33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern33"):
                opp_val = getattr(value, "Pattern33", None)
                setattr(value, "Pattern33", self)

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
    def relation(self):
        return self.__relation

    @relation.setter
    def relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Relation__relation", None)
        self.__relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transformation"):
                opp_val = getattr(old_value, "Transformation", None)
                if opp_val == self:
                    setattr(old_value, "Transformation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transformation"):
                opp_val = getattr(value, "Transformation", None)
                setattr(value, "Transformation", self)

    @property
    def relation30(self):
        return self.__relation30

    @relation30.setter
    def relation30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Relation__relation30", None)
        self.__relation30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Domain"):
                    opp_val = getattr(item, "Domain", None)
                    
                    if opp_val == self:
                        setattr(item, "Domain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Domain"):
                    opp_val = getattr(item, "Domain", None)
                    
                    setattr(item, "Domain", self)
                    

    @property
    def whereOwner(self):
        return self.__whereOwner

    @whereOwner.setter
    def whereOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_JTL_Relation__whereOwner", None)
        self.__whereOwner = value
        
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

class JTLMM_emof_Type(NamedElement):

    pass
class JTLMM_emof_Package(NamedElement):

    def __init__(self, uri: str, package: set["Type"] = None, JTLMM_emof_Package: set["Package"] = None, NamedElement: "JTLMM_emof_Comment" = None):
        self.uri = uri
        self.package = package if package is not None else set()
        self.JTLMM_emof_Package = JTLMM_emof_Package if JTLMM_emof_Package is not None else set()
        
        pass
    @property
    def uri(self):
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
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Package__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type13"):
                    opp_val = getattr(item, "Type13", None)
                    
                    if opp_val == self:
                        setattr(item, "Type13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type13"):
                    opp_val = getattr(item, "Type13", None)
                    
                    setattr(item, "Type13", self)
                    

class JTLMM_emof_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: int, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
        pass
    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered


class Parameter:

    pass
class emof_TypedElement:

    pass
class JTLMM_emof_Property(emof_MultiplicityElement, emof_TypedElement):

    def __init__(self, isReadOnly: bool, isDerived: bool, isComposite: bool, isId: bool, default: str, ownedAttribute: "Class" = None, JTLMM_emof_Property: "Property" = None):
        self.isReadOnly = isReadOnly
        self.isDerived = isDerived
        self.isComposite = isComposite
        self.isId = isId
        self.default = default
        self.ownedAttribute = ownedAttribute
        self.JTLMM_emof_Property = JTLMM_emof_Property
        
        pass
    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def isId(self):
        return self.__isId

    @isId.setter
    def isId(self, isId: bool):
        self.__isId = isId


    @property
    def isComposite(self):
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
            if hasattr(old_value, "Property23"):
                opp_val = getattr(old_value, "Property23", None)
                if opp_val == self:
                    setattr(old_value, "Property23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property23"):
                opp_val = getattr(value, "Property23", None)
                setattr(value, "Property23", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class21"):
                opp_val = getattr(old_value, "Class21", None)
                if opp_val == self:
                    setattr(old_value, "Class21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class21"):
                opp_val = getattr(value, "Class21", None)
                setattr(value, "Class21", self)

class JTLMM_emof_Parameter(emof_MultiplicityElement, emof_TypedElement):

    pass
class JTLMM_emof_Operation(emof_MultiplicityElement, emof_TypedElement):

    pass
class Class:

    pass
class JTLMM_imperativeocl_Typedef(Class):

    pass
class JTLMM_imperativeocl_AnonymousTupleType(Class):

    pass
class Operation:

    pass
class Property:

    pass
class Type:

    pass
class JTLMM_emof_DataType(Type):

    pass
class JTLMM_imperativeocl_TemplateParameterType(Type):

    def __init__(self, specification: str, Type131: "JTLMM_essentialocl_CollectionType" = None, Type219: "JTLMM_imperativeocl_DictionaryType" = None, Type92: "JTLMM_essentialocl_TypeExp" = None, Type: "JTLMM_emof_Operation" = None, Type197: "JTLMM_imperativeocl_TryExp" = None, Type202: "JTLMM_imperativeocl_RaiseExp" = None, Type13: "JTLMM_emof_Package" = None, Type206: "JTLMM_imperativeocl_Typedef" = None, Type242: "JTLMM_imperativeocl_AnonymousTupleType" = None):
        self.specification = specification
        
        pass
    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


class JTLMM_essentialocl_VoidType(Type):

    pass
class JTLMM_essentialocl_InvalidType(Type):

    pass
class JTLMM_emof_Class(Type):

    def __init__(self, isAbstract: bool, Class: set["Property"] = None, class_: set["Operation"] = None, JTLMM_emof_Class: set["Class"] = None, Type131: "JTLMM_essentialocl_CollectionType" = None, Type219: "JTLMM_imperativeocl_DictionaryType" = None, Type92: "JTLMM_essentialocl_TypeExp" = None, Type: "JTLMM_emof_Operation" = None, Type197: "JTLMM_imperativeocl_TryExp" = None, Type202: "JTLMM_imperativeocl_RaiseExp" = None, Type13: "JTLMM_emof_Package" = None, Type206: "JTLMM_imperativeocl_Typedef" = None, Type242: "JTLMM_imperativeocl_AnonymousTupleType" = None):
        self.isAbstract = isAbstract
        self.Class = Class if Class is not None else set()
        self.class_ = class_ if class_ is not None else set()
        self.JTLMM_emof_Class = JTLMM_emof_Class if JTLMM_emof_Class is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract


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
                if hasattr(item, "Class3"):
                    opp_val = getattr(item, "Class3", None)
                    
                    if opp_val == self:
                        setattr(item, "Class3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class3"):
                    opp_val = getattr(item, "Class3", None)
                    
                    setattr(item, "Class3", self)
                    

    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Class__class_", None)
        self.__class_ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTLMM_emof_Class__Class", None)
        self.__Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

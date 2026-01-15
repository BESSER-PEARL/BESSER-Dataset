from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinaryOp(Enum):
    EQUAL = "EQUAL"
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
class ResolveTraceCardinality(Enum):
    ONE_ONE = "ONE_ONE"
    ZERO_OR_ONE = "ZERO_OR_ONE"
    MANY = "MANY"


############################################
# Definition of Classes
############################################

class core_TraceCompareExpression:

    def __init__(self, multivaluedTag: bool, core_TraceCompareExpression: "core_MatchTrace" = None, core_TraceCompareExpression91: "core_TraceElement" = None, core_TraceCompareExpression94: "core_Expression" = None):
        self.multivaluedTag = multivaluedTag
        self.core_TraceCompareExpression = core_TraceCompareExpression
        self.core_TraceCompareExpression91 = core_TraceCompareExpression91
        self.core_TraceCompareExpression94 = core_TraceCompareExpression94
        
    @property
    def multivaluedTag(self) -> bool:
        return self.__multivaluedTag

    @multivaluedTag.setter
    def multivaluedTag(self, multivaluedTag: bool):
        self.__multivaluedTag = multivaluedTag

    @property
    def core_TraceCompareExpression94(self):
        return self.__core_TraceCompareExpression94

    @core_TraceCompareExpression94.setter
    def core_TraceCompareExpression94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_TraceCompareExpression__core_TraceCompareExpression94", None)
        self.__core_TraceCompareExpression94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Expression95"):
                opp_val = getattr(old_value, "core_Expression95", None)
                if opp_val == self:
                    setattr(old_value, "core_Expression95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Expression95"):
                opp_val = getattr(value, "core_Expression95", None)
                setattr(value, "core_Expression95", self)

    @property
    def core_TraceCompareExpression(self):
        return self.__core_TraceCompareExpression

    @core_TraceCompareExpression.setter
    def core_TraceCompareExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_TraceCompareExpression__core_TraceCompareExpression", None)
        self.__core_TraceCompareExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_MatchTrace89"):
                opp_val = getattr(old_value, "core_MatchTrace89", None)
                if opp_val == self:
                    setattr(old_value, "core_MatchTrace89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_MatchTrace89"):
                opp_val = getattr(value, "core_MatchTrace89", None)
                setattr(value, "core_MatchTrace89", self)

    @property
    def core_TraceCompareExpression91(self):
        return self.__core_TraceCompareExpression91

    @core_TraceCompareExpression91.setter
    def core_TraceCompareExpression91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_TraceCompareExpression__core_TraceCompareExpression91", None)
        self.__core_TraceCompareExpression91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_TraceElement92"):
                opp_val = getattr(old_value, "core_TraceElement92", None)
                if opp_val == self:
                    setattr(old_value, "core_TraceElement92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_TraceElement92"):
                opp_val = getattr(value, "core_TraceElement92", None)
                setattr(value, "core_TraceElement92", self)

class core_PutTraceParameter:

    pass
class InlineFeature:

    pass
class core_InlineReference(InlineFeature):

    pass
class core_InlineAttribute(InlineFeature):

    pass
class core_TypedWithClass(ABC):

    pass
class ImplicitlyAnnotableElement:

    pass
class TypeExpression:

    pass
class core_TraceUse(TypeExpression):

    pass
class core_ClassUse(TypeExpression, ImplicitlyAnnotableElement):

    def __init__(self, className: str, strictType: bool, core_ClassUse: "core_RepresentModel" = None, core_ClassUse72: "core_TypedWithClass" = None):
        self.className = className
        self.strictType = strictType
        self.core_ClassUse = core_ClassUse
        self.core_ClassUse72 = core_ClassUse72
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def strictType(self) -> bool:
        return self.__strictType

    @strictType.setter
    def strictType(self, strictType: bool):
        self.__strictType = strictType

    @property
    def core_ClassUse72(self):
        return self.__core_ClassUse72

    @core_ClassUse72.setter
    def core_ClassUse72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ClassUse__core_ClassUse72", None)
        self.__core_ClassUse72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_TypedWithClass"):
                opp_val = getattr(old_value, "core_TypedWithClass", None)
                if opp_val == self:
                    setattr(old_value, "core_TypedWithClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_TypedWithClass"):
                opp_val = getattr(value, "core_TypedWithClass", None)
                setattr(value, "core_TypedWithClass", self)

    @property
    def core_ClassUse(self):
        return self.__core_ClassUse

    @core_ClassUse.setter
    def core_ClassUse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ClassUse__core_ClassUse", None)
        self.__core_ClassUse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_RepresentModel69"):
                opp_val = getattr(old_value, "core_RepresentModel69", None)
                if opp_val == self:
                    setattr(old_value, "core_RepresentModel69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_RepresentModel69"):
                opp_val = getattr(value, "core_RepresentModel69", None)
                setattr(value, "core_RepresentModel69", self)

class core_TypeExpression(ABC):

    pass
class core_IfBranch:

    pass
class ClassUse:

    pass
class core_KeywordParameter:

    def __init__(self, keyword: str, core_KeywordParameter: "core_KeywordMethodCall" = None, core_KeywordParameter40: "core_Expression" = None):
        self.keyword = keyword
        self.core_KeywordParameter = core_KeywordParameter
        self.core_KeywordParameter40 = core_KeywordParameter40
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def core_KeywordParameter(self):
        return self.__core_KeywordParameter

    @core_KeywordParameter.setter
    def core_KeywordParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_KeywordParameter__core_KeywordParameter", None)
        self.__core_KeywordParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_KeywordMethodCall38"):
                opp_val = getattr(old_value, "core_KeywordMethodCall38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_KeywordMethodCall38"):
                opp_val = getattr(value, "core_KeywordMethodCall38", None)
                if opp_val is None:
                    setattr(value, "core_KeywordMethodCall38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def core_KeywordParameter40(self):
        return self.__core_KeywordParameter40

    @core_KeywordParameter40.setter
    def core_KeywordParameter40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_KeywordParameter__core_KeywordParameter40", None)
        self.__core_KeywordParameter40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Expression41"):
                opp_val = getattr(old_value, "core_Expression41", None)
                if opp_val == self:
                    setattr(old_value, "core_Expression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Expression41"):
                opp_val = getattr(value, "core_Expression41", None)
                setattr(value, "core_Expression41", self)

class Statement:

    pass
class core_Expression(Statement):

    pass
class core_Variable(ABC):

    def __init__(self, name: str, core_Variable: "core_PropertyWrite" = None, core_Variable29: "core_VariableReference" = None):
        self.name = name
        self.core_Variable = core_Variable
        self.core_Variable29 = core_Variable29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def core_Variable(self):
        return self.__core_Variable

    @core_Variable.setter
    def core_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Variable__core_Variable", None)
        self.__core_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_PropertyWrite"):
                opp_val = getattr(old_value, "core_PropertyWrite", None)
                if opp_val == self:
                    setattr(old_value, "core_PropertyWrite", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_PropertyWrite"):
                opp_val = getattr(value, "core_PropertyWrite", None)
                setattr(value, "core_PropertyWrite", self)

    @property
    def core_Variable29(self):
        return self.__core_Variable29

    @core_Variable29.setter
    def core_Variable29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_Variable__core_Variable29", None)
        self.__core_Variable29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_VariableReference"):
                opp_val = getattr(old_value, "core_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "core_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_VariableReference"):
                opp_val = getattr(value, "core_VariableReference", None)
                setattr(value, "core_VariableReference", self)

class RequireParameter:

    pass
class core_RequireModelParameter(RequireParameter):

    pass
class core_RequireParameter(ABC):

    def __init__(self, formalParameterName: str, core_RequireParameter: "core_RequireDeclaration" = None):
        self.formalParameterName = formalParameterName
        self.core_RequireParameter = core_RequireParameter
        
    @property
    def formalParameterName(self) -> str:
        return self.__formalParameterName

    @formalParameterName.setter
    def formalParameterName(self, formalParameterName: str):
        self.__formalParameterName = formalParameterName

    @property
    def core_RequireParameter(self):
        return self.__core_RequireParameter

    @core_RequireParameter.setter
    def core_RequireParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_RequireParameter__core_RequireParameter", None)
        self.__core_RequireParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_RequireDeclaration21"):
                opp_val = getattr(old_value, "core_RequireDeclaration21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_RequireDeclaration21"):
                opp_val = getattr(value, "core_RequireDeclaration21", None)
                if opp_val is None:
                    setattr(value, "core_RequireDeclaration21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Expression:

    pass
class core_ClosureDeclaration(Expression):

    pass
class core_PutTrace(Expression):

    pass
class core_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class core_VariableReference(Expression):

    pass
class core_IfExpr(Expression):

    pass
class core_KeywordMethodCall(Expression):

    pass
class core_BinaryExpr(Expression):

    def __init__(self, binaryOp: str, core_BinaryExpr: "core_Expression" = None, core_BinaryExpr45: "core_Expression" = None):
        self.binaryOp = binaryOp
        self.core_BinaryExpr = core_BinaryExpr
        self.core_BinaryExpr45 = core_BinaryExpr45
        
    @property
    def binaryOp(self) -> str:
        return self.__binaryOp

    @binaryOp.setter
    def binaryOp(self, binaryOp: str):
        self.__binaryOp = binaryOp

    @property
    def core_BinaryExpr45(self):
        return self.__core_BinaryExpr45

    @core_BinaryExpr45.setter
    def core_BinaryExpr45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_BinaryExpr__core_BinaryExpr45", None)
        self.__core_BinaryExpr45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Expression46"):
                opp_val = getattr(old_value, "core_Expression46", None)
                if opp_val == self:
                    setattr(old_value, "core_Expression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Expression46"):
                opp_val = getattr(value, "core_Expression46", None)
                setattr(value, "core_Expression46", self)

    @property
    def core_BinaryExpr(self):
        return self.__core_BinaryExpr

    @core_BinaryExpr.setter
    def core_BinaryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_BinaryExpr__core_BinaryExpr", None)
        self.__core_BinaryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Expression43"):
                opp_val = getattr(old_value, "core_Expression43", None)
                if opp_val == self:
                    setattr(old_value, "core_Expression43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Expression43"):
                opp_val = getattr(value, "core_Expression43", None)
                setattr(value, "core_Expression43", self)

class core_DoubleLiteral(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class core_NumLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class core_MethodCall(Expression):

    def __init__(self, methodName: str, withParameters: bool, core_MethodCall: "core_Expression" = None, core_MethodCall33: set["core_Expression"] = None):
        self.methodName = methodName
        self.withParameters = withParameters
        self.core_MethodCall = core_MethodCall
        self.core_MethodCall33 = core_MethodCall33 if core_MethodCall33 is not None else set()
        
    @property
    def withParameters(self) -> bool:
        return self.__withParameters

    @withParameters.setter
    def withParameters(self, withParameters: bool):
        self.__withParameters = withParameters

    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

    @property
    def core_MethodCall(self):
        return self.__core_MethodCall

    @core_MethodCall.setter
    def core_MethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_MethodCall__core_MethodCall", None)
        self.__core_MethodCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Expression31"):
                opp_val = getattr(old_value, "core_Expression31", None)
                if opp_val == self:
                    setattr(old_value, "core_Expression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Expression31"):
                opp_val = getattr(value, "core_Expression31", None)
                setattr(value, "core_Expression31", self)

    @property
    def core_MethodCall33(self):
        return self.__core_MethodCall33

    @core_MethodCall33.setter
    def core_MethodCall33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_MethodCall__core_MethodCall33", None)
        self.__core_MethodCall33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_Expression34"):
                    opp_val = getattr(item, "core_Expression34", None)
                    
                    if opp_val == self:
                        setattr(item, "core_Expression34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_Expression34"):
                    opp_val = getattr(item, "core_Expression34", None)
                    
                    setattr(item, "core_Expression34", self)
                    

class core_MatchTrace(Expression):

    def __init__(self, cardinality: str, core_MatchTrace: "core_TraceDefinition" = None, core_MatchTrace89: "core_TraceCompareExpression" = None):
        self.cardinality = cardinality
        self.core_MatchTrace = core_MatchTrace
        self.core_MatchTrace89 = core_MatchTrace89
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def core_MatchTrace(self):
        return self.__core_MatchTrace

    @core_MatchTrace.setter
    def core_MatchTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_MatchTrace__core_MatchTrace", None)
        self.__core_MatchTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_TraceDefinition87"):
                opp_val = getattr(old_value, "core_TraceDefinition87", None)
                if opp_val == self:
                    setattr(old_value, "core_TraceDefinition87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_TraceDefinition87"):
                opp_val = getattr(value, "core_TraceDefinition87", None)
                setattr(value, "core_TraceDefinition87", self)

    @property
    def core_MatchTrace89(self):
        return self.__core_MatchTrace89

    @core_MatchTrace89.setter
    def core_MatchTrace89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_MatchTrace__core_MatchTrace89", None)
        self.__core_MatchTrace89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_TraceCompareExpression"):
                opp_val = getattr(old_value, "core_TraceCompareExpression", None)
                if opp_val == self:
                    setattr(old_value, "core_TraceCompareExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_TraceCompareExpression"):
                opp_val = getattr(value, "core_TraceCompareExpression", None)
                setattr(value, "core_TraceCompareExpression", self)

class core_ResolveLink(Expression):

    def __init__(self, isExternal: str, linkName: str, featureName: str, core_ResolveLink: "core_Expression" = None, core_ResolveLink53: "core_UseDeclaration" = None):
        self.isExternal = isExternal
        self.linkName = linkName
        self.featureName = featureName
        self.core_ResolveLink = core_ResolveLink
        self.core_ResolveLink53 = core_ResolveLink53
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def linkName(self) -> str:
        return self.__linkName

    @linkName.setter
    def linkName(self, linkName: str):
        self.__linkName = linkName

    @property
    def isExternal(self) -> str:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal

    @property
    def core_ResolveLink53(self):
        return self.__core_ResolveLink53

    @core_ResolveLink53.setter
    def core_ResolveLink53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ResolveLink__core_ResolveLink53", None)
        self.__core_ResolveLink53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_UseDeclaration54"):
                opp_val = getattr(old_value, "core_UseDeclaration54", None)
                if opp_val == self:
                    setattr(old_value, "core_UseDeclaration54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_UseDeclaration54"):
                opp_val = getattr(value, "core_UseDeclaration54", None)
                setattr(value, "core_UseDeclaration54", self)

    @property
    def core_ResolveLink(self):
        return self.__core_ResolveLink

    @core_ResolveLink.setter
    def core_ResolveLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_ResolveLink__core_ResolveLink", None)
        self.__core_ResolveLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Expression51"):
                opp_val = getattr(old_value, "core_Expression51", None)
                if opp_val == self:
                    setattr(old_value, "core_Expression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Expression51"):
                opp_val = getattr(value, "core_Expression51", None)
                setattr(value, "core_Expression51", self)

class core_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class core_ModelReference(ClassUse, Expression):

    pass
class core_PropertyWrite(Expression):

    def __init__(self, property: str, core_PropertyWrite: "core_Variable" = None, core_PropertyWrite26: "core_Expression" = None):
        self.property = property
        self.core_PropertyWrite = core_PropertyWrite
        self.core_PropertyWrite26 = core_PropertyWrite26
        
    @property
    def property(self) -> str:
        return self.__property

    @property.setter
    def property(self, property: str):
        self.__property = property

    @property
    def core_PropertyWrite(self):
        return self.__core_PropertyWrite

    @core_PropertyWrite.setter
    def core_PropertyWrite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_PropertyWrite__core_PropertyWrite", None)
        self.__core_PropertyWrite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Variable"):
                opp_val = getattr(old_value, "core_Variable", None)
                if opp_val == self:
                    setattr(old_value, "core_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Variable"):
                opp_val = getattr(value, "core_Variable", None)
                setattr(value, "core_Variable", self)

    @property
    def core_PropertyWrite26(self):
        return self.__core_PropertyWrite26

    @core_PropertyWrite26.setter
    def core_PropertyWrite26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_PropertyWrite__core_PropertyWrite26", None)
        self.__core_PropertyWrite26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Expression27"):
                opp_val = getattr(old_value, "core_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "core_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Expression27"):
                opp_val = getattr(value, "core_Expression27", None)
                setattr(value, "core_Expression27", self)

class Variable:

    pass
class core_ClosureParameter(Variable):

    pass
class core_DefineVariable(Variable, Statement):

    pass
class TransformationDefinition:

    pass
class core_EclecticTransformationDefinition(TransformationDefinition):

    pass
class ModuleDefinition:

    pass
class core_TraceInterface(ModuleDefinition):

    pass
class RepresentModel:

    pass
class core_UseDeclaration(RepresentModel):

    def __init__(self, module: str, as: str, core_UseDeclaration: "core_TransformationDefinition" = None, core_UseDeclaration54: "core_ResolveLink" = None):
        self.module = module
        self.as = as
        self.core_UseDeclaration = core_UseDeclaration
        self.core_UseDeclaration54 = core_UseDeclaration54
        
    @property
    def as(self) -> str:
        return self.__as

    @as.setter
    def as(self, as: str):
        self.__as = as

    @property
    def module(self) -> str:
        return self.__module

    @module.setter
    def module(self, module: str):
        self.__module = module

    @property
    def core_UseDeclaration54(self):
        return self.__core_UseDeclaration54

    @core_UseDeclaration54.setter
    def core_UseDeclaration54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_UseDeclaration__core_UseDeclaration54", None)
        self.__core_UseDeclaration54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_ResolveLink53"):
                opp_val = getattr(old_value, "core_ResolveLink53", None)
                if opp_val == self:
                    setattr(old_value, "core_ResolveLink53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_ResolveLink53"):
                opp_val = getattr(value, "core_ResolveLink53", None)
                setattr(value, "core_ResolveLink53", self)

    @property
    def core_UseDeclaration(self):
        return self.__core_UseDeclaration

    @core_UseDeclaration.setter
    def core_UseDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_UseDeclaration__core_UseDeclaration", None)
        self.__core_UseDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_TransformationDefinition15"):
                opp_val = getattr(old_value, "core_TransformationDefinition15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_TransformationDefinition15"):
                opp_val = getattr(value, "core_TransformationDefinition15", None)
                if opp_val is None:
                    setattr(value, "core_TransformationDefinition15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class core_InlineModel(RepresentModel, ModuleDefinition):

    pass
class core_RequireDeclaration(RepresentModel):

    def __init__(self, name: str, default: str, core_RequireDeclaration: "core_TransformationDefinition" = None, core_RequireDeclaration21: set["core_RequireParameter"] = None):
        self.name = name
        self.default = default
        self.core_RequireDeclaration = core_RequireDeclaration
        self.core_RequireDeclaration21 = core_RequireDeclaration21 if core_RequireDeclaration21 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def core_RequireDeclaration21(self):
        return self.__core_RequireDeclaration21

    @core_RequireDeclaration21.setter
    def core_RequireDeclaration21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_RequireDeclaration__core_RequireDeclaration21", None)
        self.__core_RequireDeclaration21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_RequireParameter"):
                    opp_val = getattr(item, "core_RequireParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "core_RequireParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_RequireParameter"):
                    opp_val = getattr(item, "core_RequireParameter", None)
                    
                    setattr(item, "core_RequireParameter", self)
                    

    @property
    def core_RequireDeclaration(self):
        return self.__core_RequireDeclaration

    @core_RequireDeclaration.setter
    def core_RequireDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_RequireDeclaration__core_RequireDeclaration", None)
        self.__core_RequireDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_TransformationDefinition17"):
                opp_val = getattr(old_value, "core_TransformationDefinition17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_TransformationDefinition17"):
                opp_val = getattr(value, "core_TransformationDefinition17", None)
                if opp_val is None:
                    setattr(value, "core_TransformationDefinition17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class core_GenericAnnotation:

    def __init__(self, name: str, core_GenericAnnotation: set["core_AnnotationParameter"] = None):
        self.name = name
        self.core_GenericAnnotation = core_GenericAnnotation if core_GenericAnnotation is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def core_GenericAnnotation(self):
        return self.__core_GenericAnnotation

    @core_GenericAnnotation.setter
    def core_GenericAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_GenericAnnotation__core_GenericAnnotation", None)
        self.__core_GenericAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_AnnotationParameter"):
                    opp_val = getattr(item, "core_AnnotationParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "core_AnnotationParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_AnnotationParameter"):
                    opp_val = getattr(item, "core_AnnotationParameter", None)
                    
                    setattr(item, "core_AnnotationParameter", self)
                    

class SingleAnnotation:

    pass
class core_PotencyAnnotation(SingleAnnotation):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Annotation:

    pass
class core_MetamodelModelAnnotation(Annotation):

    def __init__(self, metamodel: str):
        self.metamodel = metamodel
        
    @property
    def metamodel(self) -> str:
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel

class core_OptimizationsAnnotation(Annotation):

    def __init__(self, enabled: bool):
        self.enabled = enabled
        
    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

class core_SingleAnnotation(Annotation):

    pass
class core_ImplicitlyAnnotableElement:

    pass
class core_TransformationDefinition(ModuleDefinition):

    pass
class core_AnnotationParameter(ABC):

    pass
class DefinitionParameter:

    pass
class core_TracedModelParameter(RepresentModel, DefinitionParameter):

    pass
class core_TransformationDefinitionParameter(RepresentModel, DefinitionParameter):

    pass
class core_ModuleParameter(DefinitionParameter):

    pass
class NamedElement:

    pass
class core_TraceDefinition(NamedElement):

    pass
class core_ImportedModel(NamedElement, RepresentModel):

    pass
class core_InlineClass(NamedElement):

    pass
class core_TraceElement(NamedElement):

    pass
class core_InlineFeature(NamedElement):

    def __init__(self, multivalued: bool, core_InlineFeature: "core_InlineClass" = None, core_InlineFeature84: "core_TypeExpression" = None):
        self.multivalued = multivalued
        self.core_InlineFeature = core_InlineFeature
        self.core_InlineFeature84 = core_InlineFeature84
        
    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

    @property
    def core_InlineFeature84(self):
        return self.__core_InlineFeature84

    @core_InlineFeature84.setter
    def core_InlineFeature84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_InlineFeature__core_InlineFeature84", None)
        self.__core_InlineFeature84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_TypeExpression85"):
                opp_val = getattr(old_value, "core_TypeExpression85", None)
                if opp_val == self:
                    setattr(old_value, "core_TypeExpression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_TypeExpression85"):
                opp_val = getattr(value, "core_TypeExpression85", None)
                setattr(value, "core_TypeExpression85", self)

    @property
    def core_InlineFeature(self):
        return self.__core_InlineFeature

    @core_InlineFeature.setter
    def core_InlineFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_InlineFeature__core_InlineFeature", None)
        self.__core_InlineFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_InlineClass82"):
                opp_val = getattr(old_value, "core_InlineClass82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_InlineClass82"):
                opp_val = getattr(value, "core_InlineClass82", None)
                if opp_val is None:
                    setattr(value, "core_InlineClass82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class core_DefinitionParameter(NamedElement):

    pass
class core_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class core_LocatedElement(ABC):

    def __init__(self, row: int, column: int, file: str):
        self.row = row
        self.column = column
        self.file = file
        
    @property
    def column(self) -> int:
        return self.__column

    @column.setter
    def column(self, column: int):
        self.__column = column

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def row(self) -> int:
        return self.__row

    @row.setter
    def row(self, row: int):
        self.__row = row

class core_Annotation(ABC):

    pass
class core_AnnotableElement(ABC):

    pass
class AnnotableElement:

    pass
class core_RepresentModel(AnnotableElement):

    pass
class LocatedElement:

    pass
class core_Statement(LocatedElement):

    pass
class core_ModuleDefinition(NamedElement, LocatedElement, AnnotableElement):

    pass
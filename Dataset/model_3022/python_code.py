from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BindingExprOpKind(Enum):
    ASSIGN = "ASSIGN"
    ADD = "ADD"
    BOOL = "BOOL"


############################################
# Definition of Classes
############################################

class dbl_ExpandableElement:

    pass
class Module:

    pass
class QuotedCode:

    pass
class dbl_QuotedStatements(QuotedCode):

    pass
class dbl_QuotedModuleContent(Module, QuotedCode):

    pass
class dbl_QuotedExpression(QuotedCode):

    pass
class dbl_QuotedCode:

    pass
class MappingPart:

    pass
class dbl_DynamicMappingPart(MappingPart):

    pass
class dbl_FixedMappingPart(MappingPart):

    def __init__(self, code: str):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class dbl_PropertyType(ABC):

    pass
class dbl_MappingPart(ABC):

    pass
class StructuredPropertyType:

    pass
class dbl_ReferencePropertyType(StructuredPropertyType):

    def __init__(self, rawReference: bool, dbl_ReferencePropertyType: "dbl_Pattern" = None):
        self.rawReference = rawReference
        self.dbl_ReferencePropertyType = dbl_ReferencePropertyType
        
    @property
    def rawReference(self) -> bool:
        return self.__rawReference

    @rawReference.setter
    def rawReference(self, rawReference: bool):
        self.__rawReference = rawReference

    @property
    def dbl_ReferencePropertyType(self):
        return self.__dbl_ReferencePropertyType

    @dbl_ReferencePropertyType.setter
    def dbl_ReferencePropertyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ReferencePropertyType__dbl_ReferencePropertyType", None)
        self.__dbl_ReferencePropertyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Pattern"):
                opp_val = getattr(old_value, "dbl_Pattern", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Pattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Pattern"):
                opp_val = getattr(value, "dbl_Pattern", None)
                setattr(value, "dbl_Pattern", self)

class dbl_CompositePropertyType(StructuredPropertyType):

    def __init__(self, list: bool):
        self.list = list
        
    @property
    def list(self) -> bool:
        return self.__list

    @list.setter
    def list(self, list: bool):
        self.__list = list

class PropertyType:

    pass
class dbl_BooleanPropertyType(PropertyType):

    def __init__(self, terminal: str):
        self.terminal = terminal
        
    @property
    def terminal(self) -> str:
        return self.__terminal

    @terminal.setter
    def terminal(self, terminal: str):
        self.__terminal = terminal

class dbl_StringPropertyType(PropertyType):

    pass
class dbl_StructuredPropertyType(PropertyType):

    pass
class dbl_IntPropertyType(PropertyType):

    pass
class dbl_IdPropertyType(PropertyType):

    pass
class RhsExpression:

    pass
class dbl_SequenceExpr(RhsExpression):

    pass
class dbl_TerminalExpr(RhsExpression):

    def __init__(self, terminal: str):
        self.terminal = terminal
        
    @property
    def terminal(self) -> str:
        return self.__terminal

    @terminal.setter
    def terminal(self, terminal: str):
        self.__terminal = terminal

class dbl_AlternativeExpr(RhsExpression):

    pass
class dbl_ArbitraryExpr(RhsExpression):

    pass
class dbl_AtLeastOneExpr(RhsExpression):

    pass
class dbl_RuntimeExpr(RhsExpression):

    pass
class dbl_OptionalExpr(RhsExpression):

    pass
class dbl_RuleExpr(RhsExpression):

    pass
class dbl_RhsExpression(ABC):

    def __init__(self, dbl_RhsExpression: "dbl_TsRule" = None, dbl_RhsExpression192: "dbl_SequenceExpr" = None, dbl_RhsExpression194: "dbl_OptionalExpr" = None, dbl_RhsExpression196: "dbl_RuntimeExpr" = None, dbl_RhsExpression198: "dbl_AtLeastOneExpr" = None, dbl_RhsExpression200: "dbl_ArbitraryExpr" = None, dbl_RhsExpression202: "dbl_AlternativeExpr" = None, dbl_RhsExpression205: "dbl_AlternativeExpr" = None):
        self.dbl_RhsExpression = dbl_RhsExpression
        self.dbl_RhsExpression192 = dbl_RhsExpression192
        self.dbl_RhsExpression194 = dbl_RhsExpression194
        self.dbl_RhsExpression196 = dbl_RhsExpression196
        self.dbl_RhsExpression198 = dbl_RhsExpression198
        self.dbl_RhsExpression200 = dbl_RhsExpression200
        self.dbl_RhsExpression202 = dbl_RhsExpression202
        self.dbl_RhsExpression205 = dbl_RhsExpression205
        
    @property
    def dbl_RhsExpression(self):
        return self.__dbl_RhsExpression

    @dbl_RhsExpression.setter
    def dbl_RhsExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression", None)
        self.__dbl_RhsExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_TsRule185"):
                opp_val = getattr(old_value, "dbl_TsRule185", None)
                if opp_val == self:
                    setattr(old_value, "dbl_TsRule185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_TsRule185"):
                opp_val = getattr(value, "dbl_TsRule185", None)
                setattr(value, "dbl_TsRule185", self)

    @property
    def dbl_RhsExpression202(self):
        return self.__dbl_RhsExpression202

    @dbl_RhsExpression202.setter
    def dbl_RhsExpression202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression202", None)
        self.__dbl_RhsExpression202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_AlternativeExpr"):
                opp_val = getattr(old_value, "dbl_AlternativeExpr", None)
                if opp_val == self:
                    setattr(old_value, "dbl_AlternativeExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_AlternativeExpr"):
                opp_val = getattr(value, "dbl_AlternativeExpr", None)
                setattr(value, "dbl_AlternativeExpr", self)

    @property
    def dbl_RhsExpression200(self):
        return self.__dbl_RhsExpression200

    @dbl_RhsExpression200.setter
    def dbl_RhsExpression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression200", None)
        self.__dbl_RhsExpression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ArbitraryExpr"):
                opp_val = getattr(old_value, "dbl_ArbitraryExpr", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ArbitraryExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ArbitraryExpr"):
                opp_val = getattr(value, "dbl_ArbitraryExpr", None)
                setattr(value, "dbl_ArbitraryExpr", self)

    @property
    def dbl_RhsExpression198(self):
        return self.__dbl_RhsExpression198

    @dbl_RhsExpression198.setter
    def dbl_RhsExpression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression198", None)
        self.__dbl_RhsExpression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_AtLeastOneExpr"):
                opp_val = getattr(old_value, "dbl_AtLeastOneExpr", None)
                if opp_val == self:
                    setattr(old_value, "dbl_AtLeastOneExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_AtLeastOneExpr"):
                opp_val = getattr(value, "dbl_AtLeastOneExpr", None)
                setattr(value, "dbl_AtLeastOneExpr", self)

    @property
    def dbl_RhsExpression196(self):
        return self.__dbl_RhsExpression196

    @dbl_RhsExpression196.setter
    def dbl_RhsExpression196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression196", None)
        self.__dbl_RhsExpression196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_RuntimeExpr"):
                opp_val = getattr(old_value, "dbl_RuntimeExpr", None)
                if opp_val == self:
                    setattr(old_value, "dbl_RuntimeExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_RuntimeExpr"):
                opp_val = getattr(value, "dbl_RuntimeExpr", None)
                setattr(value, "dbl_RuntimeExpr", self)

    @property
    def dbl_RhsExpression205(self):
        return self.__dbl_RhsExpression205

    @dbl_RhsExpression205.setter
    def dbl_RhsExpression205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression205", None)
        self.__dbl_RhsExpression205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_AlternativeExpr204"):
                opp_val = getattr(old_value, "dbl_AlternativeExpr204", None)
                if opp_val == self:
                    setattr(old_value, "dbl_AlternativeExpr204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_AlternativeExpr204"):
                opp_val = getattr(value, "dbl_AlternativeExpr204", None)
                setattr(value, "dbl_AlternativeExpr204", self)

    @property
    def dbl_RhsExpression192(self):
        return self.__dbl_RhsExpression192

    @dbl_RhsExpression192.setter
    def dbl_RhsExpression192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression192", None)
        self.__dbl_RhsExpression192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_SequenceExpr"):
                opp_val = getattr(old_value, "dbl_SequenceExpr", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_SequenceExpr"):
                opp_val = getattr(value, "dbl_SequenceExpr", None)
                if opp_val is None:
                    setattr(value, "dbl_SequenceExpr", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_RhsExpression194(self):
        return self.__dbl_RhsExpression194

    @dbl_RhsExpression194.setter
    def dbl_RhsExpression194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression194", None)
        self.__dbl_RhsExpression194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_OptionalExpr"):
                opp_val = getattr(old_value, "dbl_OptionalExpr", None)
                if opp_val == self:
                    setattr(old_value, "dbl_OptionalExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_OptionalExpr"):
                opp_val = getattr(value, "dbl_OptionalExpr", None)
                setattr(value, "dbl_OptionalExpr", self)

    def getSubExpressions(self) -> str:
        # TODO: Implement getSubExpressions method
        pass

class dbl_TextualSyntaxDef:

    pass
class Extension:

    pass
class VariableAccess:

    pass
class dbl_MetaAccess(VariableAccess):

    pass
class ElementAccess:

    pass
class dbl_ArgumentExpression:

    pass
class dbl_PredefinedId:

    pass
class dbl_DepIdentifiableElement(ABC):

    pass
class SetOp:

    pass
class dbl_LastInSet(SetOp):

    pass
class dbl_IndexOf(SetOp):

    pass
class dbl_Contains(SetOp):

    pass
class dbl_FirstInSet(SetOp):

    pass
class dbl_AfterInSet(SetOp):

    pass
class dbl_ObjectAt(SetOp):

    pass
class dbl_BeforeInSet(SetOp):

    pass
class dbl_SizeOfSet(SetOp):

    pass
class PredefinedId:

    pass
class dbl_SetOp(PredefinedId):

    pass
class dbl_MetaLiteral(PredefinedId):

    pass
class dbl_TypeLiteral(PredefinedId):

    pass
class dbl_SuperLiteral(PredefinedId):

    pass
class dbl_MeLiteral(PredefinedId):

    pass
class UnaryOperator:

    pass
class dbl_Neg(UnaryOperator):

    pass
class L1Expr:

    pass
class dbl_TrueLiteral(L1Expr):

    pass
class dbl_TimeLiteral(L1Expr):

    pass
class dbl_NullLiteral(L1Expr):

    pass
class dbl_DoubleLiteral(L1Expr):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class dbl_StringLiteral(L1Expr):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dbl_IntLiteral(L1Expr):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class dbl_ActiveLiteral(L1Expr):

    pass
class dbl_FalseLiteral(L1Expr):

    pass
class dbl_Not(UnaryOperator):

    pass
class BinaryOperator:

    pass
class dbl_LessEqual(BinaryOperator):

    pass
class dbl_Mul(BinaryOperator):

    pass
class dbl_GreaterEqual(BinaryOperator):

    pass
class dbl_Equal(BinaryOperator):

    pass
class dbl_Greater(BinaryOperator):

    pass
class dbl_Mod(BinaryOperator):

    pass
class dbl_InstanceOf(BinaryOperator):

    pass
class dbl_Or(BinaryOperator):

    pass
class dbl_Less(BinaryOperator):

    pass
class dbl_Div(BinaryOperator):

    pass
class dbl_Minus(BinaryOperator):

    pass
class dbl_NotEqual(BinaryOperator):

    pass
class dbl_Plus(BinaryOperator):

    pass
class dbl_And(BinaryOperator):

    pass
class Expression:

    pass
class dbl_BinaryOperator(Expression):

    pass
class dbl_UnaryOperator(Expression):

    pass
class dbl_MetaExpr(Expression):

    pass
class dbl_CodeQuoteExpression(Expression):

    pass
class dbl_EvalExpr(Expression):

    pass
class dbl_ElementAccess(Expression):

    pass
class dbl_L1Expr(Expression):

    pass
class CompositeStatement:

    pass
class dbl_ForEachStatement(CompositeStatement):

    pass
class dbl_ExpandSection(CompositeStatement):

    pass
class dbl_WhileStatement(CompositeStatement):

    pass
class dbl_IfStatement(CompositeStatement):

    pass
class SetStatement:

    pass
class dbl_AddToSet(SetStatement):

    pass
class dbl_EmptySet(SetStatement):

    pass
class dbl_RemoveFromSet(SetStatement):

    pass
class StatementExpression:

    pass
class dbl_ExpandExpression(Expression, StatementExpression):

    pass
class dbl_ProcedureCall(StatementExpression):

    pass
class ExpressionStatement:

    pass
class dbl_DeprecatedProcedureCallStatement(ExpressionStatement):

    pass
class Construct:

    pass
class dbl_CodeBlock(Construct):

    pass
class dbl_StatementExpression:

    pass
class SimpleStatement:

    pass
class dbl_Assignment(SimpleStatement):

    pass
class dbl_ContinueStatement(SimpleStatement):

    pass
class dbl_ActivateObject(SimpleStatement):

    def __init__(self, priority: int, dbl_ActivateObject: "dbl_Expression" = None):
        self.priority = priority
        self.dbl_ActivateObject = dbl_ActivateObject
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def dbl_ActivateObject(self):
        return self.__dbl_ActivateObject

    @dbl_ActivateObject.setter
    def dbl_ActivateObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ActivateObject__dbl_ActivateObject", None)
        self.__dbl_ActivateObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Expression106"):
                opp_val = getattr(old_value, "dbl_Expression106", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression106"):
                opp_val = getattr(value, "dbl_Expression106", None)
                setattr(value, "dbl_Expression106", self)

class dbl_SaveGenStatement(SimpleStatement):

    pass
class dbl_ResetGenContextStatement(SimpleStatement):

    pass
class dbl_SetGenContextStatement(SimpleStatement):

    def __init__(self, addAfterContext: bool, dbl_SetGenContextStatement: "dbl_Expression" = None):
        self.addAfterContext = addAfterContext
        self.dbl_SetGenContextStatement = dbl_SetGenContextStatement
        
    @property
    def addAfterContext(self) -> bool:
        return self.__addAfterContext

    @addAfterContext.setter
    def addAfterContext(self, addAfterContext: bool):
        self.__addAfterContext = addAfterContext

    @property
    def dbl_SetGenContextStatement(self):
        return self.__dbl_SetGenContextStatement

    @dbl_SetGenContextStatement.setter
    def dbl_SetGenContextStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_SetGenContextStatement__dbl_SetGenContextStatement", None)
        self.__dbl_SetGenContextStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Expression227"):
                opp_val = getattr(old_value, "dbl_Expression227", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression227"):
                opp_val = getattr(value, "dbl_Expression227", None)
                setattr(value, "dbl_Expression227", self)

class dbl_Terminate(SimpleStatement):

    pass
class dbl_SetStatement(SimpleStatement):

    pass
class dbl_Wait(SimpleStatement):

    pass
class dbl_ResumeGenStatement(SimpleStatement):

    pass
class dbl_BreakStatement(SimpleStatement):

    pass
class dbl_Return(SimpleStatement):

    pass
class dbl_WaitUntil(SimpleStatement):

    pass
class dbl_Print(SimpleStatement):

    pass
class dbl_Advance(SimpleStatement):

    pass
class dbl_Reactivate(SimpleStatement):

    pass
class dbl_ExpressionStatement(SimpleStatement):

    pass
class dbl_Statement(Construct):

    pass
class ExpandableElement:

    pass
class dbl_TypeAccess(ExpandableElement, ElementAccess):

    pass
class dbl_NamedElement(ExpandableElement):

    def __init__(self, name: str, dbl_NamedElement: "dbl_IdExpr" = None):
        self.name = name
        self.dbl_NamedElement = dbl_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dbl_NamedElement(self):
        return self.__dbl_NamedElement

    @dbl_NamedElement.setter
    def dbl_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_NamedElement__dbl_NamedElement", None)
        self.__dbl_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_IdExpr163"):
                opp_val = getattr(old_value, "dbl_IdExpr163", None)
                if opp_val == self:
                    setattr(old_value, "dbl_IdExpr163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_IdExpr163"):
                opp_val = getattr(value, "dbl_IdExpr163", None)
                setattr(value, "dbl_IdExpr163", self)

class Statement:

    pass
class dbl_ExpandStatement(Statement):

    pass
class dbl_SimpleStatement(Statement):

    pass
class dbl_MappingStatement(Statement):

    pass
class dbl_TestStatement(Statement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dbl_IncludePattern(Statement):

    pass
class dbl_CompositeStatement(Statement):

    pass
class dbl_PotentiallyHiddenIdElements(Statement):

    pass
class dbl_ConsiderIdElements(Statement):

    pass
class dbl_TargetStatement(Statement):

    pass
class dbl_FindContainer(Statement):

    pass
class AbstractVariable:

    pass
class dbl_Constructor:

    pass
class ClassSimilar:

    pass
class dbl_QuotedClassContent(QuotedCode, ClassSimilar):

    pass
class Classifier:

    pass
class dbl_AnnotatableElement(ABC):

    pass
class dbl_Expression(Construct):

    pass
class dbl_Interface(Classifier):

    pass
class dbl_Clazz(Classifier, ClassSimilar):

    def __init__(self, active: bool, dbl_Clazz: "dbl_ClassSimilar" = None, dbl_Clazz69: "dbl_Constructor" = None, dbl_Clazz78: "dbl_ClassAugment" = None, dbl_Clazz71: set["dbl_Expression"] = None):
        self.active = active
        self.dbl_Clazz = dbl_Clazz
        self.dbl_Clazz69 = dbl_Clazz69
        self.dbl_Clazz78 = dbl_Clazz78
        self.dbl_Clazz71 = dbl_Clazz71 if dbl_Clazz71 is not None else set()
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def dbl_Clazz71(self):
        return self.__dbl_Clazz71

    @dbl_Clazz71.setter
    def dbl_Clazz71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Clazz__dbl_Clazz71", None)
        self.__dbl_Clazz71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_Expression72"):
                    opp_val = getattr(item, "dbl_Expression72", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_Expression72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_Expression72"):
                    opp_val = getattr(item, "dbl_Expression72", None)
                    
                    setattr(item, "dbl_Expression72", self)
                    

    @property
    def dbl_Clazz69(self):
        return self.__dbl_Clazz69

    @dbl_Clazz69.setter
    def dbl_Clazz69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Clazz__dbl_Clazz69", None)
        self.__dbl_Clazz69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Constructor"):
                opp_val = getattr(old_value, "dbl_Constructor", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Constructor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Constructor"):
                opp_val = getattr(value, "dbl_Constructor", None)
                setattr(value, "dbl_Constructor", self)

    @property
    def dbl_Clazz78(self):
        return self.__dbl_Clazz78

    @dbl_Clazz78.setter
    def dbl_Clazz78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Clazz__dbl_Clazz78", None)
        self.__dbl_Clazz78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ClassAugment77"):
                opp_val = getattr(old_value, "dbl_ClassAugment77", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ClassAugment77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ClassAugment77"):
                opp_val = getattr(value, "dbl_ClassAugment77", None)
                setattr(value, "dbl_ClassAugment77", self)

    @property
    def dbl_Clazz(self):
        return self.__dbl_Clazz

    @dbl_Clazz.setter
    def dbl_Clazz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Clazz__dbl_Clazz", None)
        self.__dbl_Clazz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ClassSimilar51"):
                opp_val = getattr(old_value, "dbl_ClassSimilar51", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ClassSimilar51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ClassSimilar51"):
                opp_val = getattr(value, "dbl_ClassSimilar51", None)
                setattr(value, "dbl_ClassSimilar51", self)

class ModifierExtensionsContainer:

    pass
class dbl_NativeBinding:

    def __init__(self, targetLanguage: str, targetType: str, dbl_NativeBinding: "dbl_Classifier" = None):
        self.targetLanguage = targetLanguage
        self.targetType = targetType
        self.dbl_NativeBinding = dbl_NativeBinding
        
    @property
    def targetType(self) -> str:
        return self.__targetType

    @targetType.setter
    def targetType(self, targetType: str):
        self.__targetType = targetType

    @property
    def targetLanguage(self) -> str:
        return self.__targetLanguage

    @targetLanguage.setter
    def targetLanguage(self, targetLanguage: str):
        self.__targetLanguage = targetLanguage

    @property
    def dbl_NativeBinding(self):
        return self.__dbl_NativeBinding

    @dbl_NativeBinding.setter
    def dbl_NativeBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_NativeBinding__dbl_NativeBinding", None)
        self.__dbl_NativeBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Classifier44"):
                opp_val = getattr(old_value, "dbl_Classifier44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Classifier44"):
                opp_val = getattr(value, "dbl_Classifier44", None)
                if opp_val is None:
                    setattr(value, "dbl_Classifier44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ReferableRhsType:

    pass
class dbl_Extension:

    pass
class dbl_EmbeddableExtensionsContainer(ABC):

    pass
class dbl_IdResolution:

    def __init__(self, metaModelPlatformURI: str, dbl_IdResolution: "dbl_Module" = None, dbl_IdResolution251: set["dbl_Pattern"] = None):
        self.metaModelPlatformURI = metaModelPlatformURI
        self.dbl_IdResolution = dbl_IdResolution
        self.dbl_IdResolution251 = dbl_IdResolution251 if dbl_IdResolution251 is not None else set()
        
    @property
    def metaModelPlatformURI(self) -> str:
        return self.__metaModelPlatformURI

    @metaModelPlatformURI.setter
    def metaModelPlatformURI(self, metaModelPlatformURI: str):
        self.__metaModelPlatformURI = metaModelPlatformURI

    @property
    def dbl_IdResolution251(self):
        return self.__dbl_IdResolution251

    @dbl_IdResolution251.setter
    def dbl_IdResolution251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_IdResolution__dbl_IdResolution251", None)
        self.__dbl_IdResolution251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_Pattern252"):
                    opp_val = getattr(item, "dbl_Pattern252", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_Pattern252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_Pattern252"):
                    opp_val = getattr(item, "dbl_Pattern252", None)
                    
                    setattr(item, "dbl_Pattern252", self)
                    

    @property
    def dbl_IdResolution(self):
        return self.__dbl_IdResolution

    @dbl_IdResolution.setter
    def dbl_IdResolution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_IdResolution__dbl_IdResolution", None)
        self.__dbl_IdResolution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Module19"):
                opp_val = getattr(old_value, "dbl_Module19", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Module19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Module19"):
                opp_val = getattr(value, "dbl_Module19", None)
                setattr(value, "dbl_Module19", self)

class dbl_VariableAccess(ExpandableElement, ElementAccess):

    pass
class dbl_KeyValuePair:

    pass
class dbl_AnnotationApplication:

    pass
class dbl_Parameter(AbstractVariable):

    pass
class AnnotatableElement:

    pass
class CodeBlock:

    pass
class dbl_StartCodeBlock(CodeBlock):

    pass
class dbl_Mapping(CodeBlock):

    pass
class TypedElement:

    pass
class dbl_CreateObject(TypedElement, L1Expr):

    pass
class dbl_Cast(TypedElement, UnaryOperator):

    pass
class PrimitiveType:

    pass
class dbl_DoubleType(PrimitiveType):

    pass
class dbl_BoolType(PrimitiveType):

    pass
class dbl_IntType(PrimitiveType):

    pass
class dbl_StringType(PrimitiveType):

    pass
class dbl_VoidType(PrimitiveType):

    pass
class Type:

    pass
class dbl_IdExpr(L1Expr):

    pass
class dbl_PrimitiveType(Type):

    pass
class dbl_TypedElement(ABC):

    def __init__(self, isList: bool, dbl_TypedElement: "dbl_PrimitiveType" = None, dbl_TypedElement25: "dbl_IdExpr" = None):
        self.isList = isList
        self.dbl_TypedElement = dbl_TypedElement
        self.dbl_TypedElement25 = dbl_TypedElement25
        
    @property
    def isList(self) -> bool:
        return self.__isList

    @isList.setter
    def isList(self, isList: bool):
        self.__isList = isList

    @property
    def dbl_TypedElement25(self):
        return self.__dbl_TypedElement25

    @dbl_TypedElement25.setter
    def dbl_TypedElement25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_TypedElement__dbl_TypedElement25", None)
        self.__dbl_TypedElement25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_IdExpr"):
                opp_val = getattr(old_value, "dbl_IdExpr", None)
                if opp_val == self:
                    setattr(old_value, "dbl_IdExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_IdExpr"):
                opp_val = getattr(value, "dbl_IdExpr", None)
                setattr(value, "dbl_IdExpr", self)

    @property
    def dbl_TypedElement(self):
        return self.__dbl_TypedElement

    @dbl_TypedElement.setter
    def dbl_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_TypedElement__dbl_TypedElement", None)
        self.__dbl_TypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_PrimitiveType"):
                opp_val = getattr(old_value, "dbl_PrimitiveType", None)
                if opp_val == self:
                    setattr(old_value, "dbl_PrimitiveType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_PrimitiveType"):
                opp_val = getattr(value, "dbl_PrimitiveType", None)
                setattr(value, "dbl_PrimitiveType", self)

class dbl_Type(ABC):

    pass
class dbl_ModifierExtensionsContainer(ABC):

    pass
class NamedExtension:

    pass
class dbl_ClassContentExtension(NamedExtension):

    pass
class dbl_ModuleContentExtension(NamedExtension):

    pass
class dbl_Construct(NamedExtension):

    def __init__(self, concreteSyntax: str):
        self.concreteSyntax = concreteSyntax
        
    @property
    def concreteSyntax(self) -> str:
        return self.__concreteSyntax

    @concreteSyntax.setter
    def concreteSyntax(self, concreteSyntax: str):
        self.__concreteSyntax = concreteSyntax

class dbl_Variable(ModifierExtensionsContainer, AbstractVariable, Statement):

    def __init__(self, control: bool, clazz: bool, dbl_Variable: "dbl_Module" = None, dbl_Variable30: "dbl_Annotation" = None, dbl_Variable46: "dbl_ClassSimilar" = None, dbl_Variable86: "dbl_Expression" = None, dbl_Variable138: "dbl_ForEachStatement" = None):
        self.control = control
        self.clazz = clazz
        self.dbl_Variable = dbl_Variable
        self.dbl_Variable30 = dbl_Variable30
        self.dbl_Variable46 = dbl_Variable46
        self.dbl_Variable86 = dbl_Variable86
        self.dbl_Variable138 = dbl_Variable138
        
    @property
    def control(self) -> bool:
        return self.__control

    @control.setter
    def control(self, control: bool):
        self.__control = control

    @property
    def clazz(self) -> bool:
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: bool):
        self.__clazz = clazz

    @property
    def dbl_Variable(self):
        return self.__dbl_Variable

    @dbl_Variable.setter
    def dbl_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable", None)
        self.__dbl_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Module17"):
                opp_val = getattr(old_value, "dbl_Module17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Module17"):
                opp_val = getattr(value, "dbl_Module17", None)
                if opp_val is None:
                    setattr(value, "dbl_Module17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Variable86(self):
        return self.__dbl_Variable86

    @dbl_Variable86.setter
    def dbl_Variable86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable86", None)
        self.__dbl_Variable86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Expression87"):
                opp_val = getattr(old_value, "dbl_Expression87", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression87"):
                opp_val = getattr(value, "dbl_Expression87", None)
                setattr(value, "dbl_Expression87", self)

    @property
    def dbl_Variable46(self):
        return self.__dbl_Variable46

    @dbl_Variable46.setter
    def dbl_Variable46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable46", None)
        self.__dbl_Variable46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ClassSimilar"):
                opp_val = getattr(old_value, "dbl_ClassSimilar", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ClassSimilar"):
                opp_val = getattr(value, "dbl_ClassSimilar", None)
                if opp_val is None:
                    setattr(value, "dbl_ClassSimilar", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Variable138(self):
        return self.__dbl_Variable138

    @dbl_Variable138.setter
    def dbl_Variable138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable138", None)
        self.__dbl_Variable138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ForEachStatement"):
                opp_val = getattr(old_value, "dbl_ForEachStatement", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ForEachStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ForEachStatement"):
                opp_val = getattr(value, "dbl_ForEachStatement", None)
                setattr(value, "dbl_ForEachStatement", self)

    @property
    def dbl_Variable30(self):
        return self.__dbl_Variable30

    @dbl_Variable30.setter
    def dbl_Variable30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable30", None)
        self.__dbl_Variable30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Annotation29"):
                opp_val = getattr(old_value, "dbl_Annotation29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Annotation29"):
                opp_val = getattr(value, "dbl_Annotation29", None)
                if opp_val is None:
                    setattr(value, "dbl_Annotation29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_ClassAugment(ClassSimilar):

    pass
class EmbeddableExtensionsContainer:

    pass
class dbl_ClassSimilar(EmbeddableExtensionsContainer, ModifierExtensionsContainer):

    pass
class NamedElement:

    pass
class dbl_ExtensionRule(NamedElement):

    pass
class dbl_NamedExtension(Extension, NamedElement):

    pass
class dbl_SimpleAnnotation(NamedElement):

    def __init__(self, value: str, dbl_SimpleAnnotation: "dbl_AnnotatableElement" = None):
        self.value = value
        self.dbl_SimpleAnnotation = dbl_SimpleAnnotation
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def dbl_SimpleAnnotation(self):
        return self.__dbl_SimpleAnnotation

    @dbl_SimpleAnnotation.setter
    def dbl_SimpleAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_SimpleAnnotation__dbl_SimpleAnnotation", None)
        self.__dbl_SimpleAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_AnnotatableElement42"):
                opp_val = getattr(old_value, "dbl_AnnotatableElement42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_AnnotatableElement42"):
                opp_val = getattr(value, "dbl_AnnotatableElement42", None)
                if opp_val is None:
                    setattr(value, "dbl_AnnotatableElement42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_ReferableRhsType(NamedElement):

    pass
class dbl_Classifier(ReferableRhsType, Type, NamedElement):

    pass
class dbl_Pattern(NamedElement):

    def __init__(self, top: bool, dbl_Pattern: "dbl_ReferencePropertyType" = None, dbl_Pattern252: "dbl_IdResolution" = None, dbl_Pattern254: "dbl_Parameter" = None, dbl_Pattern257: "dbl_CodeBlock" = None, dbl_Pattern272: "dbl_IncludePattern" = None):
        self.top = top
        self.dbl_Pattern = dbl_Pattern
        self.dbl_Pattern252 = dbl_Pattern252
        self.dbl_Pattern254 = dbl_Pattern254
        self.dbl_Pattern257 = dbl_Pattern257
        self.dbl_Pattern272 = dbl_Pattern272
        
    @property
    def top(self) -> bool:
        return self.__top

    @top.setter
    def top(self, top: bool):
        self.__top = top

    @property
    def dbl_Pattern272(self):
        return self.__dbl_Pattern272

    @dbl_Pattern272.setter
    def dbl_Pattern272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern272", None)
        self.__dbl_Pattern272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_IncludePattern"):
                opp_val = getattr(old_value, "dbl_IncludePattern", None)
                if opp_val == self:
                    setattr(old_value, "dbl_IncludePattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_IncludePattern"):
                opp_val = getattr(value, "dbl_IncludePattern", None)
                setattr(value, "dbl_IncludePattern", self)

    @property
    def dbl_Pattern252(self):
        return self.__dbl_Pattern252

    @dbl_Pattern252.setter
    def dbl_Pattern252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern252", None)
        self.__dbl_Pattern252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_IdResolution251"):
                opp_val = getattr(old_value, "dbl_IdResolution251", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_IdResolution251"):
                opp_val = getattr(value, "dbl_IdResolution251", None)
                if opp_val is None:
                    setattr(value, "dbl_IdResolution251", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Pattern257(self):
        return self.__dbl_Pattern257

    @dbl_Pattern257.setter
    def dbl_Pattern257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern257", None)
        self.__dbl_Pattern257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_CodeBlock258"):
                opp_val = getattr(old_value, "dbl_CodeBlock258", None)
                if opp_val == self:
                    setattr(old_value, "dbl_CodeBlock258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_CodeBlock258"):
                opp_val = getattr(value, "dbl_CodeBlock258", None)
                setattr(value, "dbl_CodeBlock258", self)

    @property
    def dbl_Pattern(self):
        return self.__dbl_Pattern

    @dbl_Pattern.setter
    def dbl_Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern", None)
        self.__dbl_Pattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ReferencePropertyType"):
                opp_val = getattr(old_value, "dbl_ReferencePropertyType", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ReferencePropertyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ReferencePropertyType"):
                opp_val = getattr(value, "dbl_ReferencePropertyType", None)
                setattr(value, "dbl_ReferencePropertyType", self)

    @property
    def dbl_Pattern254(self):
        return self.__dbl_Pattern254

    @dbl_Pattern254.setter
    def dbl_Pattern254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern254", None)
        self.__dbl_Pattern254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Parameter255"):
                opp_val = getattr(old_value, "dbl_Parameter255", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Parameter255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Parameter255"):
                opp_val = getattr(value, "dbl_Parameter255", None)
                setattr(value, "dbl_Parameter255", self)

class dbl_Annotation(NamedElement):

    pass
class dbl_TsRule(ReferableRhsType, NamedElement):

    def __init__(self, metaClassName: str, dbl_TsRule: "dbl_TextualSyntaxDef" = None, dbl_TsRule185: "dbl_RhsExpression" = None, dbl_TsRule209: "dbl_RuleExpr" = None):
        self.metaClassName = metaClassName
        self.dbl_TsRule = dbl_TsRule
        self.dbl_TsRule185 = dbl_TsRule185
        self.dbl_TsRule209 = dbl_TsRule209
        
    @property
    def metaClassName(self) -> str:
        return self.__metaClassName

    @metaClassName.setter
    def metaClassName(self, metaClassName: str):
        self.__metaClassName = metaClassName

    @property
    def dbl_TsRule(self):
        return self.__dbl_TsRule

    @dbl_TsRule.setter
    def dbl_TsRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_TsRule__dbl_TsRule", None)
        self.__dbl_TsRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_TextualSyntaxDef183"):
                opp_val = getattr(old_value, "dbl_TextualSyntaxDef183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_TextualSyntaxDef183"):
                opp_val = getattr(value, "dbl_TextualSyntaxDef183", None)
                if opp_val is None:
                    setattr(value, "dbl_TextualSyntaxDef183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_TsRule185(self):
        return self.__dbl_TsRule185

    @dbl_TsRule185.setter
    def dbl_TsRule185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_TsRule__dbl_TsRule185", None)
        self.__dbl_TsRule185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_RhsExpression"):
                opp_val = getattr(old_value, "dbl_RhsExpression", None)
                if opp_val == self:
                    setattr(old_value, "dbl_RhsExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_RhsExpression"):
                opp_val = getattr(value, "dbl_RhsExpression", None)
                setattr(value, "dbl_RhsExpression", self)

    @property
    def dbl_TsRule209(self):
        return self.__dbl_TsRule209

    @dbl_TsRule209.setter
    def dbl_TsRule209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_TsRule__dbl_TsRule209", None)
        self.__dbl_TsRule209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_RuleExpr208"):
                opp_val = getattr(old_value, "dbl_RuleExpr208", None)
                if opp_val == self:
                    setattr(old_value, "dbl_RuleExpr208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_RuleExpr208"):
                opp_val = getattr(value, "dbl_RuleExpr208", None)
                setattr(value, "dbl_RuleExpr208", self)

class dbl_Procedure(TypedElement, NamedElement, AnnotatableElement, CodeBlock):

    def __init__(self, clazz: bool, dbl_Procedure: "dbl_Module" = None, dbl_Procedure27: set["dbl_Parameter"] = None, dbl_Procedure49: "dbl_ClassSimilar" = None, dbl_Procedure81: "dbl_Interface" = None):
        self.clazz = clazz
        self.dbl_Procedure = dbl_Procedure
        self.dbl_Procedure27 = dbl_Procedure27 if dbl_Procedure27 is not None else set()
        self.dbl_Procedure49 = dbl_Procedure49
        self.dbl_Procedure81 = dbl_Procedure81
        
    @property
    def clazz(self) -> bool:
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: bool):
        self.__clazz = clazz

    @property
    def dbl_Procedure27(self):
        return self.__dbl_Procedure27

    @dbl_Procedure27.setter
    def dbl_Procedure27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Procedure__dbl_Procedure27", None)
        self.__dbl_Procedure27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_Parameter"):
                    opp_val = getattr(item, "dbl_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_Parameter"):
                    opp_val = getattr(item, "dbl_Parameter", None)
                    
                    setattr(item, "dbl_Parameter", self)
                    

    @property
    def dbl_Procedure(self):
        return self.__dbl_Procedure

    @dbl_Procedure.setter
    def dbl_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Procedure__dbl_Procedure", None)
        self.__dbl_Procedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Module15"):
                opp_val = getattr(old_value, "dbl_Module15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Module15"):
                opp_val = getattr(value, "dbl_Module15", None)
                if opp_val is None:
                    setattr(value, "dbl_Module15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Procedure81(self):
        return self.__dbl_Procedure81

    @dbl_Procedure81.setter
    def dbl_Procedure81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Procedure__dbl_Procedure81", None)
        self.__dbl_Procedure81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Interface80"):
                opp_val = getattr(old_value, "dbl_Interface80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Interface80"):
                opp_val = getattr(value, "dbl_Interface80", None)
                if opp_val is None:
                    setattr(value, "dbl_Interface80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Procedure49(self):
        return self.__dbl_Procedure49

    @dbl_Procedure49.setter
    def dbl_Procedure49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Procedure__dbl_Procedure49", None)
        self.__dbl_Procedure49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ClassSimilar48"):
                opp_val = getattr(old_value, "dbl_ClassSimilar48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ClassSimilar48"):
                opp_val = getattr(value, "dbl_ClassSimilar48", None)
                if opp_val is None:
                    setattr(value, "dbl_ClassSimilar48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_ExtensionDefinition(NamedElement):

    pass
class dbl_AbstractVariable(TypedElement, NamedElement):

    pass
class dbl_PropertyBindingExpr(RhsExpression, NamedElement):

    def __init__(self, operator: str, dbl_PropertyBindingExpr: "dbl_PropertyType" = None):
        self.operator = operator
        self.dbl_PropertyBindingExpr = dbl_PropertyBindingExpr
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dbl_PropertyBindingExpr(self):
        return self.__dbl_PropertyBindingExpr

    @dbl_PropertyBindingExpr.setter
    def dbl_PropertyBindingExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_PropertyBindingExpr__dbl_PropertyBindingExpr", None)
        self.__dbl_PropertyBindingExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_PropertyType"):
                opp_val = getattr(old_value, "dbl_PropertyType", None)
                if opp_val == self:
                    setattr(old_value, "dbl_PropertyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_PropertyType"):
                opp_val = getattr(value, "dbl_PropertyType", None)
                setattr(value, "dbl_PropertyType", self)

class dbl_Module(EmbeddableExtensionsContainer, NamedElement):

    pass
class dbl_Import:

    def __init__(self, file: str, dbl_Import: "dbl_Model" = None, dbl_Import4: "dbl_Model" = None):
        self.file = file
        self.dbl_Import = dbl_Import
        self.dbl_Import4 = dbl_Import4
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def dbl_Import(self):
        return self.__dbl_Import

    @dbl_Import.setter
    def dbl_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Import__dbl_Import", None)
        self.__dbl_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Model"):
                opp_val = getattr(old_value, "dbl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Model"):
                opp_val = getattr(value, "dbl_Model", None)
                if opp_val is None:
                    setattr(value, "dbl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Import4(self):
        return self.__dbl_Import4

    @dbl_Import4.setter
    def dbl_Import4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Import__dbl_Import4", None)
        self.__dbl_Import4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Model5"):
                opp_val = getattr(old_value, "dbl_Model5", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Model5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Model5"):
                opp_val = getattr(value, "dbl_Model5", None)
                setattr(value, "dbl_Model5", self)

class dbl_Model:

    pass
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
class dbl_IntPropertyType(PropertyType):

    pass
class dbl_StringPropertyType(PropertyType):

    pass
class dbl_StructuredPropertyType(PropertyType):

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

class dbl_IdPropertyType(PropertyType):

    pass
class RhsExpression:

    pass
class dbl_RuntimeExpr(RhsExpression):

    pass
class dbl_OptionalExpr(RhsExpression):

    pass
class dbl_AtLeastOneExpr(RhsExpression):

    pass
class dbl_SequenceExpr(RhsExpression):

    pass
class dbl_RuleExpr(RhsExpression):

    pass
class dbl_PropertyType(ABC):

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
class ExtensibleElement:

    pass
class VariableAccess:

    pass
class dbl_MetaAccess(VariableAccess):

    pass
class ElementAccess:

    pass
class dbl_RhsExpression(ABC):

    def __init__(self, dbl_RhsExpression: "dbl_TsRule" = None, dbl_RhsExpression202: "dbl_ArbitraryExpr" = None, dbl_RhsExpression204: "dbl_AlternativeExpr" = None, dbl_RhsExpression207: "dbl_AlternativeExpr" = None, dbl_RhsExpression194: "dbl_SequenceExpr" = None, dbl_RhsExpression196: "dbl_OptionalExpr" = None, dbl_RhsExpression198: "dbl_RuntimeExpr" = None, dbl_RhsExpression200: "dbl_AtLeastOneExpr" = None):
        self.dbl_RhsExpression = dbl_RhsExpression
        self.dbl_RhsExpression202 = dbl_RhsExpression202
        self.dbl_RhsExpression204 = dbl_RhsExpression204
        self.dbl_RhsExpression207 = dbl_RhsExpression207
        self.dbl_RhsExpression194 = dbl_RhsExpression194
        self.dbl_RhsExpression196 = dbl_RhsExpression196
        self.dbl_RhsExpression198 = dbl_RhsExpression198
        self.dbl_RhsExpression200 = dbl_RhsExpression200
        
    @property
    def dbl_RhsExpression207(self):
        return self.__dbl_RhsExpression207

    @dbl_RhsExpression207.setter
    def dbl_RhsExpression207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression207", None)
        self.__dbl_RhsExpression207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_AlternativeExpr206"):
                opp_val = getattr(old_value, "dbl_AlternativeExpr206", None)
                if opp_val == self:
                    setattr(old_value, "dbl_AlternativeExpr206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_AlternativeExpr206"):
                opp_val = getattr(value, "dbl_AlternativeExpr206", None)
                setattr(value, "dbl_AlternativeExpr206", self)

    @property
    def dbl_RhsExpression204(self):
        return self.__dbl_RhsExpression204

    @dbl_RhsExpression204.setter
    def dbl_RhsExpression204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression204", None)
        self.__dbl_RhsExpression204 = value
        
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
    def dbl_RhsExpression202(self):
        return self.__dbl_RhsExpression202

    @dbl_RhsExpression202.setter
    def dbl_RhsExpression202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression202", None)
        self.__dbl_RhsExpression202 = value
        
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
    def dbl_RhsExpression194(self):
        return self.__dbl_RhsExpression194

    @dbl_RhsExpression194.setter
    def dbl_RhsExpression194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression194", None)
        self.__dbl_RhsExpression194 = value
        
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
    def dbl_RhsExpression198(self):
        return self.__dbl_RhsExpression198

    @dbl_RhsExpression198.setter
    def dbl_RhsExpression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression198", None)
        self.__dbl_RhsExpression198 = value
        
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
    def dbl_RhsExpression200(self):
        return self.__dbl_RhsExpression200

    @dbl_RhsExpression200.setter
    def dbl_RhsExpression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_RhsExpression__dbl_RhsExpression200", None)
        self.__dbl_RhsExpression200 = value
        
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
            if hasattr(old_value, "dbl_OptionalExpr"):
                opp_val = getattr(old_value, "dbl_OptionalExpr", None)
                if opp_val == self:
                    setattr(old_value, "dbl_OptionalExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_OptionalExpr"):
                opp_val = getattr(value, "dbl_OptionalExpr", None)
                setattr(value, "dbl_OptionalExpr", self)

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
            if hasattr(old_value, "dbl_TsRule187"):
                opp_val = getattr(old_value, "dbl_TsRule187", None)
                if opp_val == self:
                    setattr(old_value, "dbl_TsRule187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_TsRule187"):
                opp_val = getattr(value, "dbl_TsRule187", None)
                setattr(value, "dbl_TsRule187", self)

    def getSubExpressions(self) -> str:
        # TODO: Implement getSubExpressions method
        pass

class dbl_TextualSyntaxDef:

    pass
class PredefinedId:

    pass
class dbl_SuperLiteral(PredefinedId):

    pass
class dbl_TypeLiteral(PredefinedId):

    pass
class dbl_MetaLiteral(PredefinedId):

    pass
class dbl_SetOp(PredefinedId):

    pass
class dbl_MeLiteral(PredefinedId):

    pass
class dbl_PredefinedId:

    pass
class dbl_DepIdentifiableElement(ABC):

    pass
class SetOp:

    pass
class dbl_IndexOf(SetOp):

    pass
class dbl_LastInSet(SetOp):

    pass
class dbl_Contains(SetOp):

    pass
class dbl_FirstInSet(SetOp):

    pass
class dbl_BeforeInSet(SetOp):

    pass
class dbl_AfterInSet(SetOp):

    pass
class dbl_ObjectAt(SetOp):

    pass
class dbl_SizeOfSet(SetOp):

    pass
class UnaryOperator:

    pass
class dbl_Neg(UnaryOperator):

    pass
class BinaryOperator:

    pass
class dbl_GreaterEqual(BinaryOperator):

    pass
class dbl_Minus(BinaryOperator):

    pass
class dbl_NotEqual(BinaryOperator):

    pass
class dbl_Greater(BinaryOperator):

    pass
class dbl_Div(BinaryOperator):

    pass
class dbl_Plus(BinaryOperator):

    pass
class dbl_LessEqual(BinaryOperator):

    pass
class dbl_Equal(BinaryOperator):

    pass
class dbl_Less(BinaryOperator):

    pass
class dbl_InstanceOf(BinaryOperator):

    pass
class dbl_Or(BinaryOperator):

    pass
class dbl_Mul(BinaryOperator):

    pass
class dbl_Mod(BinaryOperator):

    pass
class dbl_And(BinaryOperator):

    pass
class L1Expr:

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

class dbl_TrueLiteral(L1Expr):

    pass
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
class dbl_TimeLiteral(L1Expr):

    pass
class dbl_NullLiteral(L1Expr):

    pass
class dbl_StringLiteral(L1Expr):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dbl_Not(UnaryOperator):

    pass
class CompositeStatement:

    pass
class dbl_ExpandSection(CompositeStatement):

    pass
class dbl_WhileStatement(CompositeStatement):

    pass
class dbl_IfStatement(CompositeStatement):

    pass
class dbl_ArgumentExpression:

    pass
class SetStatement:

    pass
class dbl_EmptySet(SetStatement):

    pass
class dbl_AddToSet(SetStatement):

    pass
class dbl_RemoveFromSet(SetStatement):

    pass
class Expression:

    pass
class dbl_BinaryOperator(Expression):

    pass
class dbl_UnaryOperator(Expression):

    pass
class dbl_ElementAccess(Expression):

    pass
class dbl_EvalExpr(Expression):

    pass
class dbl_CodeQuoteExpression(Expression):

    pass
class dbl_MetaExpr(Expression):

    pass
class dbl_L1Expr(Expression):

    pass
class dbl_ForEachStatement(CompositeStatement):

    pass
class StatementExpression:

    pass
class dbl_ExpandExpression(StatementExpression, Expression):

    pass
class dbl_ProcedureCall(StatementExpression):

    pass
class ExpressionStatement:

    pass
class dbl_DeprecatedProcedureCallStatement(ExpressionStatement):

    pass
class dbl_StatementExpression:

    pass
class SimpleStatement:

    pass
class dbl_SaveGenStatement(SimpleStatement):

    pass
class dbl_ResumeGenStatement(SimpleStatement):

    pass
class dbl_ResetGenContextStatement(SimpleStatement):

    pass
class dbl_ContinueStatement(SimpleStatement):

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
            if hasattr(old_value, "dbl_Expression229"):
                opp_val = getattr(old_value, "dbl_Expression229", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression229"):
                opp_val = getattr(value, "dbl_Expression229", None)
                setattr(value, "dbl_Expression229", self)

class dbl_BreakStatement(SimpleStatement):

    pass
class dbl_Return(SimpleStatement):

    pass
class dbl_Assignment(SimpleStatement):

    pass
class dbl_ExpressionStatement(SimpleStatement):

    pass
class dbl_SetStatement(SimpleStatement):

    pass
class dbl_Print(SimpleStatement):

    pass
class dbl_Advance(SimpleStatement):

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
            if hasattr(old_value, "dbl_Expression108"):
                opp_val = getattr(old_value, "dbl_Expression108", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression108"):
                opp_val = getattr(value, "dbl_Expression108", None)
                setattr(value, "dbl_Expression108", self)

class dbl_Reactivate(SimpleStatement):

    pass
class dbl_Wait(SimpleStatement):

    pass
class dbl_Yield(SimpleStatement):

    pass
class dbl_Terminate(SimpleStatement):

    pass
class dbl_WaitUntil(SimpleStatement):

    pass
class dbl_Constructor:

    pass
class Construct:

    pass
class dbl_Statement(Construct):

    pass
class dbl_CodeBlock(Construct):

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
            if hasattr(old_value, "dbl_IdExpr164"):
                opp_val = getattr(old_value, "dbl_IdExpr164", None)
                if opp_val == self:
                    setattr(old_value, "dbl_IdExpr164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_IdExpr164"):
                opp_val = getattr(value, "dbl_IdExpr164", None)
                setattr(value, "dbl_IdExpr164", self)

class Statement:

    pass
class dbl_ConsiderIdElements(Statement):

    pass
class dbl_SimpleStatement(Statement):

    pass
class dbl_CompositeStatement(Statement):

    pass
class dbl_TargetStatement(Statement):

    pass
class dbl_MappingStatement(Statement):

    pass
class dbl_IncludePattern(Statement):

    pass
class dbl_FindContainer(Statement):

    pass
class dbl_PotentiallyHiddenIdElements(Statement):

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

class dbl_ExpandStatement(Statement):

    pass
class AbstractVariable:

    pass
class ModifierExtensionsContainer:

    pass
class ClassSimilar:

    pass
class dbl_QuotedClassContent(ClassSimilar, QuotedCode):

    pass
class Classifier:

    pass
class dbl_Interface(Classifier):

    pass
class dbl_Clazz(ClassSimilar, Classifier):

    def __init__(self, active: bool, dbl_Clazz: "dbl_ClassSimilar" = None, dbl_Clazz71: "dbl_Constructor" = None, dbl_Clazz73: set["dbl_Expression"] = None, dbl_Clazz80: "dbl_ClassAugment" = None):
        self.active = active
        self.dbl_Clazz = dbl_Clazz
        self.dbl_Clazz71 = dbl_Clazz71
        self.dbl_Clazz73 = dbl_Clazz73 if dbl_Clazz73 is not None else set()
        self.dbl_Clazz80 = dbl_Clazz80
        
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
        self.__dbl_Clazz71 = value
        
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
    def dbl_Clazz73(self):
        return self.__dbl_Clazz73

    @dbl_Clazz73.setter
    def dbl_Clazz73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Clazz__dbl_Clazz73", None)
        self.__dbl_Clazz73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_Expression74"):
                    opp_val = getattr(item, "dbl_Expression74", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_Expression74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_Expression74"):
                    opp_val = getattr(item, "dbl_Expression74", None)
                    
                    setattr(item, "dbl_Expression74", self)
                    

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
            if hasattr(old_value, "dbl_ClassSimilar53"):
                opp_val = getattr(old_value, "dbl_ClassSimilar53", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ClassSimilar53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ClassSimilar53"):
                opp_val = getattr(value, "dbl_ClassSimilar53", None)
                setattr(value, "dbl_ClassSimilar53", self)

    @property
    def dbl_Clazz80(self):
        return self.__dbl_Clazz80

    @dbl_Clazz80.setter
    def dbl_Clazz80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Clazz__dbl_Clazz80", None)
        self.__dbl_Clazz80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ClassAugment79"):
                opp_val = getattr(old_value, "dbl_ClassAugment79", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ClassAugment79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ClassAugment79"):
                opp_val = getattr(value, "dbl_ClassAugment79", None)
                setattr(value, "dbl_ClassAugment79", self)

class dbl_Parameter(AbstractVariable):

    pass
class AnnotatableElement:

    pass
class CodeBlock:

    pass
class dbl_Mapping(CodeBlock):

    pass
class dbl_StartCodeBlock(CodeBlock):

    pass
class PrimitiveType:

    pass
class dbl_DoubleType(PrimitiveType):

    pass
class dbl_IntType(PrimitiveType):

    pass
class dbl_StringType(PrimitiveType):

    pass
class dbl_BoolType(PrimitiveType):

    pass
class dbl_VoidType(PrimitiveType):

    pass
class Type:

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
            if hasattr(old_value, "dbl_Classifier46"):
                opp_val = getattr(old_value, "dbl_Classifier46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Classifier46"):
                opp_val = getattr(value, "dbl_Classifier46", None)
                if opp_val is None:
                    setattr(value, "dbl_Classifier46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ReferableRhsType:

    pass
class dbl_AnnotatableElement(ABC):

    pass
class dbl_Expression(Construct):

    pass
class dbl_VariableAccess(ExpandableElement, ElementAccess):

    pass
class dbl_KeyValuePair:

    pass
class dbl_AnnotationApplication:

    pass
class dbl_ClassAugment(ClassSimilar):

    pass
class EmbeddableExtensionsContainer:

    pass
class dbl_ClassSimilar(EmbeddableExtensionsContainer, ModifierExtensionsContainer):

    pass
class NamedElement:

    pass
class dbl_PropertyBindingExpr(NamedElement, RhsExpression):

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

class dbl_ExtensionRule(NamedElement):

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
            if hasattr(old_value, "dbl_AnnotatableElement44"):
                opp_val = getattr(old_value, "dbl_AnnotatableElement44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_AnnotatableElement44"):
                opp_val = getattr(value, "dbl_AnnotatableElement44", None)
                if opp_val is None:
                    setattr(value, "dbl_AnnotatableElement44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_NamedExtensible(ExtensibleElement, NamedElement):

    pass
class dbl_Pattern(NamedElement):

    def __init__(self, top: bool, dbl_Pattern: "dbl_ReferencePropertyType" = None, dbl_Pattern274: "dbl_IncludePattern" = None, dbl_Pattern254: "dbl_IdResolution" = None, dbl_Pattern256: "dbl_Parameter" = None, dbl_Pattern259: "dbl_CodeBlock" = None):
        self.top = top
        self.dbl_Pattern = dbl_Pattern
        self.dbl_Pattern274 = dbl_Pattern274
        self.dbl_Pattern254 = dbl_Pattern254
        self.dbl_Pattern256 = dbl_Pattern256
        self.dbl_Pattern259 = dbl_Pattern259
        
    @property
    def top(self) -> bool:
        return self.__top

    @top.setter
    def top(self, top: bool):
        self.__top = top

    @property
    def dbl_Pattern256(self):
        return self.__dbl_Pattern256

    @dbl_Pattern256.setter
    def dbl_Pattern256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern256", None)
        self.__dbl_Pattern256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Parameter257"):
                opp_val = getattr(old_value, "dbl_Parameter257", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Parameter257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Parameter257"):
                opp_val = getattr(value, "dbl_Parameter257", None)
                setattr(value, "dbl_Parameter257", self)

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
            if hasattr(old_value, "dbl_IdResolution253"):
                opp_val = getattr(old_value, "dbl_IdResolution253", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_IdResolution253"):
                opp_val = getattr(value, "dbl_IdResolution253", None)
                if opp_val is None:
                    setattr(value, "dbl_IdResolution253", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Pattern274(self):
        return self.__dbl_Pattern274

    @dbl_Pattern274.setter
    def dbl_Pattern274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern274", None)
        self.__dbl_Pattern274 = value
        
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
    def dbl_Pattern259(self):
        return self.__dbl_Pattern259

    @dbl_Pattern259.setter
    def dbl_Pattern259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern259", None)
        self.__dbl_Pattern259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_CodeBlock260"):
                opp_val = getattr(old_value, "dbl_CodeBlock260", None)
                if opp_val == self:
                    setattr(old_value, "dbl_CodeBlock260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_CodeBlock260"):
                opp_val = getattr(value, "dbl_CodeBlock260", None)
                setattr(value, "dbl_CodeBlock260", self)

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

class dbl_ReferableRhsType(NamedElement):

    pass
class dbl_TsRule(ReferableRhsType, NamedElement):

    def __init__(self, metaClassName: str, dbl_TsRule: "dbl_TextualSyntaxDef" = None, dbl_TsRule187: "dbl_RhsExpression" = None, dbl_TsRule211: "dbl_RuleExpr" = None):
        self.metaClassName = metaClassName
        self.dbl_TsRule = dbl_TsRule
        self.dbl_TsRule187 = dbl_TsRule187
        self.dbl_TsRule211 = dbl_TsRule211
        
    @property
    def metaClassName(self) -> str:
        return self.__metaClassName

    @metaClassName.setter
    def metaClassName(self, metaClassName: str):
        self.__metaClassName = metaClassName

    @property
    def dbl_TsRule187(self):
        return self.__dbl_TsRule187

    @dbl_TsRule187.setter
    def dbl_TsRule187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_TsRule__dbl_TsRule187", None)
        self.__dbl_TsRule187 = value
        
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
    def dbl_TsRule211(self):
        return self.__dbl_TsRule211

    @dbl_TsRule211.setter
    def dbl_TsRule211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_TsRule__dbl_TsRule211", None)
        self.__dbl_TsRule211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_RuleExpr210"):
                opp_val = getattr(old_value, "dbl_RuleExpr210", None)
                if opp_val == self:
                    setattr(old_value, "dbl_RuleExpr210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_RuleExpr210"):
                opp_val = getattr(value, "dbl_RuleExpr210", None)
                setattr(value, "dbl_RuleExpr210", self)

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
            if hasattr(old_value, "dbl_TextualSyntaxDef185"):
                opp_val = getattr(old_value, "dbl_TextualSyntaxDef185", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_TextualSyntaxDef185"):
                opp_val = getattr(value, "dbl_TextualSyntaxDef185", None)
                if opp_val is None:
                    setattr(value, "dbl_TextualSyntaxDef185", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_Classifier(ReferableRhsType, NamedElement, Type):

    pass
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
class TypedElement:

    pass
class dbl_Cast(TypedElement, UnaryOperator):

    pass
class dbl_AbstractVariable(TypedElement, NamedElement):

    pass
class dbl_CreateObject(L1Expr, TypedElement):

    pass
class dbl_IdExpr(L1Expr):

    pass
class dbl_ListDimension(TypedElement):

    def __init__(self, size: int, dbl_ListDimension: "dbl_TypedElement" = None):
        self.size = size
        self.dbl_ListDimension = dbl_ListDimension
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def dbl_ListDimension(self):
        return self.__dbl_ListDimension

    @dbl_ListDimension.setter
    def dbl_ListDimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ListDimension__dbl_ListDimension", None)
        self.__dbl_ListDimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_TypedElement25"):
                opp_val = getattr(old_value, "dbl_TypedElement25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_TypedElement25"):
                opp_val = getattr(value, "dbl_TypedElement25", None)
                if opp_val is None:
                    setattr(value, "dbl_TypedElement25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_PrimitiveType(Type):

    pass
class dbl_TypedElement(ABC):

    def __init__(self, isList: bool, dbl_TypedElement: "dbl_PrimitiveType" = None, dbl_TypedElement25: set["dbl_ListDimension"] = None, dbl_TypedElement27: "dbl_IdExpr" = None):
        self.isList = isList
        self.dbl_TypedElement = dbl_TypedElement
        self.dbl_TypedElement25 = dbl_TypedElement25 if dbl_TypedElement25 is not None else set()
        self.dbl_TypedElement27 = dbl_TypedElement27
        
    @property
    def isList(self) -> bool:
        return self.__isList

    @isList.setter
    def isList(self, isList: bool):
        self.__isList = isList

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

    @property
    def dbl_TypedElement25(self):
        return self.__dbl_TypedElement25

    @dbl_TypedElement25.setter
    def dbl_TypedElement25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_TypedElement__dbl_TypedElement25", None)
        self.__dbl_TypedElement25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_ListDimension"):
                    opp_val = getattr(item, "dbl_ListDimension", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_ListDimension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_ListDimension"):
                    opp_val = getattr(item, "dbl_ListDimension", None)
                    
                    setattr(item, "dbl_ListDimension", self)
                    

    @property
    def dbl_TypedElement27(self):
        return self.__dbl_TypedElement27

    @dbl_TypedElement27.setter
    def dbl_TypedElement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_TypedElement__dbl_TypedElement27", None)
        self.__dbl_TypedElement27 = value
        
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

class dbl_Type(ABC):

    pass
class dbl_ModifierExtensionsContainer(ABC):

    pass
class dbl_ExtensibleElement:

    def __init__(self, objectIsExtensionInstance: bool, dbl_ExtensibleElement: "dbl_EmbeddableExtensionsContainer" = None, dbl_ExtensibleElement22: "dbl_ModifierExtensionsContainer" = None):
        self.objectIsExtensionInstance = objectIsExtensionInstance
        self.dbl_ExtensibleElement = dbl_ExtensibleElement
        self.dbl_ExtensibleElement22 = dbl_ExtensibleElement22
        
    @property
    def objectIsExtensionInstance(self) -> bool:
        return self.__objectIsExtensionInstance

    @objectIsExtensionInstance.setter
    def objectIsExtensionInstance(self, objectIsExtensionInstance: bool):
        self.__objectIsExtensionInstance = objectIsExtensionInstance

    @property
    def dbl_ExtensibleElement(self):
        return self.__dbl_ExtensibleElement

    @dbl_ExtensibleElement.setter
    def dbl_ExtensibleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement", None)
        self.__dbl_ExtensibleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_EmbeddableExtensionsContainer"):
                opp_val = getattr(old_value, "dbl_EmbeddableExtensionsContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_EmbeddableExtensionsContainer"):
                opp_val = getattr(value, "dbl_EmbeddableExtensionsContainer", None)
                if opp_val is None:
                    setattr(value, "dbl_EmbeddableExtensionsContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_ExtensibleElement22(self):
        return self.__dbl_ExtensibleElement22

    @dbl_ExtensibleElement22.setter
    def dbl_ExtensibleElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement22", None)
        self.__dbl_ExtensibleElement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ModifierExtensionsContainer"):
                opp_val = getattr(old_value, "dbl_ModifierExtensionsContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ModifierExtensionsContainer"):
                opp_val = getattr(value, "dbl_ModifierExtensionsContainer", None)
                if opp_val is None:
                    setattr(value, "dbl_ModifierExtensionsContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_EmbeddableExtensionsContainer(ABC):

    pass
class dbl_IdResolution:

    def __init__(self, metaModelPlatformURI: str, dbl_IdResolution: "dbl_Module" = None, dbl_IdResolution253: set["dbl_Pattern"] = None):
        self.metaModelPlatformURI = metaModelPlatformURI
        self.dbl_IdResolution = dbl_IdResolution
        self.dbl_IdResolution253 = dbl_IdResolution253 if dbl_IdResolution253 is not None else set()
        
    @property
    def metaModelPlatformURI(self) -> str:
        return self.__metaModelPlatformURI

    @metaModelPlatformURI.setter
    def metaModelPlatformURI(self, metaModelPlatformURI: str):
        self.__metaModelPlatformURI = metaModelPlatformURI

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

    @property
    def dbl_IdResolution253(self):
        return self.__dbl_IdResolution253

    @dbl_IdResolution253.setter
    def dbl_IdResolution253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_IdResolution__dbl_IdResolution253", None)
        self.__dbl_IdResolution253 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_Pattern254"):
                    opp_val = getattr(item, "dbl_Pattern254", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_Pattern254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_Pattern254"):
                    opp_val = getattr(item, "dbl_Pattern254", None)
                    
                    setattr(item, "dbl_Pattern254", self)
                    

class dbl_Variable(Statement, AbstractVariable, ModifierExtensionsContainer):

    def __init__(self, control: bool, clazz: bool, dbl_Variable: "dbl_Module" = None, dbl_Variable32: "dbl_Annotation" = None, dbl_Variable48: "dbl_ClassSimilar" = None, dbl_Variable88: "dbl_Expression" = None, dbl_Variable139: "dbl_ForEachStatement" = None):
        self.control = control
        self.clazz = clazz
        self.dbl_Variable = dbl_Variable
        self.dbl_Variable32 = dbl_Variable32
        self.dbl_Variable48 = dbl_Variable48
        self.dbl_Variable88 = dbl_Variable88
        self.dbl_Variable139 = dbl_Variable139
        
    @property
    def clazz(self) -> bool:
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: bool):
        self.__clazz = clazz

    @property
    def control(self) -> bool:
        return self.__control

    @control.setter
    def control(self, control: bool):
        self.__control = control

    @property
    def dbl_Variable32(self):
        return self.__dbl_Variable32

    @dbl_Variable32.setter
    def dbl_Variable32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable32", None)
        self.__dbl_Variable32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Annotation31"):
                opp_val = getattr(old_value, "dbl_Annotation31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Annotation31"):
                opp_val = getattr(value, "dbl_Annotation31", None)
                if opp_val is None:
                    setattr(value, "dbl_Annotation31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def dbl_Variable88(self):
        return self.__dbl_Variable88

    @dbl_Variable88.setter
    def dbl_Variable88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable88", None)
        self.__dbl_Variable88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Expression89"):
                opp_val = getattr(old_value, "dbl_Expression89", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression89"):
                opp_val = getattr(value, "dbl_Expression89", None)
                setattr(value, "dbl_Expression89", self)

    @property
    def dbl_Variable48(self):
        return self.__dbl_Variable48

    @dbl_Variable48.setter
    def dbl_Variable48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable48", None)
        self.__dbl_Variable48 = value
        
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
    def dbl_Variable139(self):
        return self.__dbl_Variable139

    @dbl_Variable139.setter
    def dbl_Variable139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable139", None)
        self.__dbl_Variable139 = value
        
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

class dbl_Procedure(NamedElement, TypedElement, AnnotatableElement, CodeBlock):

    def __init__(self, clazz: bool, dbl_Procedure: "dbl_Module" = None, dbl_Procedure29: set["dbl_Parameter"] = None, dbl_Procedure51: "dbl_ClassSimilar" = None, dbl_Procedure83: "dbl_Interface" = None):
        self.clazz = clazz
        self.dbl_Procedure = dbl_Procedure
        self.dbl_Procedure29 = dbl_Procedure29 if dbl_Procedure29 is not None else set()
        self.dbl_Procedure51 = dbl_Procedure51
        self.dbl_Procedure83 = dbl_Procedure83
        
    @property
    def clazz(self) -> bool:
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: bool):
        self.__clazz = clazz

    @property
    def dbl_Procedure51(self):
        return self.__dbl_Procedure51

    @dbl_Procedure51.setter
    def dbl_Procedure51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Procedure__dbl_Procedure51", None)
        self.__dbl_Procedure51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ClassSimilar50"):
                opp_val = getattr(old_value, "dbl_ClassSimilar50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ClassSimilar50"):
                opp_val = getattr(value, "dbl_ClassSimilar50", None)
                if opp_val is None:
                    setattr(value, "dbl_ClassSimilar50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Procedure83(self):
        return self.__dbl_Procedure83

    @dbl_Procedure83.setter
    def dbl_Procedure83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Procedure__dbl_Procedure83", None)
        self.__dbl_Procedure83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Interface82"):
                opp_val = getattr(old_value, "dbl_Interface82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Interface82"):
                opp_val = getattr(value, "dbl_Interface82", None)
                if opp_val is None:
                    setattr(value, "dbl_Interface82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def dbl_Procedure29(self):
        return self.__dbl_Procedure29

    @dbl_Procedure29.setter
    def dbl_Procedure29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Procedure__dbl_Procedure29", None)
        self.__dbl_Procedure29 = value if value is not None else set()
        
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
                    

class dbl_Annotation(NamedElement):

    pass
class dbl_ExtensionDefinition(NamedElement):

    pass
class NamedExtensible:

    pass
class dbl_ClassContentExtension(NamedExtensible):

    pass
class dbl_ModuleContentExtension(NamedExtensible):

    pass
class dbl_Construct(NamedExtensible):

    def __init__(self, concreteSyntax: str):
        self.concreteSyntax = concreteSyntax
        
    @property
    def concreteSyntax(self) -> str:
        return self.__concreteSyntax

    @concreteSyntax.setter
    def concreteSyntax(self, concreteSyntax: str):
        self.__concreteSyntax = concreteSyntax

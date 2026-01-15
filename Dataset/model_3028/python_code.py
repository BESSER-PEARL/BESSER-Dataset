from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BindingExprOpKind(Enum):
    BOOL = "BOOL"
    ASSIGN = "ASSIGN"
    ADD = "ADD"


############################################
# Definition of Classes
############################################

class odemcustom_QuotedCode:

    pass
class odemcustom_ExpandableElement:

    pass
class Module:

    pass
class QuotedCode:

    pass
class odemcustom_QuotedModuleContent(Module, QuotedCode):

    pass
class odemcustom_QuotedStatements(QuotedCode):

    pass
class odemcustom_QuotedExpression(QuotedCode):

    pass
class MappingPart:

    pass
class odemcustom_DynamicMappingPart(MappingPart):

    pass
class odemcustom_FixedMappingPart(MappingPart):

    def __init__(self, code: str):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class odemcustom_MappingPart(ABC):

    pass
class StructuredPropertyType:

    pass
class odemcustom_ReferencePropertyType(StructuredPropertyType):

    def __init__(self, rawReference: bool, odemcustom_ReferencePropertyType: "odemcustom_Pattern" = None):
        self.rawReference = rawReference
        self.odemcustom_ReferencePropertyType = odemcustom_ReferencePropertyType
        
    @property
    def rawReference(self) -> bool:
        return self.__rawReference

    @rawReference.setter
    def rawReference(self, rawReference: bool):
        self.__rawReference = rawReference

    @property
    def odemcustom_ReferencePropertyType(self):
        return self.__odemcustom_ReferencePropertyType

    @odemcustom_ReferencePropertyType.setter
    def odemcustom_ReferencePropertyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_ReferencePropertyType__odemcustom_ReferencePropertyType", None)
        self.__odemcustom_ReferencePropertyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Pattern"):
                opp_val = getattr(old_value, "odemcustom_Pattern", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_Pattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Pattern"):
                opp_val = getattr(value, "odemcustom_Pattern", None)
                setattr(value, "odemcustom_Pattern", self)

class odemcustom_CompositePropertyType(StructuredPropertyType):

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
class odemcustom_StringPropertyType(PropertyType):

    pass
class odemcustom_IntPropertyType(PropertyType):

    pass
class odemcustom_BooleanPropertyType(PropertyType):

    def __init__(self, terminal: str):
        self.terminal = terminal
        
    @property
    def terminal(self) -> str:
        return self.__terminal

    @terminal.setter
    def terminal(self, terminal: str):
        self.__terminal = terminal

class odemcustom_StructuredPropertyType(PropertyType):

    pass
class odemcustom_IdPropertyType(PropertyType):

    pass
class odemcustom_PropertyType(ABC):

    pass
class RhsExpression:

    pass
class odemcustom_ArbitraryExpr(RhsExpression):

    pass
class odemcustom_OptionalExpr(RhsExpression):

    pass
class odemcustom_RuntimeExpr(RhsExpression):

    pass
class odemcustom_AlternativeExpr(RhsExpression):

    pass
class odemcustom_TerminalExpr(RhsExpression):

    def __init__(self, terminal: str):
        self.terminal = terminal
        
    @property
    def terminal(self) -> str:
        return self.__terminal

    @terminal.setter
    def terminal(self, terminal: str):
        self.__terminal = terminal

class odemcustom_AtLeastOneExpr(RhsExpression):

    pass
class odemcustom_SequenceExpr(RhsExpression):

    pass
class odemcustom_RuleExpr(RhsExpression):

    pass
class odemcustom_RhsExpression(ABC):

    def __init__(self, odemcustom_RhsExpression: "odemcustom_TsRule" = None, odemcustom_RhsExpression192: "odemcustom_SequenceExpr" = None, odemcustom_RhsExpression194: "odemcustom_OptionalExpr" = None, odemcustom_RhsExpression198: "odemcustom_AtLeastOneExpr" = None, odemcustom_RhsExpression200: "odemcustom_ArbitraryExpr" = None, odemcustom_RhsExpression202: "odemcustom_AlternativeExpr" = None, odemcustom_RhsExpression205: "odemcustom_AlternativeExpr" = None, odemcustom_RhsExpression196: "odemcustom_RuntimeExpr" = None):
        self.odemcustom_RhsExpression = odemcustom_RhsExpression
        self.odemcustom_RhsExpression192 = odemcustom_RhsExpression192
        self.odemcustom_RhsExpression194 = odemcustom_RhsExpression194
        self.odemcustom_RhsExpression198 = odemcustom_RhsExpression198
        self.odemcustom_RhsExpression200 = odemcustom_RhsExpression200
        self.odemcustom_RhsExpression202 = odemcustom_RhsExpression202
        self.odemcustom_RhsExpression205 = odemcustom_RhsExpression205
        self.odemcustom_RhsExpression196 = odemcustom_RhsExpression196
        
    @property
    def odemcustom_RhsExpression196(self):
        return self.__odemcustom_RhsExpression196

    @odemcustom_RhsExpression196.setter
    def odemcustom_RhsExpression196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_RhsExpression__odemcustom_RhsExpression196", None)
        self.__odemcustom_RhsExpression196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_RuntimeExpr"):
                opp_val = getattr(old_value, "odemcustom_RuntimeExpr", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_RuntimeExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_RuntimeExpr"):
                opp_val = getattr(value, "odemcustom_RuntimeExpr", None)
                setattr(value, "odemcustom_RuntimeExpr", self)

    @property
    def odemcustom_RhsExpression(self):
        return self.__odemcustom_RhsExpression

    @odemcustom_RhsExpression.setter
    def odemcustom_RhsExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_RhsExpression__odemcustom_RhsExpression", None)
        self.__odemcustom_RhsExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_TsRule185"):
                opp_val = getattr(old_value, "odemcustom_TsRule185", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_TsRule185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_TsRule185"):
                opp_val = getattr(value, "odemcustom_TsRule185", None)
                setattr(value, "odemcustom_TsRule185", self)

    @property
    def odemcustom_RhsExpression198(self):
        return self.__odemcustom_RhsExpression198

    @odemcustom_RhsExpression198.setter
    def odemcustom_RhsExpression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_RhsExpression__odemcustom_RhsExpression198", None)
        self.__odemcustom_RhsExpression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_AtLeastOneExpr"):
                opp_val = getattr(old_value, "odemcustom_AtLeastOneExpr", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_AtLeastOneExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_AtLeastOneExpr"):
                opp_val = getattr(value, "odemcustom_AtLeastOneExpr", None)
                setattr(value, "odemcustom_AtLeastOneExpr", self)

    @property
    def odemcustom_RhsExpression200(self):
        return self.__odemcustom_RhsExpression200

    @odemcustom_RhsExpression200.setter
    def odemcustom_RhsExpression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_RhsExpression__odemcustom_RhsExpression200", None)
        self.__odemcustom_RhsExpression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_ArbitraryExpr"):
                opp_val = getattr(old_value, "odemcustom_ArbitraryExpr", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_ArbitraryExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_ArbitraryExpr"):
                opp_val = getattr(value, "odemcustom_ArbitraryExpr", None)
                setattr(value, "odemcustom_ArbitraryExpr", self)

    @property
    def odemcustom_RhsExpression194(self):
        return self.__odemcustom_RhsExpression194

    @odemcustom_RhsExpression194.setter
    def odemcustom_RhsExpression194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_RhsExpression__odemcustom_RhsExpression194", None)
        self.__odemcustom_RhsExpression194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_OptionalExpr"):
                opp_val = getattr(old_value, "odemcustom_OptionalExpr", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_OptionalExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_OptionalExpr"):
                opp_val = getattr(value, "odemcustom_OptionalExpr", None)
                setattr(value, "odemcustom_OptionalExpr", self)

    @property
    def odemcustom_RhsExpression202(self):
        return self.__odemcustom_RhsExpression202

    @odemcustom_RhsExpression202.setter
    def odemcustom_RhsExpression202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_RhsExpression__odemcustom_RhsExpression202", None)
        self.__odemcustom_RhsExpression202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_AlternativeExpr"):
                opp_val = getattr(old_value, "odemcustom_AlternativeExpr", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_AlternativeExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_AlternativeExpr"):
                opp_val = getattr(value, "odemcustom_AlternativeExpr", None)
                setattr(value, "odemcustom_AlternativeExpr", self)

    @property
    def odemcustom_RhsExpression205(self):
        return self.__odemcustom_RhsExpression205

    @odemcustom_RhsExpression205.setter
    def odemcustom_RhsExpression205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_RhsExpression__odemcustom_RhsExpression205", None)
        self.__odemcustom_RhsExpression205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_AlternativeExpr204"):
                opp_val = getattr(old_value, "odemcustom_AlternativeExpr204", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_AlternativeExpr204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_AlternativeExpr204"):
                opp_val = getattr(value, "odemcustom_AlternativeExpr204", None)
                setattr(value, "odemcustom_AlternativeExpr204", self)

    @property
    def odemcustom_RhsExpression192(self):
        return self.__odemcustom_RhsExpression192

    @odemcustom_RhsExpression192.setter
    def odemcustom_RhsExpression192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_RhsExpression__odemcustom_RhsExpression192", None)
        self.__odemcustom_RhsExpression192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_SequenceExpr"):
                opp_val = getattr(old_value, "odemcustom_SequenceExpr", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_SequenceExpr"):
                opp_val = getattr(value, "odemcustom_SequenceExpr", None)
                if opp_val is None:
                    setattr(value, "odemcustom_SequenceExpr", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getSubExpressions(self) -> str:
        # TODO: Implement getSubExpressions method
        pass

class ElementAccess:

    pass
class odemcustom_TextualSyntaxDef:

    pass
class Extension:

    pass
class VariableAccess:

    pass
class odemcustom_MetaAccess(VariableAccess):

    pass
class odemcustom_ArgumentExpression:

    pass
class odemcustom_PredefinedId:

    pass
class odemcustom_DepIdentifiableElement(ABC):

    pass
class PredefinedId:

    pass
class odemcustom_MetaLiteral(PredefinedId):

    pass
class odemcustom_SuperLiteral(PredefinedId):

    pass
class odemcustom_MeLiteral(PredefinedId):

    pass
class SetOp:

    pass
class odemcustom_IndexOf(SetOp):

    pass
class odemcustom_LastInSet(SetOp):

    pass
class odemcustom_BeforeInSet(SetOp):

    pass
class odemcustom_AfterInSet(SetOp):

    pass
class odemcustom_Contains(SetOp):

    pass
class odemcustom_ObjectAt(SetOp):

    pass
class odemcustom_FirstInSet(SetOp):

    pass
class odemcustom_SizeOfSet(SetOp):

    pass
class odemcustom_SetOp(PredefinedId):

    pass
class odemcustom_TypeLiteral(PredefinedId):

    pass
class UnaryOperator:

    pass
class odemcustom_Neg(UnaryOperator):

    pass
class odemcustom_Not(UnaryOperator):

    pass
class Expression:

    pass
class odemcustom_EvalExpr(Expression):

    pass
class odemcustom_TimeLiteral(Expression):

    pass
class odemcustom_ElementAccess(Expression):

    pass
class odemcustom_IntLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class odemcustom_FalseLiteral(Expression):

    pass
class odemcustom_DoubleLiteral(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class odemcustom_CodeQuoteExpression(Expression):

    pass
class odemcustom_MetaExpr(Expression):

    pass
class odemcustom_ActiveLiteral(Expression):

    pass
class odemcustom_TrueLiteral(Expression):

    pass
class odemcustom_NullLiteral(Expression):

    pass
class odemcustom_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class odemcustom_L1Expr(Expression):

    pass
class BinaryOperator:

    pass
class odemcustom_And(BinaryOperator):

    pass
class odemcustom_NotEqual(BinaryOperator):

    pass
class odemcustom_Greater(BinaryOperator):

    pass
class odemcustom_InstanceOf(BinaryOperator):

    pass
class odemcustom_Div(BinaryOperator):

    pass
class odemcustom_Equal(BinaryOperator):

    pass
class odemcustom_GreaterEqual(BinaryOperator):

    pass
class odemcustom_Minus(BinaryOperator):

    pass
class odemcustom_LessEqual(BinaryOperator):

    pass
class odemcustom_Less(BinaryOperator):

    pass
class odemcustom_Mul(BinaryOperator):

    pass
class odemcustom_Mod(BinaryOperator):

    pass
class odemcustom_Or(BinaryOperator):

    pass
class odemcustom_Plus(BinaryOperator):

    pass
class odemcustom_UnaryOperator(Expression):

    pass
class odemcustom_BinaryOperator(Expression):

    pass
class CompositeStatement:

    pass
class odemcustom_ExpandSection(CompositeStatement):

    pass
class odemcustom_WhileStatement(CompositeStatement):

    pass
class odemcustom_ForEachStatement(CompositeStatement):

    pass
class odemcustom_IfStatement(CompositeStatement):

    pass
class SetStatement:

    pass
class odemcustom_EmptySet(SetStatement):

    pass
class odemcustom_AddToSet(SetStatement):

    pass
class odemcustom_RemoveFromSet(SetStatement):

    pass
class StatementExpression:

    pass
class odemcustom_ExpandExpression(Expression, StatementExpression):

    pass
class odemcustom_ProcedureCall(StatementExpression):

    pass
class ExpressionStatement:

    pass
class odemcustom_DeprecatedProcedureCallStatement(ExpressionStatement):

    pass
class odemcustom_StatementExpression:

    pass
class SimpleStatement:

    pass
class odemcustom_Wait(SimpleStatement):

    pass
class odemcustom_Terminate(SimpleStatement):

    pass
class odemcustom_ResetGenContextStatement(SimpleStatement):

    pass
class odemcustom_Advance(SimpleStatement):

    pass
class odemcustom_Reactivate(SimpleStatement):

    pass
class odemcustom_ContinueStatement(SimpleStatement):

    pass
class odemcustom_SetGenContextStatement(SimpleStatement):

    def __init__(self, addAfterContext: bool, odemcustom_SetGenContextStatement: "odemcustom_Expression" = None):
        self.addAfterContext = addAfterContext
        self.odemcustom_SetGenContextStatement = odemcustom_SetGenContextStatement
        
    @property
    def addAfterContext(self) -> bool:
        return self.__addAfterContext

    @addAfterContext.setter
    def addAfterContext(self, addAfterContext: bool):
        self.__addAfterContext = addAfterContext

    @property
    def odemcustom_SetGenContextStatement(self):
        return self.__odemcustom_SetGenContextStatement

    @odemcustom_SetGenContextStatement.setter
    def odemcustom_SetGenContextStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_SetGenContextStatement__odemcustom_SetGenContextStatement", None)
        self.__odemcustom_SetGenContextStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Expression227"):
                opp_val = getattr(old_value, "odemcustom_Expression227", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_Expression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Expression227"):
                opp_val = getattr(value, "odemcustom_Expression227", None)
                setattr(value, "odemcustom_Expression227", self)

class odemcustom_SetStatement(SimpleStatement):

    pass
class odemcustom_WaitUntil(SimpleStatement):

    pass
class odemcustom_Return(SimpleStatement):

    pass
class odemcustom_ResumeGenStatement(SimpleStatement):

    pass
class odemcustom_ActivateObject(SimpleStatement):

    def __init__(self, priority: int, odemcustom_ActivateObject: "odemcustom_Expression" = None):
        self.priority = priority
        self.odemcustom_ActivateObject = odemcustom_ActivateObject
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def odemcustom_ActivateObject(self):
        return self.__odemcustom_ActivateObject

    @odemcustom_ActivateObject.setter
    def odemcustom_ActivateObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_ActivateObject__odemcustom_ActivateObject", None)
        self.__odemcustom_ActivateObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Expression106"):
                opp_val = getattr(old_value, "odemcustom_Expression106", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Expression106"):
                opp_val = getattr(value, "odemcustom_Expression106", None)
                setattr(value, "odemcustom_Expression106", self)

class odemcustom_Print(SimpleStatement):

    pass
class odemcustom_SaveGenStatement(SimpleStatement):

    pass
class odemcustom_BreakStatement(SimpleStatement):

    pass
class odemcustom_ExpressionStatement(SimpleStatement):

    pass
class odemcustom_Assignment(SimpleStatement):

    pass
class ExpandableElement:

    pass
class odemcustom_TypeAccess(ExpandableElement, ElementAccess):

    pass
class odemcustom_NamedElement(ExpandableElement):

    def __init__(self, name: str, odemcustom_NamedElement: "odemcustom_IdExpr" = None):
        self.name = name
        self.odemcustom_NamedElement = odemcustom_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def odemcustom_NamedElement(self):
        return self.__odemcustom_NamedElement

    @odemcustom_NamedElement.setter
    def odemcustom_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_NamedElement__odemcustom_NamedElement", None)
        self.__odemcustom_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_IdExpr163"):
                opp_val = getattr(old_value, "odemcustom_IdExpr163", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_IdExpr163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_IdExpr163"):
                opp_val = getattr(value, "odemcustom_IdExpr163", None)
                setattr(value, "odemcustom_IdExpr163", self)

class Statement:

    pass
class odemcustom_ConsiderIdElements(Statement):

    pass
class odemcustom_TestStatement(Statement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class odemcustom_ExpandStatement(Statement):

    pass
class odemcustom_CompositeStatement(Statement):

    pass
class odemcustom_TargetStatement(Statement):

    pass
class odemcustom_SimpleStatement(Statement):

    pass
class odemcustom_MappingStatement(Statement):

    pass
class odemcustom_IncludePattern(Statement):

    pass
class odemcustom_PotentiallyHiddenIdElements(Statement):

    pass
class odemcustom_FindContainer(Statement):

    pass
class AbstractVariable:

    pass
class Construct:

    pass
class odemcustom_Statement(Construct):

    pass
class odemcustom_CodeBlock(Construct):

    pass
class odemcustom_Constructor:

    pass
class ClassSimilar:

    pass
class odemcustom_QuotedClassContent(ClassSimilar, QuotedCode):

    pass
class Classifier:

    pass
class odemcustom_Interface(Classifier):

    pass
class ModifierExtensionsContainer:

    pass
class odemcustom_NativeBinding:

    def __init__(self, targetLanguage: str, targetType: str, odemcustom_NativeBinding: "odemcustom_Classifier" = None):
        self.targetLanguage = targetLanguage
        self.targetType = targetType
        self.odemcustom_NativeBinding = odemcustom_NativeBinding
        
    @property
    def targetLanguage(self) -> str:
        return self.__targetLanguage

    @targetLanguage.setter
    def targetLanguage(self, targetLanguage: str):
        self.__targetLanguage = targetLanguage

    @property
    def targetType(self) -> str:
        return self.__targetType

    @targetType.setter
    def targetType(self, targetType: str):
        self.__targetType = targetType

    @property
    def odemcustom_NativeBinding(self):
        return self.__odemcustom_NativeBinding

    @odemcustom_NativeBinding.setter
    def odemcustom_NativeBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_NativeBinding__odemcustom_NativeBinding", None)
        self.__odemcustom_NativeBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Classifier44"):
                opp_val = getattr(old_value, "odemcustom_Classifier44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Classifier44"):
                opp_val = getattr(value, "odemcustom_Classifier44", None)
                if opp_val is None:
                    setattr(value, "odemcustom_Classifier44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ReferableRhsType:

    pass
class odemcustom_Clazz(Classifier, ClassSimilar):

    def __init__(self, active: bool, odemcustom_Clazz: "odemcustom_ClassSimilar" = None, odemcustom_Clazz78: "odemcustom_ClassAugment" = None, odemcustom_Clazz69: "odemcustom_Constructor" = None, odemcustom_Clazz71: set["odemcustom_Expression"] = None):
        self.active = active
        self.odemcustom_Clazz = odemcustom_Clazz
        self.odemcustom_Clazz78 = odemcustom_Clazz78
        self.odemcustom_Clazz69 = odemcustom_Clazz69
        self.odemcustom_Clazz71 = odemcustom_Clazz71 if odemcustom_Clazz71 is not None else set()
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def odemcustom_Clazz78(self):
        return self.__odemcustom_Clazz78

    @odemcustom_Clazz78.setter
    def odemcustom_Clazz78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Clazz__odemcustom_Clazz78", None)
        self.__odemcustom_Clazz78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_ClassAugment77"):
                opp_val = getattr(old_value, "odemcustom_ClassAugment77", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_ClassAugment77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_ClassAugment77"):
                opp_val = getattr(value, "odemcustom_ClassAugment77", None)
                setattr(value, "odemcustom_ClassAugment77", self)

    @property
    def odemcustom_Clazz(self):
        return self.__odemcustom_Clazz

    @odemcustom_Clazz.setter
    def odemcustom_Clazz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Clazz__odemcustom_Clazz", None)
        self.__odemcustom_Clazz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_ClassSimilar51"):
                opp_val = getattr(old_value, "odemcustom_ClassSimilar51", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_ClassSimilar51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_ClassSimilar51"):
                opp_val = getattr(value, "odemcustom_ClassSimilar51", None)
                setattr(value, "odemcustom_ClassSimilar51", self)

    @property
    def odemcustom_Clazz71(self):
        return self.__odemcustom_Clazz71

    @odemcustom_Clazz71.setter
    def odemcustom_Clazz71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Clazz__odemcustom_Clazz71", None)
        self.__odemcustom_Clazz71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "odemcustom_Expression72"):
                    opp_val = getattr(item, "odemcustom_Expression72", None)
                    
                    if opp_val == self:
                        setattr(item, "odemcustom_Expression72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "odemcustom_Expression72"):
                    opp_val = getattr(item, "odemcustom_Expression72", None)
                    
                    setattr(item, "odemcustom_Expression72", self)
                    

    @property
    def odemcustom_Clazz69(self):
        return self.__odemcustom_Clazz69

    @odemcustom_Clazz69.setter
    def odemcustom_Clazz69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Clazz__odemcustom_Clazz69", None)
        self.__odemcustom_Clazz69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Constructor"):
                opp_val = getattr(old_value, "odemcustom_Constructor", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_Constructor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Constructor"):
                opp_val = getattr(value, "odemcustom_Constructor", None)
                setattr(value, "odemcustom_Constructor", self)

class odemcustom_VariableAccess(ExpandableElement, ElementAccess):

    pass
class odemcustom_KeyValuePair:

    pass
class odemcustom_AnnotationApplication:

    pass
class odemcustom_Parameter(AbstractVariable):

    pass
class AnnotatableElement:

    pass
class CodeBlock:

    pass
class odemcustom_StartCodeBlock(CodeBlock):

    pass
class odemcustom_Mapping(CodeBlock):

    pass
class TypedElement:

    pass
class odemcustom_Cast(TypedElement, UnaryOperator):

    pass
class odemcustom_CreateObject(TypedElement, Expression):

    pass
class odemcustom_AnnotatableElement(ABC):

    pass
class odemcustom_Expression(Construct):

    pass
class PrimitiveType:

    pass
class odemcustom_VoidType(PrimitiveType):

    pass
class Type:

    pass
class odemcustom_IdExpr(Expression):

    pass
class odemcustom_PrimitiveType(Type):

    pass
class odemcustom_TypedElement(ABC):

    def __init__(self, isList: bool, odemcustom_TypedElement: "odemcustom_PrimitiveType" = None, odemcustom_TypedElement25: "odemcustom_IdExpr" = None):
        self.isList = isList
        self.odemcustom_TypedElement = odemcustom_TypedElement
        self.odemcustom_TypedElement25 = odemcustom_TypedElement25
        
    @property
    def isList(self) -> bool:
        return self.__isList

    @isList.setter
    def isList(self, isList: bool):
        self.__isList = isList

    @property
    def odemcustom_TypedElement25(self):
        return self.__odemcustom_TypedElement25

    @odemcustom_TypedElement25.setter
    def odemcustom_TypedElement25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_TypedElement__odemcustom_TypedElement25", None)
        self.__odemcustom_TypedElement25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_IdExpr"):
                opp_val = getattr(old_value, "odemcustom_IdExpr", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_IdExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_IdExpr"):
                opp_val = getattr(value, "odemcustom_IdExpr", None)
                setattr(value, "odemcustom_IdExpr", self)

    @property
    def odemcustom_TypedElement(self):
        return self.__odemcustom_TypedElement

    @odemcustom_TypedElement.setter
    def odemcustom_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_TypedElement__odemcustom_TypedElement", None)
        self.__odemcustom_TypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_PrimitiveType"):
                opp_val = getattr(old_value, "odemcustom_PrimitiveType", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_PrimitiveType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_PrimitiveType"):
                opp_val = getattr(value, "odemcustom_PrimitiveType", None)
                setattr(value, "odemcustom_PrimitiveType", self)

class odemcustom_Type(ABC):

    pass
class odemcustom_ModifierExtensionsContainer(ABC):

    pass
class odemcustom_Extension:

    pass
class odemcustom_EmbeddableExtensionsContainer(ABC):

    pass
class odemcustom_IdResolution:

    def __init__(self, metaModelPlatformURI: str, odemcustom_IdResolution: "odemcustom_Module" = None, odemcustom_IdResolution251: set["odemcustom_Pattern"] = None):
        self.metaModelPlatformURI = metaModelPlatformURI
        self.odemcustom_IdResolution = odemcustom_IdResolution
        self.odemcustom_IdResolution251 = odemcustom_IdResolution251 if odemcustom_IdResolution251 is not None else set()
        
    @property
    def metaModelPlatformURI(self) -> str:
        return self.__metaModelPlatformURI

    @metaModelPlatformURI.setter
    def metaModelPlatformURI(self, metaModelPlatformURI: str):
        self.__metaModelPlatformURI = metaModelPlatformURI

    @property
    def odemcustom_IdResolution(self):
        return self.__odemcustom_IdResolution

    @odemcustom_IdResolution.setter
    def odemcustom_IdResolution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_IdResolution__odemcustom_IdResolution", None)
        self.__odemcustom_IdResolution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Module19"):
                opp_val = getattr(old_value, "odemcustom_Module19", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_Module19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Module19"):
                opp_val = getattr(value, "odemcustom_Module19", None)
                setattr(value, "odemcustom_Module19", self)

    @property
    def odemcustom_IdResolution251(self):
        return self.__odemcustom_IdResolution251

    @odemcustom_IdResolution251.setter
    def odemcustom_IdResolution251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_IdResolution__odemcustom_IdResolution251", None)
        self.__odemcustom_IdResolution251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "odemcustom_Pattern252"):
                    opp_val = getattr(item, "odemcustom_Pattern252", None)
                    
                    if opp_val == self:
                        setattr(item, "odemcustom_Pattern252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "odemcustom_Pattern252"):
                    opp_val = getattr(item, "odemcustom_Pattern252", None)
                    
                    setattr(item, "odemcustom_Pattern252", self)
                    

class odemcustom_StringType(PrimitiveType):

    pass
class odemcustom_DoubleType(PrimitiveType):

    pass
class odemcustom_BoolType(PrimitiveType):

    pass
class odemcustom_IntType(PrimitiveType):

    pass
class odemcustom_ClassAugment(ClassSimilar):

    pass
class EmbeddableExtensionsContainer:

    pass
class odemcustom_ClassSimilar(EmbeddableExtensionsContainer, ModifierExtensionsContainer):

    pass
class NamedElement:

    pass
class odemcustom_NamedExtension(Extension, NamedElement):

    pass
class odemcustom_PropertyBindingExpr(NamedElement, RhsExpression):

    def __init__(self, operator: str, odemcustom_PropertyBindingExpr: "odemcustom_PropertyType" = None):
        self.operator = operator
        self.odemcustom_PropertyBindingExpr = odemcustom_PropertyBindingExpr
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def odemcustom_PropertyBindingExpr(self):
        return self.__odemcustom_PropertyBindingExpr

    @odemcustom_PropertyBindingExpr.setter
    def odemcustom_PropertyBindingExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_PropertyBindingExpr__odemcustom_PropertyBindingExpr", None)
        self.__odemcustom_PropertyBindingExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_PropertyType"):
                opp_val = getattr(old_value, "odemcustom_PropertyType", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_PropertyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_PropertyType"):
                opp_val = getattr(value, "odemcustom_PropertyType", None)
                setattr(value, "odemcustom_PropertyType", self)

class odemcustom_Classifier(NamedElement, ReferableRhsType, Type):

    pass
class odemcustom_ReferableRhsType(NamedElement):

    pass
class odemcustom_Pattern(NamedElement):

    def __init__(self, top: bool, odemcustom_Pattern: "odemcustom_ReferencePropertyType" = None, odemcustom_Pattern252: "odemcustom_IdResolution" = None, odemcustom_Pattern254: "odemcustom_Parameter" = None, odemcustom_Pattern257: "odemcustom_CodeBlock" = None, odemcustom_Pattern272: "odemcustom_IncludePattern" = None):
        self.top = top
        self.odemcustom_Pattern = odemcustom_Pattern
        self.odemcustom_Pattern252 = odemcustom_Pattern252
        self.odemcustom_Pattern254 = odemcustom_Pattern254
        self.odemcustom_Pattern257 = odemcustom_Pattern257
        self.odemcustom_Pattern272 = odemcustom_Pattern272
        
    @property
    def top(self) -> bool:
        return self.__top

    @top.setter
    def top(self, top: bool):
        self.__top = top

    @property
    def odemcustom_Pattern(self):
        return self.__odemcustom_Pattern

    @odemcustom_Pattern.setter
    def odemcustom_Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Pattern__odemcustom_Pattern", None)
        self.__odemcustom_Pattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_ReferencePropertyType"):
                opp_val = getattr(old_value, "odemcustom_ReferencePropertyType", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_ReferencePropertyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_ReferencePropertyType"):
                opp_val = getattr(value, "odemcustom_ReferencePropertyType", None)
                setattr(value, "odemcustom_ReferencePropertyType", self)

    @property
    def odemcustom_Pattern272(self):
        return self.__odemcustom_Pattern272

    @odemcustom_Pattern272.setter
    def odemcustom_Pattern272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Pattern__odemcustom_Pattern272", None)
        self.__odemcustom_Pattern272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_IncludePattern"):
                opp_val = getattr(old_value, "odemcustom_IncludePattern", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_IncludePattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_IncludePattern"):
                opp_val = getattr(value, "odemcustom_IncludePattern", None)
                setattr(value, "odemcustom_IncludePattern", self)

    @property
    def odemcustom_Pattern257(self):
        return self.__odemcustom_Pattern257

    @odemcustom_Pattern257.setter
    def odemcustom_Pattern257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Pattern__odemcustom_Pattern257", None)
        self.__odemcustom_Pattern257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_CodeBlock258"):
                opp_val = getattr(old_value, "odemcustom_CodeBlock258", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_CodeBlock258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_CodeBlock258"):
                opp_val = getattr(value, "odemcustom_CodeBlock258", None)
                setattr(value, "odemcustom_CodeBlock258", self)

    @property
    def odemcustom_Pattern254(self):
        return self.__odemcustom_Pattern254

    @odemcustom_Pattern254.setter
    def odemcustom_Pattern254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Pattern__odemcustom_Pattern254", None)
        self.__odemcustom_Pattern254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Parameter255"):
                opp_val = getattr(old_value, "odemcustom_Parameter255", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_Parameter255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Parameter255"):
                opp_val = getattr(value, "odemcustom_Parameter255", None)
                setattr(value, "odemcustom_Parameter255", self)

    @property
    def odemcustom_Pattern252(self):
        return self.__odemcustom_Pattern252

    @odemcustom_Pattern252.setter
    def odemcustom_Pattern252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Pattern__odemcustom_Pattern252", None)
        self.__odemcustom_Pattern252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_IdResolution251"):
                opp_val = getattr(old_value, "odemcustom_IdResolution251", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_IdResolution251"):
                opp_val = getattr(value, "odemcustom_IdResolution251", None)
                if opp_val is None:
                    setattr(value, "odemcustom_IdResolution251", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class odemcustom_ExtensionDefinition(NamedElement):

    pass
class odemcustom_AbstractVariable(NamedElement, TypedElement):

    pass
class odemcustom_TsRule(NamedElement, ReferableRhsType):

    def __init__(self, metaClassName: str, odemcustom_TsRule185: "odemcustom_RhsExpression" = None, odemcustom_TsRule: "odemcustom_TextualSyntaxDef" = None, odemcustom_TsRule209: "odemcustom_RuleExpr" = None):
        self.metaClassName = metaClassName
        self.odemcustom_TsRule185 = odemcustom_TsRule185
        self.odemcustom_TsRule = odemcustom_TsRule
        self.odemcustom_TsRule209 = odemcustom_TsRule209
        
    @property
    def metaClassName(self) -> str:
        return self.__metaClassName

    @metaClassName.setter
    def metaClassName(self, metaClassName: str):
        self.__metaClassName = metaClassName

    @property
    def odemcustom_TsRule185(self):
        return self.__odemcustom_TsRule185

    @odemcustom_TsRule185.setter
    def odemcustom_TsRule185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_TsRule__odemcustom_TsRule185", None)
        self.__odemcustom_TsRule185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_RhsExpression"):
                opp_val = getattr(old_value, "odemcustom_RhsExpression", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_RhsExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_RhsExpression"):
                opp_val = getattr(value, "odemcustom_RhsExpression", None)
                setattr(value, "odemcustom_RhsExpression", self)

    @property
    def odemcustom_TsRule(self):
        return self.__odemcustom_TsRule

    @odemcustom_TsRule.setter
    def odemcustom_TsRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_TsRule__odemcustom_TsRule", None)
        self.__odemcustom_TsRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_TextualSyntaxDef183"):
                opp_val = getattr(old_value, "odemcustom_TextualSyntaxDef183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_TextualSyntaxDef183"):
                opp_val = getattr(value, "odemcustom_TextualSyntaxDef183", None)
                if opp_val is None:
                    setattr(value, "odemcustom_TextualSyntaxDef183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def odemcustom_TsRule209(self):
        return self.__odemcustom_TsRule209

    @odemcustom_TsRule209.setter
    def odemcustom_TsRule209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_TsRule__odemcustom_TsRule209", None)
        self.__odemcustom_TsRule209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_RuleExpr208"):
                opp_val = getattr(old_value, "odemcustom_RuleExpr208", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_RuleExpr208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_RuleExpr208"):
                opp_val = getattr(value, "odemcustom_RuleExpr208", None)
                setattr(value, "odemcustom_RuleExpr208", self)

class odemcustom_ExtensionRule(NamedElement):

    pass
class odemcustom_SimpleAnnotation(NamedElement):

    def __init__(self, value: str, odemcustom_SimpleAnnotation: "odemcustom_AnnotatableElement" = None):
        self.value = value
        self.odemcustom_SimpleAnnotation = odemcustom_SimpleAnnotation
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def odemcustom_SimpleAnnotation(self):
        return self.__odemcustom_SimpleAnnotation

    @odemcustom_SimpleAnnotation.setter
    def odemcustom_SimpleAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_SimpleAnnotation__odemcustom_SimpleAnnotation", None)
        self.__odemcustom_SimpleAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_AnnotatableElement42"):
                opp_val = getattr(old_value, "odemcustom_AnnotatableElement42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_AnnotatableElement42"):
                opp_val = getattr(value, "odemcustom_AnnotatableElement42", None)
                if opp_val is None:
                    setattr(value, "odemcustom_AnnotatableElement42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class odemcustom_Annotation(NamedElement):

    pass
class odemcustom_Module(EmbeddableExtensionsContainer, NamedElement):

    pass
class odemcustom_Variable(Statement, ModifierExtensionsContainer, AbstractVariable):

    def __init__(self, control: bool, clazz: bool, odemcustom_Variable: "odemcustom_Module" = None, odemcustom_Variable30: "odemcustom_Annotation" = None, odemcustom_Variable46: "odemcustom_ClassSimilar" = None, odemcustom_Variable86: "odemcustom_Expression" = None, odemcustom_Variable138: "odemcustom_ForEachStatement" = None):
        self.control = control
        self.clazz = clazz
        self.odemcustom_Variable = odemcustom_Variable
        self.odemcustom_Variable30 = odemcustom_Variable30
        self.odemcustom_Variable46 = odemcustom_Variable46
        self.odemcustom_Variable86 = odemcustom_Variable86
        self.odemcustom_Variable138 = odemcustom_Variable138
        
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
    def odemcustom_Variable46(self):
        return self.__odemcustom_Variable46

    @odemcustom_Variable46.setter
    def odemcustom_Variable46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Variable__odemcustom_Variable46", None)
        self.__odemcustom_Variable46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_ClassSimilar"):
                opp_val = getattr(old_value, "odemcustom_ClassSimilar", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_ClassSimilar"):
                opp_val = getattr(value, "odemcustom_ClassSimilar", None)
                if opp_val is None:
                    setattr(value, "odemcustom_ClassSimilar", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def odemcustom_Variable86(self):
        return self.__odemcustom_Variable86

    @odemcustom_Variable86.setter
    def odemcustom_Variable86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Variable__odemcustom_Variable86", None)
        self.__odemcustom_Variable86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Expression87"):
                opp_val = getattr(old_value, "odemcustom_Expression87", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_Expression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Expression87"):
                opp_val = getattr(value, "odemcustom_Expression87", None)
                setattr(value, "odemcustom_Expression87", self)

    @property
    def odemcustom_Variable138(self):
        return self.__odemcustom_Variable138

    @odemcustom_Variable138.setter
    def odemcustom_Variable138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Variable__odemcustom_Variable138", None)
        self.__odemcustom_Variable138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_ForEachStatement"):
                opp_val = getattr(old_value, "odemcustom_ForEachStatement", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_ForEachStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_ForEachStatement"):
                opp_val = getattr(value, "odemcustom_ForEachStatement", None)
                setattr(value, "odemcustom_ForEachStatement", self)

    @property
    def odemcustom_Variable(self):
        return self.__odemcustom_Variable

    @odemcustom_Variable.setter
    def odemcustom_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Variable__odemcustom_Variable", None)
        self.__odemcustom_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Module17"):
                opp_val = getattr(old_value, "odemcustom_Module17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Module17"):
                opp_val = getattr(value, "odemcustom_Module17", None)
                if opp_val is None:
                    setattr(value, "odemcustom_Module17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def odemcustom_Variable30(self):
        return self.__odemcustom_Variable30

    @odemcustom_Variable30.setter
    def odemcustom_Variable30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Variable__odemcustom_Variable30", None)
        self.__odemcustom_Variable30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Annotation29"):
                opp_val = getattr(old_value, "odemcustom_Annotation29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Annotation29"):
                opp_val = getattr(value, "odemcustom_Annotation29", None)
                if opp_val is None:
                    setattr(value, "odemcustom_Annotation29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class odemcustom_Procedure(CodeBlock, AnnotatableElement, NamedElement, TypedElement):

    def __init__(self, clazz: bool, odemcustom_Procedure: "odemcustom_Module" = None, odemcustom_Procedure27: set["odemcustom_Parameter"] = None, odemcustom_Procedure49: "odemcustom_ClassSimilar" = None, odemcustom_Procedure81: "odemcustom_Interface" = None):
        self.clazz = clazz
        self.odemcustom_Procedure = odemcustom_Procedure
        self.odemcustom_Procedure27 = odemcustom_Procedure27 if odemcustom_Procedure27 is not None else set()
        self.odemcustom_Procedure49 = odemcustom_Procedure49
        self.odemcustom_Procedure81 = odemcustom_Procedure81
        
    @property
    def clazz(self) -> bool:
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: bool):
        self.__clazz = clazz

    @property
    def odemcustom_Procedure27(self):
        return self.__odemcustom_Procedure27

    @odemcustom_Procedure27.setter
    def odemcustom_Procedure27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Procedure__odemcustom_Procedure27", None)
        self.__odemcustom_Procedure27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "odemcustom_Parameter"):
                    opp_val = getattr(item, "odemcustom_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "odemcustom_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "odemcustom_Parameter"):
                    opp_val = getattr(item, "odemcustom_Parameter", None)
                    
                    setattr(item, "odemcustom_Parameter", self)
                    

    @property
    def odemcustom_Procedure49(self):
        return self.__odemcustom_Procedure49

    @odemcustom_Procedure49.setter
    def odemcustom_Procedure49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Procedure__odemcustom_Procedure49", None)
        self.__odemcustom_Procedure49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_ClassSimilar48"):
                opp_val = getattr(old_value, "odemcustom_ClassSimilar48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_ClassSimilar48"):
                opp_val = getattr(value, "odemcustom_ClassSimilar48", None)
                if opp_val is None:
                    setattr(value, "odemcustom_ClassSimilar48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def odemcustom_Procedure(self):
        return self.__odemcustom_Procedure

    @odemcustom_Procedure.setter
    def odemcustom_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Procedure__odemcustom_Procedure", None)
        self.__odemcustom_Procedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Module15"):
                opp_val = getattr(old_value, "odemcustom_Module15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Module15"):
                opp_val = getattr(value, "odemcustom_Module15", None)
                if opp_val is None:
                    setattr(value, "odemcustom_Module15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def odemcustom_Procedure81(self):
        return self.__odemcustom_Procedure81

    @odemcustom_Procedure81.setter
    def odemcustom_Procedure81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Procedure__odemcustom_Procedure81", None)
        self.__odemcustom_Procedure81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Interface80"):
                opp_val = getattr(old_value, "odemcustom_Interface80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Interface80"):
                opp_val = getattr(value, "odemcustom_Interface80", None)
                if opp_val is None:
                    setattr(value, "odemcustom_Interface80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedExtension:

    pass
class odemcustom_ClassContentExtension(NamedExtension):

    pass
class odemcustom_ModuleContentExtension(NamedExtension):

    pass
class odemcustom_Construct(NamedExtension):

    def __init__(self, concreteSyntax: str):
        self.concreteSyntax = concreteSyntax
        
    @property
    def concreteSyntax(self) -> str:
        return self.__concreteSyntax

    @concreteSyntax.setter
    def concreteSyntax(self, concreteSyntax: str):
        self.__concreteSyntax = concreteSyntax

class odemcustom_Import:

    def __init__(self, file: str, odemcustom_Import: "odemcustom_Model" = None, odemcustom_Import4: "odemcustom_Model" = None):
        self.file = file
        self.odemcustom_Import = odemcustom_Import
        self.odemcustom_Import4 = odemcustom_Import4
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def odemcustom_Import(self):
        return self.__odemcustom_Import

    @odemcustom_Import.setter
    def odemcustom_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Import__odemcustom_Import", None)
        self.__odemcustom_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Model"):
                opp_val = getattr(old_value, "odemcustom_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Model"):
                opp_val = getattr(value, "odemcustom_Model", None)
                if opp_val is None:
                    setattr(value, "odemcustom_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def odemcustom_Import4(self):
        return self.__odemcustom_Import4

    @odemcustom_Import4.setter
    def odemcustom_Import4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_odemcustom_Import__odemcustom_Import4", None)
        self.__odemcustom_Import4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "odemcustom_Model5"):
                opp_val = getattr(old_value, "odemcustom_Model5", None)
                if opp_val == self:
                    setattr(old_value, "odemcustom_Model5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "odemcustom_Model5"):
                opp_val = getattr(value, "odemcustom_Model5", None)
                setattr(value, "odemcustom_Model5", self)

class odemcustom_Model:

    pass
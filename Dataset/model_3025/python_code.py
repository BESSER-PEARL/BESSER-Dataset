from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Module:

    pass
class Class:

    pass
class QuotedCode:

    pass
class dbl_QuotedClassContent(Class, QuotedCode):

    pass
class dbl_QuotedModuleContent(QuotedCode, Module):

    pass
class dbl_QuotedStatements(QuotedCode):

    pass
class dbl_QuotedExpression(QuotedCode):

    pass
class dbl_QuotedCode:

    pass
class ExpansionPart:

    pass
class dbl_ExpandTextPart(ExpansionPart):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class dbl_ExpansionPart(ABC):

    pass
class dbl_ExpandVariablePart(ExpansionPart):

    pass
class dbl_PropertyType(ABC):

    pass
class StructuredPropertyType:

    pass
class dbl_ReferencePropertyType(StructuredPropertyType):

    def __init__(self, rawReference: bool):
        self.rawReference = rawReference
        
    @property
    def rawReference(self) -> bool:
        return self.__rawReference

    @rawReference.setter
    def rawReference(self, rawReference: bool):
        self.__rawReference = rawReference

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
class dbl_StringPropertyType(PropertyType):

    pass
class dbl_StructuredPropertyType(PropertyType):

    pass
class dbl_IntPropertyType(PropertyType):

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
class VariableAccess:

    pass
class dbl_MetaAccess(VariableAccess):

    pass
class ElementAccess:

    pass
class dbl_TypeAccess(ElementAccess):

    pass
class L1RhsExpr:

    pass
class dbl_RhsClassifierExpr(L1RhsExpr):

    pass
class dbl_TerminalExpr(L1RhsExpr):

    def __init__(self, terminal: str):
        self.terminal = terminal
        
    @property
    def terminal(self) -> str:
        return self.__terminal

    @terminal.setter
    def terminal(self, terminal: str):
        self.__terminal = terminal

class L2RhsExpr:

    pass
class dbl_SequenceExpr(L2RhsExpr):

    pass
class RhsExpression:

    pass
class dbl_L1RhsExpr(RhsExpression):

    pass
class dbl_L2RhsExpr(RhsExpression):

    pass
class dbl_L3RhsExpr(RhsExpression):

    pass
class dbl_RhsExpression:

    pass
class LanguageConstructClassifier:

    pass
class dbl_LanguageConceptClassifier(LanguageConstructClassifier):

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
class dbl_StringLiteral(L1Expr):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dbl_TrueLiteral(L1Expr):

    pass
class dbl_FalseLiteral(L1Expr):

    pass
class dbl_TimeLiteral(L1Expr):

    pass
class dbl_NullLiteral(L1Expr):

    pass
class L2Expr:

    pass
class UnaryOperator:

    pass
class dbl_Not(L2Expr, UnaryOperator):

    pass
class dbl_Neg(L2Expr, UnaryOperator):

    pass
class dbl_CallPart:

    pass
class PredefinedId:

    pass
class dbl_MetaLiteral(PredefinedId):

    pass
class dbl_SuperLiteral(PredefinedId):

    pass
class dbl_SizeOfArray(PredefinedId):

    pass
class dbl_TypeLiteral(PredefinedId):

    pass
class dbl_MeLiteral(PredefinedId):

    pass
class dbl_PredefinedId:

    pass
class L3Expr:

    pass
class L4Expr:

    pass
class L5Expr:

    pass
class L6Expr:

    pass
class L7Expr:

    pass
class L8Expr:

    pass
class BinaryOperator:

    pass
class dbl_GreaterEqual(BinaryOperator, L5Expr):

    pass
class dbl_And(L7Expr, BinaryOperator):

    pass
class dbl_NotEqual(L6Expr, BinaryOperator):

    pass
class dbl_Minus(L4Expr, BinaryOperator):

    pass
class dbl_Equal(L6Expr, BinaryOperator):

    pass
class dbl_Div(L3Expr, BinaryOperator):

    pass
class dbl_Mul(L3Expr, BinaryOperator):

    pass
class dbl_InstanceOf(L5Expr, BinaryOperator):

    pass
class dbl_Plus(L4Expr, BinaryOperator):

    pass
class dbl_Greater(BinaryOperator, L5Expr):

    pass
class dbl_Mod(L3Expr, BinaryOperator):

    pass
class dbl_LessEqual(L5Expr, BinaryOperator):

    pass
class dbl_Less(BinaryOperator, L5Expr):

    pass
class dbl_Or(L8Expr, BinaryOperator):

    pass
class Expression:

    pass
class dbl_ParseExpr(Expression):

    pass
class dbl_ElementAccess(Expression):

    pass
class dbl_MetaExpr(Expression):

    pass
class dbl_CodeQuoteExpression(Expression):

    pass
class dbl_ExpandExpression(Expression):

    pass
class dbl_UniqueIdExpr(Expression):

    def __init__(self, identifier: str):
        self.identifier = identifier
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

class dbl_UnaryOperator(Expression):

    pass
class dbl_L1Expr(Expression):

    pass
class dbl_SwitchCase:

    pass
class dbl_BinaryOperator(Expression):

    pass
class dbl_L9Expr(Expression):

    pass
class dbl_L8Expr(Expression):

    pass
class dbl_L7Expr(Expression):

    pass
class dbl_L6Expr(Expression):

    pass
class dbl_L5Expr(Expression):

    pass
class dbl_L4Expr(Expression):

    pass
class dbl_L3Expr(Expression):

    pass
class dbl_L2Expr(Expression):

    pass
class LoopStatement:

    pass
class dbl_WhileStatement(LoopStatement):

    pass
class dbl_VariableAccess(ElementAccess):

    pass
class LanguageConceptClassifier:

    pass
class dbl_SuperClassSpecification:

    pass
class Statement:

    pass
class dbl_TestStatement(Statement):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class dbl_TargetStatement(Statement):

    pass
class dbl_ExpansionStatement(Statement):

    pass
class dbl_SimpleStatement(Statement):

    pass
class dbl_IfStatement(Statement):

    pass
class dbl_ExpandStatement(Statement):

    pass
class dbl_LoopStatement(Statement):

    pass
class dbl_NamedElement:

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
            if hasattr(old_value, "dbl_IdExpr150"):
                opp_val = getattr(old_value, "dbl_IdExpr150", None)
                if opp_val == self:
                    setattr(old_value, "dbl_IdExpr150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_IdExpr150"):
                opp_val = getattr(value, "dbl_IdExpr150", None)
                setattr(value, "dbl_IdExpr150", self)

class SimpleStatement:

    pass
class dbl_Terminate(SimpleStatement):

    pass
class dbl_ResumeGenStatement(SimpleStatement):

    pass
class dbl_Print(SimpleStatement):

    pass
class dbl_ContinueStatement(SimpleStatement):

    pass
class dbl_SwitchStatement(SimpleStatement):

    pass
class dbl_WaitUntil(SimpleStatement):

    pass
class dbl_SaveGenStatement(SimpleStatement):

    pass
class dbl_Yield(SimpleStatement):

    pass
class dbl_BreakStatement(SimpleStatement):

    pass
class dbl_FunctionCall(SimpleStatement):

    pass
class dbl_Wait(SimpleStatement):

    pass
class dbl_SetExpansionContextStatement(SimpleStatement):

    def __init__(self, addAfterContext: bool, dbl_SetExpansionContextStatement: "dbl_Expression" = None):
        self.addAfterContext = addAfterContext
        self.dbl_SetExpansionContextStatement = dbl_SetExpansionContextStatement
        
    @property
    def addAfterContext(self) -> bool:
        return self.__addAfterContext

    @addAfterContext.setter
    def addAfterContext(self, addAfterContext: bool):
        self.__addAfterContext = addAfterContext

    @property
    def dbl_SetExpansionContextStatement(self):
        return self.__dbl_SetExpansionContextStatement

    @dbl_SetExpansionContextStatement.setter
    def dbl_SetExpansionContextStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_SetExpansionContextStatement__dbl_SetExpansionContextStatement", None)
        self.__dbl_SetExpansionContextStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Expression197"):
                opp_val = getattr(old_value, "dbl_Expression197", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression197"):
                opp_val = getattr(value, "dbl_Expression197", None)
                setattr(value, "dbl_Expression197", self)

class dbl_Assignment(SimpleStatement):

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
            if hasattr(old_value, "dbl_Expression93"):
                opp_val = getattr(old_value, "dbl_Expression93", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression93"):
                opp_val = getattr(value, "dbl_Expression93", None)
                setattr(value, "dbl_Expression93", self)

class dbl_Reactivate(SimpleStatement):

    pass
class dbl_Return(SimpleStatement):

    pass
class AbstractVariable:

    pass
class dbl_LocalScope:

    pass
class dbl_TypedElement(ABC):

    pass
class dbl_ArrayDimension:

    pass
class dbl_Type(ABC):

    pass
class ConstructiveExtension:

    pass
class dbl_ClassContent(ConstructiveExtension):

    pass
class dbl_ModuleContent(ConstructiveExtension):

    pass
class dbl_ConstructiveExtensionAtContentExtensionPoint(ABC):

    pass
class ExtensibleElement:

    pass
class dbl_Statement(ExtensibleElement):

    pass
class dbl_TextualSyntaxDef(ExtensibleElement):

    pass
class dbl_ConstructiveExtension(ExtensibleElement):

    pass
class dbl_Variable(AbstractVariable, SimpleStatement):

    def __init__(self, control: bool, class: bool, dbl_Variable: "dbl_Module" = None, dbl_Variable68: "dbl_Class" = None, dbl_Variable78: "dbl_Expression" = None):
        self.control = control
        self.class = class
        self.dbl_Variable = dbl_Variable
        self.dbl_Variable68 = dbl_Variable68
        self.dbl_Variable78 = dbl_Variable78
        
    @property
    def class(self) -> bool:
        return self.__class

    @class.setter
    def class(self, class: bool):
        self.__class = class

    @property
    def control(self) -> bool:
        return self.__control

    @control.setter
    def control(self, control: bool):
        self.__control = control

    @property
    def dbl_Variable78(self):
        return self.__dbl_Variable78

    @dbl_Variable78.setter
    def dbl_Variable78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable78", None)
        self.__dbl_Variable78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Expression79"):
                opp_val = getattr(old_value, "dbl_Expression79", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression79"):
                opp_val = getattr(value, "dbl_Expression79", None)
                setattr(value, "dbl_Expression79", self)

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
            if hasattr(old_value, "dbl_Module42"):
                opp_val = getattr(old_value, "dbl_Module42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Module42"):
                opp_val = getattr(value, "dbl_Module42", None)
                if opp_val is None:
                    setattr(value, "dbl_Module42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Variable68(self):
        return self.__dbl_Variable68

    @dbl_Variable68.setter
    def dbl_Variable68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable68", None)
        self.__dbl_Variable68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Class67"):
                opp_val = getattr(old_value, "dbl_Class67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Class67"):
                opp_val = getattr(value, "dbl_Class67", None)
                if opp_val is None:
                    setattr(value, "dbl_Class67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_NativeBinding:

    def __init__(self, targetLanguage: str, targetType: str, dbl_NativeBinding: "dbl_Class" = None):
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
            if hasattr(old_value, "dbl_Class61"):
                opp_val = getattr(old_value, "dbl_Class61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Class61"):
                opp_val = getattr(value, "dbl_Class61", None)
                if opp_val is None:
                    setattr(value, "dbl_Class61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_Parameter(AbstractVariable):

    pass
class LocalScope:

    pass
class dbl_LocalScopeStatement(LocalScope, SimpleStatement):

    pass
class dbl_Constructor(LocalScope):

    pass
class dbl_ForStatement(LoopStatement, LocalScope):

    pass
class TypedElement:

    pass
class dbl_CreateObject(TypedElement, L1Expr):

    pass
class dbl_Cast(L2Expr, TypedElement, UnaryOperator):

    pass
class PrimitiveType:

    pass
class dbl_StringType(PrimitiveType):

    pass
class dbl_BoolType(PrimitiveType):

    pass
class dbl_DoubleType(PrimitiveType):

    pass
class dbl_IntType(PrimitiveType):

    pass
class dbl_VoidType(PrimitiveType):

    pass
class Type:

    pass
class dbl_Expression(TypedElement, ExtensibleElement):

    pass
class dbl_IdExpr(L1Expr):

    pass
class dbl_PrimitiveType(Type):

    pass
class Construct:

    pass
class NamedElement:

    pass
class dbl_LanguageConstructClassifier(NamedElement, ExtensibleElement):

    pass
class dbl_PropertyBindingExpr(NamedElement, L1RhsExpr):

    pass
class dbl_TsRule(NamedElement, LanguageConstructClassifier):

    pass
class dbl_AbstractVariable(TypedElement, NamedElement):

    pass
class dbl_Pattern(NamedElement):

    def __init__(self, top: bool, dbl_Pattern: "dbl_Parameter" = None, dbl_Pattern217: "dbl_Statement" = None):
        self.top = top
        self.dbl_Pattern = dbl_Pattern
        self.dbl_Pattern217 = dbl_Pattern217
        
    @property
    def top(self) -> bool:
        return self.__top

    @top.setter
    def top(self, top: bool):
        self.__top = top

    @property
    def dbl_Pattern217(self):
        return self.__dbl_Pattern217

    @dbl_Pattern217.setter
    def dbl_Pattern217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern217", None)
        self.__dbl_Pattern217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Statement218"):
                opp_val = getattr(old_value, "dbl_Statement218", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Statement218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Statement218"):
                opp_val = getattr(value, "dbl_Statement218", None)
                setattr(value, "dbl_Statement218", self)

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
            if hasattr(old_value, "dbl_Parameter215"):
                opp_val = getattr(old_value, "dbl_Parameter215", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Parameter215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Parameter215"):
                opp_val = getattr(value, "dbl_Parameter215", None)
                setattr(value, "dbl_Parameter215", self)

class dbl_Function(TypedElement, NamedElement, LocalScope):

    def __init__(self, class: bool, abstract: bool, dbl_Function54: set["dbl_Parameter"] = None, dbl_Function: "dbl_Module" = None, dbl_Function71: "dbl_Class" = None):
        self.class = class
        self.abstract = abstract
        self.dbl_Function54 = dbl_Function54 if dbl_Function54 is not None else set()
        self.dbl_Function = dbl_Function
        self.dbl_Function71 = dbl_Function71
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def class(self) -> bool:
        return self.__class

    @class.setter
    def class(self, class: bool):
        self.__class = class

    @property
    def dbl_Function71(self):
        return self.__dbl_Function71

    @dbl_Function71.setter
    def dbl_Function71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Function__dbl_Function71", None)
        self.__dbl_Function71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Class70"):
                opp_val = getattr(old_value, "dbl_Class70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Class70"):
                opp_val = getattr(value, "dbl_Class70", None)
                if opp_val is None:
                    setattr(value, "dbl_Class70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Function(self):
        return self.__dbl_Function

    @dbl_Function.setter
    def dbl_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Function__dbl_Function", None)
        self.__dbl_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Module40"):
                opp_val = getattr(old_value, "dbl_Module40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Module40"):
                opp_val = getattr(value, "dbl_Module40", None)
                if opp_val is None:
                    setattr(value, "dbl_Module40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Function54(self):
        return self.__dbl_Function54

    @dbl_Function54.setter
    def dbl_Function54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Function__dbl_Function54", None)
        self.__dbl_Function54 = value if value is not None else set()
        
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
                    

class dbl_ExtensibleElement(NamedElement, Construct):

    def __init__(self, concreteSyntax: str, instanceOfExtensionDefinition: bool, dbl_ExtensibleElement20: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement18: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement23: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement21: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement26: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement24: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement1: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement5: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement3: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement8: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement6: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement11: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement9: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement14: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement12: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement17: "dbl_ExtensibleElement" = None, dbl_ExtensibleElement15: "dbl_ExtensibleElement" = None):
        self.concreteSyntax = concreteSyntax
        self.instanceOfExtensionDefinition = instanceOfExtensionDefinition
        self.dbl_ExtensibleElement20 = dbl_ExtensibleElement20
        self.dbl_ExtensibleElement18 = dbl_ExtensibleElement18
        self.dbl_ExtensibleElement23 = dbl_ExtensibleElement23
        self.dbl_ExtensibleElement21 = dbl_ExtensibleElement21
        self.dbl_ExtensibleElement26 = dbl_ExtensibleElement26
        self.dbl_ExtensibleElement24 = dbl_ExtensibleElement24
        self.dbl_ExtensibleElement = dbl_ExtensibleElement
        self.dbl_ExtensibleElement1 = dbl_ExtensibleElement1
        self.dbl_ExtensibleElement5 = dbl_ExtensibleElement5
        self.dbl_ExtensibleElement3 = dbl_ExtensibleElement3
        self.dbl_ExtensibleElement8 = dbl_ExtensibleElement8
        self.dbl_ExtensibleElement6 = dbl_ExtensibleElement6
        self.dbl_ExtensibleElement11 = dbl_ExtensibleElement11
        self.dbl_ExtensibleElement9 = dbl_ExtensibleElement9
        self.dbl_ExtensibleElement14 = dbl_ExtensibleElement14
        self.dbl_ExtensibleElement12 = dbl_ExtensibleElement12
        self.dbl_ExtensibleElement17 = dbl_ExtensibleElement17
        self.dbl_ExtensibleElement15 = dbl_ExtensibleElement15
        
    @property
    def instanceOfExtensionDefinition(self) -> bool:
        return self.__instanceOfExtensionDefinition

    @instanceOfExtensionDefinition.setter
    def instanceOfExtensionDefinition(self, instanceOfExtensionDefinition: bool):
        self.__instanceOfExtensionDefinition = instanceOfExtensionDefinition

    @property
    def concreteSyntax(self) -> str:
        return self.__concreteSyntax

    @concreteSyntax.setter
    def concreteSyntax(self, concreteSyntax: str):
        self.__concreteSyntax = concreteSyntax

    @property
    def dbl_ExtensibleElement1(self):
        return self.__dbl_ExtensibleElement1

    @dbl_ExtensibleElement1.setter
    def dbl_ExtensibleElement1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement1", None)
        self.__dbl_ExtensibleElement1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement"):
                opp_val = getattr(value, "dbl_ExtensibleElement", None)
                setattr(value, "dbl_ExtensibleElement", self)

    @property
    def dbl_ExtensibleElement20(self):
        return self.__dbl_ExtensibleElement20

    @dbl_ExtensibleElement20.setter
    def dbl_ExtensibleElement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement20", None)
        self.__dbl_ExtensibleElement20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement18"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement18", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement18"):
                opp_val = getattr(value, "dbl_ExtensibleElement18", None)
                setattr(value, "dbl_ExtensibleElement18", self)

    @property
    def dbl_ExtensibleElement23(self):
        return self.__dbl_ExtensibleElement23

    @dbl_ExtensibleElement23.setter
    def dbl_ExtensibleElement23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement23", None)
        self.__dbl_ExtensibleElement23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement21"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement21", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement21"):
                opp_val = getattr(value, "dbl_ExtensibleElement21", None)
                setattr(value, "dbl_ExtensibleElement21", self)

    @property
    def dbl_ExtensibleElement17(self):
        return self.__dbl_ExtensibleElement17

    @dbl_ExtensibleElement17.setter
    def dbl_ExtensibleElement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement17", None)
        self.__dbl_ExtensibleElement17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement15"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement15", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement15"):
                opp_val = getattr(value, "dbl_ExtensibleElement15", None)
                setattr(value, "dbl_ExtensibleElement15", self)

    @property
    def dbl_ExtensibleElement14(self):
        return self.__dbl_ExtensibleElement14

    @dbl_ExtensibleElement14.setter
    def dbl_ExtensibleElement14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement14", None)
        self.__dbl_ExtensibleElement14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement12"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement12", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement12"):
                opp_val = getattr(value, "dbl_ExtensibleElement12", None)
                setattr(value, "dbl_ExtensibleElement12", self)

    @property
    def dbl_ExtensibleElement11(self):
        return self.__dbl_ExtensibleElement11

    @dbl_ExtensibleElement11.setter
    def dbl_ExtensibleElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement11", None)
        self.__dbl_ExtensibleElement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement9"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement9", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement9"):
                opp_val = getattr(value, "dbl_ExtensibleElement9", None)
                setattr(value, "dbl_ExtensibleElement9", self)

    @property
    def dbl_ExtensibleElement24(self):
        return self.__dbl_ExtensibleElement24

    @dbl_ExtensibleElement24.setter
    def dbl_ExtensibleElement24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement24", None)
        self.__dbl_ExtensibleElement24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement26"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement26", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement26"):
                opp_val = getattr(value, "dbl_ExtensibleElement26", None)
                setattr(value, "dbl_ExtensibleElement26", self)

    @property
    def dbl_ExtensibleElement6(self):
        return self.__dbl_ExtensibleElement6

    @dbl_ExtensibleElement6.setter
    def dbl_ExtensibleElement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement6", None)
        self.__dbl_ExtensibleElement6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement8"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement8", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement8"):
                opp_val = getattr(value, "dbl_ExtensibleElement8", None)
                setattr(value, "dbl_ExtensibleElement8", self)

    @property
    def dbl_ExtensibleElement8(self):
        return self.__dbl_ExtensibleElement8

    @dbl_ExtensibleElement8.setter
    def dbl_ExtensibleElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement8", None)
        self.__dbl_ExtensibleElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement6"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement6", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement6"):
                opp_val = getattr(value, "dbl_ExtensibleElement6", None)
                setattr(value, "dbl_ExtensibleElement6", self)

    @property
    def dbl_ExtensibleElement3(self):
        return self.__dbl_ExtensibleElement3

    @dbl_ExtensibleElement3.setter
    def dbl_ExtensibleElement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement3", None)
        self.__dbl_ExtensibleElement3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement5"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement5", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement5"):
                opp_val = getattr(value, "dbl_ExtensibleElement5", None)
                setattr(value, "dbl_ExtensibleElement5", self)

    @property
    def dbl_ExtensibleElement21(self):
        return self.__dbl_ExtensibleElement21

    @dbl_ExtensibleElement21.setter
    def dbl_ExtensibleElement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement21", None)
        self.__dbl_ExtensibleElement21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement23"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement23", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement23"):
                opp_val = getattr(value, "dbl_ExtensibleElement23", None)
                setattr(value, "dbl_ExtensibleElement23", self)

    @property
    def dbl_ExtensibleElement26(self):
        return self.__dbl_ExtensibleElement26

    @dbl_ExtensibleElement26.setter
    def dbl_ExtensibleElement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement26", None)
        self.__dbl_ExtensibleElement26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement24"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement24", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement24"):
                opp_val = getattr(value, "dbl_ExtensibleElement24", None)
                setattr(value, "dbl_ExtensibleElement24", self)

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
            if hasattr(old_value, "dbl_ExtensibleElement1"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement1", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement1"):
                opp_val = getattr(value, "dbl_ExtensibleElement1", None)
                setattr(value, "dbl_ExtensibleElement1", self)

    @property
    def dbl_ExtensibleElement9(self):
        return self.__dbl_ExtensibleElement9

    @dbl_ExtensibleElement9.setter
    def dbl_ExtensibleElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement9", None)
        self.__dbl_ExtensibleElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement11"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement11", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement11"):
                opp_val = getattr(value, "dbl_ExtensibleElement11", None)
                setattr(value, "dbl_ExtensibleElement11", self)

    @property
    def dbl_ExtensibleElement12(self):
        return self.__dbl_ExtensibleElement12

    @dbl_ExtensibleElement12.setter
    def dbl_ExtensibleElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement12", None)
        self.__dbl_ExtensibleElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement14"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement14", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement14"):
                opp_val = getattr(value, "dbl_ExtensibleElement14", None)
                setattr(value, "dbl_ExtensibleElement14", self)

    @property
    def dbl_ExtensibleElement18(self):
        return self.__dbl_ExtensibleElement18

    @dbl_ExtensibleElement18.setter
    def dbl_ExtensibleElement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement18", None)
        self.__dbl_ExtensibleElement18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement20"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement20", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement20"):
                opp_val = getattr(value, "dbl_ExtensibleElement20", None)
                setattr(value, "dbl_ExtensibleElement20", self)

    @property
    def dbl_ExtensibleElement15(self):
        return self.__dbl_ExtensibleElement15

    @dbl_ExtensibleElement15.setter
    def dbl_ExtensibleElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement15", None)
        self.__dbl_ExtensibleElement15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement17"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement17", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement17"):
                opp_val = getattr(value, "dbl_ExtensibleElement17", None)
                setattr(value, "dbl_ExtensibleElement17", self)

    @property
    def dbl_ExtensibleElement5(self):
        return self.__dbl_ExtensibleElement5

    @dbl_ExtensibleElement5.setter
    def dbl_ExtensibleElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement5", None)
        self.__dbl_ExtensibleElement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensibleElement3"):
                opp_val = getattr(old_value, "dbl_ExtensibleElement3", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensibleElement3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensibleElement3"):
                opp_val = getattr(value, "dbl_ExtensibleElement3", None)
                setattr(value, "dbl_ExtensibleElement3", self)

class dbl_ExtensionSemanticsDefinition(LocalScope, ExtensibleElement):

    pass
class dbl_ExtensionDefinition(LanguageConceptClassifier, ExtensibleElement):

    pass
class ConstructiveExtensionAtContentExtensionPoint:

    pass
class dbl_Class(LanguageConceptClassifier, Construct, Type, ConstructiveExtensionAtContentExtensionPoint, NamedElement):

    def __init__(self, active: bool, dbl_Class: "dbl_Module" = None, owningClass: set["dbl_Constructor"] = None, dbl_Class67: set["dbl_Variable"] = None, dbl_Class70: set["dbl_Function"] = None, dbl_Class73: "dbl_LocalScope" = None, Class: "dbl_Constructor" = None, dbl_Class56: "dbl_SuperClassSpecification" = None, dbl_Class61: set["dbl_NativeBinding"] = None, dbl_Class63: set["dbl_SuperClassSpecification"] = None, dbl_Class167: "dbl_ExtensionDefinition" = None):
        self.active = active
        self.dbl_Class = dbl_Class
        self.owningClass = owningClass if owningClass is not None else set()
        self.dbl_Class67 = dbl_Class67 if dbl_Class67 is not None else set()
        self.dbl_Class70 = dbl_Class70 if dbl_Class70 is not None else set()
        self.dbl_Class73 = dbl_Class73
        self.Class = Class
        self.dbl_Class56 = dbl_Class56
        self.dbl_Class61 = dbl_Class61 if dbl_Class61 is not None else set()
        self.dbl_Class63 = dbl_Class63 if dbl_Class63 is not None else set()
        self.dbl_Class167 = dbl_Class167
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def dbl_Class167(self):
        return self.__dbl_Class167

    @dbl_Class167.setter
    def dbl_Class167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class167", None)
        self.__dbl_Class167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ExtensionDefinition166"):
                opp_val = getattr(old_value, "dbl_ExtensionDefinition166", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ExtensionDefinition166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ExtensionDefinition166"):
                opp_val = getattr(value, "dbl_ExtensionDefinition166", None)
                setattr(value, "dbl_ExtensionDefinition166", self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constructors"):
                opp_val = getattr(old_value, "constructors", None)
                if opp_val == self:
                    setattr(old_value, "constructors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constructors"):
                opp_val = getattr(value, "constructors", None)
                setattr(value, "constructors", self)

    @property
    def dbl_Class70(self):
        return self.__dbl_Class70

    @dbl_Class70.setter
    def dbl_Class70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class70", None)
        self.__dbl_Class70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_Function71"):
                    opp_val = getattr(item, "dbl_Function71", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_Function71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_Function71"):
                    opp_val = getattr(item, "dbl_Function71", None)
                    
                    setattr(item, "dbl_Function71", self)
                    

    @property
    def dbl_Class73(self):
        return self.__dbl_Class73

    @dbl_Class73.setter
    def dbl_Class73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class73", None)
        self.__dbl_Class73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_LocalScope"):
                opp_val = getattr(old_value, "dbl_LocalScope", None)
                if opp_val == self:
                    setattr(old_value, "dbl_LocalScope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_LocalScope"):
                opp_val = getattr(value, "dbl_LocalScope", None)
                setattr(value, "dbl_LocalScope", self)

    @property
    def dbl_Class(self):
        return self.__dbl_Class

    @dbl_Class.setter
    def dbl_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class", None)
        self.__dbl_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Module34"):
                opp_val = getattr(old_value, "dbl_Module34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Module34"):
                opp_val = getattr(value, "dbl_Module34", None)
                if opp_val is None:
                    setattr(value, "dbl_Module34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Class61(self):
        return self.__dbl_Class61

    @dbl_Class61.setter
    def dbl_Class61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class61", None)
        self.__dbl_Class61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_NativeBinding"):
                    opp_val = getattr(item, "dbl_NativeBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_NativeBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_NativeBinding"):
                    opp_val = getattr(item, "dbl_NativeBinding", None)
                    
                    setattr(item, "dbl_NativeBinding", self)
                    

    @property
    def dbl_Class67(self):
        return self.__dbl_Class67

    @dbl_Class67.setter
    def dbl_Class67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class67", None)
        self.__dbl_Class67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_Variable68"):
                    opp_val = getattr(item, "dbl_Variable68", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_Variable68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_Variable68"):
                    opp_val = getattr(item, "dbl_Variable68", None)
                    
                    setattr(item, "dbl_Variable68", self)
                    

    @property
    def dbl_Class56(self):
        return self.__dbl_Class56

    @dbl_Class56.setter
    def dbl_Class56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class56", None)
        self.__dbl_Class56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_SuperClassSpecification"):
                opp_val = getattr(old_value, "dbl_SuperClassSpecification", None)
                if opp_val == self:
                    setattr(old_value, "dbl_SuperClassSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_SuperClassSpecification"):
                opp_val = getattr(value, "dbl_SuperClassSpecification", None)
                setattr(value, "dbl_SuperClassSpecification", self)

    @property
    def dbl_Class63(self):
        return self.__dbl_Class63

    @dbl_Class63.setter
    def dbl_Class63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class63", None)
        self.__dbl_Class63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_SuperClassSpecification64"):
                    opp_val = getattr(item, "dbl_SuperClassSpecification64", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_SuperClassSpecification64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_SuperClassSpecification64"):
                    opp_val = getattr(item, "dbl_SuperClassSpecification64", None)
                    
                    setattr(item, "dbl_SuperClassSpecification64", self)
                    

    @property
    def owningClass(self):
        return self.__owningClass

    @owningClass.setter
    def owningClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__owningClass", None)
        self.__owningClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constructor"):
                    opp_val = getattr(item, "Constructor", None)
                    
                    if opp_val == self:
                        setattr(item, "Constructor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constructor"):
                    opp_val = getattr(item, "Constructor", None)
                    
                    setattr(item, "Constructor", self)
                    

class dbl_Module(ConstructiveExtensionAtContentExtensionPoint, NamedElement, Construct):

    pass
class dbl_Import:

    def __init__(self, file: str, dbl_Import: "dbl_Model" = None, dbl_Import31: "dbl_Model" = None):
        self.file = file
        self.dbl_Import = dbl_Import
        self.dbl_Import31 = dbl_Import31
        
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
    def dbl_Import31(self):
        return self.__dbl_Import31

    @dbl_Import31.setter
    def dbl_Import31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Import__dbl_Import31", None)
        self.__dbl_Import31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Model32"):
                opp_val = getattr(old_value, "dbl_Model32", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Model32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Model32"):
                opp_val = getattr(value, "dbl_Model32", None)
                setattr(value, "dbl_Model32", self)

class dbl_Model:

    pass
class dbl_ExpandExpr(Expression):

    pass
class dbl_Construct:

    pass
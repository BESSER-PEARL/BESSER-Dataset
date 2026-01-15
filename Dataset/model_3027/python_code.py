from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dbl_QuotedCode:

    pass
class Module:

    pass
class Class:

    pass
class QuotedCode:

    pass
class dbl_QuotedExpression(QuotedCode):

    pass
class dbl_QuotedStatements(QuotedCode):

    pass
class dbl_QuotedClassContent(Class, QuotedCode):

    pass
class dbl_QuotedModuleContent(Module, QuotedCode):

    pass
class dbl_ExpansionPart(ABC):

    pass
class ExpansionPart:

    pass
class dbl_ExpandVariablePart(ExpansionPart):

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

class ElementarySymbol:

    pass
class dbl_IntSymbol(ElementarySymbol):

    pass
class dbl_Keyword(ElementarySymbol):

    def __init__(self, keyword: str):
        self.keyword = keyword
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

class dbl_StringSymbol(ElementarySymbol):

    pass
class dbl_IdSymbol(ElementarySymbol):

    pass
class Variable:

    pass
class dbl_CreateIdStatement(Variable):

    pass
class PlainSymbolReference:

    pass
class L1SyntaxExpression:

    pass
class dbl_PlainSymbolReference(L1SyntaxExpression):

    pass
class L2SyntaxExpression:

    pass
class dbl_SymbolSequence(L2SyntaxExpression):

    pass
class SyntaxExpression:

    pass
class dbl_L1SyntaxExpression(SyntaxExpression):

    pass
class dbl_L2SyntaxExpression(SyntaxExpression):

    pass
class dbl_L3SyntaxExpression(SyntaxExpression):

    pass
class dbl_SyntaxExpression:

    pass
class ComplexSymbol:

    pass
class SyntaxSymbolClassifier:

    pass
class dbl_ElementarySymbol(SyntaxSymbolClassifier):

    pass
class dbl_ComplexSymbol(SyntaxSymbolClassifier):

    pass
class dbl_CallPart:

    pass
class dbl_Concept(ComplexSymbol):

    pass
class VariableAccess:

    pass
class dbl_MetaAccess(VariableAccess):

    pass
class ElementAccess:

    pass
class dbl_TypeAccess(ElementAccess):

    pass
class PredefinedId:

    pass
class dbl_MeLiteral(PredefinedId):

    pass
class dbl_PredefinedId:

    pass
class Annotation:

    pass
class dbl_AnnotationLiteral(Annotation, PredefinedId):

    pass
class dbl_SizeOfArray(PredefinedId):

    pass
class dbl_TypeLiteral(PredefinedId):

    pass
class dbl_MetaLiteral(PredefinedId):

    pass
class dbl_SuperLiteral(PredefinedId):

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

class L2Expr:

    pass
class UnaryOperator:

    pass
class dbl_Not(L2Expr, UnaryOperator):

    pass
class dbl_Neg(L2Expr, UnaryOperator):

    pass
class dbl_FalseLiteral(L1Expr):

    pass
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

class dbl_StringLiteral(L1Expr):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dbl_ActiveLiteral(L1Expr):

    pass
class dbl_TimeLiteral(L1Expr):

    pass
class dbl_NullLiteral(L1Expr):

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
class dbl_Equal(BinaryOperator, L6Expr):

    pass
class dbl_Greater(L5Expr, BinaryOperator):

    pass
class dbl_NotEqual(BinaryOperator, L6Expr):

    pass
class dbl_And(BinaryOperator, L7Expr):

    pass
class dbl_Or(BinaryOperator, L8Expr):

    pass
class L3Expr:

    pass
class dbl_Mod(BinaryOperator, L3Expr):

    pass
class dbl_Div(BinaryOperator, L3Expr):

    pass
class dbl_Mul(BinaryOperator, L3Expr):

    pass
class L4Expr:

    pass
class dbl_Minus(L4Expr, BinaryOperator):

    pass
class dbl_Plus(L4Expr, BinaryOperator):

    pass
class dbl_InstanceOf(L5Expr, BinaryOperator):

    pass
class dbl_LessEqual(L5Expr, BinaryOperator):

    pass
class dbl_Less(L5Expr, BinaryOperator):

    pass
class dbl_GreaterEqual(L5Expr, BinaryOperator):

    pass
class Expression:

    pass
class dbl_ParseExpr(Expression):

    pass
class dbl_L5Expr(Expression):

    pass
class dbl_CodeQuoteExpression(Expression):

    pass
class dbl_L4Expr(Expression):

    pass
class dbl_L2Expr(Expression):

    pass
class dbl_MetaExpr(Expression):

    pass
class dbl_ElementAccess(Expression):

    pass
class dbl_ExpandExpression(Expression):

    pass
class dbl_L3Expr(Expression):

    pass
class dbl_L1Expr(Expression):

    pass
class dbl_UnaryOperator(Expression):

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
class dbl_SwitchCase:

    pass
class LoopStatement:

    pass
class dbl_WhileStatement(LoopStatement):

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
            if hasattr(old_value, "dbl_IdExpr129"):
                opp_val = getattr(old_value, "dbl_IdExpr129", None)
                if opp_val == self:
                    setattr(old_value, "dbl_IdExpr129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_IdExpr129"):
                opp_val = getattr(value, "dbl_IdExpr129", None)
                setattr(value, "dbl_IdExpr129", self)

class SimpleStatement:

    pass
class dbl_WaitUntil(SimpleStatement):

    pass
class dbl_TargetStatement(SimpleStatement):

    pass
class dbl_Wait(SimpleStatement):

    pass
class dbl_Reactivate(SimpleStatement):

    pass
class dbl_Advance(SimpleStatement):

    pass
class dbl_Print(SimpleStatement):

    pass
class dbl_ContinueStatement(SimpleStatement):

    pass
class dbl_BreakStatement(SimpleStatement):

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
            if hasattr(old_value, "dbl_Expression72"):
                opp_val = getattr(old_value, "dbl_Expression72", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression72"):
                opp_val = getattr(value, "dbl_Expression72", None)
                setattr(value, "dbl_Expression72", self)

class dbl_Return(SimpleStatement):

    pass
class dbl_SwitchStatement(SimpleStatement):

    pass
class dbl_Yield(SimpleStatement):

    pass
class dbl_YieldTo(SimpleStatement):

    pass
class dbl_Terminate(SimpleStatement):

    pass
class dbl_ExpansionStatement(SimpleStatement):

    def __init__(self, classContext: bool, functionContext: bool, variableContext: bool, dbl_ExpansionStatement: "dbl_IdExpr" = None, dbl_ExpansionStatement172: set["dbl_ExpansionPart"] = None, dbl_ExpansionStatement174: set["dbl_Expression"] = None):
        self.classContext = classContext
        self.functionContext = functionContext
        self.variableContext = variableContext
        self.dbl_ExpansionStatement = dbl_ExpansionStatement
        self.dbl_ExpansionStatement172 = dbl_ExpansionStatement172 if dbl_ExpansionStatement172 is not None else set()
        self.dbl_ExpansionStatement174 = dbl_ExpansionStatement174 if dbl_ExpansionStatement174 is not None else set()
        
    @property
    def functionContext(self) -> bool:
        return self.__functionContext

    @functionContext.setter
    def functionContext(self, functionContext: bool):
        self.__functionContext = functionContext

    @property
    def classContext(self) -> bool:
        return self.__classContext

    @classContext.setter
    def classContext(self, classContext: bool):
        self.__classContext = classContext

    @property
    def variableContext(self) -> bool:
        return self.__variableContext

    @variableContext.setter
    def variableContext(self, variableContext: bool):
        self.__variableContext = variableContext

    @property
    def dbl_ExpansionStatement172(self):
        return self.__dbl_ExpansionStatement172

    @dbl_ExpansionStatement172.setter
    def dbl_ExpansionStatement172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExpansionStatement__dbl_ExpansionStatement172", None)
        self.__dbl_ExpansionStatement172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_ExpansionPart"):
                    opp_val = getattr(item, "dbl_ExpansionPart", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_ExpansionPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_ExpansionPart"):
                    opp_val = getattr(item, "dbl_ExpansionPart", None)
                    
                    setattr(item, "dbl_ExpansionPart", self)
                    

    @property
    def dbl_ExpansionStatement174(self):
        return self.__dbl_ExpansionStatement174

    @dbl_ExpansionStatement174.setter
    def dbl_ExpansionStatement174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExpansionStatement__dbl_ExpansionStatement174", None)
        self.__dbl_ExpansionStatement174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_Expression175"):
                    opp_val = getattr(item, "dbl_Expression175", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_Expression175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_Expression175"):
                    opp_val = getattr(item, "dbl_Expression175", None)
                    
                    setattr(item, "dbl_Expression175", self)
                    

    @property
    def dbl_ExpansionStatement(self):
        return self.__dbl_ExpansionStatement

    @dbl_ExpansionStatement.setter
    def dbl_ExpansionStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExpansionStatement__dbl_ExpansionStatement", None)
        self.__dbl_ExpansionStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_IdExpr170"):
                opp_val = getattr(old_value, "dbl_IdExpr170", None)
                if opp_val == self:
                    setattr(old_value, "dbl_IdExpr170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_IdExpr170"):
                opp_val = getattr(value, "dbl_IdExpr170", None)
                setattr(value, "dbl_IdExpr170", self)

class AbstractVariable:

    pass
class dbl_FunctionCall(SimpleStatement):

    pass
class dbl_VariableAccess(ElementAccess):

    pass
class dbl_Assignment(SimpleStatement):

    pass
class Statement:

    pass
class dbl_SimpleStatement(Statement):

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

class dbl_IfStatement(Statement):

    pass
class dbl_ExpandStatement(Statement):

    pass
class dbl_LoopStatement(Statement):

    pass
class AnnotateableElement:

    pass
class Concept:

    pass
class dbl_LocalScope:

    pass
class dbl_NativeBinding:

    def __init__(self, targetType: str, targetLanguage: str, dbl_NativeBinding: "dbl_Class" = None):
        self.targetType = targetType
        self.targetLanguage = targetLanguage
        self.dbl_NativeBinding = dbl_NativeBinding
        
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
    def dbl_NativeBinding(self):
        return self.__dbl_NativeBinding

    @dbl_NativeBinding.setter
    def dbl_NativeBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_NativeBinding__dbl_NativeBinding", None)
        self.__dbl_NativeBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Class38"):
                opp_val = getattr(old_value, "dbl_Class38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Class38"):
                opp_val = getattr(value, "dbl_Class38", None)
                if opp_val is None:
                    setattr(value, "dbl_Class38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_Parameter(AbstractVariable):

    pass
class LocalScope:

    pass
class dbl_Constructor(LocalScope):

    pass
class dbl_LocalScopeStatement(LocalScope, SimpleStatement):

    pass
class dbl_ForStatement(LocalScope, LoopStatement):

    pass
class TypedElement:

    pass
class dbl_Cast(L2Expr, TypedElement, UnaryOperator):

    pass
class dbl_CreateObject(TypedElement, L1Expr):

    pass
class dbl_SuperClassSpecification:

    pass
class dbl_IdExpr(L1Expr):

    pass
class dbl_TypedElement(ABC):

    pass
class dbl_ArrayDimension:

    pass
class dbl_Type(ABC):

    pass
class ConstructiveExtension:

    pass
class dbl_ClassContentExtension(ConstructiveExtension):

    pass
class dbl_ModuleContentExtension(ConstructiveExtension):

    pass
class PrimitiveType:

    pass
class dbl_IntType(PrimitiveType):

    pass
class dbl_BoolType(PrimitiveType):

    pass
class dbl_DoubleType(PrimitiveType):

    pass
class dbl_StringType(PrimitiveType):

    pass
class dbl_VoidType(PrimitiveType):

    pass
class Type:

    pass
class dbl_PrimitiveType(Type):

    pass
class dbl_Variable(SimpleStatement, AbstractVariable):

    def __init__(self, control: bool, class: bool, dbl_Variable: "dbl_Module" = None, dbl_Variable45: "dbl_Class" = None, dbl_Variable55: "dbl_Expression" = None):
        self.control = control
        self.class = class
        self.dbl_Variable = dbl_Variable
        self.dbl_Variable45 = dbl_Variable45
        self.dbl_Variable55 = dbl_Variable55
        
    @property
    def control(self) -> bool:
        return self.__control

    @control.setter
    def control(self, control: bool):
        self.__control = control

    @property
    def class(self) -> bool:
        return self.__class

    @class.setter
    def class(self, class: bool):
        self.__class = class

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
            if hasattr(old_value, "dbl_Module16"):
                opp_val = getattr(old_value, "dbl_Module16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Module16"):
                opp_val = getattr(value, "dbl_Module16", None)
                if opp_val is None:
                    setattr(value, "dbl_Module16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Variable55(self):
        return self.__dbl_Variable55

    @dbl_Variable55.setter
    def dbl_Variable55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable55", None)
        self.__dbl_Variable55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Expression56"):
                opp_val = getattr(old_value, "dbl_Expression56", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression56"):
                opp_val = getattr(value, "dbl_Expression56", None)
                setattr(value, "dbl_Expression56", self)

    @property
    def dbl_Variable45(self):
        return self.__dbl_Variable45

    @dbl_Variable45.setter
    def dbl_Variable45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable45", None)
        self.__dbl_Variable45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Class44"):
                opp_val = getattr(old_value, "dbl_Class44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Class44"):
                opp_val = getattr(value, "dbl_Class44", None)
                if opp_val is None:
                    setattr(value, "dbl_Class44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_ConstructiveExtensionAtContentExtensionPoint(ABC):

    pass
class ExtensibleElement:

    pass
class dbl_Expression(ExtensibleElement, TypedElement):

    pass
class dbl_ExtensionSemantics(LocalScope, ExtensibleElement):

    pass
class dbl_SyntaxDefinition(ExtensibleElement):

    pass
class dbl_Statement(ExtensibleElement, AnnotateableElement):

    pass
class dbl_Extension(Concept, ExtensibleElement):

    pass
class dbl_ConstructiveExtension(ExtensibleElement):

    pass
class dbl_AnnotateableElement:

    pass
class dbl_AnnotationItem:

    def __init__(self, key: str, value: str, dbl_AnnotationItem: "dbl_Annotation" = None):
        self.key = key
        self.value = value
        self.dbl_AnnotationItem = dbl_AnnotationItem
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def dbl_AnnotationItem(self):
        return self.__dbl_AnnotationItem

    @dbl_AnnotationItem.setter
    def dbl_AnnotationItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_AnnotationItem__dbl_AnnotationItem", None)
        self.__dbl_AnnotationItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Annotation"):
                opp_val = getattr(old_value, "dbl_Annotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Annotation"):
                opp_val = getattr(value, "dbl_Annotation", None)
                if opp_val is None:
                    setattr(value, "dbl_Annotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_Model:

    pass
class Construct:

    pass
class NamedElement:

    pass
class dbl_Pattern(NamedElement):

    def __init__(self, top: bool, dbl_Pattern: "dbl_Parameter" = None, dbl_Pattern193: "dbl_Statement" = None):
        self.top = top
        self.dbl_Pattern = dbl_Pattern
        self.dbl_Pattern193 = dbl_Pattern193
        
    @property
    def top(self) -> bool:
        return self.__top

    @top.setter
    def top(self, top: bool):
        self.__top = top

    @property
    def dbl_Pattern193(self):
        return self.__dbl_Pattern193

    @dbl_Pattern193.setter
    def dbl_Pattern193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern193", None)
        self.__dbl_Pattern193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Statement194"):
                opp_val = getattr(old_value, "dbl_Statement194", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Statement194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Statement194"):
                opp_val = getattr(value, "dbl_Statement194", None)
                setattr(value, "dbl_Statement194", self)

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
            if hasattr(old_value, "dbl_Parameter191"):
                opp_val = getattr(old_value, "dbl_Parameter191", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Parameter191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Parameter191"):
                opp_val = getattr(value, "dbl_Parameter191", None)
                setattr(value, "dbl_Parameter191", self)

class dbl_SyntaxSymbolClassifier(NamedElement, ExtensibleElement):

    pass
class dbl_StructuralSymbolReference(PlainSymbolReference, NamedElement):

    def __init__(self, composite: bool, localScopedReference: bool, globalScopedReference: bool, list: bool):
        self.composite = composite
        self.localScopedReference = localScopedReference
        self.globalScopedReference = globalScopedReference
        self.list = list
        
    @property
    def localScopedReference(self) -> bool:
        return self.__localScopedReference

    @localScopedReference.setter
    def localScopedReference(self, localScopedReference: bool):
        self.__localScopedReference = localScopedReference

    @property
    def globalScopedReference(self) -> bool:
        return self.__globalScopedReference

    @globalScopedReference.setter
    def globalScopedReference(self, globalScopedReference: bool):
        self.__globalScopedReference = globalScopedReference

    @property
    def composite(self) -> bool:
        return self.__composite

    @composite.setter
    def composite(self, composite: bool):
        self.__composite = composite

    @property
    def list(self) -> bool:
        return self.__list

    @list.setter
    def list(self, list: bool):
        self.__list = list

class dbl_Annotation(NamedElement):

    pass
class dbl_Function(NamedElement, TypedElement, LocalScope):

    def __init__(self, class: bool, abstract: bool, detached: bool, dbl_Function: "dbl_Module" = None, dbl_Function31: set["dbl_Parameter"] = None, dbl_Function48: "dbl_Class" = None):
        self.class = class
        self.abstract = abstract
        self.detached = detached
        self.dbl_Function = dbl_Function
        self.dbl_Function31 = dbl_Function31 if dbl_Function31 is not None else set()
        self.dbl_Function48 = dbl_Function48
        
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
    def detached(self) -> bool:
        return self.__detached

    @detached.setter
    def detached(self, detached: bool):
        self.__detached = detached

    @property
    def dbl_Function31(self):
        return self.__dbl_Function31

    @dbl_Function31.setter
    def dbl_Function31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Function__dbl_Function31", None)
        self.__dbl_Function31 = value if value is not None else set()
        
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
    def dbl_Function(self):
        return self.__dbl_Function

    @dbl_Function.setter
    def dbl_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Function__dbl_Function", None)
        self.__dbl_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Module14"):
                opp_val = getattr(old_value, "dbl_Module14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Module14"):
                opp_val = getattr(value, "dbl_Module14", None)
                if opp_val is None:
                    setattr(value, "dbl_Module14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Function48(self):
        return self.__dbl_Function48

    @dbl_Function48.setter
    def dbl_Function48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Function__dbl_Function48", None)
        self.__dbl_Function48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Class47"):
                opp_val = getattr(old_value, "dbl_Class47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Class47"):
                opp_val = getattr(value, "dbl_Class47", None)
                if opp_val is None:
                    setattr(value, "dbl_Class47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_AbstractVariable(NamedElement, TypedElement, AnnotateableElement):

    pass
class dbl_MetaSymbol(NamedElement, ComplexSymbol):

    pass
class dbl_ExtensibleElement(NamedElement, Construct):

    def __init__(self, concreteSyntax: str, instanceOfExtensionDefinition: bool):
        self.concreteSyntax = concreteSyntax
        self.instanceOfExtensionDefinition = instanceOfExtensionDefinition
        
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

class dbl_ExpandExpr(Expression):

    pass
class dbl_Construct:

    pass
class ConstructiveExtensionAtContentExtensionPoint:

    pass
class dbl_Class(Concept, ConstructiveExtensionAtContentExtensionPoint, Type, NamedElement, Construct, AnnotateableElement):

    def __init__(self, active: bool, dbl_Class: "dbl_Module" = None, dbl_Class33: "dbl_SuperClassSpecification" = None, dbl_Class44: set["dbl_Variable"] = None, dbl_Class47: set["dbl_Function"] = None, dbl_Class50: "dbl_LocalScope" = None, Class: "dbl_Constructor" = None, dbl_Class38: set["dbl_NativeBinding"] = None, dbl_Class40: set["dbl_SuperClassSpecification"] = None, owningClass: set["dbl_Constructor"] = None):
        self.active = active
        self.dbl_Class = dbl_Class
        self.dbl_Class33 = dbl_Class33
        self.dbl_Class44 = dbl_Class44 if dbl_Class44 is not None else set()
        self.dbl_Class47 = dbl_Class47 if dbl_Class47 is not None else set()
        self.dbl_Class50 = dbl_Class50
        self.Class = Class
        self.dbl_Class38 = dbl_Class38 if dbl_Class38 is not None else set()
        self.dbl_Class40 = dbl_Class40 if dbl_Class40 is not None else set()
        self.owningClass = owningClass if owningClass is not None else set()
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def dbl_Class38(self):
        return self.__dbl_Class38

    @dbl_Class38.setter
    def dbl_Class38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class38", None)
        self.__dbl_Class38 = value if value is not None else set()
        
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
    def dbl_Class(self):
        return self.__dbl_Class

    @dbl_Class.setter
    def dbl_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class", None)
        self.__dbl_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Module8"):
                opp_val = getattr(old_value, "dbl_Module8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Module8"):
                opp_val = getattr(value, "dbl_Module8", None)
                if opp_val is None:
                    setattr(value, "dbl_Module8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbl_Class44(self):
        return self.__dbl_Class44

    @dbl_Class44.setter
    def dbl_Class44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class44", None)
        self.__dbl_Class44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_Variable45"):
                    opp_val = getattr(item, "dbl_Variable45", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_Variable45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_Variable45"):
                    opp_val = getattr(item, "dbl_Variable45", None)
                    
                    setattr(item, "dbl_Variable45", self)
                    

    @property
    def dbl_Class33(self):
        return self.__dbl_Class33

    @dbl_Class33.setter
    def dbl_Class33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class33", None)
        self.__dbl_Class33 = value
        
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
    def dbl_Class50(self):
        return self.__dbl_Class50

    @dbl_Class50.setter
    def dbl_Class50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class50", None)
        self.__dbl_Class50 = value
        
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
    def dbl_Class40(self):
        return self.__dbl_Class40

    @dbl_Class40.setter
    def dbl_Class40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class40", None)
        self.__dbl_Class40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_SuperClassSpecification41"):
                    opp_val = getattr(item, "dbl_SuperClassSpecification41", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_SuperClassSpecification41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_SuperClassSpecification41"):
                    opp_val = getattr(item, "dbl_SuperClassSpecification41", None)
                    
                    setattr(item, "dbl_SuperClassSpecification41", self)
                    

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
                    

    @property
    def dbl_Class47(self):
        return self.__dbl_Class47

    @dbl_Class47.setter
    def dbl_Class47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Class__dbl_Class47", None)
        self.__dbl_Class47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbl_Function48"):
                    opp_val = getattr(item, "dbl_Function48", None)
                    
                    if opp_val == self:
                        setattr(item, "dbl_Function48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbl_Function48"):
                    opp_val = getattr(item, "dbl_Function48", None)
                    
                    setattr(item, "dbl_Function48", self)
                    

class dbl_Module(ConstructiveExtensionAtContentExtensionPoint, Construct, NamedElement):

    pass
class dbl_Import:

    def __init__(self, file: str, dbl_Import: "dbl_Model" = None, dbl_Import5: "dbl_Model" = None):
        self.file = file
        self.dbl_Import = dbl_Import
        self.dbl_Import5 = dbl_Import5
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def dbl_Import5(self):
        return self.__dbl_Import5

    @dbl_Import5.setter
    def dbl_Import5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Import__dbl_Import5", None)
        self.__dbl_Import5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Model6"):
                opp_val = getattr(old_value, "dbl_Model6", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Model6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Model6"):
                opp_val = getattr(value, "dbl_Model6", None)
                setattr(value, "dbl_Model6", self)

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

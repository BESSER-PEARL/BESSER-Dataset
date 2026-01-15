from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Module:

    pass
class QuotedCode:

    pass
class dbl_QuotedModuleContent(QuotedCode, Module):

    pass
class dbl_QuotedStatements(QuotedCode):

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

class dbl_MappingPart(ABC):

    pass
class LocalScopeStatement:

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
class dbl_BooleanPropertyType(PropertyType):

    def __init__(self, terminal: str):
        self.terminal = terminal
        
    @property
    def terminal(self) -> str:
        return self.__terminal

    @terminal.setter
    def terminal(self, terminal: str):
        self.__terminal = terminal

class dbl_StructuredPropertyType(PropertyType):

    pass
class dbl_IntPropertyType(PropertyType):

    pass
class dbl_StringPropertyType(PropertyType):

    pass
class dbl_IdPropertyType(PropertyType):

    pass
class dbl_PropertyType(ABC):

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
class dbl_L2RhsExpr(RhsExpression):

    pass
class dbl_L1RhsExpr(RhsExpression):

    pass
class dbl_L3RhsExpr(RhsExpression):

    pass
class dbl_RhsExpression:

    pass
class LanguageConstructClassifier:

    pass
class dbl_Mapping(LocalScopeStatement):

    pass
class dbl_LanguageConceptClassifier(LanguageConstructClassifier):

    pass
class VariableAccess:

    pass
class dbl_MetaAccess(VariableAccess):

    pass
class ElementAccess:

    pass
class dbl_TypeAccess(ElementAccess):

    pass
class L2Expr:

    pass
class dbl_CallPart:

    pass
class PredefinedId:

    pass
class dbl_MetaLiteral(PredefinedId):

    pass
class dbl_SizeOfArray(PredefinedId):

    pass
class dbl_SuperLiteral(PredefinedId):

    pass
class dbl_TypeLiteral(PredefinedId):

    pass
class dbl_MeLiteral(PredefinedId):

    pass
class dbl_PredefinedId:

    pass
class UnaryOperator:

    pass
class dbl_Neg(UnaryOperator, L2Expr):

    pass
class L3Expr:

    pass
class L4Expr:

    pass
class L1Expr:

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

class dbl_TimeLiteral(L1Expr):

    pass
class dbl_ActiveLiteral(L1Expr):

    pass
class dbl_TrueLiteral(L1Expr):

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

class dbl_FalseLiteral(L1Expr):

    pass
class dbl_NullLiteral(L1Expr):

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

class L5Expr:

    pass
class L6Expr:

    pass
class dbl_Not(UnaryOperator, L2Expr):

    pass
class L7Expr:

    pass
class L8Expr:

    pass
class Expression:

    pass
class dbl_MetaExpr(Expression):

    pass
class dbl_L2Expr(Expression):

    pass
class dbl_ExpandExpression(Expression):

    pass
class dbl_ElementAccess(Expression):

    pass
class dbl_ParseExpr(Expression):

    pass
class dbl_CodeQuoteExpression(Expression):

    pass
class dbl_L1Expr(Expression):

    pass
class dbl_SwitchCase:

    pass
class BinaryOperator:

    pass
class dbl_Less(L5Expr, BinaryOperator):

    pass
class dbl_And(L7Expr, BinaryOperator):

    pass
class dbl_Div(L3Expr, BinaryOperator):

    pass
class dbl_Plus(L4Expr, BinaryOperator):

    pass
class dbl_Mul(L3Expr, BinaryOperator):

    pass
class dbl_Mod(L3Expr, BinaryOperator):

    pass
class dbl_Minus(L4Expr, BinaryOperator):

    pass
class dbl_InstanceOf(L5Expr, BinaryOperator):

    pass
class dbl_Greater(L5Expr, BinaryOperator):

    pass
class dbl_Equal(L6Expr, BinaryOperator):

    pass
class dbl_LessEqual(L5Expr, BinaryOperator):

    pass
class dbl_GreaterEqual(L5Expr, BinaryOperator):

    pass
class dbl_NotEqual(L6Expr, BinaryOperator):

    pass
class dbl_Or(L8Expr, BinaryOperator):

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
class dbl_L5Expr(Expression):

    pass
class dbl_L4Expr(Expression):

    pass
class dbl_L3Expr(Expression):

    pass
class LoopStatement:

    pass
class dbl_WhileStatement(LoopStatement):

    pass
class dbl_LocalScope:

    pass
class SimpleStatement:

    pass
class dbl_BreakStatement(SimpleStatement):

    pass
class dbl_SaveGenStatement(SimpleStatement):

    pass
class dbl_ResumeGenStatement(SimpleStatement):

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
            if hasattr(old_value, "dbl_Expression83"):
                opp_val = getattr(old_value, "dbl_Expression83", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression83"):
                opp_val = getattr(value, "dbl_Expression83", None)
                setattr(value, "dbl_Expression83", self)

class dbl_SwitchStatement(SimpleStatement):

    pass
class dbl_Reactivate(SimpleStatement):

    pass
class dbl_Yield(SimpleStatement):

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
            if hasattr(old_value, "dbl_Expression189"):
                opp_val = getattr(old_value, "dbl_Expression189", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression189"):
                opp_val = getattr(value, "dbl_Expression189", None)
                setattr(value, "dbl_Expression189", self)

class dbl_Wait(SimpleStatement):

    pass
class dbl_Print(SimpleStatement):

    pass
class dbl_WaitUntil(SimpleStatement):

    pass
class dbl_Terminate(SimpleStatement):

    pass
class dbl_ResetGenContextStatement(SimpleStatement):

    pass
class dbl_ContinueStatement(SimpleStatement):

    pass
class dbl_Advance(SimpleStatement):

    pass
class AbstractVariable:

    pass
class dbl_Constructor:

    pass
class LanguageConceptClassifier:

    pass
class ClassSimilar:

    pass
class dbl_QuotedClassContent(ClassSimilar, QuotedCode):

    pass
class Classifier:

    pass
class dbl_Return(SimpleStatement):

    pass
class dbl_ProcedureCall(SimpleStatement):

    pass
class dbl_VariableAccess(ElementAccess):

    pass
class dbl_Assignment(SimpleStatement):

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

class dbl_ExpandStatement(Statement):

    pass
class dbl_IfStatement(Statement):

    pass
class dbl_SimpleStatement(Statement):

    pass
class dbl_TargetStatement(Statement):

    pass
class dbl_MappingStatement(Statement):

    pass
class dbl_LoopStatement(Statement):

    pass
class ExtensibleElement:

    pass
class dbl_TextualSyntaxDef(ExtensibleElement):

    pass
class dbl_ClassContentExtension(ExtensibleElement):

    pass
class dbl_ModuleContentExtension(ExtensibleElement):

    pass
class dbl_Statement(ExtensibleElement):

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
            if hasattr(old_value, "dbl_IdExpr139"):
                opp_val = getattr(old_value, "dbl_IdExpr139", None)
                if opp_val == self:
                    setattr(old_value, "dbl_IdExpr139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_IdExpr139"):
                opp_val = getattr(value, "dbl_IdExpr139", None)
                setattr(value, "dbl_IdExpr139", self)

class dbl_SuperClassSpecification:

    pass
class PrimitiveType:

    pass
class dbl_IntType(PrimitiveType):

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

    pass
class dbl_ArrayDimension:

    pass
class dbl_Type(ABC):

    pass
class dbl_ModifierExtensionsContainer(ABC):

    pass
class dbl_EmbeddableExtensionsContainer(ABC):

    pass
class ModifierExtensionsContainer:

    pass
class dbl_NativeBinding:

    def __init__(self, targetLanguage: str, targetType: str, dbl_NativeBinding: "dbl_Clazz" = None):
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
            if hasattr(old_value, "dbl_Clazz60"):
                opp_val = getattr(old_value, "dbl_Clazz60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Clazz60"):
                opp_val = getattr(value, "dbl_Clazz60", None)
                if opp_val is None:
                    setattr(value, "dbl_Clazz60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbl_Parameter(AbstractVariable):

    pass
class LocalScope:

    pass
class dbl_LocalScopeStatement(LocalScope, SimpleStatement):

    pass
class dbl_ForStatement(LocalScope, LoopStatement):

    pass
class dbl_ClassPart(LocalScope):

    pass
class TypedElement:

    pass
class dbl_CreateObject(TypedElement, L1Expr):

    pass
class dbl_Expression(TypedElement, ExtensibleElement):

    pass
class dbl_Cast(TypedElement, UnaryOperator, L2Expr):

    pass
class dbl_StringType(PrimitiveType):

    pass
class dbl_DoubleType(PrimitiveType):

    pass
class dbl_BoolType(PrimitiveType):

    pass
class dbl_Import:

    def __init__(self, file: str, dbl_Import5: "dbl_Model" = None, dbl_Import: "dbl_Model" = None):
        self.file = file
        self.dbl_Import5 = dbl_Import5
        self.dbl_Import = dbl_Import
        
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

class dbl_Model:

    pass
class Construct:

    pass
class dbl_Clazz(LanguageConceptClassifier, Construct, ClassSimilar, Classifier):

    def __init__(self, active: bool, dbl_Clazz: "dbl_SuperClassSpecification" = None, dbl_Clazz58: "dbl_Constructor" = None, dbl_Clazz60: set["dbl_NativeBinding"] = None, dbl_Clazz66: "dbl_ClassAugment" = None):
        self.active = active
        self.dbl_Clazz = dbl_Clazz
        self.dbl_Clazz58 = dbl_Clazz58
        self.dbl_Clazz60 = dbl_Clazz60 if dbl_Clazz60 is not None else set()
        self.dbl_Clazz66 = dbl_Clazz66
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def dbl_Clazz66(self):
        return self.__dbl_Clazz66

    @dbl_Clazz66.setter
    def dbl_Clazz66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Clazz__dbl_Clazz66", None)
        self.__dbl_Clazz66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ClassAugment65"):
                opp_val = getattr(old_value, "dbl_ClassAugment65", None)
                if opp_val == self:
                    setattr(old_value, "dbl_ClassAugment65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ClassAugment65"):
                opp_val = getattr(value, "dbl_ClassAugment65", None)
                setattr(value, "dbl_ClassAugment65", self)

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
            if hasattr(old_value, "dbl_SuperClassSpecification53"):
                opp_val = getattr(old_value, "dbl_SuperClassSpecification53", None)
                if opp_val == self:
                    setattr(old_value, "dbl_SuperClassSpecification53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_SuperClassSpecification53"):
                opp_val = getattr(value, "dbl_SuperClassSpecification53", None)
                setattr(value, "dbl_SuperClassSpecification53", self)

    @property
    def dbl_Clazz58(self):
        return self.__dbl_Clazz58

    @dbl_Clazz58.setter
    def dbl_Clazz58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Clazz__dbl_Clazz58", None)
        self.__dbl_Clazz58 = value
        
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
    def dbl_Clazz60(self):
        return self.__dbl_Clazz60

    @dbl_Clazz60.setter
    def dbl_Clazz60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Clazz__dbl_Clazz60", None)
        self.__dbl_Clazz60 = value if value is not None else set()
        
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
                    

class NamedElement:

    pass
class dbl_AbstractVariable(TypedElement, NamedElement):

    pass
class dbl_TsRule(LanguageConstructClassifier, NamedElement):

    pass
class dbl_Pattern(NamedElement):

    def __init__(self, top: bool, dbl_Pattern: "dbl_Parameter" = None, dbl_Pattern211: "dbl_Statement" = None):
        self.top = top
        self.dbl_Pattern = dbl_Pattern
        self.dbl_Pattern211 = dbl_Pattern211
        
    @property
    def top(self) -> bool:
        return self.__top

    @top.setter
    def top(self, top: bool):
        self.__top = top

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
            if hasattr(old_value, "dbl_Parameter209"):
                opp_val = getattr(old_value, "dbl_Parameter209", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Parameter209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Parameter209"):
                opp_val = getattr(value, "dbl_Parameter209", None)
                setattr(value, "dbl_Parameter209", self)

    @property
    def dbl_Pattern211(self):
        return self.__dbl_Pattern211

    @dbl_Pattern211.setter
    def dbl_Pattern211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Pattern__dbl_Pattern211", None)
        self.__dbl_Pattern211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Statement212"):
                opp_val = getattr(old_value, "dbl_Statement212", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Statement212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Statement212"):
                opp_val = getattr(value, "dbl_Statement212", None)
                setattr(value, "dbl_Statement212", self)

class dbl_PropertyBindingExpr(L1RhsExpr, NamedElement):

    pass
class dbl_LanguageConstructClassifier(ExtensibleElement, NamedElement):

    pass
class dbl_ExtensibleElement(Construct, NamedElement):

    def __init__(self, concreteSyntax: str, instanceOfExtensionDefinition: bool, dbl_ExtensibleElement: "dbl_EmbeddableExtensionsContainer" = None, dbl_ExtensibleElement19: "dbl_ModifierExtensionsContainer" = None):
        self.concreteSyntax = concreteSyntax
        self.instanceOfExtensionDefinition = instanceOfExtensionDefinition
        self.dbl_ExtensibleElement = dbl_ExtensibleElement
        self.dbl_ExtensibleElement19 = dbl_ExtensibleElement19
        
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
    def dbl_ExtensibleElement19(self):
        return self.__dbl_ExtensibleElement19

    @dbl_ExtensibleElement19.setter
    def dbl_ExtensibleElement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_ExtensibleElement__dbl_ExtensibleElement19", None)
        self.__dbl_ExtensibleElement19 = value
        
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

class dbl_ExpandExpr(Expression):

    pass
class dbl_Construct:

    pass
class dbl_Variable(ModifierExtensionsContainer, AbstractVariable, SimpleStatement):

    def __init__(self, control: bool, clazz: bool, dbl_Variable32: "dbl_ClassSimilar" = None, dbl_Variable: "dbl_Module" = None, dbl_Variable68: "dbl_Expression" = None):
        self.control = control
        self.clazz = clazz
        self.dbl_Variable32 = dbl_Variable32
        self.dbl_Variable = dbl_Variable
        self.dbl_Variable68 = dbl_Variable68
        
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
    def dbl_Variable68(self):
        return self.__dbl_Variable68

    @dbl_Variable68.setter
    def dbl_Variable68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Variable__dbl_Variable68", None)
        self.__dbl_Variable68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_Expression69"):
                opp_val = getattr(old_value, "dbl_Expression69", None)
                if opp_val == self:
                    setattr(old_value, "dbl_Expression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_Expression69"):
                opp_val = getattr(value, "dbl_Expression69", None)
                setattr(value, "dbl_Expression69", self)

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

class dbl_Procedure(TypedElement, LocalScope, NamedElement):

    def __init__(self, clazz: bool, abstract: bool, dbl_Procedure: "dbl_Module" = None, dbl_Procedure30: set["dbl_Parameter"] = None, dbl_Procedure35: "dbl_ClassSimilar" = None):
        self.clazz = clazz
        self.abstract = abstract
        self.dbl_Procedure = dbl_Procedure
        self.dbl_Procedure30 = dbl_Procedure30 if dbl_Procedure30 is not None else set()
        self.dbl_Procedure35 = dbl_Procedure35
        
    @property
    def clazz(self) -> bool:
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: bool):
        self.__clazz = clazz

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def dbl_Procedure35(self):
        return self.__dbl_Procedure35

    @dbl_Procedure35.setter
    def dbl_Procedure35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Procedure__dbl_Procedure35", None)
        self.__dbl_Procedure35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbl_ClassSimilar34"):
                opp_val = getattr(old_value, "dbl_ClassSimilar34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbl_ClassSimilar34"):
                opp_val = getattr(value, "dbl_ClassSimilar34", None)
                if opp_val is None:
                    setattr(value, "dbl_ClassSimilar34", set([self]))
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
    def dbl_Procedure30(self):
        return self.__dbl_Procedure30

    @dbl_Procedure30.setter
    def dbl_Procedure30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbl_Procedure__dbl_Procedure30", None)
        self.__dbl_Procedure30 = value if value is not None else set()
        
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
                    

class dbl_ExtensionDefinition(ExtensibleElement, LanguageConceptClassifier):

    pass
class dbl_ClassAugment(ClassSimilar):

    pass
class dbl_Classifier(Type, NamedElement):

    pass
class EmbeddableExtensionsContainer:

    pass
class dbl_ClassSimilar(ModifierExtensionsContainer, EmbeddableExtensionsContainer):

    pass
class dbl_Module(EmbeddableExtensionsContainer, Construct, NamedElement):

    pass
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Module,
    Class,
    QuotedCode,
    dbl_QuotedStatements,
    dbl_QuotedClassContent,
    dbl_QuotedModuleContent,
    dbl_QuotedExpression,
    dbl_QuotedCode,
    ExpansionPart,
    dbl_ExpandVariablePart,
    dbl_ExpandTextPart,
    dbl_ExpansionPart,
    Variable,
    dbl_CreateIdStatement,
    ElementarySymbol,
    dbl_IntSymbol,
    dbl_StringSymbol,
    dbl_Keyword,
    dbl_IdSymbol,
    PlainSymbolReference,
    L2SyntaxExpression,
    dbl_SymbolSequence,
    SyntaxExpression,
    dbl_L1SyntaxExpression,
    dbl_L2SyntaxExpression,
    dbl_L3SyntaxExpression,
    dbl_SyntaxExpression,
    ComplexSymbol,
    SyntaxSymbolClassifier,
    dbl_ElementarySymbol,
    dbl_ComplexSymbol,
    L1SyntaxExpression,
    dbl_PlainSymbolReference,
    dbl_CallPart,
    Annotation,
    PredefinedId,
    dbl_AnnotationLiteral,
    dbl_MetaLiteral,
    dbl_TypeLiteral,
    dbl_SizeOfArray,
    dbl_SuperLiteral,
    dbl_MeLiteral,
    dbl_PredefinedId,
    dbl_Concept,
    VariableAccess,
    dbl_MetaAccess,
    ElementAccess,
    dbl_TypeAccess,
    L1Expr,
    dbl_TimeLiteral,
    dbl_NullLiteral,
    dbl_ActiveLiteral,
    L2Expr,
    UnaryOperator,
    dbl_Not,
    dbl_Neg,
    L3Expr,
    L4Expr,
    L5Expr,
    L6Expr,
    L7Expr,
    L8Expr,
    BinaryOperator,
    dbl_LessEqual,
    dbl_Equal,
    dbl_Less,
    dbl_GreaterEqual,
    dbl_InstanceOf,
    dbl_And,
    dbl_Div,
    dbl_Mod,
    dbl_NotEqual,
    dbl_Mul,
    dbl_Minus,
    dbl_Plus,
    dbl_Greater,
    dbl_Or,
    dbl_DoubleLiteral,
    dbl_FalseLiteral,
    dbl_TrueLiteral,
    dbl_IntLiteral,
    dbl_StringLiteral,
    Expression,
    dbl_ParseExpr,
    dbl_L3Expr,
    dbl_CodeQuoteExpression,
    dbl_ElementAccess,
    dbl_L4Expr,
    dbl_UnaryOperator,
    dbl_MetaExpr,
    dbl_ExpandExpression,
    dbl_L5Expr,
    dbl_L2Expr,
    dbl_L6Expr,
    dbl_L1Expr,
    dbl_SwitchCase,
    LoopStatement,
    dbl_WhileStatement,
    dbl_BinaryOperator,
    dbl_L9Expr,
    dbl_L8Expr,
    dbl_L7Expr,
    dbl_VariableAccess,
    SimpleStatement,
    dbl_BreakStatement,
    dbl_Advance,
    dbl_ExpansionStatement,
    dbl_Print,
    dbl_WaitUntil,
    dbl_Return,
    dbl_TargetStatement,
    dbl_ContinueStatement,
    dbl_Reactivate,
    dbl_SwitchStatement,
    dbl_Terminate,
    dbl_Yield,
    dbl_FunctionCall,
    dbl_ActivateObject,
    dbl_Wait,
    AbstractVariable,
    dbl_LocalScope,
    AnnotateableElement,
    dbl_Assignment,
    Statement,
    dbl_TestStatement,
    dbl_ExpandStatement,
    dbl_IfStatement,
    dbl_SimpleStatement,
    dbl_LoopStatement,
    dbl_NamedElement,
    dbl_NativeBinding,
    dbl_Parameter,
    LocalScope,
    dbl_ForStatement,
    dbl_LocalScopeStatement,
    dbl_Constructor,
    TypedElement,
    dbl_Cast,
    dbl_CreateObject,
    PrimitiveType,
    dbl_IntType,
    dbl_DoubleType,
    dbl_BoolType,
    dbl_StringType,
    dbl_VoidType,
    Type,
    dbl_IdExpr,
    dbl_PrimitiveType,
    dbl_TypedElement,
    dbl_ArrayDimension,
    dbl_Type,
    ConstructiveExtension,
    dbl_ClassContentExtension,
    dbl_ModuleContentExtension,
    Concept,
    dbl_SuperClassSpecification,
    dbl_AnnotationItem,
    dbl_Variable,
    ConstructiveExtensionAtContentExtensionPoint,
    dbl_Import,
    dbl_Model,
    Construct,
    NamedElement,
    dbl_AbstractVariable,
    dbl_StructuralSymbolReference,
    dbl_Annotation,
    dbl_Function,
    dbl_Module,
    dbl_Pattern,
    dbl_MetaSymbol,
    dbl_Class,
    dbl_ExtensibleElement,
    dbl_ExpandExpr,
    dbl_Construct,
    dbl_ConstructiveExtensionAtContentExtensionPoint,
    ExtensibleElement,
    dbl_Expression,
    dbl_SyntaxDefinition,
    dbl_ExtensionSemantics,
    dbl_Statement,
    dbl_SyntaxSymbolClassifier,
    dbl_Extension,
    dbl_ConstructiveExtension,
    dbl_AnnotateableElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_quotedcode_is_not_abstract():
    assert not inspect.isabstract(QuotedCode)


def test_quotedcode_constructor_exists():
    assert callable(QuotedCode.__init__)


def test_quotedcode_constructor_args():
    sig = inspect.signature(QuotedCode.__init__)
    params = list(sig.parameters.keys())



def test_dbl_quotedstatements_is_not_abstract():
    assert not inspect.isabstract(dbl_QuotedStatements)


def test_dbl_quotedstatements_constructor_exists():
    assert callable(dbl_QuotedStatements.__init__)


def test_dbl_quotedstatements_constructor_args():
    sig = inspect.signature(dbl_QuotedStatements.__init__)
    params = list(sig.parameters.keys())



def test_dbl_quotedclasscontent_is_not_abstract():
    assert not inspect.isabstract(dbl_QuotedClassContent)


def test_dbl_quotedclasscontent_constructor_exists():
    assert callable(dbl_QuotedClassContent.__init__)


def test_dbl_quotedclasscontent_constructor_args():
    sig = inspect.signature(dbl_QuotedClassContent.__init__)
    params = list(sig.parameters.keys())



def test_dbl_quotedmodulecontent_is_not_abstract():
    assert not inspect.isabstract(dbl_QuotedModuleContent)


def test_dbl_quotedmodulecontent_constructor_exists():
    assert callable(dbl_QuotedModuleContent.__init__)


def test_dbl_quotedmodulecontent_constructor_args():
    sig = inspect.signature(dbl_QuotedModuleContent.__init__)
    params = list(sig.parameters.keys())



def test_dbl_quotedexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_QuotedExpression)


def test_dbl_quotedexpression_constructor_exists():
    assert callable(dbl_QuotedExpression.__init__)


def test_dbl_quotedexpression_constructor_args():
    sig = inspect.signature(dbl_QuotedExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_quotedcode_is_not_abstract():
    assert not inspect.isabstract(dbl_QuotedCode)


def test_dbl_quotedcode_constructor_exists():
    assert callable(dbl_QuotedCode.__init__)


def test_dbl_quotedcode_constructor_args():
    sig = inspect.signature(dbl_QuotedCode.__init__)
    params = list(sig.parameters.keys())



def test_expansionpart_is_not_abstract():
    assert not inspect.isabstract(ExpansionPart)


def test_expansionpart_constructor_exists():
    assert callable(ExpansionPart.__init__)


def test_expansionpart_constructor_args():
    sig = inspect.signature(ExpansionPart.__init__)
    params = list(sig.parameters.keys())



def test_dbl_expandvariablepart_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpandVariablePart)


def test_dbl_expandvariablepart_constructor_exists():
    assert callable(dbl_ExpandVariablePart.__init__)


def test_dbl_expandvariablepart_constructor_args():
    sig = inspect.signature(dbl_ExpandVariablePart.__init__)
    params = list(sig.parameters.keys())



def test_dbl_expandtextpart_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpandTextPart)


def test_dbl_expandtextpart_constructor_exists():
    assert callable(dbl_ExpandTextPart.__init__)


def test_dbl_expandtextpart_constructor_args():
    sig = inspect.signature(dbl_ExpandTextPart.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_dbl_expandtextpart_has_text():
    assert hasattr(dbl_ExpandTextPart, "text")
    descriptor = None
    for klass in dbl_ExpandTextPart.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_dbl_expansionpart_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpansionPart)


def test_dbl_expansionpart_constructor_exists():
    assert callable(dbl_ExpansionPart.__init__)


def test_dbl_expansionpart_constructor_args():
    sig = inspect.signature(dbl_ExpansionPart.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_dbl_createidstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_CreateIdStatement)


def test_dbl_createidstatement_constructor_exists():
    assert callable(dbl_CreateIdStatement.__init__)


def test_dbl_createidstatement_constructor_args():
    sig = inspect.signature(dbl_CreateIdStatement.__init__)
    params = list(sig.parameters.keys())



def test_elementarysymbol_is_not_abstract():
    assert not inspect.isabstract(ElementarySymbol)


def test_elementarysymbol_constructor_exists():
    assert callable(ElementarySymbol.__init__)


def test_elementarysymbol_constructor_args():
    sig = inspect.signature(ElementarySymbol.__init__)
    params = list(sig.parameters.keys())



def test_dbl_intsymbol_is_not_abstract():
    assert not inspect.isabstract(dbl_IntSymbol)


def test_dbl_intsymbol_constructor_exists():
    assert callable(dbl_IntSymbol.__init__)


def test_dbl_intsymbol_constructor_args():
    sig = inspect.signature(dbl_IntSymbol.__init__)
    params = list(sig.parameters.keys())



def test_dbl_stringsymbol_is_not_abstract():
    assert not inspect.isabstract(dbl_StringSymbol)


def test_dbl_stringsymbol_constructor_exists():
    assert callable(dbl_StringSymbol.__init__)


def test_dbl_stringsymbol_constructor_args():
    sig = inspect.signature(dbl_StringSymbol.__init__)
    params = list(sig.parameters.keys())



def test_dbl_keyword_is_not_abstract():
    assert not inspect.isabstract(dbl_Keyword)


def test_dbl_keyword_constructor_exists():
    assert callable(dbl_Keyword.__init__)


def test_dbl_keyword_constructor_args():
    sig = inspect.signature(dbl_Keyword.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_dbl_keyword_has_keyword():
    assert hasattr(dbl_Keyword, "keyword")
    descriptor = None
    for klass in dbl_Keyword.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_dbl_idsymbol_is_not_abstract():
    assert not inspect.isabstract(dbl_IdSymbol)


def test_dbl_idsymbol_constructor_exists():
    assert callable(dbl_IdSymbol.__init__)


def test_dbl_idsymbol_constructor_args():
    sig = inspect.signature(dbl_IdSymbol.__init__)
    params = list(sig.parameters.keys())



def test_plainsymbolreference_is_not_abstract():
    assert not inspect.isabstract(PlainSymbolReference)


def test_plainsymbolreference_constructor_exists():
    assert callable(PlainSymbolReference.__init__)


def test_plainsymbolreference_constructor_args():
    sig = inspect.signature(PlainSymbolReference.__init__)
    params = list(sig.parameters.keys())



def test_l2syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(L2SyntaxExpression)


def test_l2syntaxexpression_constructor_exists():
    assert callable(L2SyntaxExpression.__init__)


def test_l2syntaxexpression_constructor_args():
    sig = inspect.signature(L2SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_symbolsequence_is_not_abstract():
    assert not inspect.isabstract(dbl_SymbolSequence)


def test_dbl_symbolsequence_constructor_exists():
    assert callable(dbl_SymbolSequence.__init__)


def test_dbl_symbolsequence_constructor_args():
    sig = inspect.signature(dbl_SymbolSequence.__init__)
    params = list(sig.parameters.keys())



def test_syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(SyntaxExpression)


def test_syntaxexpression_constructor_exists():
    assert callable(SyntaxExpression.__init__)


def test_syntaxexpression_constructor_args():
    sig = inspect.signature(SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l1syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_L1SyntaxExpression)


def test_dbl_l1syntaxexpression_constructor_exists():
    assert callable(dbl_L1SyntaxExpression.__init__)


def test_dbl_l1syntaxexpression_constructor_args():
    sig = inspect.signature(dbl_L1SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l2syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_L2SyntaxExpression)


def test_dbl_l2syntaxexpression_constructor_exists():
    assert callable(dbl_L2SyntaxExpression.__init__)


def test_dbl_l2syntaxexpression_constructor_args():
    sig = inspect.signature(dbl_L2SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l3syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_L3SyntaxExpression)


def test_dbl_l3syntaxexpression_constructor_exists():
    assert callable(dbl_L3SyntaxExpression.__init__)


def test_dbl_l3syntaxexpression_constructor_args():
    sig = inspect.signature(dbl_L3SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_SyntaxExpression)


def test_dbl_syntaxexpression_constructor_exists():
    assert callable(dbl_SyntaxExpression.__init__)


def test_dbl_syntaxexpression_constructor_args():
    sig = inspect.signature(dbl_SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_complexsymbol_is_not_abstract():
    assert not inspect.isabstract(ComplexSymbol)


def test_complexsymbol_constructor_exists():
    assert callable(ComplexSymbol.__init__)


def test_complexsymbol_constructor_args():
    sig = inspect.signature(ComplexSymbol.__init__)
    params = list(sig.parameters.keys())



def test_syntaxsymbolclassifier_is_not_abstract():
    assert not inspect.isabstract(SyntaxSymbolClassifier)


def test_syntaxsymbolclassifier_constructor_exists():
    assert callable(SyntaxSymbolClassifier.__init__)


def test_syntaxsymbolclassifier_constructor_args():
    sig = inspect.signature(SyntaxSymbolClassifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl_elementarysymbol_is_not_abstract():
    assert not inspect.isabstract(dbl_ElementarySymbol)


def test_dbl_elementarysymbol_constructor_exists():
    assert callable(dbl_ElementarySymbol.__init__)


def test_dbl_elementarysymbol_constructor_args():
    sig = inspect.signature(dbl_ElementarySymbol.__init__)
    params = list(sig.parameters.keys())



def test_dbl_complexsymbol_is_not_abstract():
    assert not inspect.isabstract(dbl_ComplexSymbol)


def test_dbl_complexsymbol_constructor_exists():
    assert callable(dbl_ComplexSymbol.__init__)


def test_dbl_complexsymbol_constructor_args():
    sig = inspect.signature(dbl_ComplexSymbol.__init__)
    params = list(sig.parameters.keys())



def test_l1syntaxexpression_is_not_abstract():
    assert not inspect.isabstract(L1SyntaxExpression)


def test_l1syntaxexpression_constructor_exists():
    assert callable(L1SyntaxExpression.__init__)


def test_l1syntaxexpression_constructor_args():
    sig = inspect.signature(L1SyntaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_plainsymbolreference_is_not_abstract():
    assert not inspect.isabstract(dbl_PlainSymbolReference)


def test_dbl_plainsymbolreference_constructor_exists():
    assert callable(dbl_PlainSymbolReference.__init__)


def test_dbl_plainsymbolreference_constructor_args():
    sig = inspect.signature(dbl_PlainSymbolReference.__init__)
    params = list(sig.parameters.keys())



def test_dbl_callpart_is_not_abstract():
    assert not inspect.isabstract(dbl_CallPart)


def test_dbl_callpart_constructor_exists():
    assert callable(dbl_CallPart.__init__)


def test_dbl_callpart_constructor_args():
    sig = inspect.signature(dbl_CallPart.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_predefinedid_is_not_abstract():
    assert not inspect.isabstract(PredefinedId)


def test_predefinedid_constructor_exists():
    assert callable(PredefinedId.__init__)


def test_predefinedid_constructor_args():
    sig = inspect.signature(PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_dbl_annotationliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_AnnotationLiteral)


def test_dbl_annotationliteral_constructor_exists():
    assert callable(dbl_AnnotationLiteral.__init__)


def test_dbl_annotationliteral_constructor_args():
    sig = inspect.signature(dbl_AnnotationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_metaliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_MetaLiteral)


def test_dbl_metaliteral_constructor_exists():
    assert callable(dbl_MetaLiteral.__init__)


def test_dbl_metaliteral_constructor_args():
    sig = inspect.signature(dbl_MetaLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_typeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_TypeLiteral)


def test_dbl_typeliteral_constructor_exists():
    assert callable(dbl_TypeLiteral.__init__)


def test_dbl_typeliteral_constructor_args():
    sig = inspect.signature(dbl_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_sizeofarray_is_not_abstract():
    assert not inspect.isabstract(dbl_SizeOfArray)


def test_dbl_sizeofarray_constructor_exists():
    assert callable(dbl_SizeOfArray.__init__)


def test_dbl_sizeofarray_constructor_args():
    sig = inspect.signature(dbl_SizeOfArray.__init__)
    params = list(sig.parameters.keys())



def test_dbl_superliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_SuperLiteral)


def test_dbl_superliteral_constructor_exists():
    assert callable(dbl_SuperLiteral.__init__)


def test_dbl_superliteral_constructor_args():
    sig = inspect.signature(dbl_SuperLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_meliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_MeLiteral)


def test_dbl_meliteral_constructor_exists():
    assert callable(dbl_MeLiteral.__init__)


def test_dbl_meliteral_constructor_args():
    sig = inspect.signature(dbl_MeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_predefinedid_is_not_abstract():
    assert not inspect.isabstract(dbl_PredefinedId)


def test_dbl_predefinedid_constructor_exists():
    assert callable(dbl_PredefinedId.__init__)


def test_dbl_predefinedid_constructor_args():
    sig = inspect.signature(dbl_PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_dbl_concept_is_not_abstract():
    assert not inspect.isabstract(dbl_Concept)


def test_dbl_concept_constructor_exists():
    assert callable(dbl_Concept.__init__)


def test_dbl_concept_constructor_args():
    sig = inspect.signature(dbl_Concept.__init__)
    params = list(sig.parameters.keys())



def test_variableaccess_is_not_abstract():
    assert not inspect.isabstract(VariableAccess)


def test_variableaccess_constructor_exists():
    assert callable(VariableAccess.__init__)


def test_variableaccess_constructor_args():
    sig = inspect.signature(VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl_metaaccess_is_not_abstract():
    assert not inspect.isabstract(dbl_MetaAccess)


def test_dbl_metaaccess_constructor_exists():
    assert callable(dbl_MetaAccess.__init__)


def test_dbl_metaaccess_constructor_args():
    sig = inspect.signature(dbl_MetaAccess.__init__)
    params = list(sig.parameters.keys())



def test_elementaccess_is_not_abstract():
    assert not inspect.isabstract(ElementAccess)


def test_elementaccess_constructor_exists():
    assert callable(ElementAccess.__init__)


def test_elementaccess_constructor_args():
    sig = inspect.signature(ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl_typeaccess_is_not_abstract():
    assert not inspect.isabstract(dbl_TypeAccess)


def test_dbl_typeaccess_constructor_exists():
    assert callable(dbl_TypeAccess.__init__)


def test_dbl_typeaccess_constructor_args():
    sig = inspect.signature(dbl_TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_l1expr_is_not_abstract():
    assert not inspect.isabstract(L1Expr)


def test_l1expr_constructor_exists():
    assert callable(L1Expr.__init__)


def test_l1expr_constructor_args():
    sig = inspect.signature(L1Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_timeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_TimeLiteral)


def test_dbl_timeliteral_constructor_exists():
    assert callable(dbl_TimeLiteral.__init__)


def test_dbl_timeliteral_constructor_args():
    sig = inspect.signature(dbl_TimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_nullliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_NullLiteral)


def test_dbl_nullliteral_constructor_exists():
    assert callable(dbl_NullLiteral.__init__)


def test_dbl_nullliteral_constructor_args():
    sig = inspect.signature(dbl_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_activeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_ActiveLiteral)


def test_dbl_activeliteral_constructor_exists():
    assert callable(dbl_ActiveLiteral.__init__)


def test_dbl_activeliteral_constructor_args():
    sig = inspect.signature(dbl_ActiveLiteral.__init__)
    params = list(sig.parameters.keys())



def test_l2expr_is_not_abstract():
    assert not inspect.isabstract(L2Expr)


def test_l2expr_constructor_exists():
    assert callable(L2Expr.__init__)


def test_l2expr_constructor_args():
    sig = inspect.signature(L2Expr.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl_not_is_not_abstract():
    assert not inspect.isabstract(dbl_Not)


def test_dbl_not_constructor_exists():
    assert callable(dbl_Not.__init__)


def test_dbl_not_constructor_args():
    sig = inspect.signature(dbl_Not.__init__)
    params = list(sig.parameters.keys())



def test_dbl_neg_is_not_abstract():
    assert not inspect.isabstract(dbl_Neg)


def test_dbl_neg_constructor_exists():
    assert callable(dbl_Neg.__init__)


def test_dbl_neg_constructor_args():
    sig = inspect.signature(dbl_Neg.__init__)
    params = list(sig.parameters.keys())



def test_l3expr_is_not_abstract():
    assert not inspect.isabstract(L3Expr)


def test_l3expr_constructor_exists():
    assert callable(L3Expr.__init__)


def test_l3expr_constructor_args():
    sig = inspect.signature(L3Expr.__init__)
    params = list(sig.parameters.keys())



def test_l4expr_is_not_abstract():
    assert not inspect.isabstract(L4Expr)


def test_l4expr_constructor_exists():
    assert callable(L4Expr.__init__)


def test_l4expr_constructor_args():
    sig = inspect.signature(L4Expr.__init__)
    params = list(sig.parameters.keys())



def test_l5expr_is_not_abstract():
    assert not inspect.isabstract(L5Expr)


def test_l5expr_constructor_exists():
    assert callable(L5Expr.__init__)


def test_l5expr_constructor_args():
    sig = inspect.signature(L5Expr.__init__)
    params = list(sig.parameters.keys())



def test_l6expr_is_not_abstract():
    assert not inspect.isabstract(L6Expr)


def test_l6expr_constructor_exists():
    assert callable(L6Expr.__init__)


def test_l6expr_constructor_args():
    sig = inspect.signature(L6Expr.__init__)
    params = list(sig.parameters.keys())



def test_l7expr_is_not_abstract():
    assert not inspect.isabstract(L7Expr)


def test_l7expr_constructor_exists():
    assert callable(L7Expr.__init__)


def test_l7expr_constructor_args():
    sig = inspect.signature(L7Expr.__init__)
    params = list(sig.parameters.keys())



def test_l8expr_is_not_abstract():
    assert not inspect.isabstract(L8Expr)


def test_l8expr_constructor_exists():
    assert callable(L8Expr.__init__)


def test_l8expr_constructor_args():
    sig = inspect.signature(L8Expr.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl_lessequal_is_not_abstract():
    assert not inspect.isabstract(dbl_LessEqual)


def test_dbl_lessequal_constructor_exists():
    assert callable(dbl_LessEqual.__init__)


def test_dbl_lessequal_constructor_args():
    sig = inspect.signature(dbl_LessEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl_equal_is_not_abstract():
    assert not inspect.isabstract(dbl_Equal)


def test_dbl_equal_constructor_exists():
    assert callable(dbl_Equal.__init__)


def test_dbl_equal_constructor_args():
    sig = inspect.signature(dbl_Equal.__init__)
    params = list(sig.parameters.keys())



def test_dbl_less_is_not_abstract():
    assert not inspect.isabstract(dbl_Less)


def test_dbl_less_constructor_exists():
    assert callable(dbl_Less.__init__)


def test_dbl_less_constructor_args():
    sig = inspect.signature(dbl_Less.__init__)
    params = list(sig.parameters.keys())



def test_dbl_greaterequal_is_not_abstract():
    assert not inspect.isabstract(dbl_GreaterEqual)


def test_dbl_greaterequal_constructor_exists():
    assert callable(dbl_GreaterEqual.__init__)


def test_dbl_greaterequal_constructor_args():
    sig = inspect.signature(dbl_GreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl_instanceof_is_not_abstract():
    assert not inspect.isabstract(dbl_InstanceOf)


def test_dbl_instanceof_constructor_exists():
    assert callable(dbl_InstanceOf.__init__)


def test_dbl_instanceof_constructor_args():
    sig = inspect.signature(dbl_InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_dbl_and_is_not_abstract():
    assert not inspect.isabstract(dbl_And)


def test_dbl_and_constructor_exists():
    assert callable(dbl_And.__init__)


def test_dbl_and_constructor_args():
    sig = inspect.signature(dbl_And.__init__)
    params = list(sig.parameters.keys())



def test_dbl_div_is_not_abstract():
    assert not inspect.isabstract(dbl_Div)


def test_dbl_div_constructor_exists():
    assert callable(dbl_Div.__init__)


def test_dbl_div_constructor_args():
    sig = inspect.signature(dbl_Div.__init__)
    params = list(sig.parameters.keys())



def test_dbl_mod_is_not_abstract():
    assert not inspect.isabstract(dbl_Mod)


def test_dbl_mod_constructor_exists():
    assert callable(dbl_Mod.__init__)


def test_dbl_mod_constructor_args():
    sig = inspect.signature(dbl_Mod.__init__)
    params = list(sig.parameters.keys())



def test_dbl_notequal_is_not_abstract():
    assert not inspect.isabstract(dbl_NotEqual)


def test_dbl_notequal_constructor_exists():
    assert callable(dbl_NotEqual.__init__)


def test_dbl_notequal_constructor_args():
    sig = inspect.signature(dbl_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl_mul_is_not_abstract():
    assert not inspect.isabstract(dbl_Mul)


def test_dbl_mul_constructor_exists():
    assert callable(dbl_Mul.__init__)


def test_dbl_mul_constructor_args():
    sig = inspect.signature(dbl_Mul.__init__)
    params = list(sig.parameters.keys())



def test_dbl_minus_is_not_abstract():
    assert not inspect.isabstract(dbl_Minus)


def test_dbl_minus_constructor_exists():
    assert callable(dbl_Minus.__init__)


def test_dbl_minus_constructor_args():
    sig = inspect.signature(dbl_Minus.__init__)
    params = list(sig.parameters.keys())



def test_dbl_plus_is_not_abstract():
    assert not inspect.isabstract(dbl_Plus)


def test_dbl_plus_constructor_exists():
    assert callable(dbl_Plus.__init__)


def test_dbl_plus_constructor_args():
    sig = inspect.signature(dbl_Plus.__init__)
    params = list(sig.parameters.keys())



def test_dbl_greater_is_not_abstract():
    assert not inspect.isabstract(dbl_Greater)


def test_dbl_greater_constructor_exists():
    assert callable(dbl_Greater.__init__)


def test_dbl_greater_constructor_args():
    sig = inspect.signature(dbl_Greater.__init__)
    params = list(sig.parameters.keys())



def test_dbl_or_is_not_abstract():
    assert not inspect.isabstract(dbl_Or)


def test_dbl_or_constructor_exists():
    assert callable(dbl_Or.__init__)


def test_dbl_or_constructor_args():
    sig = inspect.signature(dbl_Or.__init__)
    params = list(sig.parameters.keys())



def test_dbl_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_DoubleLiteral)


def test_dbl_doubleliteral_constructor_exists():
    assert callable(dbl_DoubleLiteral.__init__)


def test_dbl_doubleliteral_constructor_args():
    sig = inspect.signature(dbl_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl_doubleliteral_has_value():
    assert hasattr(dbl_DoubleLiteral, "value")
    descriptor = None
    for klass in dbl_DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl_falseliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_FalseLiteral)


def test_dbl_falseliteral_constructor_exists():
    assert callable(dbl_FalseLiteral.__init__)


def test_dbl_falseliteral_constructor_args():
    sig = inspect.signature(dbl_FalseLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_trueliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_TrueLiteral)


def test_dbl_trueliteral_constructor_exists():
    assert callable(dbl_TrueLiteral.__init__)


def test_dbl_trueliteral_constructor_args():
    sig = inspect.signature(dbl_TrueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_intliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_IntLiteral)


def test_dbl_intliteral_constructor_exists():
    assert callable(dbl_IntLiteral.__init__)


def test_dbl_intliteral_constructor_args():
    sig = inspect.signature(dbl_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl_intliteral_has_value():
    assert hasattr(dbl_IntLiteral, "value")
    descriptor = None
    for klass in dbl_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl_stringliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_StringLiteral)


def test_dbl_stringliteral_constructor_exists():
    assert callable(dbl_StringLiteral.__init__)


def test_dbl_stringliteral_constructor_args():
    sig = inspect.signature(dbl_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl_stringliteral_has_value():
    assert hasattr(dbl_StringLiteral, "value")
    descriptor = None
    for klass in dbl_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_parseexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_ParseExpr)


def test_dbl_parseexpr_constructor_exists():
    assert callable(dbl_ParseExpr.__init__)


def test_dbl_parseexpr_constructor_args():
    sig = inspect.signature(dbl_ParseExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l3expr_is_not_abstract():
    assert not inspect.isabstract(dbl_L3Expr)


def test_dbl_l3expr_constructor_exists():
    assert callable(dbl_L3Expr.__init__)


def test_dbl_l3expr_constructor_args():
    sig = inspect.signature(dbl_L3Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_codequoteexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_CodeQuoteExpression)


def test_dbl_codequoteexpression_constructor_exists():
    assert callable(dbl_CodeQuoteExpression.__init__)


def test_dbl_codequoteexpression_constructor_args():
    sig = inspect.signature(dbl_CodeQuoteExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_elementaccess_is_not_abstract():
    assert not inspect.isabstract(dbl_ElementAccess)


def test_dbl_elementaccess_constructor_exists():
    assert callable(dbl_ElementAccess.__init__)


def test_dbl_elementaccess_constructor_args():
    sig = inspect.signature(dbl_ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l4expr_is_not_abstract():
    assert not inspect.isabstract(dbl_L4Expr)


def test_dbl_l4expr_constructor_exists():
    assert callable(dbl_L4Expr.__init__)


def test_dbl_l4expr_constructor_args():
    sig = inspect.signature(dbl_L4Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(dbl_UnaryOperator)


def test_dbl_unaryoperator_constructor_exists():
    assert callable(dbl_UnaryOperator.__init__)


def test_dbl_unaryoperator_constructor_args():
    sig = inspect.signature(dbl_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl_metaexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_MetaExpr)


def test_dbl_metaexpr_constructor_exists():
    assert callable(dbl_MetaExpr.__init__)


def test_dbl_metaexpr_constructor_args():
    sig = inspect.signature(dbl_MetaExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_expandexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpandExpression)


def test_dbl_expandexpression_constructor_exists():
    assert callable(dbl_ExpandExpression.__init__)


def test_dbl_expandexpression_constructor_args():
    sig = inspect.signature(dbl_ExpandExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l5expr_is_not_abstract():
    assert not inspect.isabstract(dbl_L5Expr)


def test_dbl_l5expr_constructor_exists():
    assert callable(dbl_L5Expr.__init__)


def test_dbl_l5expr_constructor_args():
    sig = inspect.signature(dbl_L5Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l2expr_is_not_abstract():
    assert not inspect.isabstract(dbl_L2Expr)


def test_dbl_l2expr_constructor_exists():
    assert callable(dbl_L2Expr.__init__)


def test_dbl_l2expr_constructor_args():
    sig = inspect.signature(dbl_L2Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l6expr_is_not_abstract():
    assert not inspect.isabstract(dbl_L6Expr)


def test_dbl_l6expr_constructor_exists():
    assert callable(dbl_L6Expr.__init__)


def test_dbl_l6expr_constructor_args():
    sig = inspect.signature(dbl_L6Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l1expr_is_not_abstract():
    assert not inspect.isabstract(dbl_L1Expr)


def test_dbl_l1expr_constructor_exists():
    assert callable(dbl_L1Expr.__init__)


def test_dbl_l1expr_constructor_args():
    sig = inspect.signature(dbl_L1Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_switchcase_is_not_abstract():
    assert not inspect.isabstract(dbl_SwitchCase)


def test_dbl_switchcase_constructor_exists():
    assert callable(dbl_SwitchCase.__init__)


def test_dbl_switchcase_constructor_args():
    sig = inspect.signature(dbl_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_whilestatement_is_not_abstract():
    assert not inspect.isabstract(dbl_WhileStatement)


def test_dbl_whilestatement_constructor_exists():
    assert callable(dbl_WhileStatement.__init__)


def test_dbl_whilestatement_constructor_args():
    sig = inspect.signature(dbl_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(dbl_BinaryOperator)


def test_dbl_binaryoperator_constructor_exists():
    assert callable(dbl_BinaryOperator.__init__)


def test_dbl_binaryoperator_constructor_args():
    sig = inspect.signature(dbl_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l9expr_is_not_abstract():
    assert not inspect.isabstract(dbl_L9Expr)


def test_dbl_l9expr_constructor_exists():
    assert callable(dbl_L9Expr.__init__)


def test_dbl_l9expr_constructor_args():
    sig = inspect.signature(dbl_L9Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l8expr_is_not_abstract():
    assert not inspect.isabstract(dbl_L8Expr)


def test_dbl_l8expr_constructor_exists():
    assert callable(dbl_L8Expr.__init__)


def test_dbl_l8expr_constructor_args():
    sig = inspect.signature(dbl_L8Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_l7expr_is_not_abstract():
    assert not inspect.isabstract(dbl_L7Expr)


def test_dbl_l7expr_constructor_exists():
    assert callable(dbl_L7Expr.__init__)


def test_dbl_l7expr_constructor_args():
    sig = inspect.signature(dbl_L7Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_variableaccess_is_not_abstract():
    assert not inspect.isabstract(dbl_VariableAccess)


def test_dbl_variableaccess_constructor_exists():
    assert callable(dbl_VariableAccess.__init__)


def test_dbl_variableaccess_constructor_args():
    sig = inspect.signature(dbl_VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_breakstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_BreakStatement)


def test_dbl_breakstatement_constructor_exists():
    assert callable(dbl_BreakStatement.__init__)


def test_dbl_breakstatement_constructor_args():
    sig = inspect.signature(dbl_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_advance_is_not_abstract():
    assert not inspect.isabstract(dbl_Advance)


def test_dbl_advance_constructor_exists():
    assert callable(dbl_Advance.__init__)


def test_dbl_advance_constructor_args():
    sig = inspect.signature(dbl_Advance.__init__)
    params = list(sig.parameters.keys())



def test_dbl_expansionstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpansionStatement)


def test_dbl_expansionstatement_constructor_exists():
    assert callable(dbl_ExpansionStatement.__init__)


def test_dbl_expansionstatement_constructor_args():
    sig = inspect.signature(dbl_ExpansionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "functionContext" in params, "Missing parameter 'functionContext'"
    assert "classContext" in params, "Missing parameter 'classContext'"
    assert "variableContext" in params, "Missing parameter 'variableContext'"

def test_dbl_expansionstatement_has_functionContext():
    assert hasattr(dbl_ExpansionStatement, "functionContext")
    descriptor = None
    for klass in dbl_ExpansionStatement.__mro__:
        if "functionContext" in klass.__dict__:
            descriptor = klass.__dict__["functionContext"]
            break
    assert isinstance(descriptor, property)

def test_dbl_expansionstatement_has_classContext():
    assert hasattr(dbl_ExpansionStatement, "classContext")
    descriptor = None
    for klass in dbl_ExpansionStatement.__mro__:
        if "classContext" in klass.__dict__:
            descriptor = klass.__dict__["classContext"]
            break
    assert isinstance(descriptor, property)

def test_dbl_expansionstatement_has_variableContext():
    assert hasattr(dbl_ExpansionStatement, "variableContext")
    descriptor = None
    for klass in dbl_ExpansionStatement.__mro__:
        if "variableContext" in klass.__dict__:
            descriptor = klass.__dict__["variableContext"]
            break
    assert isinstance(descriptor, property)



def test_dbl_print_is_not_abstract():
    assert not inspect.isabstract(dbl_Print)


def test_dbl_print_constructor_exists():
    assert callable(dbl_Print.__init__)


def test_dbl_print_constructor_args():
    sig = inspect.signature(dbl_Print.__init__)
    params = list(sig.parameters.keys())



def test_dbl_waituntil_is_not_abstract():
    assert not inspect.isabstract(dbl_WaitUntil)


def test_dbl_waituntil_constructor_exists():
    assert callable(dbl_WaitUntil.__init__)


def test_dbl_waituntil_constructor_args():
    sig = inspect.signature(dbl_WaitUntil.__init__)
    params = list(sig.parameters.keys())



def test_dbl_return_is_not_abstract():
    assert not inspect.isabstract(dbl_Return)


def test_dbl_return_constructor_exists():
    assert callable(dbl_Return.__init__)


def test_dbl_return_constructor_args():
    sig = inspect.signature(dbl_Return.__init__)
    params = list(sig.parameters.keys())



def test_dbl_targetstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_TargetStatement)


def test_dbl_targetstatement_constructor_exists():
    assert callable(dbl_TargetStatement.__init__)


def test_dbl_targetstatement_constructor_args():
    sig = inspect.signature(dbl_TargetStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_continuestatement_is_not_abstract():
    assert not inspect.isabstract(dbl_ContinueStatement)


def test_dbl_continuestatement_constructor_exists():
    assert callable(dbl_ContinueStatement.__init__)


def test_dbl_continuestatement_constructor_args():
    sig = inspect.signature(dbl_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_reactivate_is_not_abstract():
    assert not inspect.isabstract(dbl_Reactivate)


def test_dbl_reactivate_constructor_exists():
    assert callable(dbl_Reactivate.__init__)


def test_dbl_reactivate_constructor_args():
    sig = inspect.signature(dbl_Reactivate.__init__)
    params = list(sig.parameters.keys())



def test_dbl_switchstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_SwitchStatement)


def test_dbl_switchstatement_constructor_exists():
    assert callable(dbl_SwitchStatement.__init__)


def test_dbl_switchstatement_constructor_args():
    sig = inspect.signature(dbl_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_terminate_is_not_abstract():
    assert not inspect.isabstract(dbl_Terminate)


def test_dbl_terminate_constructor_exists():
    assert callable(dbl_Terminate.__init__)


def test_dbl_terminate_constructor_args():
    sig = inspect.signature(dbl_Terminate.__init__)
    params = list(sig.parameters.keys())



def test_dbl_yield_is_not_abstract():
    assert not inspect.isabstract(dbl_Yield)


def test_dbl_yield_constructor_exists():
    assert callable(dbl_Yield.__init__)


def test_dbl_yield_constructor_args():
    sig = inspect.signature(dbl_Yield.__init__)
    params = list(sig.parameters.keys())



def test_dbl_functioncall_is_not_abstract():
    assert not inspect.isabstract(dbl_FunctionCall)


def test_dbl_functioncall_constructor_exists():
    assert callable(dbl_FunctionCall.__init__)


def test_dbl_functioncall_constructor_args():
    sig = inspect.signature(dbl_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_dbl_activateobject_is_not_abstract():
    assert not inspect.isabstract(dbl_ActivateObject)


def test_dbl_activateobject_constructor_exists():
    assert callable(dbl_ActivateObject.__init__)


def test_dbl_activateobject_constructor_args():
    sig = inspect.signature(dbl_ActivateObject.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_dbl_activateobject_has_priority():
    assert hasattr(dbl_ActivateObject, "priority")
    descriptor = None
    for klass in dbl_ActivateObject.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_dbl_wait_is_not_abstract():
    assert not inspect.isabstract(dbl_Wait)


def test_dbl_wait_constructor_exists():
    assert callable(dbl_Wait.__init__)


def test_dbl_wait_constructor_args():
    sig = inspect.signature(dbl_Wait.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_dbl_localscope_is_not_abstract():
    assert not inspect.isabstract(dbl_LocalScope)


def test_dbl_localscope_constructor_exists():
    assert callable(dbl_LocalScope.__init__)


def test_dbl_localscope_constructor_args():
    sig = inspect.signature(dbl_LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_annotateableelement_is_not_abstract():
    assert not inspect.isabstract(AnnotateableElement)


def test_annotateableelement_constructor_exists():
    assert callable(AnnotateableElement.__init__)


def test_annotateableelement_constructor_args():
    sig = inspect.signature(AnnotateableElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_assignment_is_not_abstract():
    assert not inspect.isabstract(dbl_Assignment)


def test_dbl_assignment_constructor_exists():
    assert callable(dbl_Assignment.__init__)


def test_dbl_assignment_constructor_args():
    sig = inspect.signature(dbl_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_teststatement_is_not_abstract():
    assert not inspect.isabstract(dbl_TestStatement)


def test_dbl_teststatement_constructor_exists():
    assert callable(dbl_TestStatement.__init__)


def test_dbl_teststatement_constructor_args():
    sig = inspect.signature(dbl_TestStatement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl_teststatement_has_value():
    assert hasattr(dbl_TestStatement, "value")
    descriptor = None
    for klass in dbl_TestStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl_expandstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpandStatement)


def test_dbl_expandstatement_constructor_exists():
    assert callable(dbl_ExpandStatement.__init__)


def test_dbl_expandstatement_constructor_args():
    sig = inspect.signature(dbl_ExpandStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_ifstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_IfStatement)


def test_dbl_ifstatement_constructor_exists():
    assert callable(dbl_IfStatement.__init__)


def test_dbl_ifstatement_constructor_args():
    sig = inspect.signature(dbl_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_simplestatement_is_not_abstract():
    assert not inspect.isabstract(dbl_SimpleStatement)


def test_dbl_simplestatement_constructor_exists():
    assert callable(dbl_SimpleStatement.__init__)


def test_dbl_simplestatement_constructor_args():
    sig = inspect.signature(dbl_SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_loopstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_LoopStatement)


def test_dbl_loopstatement_constructor_exists():
    assert callable(dbl_LoopStatement.__init__)


def test_dbl_loopstatement_constructor_args():
    sig = inspect.signature(dbl_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_namedelement_is_not_abstract():
    assert not inspect.isabstract(dbl_NamedElement)


def test_dbl_namedelement_constructor_exists():
    assert callable(dbl_NamedElement.__init__)


def test_dbl_namedelement_constructor_args():
    sig = inspect.signature(dbl_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbl_namedelement_has_name():
    assert hasattr(dbl_NamedElement, "name")
    descriptor = None
    for klass in dbl_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dbl_nativebinding_is_not_abstract():
    assert not inspect.isabstract(dbl_NativeBinding)


def test_dbl_nativebinding_constructor_exists():
    assert callable(dbl_NativeBinding.__init__)


def test_dbl_nativebinding_constructor_args():
    sig = inspect.signature(dbl_NativeBinding.__init__)
    params = list(sig.parameters.keys())
    assert "targetLanguage" in params, "Missing parameter 'targetLanguage'"
    assert "targetType" in params, "Missing parameter 'targetType'"

def test_dbl_nativebinding_has_targetLanguage():
    assert hasattr(dbl_NativeBinding, "targetLanguage")
    descriptor = None
    for klass in dbl_NativeBinding.__mro__:
        if "targetLanguage" in klass.__dict__:
            descriptor = klass.__dict__["targetLanguage"]
            break
    assert isinstance(descriptor, property)

def test_dbl_nativebinding_has_targetType():
    assert hasattr(dbl_NativeBinding, "targetType")
    descriptor = None
    for klass in dbl_NativeBinding.__mro__:
        if "targetType" in klass.__dict__:
            descriptor = klass.__dict__["targetType"]
            break
    assert isinstance(descriptor, property)



def test_dbl_parameter_is_not_abstract():
    assert not inspect.isabstract(dbl_Parameter)


def test_dbl_parameter_constructor_exists():
    assert callable(dbl_Parameter.__init__)


def test_dbl_parameter_constructor_args():
    sig = inspect.signature(dbl_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_localscope_is_not_abstract():
    assert not inspect.isabstract(LocalScope)


def test_localscope_constructor_exists():
    assert callable(LocalScope.__init__)


def test_localscope_constructor_args():
    sig = inspect.signature(LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_dbl_forstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_ForStatement)


def test_dbl_forstatement_constructor_exists():
    assert callable(dbl_ForStatement.__init__)


def test_dbl_forstatement_constructor_args():
    sig = inspect.signature(dbl_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_localscopestatement_is_not_abstract():
    assert not inspect.isabstract(dbl_LocalScopeStatement)


def test_dbl_localscopestatement_constructor_exists():
    assert callable(dbl_LocalScopeStatement.__init__)


def test_dbl_localscopestatement_constructor_args():
    sig = inspect.signature(dbl_LocalScopeStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_constructor_is_not_abstract():
    assert not inspect.isabstract(dbl_Constructor)


def test_dbl_constructor_constructor_exists():
    assert callable(dbl_Constructor.__init__)


def test_dbl_constructor_constructor_args():
    sig = inspect.signature(dbl_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_cast_is_not_abstract():
    assert not inspect.isabstract(dbl_Cast)


def test_dbl_cast_constructor_exists():
    assert callable(dbl_Cast.__init__)


def test_dbl_cast_constructor_args():
    sig = inspect.signature(dbl_Cast.__init__)
    params = list(sig.parameters.keys())



def test_dbl_createobject_is_not_abstract():
    assert not inspect.isabstract(dbl_CreateObject)


def test_dbl_createobject_constructor_exists():
    assert callable(dbl_CreateObject.__init__)


def test_dbl_createobject_constructor_args():
    sig = inspect.signature(dbl_CreateObject.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_inttype_is_not_abstract():
    assert not inspect.isabstract(dbl_IntType)


def test_dbl_inttype_constructor_exists():
    assert callable(dbl_IntType.__init__)


def test_dbl_inttype_constructor_args():
    sig = inspect.signature(dbl_IntType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_doubletype_is_not_abstract():
    assert not inspect.isabstract(dbl_DoubleType)


def test_dbl_doubletype_constructor_exists():
    assert callable(dbl_DoubleType.__init__)


def test_dbl_doubletype_constructor_args():
    sig = inspect.signature(dbl_DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_booltype_is_not_abstract():
    assert not inspect.isabstract(dbl_BoolType)


def test_dbl_booltype_constructor_exists():
    assert callable(dbl_BoolType.__init__)


def test_dbl_booltype_constructor_args():
    sig = inspect.signature(dbl_BoolType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_stringtype_is_not_abstract():
    assert not inspect.isabstract(dbl_StringType)


def test_dbl_stringtype_constructor_exists():
    assert callable(dbl_StringType.__init__)


def test_dbl_stringtype_constructor_args():
    sig = inspect.signature(dbl_StringType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_voidtype_is_not_abstract():
    assert not inspect.isabstract(dbl_VoidType)


def test_dbl_voidtype_constructor_exists():
    assert callable(dbl_VoidType.__init__)


def test_dbl_voidtype_constructor_args():
    sig = inspect.signature(dbl_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dbl_idexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_IdExpr)


def test_dbl_idexpr_constructor_exists():
    assert callable(dbl_IdExpr.__init__)


def test_dbl_idexpr_constructor_args():
    sig = inspect.signature(dbl_IdExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_primitivetype_is_not_abstract():
    assert not inspect.isabstract(dbl_PrimitiveType)


def test_dbl_primitivetype_constructor_exists():
    assert callable(dbl_PrimitiveType.__init__)


def test_dbl_primitivetype_constructor_args():
    sig = inspect.signature(dbl_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_typedelement_is_not_abstract():
    assert not inspect.isabstract(dbl_TypedElement)


def test_dbl_typedelement_constructor_exists():
    assert callable(dbl_TypedElement.__init__)


def test_dbl_typedelement_constructor_args():
    sig = inspect.signature(dbl_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_arraydimension_is_not_abstract():
    assert not inspect.isabstract(dbl_ArrayDimension)


def test_dbl_arraydimension_constructor_exists():
    assert callable(dbl_ArrayDimension.__init__)


def test_dbl_arraydimension_constructor_args():
    sig = inspect.signature(dbl_ArrayDimension.__init__)
    params = list(sig.parameters.keys())



def test_dbl_type_is_not_abstract():
    assert not inspect.isabstract(dbl_Type)


def test_dbl_type_constructor_exists():
    assert callable(dbl_Type.__init__)


def test_dbl_type_constructor_args():
    sig = inspect.signature(dbl_Type.__init__)
    params = list(sig.parameters.keys())



def test_constructiveextension_is_not_abstract():
    assert not inspect.isabstract(ConstructiveExtension)


def test_constructiveextension_constructor_exists():
    assert callable(ConstructiveExtension.__init__)


def test_constructiveextension_constructor_args():
    sig = inspect.signature(ConstructiveExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl_classcontentextension_is_not_abstract():
    assert not inspect.isabstract(dbl_ClassContentExtension)


def test_dbl_classcontentextension_constructor_exists():
    assert callable(dbl_ClassContentExtension.__init__)


def test_dbl_classcontentextension_constructor_args():
    sig = inspect.signature(dbl_ClassContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl_modulecontentextension_is_not_abstract():
    assert not inspect.isabstract(dbl_ModuleContentExtension)


def test_dbl_modulecontentextension_constructor_exists():
    assert callable(dbl_ModuleContentExtension.__init__)


def test_dbl_modulecontentextension_constructor_args():
    sig = inspect.signature(dbl_ModuleContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_concept_is_not_abstract():
    assert not inspect.isabstract(Concept)


def test_concept_constructor_exists():
    assert callable(Concept.__init__)


def test_concept_constructor_args():
    sig = inspect.signature(Concept.__init__)
    params = list(sig.parameters.keys())



def test_dbl_superclassspecification_is_not_abstract():
    assert not inspect.isabstract(dbl_SuperClassSpecification)


def test_dbl_superclassspecification_constructor_exists():
    assert callable(dbl_SuperClassSpecification.__init__)


def test_dbl_superclassspecification_constructor_args():
    sig = inspect.signature(dbl_SuperClassSpecification.__init__)
    params = list(sig.parameters.keys())



def test_dbl_annotationitem_is_not_abstract():
    assert not inspect.isabstract(dbl_AnnotationItem)


def test_dbl_annotationitem_constructor_exists():
    assert callable(dbl_AnnotationItem.__init__)


def test_dbl_annotationitem_constructor_args():
    sig = inspect.signature(dbl_AnnotationItem.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_dbl_annotationitem_has_key():
    assert hasattr(dbl_AnnotationItem, "key")
    descriptor = None
    for klass in dbl_AnnotationItem.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_dbl_annotationitem_has_value():
    assert hasattr(dbl_AnnotationItem, "value")
    descriptor = None
    for klass in dbl_AnnotationItem.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl_variable_is_not_abstract():
    assert not inspect.isabstract(dbl_Variable)


def test_dbl_variable_constructor_exists():
    assert callable(dbl_Variable.__init__)


def test_dbl_variable_constructor_args():
    sig = inspect.signature(dbl_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "control" in params, "Missing parameter 'control'"

def test_dbl_variable_has_class_():
    assert hasattr(dbl_Variable, "class_")
    descriptor = None
    for klass in dbl_Variable.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_dbl_variable_has_control():
    assert hasattr(dbl_Variable, "control")
    descriptor = None
    for klass in dbl_Variable.__mro__:
        if "control" in klass.__dict__:
            descriptor = klass.__dict__["control"]
            break
    assert isinstance(descriptor, property)



def test_constructiveextensionatcontentextensionpoint_is_not_abstract():
    assert not inspect.isabstract(ConstructiveExtensionAtContentExtensionPoint)


def test_constructiveextensionatcontentextensionpoint_constructor_exists():
    assert callable(ConstructiveExtensionAtContentExtensionPoint.__init__)


def test_constructiveextensionatcontentextensionpoint_constructor_args():
    sig = inspect.signature(ConstructiveExtensionAtContentExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_dbl_import_is_not_abstract():
    assert not inspect.isabstract(dbl_Import)


def test_dbl_import_constructor_exists():
    assert callable(dbl_Import.__init__)


def test_dbl_import_constructor_args():
    sig = inspect.signature(dbl_Import.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_dbl_import_has_file():
    assert hasattr(dbl_Import, "file")
    descriptor = None
    for klass in dbl_Import.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_dbl_model_is_not_abstract():
    assert not inspect.isabstract(dbl_Model)


def test_dbl_model_constructor_exists():
    assert callable(dbl_Model.__init__)


def test_dbl_model_constructor_args():
    sig = inspect.signature(dbl_Model.__init__)
    params = list(sig.parameters.keys())



def test_construct_is_not_abstract():
    assert not inspect.isabstract(Construct)


def test_construct_constructor_exists():
    assert callable(Construct.__init__)


def test_construct_constructor_args():
    sig = inspect.signature(Construct.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(dbl_AbstractVariable)


def test_dbl_abstractvariable_constructor_exists():
    assert callable(dbl_AbstractVariable.__init__)


def test_dbl_abstractvariable_constructor_args():
    sig = inspect.signature(dbl_AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_dbl_structuralsymbolreference_is_not_abstract():
    assert not inspect.isabstract(dbl_StructuralSymbolReference)


def test_dbl_structuralsymbolreference_constructor_exists():
    assert callable(dbl_StructuralSymbolReference.__init__)


def test_dbl_structuralsymbolreference_constructor_args():
    sig = inspect.signature(dbl_StructuralSymbolReference.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"
    assert "composite" in params, "Missing parameter 'composite'"
    assert "localScopedReference" in params, "Missing parameter 'localScopedReference'"
    assert "globalScopedReference" in params, "Missing parameter 'globalScopedReference'"

def test_dbl_structuralsymbolreference_has_list():
    assert hasattr(dbl_StructuralSymbolReference, "list")
    descriptor = None
    for klass in dbl_StructuralSymbolReference.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)

def test_dbl_structuralsymbolreference_has_composite():
    assert hasattr(dbl_StructuralSymbolReference, "composite")
    descriptor = None
    for klass in dbl_StructuralSymbolReference.__mro__:
        if "composite" in klass.__dict__:
            descriptor = klass.__dict__["composite"]
            break
    assert isinstance(descriptor, property)

def test_dbl_structuralsymbolreference_has_localScopedReference():
    assert hasattr(dbl_StructuralSymbolReference, "localScopedReference")
    descriptor = None
    for klass in dbl_StructuralSymbolReference.__mro__:
        if "localScopedReference" in klass.__dict__:
            descriptor = klass.__dict__["localScopedReference"]
            break
    assert isinstance(descriptor, property)

def test_dbl_structuralsymbolreference_has_globalScopedReference():
    assert hasattr(dbl_StructuralSymbolReference, "globalScopedReference")
    descriptor = None
    for klass in dbl_StructuralSymbolReference.__mro__:
        if "globalScopedReference" in klass.__dict__:
            descriptor = klass.__dict__["globalScopedReference"]
            break
    assert isinstance(descriptor, property)



def test_dbl_annotation_is_not_abstract():
    assert not inspect.isabstract(dbl_Annotation)


def test_dbl_annotation_constructor_exists():
    assert callable(dbl_Annotation.__init__)


def test_dbl_annotation_constructor_args():
    sig = inspect.signature(dbl_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dbl_function_is_not_abstract():
    assert not inspect.isabstract(dbl_Function)


def test_dbl_function_constructor_exists():
    assert callable(dbl_Function.__init__)


def test_dbl_function_constructor_args():
    sig = inspect.signature(dbl_Function.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_dbl_function_has_abstract():
    assert hasattr(dbl_Function, "abstract")
    descriptor = None
    for klass in dbl_Function.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_dbl_function_has_class_():
    assert hasattr(dbl_Function, "class_")
    descriptor = None
    for klass in dbl_Function.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_dbl_module_is_not_abstract():
    assert not inspect.isabstract(dbl_Module)


def test_dbl_module_constructor_exists():
    assert callable(dbl_Module.__init__)


def test_dbl_module_constructor_args():
    sig = inspect.signature(dbl_Module.__init__)
    params = list(sig.parameters.keys())



def test_dbl_pattern_is_not_abstract():
    assert not inspect.isabstract(dbl_Pattern)


def test_dbl_pattern_constructor_exists():
    assert callable(dbl_Pattern.__init__)


def test_dbl_pattern_constructor_args():
    sig = inspect.signature(dbl_Pattern.__init__)
    params = list(sig.parameters.keys())
    assert "top" in params, "Missing parameter 'top'"

def test_dbl_pattern_has_top():
    assert hasattr(dbl_Pattern, "top")
    descriptor = None
    for klass in dbl_Pattern.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)



def test_dbl_metasymbol_is_not_abstract():
    assert not inspect.isabstract(dbl_MetaSymbol)


def test_dbl_metasymbol_constructor_exists():
    assert callable(dbl_MetaSymbol.__init__)


def test_dbl_metasymbol_constructor_args():
    sig = inspect.signature(dbl_MetaSymbol.__init__)
    params = list(sig.parameters.keys())



def test_dbl_class_is_not_abstract():
    assert not inspect.isabstract(dbl_Class)


def test_dbl_class_constructor_exists():
    assert callable(dbl_Class.__init__)


def test_dbl_class_constructor_args():
    sig = inspect.signature(dbl_Class.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_dbl_class_has_active():
    assert hasattr(dbl_Class, "active")
    descriptor = None
    for klass in dbl_Class.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_dbl_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(dbl_ExtensibleElement)


def test_dbl_extensibleelement_constructor_exists():
    assert callable(dbl_ExtensibleElement.__init__)


def test_dbl_extensibleelement_constructor_args():
    sig = inspect.signature(dbl_ExtensibleElement.__init__)
    params = list(sig.parameters.keys())
    assert "instanceOfExtensionDefinition" in params, "Missing parameter 'instanceOfExtensionDefinition'"
    assert "concreteSyntax" in params, "Missing parameter 'concreteSyntax'"

def test_dbl_extensibleelement_has_instanceOfExtensionDefinition():
    assert hasattr(dbl_ExtensibleElement, "instanceOfExtensionDefinition")
    descriptor = None
    for klass in dbl_ExtensibleElement.__mro__:
        if "instanceOfExtensionDefinition" in klass.__dict__:
            descriptor = klass.__dict__["instanceOfExtensionDefinition"]
            break
    assert isinstance(descriptor, property)

def test_dbl_extensibleelement_has_concreteSyntax():
    assert hasattr(dbl_ExtensibleElement, "concreteSyntax")
    descriptor = None
    for klass in dbl_ExtensibleElement.__mro__:
        if "concreteSyntax" in klass.__dict__:
            descriptor = klass.__dict__["concreteSyntax"]
            break
    assert isinstance(descriptor, property)



def test_dbl_expandexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpandExpr)


def test_dbl_expandexpr_constructor_exists():
    assert callable(dbl_ExpandExpr.__init__)


def test_dbl_expandexpr_constructor_args():
    sig = inspect.signature(dbl_ExpandExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_construct_is_not_abstract():
    assert not inspect.isabstract(dbl_Construct)


def test_dbl_construct_constructor_exists():
    assert callable(dbl_Construct.__init__)


def test_dbl_construct_constructor_args():
    sig = inspect.signature(dbl_Construct.__init__)
    params = list(sig.parameters.keys())



def test_dbl_constructiveextensionatcontentextensionpoint_is_not_abstract():
    assert not inspect.isabstract(dbl_ConstructiveExtensionAtContentExtensionPoint)


def test_dbl_constructiveextensionatcontentextensionpoint_constructor_exists():
    assert callable(dbl_ConstructiveExtensionAtContentExtensionPoint.__init__)


def test_dbl_constructiveextensionatcontentextensionpoint_constructor_args():
    sig = inspect.signature(dbl_ConstructiveExtensionAtContentExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(ExtensibleElement)


def test_extensibleelement_constructor_exists():
    assert callable(ExtensibleElement.__init__)


def test_extensibleelement_constructor_args():
    sig = inspect.signature(ExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_expression_is_not_abstract():
    assert not inspect.isabstract(dbl_Expression)


def test_dbl_expression_constructor_exists():
    assert callable(dbl_Expression.__init__)


def test_dbl_expression_constructor_args():
    sig = inspect.signature(dbl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_syntaxdefinition_is_not_abstract():
    assert not inspect.isabstract(dbl_SyntaxDefinition)


def test_dbl_syntaxdefinition_constructor_exists():
    assert callable(dbl_SyntaxDefinition.__init__)


def test_dbl_syntaxdefinition_constructor_args():
    sig = inspect.signature(dbl_SyntaxDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dbl_extensionsemantics_is_not_abstract():
    assert not inspect.isabstract(dbl_ExtensionSemantics)


def test_dbl_extensionsemantics_constructor_exists():
    assert callable(dbl_ExtensionSemantics.__init__)


def test_dbl_extensionsemantics_constructor_args():
    sig = inspect.signature(dbl_ExtensionSemantics.__init__)
    params = list(sig.parameters.keys())



def test_dbl_statement_is_not_abstract():
    assert not inspect.isabstract(dbl_Statement)


def test_dbl_statement_constructor_exists():
    assert callable(dbl_Statement.__init__)


def test_dbl_statement_constructor_args():
    sig = inspect.signature(dbl_Statement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_syntaxsymbolclassifier_is_not_abstract():
    assert not inspect.isabstract(dbl_SyntaxSymbolClassifier)


def test_dbl_syntaxsymbolclassifier_constructor_exists():
    assert callable(dbl_SyntaxSymbolClassifier.__init__)


def test_dbl_syntaxsymbolclassifier_constructor_args():
    sig = inspect.signature(dbl_SyntaxSymbolClassifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl_extension_is_not_abstract():
    assert not inspect.isabstract(dbl_Extension)


def test_dbl_extension_constructor_exists():
    assert callable(dbl_Extension.__init__)


def test_dbl_extension_constructor_args():
    sig = inspect.signature(dbl_Extension.__init__)
    params = list(sig.parameters.keys())



def test_dbl_constructiveextension_is_not_abstract():
    assert not inspect.isabstract(dbl_ConstructiveExtension)


def test_dbl_constructiveextension_constructor_exists():
    assert callable(dbl_ConstructiveExtension.__init__)


def test_dbl_constructiveextension_constructor_args():
    sig = inspect.signature(dbl_ConstructiveExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl_annotateableelement_is_not_abstract():
    assert not inspect.isabstract(dbl_AnnotateableElement)


def test_dbl_annotateableelement_constructor_exists():
    assert callable(dbl_AnnotateableElement.__init__)


def test_dbl_annotateableelement_constructor_args():
    sig = inspect.signature(dbl_AnnotateableElement.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Module_strategy = st.builds(
    Module,
)
Class_strategy = st.builds(
    Class,
)
QuotedCode_strategy = st.builds(
    QuotedCode,
)
dbl_QuotedStatements_strategy = st.builds(
    dbl_QuotedStatements,
)
dbl_QuotedClassContent_strategy = st.builds(
    dbl_QuotedClassContent,
)
dbl_QuotedModuleContent_strategy = st.builds(
    dbl_QuotedModuleContent,
)
dbl_QuotedExpression_strategy = st.builds(
    dbl_QuotedExpression,
)
dbl_QuotedCode_strategy = st.builds(
    dbl_QuotedCode,
)
ExpansionPart_strategy = st.builds(
    ExpansionPart,
)
dbl_ExpandVariablePart_strategy = st.builds(
    dbl_ExpandVariablePart,
)
dbl_ExpandTextPart_strategy = st.builds(
    dbl_ExpandTextPart,
    text=
        safe_text
)
dbl_ExpansionPart_strategy = st.builds(
    dbl_ExpansionPart,
)
Variable_strategy = st.builds(
    Variable,
)
dbl_CreateIdStatement_strategy = st.builds(
    dbl_CreateIdStatement,
)
ElementarySymbol_strategy = st.builds(
    ElementarySymbol,
)
dbl_IntSymbol_strategy = st.builds(
    dbl_IntSymbol,
)
dbl_StringSymbol_strategy = st.builds(
    dbl_StringSymbol,
)
dbl_Keyword_strategy = st.builds(
    dbl_Keyword,
    keyword=
        safe_text
)
dbl_IdSymbol_strategy = st.builds(
    dbl_IdSymbol,
)
PlainSymbolReference_strategy = st.builds(
    PlainSymbolReference,
)
L2SyntaxExpression_strategy = st.builds(
    L2SyntaxExpression,
)
dbl_SymbolSequence_strategy = st.builds(
    dbl_SymbolSequence,
)
SyntaxExpression_strategy = st.builds(
    SyntaxExpression,
)
dbl_L1SyntaxExpression_strategy = st.builds(
    dbl_L1SyntaxExpression,
)
dbl_L2SyntaxExpression_strategy = st.builds(
    dbl_L2SyntaxExpression,
)
dbl_L3SyntaxExpression_strategy = st.builds(
    dbl_L3SyntaxExpression,
)
dbl_SyntaxExpression_strategy = st.builds(
    dbl_SyntaxExpression,
)
ComplexSymbol_strategy = st.builds(
    ComplexSymbol,
)
SyntaxSymbolClassifier_strategy = st.builds(
    SyntaxSymbolClassifier,
)
dbl_ElementarySymbol_strategy = st.builds(
    dbl_ElementarySymbol,
)
dbl_ComplexSymbol_strategy = st.builds(
    dbl_ComplexSymbol,
)
L1SyntaxExpression_strategy = st.builds(
    L1SyntaxExpression,
)
dbl_PlainSymbolReference_strategy = st.builds(
    dbl_PlainSymbolReference,
)
dbl_CallPart_strategy = st.builds(
    dbl_CallPart,
)
Annotation_strategy = st.builds(
    Annotation,
)
PredefinedId_strategy = st.builds(
    PredefinedId,
)
dbl_AnnotationLiteral_strategy = st.builds(
    dbl_AnnotationLiteral,
)
dbl_MetaLiteral_strategy = st.builds(
    dbl_MetaLiteral,
)
dbl_TypeLiteral_strategy = st.builds(
    dbl_TypeLiteral,
)
dbl_SizeOfArray_strategy = st.builds(
    dbl_SizeOfArray,
)
dbl_SuperLiteral_strategy = st.builds(
    dbl_SuperLiteral,
)
dbl_MeLiteral_strategy = st.builds(
    dbl_MeLiteral,
)
dbl_PredefinedId_strategy = st.builds(
    dbl_PredefinedId,
)
dbl_Concept_strategy = st.builds(
    dbl_Concept,
)
VariableAccess_strategy = st.builds(
    VariableAccess,
)
dbl_MetaAccess_strategy = st.builds(
    dbl_MetaAccess,
)
ElementAccess_strategy = st.builds(
    ElementAccess,
)
dbl_TypeAccess_strategy = st.builds(
    dbl_TypeAccess,
)
L1Expr_strategy = st.builds(
    L1Expr,
)
dbl_TimeLiteral_strategy = st.builds(
    dbl_TimeLiteral,
)
dbl_NullLiteral_strategy = st.builds(
    dbl_NullLiteral,
)
dbl_ActiveLiteral_strategy = st.builds(
    dbl_ActiveLiteral,
)
L2Expr_strategy = st.builds(
    L2Expr,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
dbl_Not_strategy = st.builds(
    dbl_Not,
)
dbl_Neg_strategy = st.builds(
    dbl_Neg,
)
L3Expr_strategy = st.builds(
    L3Expr,
)
L4Expr_strategy = st.builds(
    L4Expr,
)
L5Expr_strategy = st.builds(
    L5Expr,
)
L6Expr_strategy = st.builds(
    L6Expr,
)
L7Expr_strategy = st.builds(
    L7Expr,
)
L8Expr_strategy = st.builds(
    L8Expr,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
dbl_LessEqual_strategy = st.builds(
    dbl_LessEqual,
)
dbl_Equal_strategy = st.builds(
    dbl_Equal,
)
dbl_Less_strategy = st.builds(
    dbl_Less,
)
dbl_GreaterEqual_strategy = st.builds(
    dbl_GreaterEqual,
)
dbl_InstanceOf_strategy = st.builds(
    dbl_InstanceOf,
)
dbl_And_strategy = st.builds(
    dbl_And,
)
dbl_Div_strategy = st.builds(
    dbl_Div,
)
dbl_Mod_strategy = st.builds(
    dbl_Mod,
)
dbl_NotEqual_strategy = st.builds(
    dbl_NotEqual,
)
dbl_Mul_strategy = st.builds(
    dbl_Mul,
)
dbl_Minus_strategy = st.builds(
    dbl_Minus,
)
dbl_Plus_strategy = st.builds(
    dbl_Plus,
)
dbl_Greater_strategy = st.builds(
    dbl_Greater,
)
dbl_Or_strategy = st.builds(
    dbl_Or,
)
dbl_DoubleLiteral_strategy = st.builds(
    dbl_DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dbl_FalseLiteral_strategy = st.builds(
    dbl_FalseLiteral,
)
dbl_TrueLiteral_strategy = st.builds(
    dbl_TrueLiteral,
)
dbl_IntLiteral_strategy = st.builds(
    dbl_IntLiteral,
    value=
        st.integers()
)
dbl_StringLiteral_strategy = st.builds(
    dbl_StringLiteral,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
dbl_ParseExpr_strategy = st.builds(
    dbl_ParseExpr,
)
dbl_L3Expr_strategy = st.builds(
    dbl_L3Expr,
)
dbl_CodeQuoteExpression_strategy = st.builds(
    dbl_CodeQuoteExpression,
)
dbl_ElementAccess_strategy = st.builds(
    dbl_ElementAccess,
)
dbl_L4Expr_strategy = st.builds(
    dbl_L4Expr,
)
dbl_UnaryOperator_strategy = st.builds(
    dbl_UnaryOperator,
)
dbl_MetaExpr_strategy = st.builds(
    dbl_MetaExpr,
)
dbl_ExpandExpression_strategy = st.builds(
    dbl_ExpandExpression,
)
dbl_L5Expr_strategy = st.builds(
    dbl_L5Expr,
)
dbl_L2Expr_strategy = st.builds(
    dbl_L2Expr,
)
dbl_L6Expr_strategy = st.builds(
    dbl_L6Expr,
)
dbl_L1Expr_strategy = st.builds(
    dbl_L1Expr,
)
dbl_SwitchCase_strategy = st.builds(
    dbl_SwitchCase,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
dbl_WhileStatement_strategy = st.builds(
    dbl_WhileStatement,
)
dbl_BinaryOperator_strategy = st.builds(
    dbl_BinaryOperator,
)
dbl_L9Expr_strategy = st.builds(
    dbl_L9Expr,
)
dbl_L8Expr_strategy = st.builds(
    dbl_L8Expr,
)
dbl_L7Expr_strategy = st.builds(
    dbl_L7Expr,
)
dbl_VariableAccess_strategy = st.builds(
    dbl_VariableAccess,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
dbl_BreakStatement_strategy = st.builds(
    dbl_BreakStatement,
)
dbl_Advance_strategy = st.builds(
    dbl_Advance,
)
dbl_ExpansionStatement_strategy = st.builds(
    dbl_ExpansionStatement,
    functionContext=
        st.booleans(),
    classContext=
        st.booleans(),
    variableContext=
        st.booleans()
)
dbl_Print_strategy = st.builds(
    dbl_Print,
)
dbl_WaitUntil_strategy = st.builds(
    dbl_WaitUntil,
)
dbl_Return_strategy = st.builds(
    dbl_Return,
)
dbl_TargetStatement_strategy = st.builds(
    dbl_TargetStatement,
)
dbl_ContinueStatement_strategy = st.builds(
    dbl_ContinueStatement,
)
dbl_Reactivate_strategy = st.builds(
    dbl_Reactivate,
)
dbl_SwitchStatement_strategy = st.builds(
    dbl_SwitchStatement,
)
dbl_Terminate_strategy = st.builds(
    dbl_Terminate,
)
dbl_Yield_strategy = st.builds(
    dbl_Yield,
)
dbl_FunctionCall_strategy = st.builds(
    dbl_FunctionCall,
)
dbl_ActivateObject_strategy = st.builds(
    dbl_ActivateObject,
    priority=
        st.integers()
)
dbl_Wait_strategy = st.builds(
    dbl_Wait,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
dbl_LocalScope_strategy = st.builds(
    dbl_LocalScope,
)
AnnotateableElement_strategy = st.builds(
    AnnotateableElement,
)
dbl_Assignment_strategy = st.builds(
    dbl_Assignment,
)
Statement_strategy = st.builds(
    Statement,
)
dbl_TestStatement_strategy = st.builds(
    dbl_TestStatement,
    value=
        st.integers()
)
dbl_ExpandStatement_strategy = st.builds(
    dbl_ExpandStatement,
)
dbl_IfStatement_strategy = st.builds(
    dbl_IfStatement,
)
dbl_SimpleStatement_strategy = st.builds(
    dbl_SimpleStatement,
)
dbl_LoopStatement_strategy = st.builds(
    dbl_LoopStatement,
)
dbl_NamedElement_strategy = st.builds(
    dbl_NamedElement,
    name=
        safe_text
)
dbl_NativeBinding_strategy = st.builds(
    dbl_NativeBinding,
    targetLanguage=
        safe_text,
    targetType=
        safe_text
)
dbl_Parameter_strategy = st.builds(
    dbl_Parameter,
)
LocalScope_strategy = st.builds(
    LocalScope,
)
dbl_ForStatement_strategy = st.builds(
    dbl_ForStatement,
)
dbl_LocalScopeStatement_strategy = st.builds(
    dbl_LocalScopeStatement,
)
dbl_Constructor_strategy = st.builds(
    dbl_Constructor,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
dbl_Cast_strategy = st.builds(
    dbl_Cast,
)
dbl_CreateObject_strategy = st.builds(
    dbl_CreateObject,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
dbl_IntType_strategy = st.builds(
    dbl_IntType,
)
dbl_DoubleType_strategy = st.builds(
    dbl_DoubleType,
)
dbl_BoolType_strategy = st.builds(
    dbl_BoolType,
)
dbl_StringType_strategy = st.builds(
    dbl_StringType,
)
dbl_VoidType_strategy = st.builds(
    dbl_VoidType,
)
Type_strategy = st.builds(
    Type,
)
dbl_IdExpr_strategy = st.builds(
    dbl_IdExpr,
)
dbl_PrimitiveType_strategy = st.builds(
    dbl_PrimitiveType,
)
dbl_TypedElement_strategy = st.builds(
    dbl_TypedElement,
)
dbl_ArrayDimension_strategy = st.builds(
    dbl_ArrayDimension,
)
dbl_Type_strategy = st.builds(
    dbl_Type,
)
ConstructiveExtension_strategy = st.builds(
    ConstructiveExtension,
)
dbl_ClassContentExtension_strategy = st.builds(
    dbl_ClassContentExtension,
)
dbl_ModuleContentExtension_strategy = st.builds(
    dbl_ModuleContentExtension,
)
Concept_strategy = st.builds(
    Concept,
)
dbl_SuperClassSpecification_strategy = st.builds(
    dbl_SuperClassSpecification,
)
dbl_AnnotationItem_strategy = st.builds(
    dbl_AnnotationItem,
    key=
        safe_text,
    value=
        safe_text
)
dbl_Variable_strategy = st.builds(
    dbl_Variable,
    class_=
        st.booleans(),
    control=
        st.booleans()
)
ConstructiveExtensionAtContentExtensionPoint_strategy = st.builds(
    ConstructiveExtensionAtContentExtensionPoint,
)
dbl_Import_strategy = st.builds(
    dbl_Import,
    file=
        safe_text
)
dbl_Model_strategy = st.builds(
    dbl_Model,
)
Construct_strategy = st.builds(
    Construct,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dbl_AbstractVariable_strategy = st.builds(
    dbl_AbstractVariable,
)
dbl_StructuralSymbolReference_strategy = st.builds(
    dbl_StructuralSymbolReference,
    list=
        st.booleans(),
    composite=
        st.booleans(),
    localScopedReference=
        st.booleans(),
    globalScopedReference=
        st.booleans()
)
dbl_Annotation_strategy = st.builds(
    dbl_Annotation,
)
dbl_Function_strategy = st.builds(
    dbl_Function,
    abstract=
        st.booleans(),
    class_=
        st.booleans()
)
dbl_Module_strategy = st.builds(
    dbl_Module,
)
dbl_Pattern_strategy = st.builds(
    dbl_Pattern,
    top=
        st.booleans()
)
dbl_MetaSymbol_strategy = st.builds(
    dbl_MetaSymbol,
)
dbl_Class_strategy = st.builds(
    dbl_Class,
    active=
        st.booleans()
)
dbl_ExtensibleElement_strategy = st.builds(
    dbl_ExtensibleElement,
    instanceOfExtensionDefinition=
        st.booleans(),
    concreteSyntax=
        safe_text
)
dbl_ExpandExpr_strategy = st.builds(
    dbl_ExpandExpr,
)
dbl_Construct_strategy = st.builds(
    dbl_Construct,
)
dbl_ConstructiveExtensionAtContentExtensionPoint_strategy = st.builds(
    dbl_ConstructiveExtensionAtContentExtensionPoint,
)
ExtensibleElement_strategy = st.builds(
    ExtensibleElement,
)
dbl_Expression_strategy = st.builds(
    dbl_Expression,
)
dbl_SyntaxDefinition_strategy = st.builds(
    dbl_SyntaxDefinition,
)
dbl_ExtensionSemantics_strategy = st.builds(
    dbl_ExtensionSemantics,
)
dbl_Statement_strategy = st.builds(
    dbl_Statement,
)
dbl_SyntaxSymbolClassifier_strategy = st.builds(
    dbl_SyntaxSymbolClassifier,
)
dbl_Extension_strategy = st.builds(
    dbl_Extension,
)
dbl_ConstructiveExtension_strategy = st.builds(
    dbl_ConstructiveExtension,
)
dbl_AnnotateableElement_strategy = st.builds(
    dbl_AnnotateableElement,
)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=QuotedCode_strategy)
@settings(max_examples=50)
def test_quotedcode_instantiation(instance):
    assert isinstance(instance, QuotedCode)

@given(instance=dbl_QuotedStatements_strategy)
@settings(max_examples=50)
def test_dbl_quotedstatements_instantiation(instance):
    assert isinstance(instance, dbl_QuotedStatements)

@given(instance=dbl_QuotedClassContent_strategy)
@settings(max_examples=50)
def test_dbl_quotedclasscontent_instantiation(instance):
    assert isinstance(instance, dbl_QuotedClassContent)

@given(instance=dbl_QuotedModuleContent_strategy)
@settings(max_examples=50)
def test_dbl_quotedmodulecontent_instantiation(instance):
    assert isinstance(instance, dbl_QuotedModuleContent)

@given(instance=dbl_QuotedExpression_strategy)
@settings(max_examples=50)
def test_dbl_quotedexpression_instantiation(instance):
    assert isinstance(instance, dbl_QuotedExpression)

@given(instance=dbl_QuotedCode_strategy)
@settings(max_examples=50)
def test_dbl_quotedcode_instantiation(instance):
    assert isinstance(instance, dbl_QuotedCode)

@given(instance=ExpansionPart_strategy)
@settings(max_examples=50)
def test_expansionpart_instantiation(instance):
    assert isinstance(instance, ExpansionPart)

@given(instance=dbl_ExpandVariablePart_strategy)
@settings(max_examples=50)
def test_dbl_expandvariablepart_instantiation(instance):
    assert isinstance(instance, dbl_ExpandVariablePart)

@given(instance=dbl_ExpandTextPart_strategy)
@settings(max_examples=50)
def test_dbl_expandtextpart_instantiation(instance):
    assert isinstance(instance, dbl_ExpandTextPart)



@given(instance=dbl_ExpandTextPart_strategy)
def test_dbl_expandtextpart_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=dbl_ExpansionPart_strategy)
@settings(max_examples=50)
def test_dbl_expansionpart_instantiation(instance):
    assert isinstance(instance, dbl_ExpansionPart)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=dbl_CreateIdStatement_strategy)
@settings(max_examples=50)
def test_dbl_createidstatement_instantiation(instance):
    assert isinstance(instance, dbl_CreateIdStatement)

@given(instance=ElementarySymbol_strategy)
@settings(max_examples=50)
def test_elementarysymbol_instantiation(instance):
    assert isinstance(instance, ElementarySymbol)

@given(instance=dbl_IntSymbol_strategy)
@settings(max_examples=50)
def test_dbl_intsymbol_instantiation(instance):
    assert isinstance(instance, dbl_IntSymbol)

@given(instance=dbl_StringSymbol_strategy)
@settings(max_examples=50)
def test_dbl_stringsymbol_instantiation(instance):
    assert isinstance(instance, dbl_StringSymbol)

@given(instance=dbl_Keyword_strategy)
@settings(max_examples=50)
def test_dbl_keyword_instantiation(instance):
    assert isinstance(instance, dbl_Keyword)



@given(instance=dbl_Keyword_strategy)
def test_dbl_keyword_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=dbl_IdSymbol_strategy)
@settings(max_examples=50)
def test_dbl_idsymbol_instantiation(instance):
    assert isinstance(instance, dbl_IdSymbol)

@given(instance=PlainSymbolReference_strategy)
@settings(max_examples=50)
def test_plainsymbolreference_instantiation(instance):
    assert isinstance(instance, PlainSymbolReference)

@given(instance=L2SyntaxExpression_strategy)
@settings(max_examples=50)
def test_l2syntaxexpression_instantiation(instance):
    assert isinstance(instance, L2SyntaxExpression)

@given(instance=dbl_SymbolSequence_strategy)
@settings(max_examples=50)
def test_dbl_symbolsequence_instantiation(instance):
    assert isinstance(instance, dbl_SymbolSequence)

@given(instance=SyntaxExpression_strategy)
@settings(max_examples=50)
def test_syntaxexpression_instantiation(instance):
    assert isinstance(instance, SyntaxExpression)

@given(instance=dbl_L1SyntaxExpression_strategy)
@settings(max_examples=50)
def test_dbl_l1syntaxexpression_instantiation(instance):
    assert isinstance(instance, dbl_L1SyntaxExpression)

@given(instance=dbl_L2SyntaxExpression_strategy)
@settings(max_examples=50)
def test_dbl_l2syntaxexpression_instantiation(instance):
    assert isinstance(instance, dbl_L2SyntaxExpression)

@given(instance=dbl_L3SyntaxExpression_strategy)
@settings(max_examples=50)
def test_dbl_l3syntaxexpression_instantiation(instance):
    assert isinstance(instance, dbl_L3SyntaxExpression)

@given(instance=dbl_SyntaxExpression_strategy)
@settings(max_examples=50)
def test_dbl_syntaxexpression_instantiation(instance):
    assert isinstance(instance, dbl_SyntaxExpression)

@given(instance=ComplexSymbol_strategy)
@settings(max_examples=50)
def test_complexsymbol_instantiation(instance):
    assert isinstance(instance, ComplexSymbol)

@given(instance=SyntaxSymbolClassifier_strategy)
@settings(max_examples=50)
def test_syntaxsymbolclassifier_instantiation(instance):
    assert isinstance(instance, SyntaxSymbolClassifier)

@given(instance=dbl_ElementarySymbol_strategy)
@settings(max_examples=50)
def test_dbl_elementarysymbol_instantiation(instance):
    assert isinstance(instance, dbl_ElementarySymbol)

@given(instance=dbl_ComplexSymbol_strategy)
@settings(max_examples=50)
def test_dbl_complexsymbol_instantiation(instance):
    assert isinstance(instance, dbl_ComplexSymbol)

@given(instance=L1SyntaxExpression_strategy)
@settings(max_examples=50)
def test_l1syntaxexpression_instantiation(instance):
    assert isinstance(instance, L1SyntaxExpression)

@given(instance=dbl_PlainSymbolReference_strategy)
@settings(max_examples=50)
def test_dbl_plainsymbolreference_instantiation(instance):
    assert isinstance(instance, dbl_PlainSymbolReference)

@given(instance=dbl_CallPart_strategy)
@settings(max_examples=50)
def test_dbl_callpart_instantiation(instance):
    assert isinstance(instance, dbl_CallPart)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=PredefinedId_strategy)
@settings(max_examples=50)
def test_predefinedid_instantiation(instance):
    assert isinstance(instance, PredefinedId)

@given(instance=dbl_AnnotationLiteral_strategy)
@settings(max_examples=50)
def test_dbl_annotationliteral_instantiation(instance):
    assert isinstance(instance, dbl_AnnotationLiteral)

@given(instance=dbl_MetaLiteral_strategy)
@settings(max_examples=50)
def test_dbl_metaliteral_instantiation(instance):
    assert isinstance(instance, dbl_MetaLiteral)

@given(instance=dbl_TypeLiteral_strategy)
@settings(max_examples=50)
def test_dbl_typeliteral_instantiation(instance):
    assert isinstance(instance, dbl_TypeLiteral)

@given(instance=dbl_SizeOfArray_strategy)
@settings(max_examples=50)
def test_dbl_sizeofarray_instantiation(instance):
    assert isinstance(instance, dbl_SizeOfArray)

@given(instance=dbl_SuperLiteral_strategy)
@settings(max_examples=50)
def test_dbl_superliteral_instantiation(instance):
    assert isinstance(instance, dbl_SuperLiteral)

@given(instance=dbl_MeLiteral_strategy)
@settings(max_examples=50)
def test_dbl_meliteral_instantiation(instance):
    assert isinstance(instance, dbl_MeLiteral)

@given(instance=dbl_PredefinedId_strategy)
@settings(max_examples=50)
def test_dbl_predefinedid_instantiation(instance):
    assert isinstance(instance, dbl_PredefinedId)

@given(instance=dbl_Concept_strategy)
@settings(max_examples=50)
def test_dbl_concept_instantiation(instance):
    assert isinstance(instance, dbl_Concept)

@given(instance=VariableAccess_strategy)
@settings(max_examples=50)
def test_variableaccess_instantiation(instance):
    assert isinstance(instance, VariableAccess)

@given(instance=dbl_MetaAccess_strategy)
@settings(max_examples=50)
def test_dbl_metaaccess_instantiation(instance):
    assert isinstance(instance, dbl_MetaAccess)

@given(instance=ElementAccess_strategy)
@settings(max_examples=50)
def test_elementaccess_instantiation(instance):
    assert isinstance(instance, ElementAccess)

@given(instance=dbl_TypeAccess_strategy)
@settings(max_examples=50)
def test_dbl_typeaccess_instantiation(instance):
    assert isinstance(instance, dbl_TypeAccess)

@given(instance=L1Expr_strategy)
@settings(max_examples=50)
def test_l1expr_instantiation(instance):
    assert isinstance(instance, L1Expr)

@given(instance=dbl_TimeLiteral_strategy)
@settings(max_examples=50)
def test_dbl_timeliteral_instantiation(instance):
    assert isinstance(instance, dbl_TimeLiteral)

@given(instance=dbl_NullLiteral_strategy)
@settings(max_examples=50)
def test_dbl_nullliteral_instantiation(instance):
    assert isinstance(instance, dbl_NullLiteral)

@given(instance=dbl_ActiveLiteral_strategy)
@settings(max_examples=50)
def test_dbl_activeliteral_instantiation(instance):
    assert isinstance(instance, dbl_ActiveLiteral)

@given(instance=L2Expr_strategy)
@settings(max_examples=50)
def test_l2expr_instantiation(instance):
    assert isinstance(instance, L2Expr)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=dbl_Not_strategy)
@settings(max_examples=50)
def test_dbl_not_instantiation(instance):
    assert isinstance(instance, dbl_Not)

@given(instance=dbl_Neg_strategy)
@settings(max_examples=50)
def test_dbl_neg_instantiation(instance):
    assert isinstance(instance, dbl_Neg)

@given(instance=L3Expr_strategy)
@settings(max_examples=50)
def test_l3expr_instantiation(instance):
    assert isinstance(instance, L3Expr)

@given(instance=L4Expr_strategy)
@settings(max_examples=50)
def test_l4expr_instantiation(instance):
    assert isinstance(instance, L4Expr)

@given(instance=L5Expr_strategy)
@settings(max_examples=50)
def test_l5expr_instantiation(instance):
    assert isinstance(instance, L5Expr)

@given(instance=L6Expr_strategy)
@settings(max_examples=50)
def test_l6expr_instantiation(instance):
    assert isinstance(instance, L6Expr)

@given(instance=L7Expr_strategy)
@settings(max_examples=50)
def test_l7expr_instantiation(instance):
    assert isinstance(instance, L7Expr)

@given(instance=L8Expr_strategy)
@settings(max_examples=50)
def test_l8expr_instantiation(instance):
    assert isinstance(instance, L8Expr)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=dbl_LessEqual_strategy)
@settings(max_examples=50)
def test_dbl_lessequal_instantiation(instance):
    assert isinstance(instance, dbl_LessEqual)

@given(instance=dbl_Equal_strategy)
@settings(max_examples=50)
def test_dbl_equal_instantiation(instance):
    assert isinstance(instance, dbl_Equal)

@given(instance=dbl_Less_strategy)
@settings(max_examples=50)
def test_dbl_less_instantiation(instance):
    assert isinstance(instance, dbl_Less)

@given(instance=dbl_GreaterEqual_strategy)
@settings(max_examples=50)
def test_dbl_greaterequal_instantiation(instance):
    assert isinstance(instance, dbl_GreaterEqual)

@given(instance=dbl_InstanceOf_strategy)
@settings(max_examples=50)
def test_dbl_instanceof_instantiation(instance):
    assert isinstance(instance, dbl_InstanceOf)

@given(instance=dbl_And_strategy)
@settings(max_examples=50)
def test_dbl_and_instantiation(instance):
    assert isinstance(instance, dbl_And)

@given(instance=dbl_Div_strategy)
@settings(max_examples=50)
def test_dbl_div_instantiation(instance):
    assert isinstance(instance, dbl_Div)

@given(instance=dbl_Mod_strategy)
@settings(max_examples=50)
def test_dbl_mod_instantiation(instance):
    assert isinstance(instance, dbl_Mod)

@given(instance=dbl_NotEqual_strategy)
@settings(max_examples=50)
def test_dbl_notequal_instantiation(instance):
    assert isinstance(instance, dbl_NotEqual)

@given(instance=dbl_Mul_strategy)
@settings(max_examples=50)
def test_dbl_mul_instantiation(instance):
    assert isinstance(instance, dbl_Mul)

@given(instance=dbl_Minus_strategy)
@settings(max_examples=50)
def test_dbl_minus_instantiation(instance):
    assert isinstance(instance, dbl_Minus)

@given(instance=dbl_Plus_strategy)
@settings(max_examples=50)
def test_dbl_plus_instantiation(instance):
    assert isinstance(instance, dbl_Plus)

@given(instance=dbl_Greater_strategy)
@settings(max_examples=50)
def test_dbl_greater_instantiation(instance):
    assert isinstance(instance, dbl_Greater)

@given(instance=dbl_Or_strategy)
@settings(max_examples=50)
def test_dbl_or_instantiation(instance):
    assert isinstance(instance, dbl_Or)

@given(instance=dbl_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_dbl_doubleliteral_instantiation(instance):
    assert isinstance(instance, dbl_DoubleLiteral)



@given(instance=dbl_DoubleLiteral_strategy)
def test_dbl_doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl_FalseLiteral_strategy)
@settings(max_examples=50)
def test_dbl_falseliteral_instantiation(instance):
    assert isinstance(instance, dbl_FalseLiteral)

@given(instance=dbl_TrueLiteral_strategy)
@settings(max_examples=50)
def test_dbl_trueliteral_instantiation(instance):
    assert isinstance(instance, dbl_TrueLiteral)

@given(instance=dbl_IntLiteral_strategy)
@settings(max_examples=50)
def test_dbl_intliteral_instantiation(instance):
    assert isinstance(instance, dbl_IntLiteral)



@given(instance=dbl_IntLiteral_strategy)
def test_dbl_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl_StringLiteral_strategy)
@settings(max_examples=50)
def test_dbl_stringliteral_instantiation(instance):
    assert isinstance(instance, dbl_StringLiteral)



@given(instance=dbl_StringLiteral_strategy)
def test_dbl_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dbl_ParseExpr_strategy)
@settings(max_examples=50)
def test_dbl_parseexpr_instantiation(instance):
    assert isinstance(instance, dbl_ParseExpr)

@given(instance=dbl_L3Expr_strategy)
@settings(max_examples=50)
def test_dbl_l3expr_instantiation(instance):
    assert isinstance(instance, dbl_L3Expr)

@given(instance=dbl_CodeQuoteExpression_strategy)
@settings(max_examples=50)
def test_dbl_codequoteexpression_instantiation(instance):
    assert isinstance(instance, dbl_CodeQuoteExpression)

@given(instance=dbl_ElementAccess_strategy)
@settings(max_examples=50)
def test_dbl_elementaccess_instantiation(instance):
    assert isinstance(instance, dbl_ElementAccess)

@given(instance=dbl_L4Expr_strategy)
@settings(max_examples=50)
def test_dbl_l4expr_instantiation(instance):
    assert isinstance(instance, dbl_L4Expr)

@given(instance=dbl_UnaryOperator_strategy)
@settings(max_examples=50)
def test_dbl_unaryoperator_instantiation(instance):
    assert isinstance(instance, dbl_UnaryOperator)

@given(instance=dbl_MetaExpr_strategy)
@settings(max_examples=50)
def test_dbl_metaexpr_instantiation(instance):
    assert isinstance(instance, dbl_MetaExpr)

@given(instance=dbl_ExpandExpression_strategy)
@settings(max_examples=50)
def test_dbl_expandexpression_instantiation(instance):
    assert isinstance(instance, dbl_ExpandExpression)

@given(instance=dbl_L5Expr_strategy)
@settings(max_examples=50)
def test_dbl_l5expr_instantiation(instance):
    assert isinstance(instance, dbl_L5Expr)

@given(instance=dbl_L2Expr_strategy)
@settings(max_examples=50)
def test_dbl_l2expr_instantiation(instance):
    assert isinstance(instance, dbl_L2Expr)

@given(instance=dbl_L6Expr_strategy)
@settings(max_examples=50)
def test_dbl_l6expr_instantiation(instance):
    assert isinstance(instance, dbl_L6Expr)

@given(instance=dbl_L1Expr_strategy)
@settings(max_examples=50)
def test_dbl_l1expr_instantiation(instance):
    assert isinstance(instance, dbl_L1Expr)

@given(instance=dbl_SwitchCase_strategy)
@settings(max_examples=50)
def test_dbl_switchcase_instantiation(instance):
    assert isinstance(instance, dbl_SwitchCase)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=dbl_WhileStatement_strategy)
@settings(max_examples=50)
def test_dbl_whilestatement_instantiation(instance):
    assert isinstance(instance, dbl_WhileStatement)

@given(instance=dbl_BinaryOperator_strategy)
@settings(max_examples=50)
def test_dbl_binaryoperator_instantiation(instance):
    assert isinstance(instance, dbl_BinaryOperator)

@given(instance=dbl_L9Expr_strategy)
@settings(max_examples=50)
def test_dbl_l9expr_instantiation(instance):
    assert isinstance(instance, dbl_L9Expr)

@given(instance=dbl_L8Expr_strategy)
@settings(max_examples=50)
def test_dbl_l8expr_instantiation(instance):
    assert isinstance(instance, dbl_L8Expr)

@given(instance=dbl_L7Expr_strategy)
@settings(max_examples=50)
def test_dbl_l7expr_instantiation(instance):
    assert isinstance(instance, dbl_L7Expr)

@given(instance=dbl_VariableAccess_strategy)
@settings(max_examples=50)
def test_dbl_variableaccess_instantiation(instance):
    assert isinstance(instance, dbl_VariableAccess)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=dbl_BreakStatement_strategy)
@settings(max_examples=50)
def test_dbl_breakstatement_instantiation(instance):
    assert isinstance(instance, dbl_BreakStatement)

@given(instance=dbl_Advance_strategy)
@settings(max_examples=50)
def test_dbl_advance_instantiation(instance):
    assert isinstance(instance, dbl_Advance)

@given(instance=dbl_ExpansionStatement_strategy)
@settings(max_examples=50)
def test_dbl_expansionstatement_instantiation(instance):
    assert isinstance(instance, dbl_ExpansionStatement)



@given(instance=dbl_ExpansionStatement_strategy)
def test_dbl_expansionstatement_functionContext_setter(instance):
    original = instance.functionContext
    instance.functionContext = original
    assert instance.functionContext == original



@given(instance=dbl_ExpansionStatement_strategy)
def test_dbl_expansionstatement_classContext_setter(instance):
    original = instance.classContext
    instance.classContext = original
    assert instance.classContext == original



@given(instance=dbl_ExpansionStatement_strategy)
def test_dbl_expansionstatement_variableContext_setter(instance):
    original = instance.variableContext
    instance.variableContext = original
    assert instance.variableContext == original

@given(instance=dbl_Print_strategy)
@settings(max_examples=50)
def test_dbl_print_instantiation(instance):
    assert isinstance(instance, dbl_Print)

@given(instance=dbl_WaitUntil_strategy)
@settings(max_examples=50)
def test_dbl_waituntil_instantiation(instance):
    assert isinstance(instance, dbl_WaitUntil)

@given(instance=dbl_Return_strategy)
@settings(max_examples=50)
def test_dbl_return_instantiation(instance):
    assert isinstance(instance, dbl_Return)

@given(instance=dbl_TargetStatement_strategy)
@settings(max_examples=50)
def test_dbl_targetstatement_instantiation(instance):
    assert isinstance(instance, dbl_TargetStatement)

@given(instance=dbl_ContinueStatement_strategy)
@settings(max_examples=50)
def test_dbl_continuestatement_instantiation(instance):
    assert isinstance(instance, dbl_ContinueStatement)

@given(instance=dbl_Reactivate_strategy)
@settings(max_examples=50)
def test_dbl_reactivate_instantiation(instance):
    assert isinstance(instance, dbl_Reactivate)

@given(instance=dbl_SwitchStatement_strategy)
@settings(max_examples=50)
def test_dbl_switchstatement_instantiation(instance):
    assert isinstance(instance, dbl_SwitchStatement)

@given(instance=dbl_Terminate_strategy)
@settings(max_examples=50)
def test_dbl_terminate_instantiation(instance):
    assert isinstance(instance, dbl_Terminate)

@given(instance=dbl_Yield_strategy)
@settings(max_examples=50)
def test_dbl_yield_instantiation(instance):
    assert isinstance(instance, dbl_Yield)

@given(instance=dbl_FunctionCall_strategy)
@settings(max_examples=50)
def test_dbl_functioncall_instantiation(instance):
    assert isinstance(instance, dbl_FunctionCall)

@given(instance=dbl_ActivateObject_strategy)
@settings(max_examples=50)
def test_dbl_activateobject_instantiation(instance):
    assert isinstance(instance, dbl_ActivateObject)



@given(instance=dbl_ActivateObject_strategy)
def test_dbl_activateobject_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=dbl_Wait_strategy)
@settings(max_examples=50)
def test_dbl_wait_instantiation(instance):
    assert isinstance(instance, dbl_Wait)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=dbl_LocalScope_strategy)
@settings(max_examples=50)
def test_dbl_localscope_instantiation(instance):
    assert isinstance(instance, dbl_LocalScope)

@given(instance=AnnotateableElement_strategy)
@settings(max_examples=50)
def test_annotateableelement_instantiation(instance):
    assert isinstance(instance, AnnotateableElement)

@given(instance=dbl_Assignment_strategy)
@settings(max_examples=50)
def test_dbl_assignment_instantiation(instance):
    assert isinstance(instance, dbl_Assignment)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dbl_TestStatement_strategy)
@settings(max_examples=50)
def test_dbl_teststatement_instantiation(instance):
    assert isinstance(instance, dbl_TestStatement)



@given(instance=dbl_TestStatement_strategy)
def test_dbl_teststatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl_ExpandStatement_strategy)
@settings(max_examples=50)
def test_dbl_expandstatement_instantiation(instance):
    assert isinstance(instance, dbl_ExpandStatement)

@given(instance=dbl_IfStatement_strategy)
@settings(max_examples=50)
def test_dbl_ifstatement_instantiation(instance):
    assert isinstance(instance, dbl_IfStatement)

@given(instance=dbl_SimpleStatement_strategy)
@settings(max_examples=50)
def test_dbl_simplestatement_instantiation(instance):
    assert isinstance(instance, dbl_SimpleStatement)

@given(instance=dbl_LoopStatement_strategy)
@settings(max_examples=50)
def test_dbl_loopstatement_instantiation(instance):
    assert isinstance(instance, dbl_LoopStatement)

@given(instance=dbl_NamedElement_strategy)
@settings(max_examples=50)
def test_dbl_namedelement_instantiation(instance):
    assert isinstance(instance, dbl_NamedElement)



@given(instance=dbl_NamedElement_strategy)
def test_dbl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dbl_NativeBinding_strategy)
@settings(max_examples=50)
def test_dbl_nativebinding_instantiation(instance):
    assert isinstance(instance, dbl_NativeBinding)



@given(instance=dbl_NativeBinding_strategy)
def test_dbl_nativebinding_targetLanguage_setter(instance):
    original = instance.targetLanguage
    instance.targetLanguage = original
    assert instance.targetLanguage == original



@given(instance=dbl_NativeBinding_strategy)
def test_dbl_nativebinding_targetType_setter(instance):
    original = instance.targetType
    instance.targetType = original
    assert instance.targetType == original

@given(instance=dbl_Parameter_strategy)
@settings(max_examples=50)
def test_dbl_parameter_instantiation(instance):
    assert isinstance(instance, dbl_Parameter)

@given(instance=LocalScope_strategy)
@settings(max_examples=50)
def test_localscope_instantiation(instance):
    assert isinstance(instance, LocalScope)

@given(instance=dbl_ForStatement_strategy)
@settings(max_examples=50)
def test_dbl_forstatement_instantiation(instance):
    assert isinstance(instance, dbl_ForStatement)

@given(instance=dbl_LocalScopeStatement_strategy)
@settings(max_examples=50)
def test_dbl_localscopestatement_instantiation(instance):
    assert isinstance(instance, dbl_LocalScopeStatement)

@given(instance=dbl_Constructor_strategy)
@settings(max_examples=50)
def test_dbl_constructor_instantiation(instance):
    assert isinstance(instance, dbl_Constructor)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=dbl_Cast_strategy)
@settings(max_examples=50)
def test_dbl_cast_instantiation(instance):
    assert isinstance(instance, dbl_Cast)

@given(instance=dbl_CreateObject_strategy)
@settings(max_examples=50)
def test_dbl_createobject_instantiation(instance):
    assert isinstance(instance, dbl_CreateObject)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=dbl_IntType_strategy)
@settings(max_examples=50)
def test_dbl_inttype_instantiation(instance):
    assert isinstance(instance, dbl_IntType)

@given(instance=dbl_DoubleType_strategy)
@settings(max_examples=50)
def test_dbl_doubletype_instantiation(instance):
    assert isinstance(instance, dbl_DoubleType)

@given(instance=dbl_BoolType_strategy)
@settings(max_examples=50)
def test_dbl_booltype_instantiation(instance):
    assert isinstance(instance, dbl_BoolType)

@given(instance=dbl_StringType_strategy)
@settings(max_examples=50)
def test_dbl_stringtype_instantiation(instance):
    assert isinstance(instance, dbl_StringType)

@given(instance=dbl_VoidType_strategy)
@settings(max_examples=50)
def test_dbl_voidtype_instantiation(instance):
    assert isinstance(instance, dbl_VoidType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dbl_IdExpr_strategy)
@settings(max_examples=50)
def test_dbl_idexpr_instantiation(instance):
    assert isinstance(instance, dbl_IdExpr)

@given(instance=dbl_PrimitiveType_strategy)
@settings(max_examples=50)
def test_dbl_primitivetype_instantiation(instance):
    assert isinstance(instance, dbl_PrimitiveType)

@given(instance=dbl_TypedElement_strategy)
@settings(max_examples=50)
def test_dbl_typedelement_instantiation(instance):
    assert isinstance(instance, dbl_TypedElement)

@given(instance=dbl_ArrayDimension_strategy)
@settings(max_examples=50)
def test_dbl_arraydimension_instantiation(instance):
    assert isinstance(instance, dbl_ArrayDimension)

@given(instance=dbl_Type_strategy)
@settings(max_examples=50)
def test_dbl_type_instantiation(instance):
    assert isinstance(instance, dbl_Type)

@given(instance=ConstructiveExtension_strategy)
@settings(max_examples=50)
def test_constructiveextension_instantiation(instance):
    assert isinstance(instance, ConstructiveExtension)

@given(instance=dbl_ClassContentExtension_strategy)
@settings(max_examples=50)
def test_dbl_classcontentextension_instantiation(instance):
    assert isinstance(instance, dbl_ClassContentExtension)

@given(instance=dbl_ModuleContentExtension_strategy)
@settings(max_examples=50)
def test_dbl_modulecontentextension_instantiation(instance):
    assert isinstance(instance, dbl_ModuleContentExtension)

@given(instance=Concept_strategy)
@settings(max_examples=50)
def test_concept_instantiation(instance):
    assert isinstance(instance, Concept)

@given(instance=dbl_SuperClassSpecification_strategy)
@settings(max_examples=50)
def test_dbl_superclassspecification_instantiation(instance):
    assert isinstance(instance, dbl_SuperClassSpecification)

@given(instance=dbl_AnnotationItem_strategy)
@settings(max_examples=50)
def test_dbl_annotationitem_instantiation(instance):
    assert isinstance(instance, dbl_AnnotationItem)



@given(instance=dbl_AnnotationItem_strategy)
def test_dbl_annotationitem_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=dbl_AnnotationItem_strategy)
def test_dbl_annotationitem_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl_Variable_strategy)
@settings(max_examples=50)
def test_dbl_variable_instantiation(instance):
    assert isinstance(instance, dbl_Variable)



@given(instance=dbl_Variable_strategy)
def test_dbl_variable_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=dbl_Variable_strategy)
def test_dbl_variable_control_setter(instance):
    original = instance.control
    instance.control = original
    assert instance.control == original

@given(instance=ConstructiveExtensionAtContentExtensionPoint_strategy)
@settings(max_examples=50)
def test_constructiveextensionatcontentextensionpoint_instantiation(instance):
    assert isinstance(instance, ConstructiveExtensionAtContentExtensionPoint)

@given(instance=dbl_Import_strategy)
@settings(max_examples=50)
def test_dbl_import_instantiation(instance):
    assert isinstance(instance, dbl_Import)



@given(instance=dbl_Import_strategy)
def test_dbl_import_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=dbl_Model_strategy)
@settings(max_examples=50)
def test_dbl_model_instantiation(instance):
    assert isinstance(instance, dbl_Model)

@given(instance=Construct_strategy)
@settings(max_examples=50)
def test_construct_instantiation(instance):
    assert isinstance(instance, Construct)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dbl_AbstractVariable_strategy)
@settings(max_examples=50)
def test_dbl_abstractvariable_instantiation(instance):
    assert isinstance(instance, dbl_AbstractVariable)

@given(instance=dbl_StructuralSymbolReference_strategy)
@settings(max_examples=50)
def test_dbl_structuralsymbolreference_instantiation(instance):
    assert isinstance(instance, dbl_StructuralSymbolReference)



@given(instance=dbl_StructuralSymbolReference_strategy)
def test_dbl_structuralsymbolreference_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original



@given(instance=dbl_StructuralSymbolReference_strategy)
def test_dbl_structuralsymbolreference_composite_setter(instance):
    original = instance.composite
    instance.composite = original
    assert instance.composite == original



@given(instance=dbl_StructuralSymbolReference_strategy)
def test_dbl_structuralsymbolreference_localScopedReference_setter(instance):
    original = instance.localScopedReference
    instance.localScopedReference = original
    assert instance.localScopedReference == original



@given(instance=dbl_StructuralSymbolReference_strategy)
def test_dbl_structuralsymbolreference_globalScopedReference_setter(instance):
    original = instance.globalScopedReference
    instance.globalScopedReference = original
    assert instance.globalScopedReference == original

@given(instance=dbl_Annotation_strategy)
@settings(max_examples=50)
def test_dbl_annotation_instantiation(instance):
    assert isinstance(instance, dbl_Annotation)

@given(instance=dbl_Function_strategy)
@settings(max_examples=50)
def test_dbl_function_instantiation(instance):
    assert isinstance(instance, dbl_Function)



@given(instance=dbl_Function_strategy)
def test_dbl_function_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=dbl_Function_strategy)
def test_dbl_function_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=dbl_Module_strategy)
@settings(max_examples=50)
def test_dbl_module_instantiation(instance):
    assert isinstance(instance, dbl_Module)

@given(instance=dbl_Pattern_strategy)
@settings(max_examples=50)
def test_dbl_pattern_instantiation(instance):
    assert isinstance(instance, dbl_Pattern)



@given(instance=dbl_Pattern_strategy)
def test_dbl_pattern_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=dbl_MetaSymbol_strategy)
@settings(max_examples=50)
def test_dbl_metasymbol_instantiation(instance):
    assert isinstance(instance, dbl_MetaSymbol)

@given(instance=dbl_Class_strategy)
@settings(max_examples=50)
def test_dbl_class_instantiation(instance):
    assert isinstance(instance, dbl_Class)



@given(instance=dbl_Class_strategy)
def test_dbl_class_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=dbl_ExtensibleElement_strategy)
@settings(max_examples=50)
def test_dbl_extensibleelement_instantiation(instance):
    assert isinstance(instance, dbl_ExtensibleElement)



@given(instance=dbl_ExtensibleElement_strategy)
def test_dbl_extensibleelement_instanceOfExtensionDefinition_setter(instance):
    original = instance.instanceOfExtensionDefinition
    instance.instanceOfExtensionDefinition = original
    assert instance.instanceOfExtensionDefinition == original



@given(instance=dbl_ExtensibleElement_strategy)
def test_dbl_extensibleelement_concreteSyntax_setter(instance):
    original = instance.concreteSyntax
    instance.concreteSyntax = original
    assert instance.concreteSyntax == original

@given(instance=dbl_ExpandExpr_strategy)
@settings(max_examples=50)
def test_dbl_expandexpr_instantiation(instance):
    assert isinstance(instance, dbl_ExpandExpr)

@given(instance=dbl_Construct_strategy)
@settings(max_examples=50)
def test_dbl_construct_instantiation(instance):
    assert isinstance(instance, dbl_Construct)

@given(instance=dbl_ConstructiveExtensionAtContentExtensionPoint_strategy)
@settings(max_examples=50)
def test_dbl_constructiveextensionatcontentextensionpoint_instantiation(instance):
    assert isinstance(instance, dbl_ConstructiveExtensionAtContentExtensionPoint)

@given(instance=ExtensibleElement_strategy)
@settings(max_examples=50)
def test_extensibleelement_instantiation(instance):
    assert isinstance(instance, ExtensibleElement)

@given(instance=dbl_Expression_strategy)
@settings(max_examples=50)
def test_dbl_expression_instantiation(instance):
    assert isinstance(instance, dbl_Expression)

@given(instance=dbl_SyntaxDefinition_strategy)
@settings(max_examples=50)
def test_dbl_syntaxdefinition_instantiation(instance):
    assert isinstance(instance, dbl_SyntaxDefinition)

@given(instance=dbl_ExtensionSemantics_strategy)
@settings(max_examples=50)
def test_dbl_extensionsemantics_instantiation(instance):
    assert isinstance(instance, dbl_ExtensionSemantics)

@given(instance=dbl_Statement_strategy)
@settings(max_examples=50)
def test_dbl_statement_instantiation(instance):
    assert isinstance(instance, dbl_Statement)

@given(instance=dbl_SyntaxSymbolClassifier_strategy)
@settings(max_examples=50)
def test_dbl_syntaxsymbolclassifier_instantiation(instance):
    assert isinstance(instance, dbl_SyntaxSymbolClassifier)

@given(instance=dbl_Extension_strategy)
@settings(max_examples=50)
def test_dbl_extension_instantiation(instance):
    assert isinstance(instance, dbl_Extension)

@given(instance=dbl_ConstructiveExtension_strategy)
@settings(max_examples=50)
def test_dbl_constructiveextension_instantiation(instance):
    assert isinstance(instance, dbl_ConstructiveExtension)

@given(instance=dbl_AnnotateableElement_strategy)
@settings(max_examples=50)
def test_dbl_annotateableelement_instantiation(instance):
    assert isinstance(instance, dbl_AnnotateableElement)

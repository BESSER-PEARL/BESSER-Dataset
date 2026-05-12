import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dbl_ExpandableElement,
    Module,
    QuotedCode,
    dbl_QuotedStatements,
    dbl_QuotedModuleContent,
    dbl_QuotedExpression,
    dbl_QuotedCode,
    dbl_MappingPart,
    StructuredPropertyType,
    dbl_ReferencePropertyType,
    dbl_CompositePropertyType,
    MappingPart,
    dbl_DynamicMappingPart,
    dbl_FixedMappingPart,
    RhsExpression,
    dbl_OptionalExpr,
    dbl_SequenceExpr,
    dbl_RuleExpr,
    PropertyType,
    dbl_BooleanPropertyType,
    dbl_IntPropertyType,
    dbl_StringPropertyType,
    dbl_StructuredPropertyType,
    dbl_IdPropertyType,
    dbl_PropertyType,
    dbl_TerminalExpr,
    dbl_AlternativeExpr,
    dbl_ArbitraryExpr,
    dbl_AtLeastOneExpr,
    dbl_RuntimeExpr,
    dbl_RhsExpression,
    dbl_TextualSyntaxDef,
    ExtensibleElement,
    VariableAccess,
    dbl_MetaAccess,
    ElementAccess,
    CompositeStatement,
    dbl_ForEachStatement,
    dbl_WhileStatement,
    dbl_ExpandSection,
    dbl_IfStatement,
    dbl_ArgumentExpression,
    SetStatement,
    dbl_EmptySet,
    dbl_AddToSet,
    dbl_RemoveFromSet,
    Construct,
    dbl_Statement,
    dbl_CodeBlock,
    ExpandableElement,
    dbl_TypeAccess,
    dbl_NamedElement,
    Statement,
    dbl_TestStatement,
    dbl_FindContainer,
    dbl_TargetStatement,
    dbl_MappingStatement,
    dbl_PotentiallyHiddenIdElements,
    dbl_IncludePattern,
    dbl_ExpandStatement,
    dbl_ConsiderIdElements,
    StatementExpression,
    dbl_ProcedureCall,
    ExpressionStatement,
    dbl_DeprecatedProcedureCallStatement,
    dbl_StatementExpression,
    SimpleStatement,
    dbl_ResumeGenStatement,
    dbl_ContinueStatement,
    dbl_Reactivate,
    dbl_SetGenContextStatement,
    dbl_SaveGenStatement,
    dbl_Assignment,
    dbl_BreakStatement,
    dbl_SetStatement,
    dbl_Yield,
    dbl_Wait,
    dbl_ActivateObject,
    dbl_ResetGenContextStatement,
    dbl_WaitUntil,
    dbl_Print,
    dbl_Advance,
    dbl_Return,
    dbl_Terminate,
    dbl_ExpressionStatement,
    dbl_SimpleStatement,
    dbl_CompositeStatement,
    AbstractVariable,
    dbl_Constructor,
    ClassSimilar,
    dbl_QuotedClassContent,
    Classifier,
    dbl_AnnotationApplication,
    dbl_Interface,
    dbl_Clazz,
    ModifierExtensionsContainer,
    dbl_NativeBinding,
    ReferableRhsType,
    dbl_AnnotatableElement,
    dbl_Expression,
    dbl_VariableAccess,
    dbl_KeyValuePair,
    Type,
    dbl_Parameter,
    AnnotatableElement,
    CodeBlock,
    dbl_StartCodeBlock,
    dbl_Mapping,
    PrimitiveType,
    dbl_StringType,
    dbl_BoolType,
    dbl_DoubleType,
    dbl_IntType,
    dbl_VoidType,
    dbl_Import,
    dbl_Model,
    NamedExtensible,
    dbl_ClassContentExtension,
    dbl_ModuleContentExtension,
    dbl_Construct,
    TypedElement,
    dbl_ListDimension,
    dbl_PrimitiveType,
    dbl_TypedElement,
    dbl_Type,
    dbl_ModifierExtensionsContainer,
    dbl_ExtensibleElement,
    dbl_EmbeddableExtensionsContainer,
    dbl_IdResolution,
    dbl_Variable,
    dbl_ClassAugment,
    EmbeddableExtensionsContainer,
    dbl_ClassSimilar,
    NamedElement,
    dbl_Pattern,
    dbl_Module,
    dbl_ReferableRhsType,
    dbl_AbstractVariable,
    dbl_Classifier,
    dbl_ExtensionRule,
    dbl_NamedExtensible,
    dbl_ExtensionDefinition,
    dbl_Annotation,
    dbl_TsRule,
    dbl_PropertyBindingExpr,
    dbl_SimpleAnnotation,
    dbl_Procedure,
    dbl_PredefinedId,
    dbl_DepIdentifiableElement,
    SetOp,
    dbl_FirstInSet,
    dbl_IndexOf,
    dbl_Contains,
    dbl_BeforeInSet,
    dbl_AfterInSet,
    dbl_LastInSet,
    dbl_ObjectAt,
    dbl_SizeOfSet,
    PredefinedId,
    dbl_SuperLiteral,
    dbl_TypeLiteral,
    dbl_MetaLiteral,
    dbl_SetOp,
    dbl_MeLiteral,
    Expression,
    dbl_BinaryOperator,
    dbl_EvalExpr,
    dbl_ElementAccess,
    dbl_CodeQuoteExpression,
    dbl_MetaExpr,
    dbl_ExpandExpression,
    dbl_L1Expr,
    L1Expr,
    dbl_StringLiteral,
    dbl_ActiveLiteral,
    dbl_TimeLiteral,
    dbl_TrueLiteral,
    dbl_IntLiteral,
    dbl_FalseLiteral,
    dbl_IdExpr,
    dbl_NullLiteral,
    dbl_DoubleLiteral,
    dbl_CreateObject,
    UnaryOperator,
    dbl_Cast,
    dbl_Not,
    dbl_Neg,
    BinaryOperator,
    dbl_Less,
    dbl_LessEqual,
    dbl_GreaterEqual,
    dbl_Mul,
    dbl_Mod,
    dbl_Plus,
    dbl_NotEqual,
    dbl_Or,
    dbl_Greater,
    dbl_Minus,
    dbl_Equal,
    dbl_InstanceOf,
    dbl_Div,
    dbl_And,
    dbl_UnaryOperator,
    BindingExprOpKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dbl_expandableelement_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpandableElement)


def test_dbl_expandableelement_constructor_exists():
    assert callable(dbl_ExpandableElement.__init__)


def test_dbl_expandableelement_constructor_args():
    sig = inspect.signature(dbl_ExpandableElement.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
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



def test_dbl_mappingpart_is_not_abstract():
    assert not inspect.isabstract(dbl_MappingPart)


def test_dbl_mappingpart_constructor_exists():
    assert callable(dbl_MappingPart.__init__)


def test_dbl_mappingpart_constructor_args():
    sig = inspect.signature(dbl_MappingPart.__init__)
    params = list(sig.parameters.keys())



def test_structuredpropertytype_is_not_abstract():
    assert not inspect.isabstract(StructuredPropertyType)


def test_structuredpropertytype_constructor_exists():
    assert callable(StructuredPropertyType.__init__)


def test_structuredpropertytype_constructor_args():
    sig = inspect.signature(StructuredPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_referencepropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl_ReferencePropertyType)


def test_dbl_referencepropertytype_constructor_exists():
    assert callable(dbl_ReferencePropertyType.__init__)


def test_dbl_referencepropertytype_constructor_args():
    sig = inspect.signature(dbl_ReferencePropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "rawReference" in params, "Missing parameter 'rawReference'"

def test_dbl_referencepropertytype_has_rawReference():
    assert hasattr(dbl_ReferencePropertyType, "rawReference")
    descriptor = None
    for klass in dbl_ReferencePropertyType.__mro__:
        if "rawReference" in klass.__dict__:
            descriptor = klass.__dict__["rawReference"]
            break
    assert isinstance(descriptor, property)



def test_dbl_compositepropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl_CompositePropertyType)


def test_dbl_compositepropertytype_constructor_exists():
    assert callable(dbl_CompositePropertyType.__init__)


def test_dbl_compositepropertytype_constructor_args():
    sig = inspect.signature(dbl_CompositePropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"

def test_dbl_compositepropertytype_has_list():
    assert hasattr(dbl_CompositePropertyType, "list")
    descriptor = None
    for klass in dbl_CompositePropertyType.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_mappingpart_is_not_abstract():
    assert not inspect.isabstract(MappingPart)


def test_mappingpart_constructor_exists():
    assert callable(MappingPart.__init__)


def test_mappingpart_constructor_args():
    sig = inspect.signature(MappingPart.__init__)
    params = list(sig.parameters.keys())



def test_dbl_dynamicmappingpart_is_not_abstract():
    assert not inspect.isabstract(dbl_DynamicMappingPart)


def test_dbl_dynamicmappingpart_constructor_exists():
    assert callable(dbl_DynamicMappingPart.__init__)


def test_dbl_dynamicmappingpart_constructor_args():
    sig = inspect.signature(dbl_DynamicMappingPart.__init__)
    params = list(sig.parameters.keys())



def test_dbl_fixedmappingpart_is_not_abstract():
    assert not inspect.isabstract(dbl_FixedMappingPart)


def test_dbl_fixedmappingpart_constructor_exists():
    assert callable(dbl_FixedMappingPart.__init__)


def test_dbl_fixedmappingpart_constructor_args():
    sig = inspect.signature(dbl_FixedMappingPart.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_dbl_fixedmappingpart_has_code():
    assert hasattr(dbl_FixedMappingPart, "code")
    descriptor = None
    for klass in dbl_FixedMappingPart.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_rhsexpression_is_not_abstract():
    assert not inspect.isabstract(RhsExpression)


def test_rhsexpression_constructor_exists():
    assert callable(RhsExpression.__init__)


def test_rhsexpression_constructor_args():
    sig = inspect.signature(RhsExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_optionalexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_OptionalExpr)


def test_dbl_optionalexpr_constructor_exists():
    assert callable(dbl_OptionalExpr.__init__)


def test_dbl_optionalexpr_constructor_args():
    sig = inspect.signature(dbl_OptionalExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_sequenceexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_SequenceExpr)


def test_dbl_sequenceexpr_constructor_exists():
    assert callable(dbl_SequenceExpr.__init__)


def test_dbl_sequenceexpr_constructor_args():
    sig = inspect.signature(dbl_SequenceExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_ruleexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_RuleExpr)


def test_dbl_ruleexpr_constructor_exists():
    assert callable(dbl_RuleExpr.__init__)


def test_dbl_ruleexpr_constructor_args():
    sig = inspect.signature(dbl_RuleExpr.__init__)
    params = list(sig.parameters.keys())



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_booleanpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl_BooleanPropertyType)


def test_dbl_booleanpropertytype_constructor_exists():
    assert callable(dbl_BooleanPropertyType.__init__)


def test_dbl_booleanpropertytype_constructor_args():
    sig = inspect.signature(dbl_BooleanPropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "terminal" in params, "Missing parameter 'terminal'"

def test_dbl_booleanpropertytype_has_terminal():
    assert hasattr(dbl_BooleanPropertyType, "terminal")
    descriptor = None
    for klass in dbl_BooleanPropertyType.__mro__:
        if "terminal" in klass.__dict__:
            descriptor = klass.__dict__["terminal"]
            break
    assert isinstance(descriptor, property)



def test_dbl_intpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl_IntPropertyType)


def test_dbl_intpropertytype_constructor_exists():
    assert callable(dbl_IntPropertyType.__init__)


def test_dbl_intpropertytype_constructor_args():
    sig = inspect.signature(dbl_IntPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_stringpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl_StringPropertyType)


def test_dbl_stringpropertytype_constructor_exists():
    assert callable(dbl_StringPropertyType.__init__)


def test_dbl_stringpropertytype_constructor_args():
    sig = inspect.signature(dbl_StringPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_structuredpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl_StructuredPropertyType)


def test_dbl_structuredpropertytype_constructor_exists():
    assert callable(dbl_StructuredPropertyType.__init__)


def test_dbl_structuredpropertytype_constructor_args():
    sig = inspect.signature(dbl_StructuredPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_idpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl_IdPropertyType)


def test_dbl_idpropertytype_constructor_exists():
    assert callable(dbl_IdPropertyType.__init__)


def test_dbl_idpropertytype_constructor_args():
    sig = inspect.signature(dbl_IdPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_propertytype_is_not_abstract():
    assert not inspect.isabstract(dbl_PropertyType)


def test_dbl_propertytype_constructor_exists():
    assert callable(dbl_PropertyType.__init__)


def test_dbl_propertytype_constructor_args():
    sig = inspect.signature(dbl_PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_terminalexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_TerminalExpr)


def test_dbl_terminalexpr_constructor_exists():
    assert callable(dbl_TerminalExpr.__init__)


def test_dbl_terminalexpr_constructor_args():
    sig = inspect.signature(dbl_TerminalExpr.__init__)
    params = list(sig.parameters.keys())
    assert "terminal" in params, "Missing parameter 'terminal'"

def test_dbl_terminalexpr_has_terminal():
    assert hasattr(dbl_TerminalExpr, "terminal")
    descriptor = None
    for klass in dbl_TerminalExpr.__mro__:
        if "terminal" in klass.__dict__:
            descriptor = klass.__dict__["terminal"]
            break
    assert isinstance(descriptor, property)



def test_dbl_alternativeexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_AlternativeExpr)


def test_dbl_alternativeexpr_constructor_exists():
    assert callable(dbl_AlternativeExpr.__init__)


def test_dbl_alternativeexpr_constructor_args():
    sig = inspect.signature(dbl_AlternativeExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_arbitraryexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_ArbitraryExpr)


def test_dbl_arbitraryexpr_constructor_exists():
    assert callable(dbl_ArbitraryExpr.__init__)


def test_dbl_arbitraryexpr_constructor_args():
    sig = inspect.signature(dbl_ArbitraryExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_atleastoneexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_AtLeastOneExpr)


def test_dbl_atleastoneexpr_constructor_exists():
    assert callable(dbl_AtLeastOneExpr.__init__)


def test_dbl_atleastoneexpr_constructor_args():
    sig = inspect.signature(dbl_AtLeastOneExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_runtimeexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_RuntimeExpr)


def test_dbl_runtimeexpr_constructor_exists():
    assert callable(dbl_RuntimeExpr.__init__)


def test_dbl_runtimeexpr_constructor_args():
    sig = inspect.signature(dbl_RuntimeExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_rhsexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_RhsExpression)


def test_dbl_rhsexpression_constructor_exists():
    assert callable(dbl_RhsExpression.__init__)


def test_dbl_rhsexpression_constructor_args():
    sig = inspect.signature(dbl_RhsExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_textualsyntaxdef_is_not_abstract():
    assert not inspect.isabstract(dbl_TextualSyntaxDef)


def test_dbl_textualsyntaxdef_constructor_exists():
    assert callable(dbl_TextualSyntaxDef.__init__)


def test_dbl_textualsyntaxdef_constructor_args():
    sig = inspect.signature(dbl_TextualSyntaxDef.__init__)
    params = list(sig.parameters.keys())



def test_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(ExtensibleElement)


def test_extensibleelement_constructor_exists():
    assert callable(ExtensibleElement.__init__)


def test_extensibleelement_constructor_args():
    sig = inspect.signature(ExtensibleElement.__init__)
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



def test_compositestatement_is_not_abstract():
    assert not inspect.isabstract(CompositeStatement)


def test_compositestatement_constructor_exists():
    assert callable(CompositeStatement.__init__)


def test_compositestatement_constructor_args():
    sig = inspect.signature(CompositeStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_foreachstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_ForEachStatement)


def test_dbl_foreachstatement_constructor_exists():
    assert callable(dbl_ForEachStatement.__init__)


def test_dbl_foreachstatement_constructor_args():
    sig = inspect.signature(dbl_ForEachStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_whilestatement_is_not_abstract():
    assert not inspect.isabstract(dbl_WhileStatement)


def test_dbl_whilestatement_constructor_exists():
    assert callable(dbl_WhileStatement.__init__)


def test_dbl_whilestatement_constructor_args():
    sig = inspect.signature(dbl_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_expandsection_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpandSection)


def test_dbl_expandsection_constructor_exists():
    assert callable(dbl_ExpandSection.__init__)


def test_dbl_expandsection_constructor_args():
    sig = inspect.signature(dbl_ExpandSection.__init__)
    params = list(sig.parameters.keys())



def test_dbl_ifstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_IfStatement)


def test_dbl_ifstatement_constructor_exists():
    assert callable(dbl_IfStatement.__init__)


def test_dbl_ifstatement_constructor_args():
    sig = inspect.signature(dbl_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_argumentexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_ArgumentExpression)


def test_dbl_argumentexpression_constructor_exists():
    assert callable(dbl_ArgumentExpression.__init__)


def test_dbl_argumentexpression_constructor_args():
    sig = inspect.signature(dbl_ArgumentExpression.__init__)
    params = list(sig.parameters.keys())



def test_setstatement_is_not_abstract():
    assert not inspect.isabstract(SetStatement)


def test_setstatement_constructor_exists():
    assert callable(SetStatement.__init__)


def test_setstatement_constructor_args():
    sig = inspect.signature(SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_emptyset_is_not_abstract():
    assert not inspect.isabstract(dbl_EmptySet)


def test_dbl_emptyset_constructor_exists():
    assert callable(dbl_EmptySet.__init__)


def test_dbl_emptyset_constructor_args():
    sig = inspect.signature(dbl_EmptySet.__init__)
    params = list(sig.parameters.keys())



def test_dbl_addtoset_is_not_abstract():
    assert not inspect.isabstract(dbl_AddToSet)


def test_dbl_addtoset_constructor_exists():
    assert callable(dbl_AddToSet.__init__)


def test_dbl_addtoset_constructor_args():
    sig = inspect.signature(dbl_AddToSet.__init__)
    params = list(sig.parameters.keys())



def test_dbl_removefromset_is_not_abstract():
    assert not inspect.isabstract(dbl_RemoveFromSet)


def test_dbl_removefromset_constructor_exists():
    assert callable(dbl_RemoveFromSet.__init__)


def test_dbl_removefromset_constructor_args():
    sig = inspect.signature(dbl_RemoveFromSet.__init__)
    params = list(sig.parameters.keys())



def test_construct_is_not_abstract():
    assert not inspect.isabstract(Construct)


def test_construct_constructor_exists():
    assert callable(Construct.__init__)


def test_construct_constructor_args():
    sig = inspect.signature(Construct.__init__)
    params = list(sig.parameters.keys())



def test_dbl_statement_is_not_abstract():
    assert not inspect.isabstract(dbl_Statement)


def test_dbl_statement_constructor_exists():
    assert callable(dbl_Statement.__init__)


def test_dbl_statement_constructor_args():
    sig = inspect.signature(dbl_Statement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_codeblock_is_not_abstract():
    assert not inspect.isabstract(dbl_CodeBlock)


def test_dbl_codeblock_constructor_exists():
    assert callable(dbl_CodeBlock.__init__)


def test_dbl_codeblock_constructor_args():
    sig = inspect.signature(dbl_CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_expandableelement_is_not_abstract():
    assert not inspect.isabstract(ExpandableElement)


def test_expandableelement_constructor_exists():
    assert callable(ExpandableElement.__init__)


def test_expandableelement_constructor_args():
    sig = inspect.signature(ExpandableElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_typeaccess_is_not_abstract():
    assert not inspect.isabstract(dbl_TypeAccess)


def test_dbl_typeaccess_constructor_exists():
    assert callable(dbl_TypeAccess.__init__)


def test_dbl_typeaccess_constructor_args():
    sig = inspect.signature(dbl_TypeAccess.__init__)
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



def test_dbl_findcontainer_is_not_abstract():
    assert not inspect.isabstract(dbl_FindContainer)


def test_dbl_findcontainer_constructor_exists():
    assert callable(dbl_FindContainer.__init__)


def test_dbl_findcontainer_constructor_args():
    sig = inspect.signature(dbl_FindContainer.__init__)
    params = list(sig.parameters.keys())



def test_dbl_targetstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_TargetStatement)


def test_dbl_targetstatement_constructor_exists():
    assert callable(dbl_TargetStatement.__init__)


def test_dbl_targetstatement_constructor_args():
    sig = inspect.signature(dbl_TargetStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_mappingstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_MappingStatement)


def test_dbl_mappingstatement_constructor_exists():
    assert callable(dbl_MappingStatement.__init__)


def test_dbl_mappingstatement_constructor_args():
    sig = inspect.signature(dbl_MappingStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_potentiallyhiddenidelements_is_not_abstract():
    assert not inspect.isabstract(dbl_PotentiallyHiddenIdElements)


def test_dbl_potentiallyhiddenidelements_constructor_exists():
    assert callable(dbl_PotentiallyHiddenIdElements.__init__)


def test_dbl_potentiallyhiddenidelements_constructor_args():
    sig = inspect.signature(dbl_PotentiallyHiddenIdElements.__init__)
    params = list(sig.parameters.keys())



def test_dbl_includepattern_is_not_abstract():
    assert not inspect.isabstract(dbl_IncludePattern)


def test_dbl_includepattern_constructor_exists():
    assert callable(dbl_IncludePattern.__init__)


def test_dbl_includepattern_constructor_args():
    sig = inspect.signature(dbl_IncludePattern.__init__)
    params = list(sig.parameters.keys())



def test_dbl_expandstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpandStatement)


def test_dbl_expandstatement_constructor_exists():
    assert callable(dbl_ExpandStatement.__init__)


def test_dbl_expandstatement_constructor_args():
    sig = inspect.signature(dbl_ExpandStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_consideridelements_is_not_abstract():
    assert not inspect.isabstract(dbl_ConsiderIdElements)


def test_dbl_consideridelements_constructor_exists():
    assert callable(dbl_ConsiderIdElements.__init__)


def test_dbl_consideridelements_constructor_args():
    sig = inspect.signature(dbl_ConsiderIdElements.__init__)
    params = list(sig.parameters.keys())



def test_statementexpression_is_not_abstract():
    assert not inspect.isabstract(StatementExpression)


def test_statementexpression_constructor_exists():
    assert callable(StatementExpression.__init__)


def test_statementexpression_constructor_args():
    sig = inspect.signature(StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_procedurecall_is_not_abstract():
    assert not inspect.isabstract(dbl_ProcedureCall)


def test_dbl_procedurecall_constructor_exists():
    assert callable(dbl_ProcedureCall.__init__)


def test_dbl_procedurecall_constructor_args():
    sig = inspect.signature(dbl_ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ExpressionStatement)


def test_expressionstatement_constructor_exists():
    assert callable(ExpressionStatement.__init__)


def test_expressionstatement_constructor_args():
    sig = inspect.signature(ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_deprecatedprocedurecallstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_DeprecatedProcedureCallStatement)


def test_dbl_deprecatedprocedurecallstatement_constructor_exists():
    assert callable(dbl_DeprecatedProcedureCallStatement.__init__)


def test_dbl_deprecatedprocedurecallstatement_constructor_args():
    sig = inspect.signature(dbl_DeprecatedProcedureCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_statementexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_StatementExpression)


def test_dbl_statementexpression_constructor_exists():
    assert callable(dbl_StatementExpression.__init__)


def test_dbl_statementexpression_constructor_args():
    sig = inspect.signature(dbl_StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_resumegenstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_ResumeGenStatement)


def test_dbl_resumegenstatement_constructor_exists():
    assert callable(dbl_ResumeGenStatement.__init__)


def test_dbl_resumegenstatement_constructor_args():
    sig = inspect.signature(dbl_ResumeGenStatement.__init__)
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



def test_dbl_setgencontextstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_SetGenContextStatement)


def test_dbl_setgencontextstatement_constructor_exists():
    assert callable(dbl_SetGenContextStatement.__init__)


def test_dbl_setgencontextstatement_constructor_args():
    sig = inspect.signature(dbl_SetGenContextStatement.__init__)
    params = list(sig.parameters.keys())
    assert "addAfterContext" in params, "Missing parameter 'addAfterContext'"

def test_dbl_setgencontextstatement_has_addAfterContext():
    assert hasattr(dbl_SetGenContextStatement, "addAfterContext")
    descriptor = None
    for klass in dbl_SetGenContextStatement.__mro__:
        if "addAfterContext" in klass.__dict__:
            descriptor = klass.__dict__["addAfterContext"]
            break
    assert isinstance(descriptor, property)



def test_dbl_savegenstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_SaveGenStatement)


def test_dbl_savegenstatement_constructor_exists():
    assert callable(dbl_SaveGenStatement.__init__)


def test_dbl_savegenstatement_constructor_args():
    sig = inspect.signature(dbl_SaveGenStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_assignment_is_not_abstract():
    assert not inspect.isabstract(dbl_Assignment)


def test_dbl_assignment_constructor_exists():
    assert callable(dbl_Assignment.__init__)


def test_dbl_assignment_constructor_args():
    sig = inspect.signature(dbl_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_dbl_breakstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_BreakStatement)


def test_dbl_breakstatement_constructor_exists():
    assert callable(dbl_BreakStatement.__init__)


def test_dbl_breakstatement_constructor_args():
    sig = inspect.signature(dbl_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_setstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_SetStatement)


def test_dbl_setstatement_constructor_exists():
    assert callable(dbl_SetStatement.__init__)


def test_dbl_setstatement_constructor_args():
    sig = inspect.signature(dbl_SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_yield_is_not_abstract():
    assert not inspect.isabstract(dbl_Yield)


def test_dbl_yield_constructor_exists():
    assert callable(dbl_Yield.__init__)


def test_dbl_yield_constructor_args():
    sig = inspect.signature(dbl_Yield.__init__)
    params = list(sig.parameters.keys())



def test_dbl_wait_is_not_abstract():
    assert not inspect.isabstract(dbl_Wait)


def test_dbl_wait_constructor_exists():
    assert callable(dbl_Wait.__init__)


def test_dbl_wait_constructor_args():
    sig = inspect.signature(dbl_Wait.__init__)
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



def test_dbl_resetgencontextstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_ResetGenContextStatement)


def test_dbl_resetgencontextstatement_constructor_exists():
    assert callable(dbl_ResetGenContextStatement.__init__)


def test_dbl_resetgencontextstatement_constructor_args():
    sig = inspect.signature(dbl_ResetGenContextStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_waituntil_is_not_abstract():
    assert not inspect.isabstract(dbl_WaitUntil)


def test_dbl_waituntil_constructor_exists():
    assert callable(dbl_WaitUntil.__init__)


def test_dbl_waituntil_constructor_args():
    sig = inspect.signature(dbl_WaitUntil.__init__)
    params = list(sig.parameters.keys())



def test_dbl_print_is_not_abstract():
    assert not inspect.isabstract(dbl_Print)


def test_dbl_print_constructor_exists():
    assert callable(dbl_Print.__init__)


def test_dbl_print_constructor_args():
    sig = inspect.signature(dbl_Print.__init__)
    params = list(sig.parameters.keys())



def test_dbl_advance_is_not_abstract():
    assert not inspect.isabstract(dbl_Advance)


def test_dbl_advance_constructor_exists():
    assert callable(dbl_Advance.__init__)


def test_dbl_advance_constructor_args():
    sig = inspect.signature(dbl_Advance.__init__)
    params = list(sig.parameters.keys())



def test_dbl_return_is_not_abstract():
    assert not inspect.isabstract(dbl_Return)


def test_dbl_return_constructor_exists():
    assert callable(dbl_Return.__init__)


def test_dbl_return_constructor_args():
    sig = inspect.signature(dbl_Return.__init__)
    params = list(sig.parameters.keys())



def test_dbl_terminate_is_not_abstract():
    assert not inspect.isabstract(dbl_Terminate)


def test_dbl_terminate_constructor_exists():
    assert callable(dbl_Terminate.__init__)


def test_dbl_terminate_constructor_args():
    sig = inspect.signature(dbl_Terminate.__init__)
    params = list(sig.parameters.keys())



def test_dbl_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(dbl_ExpressionStatement)


def test_dbl_expressionstatement_constructor_exists():
    assert callable(dbl_ExpressionStatement.__init__)


def test_dbl_expressionstatement_constructor_args():
    sig = inspect.signature(dbl_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_simplestatement_is_not_abstract():
    assert not inspect.isabstract(dbl_SimpleStatement)


def test_dbl_simplestatement_constructor_exists():
    assert callable(dbl_SimpleStatement.__init__)


def test_dbl_simplestatement_constructor_args():
    sig = inspect.signature(dbl_SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_compositestatement_is_not_abstract():
    assert not inspect.isabstract(dbl_CompositeStatement)


def test_dbl_compositestatement_constructor_exists():
    assert callable(dbl_CompositeStatement.__init__)


def test_dbl_compositestatement_constructor_args():
    sig = inspect.signature(dbl_CompositeStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_dbl_constructor_is_not_abstract():
    assert not inspect.isabstract(dbl_Constructor)


def test_dbl_constructor_constructor_exists():
    assert callable(dbl_Constructor.__init__)


def test_dbl_constructor_constructor_args():
    sig = inspect.signature(dbl_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_classsimilar_is_not_abstract():
    assert not inspect.isabstract(ClassSimilar)


def test_classsimilar_constructor_exists():
    assert callable(ClassSimilar.__init__)


def test_classsimilar_constructor_args():
    sig = inspect.signature(ClassSimilar.__init__)
    params = list(sig.parameters.keys())



def test_dbl_quotedclasscontent_is_not_abstract():
    assert not inspect.isabstract(dbl_QuotedClassContent)


def test_dbl_quotedclasscontent_constructor_exists():
    assert callable(dbl_QuotedClassContent.__init__)


def test_dbl_quotedclasscontent_constructor_args():
    sig = inspect.signature(dbl_QuotedClassContent.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl_annotationapplication_is_not_abstract():
    assert not inspect.isabstract(dbl_AnnotationApplication)


def test_dbl_annotationapplication_constructor_exists():
    assert callable(dbl_AnnotationApplication.__init__)


def test_dbl_annotationapplication_constructor_args():
    sig = inspect.signature(dbl_AnnotationApplication.__init__)
    params = list(sig.parameters.keys())



def test_dbl_interface_is_not_abstract():
    assert not inspect.isabstract(dbl_Interface)


def test_dbl_interface_constructor_exists():
    assert callable(dbl_Interface.__init__)


def test_dbl_interface_constructor_args():
    sig = inspect.signature(dbl_Interface.__init__)
    params = list(sig.parameters.keys())



def test_dbl_clazz_is_not_abstract():
    assert not inspect.isabstract(dbl_Clazz)


def test_dbl_clazz_constructor_exists():
    assert callable(dbl_Clazz.__init__)


def test_dbl_clazz_constructor_args():
    sig = inspect.signature(dbl_Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_dbl_clazz_has_active():
    assert hasattr(dbl_Clazz, "active")
    descriptor = None
    for klass in dbl_Clazz.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_modifierextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(ModifierExtensionsContainer)


def test_modifierextensionscontainer_constructor_exists():
    assert callable(ModifierExtensionsContainer.__init__)


def test_modifierextensionscontainer_constructor_args():
    sig = inspect.signature(ModifierExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



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



def test_referablerhstype_is_not_abstract():
    assert not inspect.isabstract(ReferableRhsType)


def test_referablerhstype_constructor_exists():
    assert callable(ReferableRhsType.__init__)


def test_referablerhstype_constructor_args():
    sig = inspect.signature(ReferableRhsType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_annotatableelement_is_not_abstract():
    assert not inspect.isabstract(dbl_AnnotatableElement)


def test_dbl_annotatableelement_constructor_exists():
    assert callable(dbl_AnnotatableElement.__init__)


def test_dbl_annotatableelement_constructor_args():
    sig = inspect.signature(dbl_AnnotatableElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_expression_is_not_abstract():
    assert not inspect.isabstract(dbl_Expression)


def test_dbl_expression_constructor_exists():
    assert callable(dbl_Expression.__init__)


def test_dbl_expression_constructor_args():
    sig = inspect.signature(dbl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_variableaccess_is_not_abstract():
    assert not inspect.isabstract(dbl_VariableAccess)


def test_dbl_variableaccess_constructor_exists():
    assert callable(dbl_VariableAccess.__init__)


def test_dbl_variableaccess_constructor_args():
    sig = inspect.signature(dbl_VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl_keyvaluepair_is_not_abstract():
    assert not inspect.isabstract(dbl_KeyValuePair)


def test_dbl_keyvaluepair_constructor_exists():
    assert callable(dbl_KeyValuePair.__init__)


def test_dbl_keyvaluepair_constructor_args():
    sig = inspect.signature(dbl_KeyValuePair.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dbl_parameter_is_not_abstract():
    assert not inspect.isabstract(dbl_Parameter)


def test_dbl_parameter_constructor_exists():
    assert callable(dbl_Parameter.__init__)


def test_dbl_parameter_constructor_args():
    sig = inspect.signature(dbl_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_annotatableelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatableElement)


def test_annotatableelement_constructor_exists():
    assert callable(AnnotatableElement.__init__)


def test_annotatableelement_constructor_args():
    sig = inspect.signature(AnnotatableElement.__init__)
    params = list(sig.parameters.keys())



def test_codeblock_is_not_abstract():
    assert not inspect.isabstract(CodeBlock)


def test_codeblock_constructor_exists():
    assert callable(CodeBlock.__init__)


def test_codeblock_constructor_args():
    sig = inspect.signature(CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_dbl_startcodeblock_is_not_abstract():
    assert not inspect.isabstract(dbl_StartCodeBlock)


def test_dbl_startcodeblock_constructor_exists():
    assert callable(dbl_StartCodeBlock.__init__)


def test_dbl_startcodeblock_constructor_args():
    sig = inspect.signature(dbl_StartCodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_dbl_mapping_is_not_abstract():
    assert not inspect.isabstract(dbl_Mapping)


def test_dbl_mapping_constructor_exists():
    assert callable(dbl_Mapping.__init__)


def test_dbl_mapping_constructor_args():
    sig = inspect.signature(dbl_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_stringtype_is_not_abstract():
    assert not inspect.isabstract(dbl_StringType)


def test_dbl_stringtype_constructor_exists():
    assert callable(dbl_StringType.__init__)


def test_dbl_stringtype_constructor_args():
    sig = inspect.signature(dbl_StringType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_booltype_is_not_abstract():
    assert not inspect.isabstract(dbl_BoolType)


def test_dbl_booltype_constructor_exists():
    assert callable(dbl_BoolType.__init__)


def test_dbl_booltype_constructor_args():
    sig = inspect.signature(dbl_BoolType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_doubletype_is_not_abstract():
    assert not inspect.isabstract(dbl_DoubleType)


def test_dbl_doubletype_constructor_exists():
    assert callable(dbl_DoubleType.__init__)


def test_dbl_doubletype_constructor_args():
    sig = inspect.signature(dbl_DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_inttype_is_not_abstract():
    assert not inspect.isabstract(dbl_IntType)


def test_dbl_inttype_constructor_exists():
    assert callable(dbl_IntType.__init__)


def test_dbl_inttype_constructor_args():
    sig = inspect.signature(dbl_IntType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_voidtype_is_not_abstract():
    assert not inspect.isabstract(dbl_VoidType)


def test_dbl_voidtype_constructor_exists():
    assert callable(dbl_VoidType.__init__)


def test_dbl_voidtype_constructor_args():
    sig = inspect.signature(dbl_VoidType.__init__)
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



def test_namedextensible_is_not_abstract():
    assert not inspect.isabstract(NamedExtensible)


def test_namedextensible_constructor_exists():
    assert callable(NamedExtensible.__init__)


def test_namedextensible_constructor_args():
    sig = inspect.signature(NamedExtensible.__init__)
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



def test_dbl_construct_is_not_abstract():
    assert not inspect.isabstract(dbl_Construct)


def test_dbl_construct_constructor_exists():
    assert callable(dbl_Construct.__init__)


def test_dbl_construct_constructor_args():
    sig = inspect.signature(dbl_Construct.__init__)
    params = list(sig.parameters.keys())
    assert "concreteSyntax" in params, "Missing parameter 'concreteSyntax'"

def test_dbl_construct_has_concreteSyntax():
    assert hasattr(dbl_Construct, "concreteSyntax")
    descriptor = None
    for klass in dbl_Construct.__mro__:
        if "concreteSyntax" in klass.__dict__:
            descriptor = klass.__dict__["concreteSyntax"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl_listdimension_is_not_abstract():
    assert not inspect.isabstract(dbl_ListDimension)


def test_dbl_listdimension_constructor_exists():
    assert callable(dbl_ListDimension.__init__)


def test_dbl_listdimension_constructor_args():
    sig = inspect.signature(dbl_ListDimension.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_dbl_listdimension_has_size():
    assert hasattr(dbl_ListDimension, "size")
    descriptor = None
    for klass in dbl_ListDimension.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



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
    assert "isList" in params, "Missing parameter 'isList'"

def test_dbl_typedelement_has_isList():
    assert hasattr(dbl_TypedElement, "isList")
    descriptor = None
    for klass in dbl_TypedElement.__mro__:
        if "isList" in klass.__dict__:
            descriptor = klass.__dict__["isList"]
            break
    assert isinstance(descriptor, property)



def test_dbl_type_is_not_abstract():
    assert not inspect.isabstract(dbl_Type)


def test_dbl_type_constructor_exists():
    assert callable(dbl_Type.__init__)


def test_dbl_type_constructor_args():
    sig = inspect.signature(dbl_Type.__init__)
    params = list(sig.parameters.keys())



def test_dbl_modifierextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(dbl_ModifierExtensionsContainer)


def test_dbl_modifierextensionscontainer_constructor_exists():
    assert callable(dbl_ModifierExtensionsContainer.__init__)


def test_dbl_modifierextensionscontainer_constructor_args():
    sig = inspect.signature(dbl_ModifierExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_dbl_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(dbl_ExtensibleElement)


def test_dbl_extensibleelement_constructor_exists():
    assert callable(dbl_ExtensibleElement.__init__)


def test_dbl_extensibleelement_constructor_args():
    sig = inspect.signature(dbl_ExtensibleElement.__init__)
    params = list(sig.parameters.keys())
    assert "objectIsExtensionInstance" in params, "Missing parameter 'objectIsExtensionInstance'"

def test_dbl_extensibleelement_has_objectIsExtensionInstance():
    assert hasattr(dbl_ExtensibleElement, "objectIsExtensionInstance")
    descriptor = None
    for klass in dbl_ExtensibleElement.__mro__:
        if "objectIsExtensionInstance" in klass.__dict__:
            descriptor = klass.__dict__["objectIsExtensionInstance"]
            break
    assert isinstance(descriptor, property)



def test_dbl_embeddableextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(dbl_EmbeddableExtensionsContainer)


def test_dbl_embeddableextensionscontainer_constructor_exists():
    assert callable(dbl_EmbeddableExtensionsContainer.__init__)


def test_dbl_embeddableextensionscontainer_constructor_args():
    sig = inspect.signature(dbl_EmbeddableExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_dbl_idresolution_is_not_abstract():
    assert not inspect.isabstract(dbl_IdResolution)


def test_dbl_idresolution_constructor_exists():
    assert callable(dbl_IdResolution.__init__)


def test_dbl_idresolution_constructor_args():
    sig = inspect.signature(dbl_IdResolution.__init__)
    params = list(sig.parameters.keys())
    assert "metaModelPlatformURI" in params, "Missing parameter 'metaModelPlatformURI'"

def test_dbl_idresolution_has_metaModelPlatformURI():
    assert hasattr(dbl_IdResolution, "metaModelPlatformURI")
    descriptor = None
    for klass in dbl_IdResolution.__mro__:
        if "metaModelPlatformURI" in klass.__dict__:
            descriptor = klass.__dict__["metaModelPlatformURI"]
            break
    assert isinstance(descriptor, property)



def test_dbl_variable_is_not_abstract():
    assert not inspect.isabstract(dbl_Variable)


def test_dbl_variable_constructor_exists():
    assert callable(dbl_Variable.__init__)


def test_dbl_variable_constructor_args():
    sig = inspect.signature(dbl_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "clazz" in params, "Missing parameter 'clazz'"
    assert "control" in params, "Missing parameter 'control'"

def test_dbl_variable_has_clazz():
    assert hasattr(dbl_Variable, "clazz")
    descriptor = None
    for klass in dbl_Variable.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
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



def test_dbl_classaugment_is_not_abstract():
    assert not inspect.isabstract(dbl_ClassAugment)


def test_dbl_classaugment_constructor_exists():
    assert callable(dbl_ClassAugment.__init__)


def test_dbl_classaugment_constructor_args():
    sig = inspect.signature(dbl_ClassAugment.__init__)
    params = list(sig.parameters.keys())



def test_embeddableextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(EmbeddableExtensionsContainer)


def test_embeddableextensionscontainer_constructor_exists():
    assert callable(EmbeddableExtensionsContainer.__init__)


def test_embeddableextensionscontainer_constructor_args():
    sig = inspect.signature(EmbeddableExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_dbl_classsimilar_is_not_abstract():
    assert not inspect.isabstract(dbl_ClassSimilar)


def test_dbl_classsimilar_constructor_exists():
    assert callable(dbl_ClassSimilar.__init__)


def test_dbl_classsimilar_constructor_args():
    sig = inspect.signature(dbl_ClassSimilar.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
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



def test_dbl_module_is_not_abstract():
    assert not inspect.isabstract(dbl_Module)


def test_dbl_module_constructor_exists():
    assert callable(dbl_Module.__init__)


def test_dbl_module_constructor_args():
    sig = inspect.signature(dbl_Module.__init__)
    params = list(sig.parameters.keys())



def test_dbl_referablerhstype_is_not_abstract():
    assert not inspect.isabstract(dbl_ReferableRhsType)


def test_dbl_referablerhstype_constructor_exists():
    assert callable(dbl_ReferableRhsType.__init__)


def test_dbl_referablerhstype_constructor_args():
    sig = inspect.signature(dbl_ReferableRhsType.__init__)
    params = list(sig.parameters.keys())



def test_dbl_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(dbl_AbstractVariable)


def test_dbl_abstractvariable_constructor_exists():
    assert callable(dbl_AbstractVariable.__init__)


def test_dbl_abstractvariable_constructor_args():
    sig = inspect.signature(dbl_AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_dbl_classifier_is_not_abstract():
    assert not inspect.isabstract(dbl_Classifier)


def test_dbl_classifier_constructor_exists():
    assert callable(dbl_Classifier.__init__)


def test_dbl_classifier_constructor_args():
    sig = inspect.signature(dbl_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl_extensionrule_is_not_abstract():
    assert not inspect.isabstract(dbl_ExtensionRule)


def test_dbl_extensionrule_constructor_exists():
    assert callable(dbl_ExtensionRule.__init__)


def test_dbl_extensionrule_constructor_args():
    sig = inspect.signature(dbl_ExtensionRule.__init__)
    params = list(sig.parameters.keys())



def test_dbl_namedextensible_is_not_abstract():
    assert not inspect.isabstract(dbl_NamedExtensible)


def test_dbl_namedextensible_constructor_exists():
    assert callable(dbl_NamedExtensible.__init__)


def test_dbl_namedextensible_constructor_args():
    sig = inspect.signature(dbl_NamedExtensible.__init__)
    params = list(sig.parameters.keys())



def test_dbl_extensiondefinition_is_not_abstract():
    assert not inspect.isabstract(dbl_ExtensionDefinition)


def test_dbl_extensiondefinition_constructor_exists():
    assert callable(dbl_ExtensionDefinition.__init__)


def test_dbl_extensiondefinition_constructor_args():
    sig = inspect.signature(dbl_ExtensionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dbl_annotation_is_not_abstract():
    assert not inspect.isabstract(dbl_Annotation)


def test_dbl_annotation_constructor_exists():
    assert callable(dbl_Annotation.__init__)


def test_dbl_annotation_constructor_args():
    sig = inspect.signature(dbl_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dbl_tsrule_is_not_abstract():
    assert not inspect.isabstract(dbl_TsRule)


def test_dbl_tsrule_constructor_exists():
    assert callable(dbl_TsRule.__init__)


def test_dbl_tsrule_constructor_args():
    sig = inspect.signature(dbl_TsRule.__init__)
    params = list(sig.parameters.keys())
    assert "metaClassName" in params, "Missing parameter 'metaClassName'"

def test_dbl_tsrule_has_metaClassName():
    assert hasattr(dbl_TsRule, "metaClassName")
    descriptor = None
    for klass in dbl_TsRule.__mro__:
        if "metaClassName" in klass.__dict__:
            descriptor = klass.__dict__["metaClassName"]
            break
    assert isinstance(descriptor, property)



def test_dbl_propertybindingexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_PropertyBindingExpr)


def test_dbl_propertybindingexpr_constructor_exists():
    assert callable(dbl_PropertyBindingExpr.__init__)


def test_dbl_propertybindingexpr_constructor_args():
    sig = inspect.signature(dbl_PropertyBindingExpr.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dbl_propertybindingexpr_has_operator():
    assert hasattr(dbl_PropertyBindingExpr, "operator")
    descriptor = None
    for klass in dbl_PropertyBindingExpr.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dbl_simpleannotation_is_not_abstract():
    assert not inspect.isabstract(dbl_SimpleAnnotation)


def test_dbl_simpleannotation_constructor_exists():
    assert callable(dbl_SimpleAnnotation.__init__)


def test_dbl_simpleannotation_constructor_args():
    sig = inspect.signature(dbl_SimpleAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl_simpleannotation_has_value():
    assert hasattr(dbl_SimpleAnnotation, "value")
    descriptor = None
    for klass in dbl_SimpleAnnotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl_procedure_is_not_abstract():
    assert not inspect.isabstract(dbl_Procedure)


def test_dbl_procedure_constructor_exists():
    assert callable(dbl_Procedure.__init__)


def test_dbl_procedure_constructor_args():
    sig = inspect.signature(dbl_Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "clazz" in params, "Missing parameter 'clazz'"

def test_dbl_procedure_has_clazz():
    assert hasattr(dbl_Procedure, "clazz")
    descriptor = None
    for klass in dbl_Procedure.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)



def test_dbl_predefinedid_is_not_abstract():
    assert not inspect.isabstract(dbl_PredefinedId)


def test_dbl_predefinedid_constructor_exists():
    assert callable(dbl_PredefinedId.__init__)


def test_dbl_predefinedid_constructor_args():
    sig = inspect.signature(dbl_PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_dbl_depidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(dbl_DepIdentifiableElement)


def test_dbl_depidentifiableelement_constructor_exists():
    assert callable(dbl_DepIdentifiableElement.__init__)


def test_dbl_depidentifiableelement_constructor_args():
    sig = inspect.signature(dbl_DepIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_setop_is_not_abstract():
    assert not inspect.isabstract(SetOp)


def test_setop_constructor_exists():
    assert callable(SetOp.__init__)


def test_setop_constructor_args():
    sig = inspect.signature(SetOp.__init__)
    params = list(sig.parameters.keys())



def test_dbl_firstinset_is_not_abstract():
    assert not inspect.isabstract(dbl_FirstInSet)


def test_dbl_firstinset_constructor_exists():
    assert callable(dbl_FirstInSet.__init__)


def test_dbl_firstinset_constructor_args():
    sig = inspect.signature(dbl_FirstInSet.__init__)
    params = list(sig.parameters.keys())



def test_dbl_indexof_is_not_abstract():
    assert not inspect.isabstract(dbl_IndexOf)


def test_dbl_indexof_constructor_exists():
    assert callable(dbl_IndexOf.__init__)


def test_dbl_indexof_constructor_args():
    sig = inspect.signature(dbl_IndexOf.__init__)
    params = list(sig.parameters.keys())



def test_dbl_contains_is_not_abstract():
    assert not inspect.isabstract(dbl_Contains)


def test_dbl_contains_constructor_exists():
    assert callable(dbl_Contains.__init__)


def test_dbl_contains_constructor_args():
    sig = inspect.signature(dbl_Contains.__init__)
    params = list(sig.parameters.keys())



def test_dbl_beforeinset_is_not_abstract():
    assert not inspect.isabstract(dbl_BeforeInSet)


def test_dbl_beforeinset_constructor_exists():
    assert callable(dbl_BeforeInSet.__init__)


def test_dbl_beforeinset_constructor_args():
    sig = inspect.signature(dbl_BeforeInSet.__init__)
    params = list(sig.parameters.keys())



def test_dbl_afterinset_is_not_abstract():
    assert not inspect.isabstract(dbl_AfterInSet)


def test_dbl_afterinset_constructor_exists():
    assert callable(dbl_AfterInSet.__init__)


def test_dbl_afterinset_constructor_args():
    sig = inspect.signature(dbl_AfterInSet.__init__)
    params = list(sig.parameters.keys())



def test_dbl_lastinset_is_not_abstract():
    assert not inspect.isabstract(dbl_LastInSet)


def test_dbl_lastinset_constructor_exists():
    assert callable(dbl_LastInSet.__init__)


def test_dbl_lastinset_constructor_args():
    sig = inspect.signature(dbl_LastInSet.__init__)
    params = list(sig.parameters.keys())



def test_dbl_objectat_is_not_abstract():
    assert not inspect.isabstract(dbl_ObjectAt)


def test_dbl_objectat_constructor_exists():
    assert callable(dbl_ObjectAt.__init__)


def test_dbl_objectat_constructor_args():
    sig = inspect.signature(dbl_ObjectAt.__init__)
    params = list(sig.parameters.keys())



def test_dbl_sizeofset_is_not_abstract():
    assert not inspect.isabstract(dbl_SizeOfSet)


def test_dbl_sizeofset_constructor_exists():
    assert callable(dbl_SizeOfSet.__init__)


def test_dbl_sizeofset_constructor_args():
    sig = inspect.signature(dbl_SizeOfSet.__init__)
    params = list(sig.parameters.keys())



def test_predefinedid_is_not_abstract():
    assert not inspect.isabstract(PredefinedId)


def test_predefinedid_constructor_exists():
    assert callable(PredefinedId.__init__)


def test_predefinedid_constructor_args():
    sig = inspect.signature(PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_dbl_superliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_SuperLiteral)


def test_dbl_superliteral_constructor_exists():
    assert callable(dbl_SuperLiteral.__init__)


def test_dbl_superliteral_constructor_args():
    sig = inspect.signature(dbl_SuperLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_typeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_TypeLiteral)


def test_dbl_typeliteral_constructor_exists():
    assert callable(dbl_TypeLiteral.__init__)


def test_dbl_typeliteral_constructor_args():
    sig = inspect.signature(dbl_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_metaliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_MetaLiteral)


def test_dbl_metaliteral_constructor_exists():
    assert callable(dbl_MetaLiteral.__init__)


def test_dbl_metaliteral_constructor_args():
    sig = inspect.signature(dbl_MetaLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_setop_is_not_abstract():
    assert not inspect.isabstract(dbl_SetOp)


def test_dbl_setop_constructor_exists():
    assert callable(dbl_SetOp.__init__)


def test_dbl_setop_constructor_args():
    sig = inspect.signature(dbl_SetOp.__init__)
    params = list(sig.parameters.keys())



def test_dbl_meliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_MeLiteral)


def test_dbl_meliteral_constructor_exists():
    assert callable(dbl_MeLiteral.__init__)


def test_dbl_meliteral_constructor_args():
    sig = inspect.signature(dbl_MeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dbl_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(dbl_BinaryOperator)


def test_dbl_binaryoperator_constructor_exists():
    assert callable(dbl_BinaryOperator.__init__)


def test_dbl_binaryoperator_constructor_args():
    sig = inspect.signature(dbl_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl_evalexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_EvalExpr)


def test_dbl_evalexpr_constructor_exists():
    assert callable(dbl_EvalExpr.__init__)


def test_dbl_evalexpr_constructor_args():
    sig = inspect.signature(dbl_EvalExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_elementaccess_is_not_abstract():
    assert not inspect.isabstract(dbl_ElementAccess)


def test_dbl_elementaccess_constructor_exists():
    assert callable(dbl_ElementAccess.__init__)


def test_dbl_elementaccess_constructor_args():
    sig = inspect.signature(dbl_ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl_codequoteexpression_is_not_abstract():
    assert not inspect.isabstract(dbl_CodeQuoteExpression)


def test_dbl_codequoteexpression_constructor_exists():
    assert callable(dbl_CodeQuoteExpression.__init__)


def test_dbl_codequoteexpression_constructor_args():
    sig = inspect.signature(dbl_CodeQuoteExpression.__init__)
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



def test_dbl_l1expr_is_not_abstract():
    assert not inspect.isabstract(dbl_L1Expr)


def test_dbl_l1expr_constructor_exists():
    assert callable(dbl_L1Expr.__init__)


def test_dbl_l1expr_constructor_args():
    sig = inspect.signature(dbl_L1Expr.__init__)
    params = list(sig.parameters.keys())



def test_l1expr_is_not_abstract():
    assert not inspect.isabstract(L1Expr)


def test_l1expr_constructor_exists():
    assert callable(L1Expr.__init__)


def test_l1expr_constructor_args():
    sig = inspect.signature(L1Expr.__init__)
    params = list(sig.parameters.keys())



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



def test_dbl_activeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_ActiveLiteral)


def test_dbl_activeliteral_constructor_exists():
    assert callable(dbl_ActiveLiteral.__init__)


def test_dbl_activeliteral_constructor_args():
    sig = inspect.signature(dbl_ActiveLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_timeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_TimeLiteral)


def test_dbl_timeliteral_constructor_exists():
    assert callable(dbl_TimeLiteral.__init__)


def test_dbl_timeliteral_constructor_args():
    sig = inspect.signature(dbl_TimeLiteral.__init__)
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



def test_dbl_falseliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_FalseLiteral)


def test_dbl_falseliteral_constructor_exists():
    assert callable(dbl_FalseLiteral.__init__)


def test_dbl_falseliteral_constructor_args():
    sig = inspect.signature(dbl_FalseLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl_idexpr_is_not_abstract():
    assert not inspect.isabstract(dbl_IdExpr)


def test_dbl_idexpr_constructor_exists():
    assert callable(dbl_IdExpr.__init__)


def test_dbl_idexpr_constructor_args():
    sig = inspect.signature(dbl_IdExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl_nullliteral_is_not_abstract():
    assert not inspect.isabstract(dbl_NullLiteral)


def test_dbl_nullliteral_constructor_exists():
    assert callable(dbl_NullLiteral.__init__)


def test_dbl_nullliteral_constructor_args():
    sig = inspect.signature(dbl_NullLiteral.__init__)
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



def test_dbl_createobject_is_not_abstract():
    assert not inspect.isabstract(dbl_CreateObject)


def test_dbl_createobject_constructor_exists():
    assert callable(dbl_CreateObject.__init__)


def test_dbl_createobject_constructor_args():
    sig = inspect.signature(dbl_CreateObject.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl_cast_is_not_abstract():
    assert not inspect.isabstract(dbl_Cast)


def test_dbl_cast_constructor_exists():
    assert callable(dbl_Cast.__init__)


def test_dbl_cast_constructor_args():
    sig = inspect.signature(dbl_Cast.__init__)
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



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl_less_is_not_abstract():
    assert not inspect.isabstract(dbl_Less)


def test_dbl_less_constructor_exists():
    assert callable(dbl_Less.__init__)


def test_dbl_less_constructor_args():
    sig = inspect.signature(dbl_Less.__init__)
    params = list(sig.parameters.keys())



def test_dbl_lessequal_is_not_abstract():
    assert not inspect.isabstract(dbl_LessEqual)


def test_dbl_lessequal_constructor_exists():
    assert callable(dbl_LessEqual.__init__)


def test_dbl_lessequal_constructor_args():
    sig = inspect.signature(dbl_LessEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl_greaterequal_is_not_abstract():
    assert not inspect.isabstract(dbl_GreaterEqual)


def test_dbl_greaterequal_constructor_exists():
    assert callable(dbl_GreaterEqual.__init__)


def test_dbl_greaterequal_constructor_args():
    sig = inspect.signature(dbl_GreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl_mul_is_not_abstract():
    assert not inspect.isabstract(dbl_Mul)


def test_dbl_mul_constructor_exists():
    assert callable(dbl_Mul.__init__)


def test_dbl_mul_constructor_args():
    sig = inspect.signature(dbl_Mul.__init__)
    params = list(sig.parameters.keys())



def test_dbl_mod_is_not_abstract():
    assert not inspect.isabstract(dbl_Mod)


def test_dbl_mod_constructor_exists():
    assert callable(dbl_Mod.__init__)


def test_dbl_mod_constructor_args():
    sig = inspect.signature(dbl_Mod.__init__)
    params = list(sig.parameters.keys())



def test_dbl_plus_is_not_abstract():
    assert not inspect.isabstract(dbl_Plus)


def test_dbl_plus_constructor_exists():
    assert callable(dbl_Plus.__init__)


def test_dbl_plus_constructor_args():
    sig = inspect.signature(dbl_Plus.__init__)
    params = list(sig.parameters.keys())



def test_dbl_notequal_is_not_abstract():
    assert not inspect.isabstract(dbl_NotEqual)


def test_dbl_notequal_constructor_exists():
    assert callable(dbl_NotEqual.__init__)


def test_dbl_notequal_constructor_args():
    sig = inspect.signature(dbl_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl_or_is_not_abstract():
    assert not inspect.isabstract(dbl_Or)


def test_dbl_or_constructor_exists():
    assert callable(dbl_Or.__init__)


def test_dbl_or_constructor_args():
    sig = inspect.signature(dbl_Or.__init__)
    params = list(sig.parameters.keys())



def test_dbl_greater_is_not_abstract():
    assert not inspect.isabstract(dbl_Greater)


def test_dbl_greater_constructor_exists():
    assert callable(dbl_Greater.__init__)


def test_dbl_greater_constructor_args():
    sig = inspect.signature(dbl_Greater.__init__)
    params = list(sig.parameters.keys())



def test_dbl_minus_is_not_abstract():
    assert not inspect.isabstract(dbl_Minus)


def test_dbl_minus_constructor_exists():
    assert callable(dbl_Minus.__init__)


def test_dbl_minus_constructor_args():
    sig = inspect.signature(dbl_Minus.__init__)
    params = list(sig.parameters.keys())



def test_dbl_equal_is_not_abstract():
    assert not inspect.isabstract(dbl_Equal)


def test_dbl_equal_constructor_exists():
    assert callable(dbl_Equal.__init__)


def test_dbl_equal_constructor_args():
    sig = inspect.signature(dbl_Equal.__init__)
    params = list(sig.parameters.keys())



def test_dbl_instanceof_is_not_abstract():
    assert not inspect.isabstract(dbl_InstanceOf)


def test_dbl_instanceof_constructor_exists():
    assert callable(dbl_InstanceOf.__init__)


def test_dbl_instanceof_constructor_args():
    sig = inspect.signature(dbl_InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_dbl_div_is_not_abstract():
    assert not inspect.isabstract(dbl_Div)


def test_dbl_div_constructor_exists():
    assert callable(dbl_Div.__init__)


def test_dbl_div_constructor_args():
    sig = inspect.signature(dbl_Div.__init__)
    params = list(sig.parameters.keys())



def test_dbl_and_is_not_abstract():
    assert not inspect.isabstract(dbl_And)


def test_dbl_and_constructor_exists():
    assert callable(dbl_And.__init__)


def test_dbl_and_constructor_args():
    sig = inspect.signature(dbl_And.__init__)
    params = list(sig.parameters.keys())



def test_dbl_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(dbl_UnaryOperator)


def test_dbl_unaryoperator_constructor_exists():
    assert callable(dbl_UnaryOperator.__init__)


def test_dbl_unaryoperator_constructor_args():
    sig = inspect.signature(dbl_UnaryOperator.__init__)
    params = list(sig.parameters.keys())

def test_bindingexpropkind_exists():
    # Check that the Enumeration exists
    assert BindingExprOpKind is not None

def test_bindingexpropkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BindingExprOpKind]
    expected_literals = [
        "ASSIGN",
        "BOOL",
        "ADD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BindingExprOpKind"


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
dbl_ExpandableElement_strategy = st.builds(
    dbl_ExpandableElement,
)
Module_strategy = st.builds(
    Module,
)
QuotedCode_strategy = st.builds(
    QuotedCode,
)
dbl_QuotedStatements_strategy = st.builds(
    dbl_QuotedStatements,
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
dbl_MappingPart_strategy = st.builds(
    dbl_MappingPart,
)
StructuredPropertyType_strategy = st.builds(
    StructuredPropertyType,
)
dbl_ReferencePropertyType_strategy = st.builds(
    dbl_ReferencePropertyType,
    rawReference=
        st.booleans()
)
dbl_CompositePropertyType_strategy = st.builds(
    dbl_CompositePropertyType,
    list=
        st.booleans()
)
MappingPart_strategy = st.builds(
    MappingPart,
)
dbl_DynamicMappingPart_strategy = st.builds(
    dbl_DynamicMappingPart,
)
dbl_FixedMappingPart_strategy = st.builds(
    dbl_FixedMappingPart,
    code=
        safe_text
)
RhsExpression_strategy = st.builds(
    RhsExpression,
)
dbl_OptionalExpr_strategy = st.builds(
    dbl_OptionalExpr,
)
dbl_SequenceExpr_strategy = st.builds(
    dbl_SequenceExpr,
)
dbl_RuleExpr_strategy = st.builds(
    dbl_RuleExpr,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
dbl_BooleanPropertyType_strategy = st.builds(
    dbl_BooleanPropertyType,
    terminal=
        safe_text
)
dbl_IntPropertyType_strategy = st.builds(
    dbl_IntPropertyType,
)
dbl_StringPropertyType_strategy = st.builds(
    dbl_StringPropertyType,
)
dbl_StructuredPropertyType_strategy = st.builds(
    dbl_StructuredPropertyType,
)
dbl_IdPropertyType_strategy = st.builds(
    dbl_IdPropertyType,
)
dbl_PropertyType_strategy = st.builds(
    dbl_PropertyType,
)
dbl_TerminalExpr_strategy = st.builds(
    dbl_TerminalExpr,
    terminal=
        safe_text
)
dbl_AlternativeExpr_strategy = st.builds(
    dbl_AlternativeExpr,
)
dbl_ArbitraryExpr_strategy = st.builds(
    dbl_ArbitraryExpr,
)
dbl_AtLeastOneExpr_strategy = st.builds(
    dbl_AtLeastOneExpr,
)
dbl_RuntimeExpr_strategy = st.builds(
    dbl_RuntimeExpr,
)
dbl_RhsExpression_strategy = st.builds(
    dbl_RhsExpression,
)
dbl_TextualSyntaxDef_strategy = st.builds(
    dbl_TextualSyntaxDef,
)
ExtensibleElement_strategy = st.builds(
    ExtensibleElement,
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
CompositeStatement_strategy = st.builds(
    CompositeStatement,
)
dbl_ForEachStatement_strategy = st.builds(
    dbl_ForEachStatement,
)
dbl_WhileStatement_strategy = st.builds(
    dbl_WhileStatement,
)
dbl_ExpandSection_strategy = st.builds(
    dbl_ExpandSection,
)
dbl_IfStatement_strategy = st.builds(
    dbl_IfStatement,
)
dbl_ArgumentExpression_strategy = st.builds(
    dbl_ArgumentExpression,
)
SetStatement_strategy = st.builds(
    SetStatement,
)
dbl_EmptySet_strategy = st.builds(
    dbl_EmptySet,
)
dbl_AddToSet_strategy = st.builds(
    dbl_AddToSet,
)
dbl_RemoveFromSet_strategy = st.builds(
    dbl_RemoveFromSet,
)
Construct_strategy = st.builds(
    Construct,
)
dbl_Statement_strategy = st.builds(
    dbl_Statement,
)
dbl_CodeBlock_strategy = st.builds(
    dbl_CodeBlock,
)
ExpandableElement_strategy = st.builds(
    ExpandableElement,
)
dbl_TypeAccess_strategy = st.builds(
    dbl_TypeAccess,
)
dbl_NamedElement_strategy = st.builds(
    dbl_NamedElement,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
dbl_TestStatement_strategy = st.builds(
    dbl_TestStatement,
    value=
        safe_text
)
dbl_FindContainer_strategy = st.builds(
    dbl_FindContainer,
)
dbl_TargetStatement_strategy = st.builds(
    dbl_TargetStatement,
)
dbl_MappingStatement_strategy = st.builds(
    dbl_MappingStatement,
)
dbl_PotentiallyHiddenIdElements_strategy = st.builds(
    dbl_PotentiallyHiddenIdElements,
)
dbl_IncludePattern_strategy = st.builds(
    dbl_IncludePattern,
)
dbl_ExpandStatement_strategy = st.builds(
    dbl_ExpandStatement,
)
dbl_ConsiderIdElements_strategy = st.builds(
    dbl_ConsiderIdElements,
)
StatementExpression_strategy = st.builds(
    StatementExpression,
)
dbl_ProcedureCall_strategy = st.builds(
    dbl_ProcedureCall,
)
ExpressionStatement_strategy = st.builds(
    ExpressionStatement,
)
dbl_DeprecatedProcedureCallStatement_strategy = st.builds(
    dbl_DeprecatedProcedureCallStatement,
)
dbl_StatementExpression_strategy = st.builds(
    dbl_StatementExpression,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
dbl_ResumeGenStatement_strategy = st.builds(
    dbl_ResumeGenStatement,
)
dbl_ContinueStatement_strategy = st.builds(
    dbl_ContinueStatement,
)
dbl_Reactivate_strategy = st.builds(
    dbl_Reactivate,
)
dbl_SetGenContextStatement_strategy = st.builds(
    dbl_SetGenContextStatement,
    addAfterContext=
        st.booleans()
)
dbl_SaveGenStatement_strategy = st.builds(
    dbl_SaveGenStatement,
)
dbl_Assignment_strategy = st.builds(
    dbl_Assignment,
)
dbl_BreakStatement_strategy = st.builds(
    dbl_BreakStatement,
)
dbl_SetStatement_strategy = st.builds(
    dbl_SetStatement,
)
dbl_Yield_strategy = st.builds(
    dbl_Yield,
)
dbl_Wait_strategy = st.builds(
    dbl_Wait,
)
dbl_ActivateObject_strategy = st.builds(
    dbl_ActivateObject,
    priority=
        st.integers()
)
dbl_ResetGenContextStatement_strategy = st.builds(
    dbl_ResetGenContextStatement,
)
dbl_WaitUntil_strategy = st.builds(
    dbl_WaitUntil,
)
dbl_Print_strategy = st.builds(
    dbl_Print,
)
dbl_Advance_strategy = st.builds(
    dbl_Advance,
)
dbl_Return_strategy = st.builds(
    dbl_Return,
)
dbl_Terminate_strategy = st.builds(
    dbl_Terminate,
)
dbl_ExpressionStatement_strategy = st.builds(
    dbl_ExpressionStatement,
)
dbl_SimpleStatement_strategy = st.builds(
    dbl_SimpleStatement,
)
dbl_CompositeStatement_strategy = st.builds(
    dbl_CompositeStatement,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
dbl_Constructor_strategy = st.builds(
    dbl_Constructor,
)
ClassSimilar_strategy = st.builds(
    ClassSimilar,
)
dbl_QuotedClassContent_strategy = st.builds(
    dbl_QuotedClassContent,
)
Classifier_strategy = st.builds(
    Classifier,
)
dbl_AnnotationApplication_strategy = st.builds(
    dbl_AnnotationApplication,
)
dbl_Interface_strategy = st.builds(
    dbl_Interface,
)
dbl_Clazz_strategy = st.builds(
    dbl_Clazz,
    active=
        st.booleans()
)
ModifierExtensionsContainer_strategy = st.builds(
    ModifierExtensionsContainer,
)
dbl_NativeBinding_strategy = st.builds(
    dbl_NativeBinding,
    targetLanguage=
        safe_text,
    targetType=
        safe_text
)
ReferableRhsType_strategy = st.builds(
    ReferableRhsType,
)
dbl_AnnotatableElement_strategy = st.builds(
    dbl_AnnotatableElement,
)
dbl_Expression_strategy = st.builds(
    dbl_Expression,
)
dbl_VariableAccess_strategy = st.builds(
    dbl_VariableAccess,
)
dbl_KeyValuePair_strategy = st.builds(
    dbl_KeyValuePair,
)
Type_strategy = st.builds(
    Type,
)
dbl_Parameter_strategy = st.builds(
    dbl_Parameter,
)
AnnotatableElement_strategy = st.builds(
    AnnotatableElement,
)
CodeBlock_strategy = st.builds(
    CodeBlock,
)
dbl_StartCodeBlock_strategy = st.builds(
    dbl_StartCodeBlock,
)
dbl_Mapping_strategy = st.builds(
    dbl_Mapping,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
dbl_StringType_strategy = st.builds(
    dbl_StringType,
)
dbl_BoolType_strategy = st.builds(
    dbl_BoolType,
)
dbl_DoubleType_strategy = st.builds(
    dbl_DoubleType,
)
dbl_IntType_strategy = st.builds(
    dbl_IntType,
)
dbl_VoidType_strategy = st.builds(
    dbl_VoidType,
)
dbl_Import_strategy = st.builds(
    dbl_Import,
    file=
        safe_text
)
dbl_Model_strategy = st.builds(
    dbl_Model,
)
NamedExtensible_strategy = st.builds(
    NamedExtensible,
)
dbl_ClassContentExtension_strategy = st.builds(
    dbl_ClassContentExtension,
)
dbl_ModuleContentExtension_strategy = st.builds(
    dbl_ModuleContentExtension,
)
dbl_Construct_strategy = st.builds(
    dbl_Construct,
    concreteSyntax=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
dbl_ListDimension_strategy = st.builds(
    dbl_ListDimension,
    size=
        st.integers()
)
dbl_PrimitiveType_strategy = st.builds(
    dbl_PrimitiveType,
)
dbl_TypedElement_strategy = st.builds(
    dbl_TypedElement,
    isList=
        st.booleans()
)
dbl_Type_strategy = st.builds(
    dbl_Type,
)
dbl_ModifierExtensionsContainer_strategy = st.builds(
    dbl_ModifierExtensionsContainer,
)
dbl_ExtensibleElement_strategy = st.builds(
    dbl_ExtensibleElement,
    objectIsExtensionInstance=
        st.booleans()
)
dbl_EmbeddableExtensionsContainer_strategy = st.builds(
    dbl_EmbeddableExtensionsContainer,
)
dbl_IdResolution_strategy = st.builds(
    dbl_IdResolution,
    metaModelPlatformURI=
        safe_text
)
dbl_Variable_strategy = st.builds(
    dbl_Variable,
    clazz=
        st.booleans(),
    control=
        st.booleans()
)
dbl_ClassAugment_strategy = st.builds(
    dbl_ClassAugment,
)
EmbeddableExtensionsContainer_strategy = st.builds(
    EmbeddableExtensionsContainer,
)
dbl_ClassSimilar_strategy = st.builds(
    dbl_ClassSimilar,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dbl_Pattern_strategy = st.builds(
    dbl_Pattern,
    top=
        st.booleans()
)
dbl_Module_strategy = st.builds(
    dbl_Module,
)
dbl_ReferableRhsType_strategy = st.builds(
    dbl_ReferableRhsType,
)
dbl_AbstractVariable_strategy = st.builds(
    dbl_AbstractVariable,
)
dbl_Classifier_strategy = st.builds(
    dbl_Classifier,
)
dbl_ExtensionRule_strategy = st.builds(
    dbl_ExtensionRule,
)
dbl_NamedExtensible_strategy = st.builds(
    dbl_NamedExtensible,
)
dbl_ExtensionDefinition_strategy = st.builds(
    dbl_ExtensionDefinition,
)
dbl_Annotation_strategy = st.builds(
    dbl_Annotation,
)
dbl_TsRule_strategy = st.builds(
    dbl_TsRule,
    metaClassName=
        safe_text
)
dbl_PropertyBindingExpr_strategy = st.builds(
    dbl_PropertyBindingExpr,
    operator=
        safe_text
)
dbl_SimpleAnnotation_strategy = st.builds(
    dbl_SimpleAnnotation,
    value=
        safe_text
)
dbl_Procedure_strategy = st.builds(
    dbl_Procedure,
    clazz=
        st.booleans()
)
dbl_PredefinedId_strategy = st.builds(
    dbl_PredefinedId,
)
dbl_DepIdentifiableElement_strategy = st.builds(
    dbl_DepIdentifiableElement,
)
SetOp_strategy = st.builds(
    SetOp,
)
dbl_FirstInSet_strategy = st.builds(
    dbl_FirstInSet,
)
dbl_IndexOf_strategy = st.builds(
    dbl_IndexOf,
)
dbl_Contains_strategy = st.builds(
    dbl_Contains,
)
dbl_BeforeInSet_strategy = st.builds(
    dbl_BeforeInSet,
)
dbl_AfterInSet_strategy = st.builds(
    dbl_AfterInSet,
)
dbl_LastInSet_strategy = st.builds(
    dbl_LastInSet,
)
dbl_ObjectAt_strategy = st.builds(
    dbl_ObjectAt,
)
dbl_SizeOfSet_strategy = st.builds(
    dbl_SizeOfSet,
)
PredefinedId_strategy = st.builds(
    PredefinedId,
)
dbl_SuperLiteral_strategy = st.builds(
    dbl_SuperLiteral,
)
dbl_TypeLiteral_strategy = st.builds(
    dbl_TypeLiteral,
)
dbl_MetaLiteral_strategy = st.builds(
    dbl_MetaLiteral,
)
dbl_SetOp_strategy = st.builds(
    dbl_SetOp,
)
dbl_MeLiteral_strategy = st.builds(
    dbl_MeLiteral,
)
Expression_strategy = st.builds(
    Expression,
)
dbl_BinaryOperator_strategy = st.builds(
    dbl_BinaryOperator,
)
dbl_EvalExpr_strategy = st.builds(
    dbl_EvalExpr,
)
dbl_ElementAccess_strategy = st.builds(
    dbl_ElementAccess,
)
dbl_CodeQuoteExpression_strategy = st.builds(
    dbl_CodeQuoteExpression,
)
dbl_MetaExpr_strategy = st.builds(
    dbl_MetaExpr,
)
dbl_ExpandExpression_strategy = st.builds(
    dbl_ExpandExpression,
)
dbl_L1Expr_strategy = st.builds(
    dbl_L1Expr,
)
L1Expr_strategy = st.builds(
    L1Expr,
)
dbl_StringLiteral_strategy = st.builds(
    dbl_StringLiteral,
    value=
        safe_text
)
dbl_ActiveLiteral_strategy = st.builds(
    dbl_ActiveLiteral,
)
dbl_TimeLiteral_strategy = st.builds(
    dbl_TimeLiteral,
)
dbl_TrueLiteral_strategy = st.builds(
    dbl_TrueLiteral,
)
dbl_IntLiteral_strategy = st.builds(
    dbl_IntLiteral,
    value=
        st.integers()
)
dbl_FalseLiteral_strategy = st.builds(
    dbl_FalseLiteral,
)
dbl_IdExpr_strategy = st.builds(
    dbl_IdExpr,
)
dbl_NullLiteral_strategy = st.builds(
    dbl_NullLiteral,
)
dbl_DoubleLiteral_strategy = st.builds(
    dbl_DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dbl_CreateObject_strategy = st.builds(
    dbl_CreateObject,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
dbl_Cast_strategy = st.builds(
    dbl_Cast,
)
dbl_Not_strategy = st.builds(
    dbl_Not,
)
dbl_Neg_strategy = st.builds(
    dbl_Neg,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
dbl_Less_strategy = st.builds(
    dbl_Less,
)
dbl_LessEqual_strategy = st.builds(
    dbl_LessEqual,
)
dbl_GreaterEqual_strategy = st.builds(
    dbl_GreaterEqual,
)
dbl_Mul_strategy = st.builds(
    dbl_Mul,
)
dbl_Mod_strategy = st.builds(
    dbl_Mod,
)
dbl_Plus_strategy = st.builds(
    dbl_Plus,
)
dbl_NotEqual_strategy = st.builds(
    dbl_NotEqual,
)
dbl_Or_strategy = st.builds(
    dbl_Or,
)
dbl_Greater_strategy = st.builds(
    dbl_Greater,
)
dbl_Minus_strategy = st.builds(
    dbl_Minus,
)
dbl_Equal_strategy = st.builds(
    dbl_Equal,
)
dbl_InstanceOf_strategy = st.builds(
    dbl_InstanceOf,
)
dbl_Div_strategy = st.builds(
    dbl_Div,
)
dbl_And_strategy = st.builds(
    dbl_And,
)
dbl_UnaryOperator_strategy = st.builds(
    dbl_UnaryOperator,
)

@given(instance=dbl_ExpandableElement_strategy)
@settings(max_examples=50)
def test_dbl_expandableelement_instantiation(instance):
    assert isinstance(instance, dbl_ExpandableElement)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=QuotedCode_strategy)
@settings(max_examples=50)
def test_quotedcode_instantiation(instance):
    assert isinstance(instance, QuotedCode)

@given(instance=dbl_QuotedStatements_strategy)
@settings(max_examples=50)
def test_dbl_quotedstatements_instantiation(instance):
    assert isinstance(instance, dbl_QuotedStatements)

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

@given(instance=dbl_MappingPart_strategy)
@settings(max_examples=50)
def test_dbl_mappingpart_instantiation(instance):
    assert isinstance(instance, dbl_MappingPart)

@given(instance=StructuredPropertyType_strategy)
@settings(max_examples=50)
def test_structuredpropertytype_instantiation(instance):
    assert isinstance(instance, StructuredPropertyType)

@given(instance=dbl_ReferencePropertyType_strategy)
@settings(max_examples=50)
def test_dbl_referencepropertytype_instantiation(instance):
    assert isinstance(instance, dbl_ReferencePropertyType)



@given(instance=dbl_ReferencePropertyType_strategy)
def test_dbl_referencepropertytype_rawReference_setter(instance):
    original = instance.rawReference
    instance.rawReference = original
    assert instance.rawReference == original

@given(instance=dbl_CompositePropertyType_strategy)
@settings(max_examples=50)
def test_dbl_compositepropertytype_instantiation(instance):
    assert isinstance(instance, dbl_CompositePropertyType)



@given(instance=dbl_CompositePropertyType_strategy)
def test_dbl_compositepropertytype_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=MappingPart_strategy)
@settings(max_examples=50)
def test_mappingpart_instantiation(instance):
    assert isinstance(instance, MappingPart)

@given(instance=dbl_DynamicMappingPart_strategy)
@settings(max_examples=50)
def test_dbl_dynamicmappingpart_instantiation(instance):
    assert isinstance(instance, dbl_DynamicMappingPart)

@given(instance=dbl_FixedMappingPart_strategy)
@settings(max_examples=50)
def test_dbl_fixedmappingpart_instantiation(instance):
    assert isinstance(instance, dbl_FixedMappingPart)



@given(instance=dbl_FixedMappingPart_strategy)
def test_dbl_fixedmappingpart_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=RhsExpression_strategy)
@settings(max_examples=50)
def test_rhsexpression_instantiation(instance):
    assert isinstance(instance, RhsExpression)

@given(instance=dbl_OptionalExpr_strategy)
@settings(max_examples=50)
def test_dbl_optionalexpr_instantiation(instance):
    assert isinstance(instance, dbl_OptionalExpr)

@given(instance=dbl_SequenceExpr_strategy)
@settings(max_examples=50)
def test_dbl_sequenceexpr_instantiation(instance):
    assert isinstance(instance, dbl_SequenceExpr)

@given(instance=dbl_RuleExpr_strategy)
@settings(max_examples=50)
def test_dbl_ruleexpr_instantiation(instance):
    assert isinstance(instance, dbl_RuleExpr)

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=dbl_BooleanPropertyType_strategy)
@settings(max_examples=50)
def test_dbl_booleanpropertytype_instantiation(instance):
    assert isinstance(instance, dbl_BooleanPropertyType)



@given(instance=dbl_BooleanPropertyType_strategy)
def test_dbl_booleanpropertytype_terminal_setter(instance):
    original = instance.terminal
    instance.terminal = original
    assert instance.terminal == original

@given(instance=dbl_IntPropertyType_strategy)
@settings(max_examples=50)
def test_dbl_intpropertytype_instantiation(instance):
    assert isinstance(instance, dbl_IntPropertyType)

@given(instance=dbl_StringPropertyType_strategy)
@settings(max_examples=50)
def test_dbl_stringpropertytype_instantiation(instance):
    assert isinstance(instance, dbl_StringPropertyType)

@given(instance=dbl_StructuredPropertyType_strategy)
@settings(max_examples=50)
def test_dbl_structuredpropertytype_instantiation(instance):
    assert isinstance(instance, dbl_StructuredPropertyType)

@given(instance=dbl_IdPropertyType_strategy)
@settings(max_examples=50)
def test_dbl_idpropertytype_instantiation(instance):
    assert isinstance(instance, dbl_IdPropertyType)

@given(instance=dbl_PropertyType_strategy)
@settings(max_examples=50)
def test_dbl_propertytype_instantiation(instance):
    assert isinstance(instance, dbl_PropertyType)

@given(instance=dbl_TerminalExpr_strategy)
@settings(max_examples=50)
def test_dbl_terminalexpr_instantiation(instance):
    assert isinstance(instance, dbl_TerminalExpr)



@given(instance=dbl_TerminalExpr_strategy)
def test_dbl_terminalexpr_terminal_setter(instance):
    original = instance.terminal
    instance.terminal = original
    assert instance.terminal == original

@given(instance=dbl_AlternativeExpr_strategy)
@settings(max_examples=50)
def test_dbl_alternativeexpr_instantiation(instance):
    assert isinstance(instance, dbl_AlternativeExpr)

@given(instance=dbl_ArbitraryExpr_strategy)
@settings(max_examples=50)
def test_dbl_arbitraryexpr_instantiation(instance):
    assert isinstance(instance, dbl_ArbitraryExpr)

@given(instance=dbl_AtLeastOneExpr_strategy)
@settings(max_examples=50)
def test_dbl_atleastoneexpr_instantiation(instance):
    assert isinstance(instance, dbl_AtLeastOneExpr)

@given(instance=dbl_RuntimeExpr_strategy)
@settings(max_examples=50)
def test_dbl_runtimeexpr_instantiation(instance):
    assert isinstance(instance, dbl_RuntimeExpr)

@given(instance=dbl_RhsExpression_strategy)
@settings(max_examples=50)
def test_dbl_rhsexpression_instantiation(instance):
    assert isinstance(instance, dbl_RhsExpression)

@given(instance=dbl_TextualSyntaxDef_strategy)
@settings(max_examples=50)
def test_dbl_textualsyntaxdef_instantiation(instance):
    assert isinstance(instance, dbl_TextualSyntaxDef)

@given(instance=ExtensibleElement_strategy)
@settings(max_examples=50)
def test_extensibleelement_instantiation(instance):
    assert isinstance(instance, ExtensibleElement)

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

@given(instance=CompositeStatement_strategy)
@settings(max_examples=50)
def test_compositestatement_instantiation(instance):
    assert isinstance(instance, CompositeStatement)

@given(instance=dbl_ForEachStatement_strategy)
@settings(max_examples=50)
def test_dbl_foreachstatement_instantiation(instance):
    assert isinstance(instance, dbl_ForEachStatement)

@given(instance=dbl_WhileStatement_strategy)
@settings(max_examples=50)
def test_dbl_whilestatement_instantiation(instance):
    assert isinstance(instance, dbl_WhileStatement)

@given(instance=dbl_ExpandSection_strategy)
@settings(max_examples=50)
def test_dbl_expandsection_instantiation(instance):
    assert isinstance(instance, dbl_ExpandSection)

@given(instance=dbl_IfStatement_strategy)
@settings(max_examples=50)
def test_dbl_ifstatement_instantiation(instance):
    assert isinstance(instance, dbl_IfStatement)

@given(instance=dbl_ArgumentExpression_strategy)
@settings(max_examples=50)
def test_dbl_argumentexpression_instantiation(instance):
    assert isinstance(instance, dbl_ArgumentExpression)

@given(instance=SetStatement_strategy)
@settings(max_examples=50)
def test_setstatement_instantiation(instance):
    assert isinstance(instance, SetStatement)

@given(instance=dbl_EmptySet_strategy)
@settings(max_examples=50)
def test_dbl_emptyset_instantiation(instance):
    assert isinstance(instance, dbl_EmptySet)

@given(instance=dbl_AddToSet_strategy)
@settings(max_examples=50)
def test_dbl_addtoset_instantiation(instance):
    assert isinstance(instance, dbl_AddToSet)

@given(instance=dbl_RemoveFromSet_strategy)
@settings(max_examples=50)
def test_dbl_removefromset_instantiation(instance):
    assert isinstance(instance, dbl_RemoveFromSet)

@given(instance=Construct_strategy)
@settings(max_examples=50)
def test_construct_instantiation(instance):
    assert isinstance(instance, Construct)

@given(instance=dbl_Statement_strategy)
@settings(max_examples=50)
def test_dbl_statement_instantiation(instance):
    assert isinstance(instance, dbl_Statement)

@given(instance=dbl_CodeBlock_strategy)
@settings(max_examples=50)
def test_dbl_codeblock_instantiation(instance):
    assert isinstance(instance, dbl_CodeBlock)

@given(instance=ExpandableElement_strategy)
@settings(max_examples=50)
def test_expandableelement_instantiation(instance):
    assert isinstance(instance, ExpandableElement)

@given(instance=dbl_TypeAccess_strategy)
@settings(max_examples=50)
def test_dbl_typeaccess_instantiation(instance):
    assert isinstance(instance, dbl_TypeAccess)

@given(instance=dbl_NamedElement_strategy)
@settings(max_examples=50)
def test_dbl_namedelement_instantiation(instance):
    assert isinstance(instance, dbl_NamedElement)



@given(instance=dbl_NamedElement_strategy)
def test_dbl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=dbl_FindContainer_strategy)
@settings(max_examples=50)
def test_dbl_findcontainer_instantiation(instance):
    assert isinstance(instance, dbl_FindContainer)

@given(instance=dbl_TargetStatement_strategy)
@settings(max_examples=50)
def test_dbl_targetstatement_instantiation(instance):
    assert isinstance(instance, dbl_TargetStatement)

@given(instance=dbl_MappingStatement_strategy)
@settings(max_examples=50)
def test_dbl_mappingstatement_instantiation(instance):
    assert isinstance(instance, dbl_MappingStatement)

@given(instance=dbl_PotentiallyHiddenIdElements_strategy)
@settings(max_examples=50)
def test_dbl_potentiallyhiddenidelements_instantiation(instance):
    assert isinstance(instance, dbl_PotentiallyHiddenIdElements)

@given(instance=dbl_IncludePattern_strategy)
@settings(max_examples=50)
def test_dbl_includepattern_instantiation(instance):
    assert isinstance(instance, dbl_IncludePattern)

@given(instance=dbl_ExpandStatement_strategy)
@settings(max_examples=50)
def test_dbl_expandstatement_instantiation(instance):
    assert isinstance(instance, dbl_ExpandStatement)

@given(instance=dbl_ConsiderIdElements_strategy)
@settings(max_examples=50)
def test_dbl_consideridelements_instantiation(instance):
    assert isinstance(instance, dbl_ConsiderIdElements)

@given(instance=StatementExpression_strategy)
@settings(max_examples=50)
def test_statementexpression_instantiation(instance):
    assert isinstance(instance, StatementExpression)

@given(instance=dbl_ProcedureCall_strategy)
@settings(max_examples=50)
def test_dbl_procedurecall_instantiation(instance):
    assert isinstance(instance, dbl_ProcedureCall)

@given(instance=ExpressionStatement_strategy)
@settings(max_examples=50)
def test_expressionstatement_instantiation(instance):
    assert isinstance(instance, ExpressionStatement)

@given(instance=dbl_DeprecatedProcedureCallStatement_strategy)
@settings(max_examples=50)
def test_dbl_deprecatedprocedurecallstatement_instantiation(instance):
    assert isinstance(instance, dbl_DeprecatedProcedureCallStatement)

@given(instance=dbl_StatementExpression_strategy)
@settings(max_examples=50)
def test_dbl_statementexpression_instantiation(instance):
    assert isinstance(instance, dbl_StatementExpression)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=dbl_ResumeGenStatement_strategy)
@settings(max_examples=50)
def test_dbl_resumegenstatement_instantiation(instance):
    assert isinstance(instance, dbl_ResumeGenStatement)

@given(instance=dbl_ContinueStatement_strategy)
@settings(max_examples=50)
def test_dbl_continuestatement_instantiation(instance):
    assert isinstance(instance, dbl_ContinueStatement)

@given(instance=dbl_Reactivate_strategy)
@settings(max_examples=50)
def test_dbl_reactivate_instantiation(instance):
    assert isinstance(instance, dbl_Reactivate)

@given(instance=dbl_SetGenContextStatement_strategy)
@settings(max_examples=50)
def test_dbl_setgencontextstatement_instantiation(instance):
    assert isinstance(instance, dbl_SetGenContextStatement)



@given(instance=dbl_SetGenContextStatement_strategy)
def test_dbl_setgencontextstatement_addAfterContext_setter(instance):
    original = instance.addAfterContext
    instance.addAfterContext = original
    assert instance.addAfterContext == original

@given(instance=dbl_SaveGenStatement_strategy)
@settings(max_examples=50)
def test_dbl_savegenstatement_instantiation(instance):
    assert isinstance(instance, dbl_SaveGenStatement)

@given(instance=dbl_Assignment_strategy)
@settings(max_examples=50)
def test_dbl_assignment_instantiation(instance):
    assert isinstance(instance, dbl_Assignment)

@given(instance=dbl_BreakStatement_strategy)
@settings(max_examples=50)
def test_dbl_breakstatement_instantiation(instance):
    assert isinstance(instance, dbl_BreakStatement)

@given(instance=dbl_SetStatement_strategy)
@settings(max_examples=50)
def test_dbl_setstatement_instantiation(instance):
    assert isinstance(instance, dbl_SetStatement)

@given(instance=dbl_Yield_strategy)
@settings(max_examples=50)
def test_dbl_yield_instantiation(instance):
    assert isinstance(instance, dbl_Yield)

@given(instance=dbl_Wait_strategy)
@settings(max_examples=50)
def test_dbl_wait_instantiation(instance):
    assert isinstance(instance, dbl_Wait)

@given(instance=dbl_ActivateObject_strategy)
@settings(max_examples=50)
def test_dbl_activateobject_instantiation(instance):
    assert isinstance(instance, dbl_ActivateObject)



@given(instance=dbl_ActivateObject_strategy)
def test_dbl_activateobject_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=dbl_ResetGenContextStatement_strategy)
@settings(max_examples=50)
def test_dbl_resetgencontextstatement_instantiation(instance):
    assert isinstance(instance, dbl_ResetGenContextStatement)

@given(instance=dbl_WaitUntil_strategy)
@settings(max_examples=50)
def test_dbl_waituntil_instantiation(instance):
    assert isinstance(instance, dbl_WaitUntil)

@given(instance=dbl_Print_strategy)
@settings(max_examples=50)
def test_dbl_print_instantiation(instance):
    assert isinstance(instance, dbl_Print)

@given(instance=dbl_Advance_strategy)
@settings(max_examples=50)
def test_dbl_advance_instantiation(instance):
    assert isinstance(instance, dbl_Advance)

@given(instance=dbl_Return_strategy)
@settings(max_examples=50)
def test_dbl_return_instantiation(instance):
    assert isinstance(instance, dbl_Return)

@given(instance=dbl_Terminate_strategy)
@settings(max_examples=50)
def test_dbl_terminate_instantiation(instance):
    assert isinstance(instance, dbl_Terminate)

@given(instance=dbl_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_dbl_expressionstatement_instantiation(instance):
    assert isinstance(instance, dbl_ExpressionStatement)

@given(instance=dbl_SimpleStatement_strategy)
@settings(max_examples=50)
def test_dbl_simplestatement_instantiation(instance):
    assert isinstance(instance, dbl_SimpleStatement)

@given(instance=dbl_CompositeStatement_strategy)
@settings(max_examples=50)
def test_dbl_compositestatement_instantiation(instance):
    assert isinstance(instance, dbl_CompositeStatement)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=dbl_Constructor_strategy)
@settings(max_examples=50)
def test_dbl_constructor_instantiation(instance):
    assert isinstance(instance, dbl_Constructor)

@given(instance=ClassSimilar_strategy)
@settings(max_examples=50)
def test_classsimilar_instantiation(instance):
    assert isinstance(instance, ClassSimilar)

@given(instance=dbl_QuotedClassContent_strategy)
@settings(max_examples=50)
def test_dbl_quotedclasscontent_instantiation(instance):
    assert isinstance(instance, dbl_QuotedClassContent)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=dbl_AnnotationApplication_strategy)
@settings(max_examples=50)
def test_dbl_annotationapplication_instantiation(instance):
    assert isinstance(instance, dbl_AnnotationApplication)

@given(instance=dbl_Interface_strategy)
@settings(max_examples=50)
def test_dbl_interface_instantiation(instance):
    assert isinstance(instance, dbl_Interface)

@given(instance=dbl_Clazz_strategy)
@settings(max_examples=50)
def test_dbl_clazz_instantiation(instance):
    assert isinstance(instance, dbl_Clazz)



@given(instance=dbl_Clazz_strategy)
def test_dbl_clazz_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=ModifierExtensionsContainer_strategy)
@settings(max_examples=50)
def test_modifierextensionscontainer_instantiation(instance):
    assert isinstance(instance, ModifierExtensionsContainer)

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

@given(instance=ReferableRhsType_strategy)
@settings(max_examples=50)
def test_referablerhstype_instantiation(instance):
    assert isinstance(instance, ReferableRhsType)

@given(instance=dbl_AnnotatableElement_strategy)
@settings(max_examples=50)
def test_dbl_annotatableelement_instantiation(instance):
    assert isinstance(instance, dbl_AnnotatableElement)

@given(instance=dbl_Expression_strategy)
@settings(max_examples=50)
def test_dbl_expression_instantiation(instance):
    assert isinstance(instance, dbl_Expression)

@given(instance=dbl_VariableAccess_strategy)
@settings(max_examples=50)
def test_dbl_variableaccess_instantiation(instance):
    assert isinstance(instance, dbl_VariableAccess)

@given(instance=dbl_KeyValuePair_strategy)
@settings(max_examples=50)
def test_dbl_keyvaluepair_instantiation(instance):
    assert isinstance(instance, dbl_KeyValuePair)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dbl_Parameter_strategy)
@settings(max_examples=50)
def test_dbl_parameter_instantiation(instance):
    assert isinstance(instance, dbl_Parameter)

@given(instance=AnnotatableElement_strategy)
@settings(max_examples=50)
def test_annotatableelement_instantiation(instance):
    assert isinstance(instance, AnnotatableElement)

@given(instance=CodeBlock_strategy)
@settings(max_examples=50)
def test_codeblock_instantiation(instance):
    assert isinstance(instance, CodeBlock)

@given(instance=dbl_StartCodeBlock_strategy)
@settings(max_examples=50)
def test_dbl_startcodeblock_instantiation(instance):
    assert isinstance(instance, dbl_StartCodeBlock)

@given(instance=dbl_Mapping_strategy)
@settings(max_examples=50)
def test_dbl_mapping_instantiation(instance):
    assert isinstance(instance, dbl_Mapping)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=dbl_StringType_strategy)
@settings(max_examples=50)
def test_dbl_stringtype_instantiation(instance):
    assert isinstance(instance, dbl_StringType)

@given(instance=dbl_BoolType_strategy)
@settings(max_examples=50)
def test_dbl_booltype_instantiation(instance):
    assert isinstance(instance, dbl_BoolType)

@given(instance=dbl_DoubleType_strategy)
@settings(max_examples=50)
def test_dbl_doubletype_instantiation(instance):
    assert isinstance(instance, dbl_DoubleType)

@given(instance=dbl_IntType_strategy)
@settings(max_examples=50)
def test_dbl_inttype_instantiation(instance):
    assert isinstance(instance, dbl_IntType)

@given(instance=dbl_VoidType_strategy)
@settings(max_examples=50)
def test_dbl_voidtype_instantiation(instance):
    assert isinstance(instance, dbl_VoidType)

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

@given(instance=NamedExtensible_strategy)
@settings(max_examples=50)
def test_namedextensible_instantiation(instance):
    assert isinstance(instance, NamedExtensible)

@given(instance=dbl_ClassContentExtension_strategy)
@settings(max_examples=50)
def test_dbl_classcontentextension_instantiation(instance):
    assert isinstance(instance, dbl_ClassContentExtension)

@given(instance=dbl_ModuleContentExtension_strategy)
@settings(max_examples=50)
def test_dbl_modulecontentextension_instantiation(instance):
    assert isinstance(instance, dbl_ModuleContentExtension)

@given(instance=dbl_Construct_strategy)
@settings(max_examples=50)
def test_dbl_construct_instantiation(instance):
    assert isinstance(instance, dbl_Construct)



@given(instance=dbl_Construct_strategy)
def test_dbl_construct_concreteSyntax_setter(instance):
    original = instance.concreteSyntax
    instance.concreteSyntax = original
    assert instance.concreteSyntax == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=dbl_ListDimension_strategy)
@settings(max_examples=50)
def test_dbl_listdimension_instantiation(instance):
    assert isinstance(instance, dbl_ListDimension)



@given(instance=dbl_ListDimension_strategy)
def test_dbl_listdimension_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=dbl_PrimitiveType_strategy)
@settings(max_examples=50)
def test_dbl_primitivetype_instantiation(instance):
    assert isinstance(instance, dbl_PrimitiveType)

@given(instance=dbl_TypedElement_strategy)
@settings(max_examples=50)
def test_dbl_typedelement_instantiation(instance):
    assert isinstance(instance, dbl_TypedElement)



@given(instance=dbl_TypedElement_strategy)
def test_dbl_typedelement_isList_setter(instance):
    original = instance.isList
    instance.isList = original
    assert instance.isList == original

@given(instance=dbl_Type_strategy)
@settings(max_examples=50)
def test_dbl_type_instantiation(instance):
    assert isinstance(instance, dbl_Type)

@given(instance=dbl_ModifierExtensionsContainer_strategy)
@settings(max_examples=50)
def test_dbl_modifierextensionscontainer_instantiation(instance):
    assert isinstance(instance, dbl_ModifierExtensionsContainer)

@given(instance=dbl_ExtensibleElement_strategy)
@settings(max_examples=50)
def test_dbl_extensibleelement_instantiation(instance):
    assert isinstance(instance, dbl_ExtensibleElement)



@given(instance=dbl_ExtensibleElement_strategy)
def test_dbl_extensibleelement_objectIsExtensionInstance_setter(instance):
    original = instance.objectIsExtensionInstance
    instance.objectIsExtensionInstance = original
    assert instance.objectIsExtensionInstance == original

@given(instance=dbl_EmbeddableExtensionsContainer_strategy)
@settings(max_examples=50)
def test_dbl_embeddableextensionscontainer_instantiation(instance):
    assert isinstance(instance, dbl_EmbeddableExtensionsContainer)

@given(instance=dbl_IdResolution_strategy)
@settings(max_examples=50)
def test_dbl_idresolution_instantiation(instance):
    assert isinstance(instance, dbl_IdResolution)



@given(instance=dbl_IdResolution_strategy)
def test_dbl_idresolution_metaModelPlatformURI_setter(instance):
    original = instance.metaModelPlatformURI
    instance.metaModelPlatformURI = original
    assert instance.metaModelPlatformURI == original

@given(instance=dbl_Variable_strategy)
@settings(max_examples=50)
def test_dbl_variable_instantiation(instance):
    assert isinstance(instance, dbl_Variable)



@given(instance=dbl_Variable_strategy)
def test_dbl_variable_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original



@given(instance=dbl_Variable_strategy)
def test_dbl_variable_control_setter(instance):
    original = instance.control
    instance.control = original
    assert instance.control == original

@given(instance=dbl_ClassAugment_strategy)
@settings(max_examples=50)
def test_dbl_classaugment_instantiation(instance):
    assert isinstance(instance, dbl_ClassAugment)

@given(instance=EmbeddableExtensionsContainer_strategy)
@settings(max_examples=50)
def test_embeddableextensionscontainer_instantiation(instance):
    assert isinstance(instance, EmbeddableExtensionsContainer)

@given(instance=dbl_ClassSimilar_strategy)
@settings(max_examples=50)
def test_dbl_classsimilar_instantiation(instance):
    assert isinstance(instance, dbl_ClassSimilar)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dbl_Pattern_strategy)
@settings(max_examples=50)
def test_dbl_pattern_instantiation(instance):
    assert isinstance(instance, dbl_Pattern)



@given(instance=dbl_Pattern_strategy)
def test_dbl_pattern_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=dbl_Module_strategy)
@settings(max_examples=50)
def test_dbl_module_instantiation(instance):
    assert isinstance(instance, dbl_Module)

@given(instance=dbl_ReferableRhsType_strategy)
@settings(max_examples=50)
def test_dbl_referablerhstype_instantiation(instance):
    assert isinstance(instance, dbl_ReferableRhsType)

@given(instance=dbl_AbstractVariable_strategy)
@settings(max_examples=50)
def test_dbl_abstractvariable_instantiation(instance):
    assert isinstance(instance, dbl_AbstractVariable)

@given(instance=dbl_Classifier_strategy)
@settings(max_examples=50)
def test_dbl_classifier_instantiation(instance):
    assert isinstance(instance, dbl_Classifier)

@given(instance=dbl_ExtensionRule_strategy)
@settings(max_examples=50)
def test_dbl_extensionrule_instantiation(instance):
    assert isinstance(instance, dbl_ExtensionRule)

@given(instance=dbl_NamedExtensible_strategy)
@settings(max_examples=50)
def test_dbl_namedextensible_instantiation(instance):
    assert isinstance(instance, dbl_NamedExtensible)

@given(instance=dbl_ExtensionDefinition_strategy)
@settings(max_examples=50)
def test_dbl_extensiondefinition_instantiation(instance):
    assert isinstance(instance, dbl_ExtensionDefinition)

@given(instance=dbl_Annotation_strategy)
@settings(max_examples=50)
def test_dbl_annotation_instantiation(instance):
    assert isinstance(instance, dbl_Annotation)

@given(instance=dbl_TsRule_strategy)
@settings(max_examples=50)
def test_dbl_tsrule_instantiation(instance):
    assert isinstance(instance, dbl_TsRule)



@given(instance=dbl_TsRule_strategy)
def test_dbl_tsrule_metaClassName_setter(instance):
    original = instance.metaClassName
    instance.metaClassName = original
    assert instance.metaClassName == original

@given(instance=dbl_PropertyBindingExpr_strategy)
@settings(max_examples=50)
def test_dbl_propertybindingexpr_instantiation(instance):
    assert isinstance(instance, dbl_PropertyBindingExpr)



@given(instance=dbl_PropertyBindingExpr_strategy)
def test_dbl_propertybindingexpr_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dbl_SimpleAnnotation_strategy)
@settings(max_examples=50)
def test_dbl_simpleannotation_instantiation(instance):
    assert isinstance(instance, dbl_SimpleAnnotation)



@given(instance=dbl_SimpleAnnotation_strategy)
def test_dbl_simpleannotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl_Procedure_strategy)
@settings(max_examples=50)
def test_dbl_procedure_instantiation(instance):
    assert isinstance(instance, dbl_Procedure)



@given(instance=dbl_Procedure_strategy)
def test_dbl_procedure_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=dbl_PredefinedId_strategy)
@settings(max_examples=50)
def test_dbl_predefinedid_instantiation(instance):
    assert isinstance(instance, dbl_PredefinedId)

@given(instance=dbl_DepIdentifiableElement_strategy)
@settings(max_examples=50)
def test_dbl_depidentifiableelement_instantiation(instance):
    assert isinstance(instance, dbl_DepIdentifiableElement)

@given(instance=SetOp_strategy)
@settings(max_examples=50)
def test_setop_instantiation(instance):
    assert isinstance(instance, SetOp)

@given(instance=dbl_FirstInSet_strategy)
@settings(max_examples=50)
def test_dbl_firstinset_instantiation(instance):
    assert isinstance(instance, dbl_FirstInSet)

@given(instance=dbl_IndexOf_strategy)
@settings(max_examples=50)
def test_dbl_indexof_instantiation(instance):
    assert isinstance(instance, dbl_IndexOf)

@given(instance=dbl_Contains_strategy)
@settings(max_examples=50)
def test_dbl_contains_instantiation(instance):
    assert isinstance(instance, dbl_Contains)

@given(instance=dbl_BeforeInSet_strategy)
@settings(max_examples=50)
def test_dbl_beforeinset_instantiation(instance):
    assert isinstance(instance, dbl_BeforeInSet)

@given(instance=dbl_AfterInSet_strategy)
@settings(max_examples=50)
def test_dbl_afterinset_instantiation(instance):
    assert isinstance(instance, dbl_AfterInSet)

@given(instance=dbl_LastInSet_strategy)
@settings(max_examples=50)
def test_dbl_lastinset_instantiation(instance):
    assert isinstance(instance, dbl_LastInSet)

@given(instance=dbl_ObjectAt_strategy)
@settings(max_examples=50)
def test_dbl_objectat_instantiation(instance):
    assert isinstance(instance, dbl_ObjectAt)

@given(instance=dbl_SizeOfSet_strategy)
@settings(max_examples=50)
def test_dbl_sizeofset_instantiation(instance):
    assert isinstance(instance, dbl_SizeOfSet)

@given(instance=PredefinedId_strategy)
@settings(max_examples=50)
def test_predefinedid_instantiation(instance):
    assert isinstance(instance, PredefinedId)

@given(instance=dbl_SuperLiteral_strategy)
@settings(max_examples=50)
def test_dbl_superliteral_instantiation(instance):
    assert isinstance(instance, dbl_SuperLiteral)

@given(instance=dbl_TypeLiteral_strategy)
@settings(max_examples=50)
def test_dbl_typeliteral_instantiation(instance):
    assert isinstance(instance, dbl_TypeLiteral)

@given(instance=dbl_MetaLiteral_strategy)
@settings(max_examples=50)
def test_dbl_metaliteral_instantiation(instance):
    assert isinstance(instance, dbl_MetaLiteral)

@given(instance=dbl_SetOp_strategy)
@settings(max_examples=50)
def test_dbl_setop_instantiation(instance):
    assert isinstance(instance, dbl_SetOp)

@given(instance=dbl_MeLiteral_strategy)
@settings(max_examples=50)
def test_dbl_meliteral_instantiation(instance):
    assert isinstance(instance, dbl_MeLiteral)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dbl_BinaryOperator_strategy)
@settings(max_examples=50)
def test_dbl_binaryoperator_instantiation(instance):
    assert isinstance(instance, dbl_BinaryOperator)

@given(instance=dbl_EvalExpr_strategy)
@settings(max_examples=50)
def test_dbl_evalexpr_instantiation(instance):
    assert isinstance(instance, dbl_EvalExpr)

@given(instance=dbl_ElementAccess_strategy)
@settings(max_examples=50)
def test_dbl_elementaccess_instantiation(instance):
    assert isinstance(instance, dbl_ElementAccess)

@given(instance=dbl_CodeQuoteExpression_strategy)
@settings(max_examples=50)
def test_dbl_codequoteexpression_instantiation(instance):
    assert isinstance(instance, dbl_CodeQuoteExpression)

@given(instance=dbl_MetaExpr_strategy)
@settings(max_examples=50)
def test_dbl_metaexpr_instantiation(instance):
    assert isinstance(instance, dbl_MetaExpr)

@given(instance=dbl_ExpandExpression_strategy)
@settings(max_examples=50)
def test_dbl_expandexpression_instantiation(instance):
    assert isinstance(instance, dbl_ExpandExpression)

@given(instance=dbl_L1Expr_strategy)
@settings(max_examples=50)
def test_dbl_l1expr_instantiation(instance):
    assert isinstance(instance, dbl_L1Expr)

@given(instance=L1Expr_strategy)
@settings(max_examples=50)
def test_l1expr_instantiation(instance):
    assert isinstance(instance, L1Expr)

@given(instance=dbl_StringLiteral_strategy)
@settings(max_examples=50)
def test_dbl_stringliteral_instantiation(instance):
    assert isinstance(instance, dbl_StringLiteral)



@given(instance=dbl_StringLiteral_strategy)
def test_dbl_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl_ActiveLiteral_strategy)
@settings(max_examples=50)
def test_dbl_activeliteral_instantiation(instance):
    assert isinstance(instance, dbl_ActiveLiteral)

@given(instance=dbl_TimeLiteral_strategy)
@settings(max_examples=50)
def test_dbl_timeliteral_instantiation(instance):
    assert isinstance(instance, dbl_TimeLiteral)

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

@given(instance=dbl_FalseLiteral_strategy)
@settings(max_examples=50)
def test_dbl_falseliteral_instantiation(instance):
    assert isinstance(instance, dbl_FalseLiteral)

@given(instance=dbl_IdExpr_strategy)
@settings(max_examples=50)
def test_dbl_idexpr_instantiation(instance):
    assert isinstance(instance, dbl_IdExpr)

@given(instance=dbl_NullLiteral_strategy)
@settings(max_examples=50)
def test_dbl_nullliteral_instantiation(instance):
    assert isinstance(instance, dbl_NullLiteral)

@given(instance=dbl_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_dbl_doubleliteral_instantiation(instance):
    assert isinstance(instance, dbl_DoubleLiteral)



@given(instance=dbl_DoubleLiteral_strategy)
def test_dbl_doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl_CreateObject_strategy)
@settings(max_examples=50)
def test_dbl_createobject_instantiation(instance):
    assert isinstance(instance, dbl_CreateObject)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=dbl_Cast_strategy)
@settings(max_examples=50)
def test_dbl_cast_instantiation(instance):
    assert isinstance(instance, dbl_Cast)

@given(instance=dbl_Not_strategy)
@settings(max_examples=50)
def test_dbl_not_instantiation(instance):
    assert isinstance(instance, dbl_Not)

@given(instance=dbl_Neg_strategy)
@settings(max_examples=50)
def test_dbl_neg_instantiation(instance):
    assert isinstance(instance, dbl_Neg)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=dbl_Less_strategy)
@settings(max_examples=50)
def test_dbl_less_instantiation(instance):
    assert isinstance(instance, dbl_Less)

@given(instance=dbl_LessEqual_strategy)
@settings(max_examples=50)
def test_dbl_lessequal_instantiation(instance):
    assert isinstance(instance, dbl_LessEqual)

@given(instance=dbl_GreaterEqual_strategy)
@settings(max_examples=50)
def test_dbl_greaterequal_instantiation(instance):
    assert isinstance(instance, dbl_GreaterEqual)

@given(instance=dbl_Mul_strategy)
@settings(max_examples=50)
def test_dbl_mul_instantiation(instance):
    assert isinstance(instance, dbl_Mul)

@given(instance=dbl_Mod_strategy)
@settings(max_examples=50)
def test_dbl_mod_instantiation(instance):
    assert isinstance(instance, dbl_Mod)

@given(instance=dbl_Plus_strategy)
@settings(max_examples=50)
def test_dbl_plus_instantiation(instance):
    assert isinstance(instance, dbl_Plus)

@given(instance=dbl_NotEqual_strategy)
@settings(max_examples=50)
def test_dbl_notequal_instantiation(instance):
    assert isinstance(instance, dbl_NotEqual)

@given(instance=dbl_Or_strategy)
@settings(max_examples=50)
def test_dbl_or_instantiation(instance):
    assert isinstance(instance, dbl_Or)

@given(instance=dbl_Greater_strategy)
@settings(max_examples=50)
def test_dbl_greater_instantiation(instance):
    assert isinstance(instance, dbl_Greater)

@given(instance=dbl_Minus_strategy)
@settings(max_examples=50)
def test_dbl_minus_instantiation(instance):
    assert isinstance(instance, dbl_Minus)

@given(instance=dbl_Equal_strategy)
@settings(max_examples=50)
def test_dbl_equal_instantiation(instance):
    assert isinstance(instance, dbl_Equal)

@given(instance=dbl_InstanceOf_strategy)
@settings(max_examples=50)
def test_dbl_instanceof_instantiation(instance):
    assert isinstance(instance, dbl_InstanceOf)

@given(instance=dbl_Div_strategy)
@settings(max_examples=50)
def test_dbl_div_instantiation(instance):
    assert isinstance(instance, dbl_Div)

@given(instance=dbl_And_strategy)
@settings(max_examples=50)
def test_dbl_and_instantiation(instance):
    assert isinstance(instance, dbl_And)

@given(instance=dbl_UnaryOperator_strategy)
@settings(max_examples=50)
def test_dbl_unaryoperator_instantiation(instance):
    assert isinstance(instance, dbl_UnaryOperator)

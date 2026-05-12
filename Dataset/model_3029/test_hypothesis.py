import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    odemcustom_QuotedCode,
    odemcustom_ExpandableElement,
    Module,
    QuotedCode,
    odemcustom_QuotedModuleContent,
    odemcustom_QuotedStatements,
    odemcustom_QuotedExpression,
    MappingPart,
    odemcustom_DynamicMappingPart,
    odemcustom_FixedMappingPart,
    odemcustom_PropertyType,
    odemcustom_MappingPart,
    StructuredPropertyType,
    odemcustom_ReferencePropertyType,
    odemcustom_CompositePropertyType,
    ModifierExtensionsContainer,
    odemcustom_Constructor,
    ClassSimilar,
    odemcustom_QuotedClassContent,
    Classifier,
    odemcustom_Interface,
    odemcustom_Clazz,
    PrimitiveType,
    odemcustom_BoolType,
    odemcustom_IntType,
    odemcustom_DoubleType,
    odemcustom_VoidType,
    Type,
    odemcustom_NativeBinding,
    ReferableRhsType,
    odemcustom_AnnotatableElement,
    odemcustom_KeyValuePair,
    odemcustom_AnnotationApplication,
    AnnotatableElement,
    CodeBlock,
    odemcustom_StartCodeBlock,
    TypedElement,
    odemcustom_StringType,
    odemcustom_Import,
    odemcustom_Model,
    odemcustom_PrimitiveType,
    odemcustom_TypedElement,
    odemcustom_Type,
    odemcustom_ModifierExtensionsContainer,
    odemcustom_Extension,
    odemcustom_EmbeddableExtensionsContainer,
    odemcustom_IdResolution,
    odemcustom_ClassAugment,
    EmbeddableExtensionsContainer,
    odemcustom_ClassSimilar,
    NamedElement,
    odemcustom_SimpleAnnotation,
    odemcustom_Procedure,
    odemcustom_Pattern,
    odemcustom_ExtensionDefinition,
    odemcustom_Annotation,
    odemcustom_Module,
    odemcustom_Classifier,
    NamedExtension,
    odemcustom_Construct,
    PropertyType,
    odemcustom_StringPropertyType,
    odemcustom_BooleanPropertyType,
    odemcustom_StructuredPropertyType,
    odemcustom_IntPropertyType,
    odemcustom_IdPropertyType,
    odemcustom_RhsExpression,
    odemcustom_ReferableRhsType,
    RhsExpression,
    odemcustom_AlternativeExpr,
    odemcustom_RuntimeExpr,
    odemcustom_ArbitraryExpr,
    odemcustom_OptionalExpr,
    odemcustom_TerminalExpr,
    odemcustom_AtLeastOneExpr,
    odemcustom_PropertyBindingExpr,
    odemcustom_SequenceExpr,
    odemcustom_RuleExpr,
    odemcustom_TsRule,
    odemcustom_ExtensionRule,
    odemcustom_Mapping,
    odemcustom_TextualSyntaxDef,
    odemcustom_ModuleContentExtension,
    odemcustom_ClassContentExtension,
    Extension,
    odemcustom_NamedExtension,
    VariableAccess,
    odemcustom_MetaAccess,
    ElementAccess,
    odemcustom_ArgumentExpression,
    odemcustom_PredefinedId,
    odemcustom_DepIdentifiableElement,
    UnaryOperator,
    odemcustom_Neg,
    SetOp,
    odemcustom_FirstInSet,
    odemcustom_AfterInSet,
    odemcustom_BeforeInSet,
    odemcustom_LastInSet,
    odemcustom_Contains,
    odemcustom_ObjectAt,
    odemcustom_IndexOf,
    odemcustom_SizeOfSet,
    PredefinedId,
    odemcustom_MetaLiteral,
    odemcustom_SetOp,
    odemcustom_SuperLiteral,
    odemcustom_TypeLiteral,
    odemcustom_MeLiteral,
    odemcustom_Cast,
    odemcustom_Not,
    BinaryOperator,
    odemcustom_Less,
    odemcustom_GreaterEqual,
    odemcustom_LessEqual,
    odemcustom_Mul,
    odemcustom_Mod,
    odemcustom_Minus,
    odemcustom_Greater,
    odemcustom_And,
    odemcustom_InstanceOf,
    odemcustom_NotEqual,
    odemcustom_Or,
    odemcustom_Equal,
    odemcustom_Div,
    odemcustom_Plus,
    Expression,
    odemcustom_BinaryOperator,
    odemcustom_UnaryOperator,
    odemcustom_IdExpr,
    odemcustom_DoubleLiteral,
    odemcustom_FalseLiteral,
    odemcustom_CodeQuoteExpression,
    odemcustom_CreateObject,
    odemcustom_IntLiteral,
    odemcustom_EvalExpr,
    odemcustom_ActiveLiteral,
    odemcustom_StringLiteral,
    odemcustom_TrueLiteral,
    odemcustom_MetaExpr,
    odemcustom_TimeLiteral,
    odemcustom_NullLiteral,
    odemcustom_ElementAccess,
    odemcustom_L1Expr,
    CompositeStatement,
    odemcustom_ExpandSection,
    odemcustom_WhileStatement,
    odemcustom_ForEachStatement,
    odemcustom_IfStatement,
    SetStatement,
    odemcustom_EmptySet,
    odemcustom_AddToSet,
    odemcustom_RemoveFromSet,
    Statement,
    odemcustom_MappingStatement,
    odemcustom_FindContainer,
    odemcustom_TargetStatement,
    odemcustom_IncludePattern,
    odemcustom_ConsiderIdElements,
    odemcustom_PotentiallyHiddenIdElements,
    odemcustom_TestStatement,
    odemcustom_ExpandStatement,
    AbstractVariable,
    odemcustom_Parameter,
    odemcustom_Variable,
    odemcustom_AbstractVariable,
    StatementExpression,
    odemcustom_ExpandExpression,
    odemcustom_ProcedureCall,
    ExpressionStatement,
    odemcustom_DeprecatedProcedureCallStatement,
    odemcustom_StatementExpression,
    SimpleStatement,
    odemcustom_Advance,
    odemcustom_SaveGenStatement,
    odemcustom_Reactivate,
    odemcustom_ResumeGenStatement,
    odemcustom_Terminate,
    odemcustom_ResetGenContextStatement,
    odemcustom_SetStatement,
    odemcustom_ContinueStatement,
    odemcustom_ActivateObject,
    odemcustom_Print,
    odemcustom_WaitUntil,
    odemcustom_Return,
    odemcustom_SetGenContextStatement,
    odemcustom_Assignment,
    odemcustom_BreakStatement,
    odemcustom_Wait,
    odemcustom_ExpressionStatement,
    odemcustom_SimpleStatement,
    odemcustom_CompositeStatement,
    Construct,
    odemcustom_Statement,
    odemcustom_Expression,
    odemcustom_CodeBlock,
    ExpandableElement,
    odemcustom_TypeAccess,
    odemcustom_VariableAccess,
    odemcustom_NamedElement,
    BindingExprOpKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_odemcustom_quotedcode_is_not_abstract():
    assert not inspect.isabstract(odemcustom_QuotedCode)


def test_odemcustom_quotedcode_constructor_exists():
    assert callable(odemcustom_QuotedCode.__init__)


def test_odemcustom_quotedcode_constructor_args():
    sig = inspect.signature(odemcustom_QuotedCode.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_expandableelement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ExpandableElement)


def test_odemcustom_expandableelement_constructor_exists():
    assert callable(odemcustom_ExpandableElement.__init__)


def test_odemcustom_expandableelement_constructor_args():
    sig = inspect.signature(odemcustom_ExpandableElement.__init__)
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



def test_odemcustom_quotedmodulecontent_is_not_abstract():
    assert not inspect.isabstract(odemcustom_QuotedModuleContent)


def test_odemcustom_quotedmodulecontent_constructor_exists():
    assert callable(odemcustom_QuotedModuleContent.__init__)


def test_odemcustom_quotedmodulecontent_constructor_args():
    sig = inspect.signature(odemcustom_QuotedModuleContent.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_quotedstatements_is_not_abstract():
    assert not inspect.isabstract(odemcustom_QuotedStatements)


def test_odemcustom_quotedstatements_constructor_exists():
    assert callable(odemcustom_QuotedStatements.__init__)


def test_odemcustom_quotedstatements_constructor_args():
    sig = inspect.signature(odemcustom_QuotedStatements.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_quotedexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom_QuotedExpression)


def test_odemcustom_quotedexpression_constructor_exists():
    assert callable(odemcustom_QuotedExpression.__init__)


def test_odemcustom_quotedexpression_constructor_args():
    sig = inspect.signature(odemcustom_QuotedExpression.__init__)
    params = list(sig.parameters.keys())



def test_mappingpart_is_not_abstract():
    assert not inspect.isabstract(MappingPart)


def test_mappingpart_constructor_exists():
    assert callable(MappingPart.__init__)


def test_mappingpart_constructor_args():
    sig = inspect.signature(MappingPart.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_dynamicmappingpart_is_not_abstract():
    assert not inspect.isabstract(odemcustom_DynamicMappingPart)


def test_odemcustom_dynamicmappingpart_constructor_exists():
    assert callable(odemcustom_DynamicMappingPart.__init__)


def test_odemcustom_dynamicmappingpart_constructor_args():
    sig = inspect.signature(odemcustom_DynamicMappingPart.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_fixedmappingpart_is_not_abstract():
    assert not inspect.isabstract(odemcustom_FixedMappingPart)


def test_odemcustom_fixedmappingpart_constructor_exists():
    assert callable(odemcustom_FixedMappingPart.__init__)


def test_odemcustom_fixedmappingpart_constructor_args():
    sig = inspect.signature(odemcustom_FixedMappingPart.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_odemcustom_fixedmappingpart_has_code():
    assert hasattr(odemcustom_FixedMappingPart, "code")
    descriptor = None
    for klass in odemcustom_FixedMappingPart.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_propertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_PropertyType)


def test_odemcustom_propertytype_constructor_exists():
    assert callable(odemcustom_PropertyType.__init__)


def test_odemcustom_propertytype_constructor_args():
    sig = inspect.signature(odemcustom_PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_mappingpart_is_not_abstract():
    assert not inspect.isabstract(odemcustom_MappingPart)


def test_odemcustom_mappingpart_constructor_exists():
    assert callable(odemcustom_MappingPart.__init__)


def test_odemcustom_mappingpart_constructor_args():
    sig = inspect.signature(odemcustom_MappingPart.__init__)
    params = list(sig.parameters.keys())



def test_structuredpropertytype_is_not_abstract():
    assert not inspect.isabstract(StructuredPropertyType)


def test_structuredpropertytype_constructor_exists():
    assert callable(StructuredPropertyType.__init__)


def test_structuredpropertytype_constructor_args():
    sig = inspect.signature(StructuredPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_referencepropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ReferencePropertyType)


def test_odemcustom_referencepropertytype_constructor_exists():
    assert callable(odemcustom_ReferencePropertyType.__init__)


def test_odemcustom_referencepropertytype_constructor_args():
    sig = inspect.signature(odemcustom_ReferencePropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "rawReference" in params, "Missing parameter 'rawReference'"

def test_odemcustom_referencepropertytype_has_rawReference():
    assert hasattr(odemcustom_ReferencePropertyType, "rawReference")
    descriptor = None
    for klass in odemcustom_ReferencePropertyType.__mro__:
        if "rawReference" in klass.__dict__:
            descriptor = klass.__dict__["rawReference"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_compositepropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_CompositePropertyType)


def test_odemcustom_compositepropertytype_constructor_exists():
    assert callable(odemcustom_CompositePropertyType.__init__)


def test_odemcustom_compositepropertytype_constructor_args():
    sig = inspect.signature(odemcustom_CompositePropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"

def test_odemcustom_compositepropertytype_has_list():
    assert hasattr(odemcustom_CompositePropertyType, "list")
    descriptor = None
    for klass in odemcustom_CompositePropertyType.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_modifierextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(ModifierExtensionsContainer)


def test_modifierextensionscontainer_constructor_exists():
    assert callable(ModifierExtensionsContainer.__init__)


def test_modifierextensionscontainer_constructor_args():
    sig = inspect.signature(ModifierExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_constructor_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Constructor)


def test_odemcustom_constructor_constructor_exists():
    assert callable(odemcustom_Constructor.__init__)


def test_odemcustom_constructor_constructor_args():
    sig = inspect.signature(odemcustom_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_classsimilar_is_not_abstract():
    assert not inspect.isabstract(ClassSimilar)


def test_classsimilar_constructor_exists():
    assert callable(ClassSimilar.__init__)


def test_classsimilar_constructor_args():
    sig = inspect.signature(ClassSimilar.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_quotedclasscontent_is_not_abstract():
    assert not inspect.isabstract(odemcustom_QuotedClassContent)


def test_odemcustom_quotedclasscontent_constructor_exists():
    assert callable(odemcustom_QuotedClassContent.__init__)


def test_odemcustom_quotedclasscontent_constructor_args():
    sig = inspect.signature(odemcustom_QuotedClassContent.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_interface_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Interface)


def test_odemcustom_interface_constructor_exists():
    assert callable(odemcustom_Interface.__init__)


def test_odemcustom_interface_constructor_args():
    sig = inspect.signature(odemcustom_Interface.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_clazz_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Clazz)


def test_odemcustom_clazz_constructor_exists():
    assert callable(odemcustom_Clazz.__init__)


def test_odemcustom_clazz_constructor_args():
    sig = inspect.signature(odemcustom_Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_odemcustom_clazz_has_active():
    assert hasattr(odemcustom_Clazz, "active")
    descriptor = None
    for klass in odemcustom_Clazz.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_booltype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_BoolType)


def test_odemcustom_booltype_constructor_exists():
    assert callable(odemcustom_BoolType.__init__)


def test_odemcustom_booltype_constructor_args():
    sig = inspect.signature(odemcustom_BoolType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_inttype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_IntType)


def test_odemcustom_inttype_constructor_exists():
    assert callable(odemcustom_IntType.__init__)


def test_odemcustom_inttype_constructor_args():
    sig = inspect.signature(odemcustom_IntType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_doubletype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_DoubleType)


def test_odemcustom_doubletype_constructor_exists():
    assert callable(odemcustom_DoubleType.__init__)


def test_odemcustom_doubletype_constructor_args():
    sig = inspect.signature(odemcustom_DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_voidtype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_VoidType)


def test_odemcustom_voidtype_constructor_exists():
    assert callable(odemcustom_VoidType.__init__)


def test_odemcustom_voidtype_constructor_args():
    sig = inspect.signature(odemcustom_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_nativebinding_is_not_abstract():
    assert not inspect.isabstract(odemcustom_NativeBinding)


def test_odemcustom_nativebinding_constructor_exists():
    assert callable(odemcustom_NativeBinding.__init__)


def test_odemcustom_nativebinding_constructor_args():
    sig = inspect.signature(odemcustom_NativeBinding.__init__)
    params = list(sig.parameters.keys())
    assert "targetType" in params, "Missing parameter 'targetType'"
    assert "targetLanguage" in params, "Missing parameter 'targetLanguage'"

def test_odemcustom_nativebinding_has_targetType():
    assert hasattr(odemcustom_NativeBinding, "targetType")
    descriptor = None
    for klass in odemcustom_NativeBinding.__mro__:
        if "targetType" in klass.__dict__:
            descriptor = klass.__dict__["targetType"]
            break
    assert isinstance(descriptor, property)

def test_odemcustom_nativebinding_has_targetLanguage():
    assert hasattr(odemcustom_NativeBinding, "targetLanguage")
    descriptor = None
    for klass in odemcustom_NativeBinding.__mro__:
        if "targetLanguage" in klass.__dict__:
            descriptor = klass.__dict__["targetLanguage"]
            break
    assert isinstance(descriptor, property)



def test_referablerhstype_is_not_abstract():
    assert not inspect.isabstract(ReferableRhsType)


def test_referablerhstype_constructor_exists():
    assert callable(ReferableRhsType.__init__)


def test_referablerhstype_constructor_args():
    sig = inspect.signature(ReferableRhsType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_annotatableelement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_AnnotatableElement)


def test_odemcustom_annotatableelement_constructor_exists():
    assert callable(odemcustom_AnnotatableElement.__init__)


def test_odemcustom_annotatableelement_constructor_args():
    sig = inspect.signature(odemcustom_AnnotatableElement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_keyvaluepair_is_not_abstract():
    assert not inspect.isabstract(odemcustom_KeyValuePair)


def test_odemcustom_keyvaluepair_constructor_exists():
    assert callable(odemcustom_KeyValuePair.__init__)


def test_odemcustom_keyvaluepair_constructor_args():
    sig = inspect.signature(odemcustom_KeyValuePair.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_annotationapplication_is_not_abstract():
    assert not inspect.isabstract(odemcustom_AnnotationApplication)


def test_odemcustom_annotationapplication_constructor_exists():
    assert callable(odemcustom_AnnotationApplication.__init__)


def test_odemcustom_annotationapplication_constructor_args():
    sig = inspect.signature(odemcustom_AnnotationApplication.__init__)
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



def test_odemcustom_startcodeblock_is_not_abstract():
    assert not inspect.isabstract(odemcustom_StartCodeBlock)


def test_odemcustom_startcodeblock_constructor_exists():
    assert callable(odemcustom_StartCodeBlock.__init__)


def test_odemcustom_startcodeblock_constructor_args():
    sig = inspect.signature(odemcustom_StartCodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_stringtype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_StringType)


def test_odemcustom_stringtype_constructor_exists():
    assert callable(odemcustom_StringType.__init__)


def test_odemcustom_stringtype_constructor_args():
    sig = inspect.signature(odemcustom_StringType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_import_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Import)


def test_odemcustom_import_constructor_exists():
    assert callable(odemcustom_Import.__init__)


def test_odemcustom_import_constructor_args():
    sig = inspect.signature(odemcustom_Import.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_odemcustom_import_has_file():
    assert hasattr(odemcustom_Import, "file")
    descriptor = None
    for klass in odemcustom_Import.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_model_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Model)


def test_odemcustom_model_constructor_exists():
    assert callable(odemcustom_Model.__init__)


def test_odemcustom_model_constructor_args():
    sig = inspect.signature(odemcustom_Model.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_primitivetype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_PrimitiveType)


def test_odemcustom_primitivetype_constructor_exists():
    assert callable(odemcustom_PrimitiveType.__init__)


def test_odemcustom_primitivetype_constructor_args():
    sig = inspect.signature(odemcustom_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_typedelement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_TypedElement)


def test_odemcustom_typedelement_constructor_exists():
    assert callable(odemcustom_TypedElement.__init__)


def test_odemcustom_typedelement_constructor_args():
    sig = inspect.signature(odemcustom_TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "isList" in params, "Missing parameter 'isList'"

def test_odemcustom_typedelement_has_isList():
    assert hasattr(odemcustom_TypedElement, "isList")
    descriptor = None
    for klass in odemcustom_TypedElement.__mro__:
        if "isList" in klass.__dict__:
            descriptor = klass.__dict__["isList"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_type_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Type)


def test_odemcustom_type_constructor_exists():
    assert callable(odemcustom_Type.__init__)


def test_odemcustom_type_constructor_args():
    sig = inspect.signature(odemcustom_Type.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_modifierextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ModifierExtensionsContainer)


def test_odemcustom_modifierextensionscontainer_constructor_exists():
    assert callable(odemcustom_ModifierExtensionsContainer.__init__)


def test_odemcustom_modifierextensionscontainer_constructor_args():
    sig = inspect.signature(odemcustom_ModifierExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_extension_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Extension)


def test_odemcustom_extension_constructor_exists():
    assert callable(odemcustom_Extension.__init__)


def test_odemcustom_extension_constructor_args():
    sig = inspect.signature(odemcustom_Extension.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_embeddableextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(odemcustom_EmbeddableExtensionsContainer)


def test_odemcustom_embeddableextensionscontainer_constructor_exists():
    assert callable(odemcustom_EmbeddableExtensionsContainer.__init__)


def test_odemcustom_embeddableextensionscontainer_constructor_args():
    sig = inspect.signature(odemcustom_EmbeddableExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_idresolution_is_not_abstract():
    assert not inspect.isabstract(odemcustom_IdResolution)


def test_odemcustom_idresolution_constructor_exists():
    assert callable(odemcustom_IdResolution.__init__)


def test_odemcustom_idresolution_constructor_args():
    sig = inspect.signature(odemcustom_IdResolution.__init__)
    params = list(sig.parameters.keys())
    assert "metaModelPlatformURI" in params, "Missing parameter 'metaModelPlatformURI'"

def test_odemcustom_idresolution_has_metaModelPlatformURI():
    assert hasattr(odemcustom_IdResolution, "metaModelPlatformURI")
    descriptor = None
    for klass in odemcustom_IdResolution.__mro__:
        if "metaModelPlatformURI" in klass.__dict__:
            descriptor = klass.__dict__["metaModelPlatformURI"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_classaugment_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ClassAugment)


def test_odemcustom_classaugment_constructor_exists():
    assert callable(odemcustom_ClassAugment.__init__)


def test_odemcustom_classaugment_constructor_args():
    sig = inspect.signature(odemcustom_ClassAugment.__init__)
    params = list(sig.parameters.keys())



def test_embeddableextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(EmbeddableExtensionsContainer)


def test_embeddableextensionscontainer_constructor_exists():
    assert callable(EmbeddableExtensionsContainer.__init__)


def test_embeddableextensionscontainer_constructor_args():
    sig = inspect.signature(EmbeddableExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_classsimilar_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ClassSimilar)


def test_odemcustom_classsimilar_constructor_exists():
    assert callable(odemcustom_ClassSimilar.__init__)


def test_odemcustom_classsimilar_constructor_args():
    sig = inspect.signature(odemcustom_ClassSimilar.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_simpleannotation_is_not_abstract():
    assert not inspect.isabstract(odemcustom_SimpleAnnotation)


def test_odemcustom_simpleannotation_constructor_exists():
    assert callable(odemcustom_SimpleAnnotation.__init__)


def test_odemcustom_simpleannotation_constructor_args():
    sig = inspect.signature(odemcustom_SimpleAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_odemcustom_simpleannotation_has_value():
    assert hasattr(odemcustom_SimpleAnnotation, "value")
    descriptor = None
    for klass in odemcustom_SimpleAnnotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_procedure_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Procedure)


def test_odemcustom_procedure_constructor_exists():
    assert callable(odemcustom_Procedure.__init__)


def test_odemcustom_procedure_constructor_args():
    sig = inspect.signature(odemcustom_Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "clazz" in params, "Missing parameter 'clazz'"

def test_odemcustom_procedure_has_clazz():
    assert hasattr(odemcustom_Procedure, "clazz")
    descriptor = None
    for klass in odemcustom_Procedure.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_pattern_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Pattern)


def test_odemcustom_pattern_constructor_exists():
    assert callable(odemcustom_Pattern.__init__)


def test_odemcustom_pattern_constructor_args():
    sig = inspect.signature(odemcustom_Pattern.__init__)
    params = list(sig.parameters.keys())
    assert "top" in params, "Missing parameter 'top'"

def test_odemcustom_pattern_has_top():
    assert hasattr(odemcustom_Pattern, "top")
    descriptor = None
    for klass in odemcustom_Pattern.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_extensiondefinition_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ExtensionDefinition)


def test_odemcustom_extensiondefinition_constructor_exists():
    assert callable(odemcustom_ExtensionDefinition.__init__)


def test_odemcustom_extensiondefinition_constructor_args():
    sig = inspect.signature(odemcustom_ExtensionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_annotation_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Annotation)


def test_odemcustom_annotation_constructor_exists():
    assert callable(odemcustom_Annotation.__init__)


def test_odemcustom_annotation_constructor_args():
    sig = inspect.signature(odemcustom_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_module_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Module)


def test_odemcustom_module_constructor_exists():
    assert callable(odemcustom_Module.__init__)


def test_odemcustom_module_constructor_args():
    sig = inspect.signature(odemcustom_Module.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_classifier_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Classifier)


def test_odemcustom_classifier_constructor_exists():
    assert callable(odemcustom_Classifier.__init__)


def test_odemcustom_classifier_constructor_args():
    sig = inspect.signature(odemcustom_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_namedextension_is_not_abstract():
    assert not inspect.isabstract(NamedExtension)


def test_namedextension_constructor_exists():
    assert callable(NamedExtension.__init__)


def test_namedextension_constructor_args():
    sig = inspect.signature(NamedExtension.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_construct_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Construct)


def test_odemcustom_construct_constructor_exists():
    assert callable(odemcustom_Construct.__init__)


def test_odemcustom_construct_constructor_args():
    sig = inspect.signature(odemcustom_Construct.__init__)
    params = list(sig.parameters.keys())
    assert "concreteSyntax" in params, "Missing parameter 'concreteSyntax'"

def test_odemcustom_construct_has_concreteSyntax():
    assert hasattr(odemcustom_Construct, "concreteSyntax")
    descriptor = None
    for klass in odemcustom_Construct.__mro__:
        if "concreteSyntax" in klass.__dict__:
            descriptor = klass.__dict__["concreteSyntax"]
            break
    assert isinstance(descriptor, property)



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_stringpropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_StringPropertyType)


def test_odemcustom_stringpropertytype_constructor_exists():
    assert callable(odemcustom_StringPropertyType.__init__)


def test_odemcustom_stringpropertytype_constructor_args():
    sig = inspect.signature(odemcustom_StringPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_booleanpropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_BooleanPropertyType)


def test_odemcustom_booleanpropertytype_constructor_exists():
    assert callable(odemcustom_BooleanPropertyType.__init__)


def test_odemcustom_booleanpropertytype_constructor_args():
    sig = inspect.signature(odemcustom_BooleanPropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "terminal" in params, "Missing parameter 'terminal'"

def test_odemcustom_booleanpropertytype_has_terminal():
    assert hasattr(odemcustom_BooleanPropertyType, "terminal")
    descriptor = None
    for klass in odemcustom_BooleanPropertyType.__mro__:
        if "terminal" in klass.__dict__:
            descriptor = klass.__dict__["terminal"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_structuredpropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_StructuredPropertyType)


def test_odemcustom_structuredpropertytype_constructor_exists():
    assert callable(odemcustom_StructuredPropertyType.__init__)


def test_odemcustom_structuredpropertytype_constructor_args():
    sig = inspect.signature(odemcustom_StructuredPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_intpropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_IntPropertyType)


def test_odemcustom_intpropertytype_constructor_exists():
    assert callable(odemcustom_IntPropertyType.__init__)


def test_odemcustom_intpropertytype_constructor_args():
    sig = inspect.signature(odemcustom_IntPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_idpropertytype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_IdPropertyType)


def test_odemcustom_idpropertytype_constructor_exists():
    assert callable(odemcustom_IdPropertyType.__init__)


def test_odemcustom_idpropertytype_constructor_args():
    sig = inspect.signature(odemcustom_IdPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_rhsexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom_RhsExpression)


def test_odemcustom_rhsexpression_constructor_exists():
    assert callable(odemcustom_RhsExpression.__init__)


def test_odemcustom_rhsexpression_constructor_args():
    sig = inspect.signature(odemcustom_RhsExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_referablerhstype_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ReferableRhsType)


def test_odemcustom_referablerhstype_constructor_exists():
    assert callable(odemcustom_ReferableRhsType.__init__)


def test_odemcustom_referablerhstype_constructor_args():
    sig = inspect.signature(odemcustom_ReferableRhsType.__init__)
    params = list(sig.parameters.keys())



def test_rhsexpression_is_not_abstract():
    assert not inspect.isabstract(RhsExpression)


def test_rhsexpression_constructor_exists():
    assert callable(RhsExpression.__init__)


def test_rhsexpression_constructor_args():
    sig = inspect.signature(RhsExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_alternativeexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_AlternativeExpr)


def test_odemcustom_alternativeexpr_constructor_exists():
    assert callable(odemcustom_AlternativeExpr.__init__)


def test_odemcustom_alternativeexpr_constructor_args():
    sig = inspect.signature(odemcustom_AlternativeExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_runtimeexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_RuntimeExpr)


def test_odemcustom_runtimeexpr_constructor_exists():
    assert callable(odemcustom_RuntimeExpr.__init__)


def test_odemcustom_runtimeexpr_constructor_args():
    sig = inspect.signature(odemcustom_RuntimeExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_arbitraryexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ArbitraryExpr)


def test_odemcustom_arbitraryexpr_constructor_exists():
    assert callable(odemcustom_ArbitraryExpr.__init__)


def test_odemcustom_arbitraryexpr_constructor_args():
    sig = inspect.signature(odemcustom_ArbitraryExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_optionalexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_OptionalExpr)


def test_odemcustom_optionalexpr_constructor_exists():
    assert callable(odemcustom_OptionalExpr.__init__)


def test_odemcustom_optionalexpr_constructor_args():
    sig = inspect.signature(odemcustom_OptionalExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_terminalexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_TerminalExpr)


def test_odemcustom_terminalexpr_constructor_exists():
    assert callable(odemcustom_TerminalExpr.__init__)


def test_odemcustom_terminalexpr_constructor_args():
    sig = inspect.signature(odemcustom_TerminalExpr.__init__)
    params = list(sig.parameters.keys())
    assert "terminal" in params, "Missing parameter 'terminal'"

def test_odemcustom_terminalexpr_has_terminal():
    assert hasattr(odemcustom_TerminalExpr, "terminal")
    descriptor = None
    for klass in odemcustom_TerminalExpr.__mro__:
        if "terminal" in klass.__dict__:
            descriptor = klass.__dict__["terminal"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_atleastoneexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_AtLeastOneExpr)


def test_odemcustom_atleastoneexpr_constructor_exists():
    assert callable(odemcustom_AtLeastOneExpr.__init__)


def test_odemcustom_atleastoneexpr_constructor_args():
    sig = inspect.signature(odemcustom_AtLeastOneExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_propertybindingexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_PropertyBindingExpr)


def test_odemcustom_propertybindingexpr_constructor_exists():
    assert callable(odemcustom_PropertyBindingExpr.__init__)


def test_odemcustom_propertybindingexpr_constructor_args():
    sig = inspect.signature(odemcustom_PropertyBindingExpr.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_odemcustom_propertybindingexpr_has_operator():
    assert hasattr(odemcustom_PropertyBindingExpr, "operator")
    descriptor = None
    for klass in odemcustom_PropertyBindingExpr.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_sequenceexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_SequenceExpr)


def test_odemcustom_sequenceexpr_constructor_exists():
    assert callable(odemcustom_SequenceExpr.__init__)


def test_odemcustom_sequenceexpr_constructor_args():
    sig = inspect.signature(odemcustom_SequenceExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_ruleexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_RuleExpr)


def test_odemcustom_ruleexpr_constructor_exists():
    assert callable(odemcustom_RuleExpr.__init__)


def test_odemcustom_ruleexpr_constructor_args():
    sig = inspect.signature(odemcustom_RuleExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_tsrule_is_not_abstract():
    assert not inspect.isabstract(odemcustom_TsRule)


def test_odemcustom_tsrule_constructor_exists():
    assert callable(odemcustom_TsRule.__init__)


def test_odemcustom_tsrule_constructor_args():
    sig = inspect.signature(odemcustom_TsRule.__init__)
    params = list(sig.parameters.keys())
    assert "metaClassName" in params, "Missing parameter 'metaClassName'"

def test_odemcustom_tsrule_has_metaClassName():
    assert hasattr(odemcustom_TsRule, "metaClassName")
    descriptor = None
    for klass in odemcustom_TsRule.__mro__:
        if "metaClassName" in klass.__dict__:
            descriptor = klass.__dict__["metaClassName"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_extensionrule_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ExtensionRule)


def test_odemcustom_extensionrule_constructor_exists():
    assert callable(odemcustom_ExtensionRule.__init__)


def test_odemcustom_extensionrule_constructor_args():
    sig = inspect.signature(odemcustom_ExtensionRule.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_mapping_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Mapping)


def test_odemcustom_mapping_constructor_exists():
    assert callable(odemcustom_Mapping.__init__)


def test_odemcustom_mapping_constructor_args():
    sig = inspect.signature(odemcustom_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_textualsyntaxdef_is_not_abstract():
    assert not inspect.isabstract(odemcustom_TextualSyntaxDef)


def test_odemcustom_textualsyntaxdef_constructor_exists():
    assert callable(odemcustom_TextualSyntaxDef.__init__)


def test_odemcustom_textualsyntaxdef_constructor_args():
    sig = inspect.signature(odemcustom_TextualSyntaxDef.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_modulecontentextension_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ModuleContentExtension)


def test_odemcustom_modulecontentextension_constructor_exists():
    assert callable(odemcustom_ModuleContentExtension.__init__)


def test_odemcustom_modulecontentextension_constructor_args():
    sig = inspect.signature(odemcustom_ModuleContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_classcontentextension_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ClassContentExtension)


def test_odemcustom_classcontentextension_constructor_exists():
    assert callable(odemcustom_ClassContentExtension.__init__)


def test_odemcustom_classcontentextension_constructor_args():
    sig = inspect.signature(odemcustom_ClassContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_extension_is_not_abstract():
    assert not inspect.isabstract(Extension)


def test_extension_constructor_exists():
    assert callable(Extension.__init__)


def test_extension_constructor_args():
    sig = inspect.signature(Extension.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_namedextension_is_not_abstract():
    assert not inspect.isabstract(odemcustom_NamedExtension)


def test_odemcustom_namedextension_constructor_exists():
    assert callable(odemcustom_NamedExtension.__init__)


def test_odemcustom_namedextension_constructor_args():
    sig = inspect.signature(odemcustom_NamedExtension.__init__)
    params = list(sig.parameters.keys())



def test_variableaccess_is_not_abstract():
    assert not inspect.isabstract(VariableAccess)


def test_variableaccess_constructor_exists():
    assert callable(VariableAccess.__init__)


def test_variableaccess_constructor_args():
    sig = inspect.signature(VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_metaaccess_is_not_abstract():
    assert not inspect.isabstract(odemcustom_MetaAccess)


def test_odemcustom_metaaccess_constructor_exists():
    assert callable(odemcustom_MetaAccess.__init__)


def test_odemcustom_metaaccess_constructor_args():
    sig = inspect.signature(odemcustom_MetaAccess.__init__)
    params = list(sig.parameters.keys())



def test_elementaccess_is_not_abstract():
    assert not inspect.isabstract(ElementAccess)


def test_elementaccess_constructor_exists():
    assert callable(ElementAccess.__init__)


def test_elementaccess_constructor_args():
    sig = inspect.signature(ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_argumentexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ArgumentExpression)


def test_odemcustom_argumentexpression_constructor_exists():
    assert callable(odemcustom_ArgumentExpression.__init__)


def test_odemcustom_argumentexpression_constructor_args():
    sig = inspect.signature(odemcustom_ArgumentExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_predefinedid_is_not_abstract():
    assert not inspect.isabstract(odemcustom_PredefinedId)


def test_odemcustom_predefinedid_constructor_exists():
    assert callable(odemcustom_PredefinedId.__init__)


def test_odemcustom_predefinedid_constructor_args():
    sig = inspect.signature(odemcustom_PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_depidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_DepIdentifiableElement)


def test_odemcustom_depidentifiableelement_constructor_exists():
    assert callable(odemcustom_DepIdentifiableElement.__init__)


def test_odemcustom_depidentifiableelement_constructor_args():
    sig = inspect.signature(odemcustom_DepIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_neg_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Neg)


def test_odemcustom_neg_constructor_exists():
    assert callable(odemcustom_Neg.__init__)


def test_odemcustom_neg_constructor_args():
    sig = inspect.signature(odemcustom_Neg.__init__)
    params = list(sig.parameters.keys())



def test_setop_is_not_abstract():
    assert not inspect.isabstract(SetOp)


def test_setop_constructor_exists():
    assert callable(SetOp.__init__)


def test_setop_constructor_args():
    sig = inspect.signature(SetOp.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_firstinset_is_not_abstract():
    assert not inspect.isabstract(odemcustom_FirstInSet)


def test_odemcustom_firstinset_constructor_exists():
    assert callable(odemcustom_FirstInSet.__init__)


def test_odemcustom_firstinset_constructor_args():
    sig = inspect.signature(odemcustom_FirstInSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_afterinset_is_not_abstract():
    assert not inspect.isabstract(odemcustom_AfterInSet)


def test_odemcustom_afterinset_constructor_exists():
    assert callable(odemcustom_AfterInSet.__init__)


def test_odemcustom_afterinset_constructor_args():
    sig = inspect.signature(odemcustom_AfterInSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_beforeinset_is_not_abstract():
    assert not inspect.isabstract(odemcustom_BeforeInSet)


def test_odemcustom_beforeinset_constructor_exists():
    assert callable(odemcustom_BeforeInSet.__init__)


def test_odemcustom_beforeinset_constructor_args():
    sig = inspect.signature(odemcustom_BeforeInSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_lastinset_is_not_abstract():
    assert not inspect.isabstract(odemcustom_LastInSet)


def test_odemcustom_lastinset_constructor_exists():
    assert callable(odemcustom_LastInSet.__init__)


def test_odemcustom_lastinset_constructor_args():
    sig = inspect.signature(odemcustom_LastInSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_contains_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Contains)


def test_odemcustom_contains_constructor_exists():
    assert callable(odemcustom_Contains.__init__)


def test_odemcustom_contains_constructor_args():
    sig = inspect.signature(odemcustom_Contains.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_objectat_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ObjectAt)


def test_odemcustom_objectat_constructor_exists():
    assert callable(odemcustom_ObjectAt.__init__)


def test_odemcustom_objectat_constructor_args():
    sig = inspect.signature(odemcustom_ObjectAt.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_indexof_is_not_abstract():
    assert not inspect.isabstract(odemcustom_IndexOf)


def test_odemcustom_indexof_constructor_exists():
    assert callable(odemcustom_IndexOf.__init__)


def test_odemcustom_indexof_constructor_args():
    sig = inspect.signature(odemcustom_IndexOf.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_sizeofset_is_not_abstract():
    assert not inspect.isabstract(odemcustom_SizeOfSet)


def test_odemcustom_sizeofset_constructor_exists():
    assert callable(odemcustom_SizeOfSet.__init__)


def test_odemcustom_sizeofset_constructor_args():
    sig = inspect.signature(odemcustom_SizeOfSet.__init__)
    params = list(sig.parameters.keys())



def test_predefinedid_is_not_abstract():
    assert not inspect.isabstract(PredefinedId)


def test_predefinedid_constructor_exists():
    assert callable(PredefinedId.__init__)


def test_predefinedid_constructor_args():
    sig = inspect.signature(PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_metaliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_MetaLiteral)


def test_odemcustom_metaliteral_constructor_exists():
    assert callable(odemcustom_MetaLiteral.__init__)


def test_odemcustom_metaliteral_constructor_args():
    sig = inspect.signature(odemcustom_MetaLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_setop_is_not_abstract():
    assert not inspect.isabstract(odemcustom_SetOp)


def test_odemcustom_setop_constructor_exists():
    assert callable(odemcustom_SetOp.__init__)


def test_odemcustom_setop_constructor_args():
    sig = inspect.signature(odemcustom_SetOp.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_superliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_SuperLiteral)


def test_odemcustom_superliteral_constructor_exists():
    assert callable(odemcustom_SuperLiteral.__init__)


def test_odemcustom_superliteral_constructor_args():
    sig = inspect.signature(odemcustom_SuperLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_typeliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_TypeLiteral)


def test_odemcustom_typeliteral_constructor_exists():
    assert callable(odemcustom_TypeLiteral.__init__)


def test_odemcustom_typeliteral_constructor_args():
    sig = inspect.signature(odemcustom_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_meliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_MeLiteral)


def test_odemcustom_meliteral_constructor_exists():
    assert callable(odemcustom_MeLiteral.__init__)


def test_odemcustom_meliteral_constructor_args():
    sig = inspect.signature(odemcustom_MeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_cast_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Cast)


def test_odemcustom_cast_constructor_exists():
    assert callable(odemcustom_Cast.__init__)


def test_odemcustom_cast_constructor_args():
    sig = inspect.signature(odemcustom_Cast.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_not_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Not)


def test_odemcustom_not_constructor_exists():
    assert callable(odemcustom_Not.__init__)


def test_odemcustom_not_constructor_args():
    sig = inspect.signature(odemcustom_Not.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_less_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Less)


def test_odemcustom_less_constructor_exists():
    assert callable(odemcustom_Less.__init__)


def test_odemcustom_less_constructor_args():
    sig = inspect.signature(odemcustom_Less.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_greaterequal_is_not_abstract():
    assert not inspect.isabstract(odemcustom_GreaterEqual)


def test_odemcustom_greaterequal_constructor_exists():
    assert callable(odemcustom_GreaterEqual.__init__)


def test_odemcustom_greaterequal_constructor_args():
    sig = inspect.signature(odemcustom_GreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_lessequal_is_not_abstract():
    assert not inspect.isabstract(odemcustom_LessEqual)


def test_odemcustom_lessequal_constructor_exists():
    assert callable(odemcustom_LessEqual.__init__)


def test_odemcustom_lessequal_constructor_args():
    sig = inspect.signature(odemcustom_LessEqual.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_mul_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Mul)


def test_odemcustom_mul_constructor_exists():
    assert callable(odemcustom_Mul.__init__)


def test_odemcustom_mul_constructor_args():
    sig = inspect.signature(odemcustom_Mul.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_mod_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Mod)


def test_odemcustom_mod_constructor_exists():
    assert callable(odemcustom_Mod.__init__)


def test_odemcustom_mod_constructor_args():
    sig = inspect.signature(odemcustom_Mod.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_minus_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Minus)


def test_odemcustom_minus_constructor_exists():
    assert callable(odemcustom_Minus.__init__)


def test_odemcustom_minus_constructor_args():
    sig = inspect.signature(odemcustom_Minus.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_greater_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Greater)


def test_odemcustom_greater_constructor_exists():
    assert callable(odemcustom_Greater.__init__)


def test_odemcustom_greater_constructor_args():
    sig = inspect.signature(odemcustom_Greater.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_and_is_not_abstract():
    assert not inspect.isabstract(odemcustom_And)


def test_odemcustom_and_constructor_exists():
    assert callable(odemcustom_And.__init__)


def test_odemcustom_and_constructor_args():
    sig = inspect.signature(odemcustom_And.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_instanceof_is_not_abstract():
    assert not inspect.isabstract(odemcustom_InstanceOf)


def test_odemcustom_instanceof_constructor_exists():
    assert callable(odemcustom_InstanceOf.__init__)


def test_odemcustom_instanceof_constructor_args():
    sig = inspect.signature(odemcustom_InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_notequal_is_not_abstract():
    assert not inspect.isabstract(odemcustom_NotEqual)


def test_odemcustom_notequal_constructor_exists():
    assert callable(odemcustom_NotEqual.__init__)


def test_odemcustom_notequal_constructor_args():
    sig = inspect.signature(odemcustom_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_or_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Or)


def test_odemcustom_or_constructor_exists():
    assert callable(odemcustom_Or.__init__)


def test_odemcustom_or_constructor_args():
    sig = inspect.signature(odemcustom_Or.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_equal_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Equal)


def test_odemcustom_equal_constructor_exists():
    assert callable(odemcustom_Equal.__init__)


def test_odemcustom_equal_constructor_args():
    sig = inspect.signature(odemcustom_Equal.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_div_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Div)


def test_odemcustom_div_constructor_exists():
    assert callable(odemcustom_Div.__init__)


def test_odemcustom_div_constructor_args():
    sig = inspect.signature(odemcustom_Div.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_plus_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Plus)


def test_odemcustom_plus_constructor_exists():
    assert callable(odemcustom_Plus.__init__)


def test_odemcustom_plus_constructor_args():
    sig = inspect.signature(odemcustom_Plus.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(odemcustom_BinaryOperator)


def test_odemcustom_binaryoperator_constructor_exists():
    assert callable(odemcustom_BinaryOperator.__init__)


def test_odemcustom_binaryoperator_constructor_args():
    sig = inspect.signature(odemcustom_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(odemcustom_UnaryOperator)


def test_odemcustom_unaryoperator_constructor_exists():
    assert callable(odemcustom_UnaryOperator.__init__)


def test_odemcustom_unaryoperator_constructor_args():
    sig = inspect.signature(odemcustom_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_idexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_IdExpr)


def test_odemcustom_idexpr_constructor_exists():
    assert callable(odemcustom_IdExpr.__init__)


def test_odemcustom_idexpr_constructor_args():
    sig = inspect.signature(odemcustom_IdExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_DoubleLiteral)


def test_odemcustom_doubleliteral_constructor_exists():
    assert callable(odemcustom_DoubleLiteral.__init__)


def test_odemcustom_doubleliteral_constructor_args():
    sig = inspect.signature(odemcustom_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_odemcustom_doubleliteral_has_value():
    assert hasattr(odemcustom_DoubleLiteral, "value")
    descriptor = None
    for klass in odemcustom_DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_falseliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_FalseLiteral)


def test_odemcustom_falseliteral_constructor_exists():
    assert callable(odemcustom_FalseLiteral.__init__)


def test_odemcustom_falseliteral_constructor_args():
    sig = inspect.signature(odemcustom_FalseLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_codequoteexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom_CodeQuoteExpression)


def test_odemcustom_codequoteexpression_constructor_exists():
    assert callable(odemcustom_CodeQuoteExpression.__init__)


def test_odemcustom_codequoteexpression_constructor_args():
    sig = inspect.signature(odemcustom_CodeQuoteExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_createobject_is_not_abstract():
    assert not inspect.isabstract(odemcustom_CreateObject)


def test_odemcustom_createobject_constructor_exists():
    assert callable(odemcustom_CreateObject.__init__)


def test_odemcustom_createobject_constructor_args():
    sig = inspect.signature(odemcustom_CreateObject.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_intliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_IntLiteral)


def test_odemcustom_intliteral_constructor_exists():
    assert callable(odemcustom_IntLiteral.__init__)


def test_odemcustom_intliteral_constructor_args():
    sig = inspect.signature(odemcustom_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_odemcustom_intliteral_has_value():
    assert hasattr(odemcustom_IntLiteral, "value")
    descriptor = None
    for klass in odemcustom_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_evalexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_EvalExpr)


def test_odemcustom_evalexpr_constructor_exists():
    assert callable(odemcustom_EvalExpr.__init__)


def test_odemcustom_evalexpr_constructor_args():
    sig = inspect.signature(odemcustom_EvalExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_activeliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ActiveLiteral)


def test_odemcustom_activeliteral_constructor_exists():
    assert callable(odemcustom_ActiveLiteral.__init__)


def test_odemcustom_activeliteral_constructor_args():
    sig = inspect.signature(odemcustom_ActiveLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_stringliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_StringLiteral)


def test_odemcustom_stringliteral_constructor_exists():
    assert callable(odemcustom_StringLiteral.__init__)


def test_odemcustom_stringliteral_constructor_args():
    sig = inspect.signature(odemcustom_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_odemcustom_stringliteral_has_value():
    assert hasattr(odemcustom_StringLiteral, "value")
    descriptor = None
    for klass in odemcustom_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_trueliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_TrueLiteral)


def test_odemcustom_trueliteral_constructor_exists():
    assert callable(odemcustom_TrueLiteral.__init__)


def test_odemcustom_trueliteral_constructor_args():
    sig = inspect.signature(odemcustom_TrueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_metaexpr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_MetaExpr)


def test_odemcustom_metaexpr_constructor_exists():
    assert callable(odemcustom_MetaExpr.__init__)


def test_odemcustom_metaexpr_constructor_args():
    sig = inspect.signature(odemcustom_MetaExpr.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_timeliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_TimeLiteral)


def test_odemcustom_timeliteral_constructor_exists():
    assert callable(odemcustom_TimeLiteral.__init__)


def test_odemcustom_timeliteral_constructor_args():
    sig = inspect.signature(odemcustom_TimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_nullliteral_is_not_abstract():
    assert not inspect.isabstract(odemcustom_NullLiteral)


def test_odemcustom_nullliteral_constructor_exists():
    assert callable(odemcustom_NullLiteral.__init__)


def test_odemcustom_nullliteral_constructor_args():
    sig = inspect.signature(odemcustom_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_elementaccess_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ElementAccess)


def test_odemcustom_elementaccess_constructor_exists():
    assert callable(odemcustom_ElementAccess.__init__)


def test_odemcustom_elementaccess_constructor_args():
    sig = inspect.signature(odemcustom_ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_l1expr_is_not_abstract():
    assert not inspect.isabstract(odemcustom_L1Expr)


def test_odemcustom_l1expr_constructor_exists():
    assert callable(odemcustom_L1Expr.__init__)


def test_odemcustom_l1expr_constructor_args():
    sig = inspect.signature(odemcustom_L1Expr.__init__)
    params = list(sig.parameters.keys())



def test_compositestatement_is_not_abstract():
    assert not inspect.isabstract(CompositeStatement)


def test_compositestatement_constructor_exists():
    assert callable(CompositeStatement.__init__)


def test_compositestatement_constructor_args():
    sig = inspect.signature(CompositeStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_expandsection_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ExpandSection)


def test_odemcustom_expandsection_constructor_exists():
    assert callable(odemcustom_ExpandSection.__init__)


def test_odemcustom_expandsection_constructor_args():
    sig = inspect.signature(odemcustom_ExpandSection.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_whilestatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_WhileStatement)


def test_odemcustom_whilestatement_constructor_exists():
    assert callable(odemcustom_WhileStatement.__init__)


def test_odemcustom_whilestatement_constructor_args():
    sig = inspect.signature(odemcustom_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_foreachstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ForEachStatement)


def test_odemcustom_foreachstatement_constructor_exists():
    assert callable(odemcustom_ForEachStatement.__init__)


def test_odemcustom_foreachstatement_constructor_args():
    sig = inspect.signature(odemcustom_ForEachStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_ifstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_IfStatement)


def test_odemcustom_ifstatement_constructor_exists():
    assert callable(odemcustom_IfStatement.__init__)


def test_odemcustom_ifstatement_constructor_args():
    sig = inspect.signature(odemcustom_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_setstatement_is_not_abstract():
    assert not inspect.isabstract(SetStatement)


def test_setstatement_constructor_exists():
    assert callable(SetStatement.__init__)


def test_setstatement_constructor_args():
    sig = inspect.signature(SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_emptyset_is_not_abstract():
    assert not inspect.isabstract(odemcustom_EmptySet)


def test_odemcustom_emptyset_constructor_exists():
    assert callable(odemcustom_EmptySet.__init__)


def test_odemcustom_emptyset_constructor_args():
    sig = inspect.signature(odemcustom_EmptySet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_addtoset_is_not_abstract():
    assert not inspect.isabstract(odemcustom_AddToSet)


def test_odemcustom_addtoset_constructor_exists():
    assert callable(odemcustom_AddToSet.__init__)


def test_odemcustom_addtoset_constructor_args():
    sig = inspect.signature(odemcustom_AddToSet.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_removefromset_is_not_abstract():
    assert not inspect.isabstract(odemcustom_RemoveFromSet)


def test_odemcustom_removefromset_constructor_exists():
    assert callable(odemcustom_RemoveFromSet.__init__)


def test_odemcustom_removefromset_constructor_args():
    sig = inspect.signature(odemcustom_RemoveFromSet.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_mappingstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_MappingStatement)


def test_odemcustom_mappingstatement_constructor_exists():
    assert callable(odemcustom_MappingStatement.__init__)


def test_odemcustom_mappingstatement_constructor_args():
    sig = inspect.signature(odemcustom_MappingStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_findcontainer_is_not_abstract():
    assert not inspect.isabstract(odemcustom_FindContainer)


def test_odemcustom_findcontainer_constructor_exists():
    assert callable(odemcustom_FindContainer.__init__)


def test_odemcustom_findcontainer_constructor_args():
    sig = inspect.signature(odemcustom_FindContainer.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_targetstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_TargetStatement)


def test_odemcustom_targetstatement_constructor_exists():
    assert callable(odemcustom_TargetStatement.__init__)


def test_odemcustom_targetstatement_constructor_args():
    sig = inspect.signature(odemcustom_TargetStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_includepattern_is_not_abstract():
    assert not inspect.isabstract(odemcustom_IncludePattern)


def test_odemcustom_includepattern_constructor_exists():
    assert callable(odemcustom_IncludePattern.__init__)


def test_odemcustom_includepattern_constructor_args():
    sig = inspect.signature(odemcustom_IncludePattern.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_consideridelements_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ConsiderIdElements)


def test_odemcustom_consideridelements_constructor_exists():
    assert callable(odemcustom_ConsiderIdElements.__init__)


def test_odemcustom_consideridelements_constructor_args():
    sig = inspect.signature(odemcustom_ConsiderIdElements.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_potentiallyhiddenidelements_is_not_abstract():
    assert not inspect.isabstract(odemcustom_PotentiallyHiddenIdElements)


def test_odemcustom_potentiallyhiddenidelements_constructor_exists():
    assert callable(odemcustom_PotentiallyHiddenIdElements.__init__)


def test_odemcustom_potentiallyhiddenidelements_constructor_args():
    sig = inspect.signature(odemcustom_PotentiallyHiddenIdElements.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_teststatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_TestStatement)


def test_odemcustom_teststatement_constructor_exists():
    assert callable(odemcustom_TestStatement.__init__)


def test_odemcustom_teststatement_constructor_args():
    sig = inspect.signature(odemcustom_TestStatement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_odemcustom_teststatement_has_value():
    assert hasattr(odemcustom_TestStatement, "value")
    descriptor = None
    for klass in odemcustom_TestStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_expandstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ExpandStatement)


def test_odemcustom_expandstatement_constructor_exists():
    assert callable(odemcustom_ExpandStatement.__init__)


def test_odemcustom_expandstatement_constructor_args():
    sig = inspect.signature(odemcustom_ExpandStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_parameter_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Parameter)


def test_odemcustom_parameter_constructor_exists():
    assert callable(odemcustom_Parameter.__init__)


def test_odemcustom_parameter_constructor_args():
    sig = inspect.signature(odemcustom_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_variable_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Variable)


def test_odemcustom_variable_constructor_exists():
    assert callable(odemcustom_Variable.__init__)


def test_odemcustom_variable_constructor_args():
    sig = inspect.signature(odemcustom_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "clazz" in params, "Missing parameter 'clazz'"
    assert "control" in params, "Missing parameter 'control'"

def test_odemcustom_variable_has_clazz():
    assert hasattr(odemcustom_Variable, "clazz")
    descriptor = None
    for klass in odemcustom_Variable.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)

def test_odemcustom_variable_has_control():
    assert hasattr(odemcustom_Variable, "control")
    descriptor = None
    for klass in odemcustom_Variable.__mro__:
        if "control" in klass.__dict__:
            descriptor = klass.__dict__["control"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(odemcustom_AbstractVariable)


def test_odemcustom_abstractvariable_constructor_exists():
    assert callable(odemcustom_AbstractVariable.__init__)


def test_odemcustom_abstractvariable_constructor_args():
    sig = inspect.signature(odemcustom_AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_statementexpression_is_not_abstract():
    assert not inspect.isabstract(StatementExpression)


def test_statementexpression_constructor_exists():
    assert callable(StatementExpression.__init__)


def test_statementexpression_constructor_args():
    sig = inspect.signature(StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_expandexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ExpandExpression)


def test_odemcustom_expandexpression_constructor_exists():
    assert callable(odemcustom_ExpandExpression.__init__)


def test_odemcustom_expandexpression_constructor_args():
    sig = inspect.signature(odemcustom_ExpandExpression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_procedurecall_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ProcedureCall)


def test_odemcustom_procedurecall_constructor_exists():
    assert callable(odemcustom_ProcedureCall.__init__)


def test_odemcustom_procedurecall_constructor_args():
    sig = inspect.signature(odemcustom_ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ExpressionStatement)


def test_expressionstatement_constructor_exists():
    assert callable(ExpressionStatement.__init__)


def test_expressionstatement_constructor_args():
    sig = inspect.signature(ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_deprecatedprocedurecallstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_DeprecatedProcedureCallStatement)


def test_odemcustom_deprecatedprocedurecallstatement_constructor_exists():
    assert callable(odemcustom_DeprecatedProcedureCallStatement.__init__)


def test_odemcustom_deprecatedprocedurecallstatement_constructor_args():
    sig = inspect.signature(odemcustom_DeprecatedProcedureCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_statementexpression_is_not_abstract():
    assert not inspect.isabstract(odemcustom_StatementExpression)


def test_odemcustom_statementexpression_constructor_exists():
    assert callable(odemcustom_StatementExpression.__init__)


def test_odemcustom_statementexpression_constructor_args():
    sig = inspect.signature(odemcustom_StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_advance_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Advance)


def test_odemcustom_advance_constructor_exists():
    assert callable(odemcustom_Advance.__init__)


def test_odemcustom_advance_constructor_args():
    sig = inspect.signature(odemcustom_Advance.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_savegenstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_SaveGenStatement)


def test_odemcustom_savegenstatement_constructor_exists():
    assert callable(odemcustom_SaveGenStatement.__init__)


def test_odemcustom_savegenstatement_constructor_args():
    sig = inspect.signature(odemcustom_SaveGenStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_reactivate_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Reactivate)


def test_odemcustom_reactivate_constructor_exists():
    assert callable(odemcustom_Reactivate.__init__)


def test_odemcustom_reactivate_constructor_args():
    sig = inspect.signature(odemcustom_Reactivate.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_resumegenstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ResumeGenStatement)


def test_odemcustom_resumegenstatement_constructor_exists():
    assert callable(odemcustom_ResumeGenStatement.__init__)


def test_odemcustom_resumegenstatement_constructor_args():
    sig = inspect.signature(odemcustom_ResumeGenStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_terminate_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Terminate)


def test_odemcustom_terminate_constructor_exists():
    assert callable(odemcustom_Terminate.__init__)


def test_odemcustom_terminate_constructor_args():
    sig = inspect.signature(odemcustom_Terminate.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_resetgencontextstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ResetGenContextStatement)


def test_odemcustom_resetgencontextstatement_constructor_exists():
    assert callable(odemcustom_ResetGenContextStatement.__init__)


def test_odemcustom_resetgencontextstatement_constructor_args():
    sig = inspect.signature(odemcustom_ResetGenContextStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_setstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_SetStatement)


def test_odemcustom_setstatement_constructor_exists():
    assert callable(odemcustom_SetStatement.__init__)


def test_odemcustom_setstatement_constructor_args():
    sig = inspect.signature(odemcustom_SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_continuestatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ContinueStatement)


def test_odemcustom_continuestatement_constructor_exists():
    assert callable(odemcustom_ContinueStatement.__init__)


def test_odemcustom_continuestatement_constructor_args():
    sig = inspect.signature(odemcustom_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_activateobject_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ActivateObject)


def test_odemcustom_activateobject_constructor_exists():
    assert callable(odemcustom_ActivateObject.__init__)


def test_odemcustom_activateobject_constructor_args():
    sig = inspect.signature(odemcustom_ActivateObject.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_odemcustom_activateobject_has_priority():
    assert hasattr(odemcustom_ActivateObject, "priority")
    descriptor = None
    for klass in odemcustom_ActivateObject.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_print_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Print)


def test_odemcustom_print_constructor_exists():
    assert callable(odemcustom_Print.__init__)


def test_odemcustom_print_constructor_args():
    sig = inspect.signature(odemcustom_Print.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_waituntil_is_not_abstract():
    assert not inspect.isabstract(odemcustom_WaitUntil)


def test_odemcustom_waituntil_constructor_exists():
    assert callable(odemcustom_WaitUntil.__init__)


def test_odemcustom_waituntil_constructor_args():
    sig = inspect.signature(odemcustom_WaitUntil.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_return_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Return)


def test_odemcustom_return_constructor_exists():
    assert callable(odemcustom_Return.__init__)


def test_odemcustom_return_constructor_args():
    sig = inspect.signature(odemcustom_Return.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_setgencontextstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_SetGenContextStatement)


def test_odemcustom_setgencontextstatement_constructor_exists():
    assert callable(odemcustom_SetGenContextStatement.__init__)


def test_odemcustom_setgencontextstatement_constructor_args():
    sig = inspect.signature(odemcustom_SetGenContextStatement.__init__)
    params = list(sig.parameters.keys())
    assert "addAfterContext" in params, "Missing parameter 'addAfterContext'"

def test_odemcustom_setgencontextstatement_has_addAfterContext():
    assert hasattr(odemcustom_SetGenContextStatement, "addAfterContext")
    descriptor = None
    for klass in odemcustom_SetGenContextStatement.__mro__:
        if "addAfterContext" in klass.__dict__:
            descriptor = klass.__dict__["addAfterContext"]
            break
    assert isinstance(descriptor, property)



def test_odemcustom_assignment_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Assignment)


def test_odemcustom_assignment_constructor_exists():
    assert callable(odemcustom_Assignment.__init__)


def test_odemcustom_assignment_constructor_args():
    sig = inspect.signature(odemcustom_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_breakstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_BreakStatement)


def test_odemcustom_breakstatement_constructor_exists():
    assert callable(odemcustom_BreakStatement.__init__)


def test_odemcustom_breakstatement_constructor_args():
    sig = inspect.signature(odemcustom_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_wait_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Wait)


def test_odemcustom_wait_constructor_exists():
    assert callable(odemcustom_Wait.__init__)


def test_odemcustom_wait_constructor_args():
    sig = inspect.signature(odemcustom_Wait.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_ExpressionStatement)


def test_odemcustom_expressionstatement_constructor_exists():
    assert callable(odemcustom_ExpressionStatement.__init__)


def test_odemcustom_expressionstatement_constructor_args():
    sig = inspect.signature(odemcustom_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_simplestatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_SimpleStatement)


def test_odemcustom_simplestatement_constructor_exists():
    assert callable(odemcustom_SimpleStatement.__init__)


def test_odemcustom_simplestatement_constructor_args():
    sig = inspect.signature(odemcustom_SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_compositestatement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_CompositeStatement)


def test_odemcustom_compositestatement_constructor_exists():
    assert callable(odemcustom_CompositeStatement.__init__)


def test_odemcustom_compositestatement_constructor_args():
    sig = inspect.signature(odemcustom_CompositeStatement.__init__)
    params = list(sig.parameters.keys())



def test_construct_is_not_abstract():
    assert not inspect.isabstract(Construct)


def test_construct_constructor_exists():
    assert callable(Construct.__init__)


def test_construct_constructor_args():
    sig = inspect.signature(Construct.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_statement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Statement)


def test_odemcustom_statement_constructor_exists():
    assert callable(odemcustom_Statement.__init__)


def test_odemcustom_statement_constructor_args():
    sig = inspect.signature(odemcustom_Statement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_expression_is_not_abstract():
    assert not inspect.isabstract(odemcustom_Expression)


def test_odemcustom_expression_constructor_exists():
    assert callable(odemcustom_Expression.__init__)


def test_odemcustom_expression_constructor_args():
    sig = inspect.signature(odemcustom_Expression.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_codeblock_is_not_abstract():
    assert not inspect.isabstract(odemcustom_CodeBlock)


def test_odemcustom_codeblock_constructor_exists():
    assert callable(odemcustom_CodeBlock.__init__)


def test_odemcustom_codeblock_constructor_args():
    sig = inspect.signature(odemcustom_CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_expandableelement_is_not_abstract():
    assert not inspect.isabstract(ExpandableElement)


def test_expandableelement_constructor_exists():
    assert callable(ExpandableElement.__init__)


def test_expandableelement_constructor_args():
    sig = inspect.signature(ExpandableElement.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_typeaccess_is_not_abstract():
    assert not inspect.isabstract(odemcustom_TypeAccess)


def test_odemcustom_typeaccess_constructor_exists():
    assert callable(odemcustom_TypeAccess.__init__)


def test_odemcustom_typeaccess_constructor_args():
    sig = inspect.signature(odemcustom_TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_variableaccess_is_not_abstract():
    assert not inspect.isabstract(odemcustom_VariableAccess)


def test_odemcustom_variableaccess_constructor_exists():
    assert callable(odemcustom_VariableAccess.__init__)


def test_odemcustom_variableaccess_constructor_args():
    sig = inspect.signature(odemcustom_VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_odemcustom_namedelement_is_not_abstract():
    assert not inspect.isabstract(odemcustom_NamedElement)


def test_odemcustom_namedelement_constructor_exists():
    assert callable(odemcustom_NamedElement.__init__)


def test_odemcustom_namedelement_constructor_args():
    sig = inspect.signature(odemcustom_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_odemcustom_namedelement_has_name():
    assert hasattr(odemcustom_NamedElement, "name")
    descriptor = None
    for klass in odemcustom_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bindingexpropkind_exists():
    # Check that the Enumeration exists
    assert BindingExprOpKind is not None

def test_bindingexpropkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BindingExprOpKind]
    expected_literals = [
        "ADD",
        "BOOL",
        "ASSIGN",
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
odemcustom_QuotedCode_strategy = st.builds(
    odemcustom_QuotedCode,
)
odemcustom_ExpandableElement_strategy = st.builds(
    odemcustom_ExpandableElement,
)
Module_strategy = st.builds(
    Module,
)
QuotedCode_strategy = st.builds(
    QuotedCode,
)
odemcustom_QuotedModuleContent_strategy = st.builds(
    odemcustom_QuotedModuleContent,
)
odemcustom_QuotedStatements_strategy = st.builds(
    odemcustom_QuotedStatements,
)
odemcustom_QuotedExpression_strategy = st.builds(
    odemcustom_QuotedExpression,
)
MappingPart_strategy = st.builds(
    MappingPart,
)
odemcustom_DynamicMappingPart_strategy = st.builds(
    odemcustom_DynamicMappingPart,
)
odemcustom_FixedMappingPart_strategy = st.builds(
    odemcustom_FixedMappingPart,
    code=
        safe_text
)
odemcustom_PropertyType_strategy = st.builds(
    odemcustom_PropertyType,
)
odemcustom_MappingPart_strategy = st.builds(
    odemcustom_MappingPart,
)
StructuredPropertyType_strategy = st.builds(
    StructuredPropertyType,
)
odemcustom_ReferencePropertyType_strategy = st.builds(
    odemcustom_ReferencePropertyType,
    rawReference=
        st.booleans()
)
odemcustom_CompositePropertyType_strategy = st.builds(
    odemcustom_CompositePropertyType,
    list=
        st.booleans()
)
ModifierExtensionsContainer_strategy = st.builds(
    ModifierExtensionsContainer,
)
odemcustom_Constructor_strategy = st.builds(
    odemcustom_Constructor,
)
ClassSimilar_strategy = st.builds(
    ClassSimilar,
)
odemcustom_QuotedClassContent_strategy = st.builds(
    odemcustom_QuotedClassContent,
)
Classifier_strategy = st.builds(
    Classifier,
)
odemcustom_Interface_strategy = st.builds(
    odemcustom_Interface,
)
odemcustom_Clazz_strategy = st.builds(
    odemcustom_Clazz,
    active=
        st.booleans()
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
odemcustom_BoolType_strategy = st.builds(
    odemcustom_BoolType,
)
odemcustom_IntType_strategy = st.builds(
    odemcustom_IntType,
)
odemcustom_DoubleType_strategy = st.builds(
    odemcustom_DoubleType,
)
odemcustom_VoidType_strategy = st.builds(
    odemcustom_VoidType,
)
Type_strategy = st.builds(
    Type,
)
odemcustom_NativeBinding_strategy = st.builds(
    odemcustom_NativeBinding,
    targetType=
        safe_text,
    targetLanguage=
        safe_text
)
ReferableRhsType_strategy = st.builds(
    ReferableRhsType,
)
odemcustom_AnnotatableElement_strategy = st.builds(
    odemcustom_AnnotatableElement,
)
odemcustom_KeyValuePair_strategy = st.builds(
    odemcustom_KeyValuePair,
)
odemcustom_AnnotationApplication_strategy = st.builds(
    odemcustom_AnnotationApplication,
)
AnnotatableElement_strategy = st.builds(
    AnnotatableElement,
)
CodeBlock_strategy = st.builds(
    CodeBlock,
)
odemcustom_StartCodeBlock_strategy = st.builds(
    odemcustom_StartCodeBlock,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
odemcustom_StringType_strategy = st.builds(
    odemcustom_StringType,
)
odemcustom_Import_strategy = st.builds(
    odemcustom_Import,
    file=
        safe_text
)
odemcustom_Model_strategy = st.builds(
    odemcustom_Model,
)
odemcustom_PrimitiveType_strategy = st.builds(
    odemcustom_PrimitiveType,
)
odemcustom_TypedElement_strategy = st.builds(
    odemcustom_TypedElement,
    isList=
        st.booleans()
)
odemcustom_Type_strategy = st.builds(
    odemcustom_Type,
)
odemcustom_ModifierExtensionsContainer_strategy = st.builds(
    odemcustom_ModifierExtensionsContainer,
)
odemcustom_Extension_strategy = st.builds(
    odemcustom_Extension,
)
odemcustom_EmbeddableExtensionsContainer_strategy = st.builds(
    odemcustom_EmbeddableExtensionsContainer,
)
odemcustom_IdResolution_strategy = st.builds(
    odemcustom_IdResolution,
    metaModelPlatformURI=
        safe_text
)
odemcustom_ClassAugment_strategy = st.builds(
    odemcustom_ClassAugment,
)
EmbeddableExtensionsContainer_strategy = st.builds(
    EmbeddableExtensionsContainer,
)
odemcustom_ClassSimilar_strategy = st.builds(
    odemcustom_ClassSimilar,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
odemcustom_SimpleAnnotation_strategy = st.builds(
    odemcustom_SimpleAnnotation,
    value=
        safe_text
)
odemcustom_Procedure_strategy = st.builds(
    odemcustom_Procedure,
    clazz=
        st.booleans()
)
odemcustom_Pattern_strategy = st.builds(
    odemcustom_Pattern,
    top=
        st.booleans()
)
odemcustom_ExtensionDefinition_strategy = st.builds(
    odemcustom_ExtensionDefinition,
)
odemcustom_Annotation_strategy = st.builds(
    odemcustom_Annotation,
)
odemcustom_Module_strategy = st.builds(
    odemcustom_Module,
)
odemcustom_Classifier_strategy = st.builds(
    odemcustom_Classifier,
)
NamedExtension_strategy = st.builds(
    NamedExtension,
)
odemcustom_Construct_strategy = st.builds(
    odemcustom_Construct,
    concreteSyntax=
        safe_text
)
PropertyType_strategy = st.builds(
    PropertyType,
)
odemcustom_StringPropertyType_strategy = st.builds(
    odemcustom_StringPropertyType,
)
odemcustom_BooleanPropertyType_strategy = st.builds(
    odemcustom_BooleanPropertyType,
    terminal=
        safe_text
)
odemcustom_StructuredPropertyType_strategy = st.builds(
    odemcustom_StructuredPropertyType,
)
odemcustom_IntPropertyType_strategy = st.builds(
    odemcustom_IntPropertyType,
)
odemcustom_IdPropertyType_strategy = st.builds(
    odemcustom_IdPropertyType,
)
odemcustom_RhsExpression_strategy = st.builds(
    odemcustom_RhsExpression,
)
odemcustom_ReferableRhsType_strategy = st.builds(
    odemcustom_ReferableRhsType,
)
RhsExpression_strategy = st.builds(
    RhsExpression,
)
odemcustom_AlternativeExpr_strategy = st.builds(
    odemcustom_AlternativeExpr,
)
odemcustom_RuntimeExpr_strategy = st.builds(
    odemcustom_RuntimeExpr,
)
odemcustom_ArbitraryExpr_strategy = st.builds(
    odemcustom_ArbitraryExpr,
)
odemcustom_OptionalExpr_strategy = st.builds(
    odemcustom_OptionalExpr,
)
odemcustom_TerminalExpr_strategy = st.builds(
    odemcustom_TerminalExpr,
    terminal=
        safe_text
)
odemcustom_AtLeastOneExpr_strategy = st.builds(
    odemcustom_AtLeastOneExpr,
)
odemcustom_PropertyBindingExpr_strategy = st.builds(
    odemcustom_PropertyBindingExpr,
    operator=
        safe_text
)
odemcustom_SequenceExpr_strategy = st.builds(
    odemcustom_SequenceExpr,
)
odemcustom_RuleExpr_strategy = st.builds(
    odemcustom_RuleExpr,
)
odemcustom_TsRule_strategy = st.builds(
    odemcustom_TsRule,
    metaClassName=
        safe_text
)
odemcustom_ExtensionRule_strategy = st.builds(
    odemcustom_ExtensionRule,
)
odemcustom_Mapping_strategy = st.builds(
    odemcustom_Mapping,
)
odemcustom_TextualSyntaxDef_strategy = st.builds(
    odemcustom_TextualSyntaxDef,
)
odemcustom_ModuleContentExtension_strategy = st.builds(
    odemcustom_ModuleContentExtension,
)
odemcustom_ClassContentExtension_strategy = st.builds(
    odemcustom_ClassContentExtension,
)
Extension_strategy = st.builds(
    Extension,
)
odemcustom_NamedExtension_strategy = st.builds(
    odemcustom_NamedExtension,
)
VariableAccess_strategy = st.builds(
    VariableAccess,
)
odemcustom_MetaAccess_strategy = st.builds(
    odemcustom_MetaAccess,
)
ElementAccess_strategy = st.builds(
    ElementAccess,
)
odemcustom_ArgumentExpression_strategy = st.builds(
    odemcustom_ArgumentExpression,
)
odemcustom_PredefinedId_strategy = st.builds(
    odemcustom_PredefinedId,
)
odemcustom_DepIdentifiableElement_strategy = st.builds(
    odemcustom_DepIdentifiableElement,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
odemcustom_Neg_strategy = st.builds(
    odemcustom_Neg,
)
SetOp_strategy = st.builds(
    SetOp,
)
odemcustom_FirstInSet_strategy = st.builds(
    odemcustom_FirstInSet,
)
odemcustom_AfterInSet_strategy = st.builds(
    odemcustom_AfterInSet,
)
odemcustom_BeforeInSet_strategy = st.builds(
    odemcustom_BeforeInSet,
)
odemcustom_LastInSet_strategy = st.builds(
    odemcustom_LastInSet,
)
odemcustom_Contains_strategy = st.builds(
    odemcustom_Contains,
)
odemcustom_ObjectAt_strategy = st.builds(
    odemcustom_ObjectAt,
)
odemcustom_IndexOf_strategy = st.builds(
    odemcustom_IndexOf,
)
odemcustom_SizeOfSet_strategy = st.builds(
    odemcustom_SizeOfSet,
)
PredefinedId_strategy = st.builds(
    PredefinedId,
)
odemcustom_MetaLiteral_strategy = st.builds(
    odemcustom_MetaLiteral,
)
odemcustom_SetOp_strategy = st.builds(
    odemcustom_SetOp,
)
odemcustom_SuperLiteral_strategy = st.builds(
    odemcustom_SuperLiteral,
)
odemcustom_TypeLiteral_strategy = st.builds(
    odemcustom_TypeLiteral,
)
odemcustom_MeLiteral_strategy = st.builds(
    odemcustom_MeLiteral,
)
odemcustom_Cast_strategy = st.builds(
    odemcustom_Cast,
)
odemcustom_Not_strategy = st.builds(
    odemcustom_Not,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
odemcustom_Less_strategy = st.builds(
    odemcustom_Less,
)
odemcustom_GreaterEqual_strategy = st.builds(
    odemcustom_GreaterEqual,
)
odemcustom_LessEqual_strategy = st.builds(
    odemcustom_LessEqual,
)
odemcustom_Mul_strategy = st.builds(
    odemcustom_Mul,
)
odemcustom_Mod_strategy = st.builds(
    odemcustom_Mod,
)
odemcustom_Minus_strategy = st.builds(
    odemcustom_Minus,
)
odemcustom_Greater_strategy = st.builds(
    odemcustom_Greater,
)
odemcustom_And_strategy = st.builds(
    odemcustom_And,
)
odemcustom_InstanceOf_strategy = st.builds(
    odemcustom_InstanceOf,
)
odemcustom_NotEqual_strategy = st.builds(
    odemcustom_NotEqual,
)
odemcustom_Or_strategy = st.builds(
    odemcustom_Or,
)
odemcustom_Equal_strategy = st.builds(
    odemcustom_Equal,
)
odemcustom_Div_strategy = st.builds(
    odemcustom_Div,
)
odemcustom_Plus_strategy = st.builds(
    odemcustom_Plus,
)
Expression_strategy = st.builds(
    Expression,
)
odemcustom_BinaryOperator_strategy = st.builds(
    odemcustom_BinaryOperator,
)
odemcustom_UnaryOperator_strategy = st.builds(
    odemcustom_UnaryOperator,
)
odemcustom_IdExpr_strategy = st.builds(
    odemcustom_IdExpr,
)
odemcustom_DoubleLiteral_strategy = st.builds(
    odemcustom_DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
odemcustom_FalseLiteral_strategy = st.builds(
    odemcustom_FalseLiteral,
)
odemcustom_CodeQuoteExpression_strategy = st.builds(
    odemcustom_CodeQuoteExpression,
)
odemcustom_CreateObject_strategy = st.builds(
    odemcustom_CreateObject,
)
odemcustom_IntLiteral_strategy = st.builds(
    odemcustom_IntLiteral,
    value=
        st.integers()
)
odemcustom_EvalExpr_strategy = st.builds(
    odemcustom_EvalExpr,
)
odemcustom_ActiveLiteral_strategy = st.builds(
    odemcustom_ActiveLiteral,
)
odemcustom_StringLiteral_strategy = st.builds(
    odemcustom_StringLiteral,
    value=
        safe_text
)
odemcustom_TrueLiteral_strategy = st.builds(
    odemcustom_TrueLiteral,
)
odemcustom_MetaExpr_strategy = st.builds(
    odemcustom_MetaExpr,
)
odemcustom_TimeLiteral_strategy = st.builds(
    odemcustom_TimeLiteral,
)
odemcustom_NullLiteral_strategy = st.builds(
    odemcustom_NullLiteral,
)
odemcustom_ElementAccess_strategy = st.builds(
    odemcustom_ElementAccess,
)
odemcustom_L1Expr_strategy = st.builds(
    odemcustom_L1Expr,
)
CompositeStatement_strategy = st.builds(
    CompositeStatement,
)
odemcustom_ExpandSection_strategy = st.builds(
    odemcustom_ExpandSection,
)
odemcustom_WhileStatement_strategy = st.builds(
    odemcustom_WhileStatement,
)
odemcustom_ForEachStatement_strategy = st.builds(
    odemcustom_ForEachStatement,
)
odemcustom_IfStatement_strategy = st.builds(
    odemcustom_IfStatement,
)
SetStatement_strategy = st.builds(
    SetStatement,
)
odemcustom_EmptySet_strategy = st.builds(
    odemcustom_EmptySet,
)
odemcustom_AddToSet_strategy = st.builds(
    odemcustom_AddToSet,
)
odemcustom_RemoveFromSet_strategy = st.builds(
    odemcustom_RemoveFromSet,
)
Statement_strategy = st.builds(
    Statement,
)
odemcustom_MappingStatement_strategy = st.builds(
    odemcustom_MappingStatement,
)
odemcustom_FindContainer_strategy = st.builds(
    odemcustom_FindContainer,
)
odemcustom_TargetStatement_strategy = st.builds(
    odemcustom_TargetStatement,
)
odemcustom_IncludePattern_strategy = st.builds(
    odemcustom_IncludePattern,
)
odemcustom_ConsiderIdElements_strategy = st.builds(
    odemcustom_ConsiderIdElements,
)
odemcustom_PotentiallyHiddenIdElements_strategy = st.builds(
    odemcustom_PotentiallyHiddenIdElements,
)
odemcustom_TestStatement_strategy = st.builds(
    odemcustom_TestStatement,
    value=
        safe_text
)
odemcustom_ExpandStatement_strategy = st.builds(
    odemcustom_ExpandStatement,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
odemcustom_Parameter_strategy = st.builds(
    odemcustom_Parameter,
)
odemcustom_Variable_strategy = st.builds(
    odemcustom_Variable,
    clazz=
        st.booleans(),
    control=
        st.booleans()
)
odemcustom_AbstractVariable_strategy = st.builds(
    odemcustom_AbstractVariable,
)
StatementExpression_strategy = st.builds(
    StatementExpression,
)
odemcustom_ExpandExpression_strategy = st.builds(
    odemcustom_ExpandExpression,
)
odemcustom_ProcedureCall_strategy = st.builds(
    odemcustom_ProcedureCall,
)
ExpressionStatement_strategy = st.builds(
    ExpressionStatement,
)
odemcustom_DeprecatedProcedureCallStatement_strategy = st.builds(
    odemcustom_DeprecatedProcedureCallStatement,
)
odemcustom_StatementExpression_strategy = st.builds(
    odemcustom_StatementExpression,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
odemcustom_Advance_strategy = st.builds(
    odemcustom_Advance,
)
odemcustom_SaveGenStatement_strategy = st.builds(
    odemcustom_SaveGenStatement,
)
odemcustom_Reactivate_strategy = st.builds(
    odemcustom_Reactivate,
)
odemcustom_ResumeGenStatement_strategy = st.builds(
    odemcustom_ResumeGenStatement,
)
odemcustom_Terminate_strategy = st.builds(
    odemcustom_Terminate,
)
odemcustom_ResetGenContextStatement_strategy = st.builds(
    odemcustom_ResetGenContextStatement,
)
odemcustom_SetStatement_strategy = st.builds(
    odemcustom_SetStatement,
)
odemcustom_ContinueStatement_strategy = st.builds(
    odemcustom_ContinueStatement,
)
odemcustom_ActivateObject_strategy = st.builds(
    odemcustom_ActivateObject,
    priority=
        st.integers()
)
odemcustom_Print_strategy = st.builds(
    odemcustom_Print,
)
odemcustom_WaitUntil_strategy = st.builds(
    odemcustom_WaitUntil,
)
odemcustom_Return_strategy = st.builds(
    odemcustom_Return,
)
odemcustom_SetGenContextStatement_strategy = st.builds(
    odemcustom_SetGenContextStatement,
    addAfterContext=
        st.booleans()
)
odemcustom_Assignment_strategy = st.builds(
    odemcustom_Assignment,
)
odemcustom_BreakStatement_strategy = st.builds(
    odemcustom_BreakStatement,
)
odemcustom_Wait_strategy = st.builds(
    odemcustom_Wait,
)
odemcustom_ExpressionStatement_strategy = st.builds(
    odemcustom_ExpressionStatement,
)
odemcustom_SimpleStatement_strategy = st.builds(
    odemcustom_SimpleStatement,
)
odemcustom_CompositeStatement_strategy = st.builds(
    odemcustom_CompositeStatement,
)
Construct_strategy = st.builds(
    Construct,
)
odemcustom_Statement_strategy = st.builds(
    odemcustom_Statement,
)
odemcustom_Expression_strategy = st.builds(
    odemcustom_Expression,
)
odemcustom_CodeBlock_strategy = st.builds(
    odemcustom_CodeBlock,
)
ExpandableElement_strategy = st.builds(
    ExpandableElement,
)
odemcustom_TypeAccess_strategy = st.builds(
    odemcustom_TypeAccess,
)
odemcustom_VariableAccess_strategy = st.builds(
    odemcustom_VariableAccess,
)
odemcustom_NamedElement_strategy = st.builds(
    odemcustom_NamedElement,
    name=
        safe_text
)

@given(instance=odemcustom_QuotedCode_strategy)
@settings(max_examples=50)
def test_odemcustom_quotedcode_instantiation(instance):
    assert isinstance(instance, odemcustom_QuotedCode)

@given(instance=odemcustom_ExpandableElement_strategy)
@settings(max_examples=50)
def test_odemcustom_expandableelement_instantiation(instance):
    assert isinstance(instance, odemcustom_ExpandableElement)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=QuotedCode_strategy)
@settings(max_examples=50)
def test_quotedcode_instantiation(instance):
    assert isinstance(instance, QuotedCode)

@given(instance=odemcustom_QuotedModuleContent_strategy)
@settings(max_examples=50)
def test_odemcustom_quotedmodulecontent_instantiation(instance):
    assert isinstance(instance, odemcustom_QuotedModuleContent)

@given(instance=odemcustom_QuotedStatements_strategy)
@settings(max_examples=50)
def test_odemcustom_quotedstatements_instantiation(instance):
    assert isinstance(instance, odemcustom_QuotedStatements)

@given(instance=odemcustom_QuotedExpression_strategy)
@settings(max_examples=50)
def test_odemcustom_quotedexpression_instantiation(instance):
    assert isinstance(instance, odemcustom_QuotedExpression)

@given(instance=MappingPart_strategy)
@settings(max_examples=50)
def test_mappingpart_instantiation(instance):
    assert isinstance(instance, MappingPart)

@given(instance=odemcustom_DynamicMappingPart_strategy)
@settings(max_examples=50)
def test_odemcustom_dynamicmappingpart_instantiation(instance):
    assert isinstance(instance, odemcustom_DynamicMappingPart)

@given(instance=odemcustom_FixedMappingPart_strategy)
@settings(max_examples=50)
def test_odemcustom_fixedmappingpart_instantiation(instance):
    assert isinstance(instance, odemcustom_FixedMappingPart)



@given(instance=odemcustom_FixedMappingPart_strategy)
def test_odemcustom_fixedmappingpart_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=odemcustom_PropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom_propertytype_instantiation(instance):
    assert isinstance(instance, odemcustom_PropertyType)

@given(instance=odemcustom_MappingPart_strategy)
@settings(max_examples=50)
def test_odemcustom_mappingpart_instantiation(instance):
    assert isinstance(instance, odemcustom_MappingPart)

@given(instance=StructuredPropertyType_strategy)
@settings(max_examples=50)
def test_structuredpropertytype_instantiation(instance):
    assert isinstance(instance, StructuredPropertyType)

@given(instance=odemcustom_ReferencePropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom_referencepropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom_ReferencePropertyType)



@given(instance=odemcustom_ReferencePropertyType_strategy)
def test_odemcustom_referencepropertytype_rawReference_setter(instance):
    original = instance.rawReference
    instance.rawReference = original
    assert instance.rawReference == original

@given(instance=odemcustom_CompositePropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom_compositepropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom_CompositePropertyType)



@given(instance=odemcustom_CompositePropertyType_strategy)
def test_odemcustom_compositepropertytype_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=ModifierExtensionsContainer_strategy)
@settings(max_examples=50)
def test_modifierextensionscontainer_instantiation(instance):
    assert isinstance(instance, ModifierExtensionsContainer)

@given(instance=odemcustom_Constructor_strategy)
@settings(max_examples=50)
def test_odemcustom_constructor_instantiation(instance):
    assert isinstance(instance, odemcustom_Constructor)

@given(instance=ClassSimilar_strategy)
@settings(max_examples=50)
def test_classsimilar_instantiation(instance):
    assert isinstance(instance, ClassSimilar)

@given(instance=odemcustom_QuotedClassContent_strategy)
@settings(max_examples=50)
def test_odemcustom_quotedclasscontent_instantiation(instance):
    assert isinstance(instance, odemcustom_QuotedClassContent)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=odemcustom_Interface_strategy)
@settings(max_examples=50)
def test_odemcustom_interface_instantiation(instance):
    assert isinstance(instance, odemcustom_Interface)

@given(instance=odemcustom_Clazz_strategy)
@settings(max_examples=50)
def test_odemcustom_clazz_instantiation(instance):
    assert isinstance(instance, odemcustom_Clazz)



@given(instance=odemcustom_Clazz_strategy)
def test_odemcustom_clazz_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=odemcustom_BoolType_strategy)
@settings(max_examples=50)
def test_odemcustom_booltype_instantiation(instance):
    assert isinstance(instance, odemcustom_BoolType)

@given(instance=odemcustom_IntType_strategy)
@settings(max_examples=50)
def test_odemcustom_inttype_instantiation(instance):
    assert isinstance(instance, odemcustom_IntType)

@given(instance=odemcustom_DoubleType_strategy)
@settings(max_examples=50)
def test_odemcustom_doubletype_instantiation(instance):
    assert isinstance(instance, odemcustom_DoubleType)

@given(instance=odemcustom_VoidType_strategy)
@settings(max_examples=50)
def test_odemcustom_voidtype_instantiation(instance):
    assert isinstance(instance, odemcustom_VoidType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=odemcustom_NativeBinding_strategy)
@settings(max_examples=50)
def test_odemcustom_nativebinding_instantiation(instance):
    assert isinstance(instance, odemcustom_NativeBinding)



@given(instance=odemcustom_NativeBinding_strategy)
def test_odemcustom_nativebinding_targetType_setter(instance):
    original = instance.targetType
    instance.targetType = original
    assert instance.targetType == original



@given(instance=odemcustom_NativeBinding_strategy)
def test_odemcustom_nativebinding_targetLanguage_setter(instance):
    original = instance.targetLanguage
    instance.targetLanguage = original
    assert instance.targetLanguage == original

@given(instance=ReferableRhsType_strategy)
@settings(max_examples=50)
def test_referablerhstype_instantiation(instance):
    assert isinstance(instance, ReferableRhsType)

@given(instance=odemcustom_AnnotatableElement_strategy)
@settings(max_examples=50)
def test_odemcustom_annotatableelement_instantiation(instance):
    assert isinstance(instance, odemcustom_AnnotatableElement)

@given(instance=odemcustom_KeyValuePair_strategy)
@settings(max_examples=50)
def test_odemcustom_keyvaluepair_instantiation(instance):
    assert isinstance(instance, odemcustom_KeyValuePair)

@given(instance=odemcustom_AnnotationApplication_strategy)
@settings(max_examples=50)
def test_odemcustom_annotationapplication_instantiation(instance):
    assert isinstance(instance, odemcustom_AnnotationApplication)

@given(instance=AnnotatableElement_strategy)
@settings(max_examples=50)
def test_annotatableelement_instantiation(instance):
    assert isinstance(instance, AnnotatableElement)

@given(instance=CodeBlock_strategy)
@settings(max_examples=50)
def test_codeblock_instantiation(instance):
    assert isinstance(instance, CodeBlock)

@given(instance=odemcustom_StartCodeBlock_strategy)
@settings(max_examples=50)
def test_odemcustom_startcodeblock_instantiation(instance):
    assert isinstance(instance, odemcustom_StartCodeBlock)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=odemcustom_StringType_strategy)
@settings(max_examples=50)
def test_odemcustom_stringtype_instantiation(instance):
    assert isinstance(instance, odemcustom_StringType)

@given(instance=odemcustom_Import_strategy)
@settings(max_examples=50)
def test_odemcustom_import_instantiation(instance):
    assert isinstance(instance, odemcustom_Import)



@given(instance=odemcustom_Import_strategy)
def test_odemcustom_import_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=odemcustom_Model_strategy)
@settings(max_examples=50)
def test_odemcustom_model_instantiation(instance):
    assert isinstance(instance, odemcustom_Model)

@given(instance=odemcustom_PrimitiveType_strategy)
@settings(max_examples=50)
def test_odemcustom_primitivetype_instantiation(instance):
    assert isinstance(instance, odemcustom_PrimitiveType)

@given(instance=odemcustom_TypedElement_strategy)
@settings(max_examples=50)
def test_odemcustom_typedelement_instantiation(instance):
    assert isinstance(instance, odemcustom_TypedElement)



@given(instance=odemcustom_TypedElement_strategy)
def test_odemcustom_typedelement_isList_setter(instance):
    original = instance.isList
    instance.isList = original
    assert instance.isList == original

@given(instance=odemcustom_Type_strategy)
@settings(max_examples=50)
def test_odemcustom_type_instantiation(instance):
    assert isinstance(instance, odemcustom_Type)

@given(instance=odemcustom_ModifierExtensionsContainer_strategy)
@settings(max_examples=50)
def test_odemcustom_modifierextensionscontainer_instantiation(instance):
    assert isinstance(instance, odemcustom_ModifierExtensionsContainer)

@given(instance=odemcustom_Extension_strategy)
@settings(max_examples=50)
def test_odemcustom_extension_instantiation(instance):
    assert isinstance(instance, odemcustom_Extension)

@given(instance=odemcustom_EmbeddableExtensionsContainer_strategy)
@settings(max_examples=50)
def test_odemcustom_embeddableextensionscontainer_instantiation(instance):
    assert isinstance(instance, odemcustom_EmbeddableExtensionsContainer)

@given(instance=odemcustom_IdResolution_strategy)
@settings(max_examples=50)
def test_odemcustom_idresolution_instantiation(instance):
    assert isinstance(instance, odemcustom_IdResolution)



@given(instance=odemcustom_IdResolution_strategy)
def test_odemcustom_idresolution_metaModelPlatformURI_setter(instance):
    original = instance.metaModelPlatformURI
    instance.metaModelPlatformURI = original
    assert instance.metaModelPlatformURI == original

@given(instance=odemcustom_ClassAugment_strategy)
@settings(max_examples=50)
def test_odemcustom_classaugment_instantiation(instance):
    assert isinstance(instance, odemcustom_ClassAugment)

@given(instance=EmbeddableExtensionsContainer_strategy)
@settings(max_examples=50)
def test_embeddableextensionscontainer_instantiation(instance):
    assert isinstance(instance, EmbeddableExtensionsContainer)

@given(instance=odemcustom_ClassSimilar_strategy)
@settings(max_examples=50)
def test_odemcustom_classsimilar_instantiation(instance):
    assert isinstance(instance, odemcustom_ClassSimilar)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=odemcustom_SimpleAnnotation_strategy)
@settings(max_examples=50)
def test_odemcustom_simpleannotation_instantiation(instance):
    assert isinstance(instance, odemcustom_SimpleAnnotation)



@given(instance=odemcustom_SimpleAnnotation_strategy)
def test_odemcustom_simpleannotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=odemcustom_Procedure_strategy)
@settings(max_examples=50)
def test_odemcustom_procedure_instantiation(instance):
    assert isinstance(instance, odemcustom_Procedure)



@given(instance=odemcustom_Procedure_strategy)
def test_odemcustom_procedure_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=odemcustom_Pattern_strategy)
@settings(max_examples=50)
def test_odemcustom_pattern_instantiation(instance):
    assert isinstance(instance, odemcustom_Pattern)



@given(instance=odemcustom_Pattern_strategy)
def test_odemcustom_pattern_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=odemcustom_ExtensionDefinition_strategy)
@settings(max_examples=50)
def test_odemcustom_extensiondefinition_instantiation(instance):
    assert isinstance(instance, odemcustom_ExtensionDefinition)

@given(instance=odemcustom_Annotation_strategy)
@settings(max_examples=50)
def test_odemcustom_annotation_instantiation(instance):
    assert isinstance(instance, odemcustom_Annotation)

@given(instance=odemcustom_Module_strategy)
@settings(max_examples=50)
def test_odemcustom_module_instantiation(instance):
    assert isinstance(instance, odemcustom_Module)

@given(instance=odemcustom_Classifier_strategy)
@settings(max_examples=50)
def test_odemcustom_classifier_instantiation(instance):
    assert isinstance(instance, odemcustom_Classifier)

@given(instance=NamedExtension_strategy)
@settings(max_examples=50)
def test_namedextension_instantiation(instance):
    assert isinstance(instance, NamedExtension)

@given(instance=odemcustom_Construct_strategy)
@settings(max_examples=50)
def test_odemcustom_construct_instantiation(instance):
    assert isinstance(instance, odemcustom_Construct)



@given(instance=odemcustom_Construct_strategy)
def test_odemcustom_construct_concreteSyntax_setter(instance):
    original = instance.concreteSyntax
    instance.concreteSyntax = original
    assert instance.concreteSyntax == original

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=odemcustom_StringPropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom_stringpropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom_StringPropertyType)

@given(instance=odemcustom_BooleanPropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom_booleanpropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom_BooleanPropertyType)



@given(instance=odemcustom_BooleanPropertyType_strategy)
def test_odemcustom_booleanpropertytype_terminal_setter(instance):
    original = instance.terminal
    instance.terminal = original
    assert instance.terminal == original

@given(instance=odemcustom_StructuredPropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom_structuredpropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom_StructuredPropertyType)

@given(instance=odemcustom_IntPropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom_intpropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom_IntPropertyType)

@given(instance=odemcustom_IdPropertyType_strategy)
@settings(max_examples=50)
def test_odemcustom_idpropertytype_instantiation(instance):
    assert isinstance(instance, odemcustom_IdPropertyType)

@given(instance=odemcustom_RhsExpression_strategy)
@settings(max_examples=50)
def test_odemcustom_rhsexpression_instantiation(instance):
    assert isinstance(instance, odemcustom_RhsExpression)

@given(instance=odemcustom_ReferableRhsType_strategy)
@settings(max_examples=50)
def test_odemcustom_referablerhstype_instantiation(instance):
    assert isinstance(instance, odemcustom_ReferableRhsType)

@given(instance=RhsExpression_strategy)
@settings(max_examples=50)
def test_rhsexpression_instantiation(instance):
    assert isinstance(instance, RhsExpression)

@given(instance=odemcustom_AlternativeExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_alternativeexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_AlternativeExpr)

@given(instance=odemcustom_RuntimeExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_runtimeexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_RuntimeExpr)

@given(instance=odemcustom_ArbitraryExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_arbitraryexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_ArbitraryExpr)

@given(instance=odemcustom_OptionalExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_optionalexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_OptionalExpr)

@given(instance=odemcustom_TerminalExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_terminalexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_TerminalExpr)



@given(instance=odemcustom_TerminalExpr_strategy)
def test_odemcustom_terminalexpr_terminal_setter(instance):
    original = instance.terminal
    instance.terminal = original
    assert instance.terminal == original

@given(instance=odemcustom_AtLeastOneExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_atleastoneexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_AtLeastOneExpr)

@given(instance=odemcustom_PropertyBindingExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_propertybindingexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_PropertyBindingExpr)



@given(instance=odemcustom_PropertyBindingExpr_strategy)
def test_odemcustom_propertybindingexpr_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=odemcustom_SequenceExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_sequenceexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_SequenceExpr)

@given(instance=odemcustom_RuleExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_ruleexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_RuleExpr)

@given(instance=odemcustom_TsRule_strategy)
@settings(max_examples=50)
def test_odemcustom_tsrule_instantiation(instance):
    assert isinstance(instance, odemcustom_TsRule)



@given(instance=odemcustom_TsRule_strategy)
def test_odemcustom_tsrule_metaClassName_setter(instance):
    original = instance.metaClassName
    instance.metaClassName = original
    assert instance.metaClassName == original

@given(instance=odemcustom_ExtensionRule_strategy)
@settings(max_examples=50)
def test_odemcustom_extensionrule_instantiation(instance):
    assert isinstance(instance, odemcustom_ExtensionRule)

@given(instance=odemcustom_Mapping_strategy)
@settings(max_examples=50)
def test_odemcustom_mapping_instantiation(instance):
    assert isinstance(instance, odemcustom_Mapping)

@given(instance=odemcustom_TextualSyntaxDef_strategy)
@settings(max_examples=50)
def test_odemcustom_textualsyntaxdef_instantiation(instance):
    assert isinstance(instance, odemcustom_TextualSyntaxDef)

@given(instance=odemcustom_ModuleContentExtension_strategy)
@settings(max_examples=50)
def test_odemcustom_modulecontentextension_instantiation(instance):
    assert isinstance(instance, odemcustom_ModuleContentExtension)

@given(instance=odemcustom_ClassContentExtension_strategy)
@settings(max_examples=50)
def test_odemcustom_classcontentextension_instantiation(instance):
    assert isinstance(instance, odemcustom_ClassContentExtension)

@given(instance=Extension_strategy)
@settings(max_examples=50)
def test_extension_instantiation(instance):
    assert isinstance(instance, Extension)

@given(instance=odemcustom_NamedExtension_strategy)
@settings(max_examples=50)
def test_odemcustom_namedextension_instantiation(instance):
    assert isinstance(instance, odemcustom_NamedExtension)

@given(instance=VariableAccess_strategy)
@settings(max_examples=50)
def test_variableaccess_instantiation(instance):
    assert isinstance(instance, VariableAccess)

@given(instance=odemcustom_MetaAccess_strategy)
@settings(max_examples=50)
def test_odemcustom_metaaccess_instantiation(instance):
    assert isinstance(instance, odemcustom_MetaAccess)

@given(instance=ElementAccess_strategy)
@settings(max_examples=50)
def test_elementaccess_instantiation(instance):
    assert isinstance(instance, ElementAccess)

@given(instance=odemcustom_ArgumentExpression_strategy)
@settings(max_examples=50)
def test_odemcustom_argumentexpression_instantiation(instance):
    assert isinstance(instance, odemcustom_ArgumentExpression)

@given(instance=odemcustom_PredefinedId_strategy)
@settings(max_examples=50)
def test_odemcustom_predefinedid_instantiation(instance):
    assert isinstance(instance, odemcustom_PredefinedId)

@given(instance=odemcustom_DepIdentifiableElement_strategy)
@settings(max_examples=50)
def test_odemcustom_depidentifiableelement_instantiation(instance):
    assert isinstance(instance, odemcustom_DepIdentifiableElement)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=odemcustom_Neg_strategy)
@settings(max_examples=50)
def test_odemcustom_neg_instantiation(instance):
    assert isinstance(instance, odemcustom_Neg)

@given(instance=SetOp_strategy)
@settings(max_examples=50)
def test_setop_instantiation(instance):
    assert isinstance(instance, SetOp)

@given(instance=odemcustom_FirstInSet_strategy)
@settings(max_examples=50)
def test_odemcustom_firstinset_instantiation(instance):
    assert isinstance(instance, odemcustom_FirstInSet)

@given(instance=odemcustom_AfterInSet_strategy)
@settings(max_examples=50)
def test_odemcustom_afterinset_instantiation(instance):
    assert isinstance(instance, odemcustom_AfterInSet)

@given(instance=odemcustom_BeforeInSet_strategy)
@settings(max_examples=50)
def test_odemcustom_beforeinset_instantiation(instance):
    assert isinstance(instance, odemcustom_BeforeInSet)

@given(instance=odemcustom_LastInSet_strategy)
@settings(max_examples=50)
def test_odemcustom_lastinset_instantiation(instance):
    assert isinstance(instance, odemcustom_LastInSet)

@given(instance=odemcustom_Contains_strategy)
@settings(max_examples=50)
def test_odemcustom_contains_instantiation(instance):
    assert isinstance(instance, odemcustom_Contains)

@given(instance=odemcustom_ObjectAt_strategy)
@settings(max_examples=50)
def test_odemcustom_objectat_instantiation(instance):
    assert isinstance(instance, odemcustom_ObjectAt)

@given(instance=odemcustom_IndexOf_strategy)
@settings(max_examples=50)
def test_odemcustom_indexof_instantiation(instance):
    assert isinstance(instance, odemcustom_IndexOf)

@given(instance=odemcustom_SizeOfSet_strategy)
@settings(max_examples=50)
def test_odemcustom_sizeofset_instantiation(instance):
    assert isinstance(instance, odemcustom_SizeOfSet)

@given(instance=PredefinedId_strategy)
@settings(max_examples=50)
def test_predefinedid_instantiation(instance):
    assert isinstance(instance, PredefinedId)

@given(instance=odemcustom_MetaLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_metaliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_MetaLiteral)

@given(instance=odemcustom_SetOp_strategy)
@settings(max_examples=50)
def test_odemcustom_setop_instantiation(instance):
    assert isinstance(instance, odemcustom_SetOp)

@given(instance=odemcustom_SuperLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_superliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_SuperLiteral)

@given(instance=odemcustom_TypeLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_typeliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_TypeLiteral)

@given(instance=odemcustom_MeLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_meliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_MeLiteral)

@given(instance=odemcustom_Cast_strategy)
@settings(max_examples=50)
def test_odemcustom_cast_instantiation(instance):
    assert isinstance(instance, odemcustom_Cast)

@given(instance=odemcustom_Not_strategy)
@settings(max_examples=50)
def test_odemcustom_not_instantiation(instance):
    assert isinstance(instance, odemcustom_Not)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=odemcustom_Less_strategy)
@settings(max_examples=50)
def test_odemcustom_less_instantiation(instance):
    assert isinstance(instance, odemcustom_Less)

@given(instance=odemcustom_GreaterEqual_strategy)
@settings(max_examples=50)
def test_odemcustom_greaterequal_instantiation(instance):
    assert isinstance(instance, odemcustom_GreaterEqual)

@given(instance=odemcustom_LessEqual_strategy)
@settings(max_examples=50)
def test_odemcustom_lessequal_instantiation(instance):
    assert isinstance(instance, odemcustom_LessEqual)

@given(instance=odemcustom_Mul_strategy)
@settings(max_examples=50)
def test_odemcustom_mul_instantiation(instance):
    assert isinstance(instance, odemcustom_Mul)

@given(instance=odemcustom_Mod_strategy)
@settings(max_examples=50)
def test_odemcustom_mod_instantiation(instance):
    assert isinstance(instance, odemcustom_Mod)

@given(instance=odemcustom_Minus_strategy)
@settings(max_examples=50)
def test_odemcustom_minus_instantiation(instance):
    assert isinstance(instance, odemcustom_Minus)

@given(instance=odemcustom_Greater_strategy)
@settings(max_examples=50)
def test_odemcustom_greater_instantiation(instance):
    assert isinstance(instance, odemcustom_Greater)

@given(instance=odemcustom_And_strategy)
@settings(max_examples=50)
def test_odemcustom_and_instantiation(instance):
    assert isinstance(instance, odemcustom_And)

@given(instance=odemcustom_InstanceOf_strategy)
@settings(max_examples=50)
def test_odemcustom_instanceof_instantiation(instance):
    assert isinstance(instance, odemcustom_InstanceOf)

@given(instance=odemcustom_NotEqual_strategy)
@settings(max_examples=50)
def test_odemcustom_notequal_instantiation(instance):
    assert isinstance(instance, odemcustom_NotEqual)

@given(instance=odemcustom_Or_strategy)
@settings(max_examples=50)
def test_odemcustom_or_instantiation(instance):
    assert isinstance(instance, odemcustom_Or)

@given(instance=odemcustom_Equal_strategy)
@settings(max_examples=50)
def test_odemcustom_equal_instantiation(instance):
    assert isinstance(instance, odemcustom_Equal)

@given(instance=odemcustom_Div_strategy)
@settings(max_examples=50)
def test_odemcustom_div_instantiation(instance):
    assert isinstance(instance, odemcustom_Div)

@given(instance=odemcustom_Plus_strategy)
@settings(max_examples=50)
def test_odemcustom_plus_instantiation(instance):
    assert isinstance(instance, odemcustom_Plus)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=odemcustom_BinaryOperator_strategy)
@settings(max_examples=50)
def test_odemcustom_binaryoperator_instantiation(instance):
    assert isinstance(instance, odemcustom_BinaryOperator)

@given(instance=odemcustom_UnaryOperator_strategy)
@settings(max_examples=50)
def test_odemcustom_unaryoperator_instantiation(instance):
    assert isinstance(instance, odemcustom_UnaryOperator)

@given(instance=odemcustom_IdExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_idexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_IdExpr)

@given(instance=odemcustom_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_doubleliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_DoubleLiteral)



@given(instance=odemcustom_DoubleLiteral_strategy)
def test_odemcustom_doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=odemcustom_FalseLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_falseliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_FalseLiteral)

@given(instance=odemcustom_CodeQuoteExpression_strategy)
@settings(max_examples=50)
def test_odemcustom_codequoteexpression_instantiation(instance):
    assert isinstance(instance, odemcustom_CodeQuoteExpression)

@given(instance=odemcustom_CreateObject_strategy)
@settings(max_examples=50)
def test_odemcustom_createobject_instantiation(instance):
    assert isinstance(instance, odemcustom_CreateObject)

@given(instance=odemcustom_IntLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_intliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_IntLiteral)



@given(instance=odemcustom_IntLiteral_strategy)
def test_odemcustom_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=odemcustom_EvalExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_evalexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_EvalExpr)

@given(instance=odemcustom_ActiveLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_activeliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_ActiveLiteral)

@given(instance=odemcustom_StringLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_stringliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_StringLiteral)



@given(instance=odemcustom_StringLiteral_strategy)
def test_odemcustom_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=odemcustom_TrueLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_trueliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_TrueLiteral)

@given(instance=odemcustom_MetaExpr_strategy)
@settings(max_examples=50)
def test_odemcustom_metaexpr_instantiation(instance):
    assert isinstance(instance, odemcustom_MetaExpr)

@given(instance=odemcustom_TimeLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_timeliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_TimeLiteral)

@given(instance=odemcustom_NullLiteral_strategy)
@settings(max_examples=50)
def test_odemcustom_nullliteral_instantiation(instance):
    assert isinstance(instance, odemcustom_NullLiteral)

@given(instance=odemcustom_ElementAccess_strategy)
@settings(max_examples=50)
def test_odemcustom_elementaccess_instantiation(instance):
    assert isinstance(instance, odemcustom_ElementAccess)

@given(instance=odemcustom_L1Expr_strategy)
@settings(max_examples=50)
def test_odemcustom_l1expr_instantiation(instance):
    assert isinstance(instance, odemcustom_L1Expr)

@given(instance=CompositeStatement_strategy)
@settings(max_examples=50)
def test_compositestatement_instantiation(instance):
    assert isinstance(instance, CompositeStatement)

@given(instance=odemcustom_ExpandSection_strategy)
@settings(max_examples=50)
def test_odemcustom_expandsection_instantiation(instance):
    assert isinstance(instance, odemcustom_ExpandSection)

@given(instance=odemcustom_WhileStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_whilestatement_instantiation(instance):
    assert isinstance(instance, odemcustom_WhileStatement)

@given(instance=odemcustom_ForEachStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_foreachstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_ForEachStatement)

@given(instance=odemcustom_IfStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_ifstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_IfStatement)

@given(instance=SetStatement_strategy)
@settings(max_examples=50)
def test_setstatement_instantiation(instance):
    assert isinstance(instance, SetStatement)

@given(instance=odemcustom_EmptySet_strategy)
@settings(max_examples=50)
def test_odemcustom_emptyset_instantiation(instance):
    assert isinstance(instance, odemcustom_EmptySet)

@given(instance=odemcustom_AddToSet_strategy)
@settings(max_examples=50)
def test_odemcustom_addtoset_instantiation(instance):
    assert isinstance(instance, odemcustom_AddToSet)

@given(instance=odemcustom_RemoveFromSet_strategy)
@settings(max_examples=50)
def test_odemcustom_removefromset_instantiation(instance):
    assert isinstance(instance, odemcustom_RemoveFromSet)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=odemcustom_MappingStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_mappingstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_MappingStatement)

@given(instance=odemcustom_FindContainer_strategy)
@settings(max_examples=50)
def test_odemcustom_findcontainer_instantiation(instance):
    assert isinstance(instance, odemcustom_FindContainer)

@given(instance=odemcustom_TargetStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_targetstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_TargetStatement)

@given(instance=odemcustom_IncludePattern_strategy)
@settings(max_examples=50)
def test_odemcustom_includepattern_instantiation(instance):
    assert isinstance(instance, odemcustom_IncludePattern)

@given(instance=odemcustom_ConsiderIdElements_strategy)
@settings(max_examples=50)
def test_odemcustom_consideridelements_instantiation(instance):
    assert isinstance(instance, odemcustom_ConsiderIdElements)

@given(instance=odemcustom_PotentiallyHiddenIdElements_strategy)
@settings(max_examples=50)
def test_odemcustom_potentiallyhiddenidelements_instantiation(instance):
    assert isinstance(instance, odemcustom_PotentiallyHiddenIdElements)

@given(instance=odemcustom_TestStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_teststatement_instantiation(instance):
    assert isinstance(instance, odemcustom_TestStatement)



@given(instance=odemcustom_TestStatement_strategy)
def test_odemcustom_teststatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=odemcustom_ExpandStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_expandstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_ExpandStatement)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=odemcustom_Parameter_strategy)
@settings(max_examples=50)
def test_odemcustom_parameter_instantiation(instance):
    assert isinstance(instance, odemcustom_Parameter)

@given(instance=odemcustom_Variable_strategy)
@settings(max_examples=50)
def test_odemcustom_variable_instantiation(instance):
    assert isinstance(instance, odemcustom_Variable)



@given(instance=odemcustom_Variable_strategy)
def test_odemcustom_variable_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original



@given(instance=odemcustom_Variable_strategy)
def test_odemcustom_variable_control_setter(instance):
    original = instance.control
    instance.control = original
    assert instance.control == original

@given(instance=odemcustom_AbstractVariable_strategy)
@settings(max_examples=50)
def test_odemcustom_abstractvariable_instantiation(instance):
    assert isinstance(instance, odemcustom_AbstractVariable)

@given(instance=StatementExpression_strategy)
@settings(max_examples=50)
def test_statementexpression_instantiation(instance):
    assert isinstance(instance, StatementExpression)

@given(instance=odemcustom_ExpandExpression_strategy)
@settings(max_examples=50)
def test_odemcustom_expandexpression_instantiation(instance):
    assert isinstance(instance, odemcustom_ExpandExpression)

@given(instance=odemcustom_ProcedureCall_strategy)
@settings(max_examples=50)
def test_odemcustom_procedurecall_instantiation(instance):
    assert isinstance(instance, odemcustom_ProcedureCall)

@given(instance=ExpressionStatement_strategy)
@settings(max_examples=50)
def test_expressionstatement_instantiation(instance):
    assert isinstance(instance, ExpressionStatement)

@given(instance=odemcustom_DeprecatedProcedureCallStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_deprecatedprocedurecallstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_DeprecatedProcedureCallStatement)

@given(instance=odemcustom_StatementExpression_strategy)
@settings(max_examples=50)
def test_odemcustom_statementexpression_instantiation(instance):
    assert isinstance(instance, odemcustom_StatementExpression)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=odemcustom_Advance_strategy)
@settings(max_examples=50)
def test_odemcustom_advance_instantiation(instance):
    assert isinstance(instance, odemcustom_Advance)

@given(instance=odemcustom_SaveGenStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_savegenstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_SaveGenStatement)

@given(instance=odemcustom_Reactivate_strategy)
@settings(max_examples=50)
def test_odemcustom_reactivate_instantiation(instance):
    assert isinstance(instance, odemcustom_Reactivate)

@given(instance=odemcustom_ResumeGenStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_resumegenstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_ResumeGenStatement)

@given(instance=odemcustom_Terminate_strategy)
@settings(max_examples=50)
def test_odemcustom_terminate_instantiation(instance):
    assert isinstance(instance, odemcustom_Terminate)

@given(instance=odemcustom_ResetGenContextStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_resetgencontextstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_ResetGenContextStatement)

@given(instance=odemcustom_SetStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_setstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_SetStatement)

@given(instance=odemcustom_ContinueStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_continuestatement_instantiation(instance):
    assert isinstance(instance, odemcustom_ContinueStatement)

@given(instance=odemcustom_ActivateObject_strategy)
@settings(max_examples=50)
def test_odemcustom_activateobject_instantiation(instance):
    assert isinstance(instance, odemcustom_ActivateObject)



@given(instance=odemcustom_ActivateObject_strategy)
def test_odemcustom_activateobject_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=odemcustom_Print_strategy)
@settings(max_examples=50)
def test_odemcustom_print_instantiation(instance):
    assert isinstance(instance, odemcustom_Print)

@given(instance=odemcustom_WaitUntil_strategy)
@settings(max_examples=50)
def test_odemcustom_waituntil_instantiation(instance):
    assert isinstance(instance, odemcustom_WaitUntil)

@given(instance=odemcustom_Return_strategy)
@settings(max_examples=50)
def test_odemcustom_return_instantiation(instance):
    assert isinstance(instance, odemcustom_Return)

@given(instance=odemcustom_SetGenContextStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_setgencontextstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_SetGenContextStatement)



@given(instance=odemcustom_SetGenContextStatement_strategy)
def test_odemcustom_setgencontextstatement_addAfterContext_setter(instance):
    original = instance.addAfterContext
    instance.addAfterContext = original
    assert instance.addAfterContext == original

@given(instance=odemcustom_Assignment_strategy)
@settings(max_examples=50)
def test_odemcustom_assignment_instantiation(instance):
    assert isinstance(instance, odemcustom_Assignment)

@given(instance=odemcustom_BreakStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_breakstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_BreakStatement)

@given(instance=odemcustom_Wait_strategy)
@settings(max_examples=50)
def test_odemcustom_wait_instantiation(instance):
    assert isinstance(instance, odemcustom_Wait)

@given(instance=odemcustom_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_expressionstatement_instantiation(instance):
    assert isinstance(instance, odemcustom_ExpressionStatement)

@given(instance=odemcustom_SimpleStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_simplestatement_instantiation(instance):
    assert isinstance(instance, odemcustom_SimpleStatement)

@given(instance=odemcustom_CompositeStatement_strategy)
@settings(max_examples=50)
def test_odemcustom_compositestatement_instantiation(instance):
    assert isinstance(instance, odemcustom_CompositeStatement)

@given(instance=Construct_strategy)
@settings(max_examples=50)
def test_construct_instantiation(instance):
    assert isinstance(instance, Construct)

@given(instance=odemcustom_Statement_strategy)
@settings(max_examples=50)
def test_odemcustom_statement_instantiation(instance):
    assert isinstance(instance, odemcustom_Statement)

@given(instance=odemcustom_Expression_strategy)
@settings(max_examples=50)
def test_odemcustom_expression_instantiation(instance):
    assert isinstance(instance, odemcustom_Expression)

@given(instance=odemcustom_CodeBlock_strategy)
@settings(max_examples=50)
def test_odemcustom_codeblock_instantiation(instance):
    assert isinstance(instance, odemcustom_CodeBlock)

@given(instance=ExpandableElement_strategy)
@settings(max_examples=50)
def test_expandableelement_instantiation(instance):
    assert isinstance(instance, ExpandableElement)

@given(instance=odemcustom_TypeAccess_strategy)
@settings(max_examples=50)
def test_odemcustom_typeaccess_instantiation(instance):
    assert isinstance(instance, odemcustom_TypeAccess)

@given(instance=odemcustom_VariableAccess_strategy)
@settings(max_examples=50)
def test_odemcustom_variableaccess_instantiation(instance):
    assert isinstance(instance, odemcustom_VariableAccess)

@given(instance=odemcustom_NamedElement_strategy)
@settings(max_examples=50)
def test_odemcustom_namedelement_instantiation(instance):
    assert isinstance(instance, odemcustom_NamedElement)



@given(instance=odemcustom_NamedElement_strategy)
def test_odemcustom_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

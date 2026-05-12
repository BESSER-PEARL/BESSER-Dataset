import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypeOrVoid,
    cSharp_Void,
    cSharp_ParameterArray,
    OperatorDeclarator,
    cSharp_UnaryOperatorDeclarator,
    cSharp_BinaryOperatorDeclarator,
    cSharp_ConversionOperatorDeclarator,
    cSharp_OperatorDeclarator,
    cSharp_IndexerDeclarator,
    cSharp_ConstructorDeclarator,
    cSharp_StaticConstructorDeclaration,
    cSharp_DestructorDeclaration,
    cSharp_ConstructorDeclaration,
    cSharp_OperatorDeclaration,
    cSharp_IndexerDeclaration,
    cSharp_EventDeclaration,
    cSharp_PropertyDeclaration,
    cSharp_ConstantDeclaration,
    cSharp_MethodDeclaration,
    cSharp_FieldDeclaration,
    cSharp_Argument,
    ConstructorInitializer,
    cSharp_ConstructorInitializer,
    cSharp_InterfaceAccessors,
    cSharp_ClassMemberDeclaration,
    cSharp_ClassBody,
    cSharp_ClassBase,
    cSharp_InterfaceEventDeclaration,
    cSharp_InterfaceMethodDeclaration,
    cSharp_InterfaceMemberDeclaration,
    cSharp_InterfaceBody,
    cSharp_EnumMemberDeclaration,
    cSharp_EnumBody,
    cSharp_DelegateDeclaration,
    cSharp_EnumDeclaration,
    cSharp_InterfaceDeclaration,
    cSharp_FormalParameterList,
    cSharp_InterfacePropertyDeclaration,
    cSharp_InterfaceIndexerDeclaration,
    cSharp_TypeDeclaration,
    cSharp_NamespaceDeclaration,
    cSharp_QualifiedIdentifierList,
    ClassBase,
    ArrayType,
    BuiltInType,
    cSharp_BuiltInClassType,
    cSharp_IntegralType,
    cSharp_ConstantDeclarator,
    cSharp_AccessorDeclarations,
    cSharp_EventAccessorDeclarations,
    cSharp_ClassDeclaration,
    BuiltInClassType,
    cSharp_String,
    cSharp_Object,
    cSharp_Double,
    cSharp_Float,
    cSharp_Decimal,
    cSharp_Bool,
    IntegralType,
    cSharp_Char,
    cSharp_Short,
    cSharp_Long,
    cSharp_ULong,
    cSharp_Byte,
    cSharp_UShort,
    cSharp_UInt,
    cSharp_Int,
    cSharp_SByte,
    GetAccessorDeclaration,
    SetAccessorDeclaration,
    cSharp_MaybeEmptyBlock,
    MaybeEmptyBlock,
    AddAccessorDeclaration,
    RemoveAccessorDeclaration,
    cSharp_ElsePart,
    cSharp_SwitchLabel,
    cSharp_SwitchSection,
    cSharp_SwitchStatement,
    cSharp_IfStatement,
    cSharp_StatementExpressionList,
    cSharp_ForInitializer,
    cSharp_ForeachStatement,
    cSharp_ForStatement,
    cSharp_DoStatement,
    cSharp_WhileStatement,
    cSharp_GotoStatement,
    cSharp_ContinueStatement,
    cSharp_BreakStatement,
    cSharp_GeneralCatchclause,
    cSharp_SpecificCatchClause,
    cSharp_FinallyClause,
    cSharp_CatchClauses,
    cSharp_ThrowStatement,
    cSharp_ReturnStatement,
    cSharp_ResourceAquisition,
    cSharp_UsingStatement,
    cSharp_LockStatement,
    cSharp_Block,
    cSharp_StatementExpression,
    cSharp_LocalconstantDeclaration,
    cSharp_EmbeddedStatement,
    cSharp_DeclarationStatment,
    cSharp_LabeledStatement,
    cSharp_Statement,
    cSharp_TryStatement,
    cSharp_JumpStatement,
    cSharp_IterationStatement,
    cSharp_SelectionStatement,
    DelegateDeclaration,
    cSharp_FixedParameter,
    FormalParameterList,
    cSharp_FixedParameters,
    cSharp_MethodHeader,
    cSharp_SetAccessorDeclaration,
    cSharp_GetAccessorDeclaration,
    cSharp_RemoveAccessorDeclaration,
    cSharp_AddAccessorDeclaration,
    cSharp_NamespaceBody,
    cSharp_VariableInitializer,
    cSharp_PrimaryExpression2,
    cSharp_TypeOrVoid,
    cSharp_ArgumentList,
    cSharp_VariableDeclarator,
    ConstantDeclaration,
    FieldDeclaration,
    PropertyDeclaration,
    EventDeclaration,
    cSharp_Type,
    cSharp_BuiltInType,
    cSharp_NonArrayType,
    cSharp_PrimaryExpression,
    cSharp_Expression2,
    cSharp_UnaryExpression,
    ResourceAquisition,
    cSharp_LocalVariableDeclaration,
    Argument,
    VariableInitializer,
    cSharp_ArrayInitializer,
    cSharp_Expression,
    cSharp_ExpressionList,
    cSharp_AttributeArguments,
    cSharp_AttributeName,
    cSharp_GlobalAttributeSection,
    cSharp_ArrayType,
    cSharp_QualifiedIdentifier,
    cSharp_Identifier,
    cSharp_NamespaceMemberDeclaration,
    cSharp_GlobalAttributes,
    cSharp_UsingDirective,
    cSharp_CompilationUnit,
    cSharp_Attribute,
    AttributeSection,
    cSharp_AttributeSection,
    cSharp_Attributes,
    cSharp_AttributeList,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typeorvoid_is_not_abstract():
    assert not inspect.isabstract(TypeOrVoid)


def test_typeorvoid_constructor_exists():
    assert callable(TypeOrVoid.__init__)


def test_typeorvoid_constructor_args():
    sig = inspect.signature(TypeOrVoid.__init__)
    params = list(sig.parameters.keys())



def test_csharp_void_is_not_abstract():
    assert not inspect.isabstract(cSharp_Void)


def test_csharp_void_constructor_exists():
    assert callable(cSharp_Void.__init__)


def test_csharp_void_constructor_args():
    sig = inspect.signature(cSharp_Void.__init__)
    params = list(sig.parameters.keys())



def test_csharp_parameterarray_is_not_abstract():
    assert not inspect.isabstract(cSharp_ParameterArray)


def test_csharp_parameterarray_constructor_exists():
    assert callable(cSharp_ParameterArray.__init__)


def test_csharp_parameterarray_constructor_args():
    sig = inspect.signature(cSharp_ParameterArray.__init__)
    params = list(sig.parameters.keys())



def test_operatordeclarator_is_not_abstract():
    assert not inspect.isabstract(OperatorDeclarator)


def test_operatordeclarator_constructor_exists():
    assert callable(OperatorDeclarator.__init__)


def test_operatordeclarator_constructor_args():
    sig = inspect.signature(OperatorDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp_unaryoperatordeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp_UnaryOperatorDeclarator)


def test_csharp_unaryoperatordeclarator_constructor_exists():
    assert callable(cSharp_UnaryOperatorDeclarator.__init__)


def test_csharp_unaryoperatordeclarator_constructor_args():
    sig = inspect.signature(cSharp_UnaryOperatorDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp_binaryoperatordeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp_BinaryOperatorDeclarator)


def test_csharp_binaryoperatordeclarator_constructor_exists():
    assert callable(cSharp_BinaryOperatorDeclarator.__init__)


def test_csharp_binaryoperatordeclarator_constructor_args():
    sig = inspect.signature(cSharp_BinaryOperatorDeclarator.__init__)
    params = list(sig.parameters.keys())
    assert "overBinOperator" in params, "Missing parameter 'overBinOperator'"

def test_csharp_binaryoperatordeclarator_has_overBinOperator():
    assert hasattr(cSharp_BinaryOperatorDeclarator, "overBinOperator")
    descriptor = None
    for klass in cSharp_BinaryOperatorDeclarator.__mro__:
        if "overBinOperator" in klass.__dict__:
            descriptor = klass.__dict__["overBinOperator"]
            break
    assert isinstance(descriptor, property)



def test_csharp_conversionoperatordeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp_ConversionOperatorDeclarator)


def test_csharp_conversionoperatordeclarator_constructor_exists():
    assert callable(cSharp_ConversionOperatorDeclarator.__init__)


def test_csharp_conversionoperatordeclarator_constructor_args():
    sig = inspect.signature(cSharp_ConversionOperatorDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp_operatordeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp_OperatorDeclarator)


def test_csharp_operatordeclarator_constructor_exists():
    assert callable(cSharp_OperatorDeclarator.__init__)


def test_csharp_operatordeclarator_constructor_args():
    sig = inspect.signature(cSharp_OperatorDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp_indexerdeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp_IndexerDeclarator)


def test_csharp_indexerdeclarator_constructor_exists():
    assert callable(cSharp_IndexerDeclarator.__init__)


def test_csharp_indexerdeclarator_constructor_args():
    sig = inspect.signature(cSharp_IndexerDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp_constructordeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp_ConstructorDeclarator)


def test_csharp_constructordeclarator_constructor_exists():
    assert callable(cSharp_ConstructorDeclarator.__init__)


def test_csharp_constructordeclarator_constructor_args():
    sig = inspect.signature(cSharp_ConstructorDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp_staticconstructordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_StaticConstructorDeclaration)


def test_csharp_staticconstructordeclaration_constructor_exists():
    assert callable(cSharp_StaticConstructorDeclaration.__init__)


def test_csharp_staticconstructordeclaration_constructor_args():
    sig = inspect.signature(cSharp_StaticConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "staticCosntModifier" in params, "Missing parameter 'staticCosntModifier'"

def test_csharp_staticconstructordeclaration_has_staticCosntModifier():
    assert hasattr(cSharp_StaticConstructorDeclaration, "staticCosntModifier")
    descriptor = None
    for klass in cSharp_StaticConstructorDeclaration.__mro__:
        if "staticCosntModifier" in klass.__dict__:
            descriptor = klass.__dict__["staticCosntModifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp_destructordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_DestructorDeclaration)


def test_csharp_destructordeclaration_constructor_exists():
    assert callable(cSharp_DestructorDeclaration.__init__)


def test_csharp_destructordeclaration_constructor_args():
    sig = inspect.signature(cSharp_DestructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_ConstructorDeclaration)


def test_csharp_constructordeclaration_constructor_exists():
    assert callable(cSharp_ConstructorDeclaration.__init__)


def test_csharp_constructordeclaration_constructor_args():
    sig = inspect.signature(cSharp_ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constModifier" in params, "Missing parameter 'constModifier'"

def test_csharp_constructordeclaration_has_constModifier():
    assert hasattr(cSharp_ConstructorDeclaration, "constModifier")
    descriptor = None
    for klass in cSharp_ConstructorDeclaration.__mro__:
        if "constModifier" in klass.__dict__:
            descriptor = klass.__dict__["constModifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp_operatordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_OperatorDeclaration)


def test_csharp_operatordeclaration_constructor_exists():
    assert callable(cSharp_OperatorDeclaration.__init__)


def test_csharp_operatordeclaration_constructor_args():
    sig = inspect.signature(cSharp_OperatorDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "opModifier" in params, "Missing parameter 'opModifier'"

def test_csharp_operatordeclaration_has_opModifier():
    assert hasattr(cSharp_OperatorDeclaration, "opModifier")
    descriptor = None
    for klass in cSharp_OperatorDeclaration.__mro__:
        if "opModifier" in klass.__dict__:
            descriptor = klass.__dict__["opModifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp_indexerdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_IndexerDeclaration)


def test_csharp_indexerdeclaration_constructor_exists():
    assert callable(cSharp_IndexerDeclaration.__init__)


def test_csharp_indexerdeclaration_constructor_args():
    sig = inspect.signature(cSharp_IndexerDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "idModifier" in params, "Missing parameter 'idModifier'"

def test_csharp_indexerdeclaration_has_idModifier():
    assert hasattr(cSharp_IndexerDeclaration, "idModifier")
    descriptor = None
    for klass in cSharp_IndexerDeclaration.__mro__:
        if "idModifier" in klass.__dict__:
            descriptor = klass.__dict__["idModifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp_eventdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_EventDeclaration)


def test_csharp_eventdeclaration_constructor_exists():
    assert callable(cSharp_EventDeclaration.__init__)


def test_csharp_eventdeclaration_constructor_args():
    sig = inspect.signature(cSharp_EventDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_propertydeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_PropertyDeclaration)


def test_csharp_propertydeclaration_constructor_exists():
    assert callable(cSharp_PropertyDeclaration.__init__)


def test_csharp_propertydeclaration_constructor_args():
    sig = inspect.signature(cSharp_PropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_ConstantDeclaration)


def test_csharp_constantdeclaration_constructor_exists():
    assert callable(cSharp_ConstantDeclaration.__init__)


def test_csharp_constantdeclaration_constructor_args():
    sig = inspect.signature(cSharp_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_MethodDeclaration)


def test_csharp_methoddeclaration_constructor_exists():
    assert callable(cSharp_MethodDeclaration.__init__)


def test_csharp_methoddeclaration_constructor_args():
    sig = inspect.signature(cSharp_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_FieldDeclaration)


def test_csharp_fielddeclaration_constructor_exists():
    assert callable(cSharp_FieldDeclaration.__init__)


def test_csharp_fielddeclaration_constructor_args():
    sig = inspect.signature(cSharp_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_argument_is_not_abstract():
    assert not inspect.isabstract(cSharp_Argument)


def test_csharp_argument_constructor_exists():
    assert callable(cSharp_Argument.__init__)


def test_csharp_argument_constructor_args():
    sig = inspect.signature(cSharp_Argument.__init__)
    params = list(sig.parameters.keys())



def test_constructorinitializer_is_not_abstract():
    assert not inspect.isabstract(ConstructorInitializer)


def test_constructorinitializer_constructor_exists():
    assert callable(ConstructorInitializer.__init__)


def test_constructorinitializer_constructor_args():
    sig = inspect.signature(ConstructorInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp_constructorinitializer_is_not_abstract():
    assert not inspect.isabstract(cSharp_ConstructorInitializer)


def test_csharp_constructorinitializer_constructor_exists():
    assert callable(cSharp_ConstructorInitializer.__init__)


def test_csharp_constructorinitializer_constructor_args():
    sig = inspect.signature(cSharp_ConstructorInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp_interfaceaccessors_is_not_abstract():
    assert not inspect.isabstract(cSharp_InterfaceAccessors)


def test_csharp_interfaceaccessors_constructor_exists():
    assert callable(cSharp_InterfaceAccessors.__init__)


def test_csharp_interfaceaccessors_constructor_args():
    sig = inspect.signature(cSharp_InterfaceAccessors.__init__)
    params = list(sig.parameters.keys())



def test_csharp_classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_ClassMemberDeclaration)


def test_csharp_classmemberdeclaration_constructor_exists():
    assert callable(cSharp_ClassMemberDeclaration.__init__)


def test_csharp_classmemberdeclaration_constructor_args():
    sig = inspect.signature(cSharp_ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_classbody_is_not_abstract():
    assert not inspect.isabstract(cSharp_ClassBody)


def test_csharp_classbody_constructor_exists():
    assert callable(cSharp_ClassBody.__init__)


def test_csharp_classbody_constructor_args():
    sig = inspect.signature(cSharp_ClassBody.__init__)
    params = list(sig.parameters.keys())



def test_csharp_classbase_is_not_abstract():
    assert not inspect.isabstract(cSharp_ClassBase)


def test_csharp_classbase_constructor_exists():
    assert callable(cSharp_ClassBase.__init__)


def test_csharp_classbase_constructor_args():
    sig = inspect.signature(cSharp_ClassBase.__init__)
    params = list(sig.parameters.keys())



def test_csharp_interfaceeventdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_InterfaceEventDeclaration)


def test_csharp_interfaceeventdeclaration_constructor_exists():
    assert callable(cSharp_InterfaceEventDeclaration.__init__)


def test_csharp_interfaceeventdeclaration_constructor_args():
    sig = inspect.signature(cSharp_InterfaceEventDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_interfacemethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_InterfaceMethodDeclaration)


def test_csharp_interfacemethoddeclaration_constructor_exists():
    assert callable(cSharp_InterfaceMethodDeclaration.__init__)


def test_csharp_interfacemethoddeclaration_constructor_args():
    sig = inspect.signature(cSharp_InterfaceMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_interfacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_InterfaceMemberDeclaration)


def test_csharp_interfacememberdeclaration_constructor_exists():
    assert callable(cSharp_InterfaceMemberDeclaration.__init__)


def test_csharp_interfacememberdeclaration_constructor_args():
    sig = inspect.signature(cSharp_InterfaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_interfacebody_is_not_abstract():
    assert not inspect.isabstract(cSharp_InterfaceBody)


def test_csharp_interfacebody_constructor_exists():
    assert callable(cSharp_InterfaceBody.__init__)


def test_csharp_interfacebody_constructor_args():
    sig = inspect.signature(cSharp_InterfaceBody.__init__)
    params = list(sig.parameters.keys())



def test_csharp_enummemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_EnumMemberDeclaration)


def test_csharp_enummemberdeclaration_constructor_exists():
    assert callable(cSharp_EnumMemberDeclaration.__init__)


def test_csharp_enummemberdeclaration_constructor_args():
    sig = inspect.signature(cSharp_EnumMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_enumbody_is_not_abstract():
    assert not inspect.isabstract(cSharp_EnumBody)


def test_csharp_enumbody_constructor_exists():
    assert callable(cSharp_EnumBody.__init__)


def test_csharp_enumbody_constructor_args():
    sig = inspect.signature(cSharp_EnumBody.__init__)
    params = list(sig.parameters.keys())



def test_csharp_delegatedeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_DelegateDeclaration)


def test_csharp_delegatedeclaration_constructor_exists():
    assert callable(cSharp_DelegateDeclaration.__init__)


def test_csharp_delegatedeclaration_constructor_args():
    sig = inspect.signature(cSharp_DelegateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_EnumDeclaration)


def test_csharp_enumdeclaration_constructor_exists():
    assert callable(cSharp_EnumDeclaration.__init__)


def test_csharp_enumdeclaration_constructor_args():
    sig = inspect.signature(cSharp_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_InterfaceDeclaration)


def test_csharp_interfacedeclaration_constructor_exists():
    assert callable(cSharp_InterfaceDeclaration.__init__)


def test_csharp_interfacedeclaration_constructor_args():
    sig = inspect.signature(cSharp_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(cSharp_FormalParameterList)


def test_csharp_formalparameterlist_constructor_exists():
    assert callable(cSharp_FormalParameterList.__init__)


def test_csharp_formalparameterlist_constructor_args():
    sig = inspect.signature(cSharp_FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_csharp_interfacepropertydeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_InterfacePropertyDeclaration)


def test_csharp_interfacepropertydeclaration_constructor_exists():
    assert callable(cSharp_InterfacePropertyDeclaration.__init__)


def test_csharp_interfacepropertydeclaration_constructor_args():
    sig = inspect.signature(cSharp_InterfacePropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_interfaceindexerdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_InterfaceIndexerDeclaration)


def test_csharp_interfaceindexerdeclaration_constructor_exists():
    assert callable(cSharp_InterfaceIndexerDeclaration.__init__)


def test_csharp_interfaceindexerdeclaration_constructor_args():
    sig = inspect.signature(cSharp_InterfaceIndexerDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_TypeDeclaration)


def test_csharp_typedeclaration_constructor_exists():
    assert callable(cSharp_TypeDeclaration.__init__)


def test_csharp_typedeclaration_constructor_args():
    sig = inspect.signature(cSharp_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_namespacedeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_NamespaceDeclaration)


def test_csharp_namespacedeclaration_constructor_exists():
    assert callable(cSharp_NamespaceDeclaration.__init__)


def test_csharp_namespacedeclaration_constructor_args():
    sig = inspect.signature(cSharp_NamespaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_qualifiedidentifierlist_is_not_abstract():
    assert not inspect.isabstract(cSharp_QualifiedIdentifierList)


def test_csharp_qualifiedidentifierlist_constructor_exists():
    assert callable(cSharp_QualifiedIdentifierList.__init__)


def test_csharp_qualifiedidentifierlist_constructor_args():
    sig = inspect.signature(cSharp_QualifiedIdentifierList.__init__)
    params = list(sig.parameters.keys())



def test_classbase_is_not_abstract():
    assert not inspect.isabstract(ClassBase)


def test_classbase_constructor_exists():
    assert callable(ClassBase.__init__)


def test_classbase_constructor_args():
    sig = inspect.signature(ClassBase.__init__)
    params = list(sig.parameters.keys())



def test_arraytype_is_not_abstract():
    assert not inspect.isabstract(ArrayType)


def test_arraytype_constructor_exists():
    assert callable(ArrayType.__init__)


def test_arraytype_constructor_args():
    sig = inspect.signature(ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_builtintype_is_not_abstract():
    assert not inspect.isabstract(BuiltInType)


def test_builtintype_constructor_exists():
    assert callable(BuiltInType.__init__)


def test_builtintype_constructor_args():
    sig = inspect.signature(BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_csharp_builtinclasstype_is_not_abstract():
    assert not inspect.isabstract(cSharp_BuiltInClassType)


def test_csharp_builtinclasstype_constructor_exists():
    assert callable(cSharp_BuiltInClassType.__init__)


def test_csharp_builtinclasstype_constructor_args():
    sig = inspect.signature(cSharp_BuiltInClassType.__init__)
    params = list(sig.parameters.keys())



def test_csharp_integraltype_is_not_abstract():
    assert not inspect.isabstract(cSharp_IntegralType)


def test_csharp_integraltype_constructor_exists():
    assert callable(cSharp_IntegralType.__init__)


def test_csharp_integraltype_constructor_args():
    sig = inspect.signature(cSharp_IntegralType.__init__)
    params = list(sig.parameters.keys())



def test_csharp_constantdeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp_ConstantDeclarator)


def test_csharp_constantdeclarator_constructor_exists():
    assert callable(cSharp_ConstantDeclarator.__init__)


def test_csharp_constantdeclarator_constructor_args():
    sig = inspect.signature(cSharp_ConstantDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp_accessordeclarations_is_not_abstract():
    assert not inspect.isabstract(cSharp_AccessorDeclarations)


def test_csharp_accessordeclarations_constructor_exists():
    assert callable(cSharp_AccessorDeclarations.__init__)


def test_csharp_accessordeclarations_constructor_args():
    sig = inspect.signature(cSharp_AccessorDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_csharp_eventaccessordeclarations_is_not_abstract():
    assert not inspect.isabstract(cSharp_EventAccessorDeclarations)


def test_csharp_eventaccessordeclarations_constructor_exists():
    assert callable(cSharp_EventAccessorDeclarations.__init__)


def test_csharp_eventaccessordeclarations_constructor_args():
    sig = inspect.signature(cSharp_EventAccessorDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_csharp_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_ClassDeclaration)


def test_csharp_classdeclaration_constructor_exists():
    assert callable(cSharp_ClassDeclaration.__init__)


def test_csharp_classdeclaration_constructor_args():
    sig = inspect.signature(cSharp_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "classModifier" in params, "Missing parameter 'classModifier'"

def test_csharp_classdeclaration_has_classModifier():
    assert hasattr(cSharp_ClassDeclaration, "classModifier")
    descriptor = None
    for klass in cSharp_ClassDeclaration.__mro__:
        if "classModifier" in klass.__dict__:
            descriptor = klass.__dict__["classModifier"]
            break
    assert isinstance(descriptor, property)



def test_builtinclasstype_is_not_abstract():
    assert not inspect.isabstract(BuiltInClassType)


def test_builtinclasstype_constructor_exists():
    assert callable(BuiltInClassType.__init__)


def test_builtinclasstype_constructor_args():
    sig = inspect.signature(BuiltInClassType.__init__)
    params = list(sig.parameters.keys())



def test_csharp_string_is_not_abstract():
    assert not inspect.isabstract(cSharp_String)


def test_csharp_string_constructor_exists():
    assert callable(cSharp_String.__init__)


def test_csharp_string_constructor_args():
    sig = inspect.signature(cSharp_String.__init__)
    params = list(sig.parameters.keys())



def test_csharp_object_is_not_abstract():
    assert not inspect.isabstract(cSharp_Object)


def test_csharp_object_constructor_exists():
    assert callable(cSharp_Object.__init__)


def test_csharp_object_constructor_args():
    sig = inspect.signature(cSharp_Object.__init__)
    params = list(sig.parameters.keys())



def test_csharp_double_is_not_abstract():
    assert not inspect.isabstract(cSharp_Double)


def test_csharp_double_constructor_exists():
    assert callable(cSharp_Double.__init__)


def test_csharp_double_constructor_args():
    sig = inspect.signature(cSharp_Double.__init__)
    params = list(sig.parameters.keys())



def test_csharp_float_is_not_abstract():
    assert not inspect.isabstract(cSharp_Float)


def test_csharp_float_constructor_exists():
    assert callable(cSharp_Float.__init__)


def test_csharp_float_constructor_args():
    sig = inspect.signature(cSharp_Float.__init__)
    params = list(sig.parameters.keys())



def test_csharp_decimal_is_not_abstract():
    assert not inspect.isabstract(cSharp_Decimal)


def test_csharp_decimal_constructor_exists():
    assert callable(cSharp_Decimal.__init__)


def test_csharp_decimal_constructor_args():
    sig = inspect.signature(cSharp_Decimal.__init__)
    params = list(sig.parameters.keys())



def test_csharp_bool_is_not_abstract():
    assert not inspect.isabstract(cSharp_Bool)


def test_csharp_bool_constructor_exists():
    assert callable(cSharp_Bool.__init__)


def test_csharp_bool_constructor_args():
    sig = inspect.signature(cSharp_Bool.__init__)
    params = list(sig.parameters.keys())



def test_integraltype_is_not_abstract():
    assert not inspect.isabstract(IntegralType)


def test_integraltype_constructor_exists():
    assert callable(IntegralType.__init__)


def test_integraltype_constructor_args():
    sig = inspect.signature(IntegralType.__init__)
    params = list(sig.parameters.keys())



def test_csharp_char_is_not_abstract():
    assert not inspect.isabstract(cSharp_Char)


def test_csharp_char_constructor_exists():
    assert callable(cSharp_Char.__init__)


def test_csharp_char_constructor_args():
    sig = inspect.signature(cSharp_Char.__init__)
    params = list(sig.parameters.keys())



def test_csharp_short_is_not_abstract():
    assert not inspect.isabstract(cSharp_Short)


def test_csharp_short_constructor_exists():
    assert callable(cSharp_Short.__init__)


def test_csharp_short_constructor_args():
    sig = inspect.signature(cSharp_Short.__init__)
    params = list(sig.parameters.keys())



def test_csharp_long_is_not_abstract():
    assert not inspect.isabstract(cSharp_Long)


def test_csharp_long_constructor_exists():
    assert callable(cSharp_Long.__init__)


def test_csharp_long_constructor_args():
    sig = inspect.signature(cSharp_Long.__init__)
    params = list(sig.parameters.keys())



def test_csharp_ulong_is_not_abstract():
    assert not inspect.isabstract(cSharp_ULong)


def test_csharp_ulong_constructor_exists():
    assert callable(cSharp_ULong.__init__)


def test_csharp_ulong_constructor_args():
    sig = inspect.signature(cSharp_ULong.__init__)
    params = list(sig.parameters.keys())



def test_csharp_byte_is_not_abstract():
    assert not inspect.isabstract(cSharp_Byte)


def test_csharp_byte_constructor_exists():
    assert callable(cSharp_Byte.__init__)


def test_csharp_byte_constructor_args():
    sig = inspect.signature(cSharp_Byte.__init__)
    params = list(sig.parameters.keys())



def test_csharp_ushort_is_not_abstract():
    assert not inspect.isabstract(cSharp_UShort)


def test_csharp_ushort_constructor_exists():
    assert callable(cSharp_UShort.__init__)


def test_csharp_ushort_constructor_args():
    sig = inspect.signature(cSharp_UShort.__init__)
    params = list(sig.parameters.keys())



def test_csharp_uint_is_not_abstract():
    assert not inspect.isabstract(cSharp_UInt)


def test_csharp_uint_constructor_exists():
    assert callable(cSharp_UInt.__init__)


def test_csharp_uint_constructor_args():
    sig = inspect.signature(cSharp_UInt.__init__)
    params = list(sig.parameters.keys())



def test_csharp_int_is_not_abstract():
    assert not inspect.isabstract(cSharp_Int)


def test_csharp_int_constructor_exists():
    assert callable(cSharp_Int.__init__)


def test_csharp_int_constructor_args():
    sig = inspect.signature(cSharp_Int.__init__)
    params = list(sig.parameters.keys())



def test_csharp_sbyte_is_not_abstract():
    assert not inspect.isabstract(cSharp_SByte)


def test_csharp_sbyte_constructor_exists():
    assert callable(cSharp_SByte.__init__)


def test_csharp_sbyte_constructor_args():
    sig = inspect.signature(cSharp_SByte.__init__)
    params = list(sig.parameters.keys())



def test_getaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(GetAccessorDeclaration)


def test_getaccessordeclaration_constructor_exists():
    assert callable(GetAccessorDeclaration.__init__)


def test_getaccessordeclaration_constructor_args():
    sig = inspect.signature(GetAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_setaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(SetAccessorDeclaration)


def test_setaccessordeclaration_constructor_exists():
    assert callable(SetAccessorDeclaration.__init__)


def test_setaccessordeclaration_constructor_args():
    sig = inspect.signature(SetAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_maybeemptyblock_is_not_abstract():
    assert not inspect.isabstract(cSharp_MaybeEmptyBlock)


def test_csharp_maybeemptyblock_constructor_exists():
    assert callable(cSharp_MaybeEmptyBlock.__init__)


def test_csharp_maybeemptyblock_constructor_args():
    sig = inspect.signature(cSharp_MaybeEmptyBlock.__init__)
    params = list(sig.parameters.keys())



def test_maybeemptyblock_is_not_abstract():
    assert not inspect.isabstract(MaybeEmptyBlock)


def test_maybeemptyblock_constructor_exists():
    assert callable(MaybeEmptyBlock.__init__)


def test_maybeemptyblock_constructor_args():
    sig = inspect.signature(MaybeEmptyBlock.__init__)
    params = list(sig.parameters.keys())



def test_addaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(AddAccessorDeclaration)


def test_addaccessordeclaration_constructor_exists():
    assert callable(AddAccessorDeclaration.__init__)


def test_addaccessordeclaration_constructor_args():
    sig = inspect.signature(AddAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_removeaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(RemoveAccessorDeclaration)


def test_removeaccessordeclaration_constructor_exists():
    assert callable(RemoveAccessorDeclaration.__init__)


def test_removeaccessordeclaration_constructor_args():
    sig = inspect.signature(RemoveAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_elsepart_is_not_abstract():
    assert not inspect.isabstract(cSharp_ElsePart)


def test_csharp_elsepart_constructor_exists():
    assert callable(cSharp_ElsePart.__init__)


def test_csharp_elsepart_constructor_args():
    sig = inspect.signature(cSharp_ElsePart.__init__)
    params = list(sig.parameters.keys())



def test_csharp_switchlabel_is_not_abstract():
    assert not inspect.isabstract(cSharp_SwitchLabel)


def test_csharp_switchlabel_constructor_exists():
    assert callable(cSharp_SwitchLabel.__init__)


def test_csharp_switchlabel_constructor_args():
    sig = inspect.signature(cSharp_SwitchLabel.__init__)
    params = list(sig.parameters.keys())



def test_csharp_switchsection_is_not_abstract():
    assert not inspect.isabstract(cSharp_SwitchSection)


def test_csharp_switchsection_constructor_exists():
    assert callable(cSharp_SwitchSection.__init__)


def test_csharp_switchsection_constructor_args():
    sig = inspect.signature(cSharp_SwitchSection.__init__)
    params = list(sig.parameters.keys())



def test_csharp_switchstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_SwitchStatement)


def test_csharp_switchstatement_constructor_exists():
    assert callable(cSharp_SwitchStatement.__init__)


def test_csharp_switchstatement_constructor_args():
    sig = inspect.signature(cSharp_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_ifstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_IfStatement)


def test_csharp_ifstatement_constructor_exists():
    assert callable(cSharp_IfStatement.__init__)


def test_csharp_ifstatement_constructor_args():
    sig = inspect.signature(cSharp_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_statementexpressionlist_is_not_abstract():
    assert not inspect.isabstract(cSharp_StatementExpressionList)


def test_csharp_statementexpressionlist_constructor_exists():
    assert callable(cSharp_StatementExpressionList.__init__)


def test_csharp_statementexpressionlist_constructor_args():
    sig = inspect.signature(cSharp_StatementExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_csharp_forinitializer_is_not_abstract():
    assert not inspect.isabstract(cSharp_ForInitializer)


def test_csharp_forinitializer_constructor_exists():
    assert callable(cSharp_ForInitializer.__init__)


def test_csharp_forinitializer_constructor_args():
    sig = inspect.signature(cSharp_ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp_foreachstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_ForeachStatement)


def test_csharp_foreachstatement_constructor_exists():
    assert callable(cSharp_ForeachStatement.__init__)


def test_csharp_foreachstatement_constructor_args():
    sig = inspect.signature(cSharp_ForeachStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_forstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_ForStatement)


def test_csharp_forstatement_constructor_exists():
    assert callable(cSharp_ForStatement.__init__)


def test_csharp_forstatement_constructor_args():
    sig = inspect.signature(cSharp_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_dostatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_DoStatement)


def test_csharp_dostatement_constructor_exists():
    assert callable(cSharp_DoStatement.__init__)


def test_csharp_dostatement_constructor_args():
    sig = inspect.signature(cSharp_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_whilestatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_WhileStatement)


def test_csharp_whilestatement_constructor_exists():
    assert callable(cSharp_WhileStatement.__init__)


def test_csharp_whilestatement_constructor_args():
    sig = inspect.signature(cSharp_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_gotostatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_GotoStatement)


def test_csharp_gotostatement_constructor_exists():
    assert callable(cSharp_GotoStatement.__init__)


def test_csharp_gotostatement_constructor_args():
    sig = inspect.signature(cSharp_GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_continuestatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_ContinueStatement)


def test_csharp_continuestatement_constructor_exists():
    assert callable(cSharp_ContinueStatement.__init__)


def test_csharp_continuestatement_constructor_args():
    sig = inspect.signature(cSharp_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_breakstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_BreakStatement)


def test_csharp_breakstatement_constructor_exists():
    assert callable(cSharp_BreakStatement.__init__)


def test_csharp_breakstatement_constructor_args():
    sig = inspect.signature(cSharp_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_generalcatchclause_is_not_abstract():
    assert not inspect.isabstract(cSharp_GeneralCatchclause)


def test_csharp_generalcatchclause_constructor_exists():
    assert callable(cSharp_GeneralCatchclause.__init__)


def test_csharp_generalcatchclause_constructor_args():
    sig = inspect.signature(cSharp_GeneralCatchclause.__init__)
    params = list(sig.parameters.keys())



def test_csharp_specificcatchclause_is_not_abstract():
    assert not inspect.isabstract(cSharp_SpecificCatchClause)


def test_csharp_specificcatchclause_constructor_exists():
    assert callable(cSharp_SpecificCatchClause.__init__)


def test_csharp_specificcatchclause_constructor_args():
    sig = inspect.signature(cSharp_SpecificCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_csharp_finallyclause_is_not_abstract():
    assert not inspect.isabstract(cSharp_FinallyClause)


def test_csharp_finallyclause_constructor_exists():
    assert callable(cSharp_FinallyClause.__init__)


def test_csharp_finallyclause_constructor_args():
    sig = inspect.signature(cSharp_FinallyClause.__init__)
    params = list(sig.parameters.keys())



def test_csharp_catchclauses_is_not_abstract():
    assert not inspect.isabstract(cSharp_CatchClauses)


def test_csharp_catchclauses_constructor_exists():
    assert callable(cSharp_CatchClauses.__init__)


def test_csharp_catchclauses_constructor_args():
    sig = inspect.signature(cSharp_CatchClauses.__init__)
    params = list(sig.parameters.keys())



def test_csharp_throwstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_ThrowStatement)


def test_csharp_throwstatement_constructor_exists():
    assert callable(cSharp_ThrowStatement.__init__)


def test_csharp_throwstatement_constructor_args():
    sig = inspect.signature(cSharp_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_returnstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_ReturnStatement)


def test_csharp_returnstatement_constructor_exists():
    assert callable(cSharp_ReturnStatement.__init__)


def test_csharp_returnstatement_constructor_args():
    sig = inspect.signature(cSharp_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_resourceaquisition_is_not_abstract():
    assert not inspect.isabstract(cSharp_ResourceAquisition)


def test_csharp_resourceaquisition_constructor_exists():
    assert callable(cSharp_ResourceAquisition.__init__)


def test_csharp_resourceaquisition_constructor_args():
    sig = inspect.signature(cSharp_ResourceAquisition.__init__)
    params = list(sig.parameters.keys())



def test_csharp_usingstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_UsingStatement)


def test_csharp_usingstatement_constructor_exists():
    assert callable(cSharp_UsingStatement.__init__)


def test_csharp_usingstatement_constructor_args():
    sig = inspect.signature(cSharp_UsingStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_lockstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_LockStatement)


def test_csharp_lockstatement_constructor_exists():
    assert callable(cSharp_LockStatement.__init__)


def test_csharp_lockstatement_constructor_args():
    sig = inspect.signature(cSharp_LockStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_block_is_not_abstract():
    assert not inspect.isabstract(cSharp_Block)


def test_csharp_block_constructor_exists():
    assert callable(cSharp_Block.__init__)


def test_csharp_block_constructor_args():
    sig = inspect.signature(cSharp_Block.__init__)
    params = list(sig.parameters.keys())



def test_csharp_statementexpression_is_not_abstract():
    assert not inspect.isabstract(cSharp_StatementExpression)


def test_csharp_statementexpression_constructor_exists():
    assert callable(cSharp_StatementExpression.__init__)


def test_csharp_statementexpression_constructor_args():
    sig = inspect.signature(cSharp_StatementExpression.__init__)
    params = list(sig.parameters.keys())
    assert "incrimentDecrement" in params, "Missing parameter 'incrimentDecrement'"
    assert "assignementOperator" in params, "Missing parameter 'assignementOperator'"

def test_csharp_statementexpression_has_incrimentDecrement():
    assert hasattr(cSharp_StatementExpression, "incrimentDecrement")
    descriptor = None
    for klass in cSharp_StatementExpression.__mro__:
        if "incrimentDecrement" in klass.__dict__:
            descriptor = klass.__dict__["incrimentDecrement"]
            break
    assert isinstance(descriptor, property)

def test_csharp_statementexpression_has_assignementOperator():
    assert hasattr(cSharp_StatementExpression, "assignementOperator")
    descriptor = None
    for klass in cSharp_StatementExpression.__mro__:
        if "assignementOperator" in klass.__dict__:
            descriptor = klass.__dict__["assignementOperator"]
            break
    assert isinstance(descriptor, property)



def test_csharp_localconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_LocalconstantDeclaration)


def test_csharp_localconstantdeclaration_constructor_exists():
    assert callable(cSharp_LocalconstantDeclaration.__init__)


def test_csharp_localconstantdeclaration_constructor_args():
    sig = inspect.signature(cSharp_LocalconstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_embeddedstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_EmbeddedStatement)


def test_csharp_embeddedstatement_constructor_exists():
    assert callable(cSharp_EmbeddedStatement.__init__)


def test_csharp_embeddedstatement_constructor_args():
    sig = inspect.signature(cSharp_EmbeddedStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_declarationstatment_is_not_abstract():
    assert not inspect.isabstract(cSharp_DeclarationStatment)


def test_csharp_declarationstatment_constructor_exists():
    assert callable(cSharp_DeclarationStatment.__init__)


def test_csharp_declarationstatment_constructor_args():
    sig = inspect.signature(cSharp_DeclarationStatment.__init__)
    params = list(sig.parameters.keys())



def test_csharp_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_LabeledStatement)


def test_csharp_labeledstatement_constructor_exists():
    assert callable(cSharp_LabeledStatement.__init__)


def test_csharp_labeledstatement_constructor_args():
    sig = inspect.signature(cSharp_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_statement_is_not_abstract():
    assert not inspect.isabstract(cSharp_Statement)


def test_csharp_statement_constructor_exists():
    assert callable(cSharp_Statement.__init__)


def test_csharp_statement_constructor_args():
    sig = inspect.signature(cSharp_Statement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_trystatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_TryStatement)


def test_csharp_trystatement_constructor_exists():
    assert callable(cSharp_TryStatement.__init__)


def test_csharp_trystatement_constructor_args():
    sig = inspect.signature(cSharp_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_JumpStatement)


def test_csharp_jumpstatement_constructor_exists():
    assert callable(cSharp_JumpStatement.__init__)


def test_csharp_jumpstatement_constructor_args():
    sig = inspect.signature(cSharp_JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_iterationstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_IterationStatement)


def test_csharp_iterationstatement_constructor_exists():
    assert callable(cSharp_IterationStatement.__init__)


def test_csharp_iterationstatement_constructor_args():
    sig = inspect.signature(cSharp_IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp_selectionstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp_SelectionStatement)


def test_csharp_selectionstatement_constructor_exists():
    assert callable(cSharp_SelectionStatement.__init__)


def test_csharp_selectionstatement_constructor_args():
    sig = inspect.signature(cSharp_SelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_delegatedeclaration_is_not_abstract():
    assert not inspect.isabstract(DelegateDeclaration)


def test_delegatedeclaration_constructor_exists():
    assert callable(DelegateDeclaration.__init__)


def test_delegatedeclaration_constructor_args():
    sig = inspect.signature(DelegateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_fixedparameter_is_not_abstract():
    assert not inspect.isabstract(cSharp_FixedParameter)


def test_csharp_fixedparameter_constructor_exists():
    assert callable(cSharp_FixedParameter.__init__)


def test_csharp_fixedparameter_constructor_args():
    sig = inspect.signature(cSharp_FixedParameter.__init__)
    params = list(sig.parameters.keys())



def test_formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(FormalParameterList)


def test_formalparameterlist_constructor_exists():
    assert callable(FormalParameterList.__init__)


def test_formalparameterlist_constructor_args():
    sig = inspect.signature(FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_csharp_fixedparameters_is_not_abstract():
    assert not inspect.isabstract(cSharp_FixedParameters)


def test_csharp_fixedparameters_constructor_exists():
    assert callable(cSharp_FixedParameters.__init__)


def test_csharp_fixedparameters_constructor_args():
    sig = inspect.signature(cSharp_FixedParameters.__init__)
    params = list(sig.parameters.keys())



def test_csharp_methodheader_is_not_abstract():
    assert not inspect.isabstract(cSharp_MethodHeader)


def test_csharp_methodheader_constructor_exists():
    assert callable(cSharp_MethodHeader.__init__)


def test_csharp_methodheader_constructor_args():
    sig = inspect.signature(cSharp_MethodHeader.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_csharp_methodheader_has_modifier():
    assert hasattr(cSharp_MethodHeader, "modifier")
    descriptor = None
    for klass in cSharp_MethodHeader.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp_setaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_SetAccessorDeclaration)


def test_csharp_setaccessordeclaration_constructor_exists():
    assert callable(cSharp_SetAccessorDeclaration.__init__)


def test_csharp_setaccessordeclaration_constructor_args():
    sig = inspect.signature(cSharp_SetAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_getaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_GetAccessorDeclaration)


def test_csharp_getaccessordeclaration_constructor_exists():
    assert callable(cSharp_GetAccessorDeclaration.__init__)


def test_csharp_getaccessordeclaration_constructor_args():
    sig = inspect.signature(cSharp_GetAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_removeaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_RemoveAccessorDeclaration)


def test_csharp_removeaccessordeclaration_constructor_exists():
    assert callable(cSharp_RemoveAccessorDeclaration.__init__)


def test_csharp_removeaccessordeclaration_constructor_args():
    sig = inspect.signature(cSharp_RemoveAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_addaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_AddAccessorDeclaration)


def test_csharp_addaccessordeclaration_constructor_exists():
    assert callable(cSharp_AddAccessorDeclaration.__init__)


def test_csharp_addaccessordeclaration_constructor_args():
    sig = inspect.signature(cSharp_AddAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_namespacebody_is_not_abstract():
    assert not inspect.isabstract(cSharp_NamespaceBody)


def test_csharp_namespacebody_constructor_exists():
    assert callable(cSharp_NamespaceBody.__init__)


def test_csharp_namespacebody_constructor_args():
    sig = inspect.signature(cSharp_NamespaceBody.__init__)
    params = list(sig.parameters.keys())



def test_csharp_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(cSharp_VariableInitializer)


def test_csharp_variableinitializer_constructor_exists():
    assert callable(cSharp_VariableInitializer.__init__)


def test_csharp_variableinitializer_constructor_args():
    sig = inspect.signature(cSharp_VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp_primaryexpression2_is_not_abstract():
    assert not inspect.isabstract(cSharp_PrimaryExpression2)


def test_csharp_primaryexpression2_constructor_exists():
    assert callable(cSharp_PrimaryExpression2.__init__)


def test_csharp_primaryexpression2_constructor_args():
    sig = inspect.signature(cSharp_PrimaryExpression2.__init__)
    params = list(sig.parameters.keys())
    assert "incrementeDecrement" in params, "Missing parameter 'incrementeDecrement'"

def test_csharp_primaryexpression2_has_incrementeDecrement():
    assert hasattr(cSharp_PrimaryExpression2, "incrementeDecrement")
    descriptor = None
    for klass in cSharp_PrimaryExpression2.__mro__:
        if "incrementeDecrement" in klass.__dict__:
            descriptor = klass.__dict__["incrementeDecrement"]
            break
    assert isinstance(descriptor, property)



def test_csharp_typeorvoid_is_not_abstract():
    assert not inspect.isabstract(cSharp_TypeOrVoid)


def test_csharp_typeorvoid_constructor_exists():
    assert callable(cSharp_TypeOrVoid.__init__)


def test_csharp_typeorvoid_constructor_args():
    sig = inspect.signature(cSharp_TypeOrVoid.__init__)
    params = list(sig.parameters.keys())



def test_csharp_argumentlist_is_not_abstract():
    assert not inspect.isabstract(cSharp_ArgumentList)


def test_csharp_argumentlist_constructor_exists():
    assert callable(cSharp_ArgumentList.__init__)


def test_csharp_argumentlist_constructor_args():
    sig = inspect.signature(cSharp_ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_csharp_variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp_VariableDeclarator)


def test_csharp_variabledeclarator_constructor_exists():
    assert callable(cSharp_VariableDeclarator.__init__)


def test_csharp_variabledeclarator_constructor_args():
    sig = inspect.signature(cSharp_VariableDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(ConstantDeclaration)


def test_constantdeclaration_constructor_exists():
    assert callable(ConstantDeclaration.__init__)


def test_constantdeclaration_constructor_args():
    sig = inspect.signature(ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(FieldDeclaration)


def test_fielddeclaration_constructor_exists():
    assert callable(FieldDeclaration.__init__)


def test_fielddeclaration_constructor_args():
    sig = inspect.signature(FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_propertydeclaration_is_not_abstract():
    assert not inspect.isabstract(PropertyDeclaration)


def test_propertydeclaration_constructor_exists():
    assert callable(PropertyDeclaration.__init__)


def test_propertydeclaration_constructor_args():
    sig = inspect.signature(PropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_eventdeclaration_is_not_abstract():
    assert not inspect.isabstract(EventDeclaration)


def test_eventdeclaration_constructor_exists():
    assert callable(EventDeclaration.__init__)


def test_eventdeclaration_constructor_args():
    sig = inspect.signature(EventDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_type_is_not_abstract():
    assert not inspect.isabstract(cSharp_Type)


def test_csharp_type_constructor_exists():
    assert callable(cSharp_Type.__init__)


def test_csharp_type_constructor_args():
    sig = inspect.signature(cSharp_Type.__init__)
    params = list(sig.parameters.keys())



def test_csharp_builtintype_is_not_abstract():
    assert not inspect.isabstract(cSharp_BuiltInType)


def test_csharp_builtintype_constructor_exists():
    assert callable(cSharp_BuiltInType.__init__)


def test_csharp_builtintype_constructor_args():
    sig = inspect.signature(cSharp_BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_csharp_nonarraytype_is_not_abstract():
    assert not inspect.isabstract(cSharp_NonArrayType)


def test_csharp_nonarraytype_constructor_exists():
    assert callable(cSharp_NonArrayType.__init__)


def test_csharp_nonarraytype_constructor_args():
    sig = inspect.signature(cSharp_NonArrayType.__init__)
    params = list(sig.parameters.keys())



def test_csharp_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(cSharp_PrimaryExpression)


def test_csharp_primaryexpression_constructor_exists():
    assert callable(cSharp_PrimaryExpression.__init__)


def test_csharp_primaryexpression_constructor_args():
    sig = inspect.signature(cSharp_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "rankSpecifier" in params, "Missing parameter 'rankSpecifier'"
    assert "predefinedType" in params, "Missing parameter 'predefinedType'"
    assert "literal" in params, "Missing parameter 'literal'"

def test_csharp_primaryexpression_has_rankSpecifier():
    assert hasattr(cSharp_PrimaryExpression, "rankSpecifier")
    descriptor = None
    for klass in cSharp_PrimaryExpression.__mro__:
        if "rankSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["rankSpecifier"]
            break
    assert isinstance(descriptor, property)

def test_csharp_primaryexpression_has_predefinedType():
    assert hasattr(cSharp_PrimaryExpression, "predefinedType")
    descriptor = None
    for klass in cSharp_PrimaryExpression.__mro__:
        if "predefinedType" in klass.__dict__:
            descriptor = klass.__dict__["predefinedType"]
            break
    assert isinstance(descriptor, property)

def test_csharp_primaryexpression_has_literal():
    assert hasattr(cSharp_PrimaryExpression, "literal")
    descriptor = None
    for klass in cSharp_PrimaryExpression.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_csharp_expression2_is_not_abstract():
    assert not inspect.isabstract(cSharp_Expression2)


def test_csharp_expression2_constructor_exists():
    assert callable(cSharp_Expression2.__init__)


def test_csharp_expression2_constructor_args():
    sig = inspect.signature(cSharp_Expression2.__init__)
    params = list(sig.parameters.keys())



def test_csharp_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(cSharp_UnaryExpression)


def test_csharp_unaryexpression_constructor_exists():
    assert callable(cSharp_UnaryExpression.__init__)


def test_csharp_unaryexpression_constructor_args():
    sig = inspect.signature(cSharp_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expUnaryOperator" in params, "Missing parameter 'expUnaryOperator'"

def test_csharp_unaryexpression_has_expUnaryOperator():
    assert hasattr(cSharp_UnaryExpression, "expUnaryOperator")
    descriptor = None
    for klass in cSharp_UnaryExpression.__mro__:
        if "expUnaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["expUnaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_resourceaquisition_is_not_abstract():
    assert not inspect.isabstract(ResourceAquisition)


def test_resourceaquisition_constructor_exists():
    assert callable(ResourceAquisition.__init__)


def test_resourceaquisition_constructor_args():
    sig = inspect.signature(ResourceAquisition.__init__)
    params = list(sig.parameters.keys())



def test_csharp_localvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_LocalVariableDeclaration)


def test_csharp_localvariabledeclaration_constructor_exists():
    assert callable(cSharp_LocalVariableDeclaration.__init__)


def test_csharp_localvariabledeclaration_constructor_args():
    sig = inspect.signature(cSharp_LocalVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(VariableInitializer)


def test_variableinitializer_constructor_exists():
    assert callable(VariableInitializer.__init__)


def test_variableinitializer_constructor_args():
    sig = inspect.signature(VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(cSharp_ArrayInitializer)


def test_csharp_arrayinitializer_constructor_exists():
    assert callable(cSharp_ArrayInitializer.__init__)


def test_csharp_arrayinitializer_constructor_args():
    sig = inspect.signature(cSharp_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp_expression_is_not_abstract():
    assert not inspect.isabstract(cSharp_Expression)


def test_csharp_expression_constructor_exists():
    assert callable(cSharp_Expression.__init__)


def test_csharp_expression_constructor_args():
    sig = inspect.signature(cSharp_Expression.__init__)
    params = list(sig.parameters.keys())



def test_csharp_expressionlist_is_not_abstract():
    assert not inspect.isabstract(cSharp_ExpressionList)


def test_csharp_expressionlist_constructor_exists():
    assert callable(cSharp_ExpressionList.__init__)


def test_csharp_expressionlist_constructor_args():
    sig = inspect.signature(cSharp_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_csharp_attributearguments_is_not_abstract():
    assert not inspect.isabstract(cSharp_AttributeArguments)


def test_csharp_attributearguments_constructor_exists():
    assert callable(cSharp_AttributeArguments.__init__)


def test_csharp_attributearguments_constructor_args():
    sig = inspect.signature(cSharp_AttributeArguments.__init__)
    params = list(sig.parameters.keys())



def test_csharp_attributename_is_not_abstract():
    assert not inspect.isabstract(cSharp_AttributeName)


def test_csharp_attributename_constructor_exists():
    assert callable(cSharp_AttributeName.__init__)


def test_csharp_attributename_constructor_args():
    sig = inspect.signature(cSharp_AttributeName.__init__)
    params = list(sig.parameters.keys())



def test_csharp_globalattributesection_is_not_abstract():
    assert not inspect.isabstract(cSharp_GlobalAttributeSection)


def test_csharp_globalattributesection_constructor_exists():
    assert callable(cSharp_GlobalAttributeSection.__init__)


def test_csharp_globalattributesection_constructor_args():
    sig = inspect.signature(cSharp_GlobalAttributeSection.__init__)
    params = list(sig.parameters.keys())



def test_csharp_arraytype_is_not_abstract():
    assert not inspect.isabstract(cSharp_ArrayType)


def test_csharp_arraytype_constructor_exists():
    assert callable(cSharp_ArrayType.__init__)


def test_csharp_arraytype_constructor_args():
    sig = inspect.signature(cSharp_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_csharp_qualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(cSharp_QualifiedIdentifier)


def test_csharp_qualifiedidentifier_constructor_exists():
    assert callable(cSharp_QualifiedIdentifier.__init__)


def test_csharp_qualifiedidentifier_constructor_args():
    sig = inspect.signature(cSharp_QualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_csharp_identifier_is_not_abstract():
    assert not inspect.isabstract(cSharp_Identifier)


def test_csharp_identifier_constructor_exists():
    assert callable(cSharp_Identifier.__init__)


def test_csharp_identifier_constructor_args():
    sig = inspect.signature(cSharp_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_csharp_namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp_NamespaceMemberDeclaration)


def test_csharp_namespacememberdeclaration_constructor_exists():
    assert callable(cSharp_NamespaceMemberDeclaration.__init__)


def test_csharp_namespacememberdeclaration_constructor_args():
    sig = inspect.signature(cSharp_NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp_globalattributes_is_not_abstract():
    assert not inspect.isabstract(cSharp_GlobalAttributes)


def test_csharp_globalattributes_constructor_exists():
    assert callable(cSharp_GlobalAttributes.__init__)


def test_csharp_globalattributes_constructor_args():
    sig = inspect.signature(cSharp_GlobalAttributes.__init__)
    params = list(sig.parameters.keys())



def test_csharp_usingdirective_is_not_abstract():
    assert not inspect.isabstract(cSharp_UsingDirective)


def test_csharp_usingdirective_constructor_exists():
    assert callable(cSharp_UsingDirective.__init__)


def test_csharp_usingdirective_constructor_args():
    sig = inspect.signature(cSharp_UsingDirective.__init__)
    params = list(sig.parameters.keys())



def test_csharp_compilationunit_is_not_abstract():
    assert not inspect.isabstract(cSharp_CompilationUnit)


def test_csharp_compilationunit_constructor_exists():
    assert callable(cSharp_CompilationUnit.__init__)


def test_csharp_compilationunit_constructor_args():
    sig = inspect.signature(cSharp_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_csharp_attribute_is_not_abstract():
    assert not inspect.isabstract(cSharp_Attribute)


def test_csharp_attribute_constructor_exists():
    assert callable(cSharp_Attribute.__init__)


def test_csharp_attribute_constructor_args():
    sig = inspect.signature(cSharp_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_attributesection_is_not_abstract():
    assert not inspect.isabstract(AttributeSection)


def test_attributesection_constructor_exists():
    assert callable(AttributeSection.__init__)


def test_attributesection_constructor_args():
    sig = inspect.signature(AttributeSection.__init__)
    params = list(sig.parameters.keys())



def test_csharp_attributesection_is_not_abstract():
    assert not inspect.isabstract(cSharp_AttributeSection)


def test_csharp_attributesection_constructor_exists():
    assert callable(cSharp_AttributeSection.__init__)


def test_csharp_attributesection_constructor_args():
    sig = inspect.signature(cSharp_AttributeSection.__init__)
    params = list(sig.parameters.keys())



def test_csharp_attributes_is_not_abstract():
    assert not inspect.isabstract(cSharp_Attributes)


def test_csharp_attributes_constructor_exists():
    assert callable(cSharp_Attributes.__init__)


def test_csharp_attributes_constructor_args():
    sig = inspect.signature(cSharp_Attributes.__init__)
    params = list(sig.parameters.keys())



def test_csharp_attributelist_is_not_abstract():
    assert not inspect.isabstract(cSharp_AttributeList)


def test_csharp_attributelist_constructor_exists():
    assert callable(cSharp_AttributeList.__init__)


def test_csharp_attributelist_constructor_args():
    sig = inspect.signature(cSharp_AttributeList.__init__)
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
TypeOrVoid_strategy = st.builds(
    TypeOrVoid,
)
cSharp_Void_strategy = st.builds(
    cSharp_Void,
)
cSharp_ParameterArray_strategy = st.builds(
    cSharp_ParameterArray,
)
OperatorDeclarator_strategy = st.builds(
    OperatorDeclarator,
)
cSharp_UnaryOperatorDeclarator_strategy = st.builds(
    cSharp_UnaryOperatorDeclarator,
)
cSharp_BinaryOperatorDeclarator_strategy = st.builds(
    cSharp_BinaryOperatorDeclarator,
    overBinOperator=
        safe_text
)
cSharp_ConversionOperatorDeclarator_strategy = st.builds(
    cSharp_ConversionOperatorDeclarator,
)
cSharp_OperatorDeclarator_strategy = st.builds(
    cSharp_OperatorDeclarator,
)
cSharp_IndexerDeclarator_strategy = st.builds(
    cSharp_IndexerDeclarator,
)
cSharp_ConstructorDeclarator_strategy = st.builds(
    cSharp_ConstructorDeclarator,
)
cSharp_StaticConstructorDeclaration_strategy = st.builds(
    cSharp_StaticConstructorDeclaration,
    staticCosntModifier=
        safe_text
)
cSharp_DestructorDeclaration_strategy = st.builds(
    cSharp_DestructorDeclaration,
)
cSharp_ConstructorDeclaration_strategy = st.builds(
    cSharp_ConstructorDeclaration,
    constModifier=
        safe_text
)
cSharp_OperatorDeclaration_strategy = st.builds(
    cSharp_OperatorDeclaration,
    opModifier=
        safe_text
)
cSharp_IndexerDeclaration_strategy = st.builds(
    cSharp_IndexerDeclaration,
    idModifier=
        safe_text
)
cSharp_EventDeclaration_strategy = st.builds(
    cSharp_EventDeclaration,
)
cSharp_PropertyDeclaration_strategy = st.builds(
    cSharp_PropertyDeclaration,
)
cSharp_ConstantDeclaration_strategy = st.builds(
    cSharp_ConstantDeclaration,
)
cSharp_MethodDeclaration_strategy = st.builds(
    cSharp_MethodDeclaration,
)
cSharp_FieldDeclaration_strategy = st.builds(
    cSharp_FieldDeclaration,
)
cSharp_Argument_strategy = st.builds(
    cSharp_Argument,
)
ConstructorInitializer_strategy = st.builds(
    ConstructorInitializer,
)
cSharp_ConstructorInitializer_strategy = st.builds(
    cSharp_ConstructorInitializer,
)
cSharp_InterfaceAccessors_strategy = st.builds(
    cSharp_InterfaceAccessors,
)
cSharp_ClassMemberDeclaration_strategy = st.builds(
    cSharp_ClassMemberDeclaration,
)
cSharp_ClassBody_strategy = st.builds(
    cSharp_ClassBody,
)
cSharp_ClassBase_strategy = st.builds(
    cSharp_ClassBase,
)
cSharp_InterfaceEventDeclaration_strategy = st.builds(
    cSharp_InterfaceEventDeclaration,
)
cSharp_InterfaceMethodDeclaration_strategy = st.builds(
    cSharp_InterfaceMethodDeclaration,
)
cSharp_InterfaceMemberDeclaration_strategy = st.builds(
    cSharp_InterfaceMemberDeclaration,
)
cSharp_InterfaceBody_strategy = st.builds(
    cSharp_InterfaceBody,
)
cSharp_EnumMemberDeclaration_strategy = st.builds(
    cSharp_EnumMemberDeclaration,
)
cSharp_EnumBody_strategy = st.builds(
    cSharp_EnumBody,
)
cSharp_DelegateDeclaration_strategy = st.builds(
    cSharp_DelegateDeclaration,
)
cSharp_EnumDeclaration_strategy = st.builds(
    cSharp_EnumDeclaration,
)
cSharp_InterfaceDeclaration_strategy = st.builds(
    cSharp_InterfaceDeclaration,
)
cSharp_FormalParameterList_strategy = st.builds(
    cSharp_FormalParameterList,
)
cSharp_InterfacePropertyDeclaration_strategy = st.builds(
    cSharp_InterfacePropertyDeclaration,
)
cSharp_InterfaceIndexerDeclaration_strategy = st.builds(
    cSharp_InterfaceIndexerDeclaration,
)
cSharp_TypeDeclaration_strategy = st.builds(
    cSharp_TypeDeclaration,
)
cSharp_NamespaceDeclaration_strategy = st.builds(
    cSharp_NamespaceDeclaration,
)
cSharp_QualifiedIdentifierList_strategy = st.builds(
    cSharp_QualifiedIdentifierList,
)
ClassBase_strategy = st.builds(
    ClassBase,
)
ArrayType_strategy = st.builds(
    ArrayType,
)
BuiltInType_strategy = st.builds(
    BuiltInType,
)
cSharp_BuiltInClassType_strategy = st.builds(
    cSharp_BuiltInClassType,
)
cSharp_IntegralType_strategy = st.builds(
    cSharp_IntegralType,
)
cSharp_ConstantDeclarator_strategy = st.builds(
    cSharp_ConstantDeclarator,
)
cSharp_AccessorDeclarations_strategy = st.builds(
    cSharp_AccessorDeclarations,
)
cSharp_EventAccessorDeclarations_strategy = st.builds(
    cSharp_EventAccessorDeclarations,
)
cSharp_ClassDeclaration_strategy = st.builds(
    cSharp_ClassDeclaration,
    classModifier=
        safe_text
)
BuiltInClassType_strategy = st.builds(
    BuiltInClassType,
)
cSharp_String_strategy = st.builds(
    cSharp_String,
)
cSharp_Object_strategy = st.builds(
    cSharp_Object,
)
cSharp_Double_strategy = st.builds(
    cSharp_Double,
)
cSharp_Float_strategy = st.builds(
    cSharp_Float,
)
cSharp_Decimal_strategy = st.builds(
    cSharp_Decimal,
)
cSharp_Bool_strategy = st.builds(
    cSharp_Bool,
)
IntegralType_strategy = st.builds(
    IntegralType,
)
cSharp_Char_strategy = st.builds(
    cSharp_Char,
)
cSharp_Short_strategy = st.builds(
    cSharp_Short,
)
cSharp_Long_strategy = st.builds(
    cSharp_Long,
)
cSharp_ULong_strategy = st.builds(
    cSharp_ULong,
)
cSharp_Byte_strategy = st.builds(
    cSharp_Byte,
)
cSharp_UShort_strategy = st.builds(
    cSharp_UShort,
)
cSharp_UInt_strategy = st.builds(
    cSharp_UInt,
)
cSharp_Int_strategy = st.builds(
    cSharp_Int,
)
cSharp_SByte_strategy = st.builds(
    cSharp_SByte,
)
GetAccessorDeclaration_strategy = st.builds(
    GetAccessorDeclaration,
)
SetAccessorDeclaration_strategy = st.builds(
    SetAccessorDeclaration,
)
cSharp_MaybeEmptyBlock_strategy = st.builds(
    cSharp_MaybeEmptyBlock,
)
MaybeEmptyBlock_strategy = st.builds(
    MaybeEmptyBlock,
)
AddAccessorDeclaration_strategy = st.builds(
    AddAccessorDeclaration,
)
RemoveAccessorDeclaration_strategy = st.builds(
    RemoveAccessorDeclaration,
)
cSharp_ElsePart_strategy = st.builds(
    cSharp_ElsePart,
)
cSharp_SwitchLabel_strategy = st.builds(
    cSharp_SwitchLabel,
)
cSharp_SwitchSection_strategy = st.builds(
    cSharp_SwitchSection,
)
cSharp_SwitchStatement_strategy = st.builds(
    cSharp_SwitchStatement,
)
cSharp_IfStatement_strategy = st.builds(
    cSharp_IfStatement,
)
cSharp_StatementExpressionList_strategy = st.builds(
    cSharp_StatementExpressionList,
)
cSharp_ForInitializer_strategy = st.builds(
    cSharp_ForInitializer,
)
cSharp_ForeachStatement_strategy = st.builds(
    cSharp_ForeachStatement,
)
cSharp_ForStatement_strategy = st.builds(
    cSharp_ForStatement,
)
cSharp_DoStatement_strategy = st.builds(
    cSharp_DoStatement,
)
cSharp_WhileStatement_strategy = st.builds(
    cSharp_WhileStatement,
)
cSharp_GotoStatement_strategy = st.builds(
    cSharp_GotoStatement,
)
cSharp_ContinueStatement_strategy = st.builds(
    cSharp_ContinueStatement,
)
cSharp_BreakStatement_strategy = st.builds(
    cSharp_BreakStatement,
)
cSharp_GeneralCatchclause_strategy = st.builds(
    cSharp_GeneralCatchclause,
)
cSharp_SpecificCatchClause_strategy = st.builds(
    cSharp_SpecificCatchClause,
)
cSharp_FinallyClause_strategy = st.builds(
    cSharp_FinallyClause,
)
cSharp_CatchClauses_strategy = st.builds(
    cSharp_CatchClauses,
)
cSharp_ThrowStatement_strategy = st.builds(
    cSharp_ThrowStatement,
)
cSharp_ReturnStatement_strategy = st.builds(
    cSharp_ReturnStatement,
)
cSharp_ResourceAquisition_strategy = st.builds(
    cSharp_ResourceAquisition,
)
cSharp_UsingStatement_strategy = st.builds(
    cSharp_UsingStatement,
)
cSharp_LockStatement_strategy = st.builds(
    cSharp_LockStatement,
)
cSharp_Block_strategy = st.builds(
    cSharp_Block,
)
cSharp_StatementExpression_strategy = st.builds(
    cSharp_StatementExpression,
    incrimentDecrement=
        safe_text,
    assignementOperator=
        safe_text
)
cSharp_LocalconstantDeclaration_strategy = st.builds(
    cSharp_LocalconstantDeclaration,
)
cSharp_EmbeddedStatement_strategy = st.builds(
    cSharp_EmbeddedStatement,
)
cSharp_DeclarationStatment_strategy = st.builds(
    cSharp_DeclarationStatment,
)
cSharp_LabeledStatement_strategy = st.builds(
    cSharp_LabeledStatement,
)
cSharp_Statement_strategy = st.builds(
    cSharp_Statement,
)
cSharp_TryStatement_strategy = st.builds(
    cSharp_TryStatement,
)
cSharp_JumpStatement_strategy = st.builds(
    cSharp_JumpStatement,
)
cSharp_IterationStatement_strategy = st.builds(
    cSharp_IterationStatement,
)
cSharp_SelectionStatement_strategy = st.builds(
    cSharp_SelectionStatement,
)
DelegateDeclaration_strategy = st.builds(
    DelegateDeclaration,
)
cSharp_FixedParameter_strategy = st.builds(
    cSharp_FixedParameter,
)
FormalParameterList_strategy = st.builds(
    FormalParameterList,
)
cSharp_FixedParameters_strategy = st.builds(
    cSharp_FixedParameters,
)
cSharp_MethodHeader_strategy = st.builds(
    cSharp_MethodHeader,
    modifier=
        safe_text
)
cSharp_SetAccessorDeclaration_strategy = st.builds(
    cSharp_SetAccessorDeclaration,
)
cSharp_GetAccessorDeclaration_strategy = st.builds(
    cSharp_GetAccessorDeclaration,
)
cSharp_RemoveAccessorDeclaration_strategy = st.builds(
    cSharp_RemoveAccessorDeclaration,
)
cSharp_AddAccessorDeclaration_strategy = st.builds(
    cSharp_AddAccessorDeclaration,
)
cSharp_NamespaceBody_strategy = st.builds(
    cSharp_NamespaceBody,
)
cSharp_VariableInitializer_strategy = st.builds(
    cSharp_VariableInitializer,
)
cSharp_PrimaryExpression2_strategy = st.builds(
    cSharp_PrimaryExpression2,
    incrementeDecrement=
        safe_text
)
cSharp_TypeOrVoid_strategy = st.builds(
    cSharp_TypeOrVoid,
)
cSharp_ArgumentList_strategy = st.builds(
    cSharp_ArgumentList,
)
cSharp_VariableDeclarator_strategy = st.builds(
    cSharp_VariableDeclarator,
)
ConstantDeclaration_strategy = st.builds(
    ConstantDeclaration,
)
FieldDeclaration_strategy = st.builds(
    FieldDeclaration,
)
PropertyDeclaration_strategy = st.builds(
    PropertyDeclaration,
)
EventDeclaration_strategy = st.builds(
    EventDeclaration,
)
cSharp_Type_strategy = st.builds(
    cSharp_Type,
)
cSharp_BuiltInType_strategy = st.builds(
    cSharp_BuiltInType,
)
cSharp_NonArrayType_strategy = st.builds(
    cSharp_NonArrayType,
)
cSharp_PrimaryExpression_strategy = st.builds(
    cSharp_PrimaryExpression,
    rankSpecifier=
        safe_text,
    predefinedType=
        safe_text,
    literal=
        safe_text
)
cSharp_Expression2_strategy = st.builds(
    cSharp_Expression2,
)
cSharp_UnaryExpression_strategy = st.builds(
    cSharp_UnaryExpression,
    expUnaryOperator=
        safe_text
)
ResourceAquisition_strategy = st.builds(
    ResourceAquisition,
)
cSharp_LocalVariableDeclaration_strategy = st.builds(
    cSharp_LocalVariableDeclaration,
)
Argument_strategy = st.builds(
    Argument,
)
VariableInitializer_strategy = st.builds(
    VariableInitializer,
)
cSharp_ArrayInitializer_strategy = st.builds(
    cSharp_ArrayInitializer,
)
cSharp_Expression_strategy = st.builds(
    cSharp_Expression,
)
cSharp_ExpressionList_strategy = st.builds(
    cSharp_ExpressionList,
)
cSharp_AttributeArguments_strategy = st.builds(
    cSharp_AttributeArguments,
)
cSharp_AttributeName_strategy = st.builds(
    cSharp_AttributeName,
)
cSharp_GlobalAttributeSection_strategy = st.builds(
    cSharp_GlobalAttributeSection,
)
cSharp_ArrayType_strategy = st.builds(
    cSharp_ArrayType,
)
cSharp_QualifiedIdentifier_strategy = st.builds(
    cSharp_QualifiedIdentifier,
)
cSharp_Identifier_strategy = st.builds(
    cSharp_Identifier,
)
cSharp_NamespaceMemberDeclaration_strategy = st.builds(
    cSharp_NamespaceMemberDeclaration,
)
cSharp_GlobalAttributes_strategy = st.builds(
    cSharp_GlobalAttributes,
)
cSharp_UsingDirective_strategy = st.builds(
    cSharp_UsingDirective,
)
cSharp_CompilationUnit_strategy = st.builds(
    cSharp_CompilationUnit,
)
cSharp_Attribute_strategy = st.builds(
    cSharp_Attribute,
)
AttributeSection_strategy = st.builds(
    AttributeSection,
)
cSharp_AttributeSection_strategy = st.builds(
    cSharp_AttributeSection,
)
cSharp_Attributes_strategy = st.builds(
    cSharp_Attributes,
)
cSharp_AttributeList_strategy = st.builds(
    cSharp_AttributeList,
)

@given(instance=TypeOrVoid_strategy)
@settings(max_examples=50)
def test_typeorvoid_instantiation(instance):
    assert isinstance(instance, TypeOrVoid)

@given(instance=cSharp_Void_strategy)
@settings(max_examples=50)
def test_csharp_void_instantiation(instance):
    assert isinstance(instance, cSharp_Void)

@given(instance=cSharp_ParameterArray_strategy)
@settings(max_examples=50)
def test_csharp_parameterarray_instantiation(instance):
    assert isinstance(instance, cSharp_ParameterArray)

@given(instance=OperatorDeclarator_strategy)
@settings(max_examples=50)
def test_operatordeclarator_instantiation(instance):
    assert isinstance(instance, OperatorDeclarator)

@given(instance=cSharp_UnaryOperatorDeclarator_strategy)
@settings(max_examples=50)
def test_csharp_unaryoperatordeclarator_instantiation(instance):
    assert isinstance(instance, cSharp_UnaryOperatorDeclarator)

@given(instance=cSharp_BinaryOperatorDeclarator_strategy)
@settings(max_examples=50)
def test_csharp_binaryoperatordeclarator_instantiation(instance):
    assert isinstance(instance, cSharp_BinaryOperatorDeclarator)



@given(instance=cSharp_BinaryOperatorDeclarator_strategy)
def test_csharp_binaryoperatordeclarator_overBinOperator_setter(instance):
    original = instance.overBinOperator
    instance.overBinOperator = original
    assert instance.overBinOperator == original

@given(instance=cSharp_ConversionOperatorDeclarator_strategy)
@settings(max_examples=50)
def test_csharp_conversionoperatordeclarator_instantiation(instance):
    assert isinstance(instance, cSharp_ConversionOperatorDeclarator)

@given(instance=cSharp_OperatorDeclarator_strategy)
@settings(max_examples=50)
def test_csharp_operatordeclarator_instantiation(instance):
    assert isinstance(instance, cSharp_OperatorDeclarator)

@given(instance=cSharp_IndexerDeclarator_strategy)
@settings(max_examples=50)
def test_csharp_indexerdeclarator_instantiation(instance):
    assert isinstance(instance, cSharp_IndexerDeclarator)

@given(instance=cSharp_ConstructorDeclarator_strategy)
@settings(max_examples=50)
def test_csharp_constructordeclarator_instantiation(instance):
    assert isinstance(instance, cSharp_ConstructorDeclarator)

@given(instance=cSharp_StaticConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_staticconstructordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_StaticConstructorDeclaration)



@given(instance=cSharp_StaticConstructorDeclaration_strategy)
def test_csharp_staticconstructordeclaration_staticCosntModifier_setter(instance):
    original = instance.staticCosntModifier
    instance.staticCosntModifier = original
    assert instance.staticCosntModifier == original

@given(instance=cSharp_DestructorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_destructordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_DestructorDeclaration)

@given(instance=cSharp_ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_constructordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_ConstructorDeclaration)



@given(instance=cSharp_ConstructorDeclaration_strategy)
def test_csharp_constructordeclaration_constModifier_setter(instance):
    original = instance.constModifier
    instance.constModifier = original
    assert instance.constModifier == original

@given(instance=cSharp_OperatorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_operatordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_OperatorDeclaration)



@given(instance=cSharp_OperatorDeclaration_strategy)
def test_csharp_operatordeclaration_opModifier_setter(instance):
    original = instance.opModifier
    instance.opModifier = original
    assert instance.opModifier == original

@given(instance=cSharp_IndexerDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_indexerdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_IndexerDeclaration)



@given(instance=cSharp_IndexerDeclaration_strategy)
def test_csharp_indexerdeclaration_idModifier_setter(instance):
    original = instance.idModifier
    instance.idModifier = original
    assert instance.idModifier == original

@given(instance=cSharp_EventDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_eventdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_EventDeclaration)

@given(instance=cSharp_PropertyDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_propertydeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_PropertyDeclaration)

@given(instance=cSharp_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_constantdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_ConstantDeclaration)

@given(instance=cSharp_MethodDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_methoddeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_MethodDeclaration)

@given(instance=cSharp_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_fielddeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_FieldDeclaration)

@given(instance=cSharp_Argument_strategy)
@settings(max_examples=50)
def test_csharp_argument_instantiation(instance):
    assert isinstance(instance, cSharp_Argument)

@given(instance=ConstructorInitializer_strategy)
@settings(max_examples=50)
def test_constructorinitializer_instantiation(instance):
    assert isinstance(instance, ConstructorInitializer)

@given(instance=cSharp_ConstructorInitializer_strategy)
@settings(max_examples=50)
def test_csharp_constructorinitializer_instantiation(instance):
    assert isinstance(instance, cSharp_ConstructorInitializer)

@given(instance=cSharp_InterfaceAccessors_strategy)
@settings(max_examples=50)
def test_csharp_interfaceaccessors_instantiation(instance):
    assert isinstance(instance, cSharp_InterfaceAccessors)

@given(instance=cSharp_ClassMemberDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_classmemberdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_ClassMemberDeclaration)

@given(instance=cSharp_ClassBody_strategy)
@settings(max_examples=50)
def test_csharp_classbody_instantiation(instance):
    assert isinstance(instance, cSharp_ClassBody)

@given(instance=cSharp_ClassBase_strategy)
@settings(max_examples=50)
def test_csharp_classbase_instantiation(instance):
    assert isinstance(instance, cSharp_ClassBase)

@given(instance=cSharp_InterfaceEventDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_interfaceeventdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_InterfaceEventDeclaration)

@given(instance=cSharp_InterfaceMethodDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_interfacemethoddeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_InterfaceMethodDeclaration)

@given(instance=cSharp_InterfaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_interfacememberdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_InterfaceMemberDeclaration)

@given(instance=cSharp_InterfaceBody_strategy)
@settings(max_examples=50)
def test_csharp_interfacebody_instantiation(instance):
    assert isinstance(instance, cSharp_InterfaceBody)

@given(instance=cSharp_EnumMemberDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_enummemberdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_EnumMemberDeclaration)

@given(instance=cSharp_EnumBody_strategy)
@settings(max_examples=50)
def test_csharp_enumbody_instantiation(instance):
    assert isinstance(instance, cSharp_EnumBody)

@given(instance=cSharp_DelegateDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_delegatedeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_DelegateDeclaration)

@given(instance=cSharp_EnumDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_enumdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_EnumDeclaration)

@given(instance=cSharp_InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_interfacedeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_InterfaceDeclaration)

@given(instance=cSharp_FormalParameterList_strategy)
@settings(max_examples=50)
def test_csharp_formalparameterlist_instantiation(instance):
    assert isinstance(instance, cSharp_FormalParameterList)

@given(instance=cSharp_InterfacePropertyDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_interfacepropertydeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_InterfacePropertyDeclaration)

@given(instance=cSharp_InterfaceIndexerDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_interfaceindexerdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_InterfaceIndexerDeclaration)

@given(instance=cSharp_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_typedeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_TypeDeclaration)

@given(instance=cSharp_NamespaceDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_namespacedeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_NamespaceDeclaration)

@given(instance=cSharp_QualifiedIdentifierList_strategy)
@settings(max_examples=50)
def test_csharp_qualifiedidentifierlist_instantiation(instance):
    assert isinstance(instance, cSharp_QualifiedIdentifierList)

@given(instance=ClassBase_strategy)
@settings(max_examples=50)
def test_classbase_instantiation(instance):
    assert isinstance(instance, ClassBase)

@given(instance=ArrayType_strategy)
@settings(max_examples=50)
def test_arraytype_instantiation(instance):
    assert isinstance(instance, ArrayType)

@given(instance=BuiltInType_strategy)
@settings(max_examples=50)
def test_builtintype_instantiation(instance):
    assert isinstance(instance, BuiltInType)

@given(instance=cSharp_BuiltInClassType_strategy)
@settings(max_examples=50)
def test_csharp_builtinclasstype_instantiation(instance):
    assert isinstance(instance, cSharp_BuiltInClassType)

@given(instance=cSharp_IntegralType_strategy)
@settings(max_examples=50)
def test_csharp_integraltype_instantiation(instance):
    assert isinstance(instance, cSharp_IntegralType)

@given(instance=cSharp_ConstantDeclarator_strategy)
@settings(max_examples=50)
def test_csharp_constantdeclarator_instantiation(instance):
    assert isinstance(instance, cSharp_ConstantDeclarator)

@given(instance=cSharp_AccessorDeclarations_strategy)
@settings(max_examples=50)
def test_csharp_accessordeclarations_instantiation(instance):
    assert isinstance(instance, cSharp_AccessorDeclarations)

@given(instance=cSharp_EventAccessorDeclarations_strategy)
@settings(max_examples=50)
def test_csharp_eventaccessordeclarations_instantiation(instance):
    assert isinstance(instance, cSharp_EventAccessorDeclarations)

@given(instance=cSharp_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_classdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_ClassDeclaration)



@given(instance=cSharp_ClassDeclaration_strategy)
def test_csharp_classdeclaration_classModifier_setter(instance):
    original = instance.classModifier
    instance.classModifier = original
    assert instance.classModifier == original

@given(instance=BuiltInClassType_strategy)
@settings(max_examples=50)
def test_builtinclasstype_instantiation(instance):
    assert isinstance(instance, BuiltInClassType)

@given(instance=cSharp_String_strategy)
@settings(max_examples=50)
def test_csharp_string_instantiation(instance):
    assert isinstance(instance, cSharp_String)

@given(instance=cSharp_Object_strategy)
@settings(max_examples=50)
def test_csharp_object_instantiation(instance):
    assert isinstance(instance, cSharp_Object)

@given(instance=cSharp_Double_strategy)
@settings(max_examples=50)
def test_csharp_double_instantiation(instance):
    assert isinstance(instance, cSharp_Double)

@given(instance=cSharp_Float_strategy)
@settings(max_examples=50)
def test_csharp_float_instantiation(instance):
    assert isinstance(instance, cSharp_Float)

@given(instance=cSharp_Decimal_strategy)
@settings(max_examples=50)
def test_csharp_decimal_instantiation(instance):
    assert isinstance(instance, cSharp_Decimal)

@given(instance=cSharp_Bool_strategy)
@settings(max_examples=50)
def test_csharp_bool_instantiation(instance):
    assert isinstance(instance, cSharp_Bool)

@given(instance=IntegralType_strategy)
@settings(max_examples=50)
def test_integraltype_instantiation(instance):
    assert isinstance(instance, IntegralType)

@given(instance=cSharp_Char_strategy)
@settings(max_examples=50)
def test_csharp_char_instantiation(instance):
    assert isinstance(instance, cSharp_Char)

@given(instance=cSharp_Short_strategy)
@settings(max_examples=50)
def test_csharp_short_instantiation(instance):
    assert isinstance(instance, cSharp_Short)

@given(instance=cSharp_Long_strategy)
@settings(max_examples=50)
def test_csharp_long_instantiation(instance):
    assert isinstance(instance, cSharp_Long)

@given(instance=cSharp_ULong_strategy)
@settings(max_examples=50)
def test_csharp_ulong_instantiation(instance):
    assert isinstance(instance, cSharp_ULong)

@given(instance=cSharp_Byte_strategy)
@settings(max_examples=50)
def test_csharp_byte_instantiation(instance):
    assert isinstance(instance, cSharp_Byte)

@given(instance=cSharp_UShort_strategy)
@settings(max_examples=50)
def test_csharp_ushort_instantiation(instance):
    assert isinstance(instance, cSharp_UShort)

@given(instance=cSharp_UInt_strategy)
@settings(max_examples=50)
def test_csharp_uint_instantiation(instance):
    assert isinstance(instance, cSharp_UInt)

@given(instance=cSharp_Int_strategy)
@settings(max_examples=50)
def test_csharp_int_instantiation(instance):
    assert isinstance(instance, cSharp_Int)

@given(instance=cSharp_SByte_strategy)
@settings(max_examples=50)
def test_csharp_sbyte_instantiation(instance):
    assert isinstance(instance, cSharp_SByte)

@given(instance=GetAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_getaccessordeclaration_instantiation(instance):
    assert isinstance(instance, GetAccessorDeclaration)

@given(instance=SetAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_setaccessordeclaration_instantiation(instance):
    assert isinstance(instance, SetAccessorDeclaration)

@given(instance=cSharp_MaybeEmptyBlock_strategy)
@settings(max_examples=50)
def test_csharp_maybeemptyblock_instantiation(instance):
    assert isinstance(instance, cSharp_MaybeEmptyBlock)

@given(instance=MaybeEmptyBlock_strategy)
@settings(max_examples=50)
def test_maybeemptyblock_instantiation(instance):
    assert isinstance(instance, MaybeEmptyBlock)

@given(instance=AddAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_addaccessordeclaration_instantiation(instance):
    assert isinstance(instance, AddAccessorDeclaration)

@given(instance=RemoveAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_removeaccessordeclaration_instantiation(instance):
    assert isinstance(instance, RemoveAccessorDeclaration)

@given(instance=cSharp_ElsePart_strategy)
@settings(max_examples=50)
def test_csharp_elsepart_instantiation(instance):
    assert isinstance(instance, cSharp_ElsePart)

@given(instance=cSharp_SwitchLabel_strategy)
@settings(max_examples=50)
def test_csharp_switchlabel_instantiation(instance):
    assert isinstance(instance, cSharp_SwitchLabel)

@given(instance=cSharp_SwitchSection_strategy)
@settings(max_examples=50)
def test_csharp_switchsection_instantiation(instance):
    assert isinstance(instance, cSharp_SwitchSection)

@given(instance=cSharp_SwitchStatement_strategy)
@settings(max_examples=50)
def test_csharp_switchstatement_instantiation(instance):
    assert isinstance(instance, cSharp_SwitchStatement)

@given(instance=cSharp_IfStatement_strategy)
@settings(max_examples=50)
def test_csharp_ifstatement_instantiation(instance):
    assert isinstance(instance, cSharp_IfStatement)

@given(instance=cSharp_StatementExpressionList_strategy)
@settings(max_examples=50)
def test_csharp_statementexpressionlist_instantiation(instance):
    assert isinstance(instance, cSharp_StatementExpressionList)

@given(instance=cSharp_ForInitializer_strategy)
@settings(max_examples=50)
def test_csharp_forinitializer_instantiation(instance):
    assert isinstance(instance, cSharp_ForInitializer)

@given(instance=cSharp_ForeachStatement_strategy)
@settings(max_examples=50)
def test_csharp_foreachstatement_instantiation(instance):
    assert isinstance(instance, cSharp_ForeachStatement)

@given(instance=cSharp_ForStatement_strategy)
@settings(max_examples=50)
def test_csharp_forstatement_instantiation(instance):
    assert isinstance(instance, cSharp_ForStatement)

@given(instance=cSharp_DoStatement_strategy)
@settings(max_examples=50)
def test_csharp_dostatement_instantiation(instance):
    assert isinstance(instance, cSharp_DoStatement)

@given(instance=cSharp_WhileStatement_strategy)
@settings(max_examples=50)
def test_csharp_whilestatement_instantiation(instance):
    assert isinstance(instance, cSharp_WhileStatement)

@given(instance=cSharp_GotoStatement_strategy)
@settings(max_examples=50)
def test_csharp_gotostatement_instantiation(instance):
    assert isinstance(instance, cSharp_GotoStatement)

@given(instance=cSharp_ContinueStatement_strategy)
@settings(max_examples=50)
def test_csharp_continuestatement_instantiation(instance):
    assert isinstance(instance, cSharp_ContinueStatement)

@given(instance=cSharp_BreakStatement_strategy)
@settings(max_examples=50)
def test_csharp_breakstatement_instantiation(instance):
    assert isinstance(instance, cSharp_BreakStatement)

@given(instance=cSharp_GeneralCatchclause_strategy)
@settings(max_examples=50)
def test_csharp_generalcatchclause_instantiation(instance):
    assert isinstance(instance, cSharp_GeneralCatchclause)

@given(instance=cSharp_SpecificCatchClause_strategy)
@settings(max_examples=50)
def test_csharp_specificcatchclause_instantiation(instance):
    assert isinstance(instance, cSharp_SpecificCatchClause)

@given(instance=cSharp_FinallyClause_strategy)
@settings(max_examples=50)
def test_csharp_finallyclause_instantiation(instance):
    assert isinstance(instance, cSharp_FinallyClause)

@given(instance=cSharp_CatchClauses_strategy)
@settings(max_examples=50)
def test_csharp_catchclauses_instantiation(instance):
    assert isinstance(instance, cSharp_CatchClauses)

@given(instance=cSharp_ThrowStatement_strategy)
@settings(max_examples=50)
def test_csharp_throwstatement_instantiation(instance):
    assert isinstance(instance, cSharp_ThrowStatement)

@given(instance=cSharp_ReturnStatement_strategy)
@settings(max_examples=50)
def test_csharp_returnstatement_instantiation(instance):
    assert isinstance(instance, cSharp_ReturnStatement)

@given(instance=cSharp_ResourceAquisition_strategy)
@settings(max_examples=50)
def test_csharp_resourceaquisition_instantiation(instance):
    assert isinstance(instance, cSharp_ResourceAquisition)

@given(instance=cSharp_UsingStatement_strategy)
@settings(max_examples=50)
def test_csharp_usingstatement_instantiation(instance):
    assert isinstance(instance, cSharp_UsingStatement)

@given(instance=cSharp_LockStatement_strategy)
@settings(max_examples=50)
def test_csharp_lockstatement_instantiation(instance):
    assert isinstance(instance, cSharp_LockStatement)

@given(instance=cSharp_Block_strategy)
@settings(max_examples=50)
def test_csharp_block_instantiation(instance):
    assert isinstance(instance, cSharp_Block)

@given(instance=cSharp_StatementExpression_strategy)
@settings(max_examples=50)
def test_csharp_statementexpression_instantiation(instance):
    assert isinstance(instance, cSharp_StatementExpression)



@given(instance=cSharp_StatementExpression_strategy)
def test_csharp_statementexpression_incrimentDecrement_setter(instance):
    original = instance.incrimentDecrement
    instance.incrimentDecrement = original
    assert instance.incrimentDecrement == original



@given(instance=cSharp_StatementExpression_strategy)
def test_csharp_statementexpression_assignementOperator_setter(instance):
    original = instance.assignementOperator
    instance.assignementOperator = original
    assert instance.assignementOperator == original

@given(instance=cSharp_LocalconstantDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_localconstantdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_LocalconstantDeclaration)

@given(instance=cSharp_EmbeddedStatement_strategy)
@settings(max_examples=50)
def test_csharp_embeddedstatement_instantiation(instance):
    assert isinstance(instance, cSharp_EmbeddedStatement)

@given(instance=cSharp_DeclarationStatment_strategy)
@settings(max_examples=50)
def test_csharp_declarationstatment_instantiation(instance):
    assert isinstance(instance, cSharp_DeclarationStatment)

@given(instance=cSharp_LabeledStatement_strategy)
@settings(max_examples=50)
def test_csharp_labeledstatement_instantiation(instance):
    assert isinstance(instance, cSharp_LabeledStatement)

@given(instance=cSharp_Statement_strategy)
@settings(max_examples=50)
def test_csharp_statement_instantiation(instance):
    assert isinstance(instance, cSharp_Statement)

@given(instance=cSharp_TryStatement_strategy)
@settings(max_examples=50)
def test_csharp_trystatement_instantiation(instance):
    assert isinstance(instance, cSharp_TryStatement)

@given(instance=cSharp_JumpStatement_strategy)
@settings(max_examples=50)
def test_csharp_jumpstatement_instantiation(instance):
    assert isinstance(instance, cSharp_JumpStatement)

@given(instance=cSharp_IterationStatement_strategy)
@settings(max_examples=50)
def test_csharp_iterationstatement_instantiation(instance):
    assert isinstance(instance, cSharp_IterationStatement)

@given(instance=cSharp_SelectionStatement_strategy)
@settings(max_examples=50)
def test_csharp_selectionstatement_instantiation(instance):
    assert isinstance(instance, cSharp_SelectionStatement)

@given(instance=DelegateDeclaration_strategy)
@settings(max_examples=50)
def test_delegatedeclaration_instantiation(instance):
    assert isinstance(instance, DelegateDeclaration)

@given(instance=cSharp_FixedParameter_strategy)
@settings(max_examples=50)
def test_csharp_fixedparameter_instantiation(instance):
    assert isinstance(instance, cSharp_FixedParameter)

@given(instance=FormalParameterList_strategy)
@settings(max_examples=50)
def test_formalparameterlist_instantiation(instance):
    assert isinstance(instance, FormalParameterList)

@given(instance=cSharp_FixedParameters_strategy)
@settings(max_examples=50)
def test_csharp_fixedparameters_instantiation(instance):
    assert isinstance(instance, cSharp_FixedParameters)

@given(instance=cSharp_MethodHeader_strategy)
@settings(max_examples=50)
def test_csharp_methodheader_instantiation(instance):
    assert isinstance(instance, cSharp_MethodHeader)



@given(instance=cSharp_MethodHeader_strategy)
def test_csharp_methodheader_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=cSharp_SetAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_setaccessordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_SetAccessorDeclaration)

@given(instance=cSharp_GetAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_getaccessordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_GetAccessorDeclaration)

@given(instance=cSharp_RemoveAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_removeaccessordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_RemoveAccessorDeclaration)

@given(instance=cSharp_AddAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_addaccessordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_AddAccessorDeclaration)

@given(instance=cSharp_NamespaceBody_strategy)
@settings(max_examples=50)
def test_csharp_namespacebody_instantiation(instance):
    assert isinstance(instance, cSharp_NamespaceBody)

@given(instance=cSharp_VariableInitializer_strategy)
@settings(max_examples=50)
def test_csharp_variableinitializer_instantiation(instance):
    assert isinstance(instance, cSharp_VariableInitializer)

@given(instance=cSharp_PrimaryExpression2_strategy)
@settings(max_examples=50)
def test_csharp_primaryexpression2_instantiation(instance):
    assert isinstance(instance, cSharp_PrimaryExpression2)



@given(instance=cSharp_PrimaryExpression2_strategy)
def test_csharp_primaryexpression2_incrementeDecrement_setter(instance):
    original = instance.incrementeDecrement
    instance.incrementeDecrement = original
    assert instance.incrementeDecrement == original

@given(instance=cSharp_TypeOrVoid_strategy)
@settings(max_examples=50)
def test_csharp_typeorvoid_instantiation(instance):
    assert isinstance(instance, cSharp_TypeOrVoid)

@given(instance=cSharp_ArgumentList_strategy)
@settings(max_examples=50)
def test_csharp_argumentlist_instantiation(instance):
    assert isinstance(instance, cSharp_ArgumentList)

@given(instance=cSharp_VariableDeclarator_strategy)
@settings(max_examples=50)
def test_csharp_variabledeclarator_instantiation(instance):
    assert isinstance(instance, cSharp_VariableDeclarator)

@given(instance=ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_constantdeclaration_instantiation(instance):
    assert isinstance(instance, ConstantDeclaration)

@given(instance=FieldDeclaration_strategy)
@settings(max_examples=50)
def test_fielddeclaration_instantiation(instance):
    assert isinstance(instance, FieldDeclaration)

@given(instance=PropertyDeclaration_strategy)
@settings(max_examples=50)
def test_propertydeclaration_instantiation(instance):
    assert isinstance(instance, PropertyDeclaration)

@given(instance=EventDeclaration_strategy)
@settings(max_examples=50)
def test_eventdeclaration_instantiation(instance):
    assert isinstance(instance, EventDeclaration)

@given(instance=cSharp_Type_strategy)
@settings(max_examples=50)
def test_csharp_type_instantiation(instance):
    assert isinstance(instance, cSharp_Type)

@given(instance=cSharp_BuiltInType_strategy)
@settings(max_examples=50)
def test_csharp_builtintype_instantiation(instance):
    assert isinstance(instance, cSharp_BuiltInType)

@given(instance=cSharp_NonArrayType_strategy)
@settings(max_examples=50)
def test_csharp_nonarraytype_instantiation(instance):
    assert isinstance(instance, cSharp_NonArrayType)

@given(instance=cSharp_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_csharp_primaryexpression_instantiation(instance):
    assert isinstance(instance, cSharp_PrimaryExpression)



@given(instance=cSharp_PrimaryExpression_strategy)
def test_csharp_primaryexpression_rankSpecifier_setter(instance):
    original = instance.rankSpecifier
    instance.rankSpecifier = original
    assert instance.rankSpecifier == original



@given(instance=cSharp_PrimaryExpression_strategy)
def test_csharp_primaryexpression_predefinedType_setter(instance):
    original = instance.predefinedType
    instance.predefinedType = original
    assert instance.predefinedType == original



@given(instance=cSharp_PrimaryExpression_strategy)
def test_csharp_primaryexpression_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=cSharp_Expression2_strategy)
@settings(max_examples=50)
def test_csharp_expression2_instantiation(instance):
    assert isinstance(instance, cSharp_Expression2)

@given(instance=cSharp_UnaryExpression_strategy)
@settings(max_examples=50)
def test_csharp_unaryexpression_instantiation(instance):
    assert isinstance(instance, cSharp_UnaryExpression)



@given(instance=cSharp_UnaryExpression_strategy)
def test_csharp_unaryexpression_expUnaryOperator_setter(instance):
    original = instance.expUnaryOperator
    instance.expUnaryOperator = original
    assert instance.expUnaryOperator == original

@given(instance=ResourceAquisition_strategy)
@settings(max_examples=50)
def test_resourceaquisition_instantiation(instance):
    assert isinstance(instance, ResourceAquisition)

@given(instance=cSharp_LocalVariableDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_localvariabledeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_LocalVariableDeclaration)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=VariableInitializer_strategy)
@settings(max_examples=50)
def test_variableinitializer_instantiation(instance):
    assert isinstance(instance, VariableInitializer)

@given(instance=cSharp_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_csharp_arrayinitializer_instantiation(instance):
    assert isinstance(instance, cSharp_ArrayInitializer)

@given(instance=cSharp_Expression_strategy)
@settings(max_examples=50)
def test_csharp_expression_instantiation(instance):
    assert isinstance(instance, cSharp_Expression)

@given(instance=cSharp_ExpressionList_strategy)
@settings(max_examples=50)
def test_csharp_expressionlist_instantiation(instance):
    assert isinstance(instance, cSharp_ExpressionList)

@given(instance=cSharp_AttributeArguments_strategy)
@settings(max_examples=50)
def test_csharp_attributearguments_instantiation(instance):
    assert isinstance(instance, cSharp_AttributeArguments)

@given(instance=cSharp_AttributeName_strategy)
@settings(max_examples=50)
def test_csharp_attributename_instantiation(instance):
    assert isinstance(instance, cSharp_AttributeName)

@given(instance=cSharp_GlobalAttributeSection_strategy)
@settings(max_examples=50)
def test_csharp_globalattributesection_instantiation(instance):
    assert isinstance(instance, cSharp_GlobalAttributeSection)

@given(instance=cSharp_ArrayType_strategy)
@settings(max_examples=50)
def test_csharp_arraytype_instantiation(instance):
    assert isinstance(instance, cSharp_ArrayType)

@given(instance=cSharp_QualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_csharp_qualifiedidentifier_instantiation(instance):
    assert isinstance(instance, cSharp_QualifiedIdentifier)

@given(instance=cSharp_Identifier_strategy)
@settings(max_examples=50)
def test_csharp_identifier_instantiation(instance):
    assert isinstance(instance, cSharp_Identifier)

@given(instance=cSharp_NamespaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_csharp_namespacememberdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp_NamespaceMemberDeclaration)

@given(instance=cSharp_GlobalAttributes_strategy)
@settings(max_examples=50)
def test_csharp_globalattributes_instantiation(instance):
    assert isinstance(instance, cSharp_GlobalAttributes)

@given(instance=cSharp_UsingDirective_strategy)
@settings(max_examples=50)
def test_csharp_usingdirective_instantiation(instance):
    assert isinstance(instance, cSharp_UsingDirective)

@given(instance=cSharp_CompilationUnit_strategy)
@settings(max_examples=50)
def test_csharp_compilationunit_instantiation(instance):
    assert isinstance(instance, cSharp_CompilationUnit)

@given(instance=cSharp_Attribute_strategy)
@settings(max_examples=50)
def test_csharp_attribute_instantiation(instance):
    assert isinstance(instance, cSharp_Attribute)

@given(instance=AttributeSection_strategy)
@settings(max_examples=50)
def test_attributesection_instantiation(instance):
    assert isinstance(instance, AttributeSection)

@given(instance=cSharp_AttributeSection_strategy)
@settings(max_examples=50)
def test_csharp_attributesection_instantiation(instance):
    assert isinstance(instance, cSharp_AttributeSection)

@given(instance=cSharp_Attributes_strategy)
@settings(max_examples=50)
def test_csharp_attributes_instantiation(instance):
    assert isinstance(instance, cSharp_Attributes)

@given(instance=cSharp_AttributeList_strategy)
@settings(max_examples=50)
def test_csharp_attributelist_instantiation(instance):
    assert isinstance(instance, cSharp_AttributeList)

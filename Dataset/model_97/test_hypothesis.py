import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BodyDeclaration,
    Java5_AbstractTypeDeclaration,
    VariableDeclaration,
    PrimitiveType,
    Java5_PrimitiveTypeInt,
    Java5_PrimitiveTypeDouble,
    Java5_PrimitiveTypeLong,
    Java5_PrimitiveTypeVoid,
    Java5_PrimitiveTypeChar,
    Java5_PrimitiveTypeByte,
    Java5_PrimitiveTypeShort,
    Java5_PrimitiveTypeFloat,
    Java5_PrimitiveTypeBoolean,
    Java5_Model,
    Java5_MethodDeclaration,
    Java5_Initializer,
    Java5_VariableDeclarationFragment,
    Java5_FieldDeclaration,
    Java5_EnumConstantDeclaration,
    Java5_SingleVariableDeclaration,
    TypeDeclaration,
    Java5_InterfaceDeclaration,
    Java5_ClassDeclaration,
    OrphanType,
    Java5_WildCardType,
    Java5_PrimitiveType,
    Java5_ParameterizedType,
    Java5_ArrayType,
    Java5_ASTNode,
    Statement,
    Java5_BreakStatement,
    Java5_SynchronizedStatement,
    Java5_IfStatement,
    Java5_VariableDeclarationStatement,
    Java5_EmptyStatement,
    Java5_ConstructorInvocation,
    Java5_TypeDeclarationStatement,
    Java5_DoStatement,
    Java5_SwitchStatement,
    Java5_WhileStatement,
    Java5_CatchClause,
    Java5_TryStatement,
    Java5_SwitchCase,
    Java5_ReturnStatement,
    Java5_Block,
    Java5_ForStatement,
    Java5_ThrowStatement,
    Java5_ExpressionStatement,
    Java5_SuperConstructorInvocation,
    Java5_ContinueStatement,
    Java5_EnhancedForStatement,
    Java5_AssertStatement,
    NamedElement,
    Java5_LabeledStatement,
    Java5_BodyDeclaration,
    Java5_UnresolvedItem,
    Java5_TypeParameter,
    Java5_CompilationUnit,
    Java5_PackageDeclaration,
    Java5_OrphanType,
    Java5_VariableDeclaration,
    Java5_AnnotationMemberValuePair,
    ASTNode,
    Java5_MethodRef,
    Java5_Expression,
    Java5_TextElement,
    Java5_ImportDeclaration,
    Java5_TagElement,
    Java5_NamedElement,
    Java5_MethodRefParameter,
    Java5_Modifier,
    Java5_Statement,
    Java5_MemberRef,
    Java5_AnonymousClassDeclaration,
    Java5_AnnotationTypeMemberDeclaration,
    AbstractTypeDeclaration,
    Java5_AnnotationTypeDeclaration,
    Java5_EnumDeclaration,
    Java5_TypeDeclaration,
    Expression,
    Java5_StringLiteral,
    Java5_ParenthesizedExpression,
    Java5_ThisExpression,
    Java5_ArrayInitializer,
    Java5_CastExpression,
    Java5_NullLiteral,
    Java5_ArrayAccess,
    Java5_VariableDeclarationExpression,
    Java5_NamedElementRef,
    Java5_NumberLiteral,
    Java5_Assignment,
    Java5_SuperFieldAccess,
    Java5_SuperMethodInvocation,
    Java5_InfixExpression,
    Java5_ArrayCreation,
    Java5_PostfixExpression,
    Java5_BooleanLiteral,
    Java5_ClassInstanceCreation,
    Java5_TypeLiteral,
    Java5_MethodInvocation,
    Java5_CharacterLiteral,
    Java5_FieldAccess,
    Java5_PrefixExpression,
    Java5_InstanceofExpression,
    Java5_ArrayLengthAccess,
    Java5_Annotation,
    Java5_ConditionalExpression,
    VisibilityKind,
    InheritanceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_AbstractTypeDeclaration)


def test_java5_abstracttypedeclaration_constructor_exists():
    assert callable(Java5_AbstractTypeDeclaration.__init__)


def test_java5_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(Java5_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_java5_abstracttypedeclaration_has_qualifiedName():
    assert hasattr(Java5_AbstractTypeDeclaration, "qualifiedName")
    descriptor = None
    for klass in Java5_AbstractTypeDeclaration.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java5_primitivetypeint_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeInt)


def test_java5_primitivetypeint_constructor_exists():
    assert callable(Java5_PrimitiveTypeInt.__init__)


def test_java5_primitivetypeint_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_java5_primitivetypedouble_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeDouble)


def test_java5_primitivetypedouble_constructor_exists():
    assert callable(Java5_PrimitiveTypeDouble.__init__)


def test_java5_primitivetypedouble_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_java5_primitivetypelong_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeLong)


def test_java5_primitivetypelong_constructor_exists():
    assert callable(Java5_PrimitiveTypeLong.__init__)


def test_java5_primitivetypelong_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeLong.__init__)
    params = list(sig.parameters.keys())



def test_java5_primitivetypevoid_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeVoid)


def test_java5_primitivetypevoid_constructor_exists():
    assert callable(Java5_PrimitiveTypeVoid.__init__)


def test_java5_primitivetypevoid_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeVoid.__init__)
    params = list(sig.parameters.keys())



def test_java5_primitivetypechar_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeChar)


def test_java5_primitivetypechar_constructor_exists():
    assert callable(Java5_PrimitiveTypeChar.__init__)


def test_java5_primitivetypechar_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeChar.__init__)
    params = list(sig.parameters.keys())



def test_java5_primitivetypebyte_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeByte)


def test_java5_primitivetypebyte_constructor_exists():
    assert callable(Java5_PrimitiveTypeByte.__init__)


def test_java5_primitivetypebyte_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeByte.__init__)
    params = list(sig.parameters.keys())



def test_java5_primitivetypeshort_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeShort)


def test_java5_primitivetypeshort_constructor_exists():
    assert callable(Java5_PrimitiveTypeShort.__init__)


def test_java5_primitivetypeshort_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeShort.__init__)
    params = list(sig.parameters.keys())



def test_java5_primitivetypefloat_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeFloat)


def test_java5_primitivetypefloat_constructor_exists():
    assert callable(Java5_PrimitiveTypeFloat.__init__)


def test_java5_primitivetypefloat_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_java5_primitivetypeboolean_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeBoolean)


def test_java5_primitivetypeboolean_constructor_exists():
    assert callable(Java5_PrimitiveTypeBoolean.__init__)


def test_java5_primitivetypeboolean_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_java5_model_is_not_abstract():
    assert not inspect.isabstract(Java5_Model)


def test_java5_model_constructor_exists():
    assert callable(Java5_Model.__init__)


def test_java5_model_constructor_args():
    sig = inspect.signature(Java5_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java5_model_has_name():
    assert hasattr(Java5_Model, "name")
    descriptor = None
    for klass in Java5_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java5_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_MethodDeclaration)


def test_java5_methoddeclaration_constructor_exists():
    assert callable(Java5_MethodDeclaration.__init__)


def test_java5_methoddeclaration_constructor_args():
    sig = inspect.signature(Java5_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "constructor" in params, "Missing parameter 'constructor'"

def test_java5_methoddeclaration_has_extraArrayDimensions():
    assert hasattr(Java5_MethodDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in Java5_MethodDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)

def test_java5_methoddeclaration_has_varargs():
    assert hasattr(Java5_MethodDeclaration, "varargs")
    descriptor = None
    for klass in Java5_MethodDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)

def test_java5_methoddeclaration_has_constructor():
    assert hasattr(Java5_MethodDeclaration, "constructor")
    descriptor = None
    for klass in Java5_MethodDeclaration.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)



def test_java5_initializer_is_not_abstract():
    assert not inspect.isabstract(Java5_Initializer)


def test_java5_initializer_constructor_exists():
    assert callable(Java5_Initializer.__init__)


def test_java5_initializer_constructor_args():
    sig = inspect.signature(Java5_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_java5_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(Java5_VariableDeclarationFragment)


def test_java5_variabledeclarationfragment_constructor_exists():
    assert callable(Java5_VariableDeclarationFragment.__init__)


def test_java5_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(Java5_VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_java5_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_FieldDeclaration)


def test_java5_fielddeclaration_constructor_exists():
    assert callable(Java5_FieldDeclaration.__init__)


def test_java5_fielddeclaration_constructor_args():
    sig = inspect.signature(Java5_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_EnumConstantDeclaration)


def test_java5_enumconstantdeclaration_constructor_exists():
    assert callable(Java5_EnumConstantDeclaration.__init__)


def test_java5_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(Java5_EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_SingleVariableDeclaration)


def test_java5_singlevariabledeclaration_constructor_exists():
    assert callable(Java5_SingleVariableDeclaration.__init__)


def test_java5_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(Java5_SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"

def test_java5_singlevariabledeclaration_has_varargs():
    assert hasattr(Java5_SingleVariableDeclaration, "varargs")
    descriptor = None
    for klass in Java5_SingleVariableDeclaration.__mro__:
        if "varargs" in klass.__dict__:
            descriptor = klass.__dict__["varargs"]
            break
    assert isinstance(descriptor, property)



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_InterfaceDeclaration)


def test_java5_interfacedeclaration_constructor_exists():
    assert callable(Java5_InterfaceDeclaration.__init__)


def test_java5_interfacedeclaration_constructor_args():
    sig = inspect.signature(Java5_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_ClassDeclaration)


def test_java5_classdeclaration_constructor_exists():
    assert callable(Java5_ClassDeclaration.__init__)


def test_java5_classdeclaration_constructor_args():
    sig = inspect.signature(Java5_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_orphantype_is_not_abstract():
    assert not inspect.isabstract(OrphanType)


def test_orphantype_constructor_exists():
    assert callable(OrphanType.__init__)


def test_orphantype_constructor_args():
    sig = inspect.signature(OrphanType.__init__)
    params = list(sig.parameters.keys())



def test_java5_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(Java5_WildCardType)


def test_java5_wildcardtype_constructor_exists():
    assert callable(Java5_WildCardType.__init__)


def test_java5_wildcardtype_constructor_args():
    sig = inspect.signature(Java5_WildCardType.__init__)
    params = list(sig.parameters.keys())
    assert "isUpperBound" in params, "Missing parameter 'isUpperBound'"

def test_java5_wildcardtype_has_isUpperBound():
    assert hasattr(Java5_WildCardType, "isUpperBound")
    descriptor = None
    for klass in Java5_WildCardType.__mro__:
        if "isUpperBound" in klass.__dict__:
            descriptor = klass.__dict__["isUpperBound"]
            break
    assert isinstance(descriptor, property)



def test_java5_primitivetype_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveType)


def test_java5_primitivetype_constructor_exists():
    assert callable(Java5_PrimitiveType.__init__)


def test_java5_primitivetype_constructor_args():
    sig = inspect.signature(Java5_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java5_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(Java5_ParameterizedType)


def test_java5_parameterizedtype_constructor_exists():
    assert callable(Java5_ParameterizedType.__init__)


def test_java5_parameterizedtype_constructor_args():
    sig = inspect.signature(Java5_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_java5_arraytype_is_not_abstract():
    assert not inspect.isabstract(Java5_ArrayType)


def test_java5_arraytype_constructor_exists():
    assert callable(Java5_ArrayType.__init__)


def test_java5_arraytype_constructor_args():
    sig = inspect.signature(Java5_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"
    assert "originalName" in params, "Missing parameter 'originalName'"

def test_java5_arraytype_has_dimensions():
    assert hasattr(Java5_ArrayType, "dimensions")
    descriptor = None
    for klass in Java5_ArrayType.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)

def test_java5_arraytype_has_originalName():
    assert hasattr(Java5_ArrayType, "originalName")
    descriptor = None
    for klass in Java5_ArrayType.__mro__:
        if "originalName" in klass.__dict__:
            descriptor = klass.__dict__["originalName"]
            break
    assert isinstance(descriptor, property)



def test_java5_astnode_is_not_abstract():
    assert not inspect.isabstract(Java5_ASTNode)


def test_java5_astnode_constructor_exists():
    assert callable(Java5_ASTNode.__init__)


def test_java5_astnode_constructor_args():
    sig = inspect.signature(Java5_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java5_breakstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_BreakStatement)


def test_java5_breakstatement_constructor_exists():
    assert callable(Java5_BreakStatement.__init__)


def test_java5_breakstatement_constructor_args():
    sig = inspect.signature(Java5_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_SynchronizedStatement)


def test_java5_synchronizedstatement_constructor_exists():
    assert callable(Java5_SynchronizedStatement.__init__)


def test_java5_synchronizedstatement_constructor_args():
    sig = inspect.signature(Java5_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_ifstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_IfStatement)


def test_java5_ifstatement_constructor_exists():
    assert callable(Java5_IfStatement.__init__)


def test_java5_ifstatement_constructor_args():
    sig = inspect.signature(Java5_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_VariableDeclarationStatement)


def test_java5_variabledeclarationstatement_constructor_exists():
    assert callable(Java5_VariableDeclarationStatement.__init__)


def test_java5_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(Java5_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java5_variabledeclarationstatement_has_extraArrayDimensions():
    assert hasattr(Java5_VariableDeclarationStatement, "extraArrayDimensions")
    descriptor = None
    for klass in Java5_VariableDeclarationStatement.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java5_emptystatement_is_not_abstract():
    assert not inspect.isabstract(Java5_EmptyStatement)


def test_java5_emptystatement_constructor_exists():
    assert callable(Java5_EmptyStatement.__init__)


def test_java5_emptystatement_constructor_args():
    sig = inspect.signature(Java5_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5_ConstructorInvocation)


def test_java5_constructorinvocation_constructor_exists():
    assert callable(Java5_ConstructorInvocation.__init__)


def test_java5_constructorinvocation_constructor_args():
    sig = inspect.signature(Java5_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java5_typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_TypeDeclarationStatement)


def test_java5_typedeclarationstatement_constructor_exists():
    assert callable(Java5_TypeDeclarationStatement.__init__)


def test_java5_typedeclarationstatement_constructor_args():
    sig = inspect.signature(Java5_TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_dostatement_is_not_abstract():
    assert not inspect.isabstract(Java5_DoStatement)


def test_java5_dostatement_constructor_exists():
    assert callable(Java5_DoStatement.__init__)


def test_java5_dostatement_constructor_args():
    sig = inspect.signature(Java5_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_switchstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_SwitchStatement)


def test_java5_switchstatement_constructor_exists():
    assert callable(Java5_SwitchStatement.__init__)


def test_java5_switchstatement_constructor_args():
    sig = inspect.signature(Java5_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_whilestatement_is_not_abstract():
    assert not inspect.isabstract(Java5_WhileStatement)


def test_java5_whilestatement_constructor_exists():
    assert callable(Java5_WhileStatement.__init__)


def test_java5_whilestatement_constructor_args():
    sig = inspect.signature(Java5_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_catchclause_is_not_abstract():
    assert not inspect.isabstract(Java5_CatchClause)


def test_java5_catchclause_constructor_exists():
    assert callable(Java5_CatchClause.__init__)


def test_java5_catchclause_constructor_args():
    sig = inspect.signature(Java5_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_java5_trystatement_is_not_abstract():
    assert not inspect.isabstract(Java5_TryStatement)


def test_java5_trystatement_constructor_exists():
    assert callable(Java5_TryStatement.__init__)


def test_java5_trystatement_constructor_args():
    sig = inspect.signature(Java5_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_switchcase_is_not_abstract():
    assert not inspect.isabstract(Java5_SwitchCase)


def test_java5_switchcase_constructor_exists():
    assert callable(Java5_SwitchCase.__init__)


def test_java5_switchcase_constructor_args():
    sig = inspect.signature(Java5_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_java5_switchcase_has_default():
    assert hasattr(Java5_SwitchCase, "default")
    descriptor = None
    for klass in Java5_SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_java5_returnstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_ReturnStatement)


def test_java5_returnstatement_constructor_exists():
    assert callable(Java5_ReturnStatement.__init__)


def test_java5_returnstatement_constructor_args():
    sig = inspect.signature(Java5_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_block_is_not_abstract():
    assert not inspect.isabstract(Java5_Block)


def test_java5_block_constructor_exists():
    assert callable(Java5_Block.__init__)


def test_java5_block_constructor_args():
    sig = inspect.signature(Java5_Block.__init__)
    params = list(sig.parameters.keys())



def test_java5_forstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_ForStatement)


def test_java5_forstatement_constructor_exists():
    assert callable(Java5_ForStatement.__init__)


def test_java5_forstatement_constructor_args():
    sig = inspect.signature(Java5_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_throwstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_ThrowStatement)


def test_java5_throwstatement_constructor_exists():
    assert callable(Java5_ThrowStatement.__init__)


def test_java5_throwstatement_constructor_args():
    sig = inspect.signature(Java5_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_ExpressionStatement)


def test_java5_expressionstatement_constructor_exists():
    assert callable(Java5_ExpressionStatement.__init__)


def test_java5_expressionstatement_constructor_args():
    sig = inspect.signature(Java5_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5_SuperConstructorInvocation)


def test_java5_superconstructorinvocation_constructor_exists():
    assert callable(Java5_SuperConstructorInvocation.__init__)


def test_java5_superconstructorinvocation_constructor_args():
    sig = inspect.signature(Java5_SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java5_continuestatement_is_not_abstract():
    assert not inspect.isabstract(Java5_ContinueStatement)


def test_java5_continuestatement_constructor_exists():
    assert callable(Java5_ContinueStatement.__init__)


def test_java5_continuestatement_constructor_args():
    sig = inspect.signature(Java5_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_EnhancedForStatement)


def test_java5_enhancedforstatement_constructor_exists():
    assert callable(Java5_EnhancedForStatement.__init__)


def test_java5_enhancedforstatement_constructor_args():
    sig = inspect.signature(Java5_EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_assertstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_AssertStatement)


def test_java5_assertstatement_constructor_exists():
    assert callable(Java5_AssertStatement.__init__)


def test_java5_assertstatement_constructor_args():
    sig = inspect.signature(Java5_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_java5_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_LabeledStatement)


def test_java5_labeledstatement_constructor_exists():
    assert callable(Java5_LabeledStatement.__init__)


def test_java5_labeledstatement_constructor_args():
    sig = inspect.signature(Java5_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_java5_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_BodyDeclaration)


def test_java5_bodydeclaration_constructor_exists():
    assert callable(Java5_BodyDeclaration.__init__)


def test_java5_bodydeclaration_constructor_args():
    sig = inspect.signature(Java5_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5_unresolveditem_is_not_abstract():
    assert not inspect.isabstract(Java5_UnresolvedItem)


def test_java5_unresolveditem_constructor_exists():
    assert callable(Java5_UnresolvedItem.__init__)


def test_java5_unresolveditem_constructor_args():
    sig = inspect.signature(Java5_UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_java5_typeparameter_is_not_abstract():
    assert not inspect.isabstract(Java5_TypeParameter)


def test_java5_typeparameter_constructor_exists():
    assert callable(Java5_TypeParameter.__init__)


def test_java5_typeparameter_constructor_args():
    sig = inspect.signature(Java5_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_java5_compilationunit_is_not_abstract():
    assert not inspect.isabstract(Java5_CompilationUnit)


def test_java5_compilationunit_constructor_exists():
    assert callable(Java5_CompilationUnit.__init__)


def test_java5_compilationunit_constructor_args():
    sig = inspect.signature(Java5_CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"

def test_java5_compilationunit_has_originalFilePath():
    assert hasattr(Java5_CompilationUnit, "originalFilePath")
    descriptor = None
    for klass in Java5_CompilationUnit.__mro__:
        if "originalFilePath" in klass.__dict__:
            descriptor = klass.__dict__["originalFilePath"]
            break
    assert isinstance(descriptor, property)



def test_java5_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_PackageDeclaration)


def test_java5_packagedeclaration_constructor_exists():
    assert callable(Java5_PackageDeclaration.__init__)


def test_java5_packagedeclaration_constructor_args():
    sig = inspect.signature(Java5_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_java5_packagedeclaration_has_qualifiedName():
    assert hasattr(Java5_PackageDeclaration, "qualifiedName")
    descriptor = None
    for klass in Java5_PackageDeclaration.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_java5_orphantype_is_not_abstract():
    assert not inspect.isabstract(Java5_OrphanType)


def test_java5_orphantype_constructor_exists():
    assert callable(Java5_OrphanType.__init__)


def test_java5_orphantype_constructor_args():
    sig = inspect.signature(Java5_OrphanType.__init__)
    params = list(sig.parameters.keys())



def test_java5_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_VariableDeclaration)


def test_java5_variabledeclaration_constructor_exists():
    assert callable(Java5_VariableDeclaration.__init__)


def test_java5_variabledeclaration_constructor_args():
    sig = inspect.signature(Java5_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"

def test_java5_variabledeclaration_has_extraArrayDimensions():
    assert hasattr(Java5_VariableDeclaration, "extraArrayDimensions")
    descriptor = None
    for klass in Java5_VariableDeclaration.__mro__:
        if "extraArrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["extraArrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_java5_annotationmembervaluepair_is_not_abstract():
    assert not inspect.isabstract(Java5_AnnotationMemberValuePair)


def test_java5_annotationmembervaluepair_constructor_exists():
    assert callable(Java5_AnnotationMemberValuePair.__init__)


def test_java5_annotationmembervaluepair_constructor_args():
    sig = inspect.signature(Java5_AnnotationMemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_java5_methodref_is_not_abstract():
    assert not inspect.isabstract(Java5_MethodRef)


def test_java5_methodref_constructor_exists():
    assert callable(Java5_MethodRef.__init__)


def test_java5_methodref_constructor_args():
    sig = inspect.signature(Java5_MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_java5_expression_is_not_abstract():
    assert not inspect.isabstract(Java5_Expression)


def test_java5_expression_constructor_exists():
    assert callable(Java5_Expression.__init__)


def test_java5_expression_constructor_args():
    sig = inspect.signature(Java5_Expression.__init__)
    params = list(sig.parameters.keys())



def test_java5_textelement_is_not_abstract():
    assert not inspect.isabstract(Java5_TextElement)


def test_java5_textelement_constructor_exists():
    assert callable(Java5_TextElement.__init__)


def test_java5_textelement_constructor_args():
    sig = inspect.signature(Java5_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_java5_textelement_has_text():
    assert hasattr(Java5_TextElement, "text")
    descriptor = None
    for klass in Java5_TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_java5_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_ImportDeclaration)


def test_java5_importdeclaration_constructor_exists():
    assert callable(Java5_ImportDeclaration.__init__)


def test_java5_importdeclaration_constructor_args():
    sig = inspect.signature(Java5_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_java5_importdeclaration_has_static():
    assert hasattr(Java5_ImportDeclaration, "static")
    descriptor = None
    for klass in Java5_ImportDeclaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_java5_tagelement_is_not_abstract():
    assert not inspect.isabstract(Java5_TagElement)


def test_java5_tagelement_constructor_exists():
    assert callable(Java5_TagElement.__init__)


def test_java5_tagelement_constructor_args():
    sig = inspect.signature(Java5_TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_java5_tagelement_has_tagName():
    assert hasattr(Java5_TagElement, "tagName")
    descriptor = None
    for klass in Java5_TagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_java5_namedelement_is_not_abstract():
    assert not inspect.isabstract(Java5_NamedElement)


def test_java5_namedelement_constructor_exists():
    assert callable(Java5_NamedElement.__init__)


def test_java5_namedelement_constructor_args():
    sig = inspect.signature(Java5_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"

def test_java5_namedelement_has_name():
    assert hasattr(Java5_NamedElement, "name")
    descriptor = None
    for klass in Java5_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java5_namedelement_has_proxy():
    assert hasattr(Java5_NamedElement, "proxy")
    descriptor = None
    for klass in Java5_NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)



def test_java5_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(Java5_MethodRefParameter)


def test_java5_methodrefparameter_constructor_exists():
    assert callable(Java5_MethodRefParameter.__init__)


def test_java5_methodrefparameter_constructor_args():
    sig = inspect.signature(Java5_MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isVarargs" in params, "Missing parameter 'isVarargs'"
    assert "name" in params, "Missing parameter 'name'"

def test_java5_methodrefparameter_has_isVarargs():
    assert hasattr(Java5_MethodRefParameter, "isVarargs")
    descriptor = None
    for klass in Java5_MethodRefParameter.__mro__:
        if "isVarargs" in klass.__dict__:
            descriptor = klass.__dict__["isVarargs"]
            break
    assert isinstance(descriptor, property)

def test_java5_methodrefparameter_has_name():
    assert hasattr(Java5_MethodRefParameter, "name")
    descriptor = None
    for klass in Java5_MethodRefParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java5_modifier_is_not_abstract():
    assert not inspect.isabstract(Java5_Modifier)


def test_java5_modifier_constructor_exists():
    assert callable(Java5_Modifier.__init__)


def test_java5_modifier_constructor_args():
    sig = inspect.signature(Java5_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "inheritance" in params, "Missing parameter 'inheritance'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "native" in params, "Missing parameter 'native'"

def test_java5_modifier_has_static():
    assert hasattr(Java5_Modifier, "static")
    descriptor = None
    for klass in Java5_Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_java5_modifier_has_visibility():
    assert hasattr(Java5_Modifier, "visibility")
    descriptor = None
    for klass in Java5_Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_java5_modifier_has_transient():
    assert hasattr(Java5_Modifier, "transient")
    descriptor = None
    for klass in Java5_Modifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_java5_modifier_has_inheritance():
    assert hasattr(Java5_Modifier, "inheritance")
    descriptor = None
    for klass in Java5_Modifier.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)

def test_java5_modifier_has_volatile():
    assert hasattr(Java5_Modifier, "volatile")
    descriptor = None
    for klass in Java5_Modifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_java5_modifier_has_synchronized():
    assert hasattr(Java5_Modifier, "synchronized")
    descriptor = None
    for klass in Java5_Modifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_java5_modifier_has_strictfp():
    assert hasattr(Java5_Modifier, "strictfp")
    descriptor = None
    for klass in Java5_Modifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_java5_modifier_has_native():
    assert hasattr(Java5_Modifier, "native")
    descriptor = None
    for klass in Java5_Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)



def test_java5_statement_is_not_abstract():
    assert not inspect.isabstract(Java5_Statement)


def test_java5_statement_constructor_exists():
    assert callable(Java5_Statement.__init__)


def test_java5_statement_constructor_args():
    sig = inspect.signature(Java5_Statement.__init__)
    params = list(sig.parameters.keys())



def test_java5_memberref_is_not_abstract():
    assert not inspect.isabstract(Java5_MemberRef)


def test_java5_memberref_constructor_exists():
    assert callable(Java5_MemberRef.__init__)


def test_java5_memberref_constructor_args():
    sig = inspect.signature(Java5_MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_java5_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_AnonymousClassDeclaration)


def test_java5_anonymousclassdeclaration_constructor_exists():
    assert callable(Java5_AnonymousClassDeclaration.__init__)


def test_java5_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(Java5_AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_AnnotationTypeMemberDeclaration)


def test_java5_annotationtypememberdeclaration_constructor_exists():
    assert callable(Java5_AnnotationTypeMemberDeclaration.__init__)


def test_java5_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(Java5_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_AnnotationTypeDeclaration)


def test_java5_annotationtypedeclaration_constructor_exists():
    assert callable(Java5_AnnotationTypeDeclaration.__init__)


def test_java5_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(Java5_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_EnumDeclaration)


def test_java5_enumdeclaration_constructor_exists():
    assert callable(Java5_EnumDeclaration.__init__)


def test_java5_enumdeclaration_constructor_args():
    sig = inspect.signature(Java5_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java5_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_TypeDeclaration)


def test_java5_typedeclaration_constructor_exists():
    assert callable(Java5_TypeDeclaration.__init__)


def test_java5_typedeclaration_constructor_args():
    sig = inspect.signature(Java5_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_java5_stringliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_StringLiteral)


def test_java5_stringliteral_constructor_exists():
    assert callable(Java5_StringLiteral.__init__)


def test_java5_stringliteral_constructor_args():
    sig = inspect.signature(Java5_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "value" in params, "Missing parameter 'value'"

def test_java5_stringliteral_has_escapedValue():
    assert hasattr(Java5_StringLiteral, "escapedValue")
    descriptor = None
    for klass in Java5_StringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)

def test_java5_stringliteral_has_value():
    assert hasattr(Java5_StringLiteral, "value")
    descriptor = None
    for klass in Java5_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java5_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_ParenthesizedExpression)


def test_java5_parenthesizedexpression_constructor_exists():
    assert callable(Java5_ParenthesizedExpression.__init__)


def test_java5_parenthesizedexpression_constructor_args():
    sig = inspect.signature(Java5_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5_thisexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_ThisExpression)


def test_java5_thisexpression_constructor_exists():
    assert callable(Java5_ThisExpression.__init__)


def test_java5_thisexpression_constructor_args():
    sig = inspect.signature(Java5_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(Java5_ArrayInitializer)


def test_java5_arrayinitializer_constructor_exists():
    assert callable(Java5_ArrayInitializer.__init__)


def test_java5_arrayinitializer_constructor_args():
    sig = inspect.signature(Java5_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_java5_castexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_CastExpression)


def test_java5_castexpression_constructor_exists():
    assert callable(Java5_CastExpression.__init__)


def test_java5_castexpression_constructor_args():
    sig = inspect.signature(Java5_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5_nullliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_NullLiteral)


def test_java5_nullliteral_constructor_exists():
    assert callable(Java5_NullLiteral.__init__)


def test_java5_nullliteral_constructor_args():
    sig = inspect.signature(Java5_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java5_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(Java5_ArrayAccess)


def test_java5_arrayaccess_constructor_exists():
    assert callable(Java5_ArrayAccess.__init__)


def test_java5_arrayaccess_constructor_args():
    sig = inspect.signature(Java5_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_java5_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_VariableDeclarationExpression)


def test_java5_variabledeclarationexpression_constructor_exists():
    assert callable(Java5_VariableDeclarationExpression.__init__)


def test_java5_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(Java5_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5_namedelementref_is_not_abstract():
    assert not inspect.isabstract(Java5_NamedElementRef)


def test_java5_namedelementref_constructor_exists():
    assert callable(Java5_NamedElementRef.__init__)


def test_java5_namedelementref_constructor_args():
    sig = inspect.signature(Java5_NamedElementRef.__init__)
    params = list(sig.parameters.keys())



def test_java5_numberliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_NumberLiteral)


def test_java5_numberliteral_constructor_exists():
    assert callable(Java5_NumberLiteral.__init__)


def test_java5_numberliteral_constructor_args():
    sig = inspect.signature(Java5_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "tokenValue" in params, "Missing parameter 'tokenValue'"

def test_java5_numberliteral_has_tokenValue():
    assert hasattr(Java5_NumberLiteral, "tokenValue")
    descriptor = None
    for klass in Java5_NumberLiteral.__mro__:
        if "tokenValue" in klass.__dict__:
            descriptor = klass.__dict__["tokenValue"]
            break
    assert isinstance(descriptor, property)



def test_java5_assignment_is_not_abstract():
    assert not inspect.isabstract(Java5_Assignment)


def test_java5_assignment_constructor_exists():
    assert callable(Java5_Assignment.__init__)


def test_java5_assignment_constructor_args():
    sig = inspect.signature(Java5_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java5_assignment_has_operator():
    assert hasattr(Java5_Assignment, "operator")
    descriptor = None
    for klass in Java5_Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java5_superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(Java5_SuperFieldAccess)


def test_java5_superfieldaccess_constructor_exists():
    assert callable(Java5_SuperFieldAccess.__init__)


def test_java5_superfieldaccess_constructor_args():
    sig = inspect.signature(Java5_SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_java5_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5_SuperMethodInvocation)


def test_java5_supermethodinvocation_constructor_exists():
    assert callable(Java5_SuperMethodInvocation.__init__)


def test_java5_supermethodinvocation_constructor_args():
    sig = inspect.signature(Java5_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java5_infixexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_InfixExpression)


def test_java5_infixexpression_constructor_exists():
    assert callable(Java5_InfixExpression.__init__)


def test_java5_infixexpression_constructor_args():
    sig = inspect.signature(Java5_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java5_infixexpression_has_operator():
    assert hasattr(Java5_InfixExpression, "operator")
    descriptor = None
    for klass in Java5_InfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java5_arraycreation_is_not_abstract():
    assert not inspect.isabstract(Java5_ArrayCreation)


def test_java5_arraycreation_constructor_exists():
    assert callable(Java5_ArrayCreation.__init__)


def test_java5_arraycreation_constructor_args():
    sig = inspect.signature(Java5_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_java5_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_PostfixExpression)


def test_java5_postfixexpression_constructor_exists():
    assert callable(Java5_PostfixExpression.__init__)


def test_java5_postfixexpression_constructor_args():
    sig = inspect.signature(Java5_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java5_postfixexpression_has_operator():
    assert hasattr(Java5_PostfixExpression, "operator")
    descriptor = None
    for klass in Java5_PostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java5_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_BooleanLiteral)


def test_java5_booleanliteral_constructor_exists():
    assert callable(Java5_BooleanLiteral.__init__)


def test_java5_booleanliteral_constructor_args():
    sig = inspect.signature(Java5_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_java5_booleanliteral_has_value():
    assert hasattr(Java5_BooleanLiteral, "value")
    descriptor = None
    for klass in Java5_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_java5_classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(Java5_ClassInstanceCreation)


def test_java5_classinstancecreation_constructor_exists():
    assert callable(Java5_ClassInstanceCreation.__init__)


def test_java5_classinstancecreation_constructor_args():
    sig = inspect.signature(Java5_ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_java5_typeliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_TypeLiteral)


def test_java5_typeliteral_constructor_exists():
    assert callable(Java5_TypeLiteral.__init__)


def test_java5_typeliteral_constructor_args():
    sig = inspect.signature(Java5_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_java5_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5_MethodInvocation)


def test_java5_methodinvocation_constructor_exists():
    assert callable(Java5_MethodInvocation.__init__)


def test_java5_methodinvocation_constructor_args():
    sig = inspect.signature(Java5_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_java5_characterliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_CharacterLiteral)


def test_java5_characterliteral_constructor_exists():
    assert callable(Java5_CharacterLiteral.__init__)


def test_java5_characterliteral_constructor_args():
    sig = inspect.signature(Java5_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_java5_characterliteral_has_value():
    assert hasattr(Java5_CharacterLiteral, "value")
    descriptor = None
    for klass in Java5_CharacterLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_java5_characterliteral_has_escapedValue():
    assert hasattr(Java5_CharacterLiteral, "escapedValue")
    descriptor = None
    for klass in Java5_CharacterLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_java5_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(Java5_FieldAccess)


def test_java5_fieldaccess_constructor_exists():
    assert callable(Java5_FieldAccess.__init__)


def test_java5_fieldaccess_constructor_args():
    sig = inspect.signature(Java5_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_java5_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_PrefixExpression)


def test_java5_prefixexpression_constructor_exists():
    assert callable(Java5_PrefixExpression.__init__)


def test_java5_prefixexpression_constructor_args():
    sig = inspect.signature(Java5_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_java5_prefixexpression_has_operator():
    assert hasattr(Java5_PrefixExpression, "operator")
    descriptor = None
    for klass in Java5_PrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_java5_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_InstanceofExpression)


def test_java5_instanceofexpression_constructor_exists():
    assert callable(Java5_InstanceofExpression.__init__)


def test_java5_instanceofexpression_constructor_args():
    sig = inspect.signature(Java5_InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_java5_arraylengthaccess_is_not_abstract():
    assert not inspect.isabstract(Java5_ArrayLengthAccess)


def test_java5_arraylengthaccess_constructor_exists():
    assert callable(Java5_ArrayLengthAccess.__init__)


def test_java5_arraylengthaccess_constructor_args():
    sig = inspect.signature(Java5_ArrayLengthAccess.__init__)
    params = list(sig.parameters.keys())



def test_java5_annotation_is_not_abstract():
    assert not inspect.isabstract(Java5_Annotation)


def test_java5_annotation_constructor_exists():
    assert callable(Java5_Annotation.__init__)


def test_java5_annotation_constructor_args():
    sig = inspect.signature(Java5_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_java5_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_ConditionalExpression)


def test_java5_conditionalexpression_constructor_exists():
    assert callable(Java5_ConditionalExpression.__init__)


def test_java5_conditionalexpression_constructor_args():
    sig = inspect.signature(Java5_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "protected",
        "none",
        "private",
        "public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_inheritancekind_exists():
    # Check that the Enumeration exists
    assert InheritanceKind is not None

def test_inheritancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceKind]
    expected_literals = [
        "final",
        "abstract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceKind"


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
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
Java5_AbstractTypeDeclaration_strategy = st.builds(
    Java5_AbstractTypeDeclaration,
    qualifiedName=
        safe_text
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
Java5_PrimitiveTypeInt_strategy = st.builds(
    Java5_PrimitiveTypeInt,
)
Java5_PrimitiveTypeDouble_strategy = st.builds(
    Java5_PrimitiveTypeDouble,
)
Java5_PrimitiveTypeLong_strategy = st.builds(
    Java5_PrimitiveTypeLong,
)
Java5_PrimitiveTypeVoid_strategy = st.builds(
    Java5_PrimitiveTypeVoid,
)
Java5_PrimitiveTypeChar_strategy = st.builds(
    Java5_PrimitiveTypeChar,
)
Java5_PrimitiveTypeByte_strategy = st.builds(
    Java5_PrimitiveTypeByte,
)
Java5_PrimitiveTypeShort_strategy = st.builds(
    Java5_PrimitiveTypeShort,
)
Java5_PrimitiveTypeFloat_strategy = st.builds(
    Java5_PrimitiveTypeFloat,
)
Java5_PrimitiveTypeBoolean_strategy = st.builds(
    Java5_PrimitiveTypeBoolean,
)
Java5_Model_strategy = st.builds(
    Java5_Model,
    name=
        safe_text
)
Java5_MethodDeclaration_strategy = st.builds(
    Java5_MethodDeclaration,
    extraArrayDimensions=
        st.integers(),
    varargs=
        st.booleans(),
    constructor=
        st.booleans()
)
Java5_Initializer_strategy = st.builds(
    Java5_Initializer,
)
Java5_VariableDeclarationFragment_strategy = st.builds(
    Java5_VariableDeclarationFragment,
)
Java5_FieldDeclaration_strategy = st.builds(
    Java5_FieldDeclaration,
)
Java5_EnumConstantDeclaration_strategy = st.builds(
    Java5_EnumConstantDeclaration,
)
Java5_SingleVariableDeclaration_strategy = st.builds(
    Java5_SingleVariableDeclaration,
    varargs=
        st.booleans()
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
Java5_InterfaceDeclaration_strategy = st.builds(
    Java5_InterfaceDeclaration,
)
Java5_ClassDeclaration_strategy = st.builds(
    Java5_ClassDeclaration,
)
OrphanType_strategy = st.builds(
    OrphanType,
)
Java5_WildCardType_strategy = st.builds(
    Java5_WildCardType,
    isUpperBound=
        safe_text
)
Java5_PrimitiveType_strategy = st.builds(
    Java5_PrimitiveType,
)
Java5_ParameterizedType_strategy = st.builds(
    Java5_ParameterizedType,
)
Java5_ArrayType_strategy = st.builds(
    Java5_ArrayType,
    dimensions=
        st.integers(),
    originalName=
        safe_text
)
Java5_ASTNode_strategy = st.builds(
    Java5_ASTNode,
)
Statement_strategy = st.builds(
    Statement,
)
Java5_BreakStatement_strategy = st.builds(
    Java5_BreakStatement,
)
Java5_SynchronizedStatement_strategy = st.builds(
    Java5_SynchronizedStatement,
)
Java5_IfStatement_strategy = st.builds(
    Java5_IfStatement,
)
Java5_VariableDeclarationStatement_strategy = st.builds(
    Java5_VariableDeclarationStatement,
    extraArrayDimensions=
        st.integers()
)
Java5_EmptyStatement_strategy = st.builds(
    Java5_EmptyStatement,
)
Java5_ConstructorInvocation_strategy = st.builds(
    Java5_ConstructorInvocation,
)
Java5_TypeDeclarationStatement_strategy = st.builds(
    Java5_TypeDeclarationStatement,
)
Java5_DoStatement_strategy = st.builds(
    Java5_DoStatement,
)
Java5_SwitchStatement_strategy = st.builds(
    Java5_SwitchStatement,
)
Java5_WhileStatement_strategy = st.builds(
    Java5_WhileStatement,
)
Java5_CatchClause_strategy = st.builds(
    Java5_CatchClause,
)
Java5_TryStatement_strategy = st.builds(
    Java5_TryStatement,
)
Java5_SwitchCase_strategy = st.builds(
    Java5_SwitchCase,
    default=
        st.booleans()
)
Java5_ReturnStatement_strategy = st.builds(
    Java5_ReturnStatement,
)
Java5_Block_strategy = st.builds(
    Java5_Block,
)
Java5_ForStatement_strategy = st.builds(
    Java5_ForStatement,
)
Java5_ThrowStatement_strategy = st.builds(
    Java5_ThrowStatement,
)
Java5_ExpressionStatement_strategy = st.builds(
    Java5_ExpressionStatement,
)
Java5_SuperConstructorInvocation_strategy = st.builds(
    Java5_SuperConstructorInvocation,
)
Java5_ContinueStatement_strategy = st.builds(
    Java5_ContinueStatement,
)
Java5_EnhancedForStatement_strategy = st.builds(
    Java5_EnhancedForStatement,
)
Java5_AssertStatement_strategy = st.builds(
    Java5_AssertStatement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Java5_LabeledStatement_strategy = st.builds(
    Java5_LabeledStatement,
)
Java5_BodyDeclaration_strategy = st.builds(
    Java5_BodyDeclaration,
)
Java5_UnresolvedItem_strategy = st.builds(
    Java5_UnresolvedItem,
)
Java5_TypeParameter_strategy = st.builds(
    Java5_TypeParameter,
)
Java5_CompilationUnit_strategy = st.builds(
    Java5_CompilationUnit,
    originalFilePath=
        safe_text
)
Java5_PackageDeclaration_strategy = st.builds(
    Java5_PackageDeclaration,
    qualifiedName=
        safe_text
)
Java5_OrphanType_strategy = st.builds(
    Java5_OrphanType,
)
Java5_VariableDeclaration_strategy = st.builds(
    Java5_VariableDeclaration,
    extraArrayDimensions=
        st.integers()
)
Java5_AnnotationMemberValuePair_strategy = st.builds(
    Java5_AnnotationMemberValuePair,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
Java5_MethodRef_strategy = st.builds(
    Java5_MethodRef,
)
Java5_Expression_strategy = st.builds(
    Java5_Expression,
)
Java5_TextElement_strategy = st.builds(
    Java5_TextElement,
    text=
        safe_text
)
Java5_ImportDeclaration_strategy = st.builds(
    Java5_ImportDeclaration,
    static=
        st.booleans()
)
Java5_TagElement_strategy = st.builds(
    Java5_TagElement,
    tagName=
        safe_text
)
Java5_NamedElement_strategy = st.builds(
    Java5_NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
Java5_MethodRefParameter_strategy = st.builds(
    Java5_MethodRefParameter,
    isVarargs=
        safe_text,
    name=
        safe_text
)
Java5_Modifier_strategy = st.builds(
    Java5_Modifier,
    static=
        st.booleans(),
    visibility=
        safe_text,
    transient=
        st.booleans(),
    inheritance=
        safe_text,
    volatile=
        st.booleans(),
    synchronized=
        st.booleans(),
    strictfp=
        st.booleans(),
    native=
        st.booleans()
)
Java5_Statement_strategy = st.builds(
    Java5_Statement,
)
Java5_MemberRef_strategy = st.builds(
    Java5_MemberRef,
)
Java5_AnonymousClassDeclaration_strategy = st.builds(
    Java5_AnonymousClassDeclaration,
)
Java5_AnnotationTypeMemberDeclaration_strategy = st.builds(
    Java5_AnnotationTypeMemberDeclaration,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
Java5_AnnotationTypeDeclaration_strategy = st.builds(
    Java5_AnnotationTypeDeclaration,
)
Java5_EnumDeclaration_strategy = st.builds(
    Java5_EnumDeclaration,
)
Java5_TypeDeclaration_strategy = st.builds(
    Java5_TypeDeclaration,
)
Expression_strategy = st.builds(
    Expression,
)
Java5_StringLiteral_strategy = st.builds(
    Java5_StringLiteral,
    escapedValue=
        safe_text,
    value=
        safe_text
)
Java5_ParenthesizedExpression_strategy = st.builds(
    Java5_ParenthesizedExpression,
)
Java5_ThisExpression_strategy = st.builds(
    Java5_ThisExpression,
)
Java5_ArrayInitializer_strategy = st.builds(
    Java5_ArrayInitializer,
)
Java5_CastExpression_strategy = st.builds(
    Java5_CastExpression,
)
Java5_NullLiteral_strategy = st.builds(
    Java5_NullLiteral,
)
Java5_ArrayAccess_strategy = st.builds(
    Java5_ArrayAccess,
)
Java5_VariableDeclarationExpression_strategy = st.builds(
    Java5_VariableDeclarationExpression,
)
Java5_NamedElementRef_strategy = st.builds(
    Java5_NamedElementRef,
)
Java5_NumberLiteral_strategy = st.builds(
    Java5_NumberLiteral,
    tokenValue=
        safe_text
)
Java5_Assignment_strategy = st.builds(
    Java5_Assignment,
    operator=
        safe_text
)
Java5_SuperFieldAccess_strategy = st.builds(
    Java5_SuperFieldAccess,
)
Java5_SuperMethodInvocation_strategy = st.builds(
    Java5_SuperMethodInvocation,
)
Java5_InfixExpression_strategy = st.builds(
    Java5_InfixExpression,
    operator=
        safe_text
)
Java5_ArrayCreation_strategy = st.builds(
    Java5_ArrayCreation,
)
Java5_PostfixExpression_strategy = st.builds(
    Java5_PostfixExpression,
    operator=
        safe_text
)
Java5_BooleanLiteral_strategy = st.builds(
    Java5_BooleanLiteral,
    value=
        st.booleans()
)
Java5_ClassInstanceCreation_strategy = st.builds(
    Java5_ClassInstanceCreation,
)
Java5_TypeLiteral_strategy = st.builds(
    Java5_TypeLiteral,
)
Java5_MethodInvocation_strategy = st.builds(
    Java5_MethodInvocation,
)
Java5_CharacterLiteral_strategy = st.builds(
    Java5_CharacterLiteral,
    value=
        safe_text,
    escapedValue=
        safe_text
)
Java5_FieldAccess_strategy = st.builds(
    Java5_FieldAccess,
)
Java5_PrefixExpression_strategy = st.builds(
    Java5_PrefixExpression,
    operator=
        safe_text
)
Java5_InstanceofExpression_strategy = st.builds(
    Java5_InstanceofExpression,
)
Java5_ArrayLengthAccess_strategy = st.builds(
    Java5_ArrayLengthAccess,
)
Java5_Annotation_strategy = st.builds(
    Java5_Annotation,
)
Java5_ConditionalExpression_strategy = st.builds(
    Java5_ConditionalExpression,
)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=Java5_AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java5_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, Java5_AbstractTypeDeclaration)



@given(instance=Java5_AbstractTypeDeclaration_strategy)
def test_java5_abstracttypedeclaration_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=Java5_PrimitiveTypeInt_strategy)
@settings(max_examples=50)
def test_java5_primitivetypeint_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeInt)

@given(instance=Java5_PrimitiveTypeDouble_strategy)
@settings(max_examples=50)
def test_java5_primitivetypedouble_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeDouble)

@given(instance=Java5_PrimitiveTypeLong_strategy)
@settings(max_examples=50)
def test_java5_primitivetypelong_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeLong)

@given(instance=Java5_PrimitiveTypeVoid_strategy)
@settings(max_examples=50)
def test_java5_primitivetypevoid_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeVoid)

@given(instance=Java5_PrimitiveTypeChar_strategy)
@settings(max_examples=50)
def test_java5_primitivetypechar_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeChar)

@given(instance=Java5_PrimitiveTypeByte_strategy)
@settings(max_examples=50)
def test_java5_primitivetypebyte_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeByte)

@given(instance=Java5_PrimitiveTypeShort_strategy)
@settings(max_examples=50)
def test_java5_primitivetypeshort_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeShort)

@given(instance=Java5_PrimitiveTypeFloat_strategy)
@settings(max_examples=50)
def test_java5_primitivetypefloat_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeFloat)

@given(instance=Java5_PrimitiveTypeBoolean_strategy)
@settings(max_examples=50)
def test_java5_primitivetypeboolean_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeBoolean)

@given(instance=Java5_Model_strategy)
@settings(max_examples=50)
def test_java5_model_instantiation(instance):
    assert isinstance(instance, Java5_Model)



@given(instance=Java5_Model_strategy)
def test_java5_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java5_MethodDeclaration_strategy)
@settings(max_examples=50)
def test_java5_methoddeclaration_instantiation(instance):
    assert isinstance(instance, Java5_MethodDeclaration)



@given(instance=Java5_MethodDeclaration_strategy)
def test_java5_methoddeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original



@given(instance=Java5_MethodDeclaration_strategy)
def test_java5_methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original



@given(instance=Java5_MethodDeclaration_strategy)
def test_java5_methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original

@given(instance=Java5_Initializer_strategy)
@settings(max_examples=50)
def test_java5_initializer_instantiation(instance):
    assert isinstance(instance, Java5_Initializer)

@given(instance=Java5_VariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_java5_variabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, Java5_VariableDeclarationFragment)

@given(instance=Java5_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_java5_fielddeclaration_instantiation(instance):
    assert isinstance(instance, Java5_FieldDeclaration)

@given(instance=Java5_EnumConstantDeclaration_strategy)
@settings(max_examples=50)
def test_java5_enumconstantdeclaration_instantiation(instance):
    assert isinstance(instance, Java5_EnumConstantDeclaration)

@given(instance=Java5_SingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_java5_singlevariabledeclaration_instantiation(instance):
    assert isinstance(instance, Java5_SingleVariableDeclaration)



@given(instance=Java5_SingleVariableDeclaration_strategy)
def test_java5_singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=Java5_InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java5_interfacedeclaration_instantiation(instance):
    assert isinstance(instance, Java5_InterfaceDeclaration)

@given(instance=Java5_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_java5_classdeclaration_instantiation(instance):
    assert isinstance(instance, Java5_ClassDeclaration)

@given(instance=OrphanType_strategy)
@settings(max_examples=50)
def test_orphantype_instantiation(instance):
    assert isinstance(instance, OrphanType)

@given(instance=Java5_WildCardType_strategy)
@settings(max_examples=50)
def test_java5_wildcardtype_instantiation(instance):
    assert isinstance(instance, Java5_WildCardType)



@given(instance=Java5_WildCardType_strategy)
def test_java5_wildcardtype_isUpperBound_setter(instance):
    original = instance.isUpperBound
    instance.isUpperBound = original
    assert instance.isUpperBound == original

@given(instance=Java5_PrimitiveType_strategy)
@settings(max_examples=50)
def test_java5_primitivetype_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveType)

@given(instance=Java5_ParameterizedType_strategy)
@settings(max_examples=50)
def test_java5_parameterizedtype_instantiation(instance):
    assert isinstance(instance, Java5_ParameterizedType)

@given(instance=Java5_ArrayType_strategy)
@settings(max_examples=50)
def test_java5_arraytype_instantiation(instance):
    assert isinstance(instance, Java5_ArrayType)



@given(instance=Java5_ArrayType_strategy)
def test_java5_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original



@given(instance=Java5_ArrayType_strategy)
def test_java5_arraytype_originalName_setter(instance):
    original = instance.originalName
    instance.originalName = original
    assert instance.originalName == original

@given(instance=Java5_ASTNode_strategy)
@settings(max_examples=50)
def test_java5_astnode_instantiation(instance):
    assert isinstance(instance, Java5_ASTNode)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=Java5_BreakStatement_strategy)
@settings(max_examples=50)
def test_java5_breakstatement_instantiation(instance):
    assert isinstance(instance, Java5_BreakStatement)

@given(instance=Java5_SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_java5_synchronizedstatement_instantiation(instance):
    assert isinstance(instance, Java5_SynchronizedStatement)

@given(instance=Java5_IfStatement_strategy)
@settings(max_examples=50)
def test_java5_ifstatement_instantiation(instance):
    assert isinstance(instance, Java5_IfStatement)

@given(instance=Java5_VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java5_variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, Java5_VariableDeclarationStatement)



@given(instance=Java5_VariableDeclarationStatement_strategy)
def test_java5_variabledeclarationstatement_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java5_EmptyStatement_strategy)
@settings(max_examples=50)
def test_java5_emptystatement_instantiation(instance):
    assert isinstance(instance, Java5_EmptyStatement)

@given(instance=Java5_ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java5_constructorinvocation_instantiation(instance):
    assert isinstance(instance, Java5_ConstructorInvocation)

@given(instance=Java5_TypeDeclarationStatement_strategy)
@settings(max_examples=50)
def test_java5_typedeclarationstatement_instantiation(instance):
    assert isinstance(instance, Java5_TypeDeclarationStatement)

@given(instance=Java5_DoStatement_strategy)
@settings(max_examples=50)
def test_java5_dostatement_instantiation(instance):
    assert isinstance(instance, Java5_DoStatement)

@given(instance=Java5_SwitchStatement_strategy)
@settings(max_examples=50)
def test_java5_switchstatement_instantiation(instance):
    assert isinstance(instance, Java5_SwitchStatement)

@given(instance=Java5_WhileStatement_strategy)
@settings(max_examples=50)
def test_java5_whilestatement_instantiation(instance):
    assert isinstance(instance, Java5_WhileStatement)

@given(instance=Java5_CatchClause_strategy)
@settings(max_examples=50)
def test_java5_catchclause_instantiation(instance):
    assert isinstance(instance, Java5_CatchClause)

@given(instance=Java5_TryStatement_strategy)
@settings(max_examples=50)
def test_java5_trystatement_instantiation(instance):
    assert isinstance(instance, Java5_TryStatement)

@given(instance=Java5_SwitchCase_strategy)
@settings(max_examples=50)
def test_java5_switchcase_instantiation(instance):
    assert isinstance(instance, Java5_SwitchCase)



@given(instance=Java5_SwitchCase_strategy)
def test_java5_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=Java5_ReturnStatement_strategy)
@settings(max_examples=50)
def test_java5_returnstatement_instantiation(instance):
    assert isinstance(instance, Java5_ReturnStatement)

@given(instance=Java5_Block_strategy)
@settings(max_examples=50)
def test_java5_block_instantiation(instance):
    assert isinstance(instance, Java5_Block)

@given(instance=Java5_ForStatement_strategy)
@settings(max_examples=50)
def test_java5_forstatement_instantiation(instance):
    assert isinstance(instance, Java5_ForStatement)

@given(instance=Java5_ThrowStatement_strategy)
@settings(max_examples=50)
def test_java5_throwstatement_instantiation(instance):
    assert isinstance(instance, Java5_ThrowStatement)

@given(instance=Java5_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_java5_expressionstatement_instantiation(instance):
    assert isinstance(instance, Java5_ExpressionStatement)

@given(instance=Java5_SuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_java5_superconstructorinvocation_instantiation(instance):
    assert isinstance(instance, Java5_SuperConstructorInvocation)

@given(instance=Java5_ContinueStatement_strategy)
@settings(max_examples=50)
def test_java5_continuestatement_instantiation(instance):
    assert isinstance(instance, Java5_ContinueStatement)

@given(instance=Java5_EnhancedForStatement_strategy)
@settings(max_examples=50)
def test_java5_enhancedforstatement_instantiation(instance):
    assert isinstance(instance, Java5_EnhancedForStatement)

@given(instance=Java5_AssertStatement_strategy)
@settings(max_examples=50)
def test_java5_assertstatement_instantiation(instance):
    assert isinstance(instance, Java5_AssertStatement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Java5_LabeledStatement_strategy)
@settings(max_examples=50)
def test_java5_labeledstatement_instantiation(instance):
    assert isinstance(instance, Java5_LabeledStatement)

@given(instance=Java5_BodyDeclaration_strategy)
@settings(max_examples=50)
def test_java5_bodydeclaration_instantiation(instance):
    assert isinstance(instance, Java5_BodyDeclaration)

@given(instance=Java5_UnresolvedItem_strategy)
@settings(max_examples=50)
def test_java5_unresolveditem_instantiation(instance):
    assert isinstance(instance, Java5_UnresolvedItem)

@given(instance=Java5_TypeParameter_strategy)
@settings(max_examples=50)
def test_java5_typeparameter_instantiation(instance):
    assert isinstance(instance, Java5_TypeParameter)

@given(instance=Java5_CompilationUnit_strategy)
@settings(max_examples=50)
def test_java5_compilationunit_instantiation(instance):
    assert isinstance(instance, Java5_CompilationUnit)



@given(instance=Java5_CompilationUnit_strategy)
def test_java5_compilationunit_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original

@given(instance=Java5_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_java5_packagedeclaration_instantiation(instance):
    assert isinstance(instance, Java5_PackageDeclaration)



@given(instance=Java5_PackageDeclaration_strategy)
def test_java5_packagedeclaration_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=Java5_OrphanType_strategy)
@settings(max_examples=50)
def test_java5_orphantype_instantiation(instance):
    assert isinstance(instance, Java5_OrphanType)

@given(instance=Java5_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_java5_variabledeclaration_instantiation(instance):
    assert isinstance(instance, Java5_VariableDeclaration)



@given(instance=Java5_VariableDeclaration_strategy)
def test_java5_variabledeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original

@given(instance=Java5_AnnotationMemberValuePair_strategy)
@settings(max_examples=50)
def test_java5_annotationmembervaluepair_instantiation(instance):
    assert isinstance(instance, Java5_AnnotationMemberValuePair)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=Java5_MethodRef_strategy)
@settings(max_examples=50)
def test_java5_methodref_instantiation(instance):
    assert isinstance(instance, Java5_MethodRef)

@given(instance=Java5_Expression_strategy)
@settings(max_examples=50)
def test_java5_expression_instantiation(instance):
    assert isinstance(instance, Java5_Expression)

@given(instance=Java5_TextElement_strategy)
@settings(max_examples=50)
def test_java5_textelement_instantiation(instance):
    assert isinstance(instance, Java5_TextElement)



@given(instance=Java5_TextElement_strategy)
def test_java5_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Java5_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_java5_importdeclaration_instantiation(instance):
    assert isinstance(instance, Java5_ImportDeclaration)



@given(instance=Java5_ImportDeclaration_strategy)
def test_java5_importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Java5_TagElement_strategy)
@settings(max_examples=50)
def test_java5_tagelement_instantiation(instance):
    assert isinstance(instance, Java5_TagElement)



@given(instance=Java5_TagElement_strategy)
def test_java5_tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=Java5_NamedElement_strategy)
@settings(max_examples=50)
def test_java5_namedelement_instantiation(instance):
    assert isinstance(instance, Java5_NamedElement)



@given(instance=Java5_NamedElement_strategy)
def test_java5_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Java5_NamedElement_strategy)
def test_java5_namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=Java5_MethodRefParameter_strategy)
@settings(max_examples=50)
def test_java5_methodrefparameter_instantiation(instance):
    assert isinstance(instance, Java5_MethodRefParameter)



@given(instance=Java5_MethodRefParameter_strategy)
def test_java5_methodrefparameter_isVarargs_setter(instance):
    original = instance.isVarargs
    instance.isVarargs = original
    assert instance.isVarargs == original



@given(instance=Java5_MethodRefParameter_strategy)
def test_java5_methodrefparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java5_Modifier_strategy)
@settings(max_examples=50)
def test_java5_modifier_instantiation(instance):
    assert isinstance(instance, Java5_Modifier)



@given(instance=Java5_Modifier_strategy)
def test_java5_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=Java5_Modifier_strategy)
def test_java5_modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=Java5_Modifier_strategy)
def test_java5_modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=Java5_Modifier_strategy)
def test_java5_modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original



@given(instance=Java5_Modifier_strategy)
def test_java5_modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=Java5_Modifier_strategy)
def test_java5_modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=Java5_Modifier_strategy)
def test_java5_modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original



@given(instance=Java5_Modifier_strategy)
def test_java5_modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=Java5_Statement_strategy)
@settings(max_examples=50)
def test_java5_statement_instantiation(instance):
    assert isinstance(instance, Java5_Statement)

@given(instance=Java5_MemberRef_strategy)
@settings(max_examples=50)
def test_java5_memberref_instantiation(instance):
    assert isinstance(instance, Java5_MemberRef)

@given(instance=Java5_AnonymousClassDeclaration_strategy)
@settings(max_examples=50)
def test_java5_anonymousclassdeclaration_instantiation(instance):
    assert isinstance(instance, Java5_AnonymousClassDeclaration)

@given(instance=Java5_AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_java5_annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, Java5_AnnotationTypeMemberDeclaration)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=Java5_AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java5_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, Java5_AnnotationTypeDeclaration)

@given(instance=Java5_EnumDeclaration_strategy)
@settings(max_examples=50)
def test_java5_enumdeclaration_instantiation(instance):
    assert isinstance(instance, Java5_EnumDeclaration)

@given(instance=Java5_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_java5_typedeclaration_instantiation(instance):
    assert isinstance(instance, Java5_TypeDeclaration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=Java5_StringLiteral_strategy)
@settings(max_examples=50)
def test_java5_stringliteral_instantiation(instance):
    assert isinstance(instance, Java5_StringLiteral)



@given(instance=Java5_StringLiteral_strategy)
def test_java5_stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original



@given(instance=Java5_StringLiteral_strategy)
def test_java5_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Java5_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_java5_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, Java5_ParenthesizedExpression)

@given(instance=Java5_ThisExpression_strategy)
@settings(max_examples=50)
def test_java5_thisexpression_instantiation(instance):
    assert isinstance(instance, Java5_ThisExpression)

@given(instance=Java5_ArrayInitializer_strategy)
@settings(max_examples=50)
def test_java5_arrayinitializer_instantiation(instance):
    assert isinstance(instance, Java5_ArrayInitializer)

@given(instance=Java5_CastExpression_strategy)
@settings(max_examples=50)
def test_java5_castexpression_instantiation(instance):
    assert isinstance(instance, Java5_CastExpression)

@given(instance=Java5_NullLiteral_strategy)
@settings(max_examples=50)
def test_java5_nullliteral_instantiation(instance):
    assert isinstance(instance, Java5_NullLiteral)

@given(instance=Java5_ArrayAccess_strategy)
@settings(max_examples=50)
def test_java5_arrayaccess_instantiation(instance):
    assert isinstance(instance, Java5_ArrayAccess)

@given(instance=Java5_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_java5_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, Java5_VariableDeclarationExpression)

@given(instance=Java5_NamedElementRef_strategy)
@settings(max_examples=50)
def test_java5_namedelementref_instantiation(instance):
    assert isinstance(instance, Java5_NamedElementRef)

@given(instance=Java5_NumberLiteral_strategy)
@settings(max_examples=50)
def test_java5_numberliteral_instantiation(instance):
    assert isinstance(instance, Java5_NumberLiteral)



@given(instance=Java5_NumberLiteral_strategy)
def test_java5_numberliteral_tokenValue_setter(instance):
    original = instance.tokenValue
    instance.tokenValue = original
    assert instance.tokenValue == original

@given(instance=Java5_Assignment_strategy)
@settings(max_examples=50)
def test_java5_assignment_instantiation(instance):
    assert isinstance(instance, Java5_Assignment)



@given(instance=Java5_Assignment_strategy)
def test_java5_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java5_SuperFieldAccess_strategy)
@settings(max_examples=50)
def test_java5_superfieldaccess_instantiation(instance):
    assert isinstance(instance, Java5_SuperFieldAccess)

@given(instance=Java5_SuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_java5_supermethodinvocation_instantiation(instance):
    assert isinstance(instance, Java5_SuperMethodInvocation)

@given(instance=Java5_InfixExpression_strategy)
@settings(max_examples=50)
def test_java5_infixexpression_instantiation(instance):
    assert isinstance(instance, Java5_InfixExpression)



@given(instance=Java5_InfixExpression_strategy)
def test_java5_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java5_ArrayCreation_strategy)
@settings(max_examples=50)
def test_java5_arraycreation_instantiation(instance):
    assert isinstance(instance, Java5_ArrayCreation)

@given(instance=Java5_PostfixExpression_strategy)
@settings(max_examples=50)
def test_java5_postfixexpression_instantiation(instance):
    assert isinstance(instance, Java5_PostfixExpression)



@given(instance=Java5_PostfixExpression_strategy)
def test_java5_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java5_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_java5_booleanliteral_instantiation(instance):
    assert isinstance(instance, Java5_BooleanLiteral)



@given(instance=Java5_BooleanLiteral_strategy)
def test_java5_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Java5_ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_java5_classinstancecreation_instantiation(instance):
    assert isinstance(instance, Java5_ClassInstanceCreation)

@given(instance=Java5_TypeLiteral_strategy)
@settings(max_examples=50)
def test_java5_typeliteral_instantiation(instance):
    assert isinstance(instance, Java5_TypeLiteral)

@given(instance=Java5_MethodInvocation_strategy)
@settings(max_examples=50)
def test_java5_methodinvocation_instantiation(instance):
    assert isinstance(instance, Java5_MethodInvocation)

@given(instance=Java5_CharacterLiteral_strategy)
@settings(max_examples=50)
def test_java5_characterliteral_instantiation(instance):
    assert isinstance(instance, Java5_CharacterLiteral)



@given(instance=Java5_CharacterLiteral_strategy)
def test_java5_characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Java5_CharacterLiteral_strategy)
def test_java5_characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=Java5_FieldAccess_strategy)
@settings(max_examples=50)
def test_java5_fieldaccess_instantiation(instance):
    assert isinstance(instance, Java5_FieldAccess)

@given(instance=Java5_PrefixExpression_strategy)
@settings(max_examples=50)
def test_java5_prefixexpression_instantiation(instance):
    assert isinstance(instance, Java5_PrefixExpression)



@given(instance=Java5_PrefixExpression_strategy)
def test_java5_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Java5_InstanceofExpression_strategy)
@settings(max_examples=50)
def test_java5_instanceofexpression_instantiation(instance):
    assert isinstance(instance, Java5_InstanceofExpression)

@given(instance=Java5_ArrayLengthAccess_strategy)
@settings(max_examples=50)
def test_java5_arraylengthaccess_instantiation(instance):
    assert isinstance(instance, Java5_ArrayLengthAccess)

@given(instance=Java5_Annotation_strategy)
@settings(max_examples=50)
def test_java5_annotation_instantiation(instance):
    assert isinstance(instance, Java5_Annotation)

@given(instance=Java5_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_java5_conditionalexpression_instantiation(instance):
    assert isinstance(instance, Java5_ConditionalExpression)

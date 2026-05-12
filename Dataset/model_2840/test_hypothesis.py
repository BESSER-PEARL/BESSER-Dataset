import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NameExp,
    backtrackingContentAssistTest_SimpleNameExp,
    backtrackingContentAssistTest_PathNameExp,
    backtrackingContentAssistTest_LetVariable,
    backtrackingContentAssistTest_iteratorAccumulator,
    backtrackingContentAssistTest_iteratorVariable,
    PrimitiveLiteralExp,
    backtrackingContentAssistTest_BooleanLiteralExp,
    backtrackingContentAssistTest_InvalidLiteralExp,
    backtrackingContentAssistTest_StringLiteralExp,
    backtrackingContentAssistTest_NullLiteralExp,
    backtrackingContentAssistTest_NumberLiteralExp,
    backtrackingContentAssistTest_EObject,
    backtrackingContentAssistTest_CollectionLiteralPart,
    backtrackingContentAssistTest_tuplePart,
    CollectionLiteralExp,
    Expression,
    backtrackingContentAssistTest_PreExp,
    backtrackingContentAssistTest_SquareBracketExp,
    backtrackingContentAssistTest_InfixExp,
    backtrackingContentAssistTest_NestedExp,
    backtrackingContentAssistTest_IfExp,
    backtrackingContentAssistTest_CollectionLiteralExp,
    backtrackingContentAssistTest_PrefixExp,
    backtrackingContentAssistTest_LetExp,
    backtrackingContentAssistTest_RoundBracketExp,
    backtrackingContentAssistTest_OclMessage,
    backtrackingContentAssistTest_SelfExp,
    TypeExp,
    backtrackingContentAssistTest_CollectionType,
    backtrackingContentAssistTest_NameExp,
    backtrackingContentAssistTest_TupleType,
    backtrackingContentAssistTest_PrimitiveType,
    backtrackingContentAssistTest_TupleLiteralPart,
    backtrackingContentAssistTest_TupleLiteralExp,
    backtrackingContentAssistTest_PrimitiveLiteralExp,
    PropertyRef,
    backtrackingContentAssistTest_QualifiedPropertyRef,
    OperationRef,
    backtrackingContentAssistTest_QualifiedOperationRef,
    ClassifierRef,
    backtrackingContentAssistTest_QualifiedClassifierRef,
    backtrackingContentAssistTest_PropertyRef,
    backtrackingContentAssistTest_OclMessageArg,
    backtrackingContentAssistTest_NavigatingExp,
    OclMessageArg,
    NavigatingExp,
    backtrackingContentAssistTest_SimplePropertyRef,
    backtrackingContentAssistTest_SimpleOperationRef,
    backtrackingContentAssistTest_SimpleClassifierRef,
    PackageRef,
    backtrackingContentAssistTest_SimplePackageRef,
    backtrackingContentAssistTest_QualifiedPackageRef,
    backtrackingContentAssistTest_Pre,
    backtrackingContentAssistTest_OperationRef,
    backtrackingContentAssistTest_Init,
    backtrackingContentAssistTest_PackageRef,
    backtrackingContentAssistTest_Post,
    backtrackingContentAssistTest_Expression,
    backtrackingContentAssistTest_Body,
    backtrackingContentAssistTest_ContextDecl,
    backtrackingContentAssistTest_PackageDeclaration,
    backtrackingContentAssistTest_Document,
    backtrackingContentAssistTest_Der,
    backtrackingContentAssistTest_TypeExp,
    backtrackingContentAssistTest_Parameter,
    backtrackingContentAssistTest_Definition,
    backtrackingContentAssistTest_Invariant,
    backtrackingContentAssistTest_ClassifierRef,
    ContextDecl,
    backtrackingContentAssistTest_OperationContextDecl,
    backtrackingContentAssistTest_ClassifierContextDecl,
    backtrackingContentAssistTest_PropertyContextDecl,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nameexp_is_not_abstract():
    assert not inspect.isabstract(NameExp)


def test_nameexp_constructor_exists():
    assert callable(NameExp.__init__)


def test_nameexp_constructor_args():
    sig = inspect.signature(NameExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_simplenameexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_SimpleNameExp)


def test_backtrackingcontentassisttest_simplenameexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_SimpleNameExp.__init__)


def test_backtrackingcontentassisttest_simplenameexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_SimpleNameExp.__init__)
    params = list(sig.parameters.keys())
    assert "element" in params, "Missing parameter 'element'"

def test_backtrackingcontentassisttest_simplenameexp_has_element():
    assert hasattr(backtrackingContentAssistTest_SimpleNameExp, "element")
    descriptor = None
    for klass in backtrackingContentAssistTest_SimpleNameExp.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_pathnameexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_PathNameExp)


def test_backtrackingcontentassisttest_pathnameexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_PathNameExp.__init__)


def test_backtrackingcontentassisttest_pathnameexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_PathNameExp.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_backtrackingcontentassisttest_pathnameexp_has_namespace():
    assert hasattr(backtrackingContentAssistTest_PathNameExp, "namespace")
    descriptor = None
    for klass in backtrackingContentAssistTest_PathNameExp.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_letvariable_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_LetVariable)


def test_backtrackingcontentassisttest_letvariable_constructor_exists():
    assert callable(backtrackingContentAssistTest_LetVariable.__init__)


def test_backtrackingcontentassisttest_letvariable_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_LetVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest_letvariable_has_name():
    assert hasattr(backtrackingContentAssistTest_LetVariable, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest_LetVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_iteratoraccumulator_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_iteratorAccumulator)


def test_backtrackingcontentassisttest_iteratoraccumulator_constructor_exists():
    assert callable(backtrackingContentAssistTest_iteratorAccumulator.__init__)


def test_backtrackingcontentassisttest_iteratoraccumulator_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_iteratorAccumulator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest_iteratoraccumulator_has_name():
    assert hasattr(backtrackingContentAssistTest_iteratorAccumulator, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest_iteratorAccumulator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_iteratorvariable_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_iteratorVariable)


def test_backtrackingcontentassisttest_iteratorvariable_constructor_exists():
    assert callable(backtrackingContentAssistTest_iteratorVariable.__init__)


def test_backtrackingcontentassisttest_iteratorvariable_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_iteratorVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest_iteratorvariable_has_name():
    assert hasattr(backtrackingContentAssistTest_iteratorVariable, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest_iteratorVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_BooleanLiteralExp)


def test_backtrackingcontentassisttest_booleanliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_BooleanLiteralExp.__init__)


def test_backtrackingcontentassisttest_booleanliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_backtrackingcontentassisttest_booleanliteralexp_has_isTrue():
    assert hasattr(backtrackingContentAssistTest_BooleanLiteralExp, "isTrue")
    descriptor = None
    for klass in backtrackingContentAssistTest_BooleanLiteralExp.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_InvalidLiteralExp)


def test_backtrackingcontentassisttest_invalidliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_InvalidLiteralExp.__init__)


def test_backtrackingcontentassisttest_invalidliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_StringLiteralExp)


def test_backtrackingcontentassisttest_stringliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_StringLiteralExp.__init__)


def test_backtrackingcontentassisttest_stringliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_backtrackingcontentassisttest_stringliteralexp_has_values():
    assert hasattr(backtrackingContentAssistTest_StringLiteralExp, "values")
    descriptor = None
    for klass in backtrackingContentAssistTest_StringLiteralExp.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_NullLiteralExp)


def test_backtrackingcontentassisttest_nullliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_NullLiteralExp.__init__)


def test_backtrackingcontentassisttest_nullliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_numberliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_NumberLiteralExp)


def test_backtrackingcontentassisttest_numberliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_NumberLiteralExp.__init__)


def test_backtrackingcontentassisttest_numberliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_NumberLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest_numberliteralexp_has_name():
    assert hasattr(backtrackingContentAssistTest_NumberLiteralExp, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest_NumberLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_eobject_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_EObject)


def test_backtrackingcontentassisttest_eobject_constructor_exists():
    assert callable(backtrackingContentAssistTest_EObject.__init__)


def test_backtrackingcontentassisttest_eobject_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_EObject.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_CollectionLiteralPart)


def test_backtrackingcontentassisttest_collectionliteralpart_constructor_exists():
    assert callable(backtrackingContentAssistTest_CollectionLiteralPart.__init__)


def test_backtrackingcontentassisttest_collectionliteralpart_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_tuplepart_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_tuplePart)


def test_backtrackingcontentassisttest_tuplepart_constructor_exists():
    assert callable(backtrackingContentAssistTest_tuplePart.__init__)


def test_backtrackingcontentassisttest_tuplepart_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_tuplePart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest_tuplepart_has_name():
    assert hasattr(backtrackingContentAssistTest_tuplePart, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest_tuplePart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_preexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_PreExp)


def test_backtrackingcontentassisttest_preexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_PreExp.__init__)


def test_backtrackingcontentassisttest_preexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_PreExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_squarebracketexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_SquareBracketExp)


def test_backtrackingcontentassisttest_squarebracketexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_SquareBracketExp.__init__)


def test_backtrackingcontentassisttest_squarebracketexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_SquareBracketExp.__init__)
    params = list(sig.parameters.keys())
    assert "pre" in params, "Missing parameter 'pre'"

def test_backtrackingcontentassisttest_squarebracketexp_has_pre():
    assert hasattr(backtrackingContentAssistTest_SquareBracketExp, "pre")
    descriptor = None
    for klass in backtrackingContentAssistTest_SquareBracketExp.__mro__:
        if "pre" in klass.__dict__:
            descriptor = klass.__dict__["pre"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_infixexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_InfixExp)


def test_backtrackingcontentassisttest_infixexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_InfixExp.__init__)


def test_backtrackingcontentassisttest_infixexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_InfixExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_backtrackingcontentassisttest_infixexp_has_op():
    assert hasattr(backtrackingContentAssistTest_InfixExp, "op")
    descriptor = None
    for klass in backtrackingContentAssistTest_InfixExp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_nestedexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_NestedExp)


def test_backtrackingcontentassisttest_nestedexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_NestedExp.__init__)


def test_backtrackingcontentassisttest_nestedexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_NestedExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_ifexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_IfExp)


def test_backtrackingcontentassisttest_ifexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_IfExp.__init__)


def test_backtrackingcontentassisttest_ifexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_CollectionLiteralExp)


def test_backtrackingcontentassisttest_collectionliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_CollectionLiteralExp.__init__)


def test_backtrackingcontentassisttest_collectionliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_prefixexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_PrefixExp)


def test_backtrackingcontentassisttest_prefixexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_PrefixExp.__init__)


def test_backtrackingcontentassisttest_prefixexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_PrefixExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_backtrackingcontentassisttest_prefixexp_has_op():
    assert hasattr(backtrackingContentAssistTest_PrefixExp, "op")
    descriptor = None
    for klass in backtrackingContentAssistTest_PrefixExp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_letexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_LetExp)


def test_backtrackingcontentassisttest_letexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_LetExp.__init__)


def test_backtrackingcontentassisttest_letexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_roundbracketexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_RoundBracketExp)


def test_backtrackingcontentassisttest_roundbracketexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_RoundBracketExp.__init__)


def test_backtrackingcontentassisttest_roundbracketexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_RoundBracketExp.__init__)
    params = list(sig.parameters.keys())
    assert "pre" in params, "Missing parameter 'pre'"

def test_backtrackingcontentassisttest_roundbracketexp_has_pre():
    assert hasattr(backtrackingContentAssistTest_RoundBracketExp, "pre")
    descriptor = None
    for klass in backtrackingContentAssistTest_RoundBracketExp.__mro__:
        if "pre" in klass.__dict__:
            descriptor = klass.__dict__["pre"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_oclmessage_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_OclMessage)


def test_backtrackingcontentassisttest_oclmessage_constructor_exists():
    assert callable(backtrackingContentAssistTest_OclMessage.__init__)


def test_backtrackingcontentassisttest_oclmessage_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_OclMessage.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "messageName" in params, "Missing parameter 'messageName'"

def test_backtrackingcontentassisttest_oclmessage_has_op():
    assert hasattr(backtrackingContentAssistTest_OclMessage, "op")
    descriptor = None
    for klass in backtrackingContentAssistTest_OclMessage.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_backtrackingcontentassisttest_oclmessage_has_messageName():
    assert hasattr(backtrackingContentAssistTest_OclMessage, "messageName")
    descriptor = None
    for klass in backtrackingContentAssistTest_OclMessage.__mro__:
        if "messageName" in klass.__dict__:
            descriptor = klass.__dict__["messageName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_selfexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_SelfExp)


def test_backtrackingcontentassisttest_selfexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_SelfExp.__init__)


def test_backtrackingcontentassisttest_selfexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_typeexp_is_not_abstract():
    assert not inspect.isabstract(TypeExp)


def test_typeexp_constructor_exists():
    assert callable(TypeExp.__init__)


def test_typeexp_constructor_args():
    sig = inspect.signature(TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_collectiontype_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_CollectionType)


def test_backtrackingcontentassisttest_collectiontype_constructor_exists():
    assert callable(backtrackingContentAssistTest_CollectionType.__init__)


def test_backtrackingcontentassisttest_collectiontype_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "typeIdentifier" in params, "Missing parameter 'typeIdentifier'"

def test_backtrackingcontentassisttest_collectiontype_has_typeIdentifier():
    assert hasattr(backtrackingContentAssistTest_CollectionType, "typeIdentifier")
    descriptor = None
    for klass in backtrackingContentAssistTest_CollectionType.__mro__:
        if "typeIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["typeIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_nameexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_NameExp)


def test_backtrackingcontentassisttest_nameexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_NameExp.__init__)


def test_backtrackingcontentassisttest_nameexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_NameExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_tupletype_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_TupleType)


def test_backtrackingcontentassisttest_tupletype_constructor_exists():
    assert callable(backtrackingContentAssistTest_TupleType.__init__)


def test_backtrackingcontentassisttest_tupletype_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_TupleType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest_tupletype_has_name():
    assert hasattr(backtrackingContentAssistTest_TupleType, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest_TupleType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_primitivetype_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_PrimitiveType)


def test_backtrackingcontentassisttest_primitivetype_constructor_exists():
    assert callable(backtrackingContentAssistTest_PrimitiveType.__init__)


def test_backtrackingcontentassisttest_primitivetype_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest_primitivetype_has_name():
    assert hasattr(backtrackingContentAssistTest_PrimitiveType, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest_PrimitiveType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_TupleLiteralPart)


def test_backtrackingcontentassisttest_tupleliteralpart_constructor_exists():
    assert callable(backtrackingContentAssistTest_TupleLiteralPart.__init__)


def test_backtrackingcontentassisttest_tupleliteralpart_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest_tupleliteralpart_has_name():
    assert hasattr(backtrackingContentAssistTest_TupleLiteralPart, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest_TupleLiteralPart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_TupleLiteralExp)


def test_backtrackingcontentassisttest_tupleliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_TupleLiteralExp.__init__)


def test_backtrackingcontentassisttest_tupleliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_PrimitiveLiteralExp)


def test_backtrackingcontentassisttest_primitiveliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_PrimitiveLiteralExp.__init__)


def test_backtrackingcontentassisttest_primitiveliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_propertyref_is_not_abstract():
    assert not inspect.isabstract(PropertyRef)


def test_propertyref_constructor_exists():
    assert callable(PropertyRef.__init__)


def test_propertyref_constructor_args():
    sig = inspect.signature(PropertyRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_qualifiedpropertyref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_QualifiedPropertyRef)


def test_backtrackingcontentassisttest_qualifiedpropertyref_constructor_exists():
    assert callable(backtrackingContentAssistTest_QualifiedPropertyRef.__init__)


def test_backtrackingcontentassisttest_qualifiedpropertyref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_QualifiedPropertyRef.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_backtrackingcontentassisttest_qualifiedpropertyref_has_namespace():
    assert hasattr(backtrackingContentAssistTest_QualifiedPropertyRef, "namespace")
    descriptor = None
    for klass in backtrackingContentAssistTest_QualifiedPropertyRef.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_operationref_is_not_abstract():
    assert not inspect.isabstract(OperationRef)


def test_operationref_constructor_exists():
    assert callable(OperationRef.__init__)


def test_operationref_constructor_args():
    sig = inspect.signature(OperationRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_qualifiedoperationref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_QualifiedOperationRef)


def test_backtrackingcontentassisttest_qualifiedoperationref_constructor_exists():
    assert callable(backtrackingContentAssistTest_QualifiedOperationRef.__init__)


def test_backtrackingcontentassisttest_qualifiedoperationref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_QualifiedOperationRef.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_backtrackingcontentassisttest_qualifiedoperationref_has_namespace():
    assert hasattr(backtrackingContentAssistTest_QualifiedOperationRef, "namespace")
    descriptor = None
    for klass in backtrackingContentAssistTest_QualifiedOperationRef.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_classifierref_is_not_abstract():
    assert not inspect.isabstract(ClassifierRef)


def test_classifierref_constructor_exists():
    assert callable(ClassifierRef.__init__)


def test_classifierref_constructor_args():
    sig = inspect.signature(ClassifierRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_qualifiedclassifierref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_QualifiedClassifierRef)


def test_backtrackingcontentassisttest_qualifiedclassifierref_constructor_exists():
    assert callable(backtrackingContentAssistTest_QualifiedClassifierRef.__init__)


def test_backtrackingcontentassisttest_qualifiedclassifierref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_QualifiedClassifierRef.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_backtrackingcontentassisttest_qualifiedclassifierref_has_namespace():
    assert hasattr(backtrackingContentAssistTest_QualifiedClassifierRef, "namespace")
    descriptor = None
    for klass in backtrackingContentAssistTest_QualifiedClassifierRef.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_propertyref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_PropertyRef)


def test_backtrackingcontentassisttest_propertyref_constructor_exists():
    assert callable(backtrackingContentAssistTest_PropertyRef.__init__)


def test_backtrackingcontentassisttest_propertyref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_PropertyRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_oclmessagearg_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_OclMessageArg)


def test_backtrackingcontentassisttest_oclmessagearg_constructor_exists():
    assert callable(backtrackingContentAssistTest_OclMessageArg.__init__)


def test_backtrackingcontentassisttest_oclmessagearg_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_OclMessageArg.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_navigatingexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_NavigatingExp)


def test_backtrackingcontentassisttest_navigatingexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_NavigatingExp.__init__)


def test_backtrackingcontentassisttest_navigatingexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_NavigatingExp.__init__)
    params = list(sig.parameters.keys())



def test_oclmessagearg_is_not_abstract():
    assert not inspect.isabstract(OclMessageArg)


def test_oclmessagearg_constructor_exists():
    assert callable(OclMessageArg.__init__)


def test_oclmessagearg_constructor_args():
    sig = inspect.signature(OclMessageArg.__init__)
    params = list(sig.parameters.keys())



def test_navigatingexp_is_not_abstract():
    assert not inspect.isabstract(NavigatingExp)


def test_navigatingexp_constructor_exists():
    assert callable(NavigatingExp.__init__)


def test_navigatingexp_constructor_args():
    sig = inspect.signature(NavigatingExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_simplepropertyref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_SimplePropertyRef)


def test_backtrackingcontentassisttest_simplepropertyref_constructor_exists():
    assert callable(backtrackingContentAssistTest_SimplePropertyRef.__init__)


def test_backtrackingcontentassisttest_simplepropertyref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_SimplePropertyRef.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_backtrackingcontentassisttest_simplepropertyref_has_feature():
    assert hasattr(backtrackingContentAssistTest_SimplePropertyRef, "feature")
    descriptor = None
    for klass in backtrackingContentAssistTest_SimplePropertyRef.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_simpleoperationref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_SimpleOperationRef)


def test_backtrackingcontentassisttest_simpleoperationref_constructor_exists():
    assert callable(backtrackingContentAssistTest_SimpleOperationRef.__init__)


def test_backtrackingcontentassisttest_simpleoperationref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_SimpleOperationRef.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_backtrackingcontentassisttest_simpleoperationref_has_operation():
    assert hasattr(backtrackingContentAssistTest_SimpleOperationRef, "operation")
    descriptor = None
    for klass in backtrackingContentAssistTest_SimpleOperationRef.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_simpleclassifierref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_SimpleClassifierRef)


def test_backtrackingcontentassisttest_simpleclassifierref_constructor_exists():
    assert callable(backtrackingContentAssistTest_SimpleClassifierRef.__init__)


def test_backtrackingcontentassisttest_simpleclassifierref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_SimpleClassifierRef.__init__)
    params = list(sig.parameters.keys())
    assert "classifier" in params, "Missing parameter 'classifier'"

def test_backtrackingcontentassisttest_simpleclassifierref_has_classifier():
    assert hasattr(backtrackingContentAssistTest_SimpleClassifierRef, "classifier")
    descriptor = None
    for klass in backtrackingContentAssistTest_SimpleClassifierRef.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)



def test_packageref_is_not_abstract():
    assert not inspect.isabstract(PackageRef)


def test_packageref_constructor_exists():
    assert callable(PackageRef.__init__)


def test_packageref_constructor_args():
    sig = inspect.signature(PackageRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_simplepackageref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_SimplePackageRef)


def test_backtrackingcontentassisttest_simplepackageref_constructor_exists():
    assert callable(backtrackingContentAssistTest_SimplePackageRef.__init__)


def test_backtrackingcontentassisttest_simplepackageref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_SimplePackageRef.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_backtrackingcontentassisttest_simplepackageref_has_package():
    assert hasattr(backtrackingContentAssistTest_SimplePackageRef, "package")
    descriptor = None
    for klass in backtrackingContentAssistTest_SimplePackageRef.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_qualifiedpackageref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_QualifiedPackageRef)


def test_backtrackingcontentassisttest_qualifiedpackageref_constructor_exists():
    assert callable(backtrackingContentAssistTest_QualifiedPackageRef.__init__)


def test_backtrackingcontentassisttest_qualifiedpackageref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_QualifiedPackageRef.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_backtrackingcontentassisttest_qualifiedpackageref_has_namespace():
    assert hasattr(backtrackingContentAssistTest_QualifiedPackageRef, "namespace")
    descriptor = None
    for klass in backtrackingContentAssistTest_QualifiedPackageRef.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_pre_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_Pre)


def test_backtrackingcontentassisttest_pre_constructor_exists():
    assert callable(backtrackingContentAssistTest_Pre.__init__)


def test_backtrackingcontentassisttest_pre_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_Pre.__init__)
    params = list(sig.parameters.keys())
    assert "constraintName" in params, "Missing parameter 'constraintName'"

def test_backtrackingcontentassisttest_pre_has_constraintName():
    assert hasattr(backtrackingContentAssistTest_Pre, "constraintName")
    descriptor = None
    for klass in backtrackingContentAssistTest_Pre.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_operationref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_OperationRef)


def test_backtrackingcontentassisttest_operationref_constructor_exists():
    assert callable(backtrackingContentAssistTest_OperationRef.__init__)


def test_backtrackingcontentassisttest_operationref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_OperationRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_init_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_Init)


def test_backtrackingcontentassisttest_init_constructor_exists():
    assert callable(backtrackingContentAssistTest_Init.__init__)


def test_backtrackingcontentassisttest_init_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_Init.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_packageref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_PackageRef)


def test_backtrackingcontentassisttest_packageref_constructor_exists():
    assert callable(backtrackingContentAssistTest_PackageRef.__init__)


def test_backtrackingcontentassisttest_packageref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_PackageRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_post_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_Post)


def test_backtrackingcontentassisttest_post_constructor_exists():
    assert callable(backtrackingContentAssistTest_Post.__init__)


def test_backtrackingcontentassisttest_post_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_Post.__init__)
    params = list(sig.parameters.keys())
    assert "constraintName" in params, "Missing parameter 'constraintName'"

def test_backtrackingcontentassisttest_post_has_constraintName():
    assert hasattr(backtrackingContentAssistTest_Post, "constraintName")
    descriptor = None
    for klass in backtrackingContentAssistTest_Post.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_expression_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_Expression)


def test_backtrackingcontentassisttest_expression_constructor_exists():
    assert callable(backtrackingContentAssistTest_Expression.__init__)


def test_backtrackingcontentassisttest_expression_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_Expression.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_body_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_Body)


def test_backtrackingcontentassisttest_body_constructor_exists():
    assert callable(backtrackingContentAssistTest_Body.__init__)


def test_backtrackingcontentassisttest_body_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_Body.__init__)
    params = list(sig.parameters.keys())
    assert "constraintName" in params, "Missing parameter 'constraintName'"

def test_backtrackingcontentassisttest_body_has_constraintName():
    assert hasattr(backtrackingContentAssistTest_Body, "constraintName")
    descriptor = None
    for klass in backtrackingContentAssistTest_Body.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_contextdecl_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_ContextDecl)


def test_backtrackingcontentassisttest_contextdecl_constructor_exists():
    assert callable(backtrackingContentAssistTest_ContextDecl.__init__)


def test_backtrackingcontentassisttest_contextdecl_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_ContextDecl.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_PackageDeclaration)


def test_backtrackingcontentassisttest_packagedeclaration_constructor_exists():
    assert callable(backtrackingContentAssistTest_PackageDeclaration.__init__)


def test_backtrackingcontentassisttest_packagedeclaration_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_document_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_Document)


def test_backtrackingcontentassisttest_document_constructor_exists():
    assert callable(backtrackingContentAssistTest_Document.__init__)


def test_backtrackingcontentassisttest_document_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_Document.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_der_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_Der)


def test_backtrackingcontentassisttest_der_constructor_exists():
    assert callable(backtrackingContentAssistTest_Der.__init__)


def test_backtrackingcontentassisttest_der_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_Der.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_typeexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_TypeExp)


def test_backtrackingcontentassisttest_typeexp_constructor_exists():
    assert callable(backtrackingContentAssistTest_TypeExp.__init__)


def test_backtrackingcontentassisttest_typeexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_parameter_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_Parameter)


def test_backtrackingcontentassisttest_parameter_constructor_exists():
    assert callable(backtrackingContentAssistTest_Parameter.__init__)


def test_backtrackingcontentassisttest_parameter_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest_parameter_has_name():
    assert hasattr(backtrackingContentAssistTest_Parameter, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_definition_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_Definition)


def test_backtrackingcontentassisttest_definition_constructor_exists():
    assert callable(backtrackingContentAssistTest_Definition.__init__)


def test_backtrackingcontentassisttest_definition_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "constrainedName" in params, "Missing parameter 'constrainedName'"
    assert "static" in params, "Missing parameter 'static'"
    assert "constraintName" in params, "Missing parameter 'constraintName'"

def test_backtrackingcontentassisttest_definition_has_constrainedName():
    assert hasattr(backtrackingContentAssistTest_Definition, "constrainedName")
    descriptor = None
    for klass in backtrackingContentAssistTest_Definition.__mro__:
        if "constrainedName" in klass.__dict__:
            descriptor = klass.__dict__["constrainedName"]
            break
    assert isinstance(descriptor, property)

def test_backtrackingcontentassisttest_definition_has_static():
    assert hasattr(backtrackingContentAssistTest_Definition, "static")
    descriptor = None
    for klass in backtrackingContentAssistTest_Definition.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_backtrackingcontentassisttest_definition_has_constraintName():
    assert hasattr(backtrackingContentAssistTest_Definition, "constraintName")
    descriptor = None
    for klass in backtrackingContentAssistTest_Definition.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_invariant_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_Invariant)


def test_backtrackingcontentassisttest_invariant_constructor_exists():
    assert callable(backtrackingContentAssistTest_Invariant.__init__)


def test_backtrackingcontentassisttest_invariant_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_Invariant.__init__)
    params = list(sig.parameters.keys())
    assert "constraintName" in params, "Missing parameter 'constraintName'"

def test_backtrackingcontentassisttest_invariant_has_constraintName():
    assert hasattr(backtrackingContentAssistTest_Invariant, "constraintName")
    descriptor = None
    for klass in backtrackingContentAssistTest_Invariant.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_classifierref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_ClassifierRef)


def test_backtrackingcontentassisttest_classifierref_constructor_exists():
    assert callable(backtrackingContentAssistTest_ClassifierRef.__init__)


def test_backtrackingcontentassisttest_classifierref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_ClassifierRef.__init__)
    params = list(sig.parameters.keys())



def test_contextdecl_is_not_abstract():
    assert not inspect.isabstract(ContextDecl)


def test_contextdecl_constructor_exists():
    assert callable(ContextDecl.__init__)


def test_contextdecl_constructor_args():
    sig = inspect.signature(ContextDecl.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_operationcontextdecl_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_OperationContextDecl)


def test_backtrackingcontentassisttest_operationcontextdecl_constructor_exists():
    assert callable(backtrackingContentAssistTest_OperationContextDecl.__init__)


def test_backtrackingcontentassisttest_operationcontextdecl_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_OperationContextDecl.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest_classifiercontextdecl_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_ClassifierContextDecl)


def test_backtrackingcontentassisttest_classifiercontextdecl_constructor_exists():
    assert callable(backtrackingContentAssistTest_ClassifierContextDecl.__init__)


def test_backtrackingcontentassisttest_classifiercontextdecl_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_ClassifierContextDecl.__init__)
    params = list(sig.parameters.keys())
    assert "selfName" in params, "Missing parameter 'selfName'"

def test_backtrackingcontentassisttest_classifiercontextdecl_has_selfName():
    assert hasattr(backtrackingContentAssistTest_ClassifierContextDecl, "selfName")
    descriptor = None
    for klass in backtrackingContentAssistTest_ClassifierContextDecl.__mro__:
        if "selfName" in klass.__dict__:
            descriptor = klass.__dict__["selfName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest_propertycontextdecl_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest_PropertyContextDecl)


def test_backtrackingcontentassisttest_propertycontextdecl_constructor_exists():
    assert callable(backtrackingContentAssistTest_PropertyContextDecl.__init__)


def test_backtrackingcontentassisttest_propertycontextdecl_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest_PropertyContextDecl.__init__)
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
NameExp_strategy = st.builds(
    NameExp,
)
backtrackingContentAssistTest_SimpleNameExp_strategy = st.builds(
    backtrackingContentAssistTest_SimpleNameExp,
    element=
        safe_text
)
backtrackingContentAssistTest_PathNameExp_strategy = st.builds(
    backtrackingContentAssistTest_PathNameExp,
    namespace=
        safe_text
)
backtrackingContentAssistTest_LetVariable_strategy = st.builds(
    backtrackingContentAssistTest_LetVariable,
    name=
        safe_text
)
backtrackingContentAssistTest_iteratorAccumulator_strategy = st.builds(
    backtrackingContentAssistTest_iteratorAccumulator,
    name=
        safe_text
)
backtrackingContentAssistTest_iteratorVariable_strategy = st.builds(
    backtrackingContentAssistTest_iteratorVariable,
    name=
        safe_text
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
backtrackingContentAssistTest_BooleanLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest_BooleanLiteralExp,
    isTrue=
        st.booleans()
)
backtrackingContentAssistTest_InvalidLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest_InvalidLiteralExp,
)
backtrackingContentAssistTest_StringLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest_StringLiteralExp,
    values=
        safe_text
)
backtrackingContentAssistTest_NullLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest_NullLiteralExp,
)
backtrackingContentAssistTest_NumberLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest_NumberLiteralExp,
    name=
        safe_text
)
backtrackingContentAssistTest_EObject_strategy = st.builds(
    backtrackingContentAssistTest_EObject,
)
backtrackingContentAssistTest_CollectionLiteralPart_strategy = st.builds(
    backtrackingContentAssistTest_CollectionLiteralPart,
)
backtrackingContentAssistTest_tuplePart_strategy = st.builds(
    backtrackingContentAssistTest_tuplePart,
    name=
        safe_text
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
Expression_strategy = st.builds(
    Expression,
)
backtrackingContentAssistTest_PreExp_strategy = st.builds(
    backtrackingContentAssistTest_PreExp,
)
backtrackingContentAssistTest_SquareBracketExp_strategy = st.builds(
    backtrackingContentAssistTest_SquareBracketExp,
    pre=
        st.booleans()
)
backtrackingContentAssistTest_InfixExp_strategy = st.builds(
    backtrackingContentAssistTest_InfixExp,
    op=
        safe_text
)
backtrackingContentAssistTest_NestedExp_strategy = st.builds(
    backtrackingContentAssistTest_NestedExp,
)
backtrackingContentAssistTest_IfExp_strategy = st.builds(
    backtrackingContentAssistTest_IfExp,
)
backtrackingContentAssistTest_CollectionLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest_CollectionLiteralExp,
)
backtrackingContentAssistTest_PrefixExp_strategy = st.builds(
    backtrackingContentAssistTest_PrefixExp,
    op=
        safe_text
)
backtrackingContentAssistTest_LetExp_strategy = st.builds(
    backtrackingContentAssistTest_LetExp,
)
backtrackingContentAssistTest_RoundBracketExp_strategy = st.builds(
    backtrackingContentAssistTest_RoundBracketExp,
    pre=
        st.booleans()
)
backtrackingContentAssistTest_OclMessage_strategy = st.builds(
    backtrackingContentAssistTest_OclMessage,
    op=
        safe_text,
    messageName=
        safe_text
)
backtrackingContentAssistTest_SelfExp_strategy = st.builds(
    backtrackingContentAssistTest_SelfExp,
)
TypeExp_strategy = st.builds(
    TypeExp,
)
backtrackingContentAssistTest_CollectionType_strategy = st.builds(
    backtrackingContentAssistTest_CollectionType,
    typeIdentifier=
        safe_text
)
backtrackingContentAssistTest_NameExp_strategy = st.builds(
    backtrackingContentAssistTest_NameExp,
)
backtrackingContentAssistTest_TupleType_strategy = st.builds(
    backtrackingContentAssistTest_TupleType,
    name=
        safe_text
)
backtrackingContentAssistTest_PrimitiveType_strategy = st.builds(
    backtrackingContentAssistTest_PrimitiveType,
    name=
        safe_text
)
backtrackingContentAssistTest_TupleLiteralPart_strategy = st.builds(
    backtrackingContentAssistTest_TupleLiteralPart,
    name=
        safe_text
)
backtrackingContentAssistTest_TupleLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest_TupleLiteralExp,
)
backtrackingContentAssistTest_PrimitiveLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest_PrimitiveLiteralExp,
)
PropertyRef_strategy = st.builds(
    PropertyRef,
)
backtrackingContentAssistTest_QualifiedPropertyRef_strategy = st.builds(
    backtrackingContentAssistTest_QualifiedPropertyRef,
    namespace=
        safe_text
)
OperationRef_strategy = st.builds(
    OperationRef,
)
backtrackingContentAssistTest_QualifiedOperationRef_strategy = st.builds(
    backtrackingContentAssistTest_QualifiedOperationRef,
    namespace=
        safe_text
)
ClassifierRef_strategy = st.builds(
    ClassifierRef,
)
backtrackingContentAssistTest_QualifiedClassifierRef_strategy = st.builds(
    backtrackingContentAssistTest_QualifiedClassifierRef,
    namespace=
        safe_text
)
backtrackingContentAssistTest_PropertyRef_strategy = st.builds(
    backtrackingContentAssistTest_PropertyRef,
)
backtrackingContentAssistTest_OclMessageArg_strategy = st.builds(
    backtrackingContentAssistTest_OclMessageArg,
)
backtrackingContentAssistTest_NavigatingExp_strategy = st.builds(
    backtrackingContentAssistTest_NavigatingExp,
)
OclMessageArg_strategy = st.builds(
    OclMessageArg,
)
NavigatingExp_strategy = st.builds(
    NavigatingExp,
)
backtrackingContentAssistTest_SimplePropertyRef_strategy = st.builds(
    backtrackingContentAssistTest_SimplePropertyRef,
    feature=
        safe_text
)
backtrackingContentAssistTest_SimpleOperationRef_strategy = st.builds(
    backtrackingContentAssistTest_SimpleOperationRef,
    operation=
        safe_text
)
backtrackingContentAssistTest_SimpleClassifierRef_strategy = st.builds(
    backtrackingContentAssistTest_SimpleClassifierRef,
    classifier=
        safe_text
)
PackageRef_strategy = st.builds(
    PackageRef,
)
backtrackingContentAssistTest_SimplePackageRef_strategy = st.builds(
    backtrackingContentAssistTest_SimplePackageRef,
    package=
        safe_text
)
backtrackingContentAssistTest_QualifiedPackageRef_strategy = st.builds(
    backtrackingContentAssistTest_QualifiedPackageRef,
    namespace=
        safe_text
)
backtrackingContentAssistTest_Pre_strategy = st.builds(
    backtrackingContentAssistTest_Pre,
    constraintName=
        safe_text
)
backtrackingContentAssistTest_OperationRef_strategy = st.builds(
    backtrackingContentAssistTest_OperationRef,
)
backtrackingContentAssistTest_Init_strategy = st.builds(
    backtrackingContentAssistTest_Init,
)
backtrackingContentAssistTest_PackageRef_strategy = st.builds(
    backtrackingContentAssistTest_PackageRef,
)
backtrackingContentAssistTest_Post_strategy = st.builds(
    backtrackingContentAssistTest_Post,
    constraintName=
        safe_text
)
backtrackingContentAssistTest_Expression_strategy = st.builds(
    backtrackingContentAssistTest_Expression,
)
backtrackingContentAssistTest_Body_strategy = st.builds(
    backtrackingContentAssistTest_Body,
    constraintName=
        safe_text
)
backtrackingContentAssistTest_ContextDecl_strategy = st.builds(
    backtrackingContentAssistTest_ContextDecl,
)
backtrackingContentAssistTest_PackageDeclaration_strategy = st.builds(
    backtrackingContentAssistTest_PackageDeclaration,
)
backtrackingContentAssistTest_Document_strategy = st.builds(
    backtrackingContentAssistTest_Document,
)
backtrackingContentAssistTest_Der_strategy = st.builds(
    backtrackingContentAssistTest_Der,
)
backtrackingContentAssistTest_TypeExp_strategy = st.builds(
    backtrackingContentAssistTest_TypeExp,
)
backtrackingContentAssistTest_Parameter_strategy = st.builds(
    backtrackingContentAssistTest_Parameter,
    name=
        safe_text
)
backtrackingContentAssistTest_Definition_strategy = st.builds(
    backtrackingContentAssistTest_Definition,
    constrainedName=
        safe_text,
    static=
        st.booleans(),
    constraintName=
        safe_text
)
backtrackingContentAssistTest_Invariant_strategy = st.builds(
    backtrackingContentAssistTest_Invariant,
    constraintName=
        safe_text
)
backtrackingContentAssistTest_ClassifierRef_strategy = st.builds(
    backtrackingContentAssistTest_ClassifierRef,
)
ContextDecl_strategy = st.builds(
    ContextDecl,
)
backtrackingContentAssistTest_OperationContextDecl_strategy = st.builds(
    backtrackingContentAssistTest_OperationContextDecl,
)
backtrackingContentAssistTest_ClassifierContextDecl_strategy = st.builds(
    backtrackingContentAssistTest_ClassifierContextDecl,
    selfName=
        safe_text
)
backtrackingContentAssistTest_PropertyContextDecl_strategy = st.builds(
    backtrackingContentAssistTest_PropertyContextDecl,
)

@given(instance=NameExp_strategy)
@settings(max_examples=50)
def test_nameexp_instantiation(instance):
    assert isinstance(instance, NameExp)

@given(instance=backtrackingContentAssistTest_SimpleNameExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_simplenameexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_SimpleNameExp)



@given(instance=backtrackingContentAssistTest_SimpleNameExp_strategy)
def test_backtrackingcontentassisttest_simplenameexp_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=backtrackingContentAssistTest_PathNameExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_pathnameexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_PathNameExp)



@given(instance=backtrackingContentAssistTest_PathNameExp_strategy)
def test_backtrackingcontentassisttest_pathnameexp_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=backtrackingContentAssistTest_LetVariable_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_letvariable_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_LetVariable)



@given(instance=backtrackingContentAssistTest_LetVariable_strategy)
def test_backtrackingcontentassisttest_letvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest_iteratorAccumulator_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_iteratoraccumulator_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_iteratorAccumulator)



@given(instance=backtrackingContentAssistTest_iteratorAccumulator_strategy)
def test_backtrackingcontentassisttest_iteratoraccumulator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest_iteratorVariable_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_iteratorvariable_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_iteratorVariable)



@given(instance=backtrackingContentAssistTest_iteratorVariable_strategy)
def test_backtrackingcontentassisttest_iteratorvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=backtrackingContentAssistTest_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_BooleanLiteralExp)



@given(instance=backtrackingContentAssistTest_BooleanLiteralExp_strategy)
def test_backtrackingcontentassisttest_booleanliteralexp_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=backtrackingContentAssistTest_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_InvalidLiteralExp)

@given(instance=backtrackingContentAssistTest_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_stringliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_StringLiteralExp)



@given(instance=backtrackingContentAssistTest_StringLiteralExp_strategy)
def test_backtrackingcontentassisttest_stringliteralexp_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=backtrackingContentAssistTest_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_nullliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_NullLiteralExp)

@given(instance=backtrackingContentAssistTest_NumberLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_numberliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_NumberLiteralExp)



@given(instance=backtrackingContentAssistTest_NumberLiteralExp_strategy)
def test_backtrackingcontentassisttest_numberliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest_EObject_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_eobject_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_EObject)

@given(instance=backtrackingContentAssistTest_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_CollectionLiteralPart)

@given(instance=backtrackingContentAssistTest_tuplePart_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_tuplepart_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_tuplePart)



@given(instance=backtrackingContentAssistTest_tuplePart_strategy)
def test_backtrackingcontentassisttest_tuplepart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=backtrackingContentAssistTest_PreExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_preexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_PreExp)

@given(instance=backtrackingContentAssistTest_SquareBracketExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_squarebracketexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_SquareBracketExp)



@given(instance=backtrackingContentAssistTest_SquareBracketExp_strategy)
def test_backtrackingcontentassisttest_squarebracketexp_pre_setter(instance):
    original = instance.pre
    instance.pre = original
    assert instance.pre == original

@given(instance=backtrackingContentAssistTest_InfixExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_infixexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_InfixExp)



@given(instance=backtrackingContentAssistTest_InfixExp_strategy)
def test_backtrackingcontentassisttest_infixexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=backtrackingContentAssistTest_NestedExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_nestedexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_NestedExp)

@given(instance=backtrackingContentAssistTest_IfExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_ifexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_IfExp)

@given(instance=backtrackingContentAssistTest_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_CollectionLiteralExp)

@given(instance=backtrackingContentAssistTest_PrefixExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_prefixexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_PrefixExp)



@given(instance=backtrackingContentAssistTest_PrefixExp_strategy)
def test_backtrackingcontentassisttest_prefixexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=backtrackingContentAssistTest_LetExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_letexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_LetExp)

@given(instance=backtrackingContentAssistTest_RoundBracketExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_roundbracketexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_RoundBracketExp)



@given(instance=backtrackingContentAssistTest_RoundBracketExp_strategy)
def test_backtrackingcontentassisttest_roundbracketexp_pre_setter(instance):
    original = instance.pre
    instance.pre = original
    assert instance.pre == original

@given(instance=backtrackingContentAssistTest_OclMessage_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_oclmessage_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_OclMessage)



@given(instance=backtrackingContentAssistTest_OclMessage_strategy)
def test_backtrackingcontentassisttest_oclmessage_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=backtrackingContentAssistTest_OclMessage_strategy)
def test_backtrackingcontentassisttest_oclmessage_messageName_setter(instance):
    original = instance.messageName
    instance.messageName = original
    assert instance.messageName == original

@given(instance=backtrackingContentAssistTest_SelfExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_selfexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_SelfExp)

@given(instance=TypeExp_strategy)
@settings(max_examples=50)
def test_typeexp_instantiation(instance):
    assert isinstance(instance, TypeExp)

@given(instance=backtrackingContentAssistTest_CollectionType_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_collectiontype_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_CollectionType)



@given(instance=backtrackingContentAssistTest_CollectionType_strategy)
def test_backtrackingcontentassisttest_collectiontype_typeIdentifier_setter(instance):
    original = instance.typeIdentifier
    instance.typeIdentifier = original
    assert instance.typeIdentifier == original

@given(instance=backtrackingContentAssistTest_NameExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_nameexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_NameExp)

@given(instance=backtrackingContentAssistTest_TupleType_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_tupletype_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_TupleType)



@given(instance=backtrackingContentAssistTest_TupleType_strategy)
def test_backtrackingcontentassisttest_tupletype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest_PrimitiveType_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_primitivetype_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_PrimitiveType)



@given(instance=backtrackingContentAssistTest_PrimitiveType_strategy)
def test_backtrackingcontentassisttest_primitivetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_TupleLiteralPart)



@given(instance=backtrackingContentAssistTest_TupleLiteralPart_strategy)
def test_backtrackingcontentassisttest_tupleliteralpart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_TupleLiteralExp)

@given(instance=backtrackingContentAssistTest_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_PrimitiveLiteralExp)

@given(instance=PropertyRef_strategy)
@settings(max_examples=50)
def test_propertyref_instantiation(instance):
    assert isinstance(instance, PropertyRef)

@given(instance=backtrackingContentAssistTest_QualifiedPropertyRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_qualifiedpropertyref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_QualifiedPropertyRef)



@given(instance=backtrackingContentAssistTest_QualifiedPropertyRef_strategy)
def test_backtrackingcontentassisttest_qualifiedpropertyref_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=OperationRef_strategy)
@settings(max_examples=50)
def test_operationref_instantiation(instance):
    assert isinstance(instance, OperationRef)

@given(instance=backtrackingContentAssistTest_QualifiedOperationRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_qualifiedoperationref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_QualifiedOperationRef)



@given(instance=backtrackingContentAssistTest_QualifiedOperationRef_strategy)
def test_backtrackingcontentassisttest_qualifiedoperationref_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=ClassifierRef_strategy)
@settings(max_examples=50)
def test_classifierref_instantiation(instance):
    assert isinstance(instance, ClassifierRef)

@given(instance=backtrackingContentAssistTest_QualifiedClassifierRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_qualifiedclassifierref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_QualifiedClassifierRef)



@given(instance=backtrackingContentAssistTest_QualifiedClassifierRef_strategy)
def test_backtrackingcontentassisttest_qualifiedclassifierref_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=backtrackingContentAssistTest_PropertyRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_propertyref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_PropertyRef)

@given(instance=backtrackingContentAssistTest_OclMessageArg_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_oclmessagearg_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_OclMessageArg)

@given(instance=backtrackingContentAssistTest_NavigatingExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_navigatingexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_NavigatingExp)

@given(instance=OclMessageArg_strategy)
@settings(max_examples=50)
def test_oclmessagearg_instantiation(instance):
    assert isinstance(instance, OclMessageArg)

@given(instance=NavigatingExp_strategy)
@settings(max_examples=50)
def test_navigatingexp_instantiation(instance):
    assert isinstance(instance, NavigatingExp)

@given(instance=backtrackingContentAssistTest_SimplePropertyRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_simplepropertyref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_SimplePropertyRef)



@given(instance=backtrackingContentAssistTest_SimplePropertyRef_strategy)
def test_backtrackingcontentassisttest_simplepropertyref_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=backtrackingContentAssistTest_SimpleOperationRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_simpleoperationref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_SimpleOperationRef)



@given(instance=backtrackingContentAssistTest_SimpleOperationRef_strategy)
def test_backtrackingcontentassisttest_simpleoperationref_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=backtrackingContentAssistTest_SimpleClassifierRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_simpleclassifierref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_SimpleClassifierRef)



@given(instance=backtrackingContentAssistTest_SimpleClassifierRef_strategy)
def test_backtrackingcontentassisttest_simpleclassifierref_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=PackageRef_strategy)
@settings(max_examples=50)
def test_packageref_instantiation(instance):
    assert isinstance(instance, PackageRef)

@given(instance=backtrackingContentAssistTest_SimplePackageRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_simplepackageref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_SimplePackageRef)



@given(instance=backtrackingContentAssistTest_SimplePackageRef_strategy)
def test_backtrackingcontentassisttest_simplepackageref_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=backtrackingContentAssistTest_QualifiedPackageRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_qualifiedpackageref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_QualifiedPackageRef)



@given(instance=backtrackingContentAssistTest_QualifiedPackageRef_strategy)
def test_backtrackingcontentassisttest_qualifiedpackageref_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=backtrackingContentAssistTest_Pre_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_pre_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_Pre)



@given(instance=backtrackingContentAssistTest_Pre_strategy)
def test_backtrackingcontentassisttest_pre_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=backtrackingContentAssistTest_OperationRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_operationref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_OperationRef)

@given(instance=backtrackingContentAssistTest_Init_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_init_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_Init)

@given(instance=backtrackingContentAssistTest_PackageRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_packageref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_PackageRef)

@given(instance=backtrackingContentAssistTest_Post_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_post_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_Post)



@given(instance=backtrackingContentAssistTest_Post_strategy)
def test_backtrackingcontentassisttest_post_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=backtrackingContentAssistTest_Expression_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_expression_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_Expression)

@given(instance=backtrackingContentAssistTest_Body_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_body_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_Body)



@given(instance=backtrackingContentAssistTest_Body_strategy)
def test_backtrackingcontentassisttest_body_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=backtrackingContentAssistTest_ContextDecl_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_contextdecl_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_ContextDecl)

@given(instance=backtrackingContentAssistTest_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_packagedeclaration_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_PackageDeclaration)

@given(instance=backtrackingContentAssistTest_Document_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_document_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_Document)

@given(instance=backtrackingContentAssistTest_Der_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_der_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_Der)

@given(instance=backtrackingContentAssistTest_TypeExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_typeexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_TypeExp)

@given(instance=backtrackingContentAssistTest_Parameter_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_parameter_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_Parameter)



@given(instance=backtrackingContentAssistTest_Parameter_strategy)
def test_backtrackingcontentassisttest_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest_Definition_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_definition_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_Definition)



@given(instance=backtrackingContentAssistTest_Definition_strategy)
def test_backtrackingcontentassisttest_definition_constrainedName_setter(instance):
    original = instance.constrainedName
    instance.constrainedName = original
    assert instance.constrainedName == original



@given(instance=backtrackingContentAssistTest_Definition_strategy)
def test_backtrackingcontentassisttest_definition_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=backtrackingContentAssistTest_Definition_strategy)
def test_backtrackingcontentassisttest_definition_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=backtrackingContentAssistTest_Invariant_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_invariant_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_Invariant)



@given(instance=backtrackingContentAssistTest_Invariant_strategy)
def test_backtrackingcontentassisttest_invariant_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=backtrackingContentAssistTest_ClassifierRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_classifierref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_ClassifierRef)

@given(instance=ContextDecl_strategy)
@settings(max_examples=50)
def test_contextdecl_instantiation(instance):
    assert isinstance(instance, ContextDecl)

@given(instance=backtrackingContentAssistTest_OperationContextDecl_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_operationcontextdecl_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_OperationContextDecl)

@given(instance=backtrackingContentAssistTest_ClassifierContextDecl_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_classifiercontextdecl_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_ClassifierContextDecl)



@given(instance=backtrackingContentAssistTest_ClassifierContextDecl_strategy)
def test_backtrackingcontentassisttest_classifiercontextdecl_selfName_setter(instance):
    original = instance.selfName
    instance.selfName = original
    assert instance.selfName == original

@given(instance=backtrackingContentAssistTest_PropertyContextDecl_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest_propertycontextdecl_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest_PropertyContextDecl)

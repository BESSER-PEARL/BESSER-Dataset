import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    essentialoclcs_Type,
    BinaryOperatorCS,
    essentialoclcs_NavigationOperatorCS,
    essentialoclcs_PathNameCS,
    AbstractNameExpCS,
    essentialoclcs_NamedExpCS,
    essentialoclcs_NameExpCS,
    VariableCS,
    essentialoclcs_TupleLiteralPartCS,
    SpecificationCS,
    essentialoclcs_ExpSpecificationCS,
    RootCS,
    NamedElementCS,
    essentialoclcs_VariableCS,
    essentialoclcs_ContextCS,
    essentialoclcs_Property,
    NamedExpCS,
    essentialoclcs_InvocationExpCS,
    essentialoclcs_IndexExpCS,
    essentialoclcs_ConstructorExpCS,
    essentialoclcs_TypedRefCS,
    Nameable,
    TypedRefCS,
    essentialoclcs_TypeNameExpCS,
    ModelElementCS,
    essentialoclcs_NavigatingArgCS,
    essentialoclcs_ConstructorPartCS,
    essentialoclcs_CollectionLiteralPartCS,
    essentialoclcs_CollectionTypeCS,
    LiteralExpCS,
    essentialoclcs_TupleLiteralExpCS,
    essentialoclcs_TypeLiteralExpCS,
    essentialoclcs_PrimitiveLiteralExpCS,
    essentialoclcs_CollectionLiteralExpCS,
    PrimitiveLiteralExpCS,
    essentialoclcs_NullLiteralExpCS,
    essentialoclcs_UnlimitedNaturalLiteralExpCS,
    essentialoclcs_NumberLiteralExpCS,
    essentialoclcs_InvalidLiteralExpCS,
    essentialoclcs_StringLiteralExpCS,
    essentialoclcs_BooleanLiteralExpCS,
    essentialoclcs_ExpCS,
    OperatorCS,
    essentialoclcs_UnaryOperatorCS,
    essentialoclcs_BinaryOperatorCS,
    ExpCS,
    essentialoclcs_SelfExpCS,
    essentialoclcs_LetExpCS,
    essentialoclcs_LetVariableCS,
    essentialoclcs_NestedExpCS,
    essentialoclcs_PrefixExpCS,
    essentialoclcs_LiteralExpCS,
    essentialoclcs_IfExpCS,
    essentialoclcs_InfixExpCS,
    essentialoclcs_OperatorCS,
    essentialoclcs_AbstractNameExpCS,
    NavigationRole,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_essentialoclcs_type_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Type)


def test_essentialoclcs_type_constructor_exists():
    assert callable(essentialoclcs_Type.__init__)


def test_essentialoclcs_type_constructor_args():
    sig = inspect.signature(essentialoclcs_Type.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorCS)


def test_binaryoperatorcs_constructor_exists():
    assert callable(BinaryOperatorCS.__init__)


def test_binaryoperatorcs_constructor_args():
    sig = inspect.signature(BinaryOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_navigationoperatorcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NavigationOperatorCS)


def test_essentialoclcs_navigationoperatorcs_constructor_exists():
    assert callable(essentialoclcs_NavigationOperatorCS.__init__)


def test_essentialoclcs_navigationoperatorcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NavigationOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PathNameCS)


def test_essentialoclcs_pathnamecs_constructor_exists():
    assert callable(essentialoclcs_PathNameCS.__init__)


def test_essentialoclcs_pathnamecs_constructor_args():
    sig = inspect.signature(essentialoclcs_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_abstractnameexpcs_is_not_abstract():
    assert not inspect.isabstract(AbstractNameExpCS)


def test_abstractnameexpcs_constructor_exists():
    assert callable(AbstractNameExpCS.__init__)


def test_abstractnameexpcs_constructor_args():
    sig = inspect.signature(AbstractNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_namedexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NamedExpCS)


def test_essentialoclcs_namedexpcs_constructor_exists():
    assert callable(essentialoclcs_NamedExpCS.__init__)


def test_essentialoclcs_namedexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NamedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_nameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NameExpCS)


def test_essentialoclcs_nameexpcs_constructor_exists():
    assert callable(essentialoclcs_NameExpCS.__init__)


def test_essentialoclcs_nameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NameExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "atPre" in params, "Missing parameter 'atPre'"

def test_essentialoclcs_nameexpcs_has_atPre():
    assert hasattr(essentialoclcs_NameExpCS, "atPre")
    descriptor = None
    for klass in essentialoclcs_NameExpCS.__mro__:
        if "atPre" in klass.__dict__:
            descriptor = klass.__dict__["atPre"]
            break
    assert isinstance(descriptor, property)



def test_variablecs_is_not_abstract():
    assert not inspect.isabstract(VariableCS)


def test_variablecs_constructor_exists():
    assert callable(VariableCS.__init__)


def test_variablecs_constructor_args():
    sig = inspect.signature(VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_tupleliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TupleLiteralPartCS)


def test_essentialoclcs_tupleliteralpartcs_constructor_exists():
    assert callable(essentialoclcs_TupleLiteralPartCS.__init__)


def test_essentialoclcs_tupleliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TupleLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_specificationcs_is_not_abstract():
    assert not inspect.isabstract(SpecificationCS)


def test_specificationcs_constructor_exists():
    assert callable(SpecificationCS.__init__)


def test_specificationcs_constructor_args():
    sig = inspect.signature(SpecificationCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_expspecificationcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ExpSpecificationCS)


def test_essentialoclcs_expspecificationcs_constructor_exists():
    assert callable(essentialoclcs_ExpSpecificationCS.__init__)


def test_essentialoclcs_expspecificationcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ExpSpecificationCS.__init__)
    params = list(sig.parameters.keys())



def test_rootcs_is_not_abstract():
    assert not inspect.isabstract(RootCS)


def test_rootcs_constructor_exists():
    assert callable(RootCS.__init__)


def test_rootcs_constructor_args():
    sig = inspect.signature(RootCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_variablecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_VariableCS)


def test_essentialoclcs_variablecs_constructor_exists():
    assert callable(essentialoclcs_VariableCS.__init__)


def test_essentialoclcs_variablecs_constructor_args():
    sig = inspect.signature(essentialoclcs_VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_contextcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ContextCS)


def test_essentialoclcs_contextcs_constructor_exists():
    assert callable(essentialoclcs_ContextCS.__init__)


def test_essentialoclcs_contextcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ContextCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_property_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Property)


def test_essentialoclcs_property_constructor_exists():
    assert callable(essentialoclcs_Property.__init__)


def test_essentialoclcs_property_constructor_args():
    sig = inspect.signature(essentialoclcs_Property.__init__)
    params = list(sig.parameters.keys())



def test_namedexpcs_is_not_abstract():
    assert not inspect.isabstract(NamedExpCS)


def test_namedexpcs_constructor_exists():
    assert callable(NamedExpCS.__init__)


def test_namedexpcs_constructor_args():
    sig = inspect.signature(NamedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_invocationexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_InvocationExpCS)


def test_essentialoclcs_invocationexpcs_constructor_exists():
    assert callable(essentialoclcs_InvocationExpCS.__init__)


def test_essentialoclcs_invocationexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_InvocationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_indexexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_IndexExpCS)


def test_essentialoclcs_indexexpcs_constructor_exists():
    assert callable(essentialoclcs_IndexExpCS.__init__)


def test_essentialoclcs_indexexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_IndexExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "atPre" in params, "Missing parameter 'atPre'"

def test_essentialoclcs_indexexpcs_has_atPre():
    assert hasattr(essentialoclcs_IndexExpCS, "atPre")
    descriptor = None
    for klass in essentialoclcs_IndexExpCS.__mro__:
        if "atPre" in klass.__dict__:
            descriptor = klass.__dict__["atPre"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_constructorexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ConstructorExpCS)


def test_essentialoclcs_constructorexpcs_constructor_exists():
    assert callable(essentialoclcs_ConstructorExpCS.__init__)


def test_essentialoclcs_constructorexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ConstructorExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcs_constructorexpcs_has_value():
    assert hasattr(essentialoclcs_ConstructorExpCS, "value")
    descriptor = None
    for klass in essentialoclcs_ConstructorExpCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypedRefCS)


def test_essentialoclcs_typedrefcs_constructor_exists():
    assert callable(essentialoclcs_TypedRefCS.__init__)


def test_essentialoclcs_typedrefcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(TypedRefCS)


def test_typedrefcs_constructor_exists():
    assert callable(TypedRefCS.__init__)


def test_typedrefcs_constructor_args():
    sig = inspect.signature(TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_typenameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypeNameExpCS)


def test_essentialoclcs_typenameexpcs_constructor_exists():
    assert callable(essentialoclcs_TypeNameExpCS.__init__)


def test_essentialoclcs_typenameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypeNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_navigatingargcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NavigatingArgCS)


def test_essentialoclcs_navigatingargcs_constructor_exists():
    assert callable(essentialoclcs_NavigatingArgCS.__init__)


def test_essentialoclcs_navigatingargcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NavigatingArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "role" in params, "Missing parameter 'role'"

def test_essentialoclcs_navigatingargcs_has_prefix():
    assert hasattr(essentialoclcs_NavigatingArgCS, "prefix")
    descriptor = None
    for klass in essentialoclcs_NavigatingArgCS.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_essentialoclcs_navigatingargcs_has_role():
    assert hasattr(essentialoclcs_NavigatingArgCS, "role")
    descriptor = None
    for klass in essentialoclcs_NavigatingArgCS.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_constructorpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ConstructorPartCS)


def test_essentialoclcs_constructorpartcs_constructor_exists():
    assert callable(essentialoclcs_ConstructorPartCS.__init__)


def test_essentialoclcs_constructorpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ConstructorPartCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionLiteralPartCS)


def test_essentialoclcs_collectionliteralpartcs_constructor_exists():
    assert callable(essentialoclcs_CollectionLiteralPartCS.__init__)


def test_essentialoclcs_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionTypeCS)


def test_essentialoclcs_collectiontypecs_constructor_exists():
    assert callable(essentialoclcs_CollectionTypeCS.__init__)


def test_essentialoclcs_collectiontypecs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs_collectiontypecs_has_name():
    assert hasattr(essentialoclcs_CollectionTypeCS, "name")
    descriptor = None
    for klass in essentialoclcs_CollectionTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TupleLiteralExpCS)


def test_essentialoclcs_tupleliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_TupleLiteralExpCS.__init__)


def test_essentialoclcs_tupleliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypeLiteralExpCS)


def test_essentialoclcs_typeliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_TypeLiteralExpCS.__init__)


def test_essentialoclcs_typeliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PrimitiveLiteralExpCS)


def test_essentialoclcs_primitiveliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_PrimitiveLiteralExpCS.__init__)


def test_essentialoclcs_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionLiteralExpCS)


def test_essentialoclcs_collectionliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_CollectionLiteralExpCS.__init__)


def test_essentialoclcs_collectionliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NullLiteralExpCS)


def test_essentialoclcs_nullliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_NullLiteralExpCS.__init__)


def test_essentialoclcs_nullliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_UnlimitedNaturalLiteralExpCS)


def test_essentialoclcs_unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_UnlimitedNaturalLiteralExpCS.__init__)


def test_essentialoclcs_unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_numberliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NumberLiteralExpCS)


def test_essentialoclcs_numberliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_NumberLiteralExpCS.__init__)


def test_essentialoclcs_numberliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NumberLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs_numberliteralexpcs_has_name():
    assert hasattr(essentialoclcs_NumberLiteralExpCS, "name")
    descriptor = None
    for klass in essentialoclcs_NumberLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_InvalidLiteralExpCS)


def test_essentialoclcs_invalidliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_InvalidLiteralExpCS.__init__)


def test_essentialoclcs_invalidliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_StringLiteralExpCS)


def test_essentialoclcs_stringliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_StringLiteralExpCS.__init__)


def test_essentialoclcs_stringliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs_stringliteralexpcs_has_name():
    assert hasattr(essentialoclcs_StringLiteralExpCS, "name")
    descriptor = None
    for klass in essentialoclcs_StringLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_BooleanLiteralExpCS)


def test_essentialoclcs_booleanliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_BooleanLiteralExpCS.__init__)


def test_essentialoclcs_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs_booleanliteralexpcs_has_name():
    assert hasattr(essentialoclcs_BooleanLiteralExpCS, "name")
    descriptor = None
    for klass in essentialoclcs_BooleanLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_expcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ExpCS)


def test_essentialoclcs_expcs_constructor_exists():
    assert callable(essentialoclcs_ExpCS.__init__)


def test_essentialoclcs_expcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_operatorcs_is_not_abstract():
    assert not inspect.isabstract(OperatorCS)


def test_operatorcs_constructor_exists():
    assert callable(OperatorCS.__init__)


def test_operatorcs_constructor_args():
    sig = inspect.signature(OperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_unaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_UnaryOperatorCS)


def test_essentialoclcs_unaryoperatorcs_constructor_exists():
    assert callable(essentialoclcs_UnaryOperatorCS.__init__)


def test_essentialoclcs_unaryoperatorcs_constructor_args():
    sig = inspect.signature(essentialoclcs_UnaryOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_binaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_BinaryOperatorCS)


def test_essentialoclcs_binaryoperatorcs_constructor_exists():
    assert callable(essentialoclcs_BinaryOperatorCS.__init__)


def test_essentialoclcs_binaryoperatorcs_constructor_args():
    sig = inspect.signature(essentialoclcs_BinaryOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_selfexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_SelfExpCS)


def test_essentialoclcs_selfexpcs_constructor_exists():
    assert callable(essentialoclcs_SelfExpCS.__init__)


def test_essentialoclcs_selfexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_SelfExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs_selfexpcs_has_name():
    assert hasattr(essentialoclcs_SelfExpCS, "name")
    descriptor = None
    for klass in essentialoclcs_SelfExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_letexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LetExpCS)


def test_essentialoclcs_letexpcs_constructor_exists():
    assert callable(essentialoclcs_LetExpCS.__init__)


def test_essentialoclcs_letexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_letvariablecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LetVariableCS)


def test_essentialoclcs_letvariablecs_constructor_exists():
    assert callable(essentialoclcs_LetVariableCS.__init__)


def test_essentialoclcs_letvariablecs_constructor_args():
    sig = inspect.signature(essentialoclcs_LetVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_nestedexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NestedExpCS)


def test_essentialoclcs_nestedexpcs_constructor_exists():
    assert callable(essentialoclcs_NestedExpCS.__init__)


def test_essentialoclcs_nestedexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NestedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_prefixexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PrefixExpCS)


def test_essentialoclcs_prefixexpcs_constructor_exists():
    assert callable(essentialoclcs_PrefixExpCS.__init__)


def test_essentialoclcs_prefixexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_PrefixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LiteralExpCS)


def test_essentialoclcs_literalexpcs_constructor_exists():
    assert callable(essentialoclcs_LiteralExpCS.__init__)


def test_essentialoclcs_literalexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_ifexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_IfExpCS)


def test_essentialoclcs_ifexpcs_constructor_exists():
    assert callable(essentialoclcs_IfExpCS.__init__)


def test_essentialoclcs_ifexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_IfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_infixexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_InfixExpCS)


def test_essentialoclcs_infixexpcs_constructor_exists():
    assert callable(essentialoclcs_InfixExpCS.__init__)


def test_essentialoclcs_infixexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_InfixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_operatorcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_OperatorCS)


def test_essentialoclcs_operatorcs_constructor_exists():
    assert callable(essentialoclcs_OperatorCS.__init__)


def test_essentialoclcs_operatorcs_constructor_args():
    sig = inspect.signature(essentialoclcs_OperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_abstractnameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_AbstractNameExpCS)


def test_essentialoclcs_abstractnameexpcs_constructor_exists():
    assert callable(essentialoclcs_AbstractNameExpCS.__init__)


def test_essentialoclcs_abstractnameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_AbstractNameExpCS.__init__)
    params = list(sig.parameters.keys())

def test_navigationrole_exists():
    # Check that the Enumeration exists
    assert NavigationRole is not None

def test_navigationrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NavigationRole]
    expected_literals = [
        "ACCUMULATOR",
        "EXPRESSION",
        "ITERATOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NavigationRole"


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
essentialoclcs_Type_strategy = st.builds(
    essentialoclcs_Type,
)
BinaryOperatorCS_strategy = st.builds(
    BinaryOperatorCS,
)
essentialoclcs_NavigationOperatorCS_strategy = st.builds(
    essentialoclcs_NavigationOperatorCS,
)
essentialoclcs_PathNameCS_strategy = st.builds(
    essentialoclcs_PathNameCS,
)
AbstractNameExpCS_strategy = st.builds(
    AbstractNameExpCS,
)
essentialoclcs_NamedExpCS_strategy = st.builds(
    essentialoclcs_NamedExpCS,
)
essentialoclcs_NameExpCS_strategy = st.builds(
    essentialoclcs_NameExpCS,
    atPre=
        st.booleans()
)
VariableCS_strategy = st.builds(
    VariableCS,
)
essentialoclcs_TupleLiteralPartCS_strategy = st.builds(
    essentialoclcs_TupleLiteralPartCS,
)
SpecificationCS_strategy = st.builds(
    SpecificationCS,
)
essentialoclcs_ExpSpecificationCS_strategy = st.builds(
    essentialoclcs_ExpSpecificationCS,
)
RootCS_strategy = st.builds(
    RootCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
essentialoclcs_VariableCS_strategy = st.builds(
    essentialoclcs_VariableCS,
)
essentialoclcs_ContextCS_strategy = st.builds(
    essentialoclcs_ContextCS,
)
essentialoclcs_Property_strategy = st.builds(
    essentialoclcs_Property,
)
NamedExpCS_strategy = st.builds(
    NamedExpCS,
)
essentialoclcs_InvocationExpCS_strategy = st.builds(
    essentialoclcs_InvocationExpCS,
)
essentialoclcs_IndexExpCS_strategy = st.builds(
    essentialoclcs_IndexExpCS,
    atPre=
        st.booleans()
)
essentialoclcs_ConstructorExpCS_strategy = st.builds(
    essentialoclcs_ConstructorExpCS,
    value=
        safe_text
)
essentialoclcs_TypedRefCS_strategy = st.builds(
    essentialoclcs_TypedRefCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
essentialoclcs_TypeNameExpCS_strategy = st.builds(
    essentialoclcs_TypeNameExpCS,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
essentialoclcs_NavigatingArgCS_strategy = st.builds(
    essentialoclcs_NavigatingArgCS,
    prefix=
        safe_text,
    role=
        safe_text
)
essentialoclcs_ConstructorPartCS_strategy = st.builds(
    essentialoclcs_ConstructorPartCS,
)
essentialoclcs_CollectionLiteralPartCS_strategy = st.builds(
    essentialoclcs_CollectionLiteralPartCS,
)
essentialoclcs_CollectionTypeCS_strategy = st.builds(
    essentialoclcs_CollectionTypeCS,
    name=
        safe_text
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
essentialoclcs_TupleLiteralExpCS_strategy = st.builds(
    essentialoclcs_TupleLiteralExpCS,
)
essentialoclcs_TypeLiteralExpCS_strategy = st.builds(
    essentialoclcs_TypeLiteralExpCS,
)
essentialoclcs_PrimitiveLiteralExpCS_strategy = st.builds(
    essentialoclcs_PrimitiveLiteralExpCS,
)
essentialoclcs_CollectionLiteralExpCS_strategy = st.builds(
    essentialoclcs_CollectionLiteralExpCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
essentialoclcs_NullLiteralExpCS_strategy = st.builds(
    essentialoclcs_NullLiteralExpCS,
)
essentialoclcs_UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    essentialoclcs_UnlimitedNaturalLiteralExpCS,
)
essentialoclcs_NumberLiteralExpCS_strategy = st.builds(
    essentialoclcs_NumberLiteralExpCS,
    name=
        safe_text
)
essentialoclcs_InvalidLiteralExpCS_strategy = st.builds(
    essentialoclcs_InvalidLiteralExpCS,
)
essentialoclcs_StringLiteralExpCS_strategy = st.builds(
    essentialoclcs_StringLiteralExpCS,
    name=
        safe_text
)
essentialoclcs_BooleanLiteralExpCS_strategy = st.builds(
    essentialoclcs_BooleanLiteralExpCS,
    name=
        safe_text
)
essentialoclcs_ExpCS_strategy = st.builds(
    essentialoclcs_ExpCS,
)
OperatorCS_strategy = st.builds(
    OperatorCS,
)
essentialoclcs_UnaryOperatorCS_strategy = st.builds(
    essentialoclcs_UnaryOperatorCS,
)
essentialoclcs_BinaryOperatorCS_strategy = st.builds(
    essentialoclcs_BinaryOperatorCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
essentialoclcs_SelfExpCS_strategy = st.builds(
    essentialoclcs_SelfExpCS,
    name=
        safe_text
)
essentialoclcs_LetExpCS_strategy = st.builds(
    essentialoclcs_LetExpCS,
)
essentialoclcs_LetVariableCS_strategy = st.builds(
    essentialoclcs_LetVariableCS,
)
essentialoclcs_NestedExpCS_strategy = st.builds(
    essentialoclcs_NestedExpCS,
)
essentialoclcs_PrefixExpCS_strategy = st.builds(
    essentialoclcs_PrefixExpCS,
)
essentialoclcs_LiteralExpCS_strategy = st.builds(
    essentialoclcs_LiteralExpCS,
)
essentialoclcs_IfExpCS_strategy = st.builds(
    essentialoclcs_IfExpCS,
)
essentialoclcs_InfixExpCS_strategy = st.builds(
    essentialoclcs_InfixExpCS,
)
essentialoclcs_OperatorCS_strategy = st.builds(
    essentialoclcs_OperatorCS,
)
essentialoclcs_AbstractNameExpCS_strategy = st.builds(
    essentialoclcs_AbstractNameExpCS,
)

@given(instance=essentialoclcs_Type_strategy)
@settings(max_examples=50)
def test_essentialoclcs_type_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Type)

@given(instance=BinaryOperatorCS_strategy)
@settings(max_examples=50)
def test_binaryoperatorcs_instantiation(instance):
    assert isinstance(instance, BinaryOperatorCS)

@given(instance=essentialoclcs_NavigationOperatorCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_navigationoperatorcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NavigationOperatorCS)

@given(instance=essentialoclcs_PathNameCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_pathnamecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PathNameCS)

@given(instance=AbstractNameExpCS_strategy)
@settings(max_examples=50)
def test_abstractnameexpcs_instantiation(instance):
    assert isinstance(instance, AbstractNameExpCS)

@given(instance=essentialoclcs_NamedExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_namedexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NamedExpCS)

@given(instance=essentialoclcs_NameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_nameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NameExpCS)



@given(instance=essentialoclcs_NameExpCS_strategy)
def test_essentialoclcs_nameexpcs_atPre_setter(instance):
    original = instance.atPre
    instance.atPre = original
    assert instance.atPre == original

@given(instance=VariableCS_strategy)
@settings(max_examples=50)
def test_variablecs_instantiation(instance):
    assert isinstance(instance, VariableCS)

@given(instance=essentialoclcs_TupleLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_tupleliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TupleLiteralPartCS)

@given(instance=SpecificationCS_strategy)
@settings(max_examples=50)
def test_specificationcs_instantiation(instance):
    assert isinstance(instance, SpecificationCS)

@given(instance=essentialoclcs_ExpSpecificationCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_expspecificationcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ExpSpecificationCS)

@given(instance=RootCS_strategy)
@settings(max_examples=50)
def test_rootcs_instantiation(instance):
    assert isinstance(instance, RootCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=essentialoclcs_VariableCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_variablecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_VariableCS)

@given(instance=essentialoclcs_ContextCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_contextcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ContextCS)

@given(instance=essentialoclcs_Property_strategy)
@settings(max_examples=50)
def test_essentialoclcs_property_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Property)

@given(instance=NamedExpCS_strategy)
@settings(max_examples=50)
def test_namedexpcs_instantiation(instance):
    assert isinstance(instance, NamedExpCS)

@given(instance=essentialoclcs_InvocationExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_invocationexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_InvocationExpCS)

@given(instance=essentialoclcs_IndexExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_indexexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_IndexExpCS)



@given(instance=essentialoclcs_IndexExpCS_strategy)
def test_essentialoclcs_indexexpcs_atPre_setter(instance):
    original = instance.atPre
    instance.atPre = original
    assert instance.atPre == original

@given(instance=essentialoclcs_ConstructorExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_constructorexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ConstructorExpCS)



@given(instance=essentialoclcs_ConstructorExpCS_strategy)
def test_essentialoclcs_constructorexpcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=essentialoclcs_TypedRefCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_typedrefcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypedRefCS)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=TypedRefCS_strategy)
@settings(max_examples=50)
def test_typedrefcs_instantiation(instance):
    assert isinstance(instance, TypedRefCS)

@given(instance=essentialoclcs_TypeNameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_typenameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypeNameExpCS)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=essentialoclcs_NavigatingArgCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_navigatingargcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NavigatingArgCS)



@given(instance=essentialoclcs_NavigatingArgCS_strategy)
def test_essentialoclcs_navigatingargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=essentialoclcs_NavigatingArgCS_strategy)
def test_essentialoclcs_navigatingargcs_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=essentialoclcs_ConstructorPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_constructorpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ConstructorPartCS)

@given(instance=essentialoclcs_CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionLiteralPartCS)

@given(instance=essentialoclcs_CollectionTypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_collectiontypecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionTypeCS)



@given(instance=essentialoclcs_CollectionTypeCS_strategy)
def test_essentialoclcs_collectiontypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=essentialoclcs_TupleLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_tupleliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TupleLiteralExpCS)

@given(instance=essentialoclcs_TypeLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_typeliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypeLiteralExpCS)

@given(instance=essentialoclcs_PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PrimitiveLiteralExpCS)

@given(instance=essentialoclcs_CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionLiteralExpCS)

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=essentialoclcs_NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NullLiteralExpCS)

@given(instance=essentialoclcs_UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_unlimitednaturalliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_UnlimitedNaturalLiteralExpCS)

@given(instance=essentialoclcs_NumberLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_numberliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NumberLiteralExpCS)



@given(instance=essentialoclcs_NumberLiteralExpCS_strategy)
def test_essentialoclcs_numberliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs_InvalidLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_invalidliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_InvalidLiteralExpCS)

@given(instance=essentialoclcs_StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_StringLiteralExpCS)



@given(instance=essentialoclcs_StringLiteralExpCS_strategy)
def test_essentialoclcs_stringliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs_BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_BooleanLiteralExpCS)



@given(instance=essentialoclcs_BooleanLiteralExpCS_strategy)
def test_essentialoclcs_booleanliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs_ExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_expcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ExpCS)

@given(instance=OperatorCS_strategy)
@settings(max_examples=50)
def test_operatorcs_instantiation(instance):
    assert isinstance(instance, OperatorCS)

@given(instance=essentialoclcs_UnaryOperatorCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_unaryoperatorcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_UnaryOperatorCS)

@given(instance=essentialoclcs_BinaryOperatorCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_binaryoperatorcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_BinaryOperatorCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=essentialoclcs_SelfExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_selfexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_SelfExpCS)



@given(instance=essentialoclcs_SelfExpCS_strategy)
def test_essentialoclcs_selfexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs_LetExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_letexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LetExpCS)

@given(instance=essentialoclcs_LetVariableCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_letvariablecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LetVariableCS)

@given(instance=essentialoclcs_NestedExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_nestedexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NestedExpCS)

@given(instance=essentialoclcs_PrefixExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_prefixexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PrefixExpCS)

@given(instance=essentialoclcs_LiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_literalexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LiteralExpCS)

@given(instance=essentialoclcs_IfExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_ifexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_IfExpCS)

@given(instance=essentialoclcs_InfixExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_infixexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_InfixExpCS)

@given(instance=essentialoclcs_OperatorCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_operatorcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_OperatorCS)

@given(instance=essentialoclcs_AbstractNameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_abstractnameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_AbstractNameExpCS)

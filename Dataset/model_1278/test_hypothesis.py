import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    essentialoclcs::Type,
    BinaryOperatorCS,
    essentialoclcs::NavigationOperatorCS,
    essentialoclcs::PathNameCS,
    AbstractNameExpCS,
    essentialoclcs::NamedExpCS,
    essentialoclcs::NameExpCS,
    VariableCS,
    essentialoclcs::TupleLiteralPartCS,
    SpecificationCS,
    essentialoclcs::ExpSpecificationCS,
    RootCS,
    NamedElementCS,
    essentialoclcs::VariableCS,
    essentialoclcs::ContextCS,
    essentialoclcs::Property,
    NamedExpCS,
    essentialoclcs::InvocationExpCS,
    essentialoclcs::IndexExpCS,
    essentialoclcs::ConstructorExpCS,
    essentialoclcs::TypedRefCS,
    Nameable,
    TypedRefCS,
    essentialoclcs::TypeNameExpCS,
    ModelElementCS,
    essentialoclcs::ConstructorPartCS,
    essentialoclcs::NavigatingArgCS,
    essentialoclcs::CollectionLiteralPartCS,
    essentialoclcs::CollectionTypeCS,
    LiteralExpCS,
    essentialoclcs::PrimitiveLiteralExpCS,
    essentialoclcs::TypeLiteralExpCS,
    essentialoclcs::TupleLiteralExpCS,
    essentialoclcs::CollectionLiteralExpCS,
    PrimitiveLiteralExpCS,
    essentialoclcs::InvalidLiteralExpCS,
    essentialoclcs::UnlimitedNaturalLiteralExpCS,
    essentialoclcs::StringLiteralExpCS,
    essentialoclcs::NumberLiteralExpCS,
    essentialoclcs::NullLiteralExpCS,
    essentialoclcs::BooleanLiteralExpCS,
    essentialoclcs::ExpCS,
    OperatorCS,
    essentialoclcs::UnaryOperatorCS,
    essentialoclcs::BinaryOperatorCS,
    ExpCS,
    essentialoclcs::OperatorCS,
    essentialoclcs::IfExpCS,
    essentialoclcs::LetVariableCS,
    essentialoclcs::LiteralExpCS,
    essentialoclcs::InfixExpCS,
    essentialoclcs::LetExpCS,
    essentialoclcs::PrefixExpCS,
    essentialoclcs::NestedExpCS,
    essentialoclcs::SelfExpCS,
    essentialoclcs::AbstractNameExpCS,
    NavigationRole,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_essentialoclcs::type_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::Type)


def test_essentialoclcs::type_constructor_exists():
    assert callable(essentialoclcs::Type.__init__)


def test_essentialoclcs::type_constructor_args():
    sig = inspect.signature(essentialoclcs::Type.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorCS)


def test_binaryoperatorcs_constructor_exists():
    assert callable(BinaryOperatorCS.__init__)


def test_binaryoperatorcs_constructor_args():
    sig = inspect.signature(BinaryOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::navigationoperatorcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NavigationOperatorCS)


def test_essentialoclcs::navigationoperatorcs_constructor_exists():
    assert callable(essentialoclcs::NavigationOperatorCS.__init__)


def test_essentialoclcs::navigationoperatorcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NavigationOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::PathNameCS)


def test_essentialoclcs::pathnamecs_constructor_exists():
    assert callable(essentialoclcs::PathNameCS.__init__)


def test_essentialoclcs::pathnamecs_constructor_args():
    sig = inspect.signature(essentialoclcs::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_abstractnameexpcs_is_not_abstract():
    assert not inspect.isabstract(AbstractNameExpCS)


def test_abstractnameexpcs_constructor_exists():
    assert callable(AbstractNameExpCS.__init__)


def test_abstractnameexpcs_constructor_args():
    sig = inspect.signature(AbstractNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::namedexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NamedExpCS)


def test_essentialoclcs::namedexpcs_constructor_exists():
    assert callable(essentialoclcs::NamedExpCS.__init__)


def test_essentialoclcs::namedexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NamedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::nameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NameExpCS)


def test_essentialoclcs::nameexpcs_constructor_exists():
    assert callable(essentialoclcs::NameExpCS.__init__)


def test_essentialoclcs::nameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NameExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "atPre" in params, "Missing parameter 'atPre'"

def test_essentialoclcs::nameexpcs_has_atPre():
    assert hasattr(essentialoclcs::NameExpCS, "atPre")
    descriptor = None
    for klass in essentialoclcs::NameExpCS.__mro__:
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



def test_essentialoclcs::tupleliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TupleLiteralPartCS)


def test_essentialoclcs::tupleliteralpartcs_constructor_exists():
    assert callable(essentialoclcs::TupleLiteralPartCS.__init__)


def test_essentialoclcs::tupleliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TupleLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_specificationcs_is_not_abstract():
    assert not inspect.isabstract(SpecificationCS)


def test_specificationcs_constructor_exists():
    assert callable(SpecificationCS.__init__)


def test_specificationcs_constructor_args():
    sig = inspect.signature(SpecificationCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::expspecificationcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::ExpSpecificationCS)


def test_essentialoclcs::expspecificationcs_constructor_exists():
    assert callable(essentialoclcs::ExpSpecificationCS.__init__)


def test_essentialoclcs::expspecificationcs_constructor_args():
    sig = inspect.signature(essentialoclcs::ExpSpecificationCS.__init__)
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



def test_essentialoclcs::variablecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::VariableCS)


def test_essentialoclcs::variablecs_constructor_exists():
    assert callable(essentialoclcs::VariableCS.__init__)


def test_essentialoclcs::variablecs_constructor_args():
    sig = inspect.signature(essentialoclcs::VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::contextcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::ContextCS)


def test_essentialoclcs::contextcs_constructor_exists():
    assert callable(essentialoclcs::ContextCS.__init__)


def test_essentialoclcs::contextcs_constructor_args():
    sig = inspect.signature(essentialoclcs::ContextCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::property_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::Property)


def test_essentialoclcs::property_constructor_exists():
    assert callable(essentialoclcs::Property.__init__)


def test_essentialoclcs::property_constructor_args():
    sig = inspect.signature(essentialoclcs::Property.__init__)
    params = list(sig.parameters.keys())



def test_namedexpcs_is_not_abstract():
    assert not inspect.isabstract(NamedExpCS)


def test_namedexpcs_constructor_exists():
    assert callable(NamedExpCS.__init__)


def test_namedexpcs_constructor_args():
    sig = inspect.signature(NamedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::invocationexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::InvocationExpCS)


def test_essentialoclcs::invocationexpcs_constructor_exists():
    assert callable(essentialoclcs::InvocationExpCS.__init__)


def test_essentialoclcs::invocationexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::InvocationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::indexexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::IndexExpCS)


def test_essentialoclcs::indexexpcs_constructor_exists():
    assert callable(essentialoclcs::IndexExpCS.__init__)


def test_essentialoclcs::indexexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::IndexExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "atPre" in params, "Missing parameter 'atPre'"

def test_essentialoclcs::indexexpcs_has_atPre():
    assert hasattr(essentialoclcs::IndexExpCS, "atPre")
    descriptor = None
    for klass in essentialoclcs::IndexExpCS.__mro__:
        if "atPre" in klass.__dict__:
            descriptor = klass.__dict__["atPre"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::constructorexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::ConstructorExpCS)


def test_essentialoclcs::constructorexpcs_constructor_exists():
    assert callable(essentialoclcs::ConstructorExpCS.__init__)


def test_essentialoclcs::constructorexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::ConstructorExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcs::constructorexpcs_has_value():
    assert hasattr(essentialoclcs::ConstructorExpCS, "value")
    descriptor = None
    for klass in essentialoclcs::ConstructorExpCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::typedrefcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TypedRefCS)


def test_essentialoclcs::typedrefcs_constructor_exists():
    assert callable(essentialoclcs::TypedRefCS.__init__)


def test_essentialoclcs::typedrefcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TypedRefCS.__init__)
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



def test_essentialoclcs::typenameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TypeNameExpCS)


def test_essentialoclcs::typenameexpcs_constructor_exists():
    assert callable(essentialoclcs::TypeNameExpCS.__init__)


def test_essentialoclcs::typenameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TypeNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::constructorpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::ConstructorPartCS)


def test_essentialoclcs::constructorpartcs_constructor_exists():
    assert callable(essentialoclcs::ConstructorPartCS.__init__)


def test_essentialoclcs::constructorpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs::ConstructorPartCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::navigatingargcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NavigatingArgCS)


def test_essentialoclcs::navigatingargcs_constructor_exists():
    assert callable(essentialoclcs::NavigatingArgCS.__init__)


def test_essentialoclcs::navigatingargcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NavigatingArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_essentialoclcs::navigatingargcs_has_role():
    assert hasattr(essentialoclcs::NavigatingArgCS, "role")
    descriptor = None
    for klass in essentialoclcs::NavigatingArgCS.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_essentialoclcs::navigatingargcs_has_prefix():
    assert hasattr(essentialoclcs::NavigatingArgCS, "prefix")
    descriptor = None
    for klass in essentialoclcs::NavigatingArgCS.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::CollectionLiteralPartCS)


def test_essentialoclcs::collectionliteralpartcs_constructor_exists():
    assert callable(essentialoclcs::CollectionLiteralPartCS.__init__)


def test_essentialoclcs::collectionliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs::CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::CollectionTypeCS)


def test_essentialoclcs::collectiontypecs_constructor_exists():
    assert callable(essentialoclcs::CollectionTypeCS.__init__)


def test_essentialoclcs::collectiontypecs_constructor_args():
    sig = inspect.signature(essentialoclcs::CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs::collectiontypecs_has_name():
    assert hasattr(essentialoclcs::CollectionTypeCS, "name")
    descriptor = None
    for klass in essentialoclcs::CollectionTypeCS.__mro__:
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



def test_essentialoclcs::primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::PrimitiveLiteralExpCS)


def test_essentialoclcs::primitiveliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::PrimitiveLiteralExpCS.__init__)


def test_essentialoclcs::primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TypeLiteralExpCS)


def test_essentialoclcs::typeliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::TypeLiteralExpCS.__init__)


def test_essentialoclcs::typeliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TupleLiteralExpCS)


def test_essentialoclcs::tupleliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::TupleLiteralExpCS.__init__)


def test_essentialoclcs::tupleliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::CollectionLiteralExpCS)


def test_essentialoclcs::collectionliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::CollectionLiteralExpCS.__init__)


def test_essentialoclcs::collectionliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::InvalidLiteralExpCS)


def test_essentialoclcs::invalidliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::InvalidLiteralExpCS.__init__)


def test_essentialoclcs::invalidliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::UnlimitedNaturalLiteralExpCS)


def test_essentialoclcs::unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::UnlimitedNaturalLiteralExpCS.__init__)


def test_essentialoclcs::unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::StringLiteralExpCS)


def test_essentialoclcs::stringliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::StringLiteralExpCS.__init__)


def test_essentialoclcs::stringliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs::stringliteralexpcs_has_name():
    assert hasattr(essentialoclcs::StringLiteralExpCS, "name")
    descriptor = None
    for klass in essentialoclcs::StringLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::numberliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NumberLiteralExpCS)


def test_essentialoclcs::numberliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::NumberLiteralExpCS.__init__)


def test_essentialoclcs::numberliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NumberLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs::numberliteralexpcs_has_name():
    assert hasattr(essentialoclcs::NumberLiteralExpCS, "name")
    descriptor = None
    for klass in essentialoclcs::NumberLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NullLiteralExpCS)


def test_essentialoclcs::nullliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::NullLiteralExpCS.__init__)


def test_essentialoclcs::nullliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::BooleanLiteralExpCS)


def test_essentialoclcs::booleanliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::BooleanLiteralExpCS.__init__)


def test_essentialoclcs::booleanliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs::booleanliteralexpcs_has_name():
    assert hasattr(essentialoclcs::BooleanLiteralExpCS, "name")
    descriptor = None
    for klass in essentialoclcs::BooleanLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::expcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::ExpCS)


def test_essentialoclcs::expcs_constructor_exists():
    assert callable(essentialoclcs::ExpCS.__init__)


def test_essentialoclcs::expcs_constructor_args():
    sig = inspect.signature(essentialoclcs::ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_operatorcs_is_not_abstract():
    assert not inspect.isabstract(OperatorCS)


def test_operatorcs_constructor_exists():
    assert callable(OperatorCS.__init__)


def test_operatorcs_constructor_args():
    sig = inspect.signature(OperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::unaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::UnaryOperatorCS)


def test_essentialoclcs::unaryoperatorcs_constructor_exists():
    assert callable(essentialoclcs::UnaryOperatorCS.__init__)


def test_essentialoclcs::unaryoperatorcs_constructor_args():
    sig = inspect.signature(essentialoclcs::UnaryOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::binaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::BinaryOperatorCS)


def test_essentialoclcs::binaryoperatorcs_constructor_exists():
    assert callable(essentialoclcs::BinaryOperatorCS.__init__)


def test_essentialoclcs::binaryoperatorcs_constructor_args():
    sig = inspect.signature(essentialoclcs::BinaryOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::operatorcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::OperatorCS)


def test_essentialoclcs::operatorcs_constructor_exists():
    assert callable(essentialoclcs::OperatorCS.__init__)


def test_essentialoclcs::operatorcs_constructor_args():
    sig = inspect.signature(essentialoclcs::OperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::ifexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::IfExpCS)


def test_essentialoclcs::ifexpcs_constructor_exists():
    assert callable(essentialoclcs::IfExpCS.__init__)


def test_essentialoclcs::ifexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::IfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::letvariablecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::LetVariableCS)


def test_essentialoclcs::letvariablecs_constructor_exists():
    assert callable(essentialoclcs::LetVariableCS.__init__)


def test_essentialoclcs::letvariablecs_constructor_args():
    sig = inspect.signature(essentialoclcs::LetVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::literalexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::LiteralExpCS)


def test_essentialoclcs::literalexpcs_constructor_exists():
    assert callable(essentialoclcs::LiteralExpCS.__init__)


def test_essentialoclcs::literalexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::infixexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::InfixExpCS)


def test_essentialoclcs::infixexpcs_constructor_exists():
    assert callable(essentialoclcs::InfixExpCS.__init__)


def test_essentialoclcs::infixexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::InfixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::letexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::LetExpCS)


def test_essentialoclcs::letexpcs_constructor_exists():
    assert callable(essentialoclcs::LetExpCS.__init__)


def test_essentialoclcs::letexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::prefixexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::PrefixExpCS)


def test_essentialoclcs::prefixexpcs_constructor_exists():
    assert callable(essentialoclcs::PrefixExpCS.__init__)


def test_essentialoclcs::prefixexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::PrefixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::nestedexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NestedExpCS)


def test_essentialoclcs::nestedexpcs_constructor_exists():
    assert callable(essentialoclcs::NestedExpCS.__init__)


def test_essentialoclcs::nestedexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NestedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::selfexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::SelfExpCS)


def test_essentialoclcs::selfexpcs_constructor_exists():
    assert callable(essentialoclcs::SelfExpCS.__init__)


def test_essentialoclcs::selfexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::SelfExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs::selfexpcs_has_name():
    assert hasattr(essentialoclcs::SelfExpCS, "name")
    descriptor = None
    for klass in essentialoclcs::SelfExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::abstractnameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::AbstractNameExpCS)


def test_essentialoclcs::abstractnameexpcs_constructor_exists():
    assert callable(essentialoclcs::AbstractNameExpCS.__init__)


def test_essentialoclcs::abstractnameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::AbstractNameExpCS.__init__)
    params = list(sig.parameters.keys())

def test_navigationrole_exists():
    # Check that the Enumeration exists
    assert NavigationRole is not None

def test_navigationrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NavigationRole]
    expected_literals = [
        "ITERATOR",
        "ACCUMULATOR",
        "EXPRESSION",
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
essentialoclcs::Type_strategy = st.builds(
    essentialoclcs::Type,
)
BinaryOperatorCS_strategy = st.builds(
    BinaryOperatorCS,
)
essentialoclcs::NavigationOperatorCS_strategy = st.builds(
    essentialoclcs::NavigationOperatorCS,
)
essentialoclcs::PathNameCS_strategy = st.builds(
    essentialoclcs::PathNameCS,
)
AbstractNameExpCS_strategy = st.builds(
    AbstractNameExpCS,
)
essentialoclcs::NamedExpCS_strategy = st.builds(
    essentialoclcs::NamedExpCS,
)
essentialoclcs::NameExpCS_strategy = st.builds(
    essentialoclcs::NameExpCS,
    atPre=
        st.booleans()
)
VariableCS_strategy = st.builds(
    VariableCS,
)
essentialoclcs::TupleLiteralPartCS_strategy = st.builds(
    essentialoclcs::TupleLiteralPartCS,
)
SpecificationCS_strategy = st.builds(
    SpecificationCS,
)
essentialoclcs::ExpSpecificationCS_strategy = st.builds(
    essentialoclcs::ExpSpecificationCS,
)
RootCS_strategy = st.builds(
    RootCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
essentialoclcs::VariableCS_strategy = st.builds(
    essentialoclcs::VariableCS,
)
essentialoclcs::ContextCS_strategy = st.builds(
    essentialoclcs::ContextCS,
)
essentialoclcs::Property_strategy = st.builds(
    essentialoclcs::Property,
)
NamedExpCS_strategy = st.builds(
    NamedExpCS,
)
essentialoclcs::InvocationExpCS_strategy = st.builds(
    essentialoclcs::InvocationExpCS,
)
essentialoclcs::IndexExpCS_strategy = st.builds(
    essentialoclcs::IndexExpCS,
    atPre=
        st.booleans()
)
essentialoclcs::ConstructorExpCS_strategy = st.builds(
    essentialoclcs::ConstructorExpCS,
    value=
        safe_text
)
essentialoclcs::TypedRefCS_strategy = st.builds(
    essentialoclcs::TypedRefCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
essentialoclcs::TypeNameExpCS_strategy = st.builds(
    essentialoclcs::TypeNameExpCS,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
essentialoclcs::ConstructorPartCS_strategy = st.builds(
    essentialoclcs::ConstructorPartCS,
)
essentialoclcs::NavigatingArgCS_strategy = st.builds(
    essentialoclcs::NavigatingArgCS,
    role=
        safe_text,
    prefix=
        safe_text
)
essentialoclcs::CollectionLiteralPartCS_strategy = st.builds(
    essentialoclcs::CollectionLiteralPartCS,
)
essentialoclcs::CollectionTypeCS_strategy = st.builds(
    essentialoclcs::CollectionTypeCS,
    name=
        safe_text
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
essentialoclcs::PrimitiveLiteralExpCS_strategy = st.builds(
    essentialoclcs::PrimitiveLiteralExpCS,
)
essentialoclcs::TypeLiteralExpCS_strategy = st.builds(
    essentialoclcs::TypeLiteralExpCS,
)
essentialoclcs::TupleLiteralExpCS_strategy = st.builds(
    essentialoclcs::TupleLiteralExpCS,
)
essentialoclcs::CollectionLiteralExpCS_strategy = st.builds(
    essentialoclcs::CollectionLiteralExpCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
essentialoclcs::InvalidLiteralExpCS_strategy = st.builds(
    essentialoclcs::InvalidLiteralExpCS,
)
essentialoclcs::UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    essentialoclcs::UnlimitedNaturalLiteralExpCS,
)
essentialoclcs::StringLiteralExpCS_strategy = st.builds(
    essentialoclcs::StringLiteralExpCS,
    name=
        safe_text
)
essentialoclcs::NumberLiteralExpCS_strategy = st.builds(
    essentialoclcs::NumberLiteralExpCS,
    name=
        safe_text
)
essentialoclcs::NullLiteralExpCS_strategy = st.builds(
    essentialoclcs::NullLiteralExpCS,
)
essentialoclcs::BooleanLiteralExpCS_strategy = st.builds(
    essentialoclcs::BooleanLiteralExpCS,
    name=
        safe_text
)
essentialoclcs::ExpCS_strategy = st.builds(
    essentialoclcs::ExpCS,
)
OperatorCS_strategy = st.builds(
    OperatorCS,
)
essentialoclcs::UnaryOperatorCS_strategy = st.builds(
    essentialoclcs::UnaryOperatorCS,
)
essentialoclcs::BinaryOperatorCS_strategy = st.builds(
    essentialoclcs::BinaryOperatorCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
essentialoclcs::OperatorCS_strategy = st.builds(
    essentialoclcs::OperatorCS,
)
essentialoclcs::IfExpCS_strategy = st.builds(
    essentialoclcs::IfExpCS,
)
essentialoclcs::LetVariableCS_strategy = st.builds(
    essentialoclcs::LetVariableCS,
)
essentialoclcs::LiteralExpCS_strategy = st.builds(
    essentialoclcs::LiteralExpCS,
)
essentialoclcs::InfixExpCS_strategy = st.builds(
    essentialoclcs::InfixExpCS,
)
essentialoclcs::LetExpCS_strategy = st.builds(
    essentialoclcs::LetExpCS,
)
essentialoclcs::PrefixExpCS_strategy = st.builds(
    essentialoclcs::PrefixExpCS,
)
essentialoclcs::NestedExpCS_strategy = st.builds(
    essentialoclcs::NestedExpCS,
)
essentialoclcs::SelfExpCS_strategy = st.builds(
    essentialoclcs::SelfExpCS,
    name=
        safe_text
)
essentialoclcs::AbstractNameExpCS_strategy = st.builds(
    essentialoclcs::AbstractNameExpCS,
)

@given(instance=essentialoclcs::Type_strategy)
@settings(max_examples=50)
def test_essentialoclcs::type_instantiation(instance):
    assert isinstance(instance, essentialoclcs::Type)

@given(instance=BinaryOperatorCS_strategy)
@settings(max_examples=50)
def test_binaryoperatorcs_instantiation(instance):
    assert isinstance(instance, BinaryOperatorCS)

@given(instance=essentialoclcs::NavigationOperatorCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::navigationoperatorcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NavigationOperatorCS)

@given(instance=essentialoclcs::PathNameCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::pathnamecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::PathNameCS)

@given(instance=AbstractNameExpCS_strategy)
@settings(max_examples=50)
def test_abstractnameexpcs_instantiation(instance):
    assert isinstance(instance, AbstractNameExpCS)

@given(instance=essentialoclcs::NamedExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::namedexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NamedExpCS)

@given(instance=essentialoclcs::NameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::nameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NameExpCS)

@given(instance=essentialoclcs::NameExpCS_strategy)
def test_essentialoclcs::nameexpcs_atPre_type(instance):
    assert isinstance(instance.atPre, bool)


@given(instance=essentialoclcs::NameExpCS_strategy)
def test_essentialoclcs::nameexpcs_atPre_setter(instance):
    original = instance.atPre
    instance.atPre = original
    assert instance.atPre == original

@given(instance=VariableCS_strategy)
@settings(max_examples=50)
def test_variablecs_instantiation(instance):
    assert isinstance(instance, VariableCS)

@given(instance=essentialoclcs::TupleLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::tupleliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TupleLiteralPartCS)

@given(instance=SpecificationCS_strategy)
@settings(max_examples=50)
def test_specificationcs_instantiation(instance):
    assert isinstance(instance, SpecificationCS)

@given(instance=essentialoclcs::ExpSpecificationCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::expspecificationcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::ExpSpecificationCS)

@given(instance=RootCS_strategy)
@settings(max_examples=50)
def test_rootcs_instantiation(instance):
    assert isinstance(instance, RootCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=essentialoclcs::VariableCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::variablecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::VariableCS)

@given(instance=essentialoclcs::ContextCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::contextcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::ContextCS)

@given(instance=essentialoclcs::Property_strategy)
@settings(max_examples=50)
def test_essentialoclcs::property_instantiation(instance):
    assert isinstance(instance, essentialoclcs::Property)

@given(instance=NamedExpCS_strategy)
@settings(max_examples=50)
def test_namedexpcs_instantiation(instance):
    assert isinstance(instance, NamedExpCS)

@given(instance=essentialoclcs::InvocationExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::invocationexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::InvocationExpCS)

@given(instance=essentialoclcs::IndexExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::indexexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::IndexExpCS)

@given(instance=essentialoclcs::IndexExpCS_strategy)
def test_essentialoclcs::indexexpcs_atPre_type(instance):
    assert isinstance(instance.atPre, bool)


@given(instance=essentialoclcs::IndexExpCS_strategy)
def test_essentialoclcs::indexexpcs_atPre_setter(instance):
    original = instance.atPre
    instance.atPre = original
    assert instance.atPre == original

@given(instance=essentialoclcs::ConstructorExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::constructorexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::ConstructorExpCS)

@given(instance=essentialoclcs::ConstructorExpCS_strategy)
def test_essentialoclcs::constructorexpcs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=essentialoclcs::ConstructorExpCS_strategy)
def test_essentialoclcs::constructorexpcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=essentialoclcs::TypedRefCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::typedrefcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TypedRefCS)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=TypedRefCS_strategy)
@settings(max_examples=50)
def test_typedrefcs_instantiation(instance):
    assert isinstance(instance, TypedRefCS)

@given(instance=essentialoclcs::TypeNameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::typenameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TypeNameExpCS)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=essentialoclcs::ConstructorPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::constructorpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::ConstructorPartCS)

@given(instance=essentialoclcs::NavigatingArgCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::navigatingargcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NavigatingArgCS)

@given(instance=essentialoclcs::NavigatingArgCS_strategy)
def test_essentialoclcs::navigatingargcs_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=essentialoclcs::NavigatingArgCS_strategy)
def test_essentialoclcs::navigatingargcs_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=essentialoclcs::NavigatingArgCS_strategy)
def test_essentialoclcs::navigatingargcs_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=essentialoclcs::NavigatingArgCS_strategy)
def test_essentialoclcs::navigatingargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=essentialoclcs::CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::CollectionLiteralPartCS)

@given(instance=essentialoclcs::CollectionTypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::collectiontypecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::CollectionTypeCS)

@given(instance=essentialoclcs::CollectionTypeCS_strategy)
def test_essentialoclcs::collectiontypecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=essentialoclcs::CollectionTypeCS_strategy)
def test_essentialoclcs::collectiontypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=essentialoclcs::PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::PrimitiveLiteralExpCS)

@given(instance=essentialoclcs::TypeLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::typeliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TypeLiteralExpCS)

@given(instance=essentialoclcs::TupleLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::tupleliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TupleLiteralExpCS)

@given(instance=essentialoclcs::CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::CollectionLiteralExpCS)

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=essentialoclcs::InvalidLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::invalidliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::InvalidLiteralExpCS)

@given(instance=essentialoclcs::UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::unlimitednaturalliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::UnlimitedNaturalLiteralExpCS)

@given(instance=essentialoclcs::StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::StringLiteralExpCS)

@given(instance=essentialoclcs::StringLiteralExpCS_strategy)
def test_essentialoclcs::stringliteralexpcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=essentialoclcs::StringLiteralExpCS_strategy)
def test_essentialoclcs::stringliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs::NumberLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::numberliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NumberLiteralExpCS)

@given(instance=essentialoclcs::NumberLiteralExpCS_strategy)
def test_essentialoclcs::numberliteralexpcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=essentialoclcs::NumberLiteralExpCS_strategy)
def test_essentialoclcs::numberliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs::NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NullLiteralExpCS)

@given(instance=essentialoclcs::BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::BooleanLiteralExpCS)

@given(instance=essentialoclcs::BooleanLiteralExpCS_strategy)
def test_essentialoclcs::booleanliteralexpcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=essentialoclcs::BooleanLiteralExpCS_strategy)
def test_essentialoclcs::booleanliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs::ExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::expcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::ExpCS)

@given(instance=OperatorCS_strategy)
@settings(max_examples=50)
def test_operatorcs_instantiation(instance):
    assert isinstance(instance, OperatorCS)

@given(instance=essentialoclcs::UnaryOperatorCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::unaryoperatorcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::UnaryOperatorCS)

@given(instance=essentialoclcs::BinaryOperatorCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::binaryoperatorcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::BinaryOperatorCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=essentialoclcs::OperatorCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::operatorcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::OperatorCS)

@given(instance=essentialoclcs::IfExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::ifexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::IfExpCS)

@given(instance=essentialoclcs::LetVariableCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::letvariablecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::LetVariableCS)

@given(instance=essentialoclcs::LiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::literalexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::LiteralExpCS)

@given(instance=essentialoclcs::InfixExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::infixexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::InfixExpCS)

@given(instance=essentialoclcs::LetExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::letexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::LetExpCS)

@given(instance=essentialoclcs::PrefixExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::prefixexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::PrefixExpCS)

@given(instance=essentialoclcs::NestedExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::nestedexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NestedExpCS)

@given(instance=essentialoclcs::SelfExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::selfexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::SelfExpCS)

@given(instance=essentialoclcs::SelfExpCS_strategy)
def test_essentialoclcs::selfexpcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=essentialoclcs::SelfExpCS_strategy)
def test_essentialoclcs::selfexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs::AbstractNameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::abstractnameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::AbstractNameExpCS)

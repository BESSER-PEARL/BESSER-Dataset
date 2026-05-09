import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myAtl::EObject,
    NavigatingExpCS,
    myAtl::NavigatingExpCS::Base,
    NavigatingExpCS::Base,
    myAtl::IndexExpCS,
    myAtl::UnaryOperatorCS,
    InfixedExpCS,
    myAtl::InfixExpCS,
    myAtl::PrefixedExpCS,
    BinaryOperatorCS,
    myAtl::NavigationOperatorCS,
    myAtl::InfixOperatorCS,
    myAtl::BinaryOperatorCS,
    ExpCS,
    myAtl::InfixedExpCS,
    NavigatingArgExpCS,
    IndexExpCS,
    PrefixedExpCS,
    myAtl::PrefixExpCS,
    myAtl::PrimaryExpCS,
    myAtl::LetVariableCS,
    myAtl::NavigatingSemiArgCS,
    myAtl::NavigatingCommaArgCS,
    myAtl::NavigatingBarArgCS,
    myAtl::NavigatingArgExpCS,
    myAtl::NavigatingArgCS,
    myAtl::TypeLiteralExpCS,
    TypeExpCS,
    myAtl::TypeNameExpCS,
    myAtl::TypeLiteralCS,
    PrimitiveLiteralExpCS,
    myAtl::BooleanLiteralExpCS,
    myAtl::UnlimitedNaturalLiteralExpCS,
    myAtl::StringLiteralExpCS,
    myAtl::NullLiteralExpCS,
    myAtl::InvalidLiteralExpCS,
    myAtl::NumberLiteralExpCS,
    myAtl::TupleLiteralPartCS,
    PrimaryExpCS,
    myAtl::StringExpCs,
    myAtl::NavigatingExpCS,
    myAtl::IfExpCS,
    myAtl::SelfExpCS,
    myAtl::TupleLiteralExpCS,
    myAtl::LetExpCS,
    myAtl::NestedExpCS,
    myAtl::PrimitiveLiteralExpCS,
    myAtl::tuplePartCS,
    TypeLiteralCS,
    myAtl::PrimitiveTypeCS,
    myAtl::TupleTypeCS,
    myAtl::CollectionTypeCS,
    myAtl::TypeExpCS,
    Statement,
    myAtl::BindingStat,
    myAtl::Statement,
    myAtl::Binding,
    OutPatternElement,
    myAtl::ForEachOutPatternElement,
    myAtl::SimpleOutPatternElement,
    myAtl::OutPatternElement,
    myAtl::InPatternElement,
    myAtl::ATLType,
    myAtl::ATLDefCS,
    myAtl::ExpCS,
    myAtl::ATLParameterCS,
    myAtl::ActionBlock,
    myAtl::OutPattern,
    myAtl::RuleVariableDeclaration,
    myAtl::InPattern,
    ModuleElement,
    myAtl::Helper,
    myAtl::QueryRule,
    myAtl::CalledRule,
    myAtl::MatchedRule,
    myAtl::ModuleElement,
    myAtl::NameExpCS,
    myAtl::Module,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myatl::eobject_is_not_abstract():
    assert not inspect.isabstract(myAtl::EObject)


def test_myatl::eobject_constructor_exists():
    assert callable(myAtl::EObject.__init__)


def test_myatl::eobject_constructor_args():
    sig = inspect.signature(myAtl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_navigatingexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigatingExpCS)


def test_navigatingexpcs_constructor_exists():
    assert callable(NavigatingExpCS.__init__)


def test_navigatingexpcs_constructor_args():
    sig = inspect.signature(NavigatingExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::navigatingexpcs::base_is_not_abstract():
    assert not inspect.isabstract(myAtl::NavigatingExpCS::Base)


def test_myatl::navigatingexpcs::base_constructor_exists():
    assert callable(myAtl::NavigatingExpCS::Base.__init__)


def test_myatl::navigatingexpcs::base_constructor_args():
    sig = inspect.signature(myAtl::NavigatingExpCS::Base.__init__)
    params = list(sig.parameters.keys())



def test_navigatingexpcs::base_is_not_abstract():
    assert not inspect.isabstract(NavigatingExpCS::Base)


def test_navigatingexpcs::base_constructor_exists():
    assert callable(NavigatingExpCS::Base.__init__)


def test_navigatingexpcs::base_constructor_args():
    sig = inspect.signature(NavigatingExpCS::Base.__init__)
    params = list(sig.parameters.keys())



def test_myatl::indexexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::IndexExpCS)


def test_myatl::indexexpcs_constructor_exists():
    assert callable(myAtl::IndexExpCS.__init__)


def test_myatl::indexexpcs_constructor_args():
    sig = inspect.signature(myAtl::IndexExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::unaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::UnaryOperatorCS)


def test_myatl::unaryoperatorcs_constructor_exists():
    assert callable(myAtl::UnaryOperatorCS.__init__)


def test_myatl::unaryoperatorcs_constructor_args():
    sig = inspect.signature(myAtl::UnaryOperatorCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::unaryoperatorcs_has_name():
    assert hasattr(myAtl::UnaryOperatorCS, "name")
    descriptor = None
    for klass in myAtl::UnaryOperatorCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_infixedexpcs_is_not_abstract():
    assert not inspect.isabstract(InfixedExpCS)


def test_infixedexpcs_constructor_exists():
    assert callable(InfixedExpCS.__init__)


def test_infixedexpcs_constructor_args():
    sig = inspect.signature(InfixedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::infixexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::InfixExpCS)


def test_myatl::infixexpcs_constructor_exists():
    assert callable(myAtl::InfixExpCS.__init__)


def test_myatl::infixexpcs_constructor_args():
    sig = inspect.signature(myAtl::InfixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::prefixedexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::PrefixedExpCS)


def test_myatl::prefixedexpcs_constructor_exists():
    assert callable(myAtl::PrefixedExpCS.__init__)


def test_myatl::prefixedexpcs_constructor_args():
    sig = inspect.signature(myAtl::PrefixedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorCS)


def test_binaryoperatorcs_constructor_exists():
    assert callable(BinaryOperatorCS.__init__)


def test_binaryoperatorcs_constructor_args():
    sig = inspect.signature(BinaryOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::navigationoperatorcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NavigationOperatorCS)


def test_myatl::navigationoperatorcs_constructor_exists():
    assert callable(myAtl::NavigationOperatorCS.__init__)


def test_myatl::navigationoperatorcs_constructor_args():
    sig = inspect.signature(myAtl::NavigationOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::infixoperatorcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::InfixOperatorCS)


def test_myatl::infixoperatorcs_constructor_exists():
    assert callable(myAtl::InfixOperatorCS.__init__)


def test_myatl::infixoperatorcs_constructor_args():
    sig = inspect.signature(myAtl::InfixOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::binaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::BinaryOperatorCS)


def test_myatl::binaryoperatorcs_constructor_exists():
    assert callable(myAtl::BinaryOperatorCS.__init__)


def test_myatl::binaryoperatorcs_constructor_args():
    sig = inspect.signature(myAtl::BinaryOperatorCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::binaryoperatorcs_has_name():
    assert hasattr(myAtl::BinaryOperatorCS, "name")
    descriptor = None
    for klass in myAtl::BinaryOperatorCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::infixedexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::InfixedExpCS)


def test_myatl::infixedexpcs_constructor_exists():
    assert callable(myAtl::InfixedExpCS.__init__)


def test_myatl::infixedexpcs_constructor_args():
    sig = inspect.signature(myAtl::InfixedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_navigatingargexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigatingArgExpCS)


def test_navigatingargexpcs_constructor_exists():
    assert callable(NavigatingArgExpCS.__init__)


def test_navigatingargexpcs_constructor_args():
    sig = inspect.signature(NavigatingArgExpCS.__init__)
    params = list(sig.parameters.keys())



def test_indexexpcs_is_not_abstract():
    assert not inspect.isabstract(IndexExpCS)


def test_indexexpcs_constructor_exists():
    assert callable(IndexExpCS.__init__)


def test_indexexpcs_constructor_args():
    sig = inspect.signature(IndexExpCS.__init__)
    params = list(sig.parameters.keys())



def test_prefixedexpcs_is_not_abstract():
    assert not inspect.isabstract(PrefixedExpCS)


def test_prefixedexpcs_constructor_exists():
    assert callable(PrefixedExpCS.__init__)


def test_prefixedexpcs_constructor_args():
    sig = inspect.signature(PrefixedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::prefixexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::PrefixExpCS)


def test_myatl::prefixexpcs_constructor_exists():
    assert callable(myAtl::PrefixExpCS.__init__)


def test_myatl::prefixexpcs_constructor_args():
    sig = inspect.signature(myAtl::PrefixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::PrimaryExpCS)


def test_myatl::primaryexpcs_constructor_exists():
    assert callable(myAtl::PrimaryExpCS.__init__)


def test_myatl::primaryexpcs_constructor_args():
    sig = inspect.signature(myAtl::PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::letvariablecs_is_not_abstract():
    assert not inspect.isabstract(myAtl::LetVariableCS)


def test_myatl::letvariablecs_constructor_exists():
    assert callable(myAtl::LetVariableCS.__init__)


def test_myatl::letvariablecs_constructor_args():
    sig = inspect.signature(myAtl::LetVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::letvariablecs_has_name():
    assert hasattr(myAtl::LetVariableCS, "name")
    descriptor = None
    for klass in myAtl::LetVariableCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl::navigatingsemiargcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NavigatingSemiArgCS)


def test_myatl::navigatingsemiargcs_constructor_exists():
    assert callable(myAtl::NavigatingSemiArgCS.__init__)


def test_myatl::navigatingsemiargcs_constructor_args():
    sig = inspect.signature(myAtl::NavigatingSemiArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_myatl::navigatingsemiargcs_has_prefix():
    assert hasattr(myAtl::NavigatingSemiArgCS, "prefix")
    descriptor = None
    for klass in myAtl::NavigatingSemiArgCS.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_myatl::navigatingcommaargcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NavigatingCommaArgCS)


def test_myatl::navigatingcommaargcs_constructor_exists():
    assert callable(myAtl::NavigatingCommaArgCS.__init__)


def test_myatl::navigatingcommaargcs_constructor_args():
    sig = inspect.signature(myAtl::NavigatingCommaArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_myatl::navigatingcommaargcs_has_prefix():
    assert hasattr(myAtl::NavigatingCommaArgCS, "prefix")
    descriptor = None
    for klass in myAtl::NavigatingCommaArgCS.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_myatl::navigatingbarargcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NavigatingBarArgCS)


def test_myatl::navigatingbarargcs_constructor_exists():
    assert callable(myAtl::NavigatingBarArgCS.__init__)


def test_myatl::navigatingbarargcs_constructor_args():
    sig = inspect.signature(myAtl::NavigatingBarArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_myatl::navigatingbarargcs_has_prefix():
    assert hasattr(myAtl::NavigatingBarArgCS, "prefix")
    descriptor = None
    for klass in myAtl::NavigatingBarArgCS.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_myatl::navigatingargexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NavigatingArgExpCS)


def test_myatl::navigatingargexpcs_constructor_exists():
    assert callable(myAtl::NavigatingArgExpCS.__init__)


def test_myatl::navigatingargexpcs_constructor_args():
    sig = inspect.signature(myAtl::NavigatingArgExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::navigatingargcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NavigatingArgCS)


def test_myatl::navigatingargcs_constructor_exists():
    assert callable(myAtl::NavigatingArgCS.__init__)


def test_myatl::navigatingargcs_constructor_args():
    sig = inspect.signature(myAtl::NavigatingArgCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::TypeLiteralExpCS)


def test_myatl::typeliteralexpcs_constructor_exists():
    assert callable(myAtl::TypeLiteralExpCS.__init__)


def test_myatl::typeliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl::TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_typeexpcs_is_not_abstract():
    assert not inspect.isabstract(TypeExpCS)


def test_typeexpcs_constructor_exists():
    assert callable(TypeExpCS.__init__)


def test_typeexpcs_constructor_args():
    sig = inspect.signature(TypeExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::typenameexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::TypeNameExpCS)


def test_myatl::typenameexpcs_constructor_exists():
    assert callable(myAtl::TypeNameExpCS.__init__)


def test_myatl::typenameexpcs_constructor_args():
    sig = inspect.signature(myAtl::TypeNameExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "element" in params, "Missing parameter 'element'"

def test_myatl::typenameexpcs_has_namespace():
    assert hasattr(myAtl::TypeNameExpCS, "namespace")
    descriptor = None
    for klass in myAtl::TypeNameExpCS.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_myatl::typenameexpcs_has_element():
    assert hasattr(myAtl::TypeNameExpCS, "element")
    descriptor = None
    for klass in myAtl::TypeNameExpCS.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_myatl::typeliteralcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::TypeLiteralCS)


def test_myatl::typeliteralcs_constructor_exists():
    assert callable(myAtl::TypeLiteralCS.__init__)


def test_myatl::typeliteralcs_constructor_args():
    sig = inspect.signature(myAtl::TypeLiteralCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::typeliteralcs_has_name():
    assert hasattr(myAtl::TypeLiteralCS, "name")
    descriptor = None
    for klass in myAtl::TypeLiteralCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::BooleanLiteralExpCS)


def test_myatl::booleanliteralexpcs_constructor_exists():
    assert callable(myAtl::BooleanLiteralExpCS.__init__)


def test_myatl::booleanliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl::BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::booleanliteralexpcs_has_name():
    assert hasattr(myAtl::BooleanLiteralExpCS, "name")
    descriptor = None
    for klass in myAtl::BooleanLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl::unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::UnlimitedNaturalLiteralExpCS)


def test_myatl::unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(myAtl::UnlimitedNaturalLiteralExpCS.__init__)


def test_myatl::unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl::UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::StringLiteralExpCS)


def test_myatl::stringliteralexpcs_constructor_exists():
    assert callable(myAtl::StringLiteralExpCS.__init__)


def test_myatl::stringliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl::StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::stringliteralexpcs_has_name():
    assert hasattr(myAtl::StringLiteralExpCS, "name")
    descriptor = None
    for klass in myAtl::StringLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl::nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NullLiteralExpCS)


def test_myatl::nullliteralexpcs_constructor_exists():
    assert callable(myAtl::NullLiteralExpCS.__init__)


def test_myatl::nullliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl::NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::InvalidLiteralExpCS)


def test_myatl::invalidliteralexpcs_constructor_exists():
    assert callable(myAtl::InvalidLiteralExpCS.__init__)


def test_myatl::invalidliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl::InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::numberliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NumberLiteralExpCS)


def test_myatl::numberliteralexpcs_constructor_exists():
    assert callable(myAtl::NumberLiteralExpCS.__init__)


def test_myatl::numberliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl::NumberLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::numberliteralexpcs_has_name():
    assert hasattr(myAtl::NumberLiteralExpCS, "name")
    descriptor = None
    for klass in myAtl::NumberLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl::tupleliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::TupleLiteralPartCS)


def test_myatl::tupleliteralpartcs_constructor_exists():
    assert callable(myAtl::TupleLiteralPartCS.__init__)


def test_myatl::tupleliteralpartcs_constructor_args():
    sig = inspect.signature(myAtl::TupleLiteralPartCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::tupleliteralpartcs_has_name():
    assert hasattr(myAtl::TupleLiteralPartCS, "name")
    descriptor = None
    for klass in myAtl::TupleLiteralPartCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::stringexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::StringExpCs)


def test_myatl::stringexpcs_constructor_exists():
    assert callable(myAtl::StringExpCs.__init__)


def test_myatl::stringexpcs_constructor_args():
    sig = inspect.signature(myAtl::StringExpCs.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::stringexpcs_has_name():
    assert hasattr(myAtl::StringExpCs, "name")
    descriptor = None
    for klass in myAtl::StringExpCs.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl::navigatingexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NavigatingExpCS)


def test_myatl::navigatingexpcs_constructor_exists():
    assert callable(myAtl::NavigatingExpCS.__init__)


def test_myatl::navigatingexpcs_constructor_args():
    sig = inspect.signature(myAtl::NavigatingExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::ifexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::IfExpCS)


def test_myatl::ifexpcs_constructor_exists():
    assert callable(myAtl::IfExpCS.__init__)


def test_myatl::ifexpcs_constructor_args():
    sig = inspect.signature(myAtl::IfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::selfexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::SelfExpCS)


def test_myatl::selfexpcs_constructor_exists():
    assert callable(myAtl::SelfExpCS.__init__)


def test_myatl::selfexpcs_constructor_args():
    sig = inspect.signature(myAtl::SelfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::TupleLiteralExpCS)


def test_myatl::tupleliteralexpcs_constructor_exists():
    assert callable(myAtl::TupleLiteralExpCS.__init__)


def test_myatl::tupleliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl::TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::letexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::LetExpCS)


def test_myatl::letexpcs_constructor_exists():
    assert callable(myAtl::LetExpCS.__init__)


def test_myatl::letexpcs_constructor_args():
    sig = inspect.signature(myAtl::LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::nestedexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NestedExpCS)


def test_myatl::nestedexpcs_constructor_exists():
    assert callable(myAtl::NestedExpCS.__init__)


def test_myatl::nestedexpcs_constructor_args():
    sig = inspect.signature(myAtl::NestedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::PrimitiveLiteralExpCS)


def test_myatl::primitiveliteralexpcs_constructor_exists():
    assert callable(myAtl::PrimitiveLiteralExpCS.__init__)


def test_myatl::primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl::PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::tuplepartcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::tuplePartCS)


def test_myatl::tuplepartcs_constructor_exists():
    assert callable(myAtl::tuplePartCS.__init__)


def test_myatl::tuplepartcs_constructor_args():
    sig = inspect.signature(myAtl::tuplePartCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::tuplepartcs_has_name():
    assert hasattr(myAtl::tuplePartCS, "name")
    descriptor = None
    for klass in myAtl::tuplePartCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeliteralcs_is_not_abstract():
    assert not inspect.isabstract(TypeLiteralCS)


def test_typeliteralcs_constructor_exists():
    assert callable(TypeLiteralCS.__init__)


def test_typeliteralcs_constructor_args():
    sig = inspect.signature(TypeLiteralCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::primitivetypecs_is_not_abstract():
    assert not inspect.isabstract(myAtl::PrimitiveTypeCS)


def test_myatl::primitivetypecs_constructor_exists():
    assert callable(myAtl::PrimitiveTypeCS.__init__)


def test_myatl::primitivetypecs_constructor_args():
    sig = inspect.signature(myAtl::PrimitiveTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::tupletypecs_is_not_abstract():
    assert not inspect.isabstract(myAtl::TupleTypeCS)


def test_myatl::tupletypecs_constructor_exists():
    assert callable(myAtl::TupleTypeCS.__init__)


def test_myatl::tupletypecs_constructor_args():
    sig = inspect.signature(myAtl::TupleTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "backtrack" in params, "Missing parameter 'backtrack'"

def test_myatl::tupletypecs_has_backtrack():
    assert hasattr(myAtl::TupleTypeCS, "backtrack")
    descriptor = None
    for klass in myAtl::TupleTypeCS.__mro__:
        if "backtrack" in klass.__dict__:
            descriptor = klass.__dict__["backtrack"]
            break
    assert isinstance(descriptor, property)



def test_myatl::collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(myAtl::CollectionTypeCS)


def test_myatl::collectiontypecs_constructor_exists():
    assert callable(myAtl::CollectionTypeCS.__init__)


def test_myatl::collectiontypecs_constructor_args():
    sig = inspect.signature(myAtl::CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::typeexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::TypeExpCS)


def test_myatl::typeexpcs_constructor_exists():
    assert callable(myAtl::TypeExpCS.__init__)


def test_myatl::typeexpcs_constructor_args():
    sig = inspect.signature(myAtl::TypeExpCS.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_myatl::bindingstat_is_not_abstract():
    assert not inspect.isabstract(myAtl::BindingStat)


def test_myatl::bindingstat_constructor_exists():
    assert callable(myAtl::BindingStat.__init__)


def test_myatl::bindingstat_constructor_args():
    sig = inspect.signature(myAtl::BindingStat.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_myatl::bindingstat_has_propertyName():
    assert hasattr(myAtl::BindingStat, "propertyName")
    descriptor = None
    for klass in myAtl::BindingStat.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_myatl::statement_is_not_abstract():
    assert not inspect.isabstract(myAtl::Statement)


def test_myatl::statement_constructor_exists():
    assert callable(myAtl::Statement.__init__)


def test_myatl::statement_constructor_args():
    sig = inspect.signature(myAtl::Statement.__init__)
    params = list(sig.parameters.keys())



def test_myatl::binding_is_not_abstract():
    assert not inspect.isabstract(myAtl::Binding)


def test_myatl::binding_constructor_exists():
    assert callable(myAtl::Binding.__init__)


def test_myatl::binding_constructor_args():
    sig = inspect.signature(myAtl::Binding.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_myatl::binding_has_propertyName():
    assert hasattr(myAtl::Binding, "propertyName")
    descriptor = None
    for klass in myAtl::Binding.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(OutPatternElement)


def test_outpatternelement_constructor_exists():
    assert callable(OutPatternElement.__init__)


def test_outpatternelement_constructor_args():
    sig = inspect.signature(OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_myatl::foreachoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(myAtl::ForEachOutPatternElement)


def test_myatl::foreachoutpatternelement_constructor_exists():
    assert callable(myAtl::ForEachOutPatternElement.__init__)


def test_myatl::foreachoutpatternelement_constructor_args():
    sig = inspect.signature(myAtl::ForEachOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_myatl::simpleoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(myAtl::SimpleOutPatternElement)


def test_myatl::simpleoutpatternelement_constructor_exists():
    assert callable(myAtl::SimpleOutPatternElement.__init__)


def test_myatl::simpleoutpatternelement_constructor_args():
    sig = inspect.signature(myAtl::SimpleOutPatternElement.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_myatl::simpleoutpatternelement_has_varName():
    assert hasattr(myAtl::SimpleOutPatternElement, "varName")
    descriptor = None
    for klass in myAtl::SimpleOutPatternElement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_myatl::outpatternelement_is_not_abstract():
    assert not inspect.isabstract(myAtl::OutPatternElement)


def test_myatl::outpatternelement_constructor_exists():
    assert callable(myAtl::OutPatternElement.__init__)


def test_myatl::outpatternelement_constructor_args():
    sig = inspect.signature(myAtl::OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_myatl::inpatternelement_is_not_abstract():
    assert not inspect.isabstract(myAtl::InPatternElement)


def test_myatl::inpatternelement_constructor_exists():
    assert callable(myAtl::InPatternElement.__init__)


def test_myatl::inpatternelement_constructor_args():
    sig = inspect.signature(myAtl::InPatternElement.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_myatl::inpatternelement_has_varName():
    assert hasattr(myAtl::InPatternElement, "varName")
    descriptor = None
    for klass in myAtl::InPatternElement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_myatl::atltype_is_not_abstract():
    assert not inspect.isabstract(myAtl::ATLType)


def test_myatl::atltype_constructor_exists():
    assert callable(myAtl::ATLType.__init__)


def test_myatl::atltype_constructor_args():
    sig = inspect.signature(myAtl::ATLType.__init__)
    params = list(sig.parameters.keys())
    assert "modelName" in params, "Missing parameter 'modelName'"

def test_myatl::atltype_has_modelName():
    assert hasattr(myAtl::ATLType, "modelName")
    descriptor = None
    for klass in myAtl::ATLType.__mro__:
        if "modelName" in klass.__dict__:
            descriptor = klass.__dict__["modelName"]
            break
    assert isinstance(descriptor, property)



def test_myatl::atldefcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::ATLDefCS)


def test_myatl::atldefcs_constructor_exists():
    assert callable(myAtl::ATLDefCS.__init__)


def test_myatl::atldefcs_constructor_args():
    sig = inspect.signature(myAtl::ATLDefCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_myatl::atldefcs_has_varName():
    assert hasattr(myAtl::ATLDefCS, "varName")
    descriptor = None
    for klass in myAtl::ATLDefCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_myatl::expcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::ExpCS)


def test_myatl::expcs_constructor_exists():
    assert callable(myAtl::ExpCS.__init__)


def test_myatl::expcs_constructor_args():
    sig = inspect.signature(myAtl::ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl::atlparametercs_is_not_abstract():
    assert not inspect.isabstract(myAtl::ATLParameterCS)


def test_myatl::atlparametercs_constructor_exists():
    assert callable(myAtl::ATLParameterCS.__init__)


def test_myatl::atlparametercs_constructor_args():
    sig = inspect.signature(myAtl::ATLParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_myatl::atlparametercs_has_varName():
    assert hasattr(myAtl::ATLParameterCS, "varName")
    descriptor = None
    for klass in myAtl::ATLParameterCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_myatl::actionblock_is_not_abstract():
    assert not inspect.isabstract(myAtl::ActionBlock)


def test_myatl::actionblock_constructor_exists():
    assert callable(myAtl::ActionBlock.__init__)


def test_myatl::actionblock_constructor_args():
    sig = inspect.signature(myAtl::ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_myatl::outpattern_is_not_abstract():
    assert not inspect.isabstract(myAtl::OutPattern)


def test_myatl::outpattern_constructor_exists():
    assert callable(myAtl::OutPattern.__init__)


def test_myatl::outpattern_constructor_args():
    sig = inspect.signature(myAtl::OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_myatl::rulevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(myAtl::RuleVariableDeclaration)


def test_myatl::rulevariabledeclaration_constructor_exists():
    assert callable(myAtl::RuleVariableDeclaration.__init__)


def test_myatl::rulevariabledeclaration_constructor_args():
    sig = inspect.signature(myAtl::RuleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_myatl::rulevariabledeclaration_has_varName():
    assert hasattr(myAtl::RuleVariableDeclaration, "varName")
    descriptor = None
    for klass in myAtl::RuleVariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_myatl::inpattern_is_not_abstract():
    assert not inspect.isabstract(myAtl::InPattern)


def test_myatl::inpattern_constructor_exists():
    assert callable(myAtl::InPattern.__init__)


def test_myatl::inpattern_constructor_args():
    sig = inspect.signature(myAtl::InPattern.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_myatl::helper_is_not_abstract():
    assert not inspect.isabstract(myAtl::Helper)


def test_myatl::helper_constructor_exists():
    assert callable(myAtl::Helper.__init__)


def test_myatl::helper_constructor_args():
    sig = inspect.signature(myAtl::Helper.__init__)
    params = list(sig.parameters.keys())



def test_myatl::queryrule_is_not_abstract():
    assert not inspect.isabstract(myAtl::QueryRule)


def test_myatl::queryrule_constructor_exists():
    assert callable(myAtl::QueryRule.__init__)


def test_myatl::queryrule_constructor_args():
    sig = inspect.signature(myAtl::QueryRule.__init__)
    params = list(sig.parameters.keys())



def test_myatl::calledrule_is_not_abstract():
    assert not inspect.isabstract(myAtl::CalledRule)


def test_myatl::calledrule_constructor_exists():
    assert callable(myAtl::CalledRule.__init__)


def test_myatl::calledrule_constructor_args():
    sig = inspect.signature(myAtl::CalledRule.__init__)
    params = list(sig.parameters.keys())



def test_myatl::matchedrule_is_not_abstract():
    assert not inspect.isabstract(myAtl::MatchedRule)


def test_myatl::matchedrule_constructor_exists():
    assert callable(myAtl::MatchedRule.__init__)


def test_myatl::matchedrule_constructor_args():
    sig = inspect.signature(myAtl::MatchedRule.__init__)
    params = list(sig.parameters.keys())



def test_myatl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(myAtl::ModuleElement)


def test_myatl::moduleelement_constructor_exists():
    assert callable(myAtl::ModuleElement.__init__)


def test_myatl::moduleelement_constructor_args():
    sig = inspect.signature(myAtl::ModuleElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::moduleelement_has_name():
    assert hasattr(myAtl::ModuleElement, "name")
    descriptor = None
    for klass in myAtl::ModuleElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl::nameexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl::NameExpCS)


def test_myatl::nameexpcs_constructor_exists():
    assert callable(myAtl::NameExpCS.__init__)


def test_myatl::nameexpcs_constructor_args():
    sig = inspect.signature(myAtl::NameExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "element" in params, "Missing parameter 'element'"

def test_myatl::nameexpcs_has_namespace():
    assert hasattr(myAtl::NameExpCS, "namespace")
    descriptor = None
    for klass in myAtl::NameExpCS.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_myatl::nameexpcs_has_element():
    assert hasattr(myAtl::NameExpCS, "element")
    descriptor = None
    for klass in myAtl::NameExpCS.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_myatl::module_is_not_abstract():
    assert not inspect.isabstract(myAtl::Module)


def test_myatl::module_constructor_exists():
    assert callable(myAtl::Module.__init__)


def test_myatl::module_constructor_args():
    sig = inspect.signature(myAtl::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl::module_has_name():
    assert hasattr(myAtl::Module, "name")
    descriptor = None
    for klass in myAtl::Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
myAtl::EObject_strategy = st.builds(
    myAtl::EObject,
)
NavigatingExpCS_strategy = st.builds(
    NavigatingExpCS,
)
myAtl::NavigatingExpCS::Base_strategy = st.builds(
    myAtl::NavigatingExpCS::Base,
)
NavigatingExpCS::Base_strategy = st.builds(
    NavigatingExpCS::Base,
)
myAtl::IndexExpCS_strategy = st.builds(
    myAtl::IndexExpCS,
)
myAtl::UnaryOperatorCS_strategy = st.builds(
    myAtl::UnaryOperatorCS,
    name=
        safe_text
)
InfixedExpCS_strategy = st.builds(
    InfixedExpCS,
)
myAtl::InfixExpCS_strategy = st.builds(
    myAtl::InfixExpCS,
)
myAtl::PrefixedExpCS_strategy = st.builds(
    myAtl::PrefixedExpCS,
)
BinaryOperatorCS_strategy = st.builds(
    BinaryOperatorCS,
)
myAtl::NavigationOperatorCS_strategy = st.builds(
    myAtl::NavigationOperatorCS,
)
myAtl::InfixOperatorCS_strategy = st.builds(
    myAtl::InfixOperatorCS,
)
myAtl::BinaryOperatorCS_strategy = st.builds(
    myAtl::BinaryOperatorCS,
    name=
        safe_text
)
ExpCS_strategy = st.builds(
    ExpCS,
)
myAtl::InfixedExpCS_strategy = st.builds(
    myAtl::InfixedExpCS,
)
NavigatingArgExpCS_strategy = st.builds(
    NavigatingArgExpCS,
)
IndexExpCS_strategy = st.builds(
    IndexExpCS,
)
PrefixedExpCS_strategy = st.builds(
    PrefixedExpCS,
)
myAtl::PrefixExpCS_strategy = st.builds(
    myAtl::PrefixExpCS,
)
myAtl::PrimaryExpCS_strategy = st.builds(
    myAtl::PrimaryExpCS,
)
myAtl::LetVariableCS_strategy = st.builds(
    myAtl::LetVariableCS,
    name=
        safe_text
)
myAtl::NavigatingSemiArgCS_strategy = st.builds(
    myAtl::NavigatingSemiArgCS,
    prefix=
        safe_text
)
myAtl::NavigatingCommaArgCS_strategy = st.builds(
    myAtl::NavigatingCommaArgCS,
    prefix=
        safe_text
)
myAtl::NavigatingBarArgCS_strategy = st.builds(
    myAtl::NavigatingBarArgCS,
    prefix=
        safe_text
)
myAtl::NavigatingArgExpCS_strategy = st.builds(
    myAtl::NavigatingArgExpCS,
)
myAtl::NavigatingArgCS_strategy = st.builds(
    myAtl::NavigatingArgCS,
)
myAtl::TypeLiteralExpCS_strategy = st.builds(
    myAtl::TypeLiteralExpCS,
)
TypeExpCS_strategy = st.builds(
    TypeExpCS,
)
myAtl::TypeNameExpCS_strategy = st.builds(
    myAtl::TypeNameExpCS,
    namespace=
        safe_text,
    element=
        safe_text
)
myAtl::TypeLiteralCS_strategy = st.builds(
    myAtl::TypeLiteralCS,
    name=
        safe_text
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
myAtl::BooleanLiteralExpCS_strategy = st.builds(
    myAtl::BooleanLiteralExpCS,
    name=
        safe_text
)
myAtl::UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    myAtl::UnlimitedNaturalLiteralExpCS,
)
myAtl::StringLiteralExpCS_strategy = st.builds(
    myAtl::StringLiteralExpCS,
    name=
        safe_text
)
myAtl::NullLiteralExpCS_strategy = st.builds(
    myAtl::NullLiteralExpCS,
)
myAtl::InvalidLiteralExpCS_strategy = st.builds(
    myAtl::InvalidLiteralExpCS,
)
myAtl::NumberLiteralExpCS_strategy = st.builds(
    myAtl::NumberLiteralExpCS,
    name=
        safe_text
)
myAtl::TupleLiteralPartCS_strategy = st.builds(
    myAtl::TupleLiteralPartCS,
    name=
        safe_text
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
myAtl::StringExpCs_strategy = st.builds(
    myAtl::StringExpCs,
    name=
        safe_text
)
myAtl::NavigatingExpCS_strategy = st.builds(
    myAtl::NavigatingExpCS,
)
myAtl::IfExpCS_strategy = st.builds(
    myAtl::IfExpCS,
)
myAtl::SelfExpCS_strategy = st.builds(
    myAtl::SelfExpCS,
)
myAtl::TupleLiteralExpCS_strategy = st.builds(
    myAtl::TupleLiteralExpCS,
)
myAtl::LetExpCS_strategy = st.builds(
    myAtl::LetExpCS,
)
myAtl::NestedExpCS_strategy = st.builds(
    myAtl::NestedExpCS,
)
myAtl::PrimitiveLiteralExpCS_strategy = st.builds(
    myAtl::PrimitiveLiteralExpCS,
)
myAtl::tuplePartCS_strategy = st.builds(
    myAtl::tuplePartCS,
    name=
        safe_text
)
TypeLiteralCS_strategy = st.builds(
    TypeLiteralCS,
)
myAtl::PrimitiveTypeCS_strategy = st.builds(
    myAtl::PrimitiveTypeCS,
)
myAtl::TupleTypeCS_strategy = st.builds(
    myAtl::TupleTypeCS,
    backtrack=
        safe_text
)
myAtl::CollectionTypeCS_strategy = st.builds(
    myAtl::CollectionTypeCS,
)
myAtl::TypeExpCS_strategy = st.builds(
    myAtl::TypeExpCS,
)
Statement_strategy = st.builds(
    Statement,
)
myAtl::BindingStat_strategy = st.builds(
    myAtl::BindingStat,
    propertyName=
        safe_text
)
myAtl::Statement_strategy = st.builds(
    myAtl::Statement,
)
myAtl::Binding_strategy = st.builds(
    myAtl::Binding,
    propertyName=
        safe_text
)
OutPatternElement_strategy = st.builds(
    OutPatternElement,
)
myAtl::ForEachOutPatternElement_strategy = st.builds(
    myAtl::ForEachOutPatternElement,
)
myAtl::SimpleOutPatternElement_strategy = st.builds(
    myAtl::SimpleOutPatternElement,
    varName=
        safe_text
)
myAtl::OutPatternElement_strategy = st.builds(
    myAtl::OutPatternElement,
)
myAtl::InPatternElement_strategy = st.builds(
    myAtl::InPatternElement,
    varName=
        safe_text
)
myAtl::ATLType_strategy = st.builds(
    myAtl::ATLType,
    modelName=
        safe_text
)
myAtl::ATLDefCS_strategy = st.builds(
    myAtl::ATLDefCS,
    varName=
        safe_text
)
myAtl::ExpCS_strategy = st.builds(
    myAtl::ExpCS,
)
myAtl::ATLParameterCS_strategy = st.builds(
    myAtl::ATLParameterCS,
    varName=
        safe_text
)
myAtl::ActionBlock_strategy = st.builds(
    myAtl::ActionBlock,
)
myAtl::OutPattern_strategy = st.builds(
    myAtl::OutPattern,
)
myAtl::RuleVariableDeclaration_strategy = st.builds(
    myAtl::RuleVariableDeclaration,
    varName=
        safe_text
)
myAtl::InPattern_strategy = st.builds(
    myAtl::InPattern,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
myAtl::Helper_strategy = st.builds(
    myAtl::Helper,
)
myAtl::QueryRule_strategy = st.builds(
    myAtl::QueryRule,
)
myAtl::CalledRule_strategy = st.builds(
    myAtl::CalledRule,
)
myAtl::MatchedRule_strategy = st.builds(
    myAtl::MatchedRule,
)
myAtl::ModuleElement_strategy = st.builds(
    myAtl::ModuleElement,
    name=
        safe_text
)
myAtl::NameExpCS_strategy = st.builds(
    myAtl::NameExpCS,
    namespace=
        safe_text,
    element=
        safe_text
)
myAtl::Module_strategy = st.builds(
    myAtl::Module,
    name=
        safe_text
)

@given(instance=myAtl::EObject_strategy)
@settings(max_examples=50)
def test_myatl::eobject_instantiation(instance):
    assert isinstance(instance, myAtl::EObject)

@given(instance=NavigatingExpCS_strategy)
@settings(max_examples=50)
def test_navigatingexpcs_instantiation(instance):
    assert isinstance(instance, NavigatingExpCS)

@given(instance=myAtl::NavigatingExpCS::Base_strategy)
@settings(max_examples=50)
def test_myatl::navigatingexpcs::base_instantiation(instance):
    assert isinstance(instance, myAtl::NavigatingExpCS::Base)

@given(instance=NavigatingExpCS::Base_strategy)
@settings(max_examples=50)
def test_navigatingexpcs::base_instantiation(instance):
    assert isinstance(instance, NavigatingExpCS::Base)

@given(instance=myAtl::IndexExpCS_strategy)
@settings(max_examples=50)
def test_myatl::indexexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::IndexExpCS)

@given(instance=myAtl::UnaryOperatorCS_strategy)
@settings(max_examples=50)
def test_myatl::unaryoperatorcs_instantiation(instance):
    assert isinstance(instance, myAtl::UnaryOperatorCS)

@given(instance=myAtl::UnaryOperatorCS_strategy)
def test_myatl::unaryoperatorcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::UnaryOperatorCS_strategy)
def test_myatl::unaryoperatorcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=InfixedExpCS_strategy)
@settings(max_examples=50)
def test_infixedexpcs_instantiation(instance):
    assert isinstance(instance, InfixedExpCS)

@given(instance=myAtl::InfixExpCS_strategy)
@settings(max_examples=50)
def test_myatl::infixexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::InfixExpCS)

@given(instance=myAtl::PrefixedExpCS_strategy)
@settings(max_examples=50)
def test_myatl::prefixedexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::PrefixedExpCS)

@given(instance=BinaryOperatorCS_strategy)
@settings(max_examples=50)
def test_binaryoperatorcs_instantiation(instance):
    assert isinstance(instance, BinaryOperatorCS)

@given(instance=myAtl::NavigationOperatorCS_strategy)
@settings(max_examples=50)
def test_myatl::navigationoperatorcs_instantiation(instance):
    assert isinstance(instance, myAtl::NavigationOperatorCS)

@given(instance=myAtl::InfixOperatorCS_strategy)
@settings(max_examples=50)
def test_myatl::infixoperatorcs_instantiation(instance):
    assert isinstance(instance, myAtl::InfixOperatorCS)

@given(instance=myAtl::BinaryOperatorCS_strategy)
@settings(max_examples=50)
def test_myatl::binaryoperatorcs_instantiation(instance):
    assert isinstance(instance, myAtl::BinaryOperatorCS)

@given(instance=myAtl::BinaryOperatorCS_strategy)
def test_myatl::binaryoperatorcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::BinaryOperatorCS_strategy)
def test_myatl::binaryoperatorcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=myAtl::InfixedExpCS_strategy)
@settings(max_examples=50)
def test_myatl::infixedexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::InfixedExpCS)

@given(instance=NavigatingArgExpCS_strategy)
@settings(max_examples=50)
def test_navigatingargexpcs_instantiation(instance):
    assert isinstance(instance, NavigatingArgExpCS)

@given(instance=IndexExpCS_strategy)
@settings(max_examples=50)
def test_indexexpcs_instantiation(instance):
    assert isinstance(instance, IndexExpCS)

@given(instance=PrefixedExpCS_strategy)
@settings(max_examples=50)
def test_prefixedexpcs_instantiation(instance):
    assert isinstance(instance, PrefixedExpCS)

@given(instance=myAtl::PrefixExpCS_strategy)
@settings(max_examples=50)
def test_myatl::prefixexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::PrefixExpCS)

@given(instance=myAtl::PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_myatl::primaryexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::PrimaryExpCS)

@given(instance=myAtl::LetVariableCS_strategy)
@settings(max_examples=50)
def test_myatl::letvariablecs_instantiation(instance):
    assert isinstance(instance, myAtl::LetVariableCS)

@given(instance=myAtl::LetVariableCS_strategy)
def test_myatl::letvariablecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::LetVariableCS_strategy)
def test_myatl::letvariablecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl::NavigatingSemiArgCS_strategy)
@settings(max_examples=50)
def test_myatl::navigatingsemiargcs_instantiation(instance):
    assert isinstance(instance, myAtl::NavigatingSemiArgCS)

@given(instance=myAtl::NavigatingSemiArgCS_strategy)
def test_myatl::navigatingsemiargcs_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=myAtl::NavigatingSemiArgCS_strategy)
def test_myatl::navigatingsemiargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=myAtl::NavigatingCommaArgCS_strategy)
@settings(max_examples=50)
def test_myatl::navigatingcommaargcs_instantiation(instance):
    assert isinstance(instance, myAtl::NavigatingCommaArgCS)

@given(instance=myAtl::NavigatingCommaArgCS_strategy)
def test_myatl::navigatingcommaargcs_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=myAtl::NavigatingCommaArgCS_strategy)
def test_myatl::navigatingcommaargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=myAtl::NavigatingBarArgCS_strategy)
@settings(max_examples=50)
def test_myatl::navigatingbarargcs_instantiation(instance):
    assert isinstance(instance, myAtl::NavigatingBarArgCS)

@given(instance=myAtl::NavigatingBarArgCS_strategy)
def test_myatl::navigatingbarargcs_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=myAtl::NavigatingBarArgCS_strategy)
def test_myatl::navigatingbarargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=myAtl::NavigatingArgExpCS_strategy)
@settings(max_examples=50)
def test_myatl::navigatingargexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::NavigatingArgExpCS)

@given(instance=myAtl::NavigatingArgCS_strategy)
@settings(max_examples=50)
def test_myatl::navigatingargcs_instantiation(instance):
    assert isinstance(instance, myAtl::NavigatingArgCS)

@given(instance=myAtl::TypeLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl::typeliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::TypeLiteralExpCS)

@given(instance=TypeExpCS_strategy)
@settings(max_examples=50)
def test_typeexpcs_instantiation(instance):
    assert isinstance(instance, TypeExpCS)

@given(instance=myAtl::TypeNameExpCS_strategy)
@settings(max_examples=50)
def test_myatl::typenameexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::TypeNameExpCS)

@given(instance=myAtl::TypeNameExpCS_strategy)
def test_myatl::typenameexpcs_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=myAtl::TypeNameExpCS_strategy)
def test_myatl::typenameexpcs_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=myAtl::TypeNameExpCS_strategy)
def test_myatl::typenameexpcs_element_type(instance):
    assert isinstance(instance.element, str)


@given(instance=myAtl::TypeNameExpCS_strategy)
def test_myatl::typenameexpcs_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=myAtl::TypeLiteralCS_strategy)
@settings(max_examples=50)
def test_myatl::typeliteralcs_instantiation(instance):
    assert isinstance(instance, myAtl::TypeLiteralCS)

@given(instance=myAtl::TypeLiteralCS_strategy)
def test_myatl::typeliteralcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::TypeLiteralCS_strategy)
def test_myatl::typeliteralcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=myAtl::BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl::booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::BooleanLiteralExpCS)

@given(instance=myAtl::BooleanLiteralExpCS_strategy)
def test_myatl::booleanliteralexpcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::BooleanLiteralExpCS_strategy)
def test_myatl::booleanliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl::UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl::unlimitednaturalliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::UnlimitedNaturalLiteralExpCS)

@given(instance=myAtl::StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl::stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::StringLiteralExpCS)

@given(instance=myAtl::StringLiteralExpCS_strategy)
def test_myatl::stringliteralexpcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::StringLiteralExpCS_strategy)
def test_myatl::stringliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl::NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl::nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::NullLiteralExpCS)

@given(instance=myAtl::InvalidLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl::invalidliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::InvalidLiteralExpCS)

@given(instance=myAtl::NumberLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl::numberliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::NumberLiteralExpCS)

@given(instance=myAtl::NumberLiteralExpCS_strategy)
def test_myatl::numberliteralexpcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::NumberLiteralExpCS_strategy)
def test_myatl::numberliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl::TupleLiteralPartCS_strategy)
@settings(max_examples=50)
def test_myatl::tupleliteralpartcs_instantiation(instance):
    assert isinstance(instance, myAtl::TupleLiteralPartCS)

@given(instance=myAtl::TupleLiteralPartCS_strategy)
def test_myatl::tupleliteralpartcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::TupleLiteralPartCS_strategy)
def test_myatl::tupleliteralpartcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_primaryexpcs_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)

@given(instance=myAtl::StringExpCs_strategy)
@settings(max_examples=50)
def test_myatl::stringexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::StringExpCs)

@given(instance=myAtl::StringExpCs_strategy)
def test_myatl::stringexpcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::StringExpCs_strategy)
def test_myatl::stringexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl::NavigatingExpCS_strategy)
@settings(max_examples=50)
def test_myatl::navigatingexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::NavigatingExpCS)

@given(instance=myAtl::IfExpCS_strategy)
@settings(max_examples=50)
def test_myatl::ifexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::IfExpCS)

@given(instance=myAtl::SelfExpCS_strategy)
@settings(max_examples=50)
def test_myatl::selfexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::SelfExpCS)

@given(instance=myAtl::TupleLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl::tupleliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::TupleLiteralExpCS)

@given(instance=myAtl::LetExpCS_strategy)
@settings(max_examples=50)
def test_myatl::letexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::LetExpCS)

@given(instance=myAtl::NestedExpCS_strategy)
@settings(max_examples=50)
def test_myatl::nestedexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::NestedExpCS)

@given(instance=myAtl::PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl::primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::PrimitiveLiteralExpCS)

@given(instance=myAtl::tuplePartCS_strategy)
@settings(max_examples=50)
def test_myatl::tuplepartcs_instantiation(instance):
    assert isinstance(instance, myAtl::tuplePartCS)

@given(instance=myAtl::tuplePartCS_strategy)
def test_myatl::tuplepartcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::tuplePartCS_strategy)
def test_myatl::tuplepartcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeLiteralCS_strategy)
@settings(max_examples=50)
def test_typeliteralcs_instantiation(instance):
    assert isinstance(instance, TypeLiteralCS)

@given(instance=myAtl::PrimitiveTypeCS_strategy)
@settings(max_examples=50)
def test_myatl::primitivetypecs_instantiation(instance):
    assert isinstance(instance, myAtl::PrimitiveTypeCS)

@given(instance=myAtl::TupleTypeCS_strategy)
@settings(max_examples=50)
def test_myatl::tupletypecs_instantiation(instance):
    assert isinstance(instance, myAtl::TupleTypeCS)

@given(instance=myAtl::TupleTypeCS_strategy)
def test_myatl::tupletypecs_backtrack_type(instance):
    assert isinstance(instance.backtrack, str)


@given(instance=myAtl::TupleTypeCS_strategy)
def test_myatl::tupletypecs_backtrack_setter(instance):
    original = instance.backtrack
    instance.backtrack = original
    assert instance.backtrack == original

@given(instance=myAtl::CollectionTypeCS_strategy)
@settings(max_examples=50)
def test_myatl::collectiontypecs_instantiation(instance):
    assert isinstance(instance, myAtl::CollectionTypeCS)

@given(instance=myAtl::TypeExpCS_strategy)
@settings(max_examples=50)
def test_myatl::typeexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::TypeExpCS)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=myAtl::BindingStat_strategy)
@settings(max_examples=50)
def test_myatl::bindingstat_instantiation(instance):
    assert isinstance(instance, myAtl::BindingStat)

@given(instance=myAtl::BindingStat_strategy)
def test_myatl::bindingstat_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=myAtl::BindingStat_strategy)
def test_myatl::bindingstat_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=myAtl::Statement_strategy)
@settings(max_examples=50)
def test_myatl::statement_instantiation(instance):
    assert isinstance(instance, myAtl::Statement)

@given(instance=myAtl::Binding_strategy)
@settings(max_examples=50)
def test_myatl::binding_instantiation(instance):
    assert isinstance(instance, myAtl::Binding)

@given(instance=myAtl::Binding_strategy)
def test_myatl::binding_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=myAtl::Binding_strategy)
def test_myatl::binding_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=OutPatternElement_strategy)
@settings(max_examples=50)
def test_outpatternelement_instantiation(instance):
    assert isinstance(instance, OutPatternElement)

@given(instance=myAtl::ForEachOutPatternElement_strategy)
@settings(max_examples=50)
def test_myatl::foreachoutpatternelement_instantiation(instance):
    assert isinstance(instance, myAtl::ForEachOutPatternElement)

@given(instance=myAtl::SimpleOutPatternElement_strategy)
@settings(max_examples=50)
def test_myatl::simpleoutpatternelement_instantiation(instance):
    assert isinstance(instance, myAtl::SimpleOutPatternElement)

@given(instance=myAtl::SimpleOutPatternElement_strategy)
def test_myatl::simpleoutpatternelement_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=myAtl::SimpleOutPatternElement_strategy)
def test_myatl::simpleoutpatternelement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=myAtl::OutPatternElement_strategy)
@settings(max_examples=50)
def test_myatl::outpatternelement_instantiation(instance):
    assert isinstance(instance, myAtl::OutPatternElement)

@given(instance=myAtl::InPatternElement_strategy)
@settings(max_examples=50)
def test_myatl::inpatternelement_instantiation(instance):
    assert isinstance(instance, myAtl::InPatternElement)

@given(instance=myAtl::InPatternElement_strategy)
def test_myatl::inpatternelement_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=myAtl::InPatternElement_strategy)
def test_myatl::inpatternelement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=myAtl::ATLType_strategy)
@settings(max_examples=50)
def test_myatl::atltype_instantiation(instance):
    assert isinstance(instance, myAtl::ATLType)

@given(instance=myAtl::ATLType_strategy)
def test_myatl::atltype_modelName_type(instance):
    assert isinstance(instance.modelName, str)


@given(instance=myAtl::ATLType_strategy)
def test_myatl::atltype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original

@given(instance=myAtl::ATLDefCS_strategy)
@settings(max_examples=50)
def test_myatl::atldefcs_instantiation(instance):
    assert isinstance(instance, myAtl::ATLDefCS)

@given(instance=myAtl::ATLDefCS_strategy)
def test_myatl::atldefcs_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=myAtl::ATLDefCS_strategy)
def test_myatl::atldefcs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=myAtl::ExpCS_strategy)
@settings(max_examples=50)
def test_myatl::expcs_instantiation(instance):
    assert isinstance(instance, myAtl::ExpCS)

@given(instance=myAtl::ATLParameterCS_strategy)
@settings(max_examples=50)
def test_myatl::atlparametercs_instantiation(instance):
    assert isinstance(instance, myAtl::ATLParameterCS)

@given(instance=myAtl::ATLParameterCS_strategy)
def test_myatl::atlparametercs_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=myAtl::ATLParameterCS_strategy)
def test_myatl::atlparametercs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=myAtl::ActionBlock_strategy)
@settings(max_examples=50)
def test_myatl::actionblock_instantiation(instance):
    assert isinstance(instance, myAtl::ActionBlock)

@given(instance=myAtl::OutPattern_strategy)
@settings(max_examples=50)
def test_myatl::outpattern_instantiation(instance):
    assert isinstance(instance, myAtl::OutPattern)

@given(instance=myAtl::RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_myatl::rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, myAtl::RuleVariableDeclaration)

@given(instance=myAtl::RuleVariableDeclaration_strategy)
def test_myatl::rulevariabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=myAtl::RuleVariableDeclaration_strategy)
def test_myatl::rulevariabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=myAtl::InPattern_strategy)
@settings(max_examples=50)
def test_myatl::inpattern_instantiation(instance):
    assert isinstance(instance, myAtl::InPattern)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=myAtl::Helper_strategy)
@settings(max_examples=50)
def test_myatl::helper_instantiation(instance):
    assert isinstance(instance, myAtl::Helper)

@given(instance=myAtl::QueryRule_strategy)
@settings(max_examples=50)
def test_myatl::queryrule_instantiation(instance):
    assert isinstance(instance, myAtl::QueryRule)

@given(instance=myAtl::CalledRule_strategy)
@settings(max_examples=50)
def test_myatl::calledrule_instantiation(instance):
    assert isinstance(instance, myAtl::CalledRule)

@given(instance=myAtl::MatchedRule_strategy)
@settings(max_examples=50)
def test_myatl::matchedrule_instantiation(instance):
    assert isinstance(instance, myAtl::MatchedRule)

@given(instance=myAtl::ModuleElement_strategy)
@settings(max_examples=50)
def test_myatl::moduleelement_instantiation(instance):
    assert isinstance(instance, myAtl::ModuleElement)

@given(instance=myAtl::ModuleElement_strategy)
def test_myatl::moduleelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::ModuleElement_strategy)
def test_myatl::moduleelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl::NameExpCS_strategy)
@settings(max_examples=50)
def test_myatl::nameexpcs_instantiation(instance):
    assert isinstance(instance, myAtl::NameExpCS)

@given(instance=myAtl::NameExpCS_strategy)
def test_myatl::nameexpcs_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=myAtl::NameExpCS_strategy)
def test_myatl::nameexpcs_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=myAtl::NameExpCS_strategy)
def test_myatl::nameexpcs_element_type(instance):
    assert isinstance(instance.element, str)


@given(instance=myAtl::NameExpCS_strategy)
def test_myatl::nameexpcs_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=myAtl::Module_strategy)
@settings(max_examples=50)
def test_myatl::module_instantiation(instance):
    assert isinstance(instance, myAtl::Module)

@given(instance=myAtl::Module_strategy)
def test_myatl::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myAtl::Module_strategy)
def test_myatl::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

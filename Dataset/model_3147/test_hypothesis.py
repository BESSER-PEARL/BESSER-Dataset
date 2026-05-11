import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    LiteralExp,
    XPath::StringExp,
    XPath::IntegerExp,
    NamedElement,
    Expression,
    XPath::LiteralExp,
    XPath::VariableExp,
    LocatedElement,
    XPath::OperatorCallExp,
    XPath::Expression,
    XPath::NamedElement,
    XPath::LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath::stringexp_is_not_abstract():
    assert not inspect.isabstract(XPath::StringExp)


def test_xpath::stringexp_constructor_exists():
    assert callable(XPath::StringExp.__init__)


def test_xpath::stringexp_constructor_args():
    sig = inspect.signature(XPath::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_xpath::stringexp_has_symbol():
    assert hasattr(XPath::StringExp, "symbol")
    descriptor = None
    for klass in XPath::StringExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_xpath::integerexp_is_not_abstract():
    assert not inspect.isabstract(XPath::IntegerExp)


def test_xpath::integerexp_constructor_exists():
    assert callable(XPath::IntegerExp.__init__)


def test_xpath::integerexp_constructor_args():
    sig = inspect.signature(XPath::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_xpath::integerexp_has_symbol():
    assert hasattr(XPath::IntegerExp, "symbol")
    descriptor = None
    for klass in XPath::IntegerExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_xpath::literalexp_is_not_abstract():
    assert not inspect.isabstract(XPath::LiteralExp)


def test_xpath::literalexp_constructor_exists():
    assert callable(XPath::LiteralExp.__init__)


def test_xpath::literalexp_constructor_args():
    sig = inspect.signature(XPath::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath::variableexp_is_not_abstract():
    assert not inspect.isabstract(XPath::VariableExp)


def test_xpath::variableexp_constructor_exists():
    assert callable(XPath::VariableExp.__init__)


def test_xpath::variableexp_constructor_args():
    sig = inspect.signature(XPath::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_xpath::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(XPath::OperatorCallExp)


def test_xpath::operatorcallexp_constructor_exists():
    assert callable(XPath::OperatorCallExp.__init__)


def test_xpath::operatorcallexp_constructor_args():
    sig = inspect.signature(XPath::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath::expression_is_not_abstract():
    assert not inspect.isabstract(XPath::Expression)


def test_xpath::expression_constructor_exists():
    assert callable(XPath::Expression.__init__)


def test_xpath::expression_constructor_args():
    sig = inspect.signature(XPath::Expression.__init__)
    params = list(sig.parameters.keys())



def test_xpath::namedelement_is_not_abstract():
    assert not inspect.isabstract(XPath::NamedElement)


def test_xpath::namedelement_constructor_exists():
    assert callable(XPath::NamedElement.__init__)


def test_xpath::namedelement_constructor_args():
    sig = inspect.signature(XPath::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xpath::namedelement_has_name():
    assert hasattr(XPath::NamedElement, "name")
    descriptor = None
    for klass in XPath::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpath::locatedelement_is_not_abstract():
    assert not inspect.isabstract(XPath::LocatedElement)


def test_xpath::locatedelement_constructor_exists():
    assert callable(XPath::LocatedElement.__init__)


def test_xpath::locatedelement_constructor_args():
    sig = inspect.signature(XPath::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"

def test_xpath::locatedelement_has_commentsAfter():
    assert hasattr(XPath::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in XPath::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_xpath::locatedelement_has_commentsBefore():
    assert hasattr(XPath::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in XPath::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_xpath::locatedelement_has_location():
    assert hasattr(XPath::LocatedElement, "location")
    descriptor = None
    for klass in XPath::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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
LiteralExp_strategy = st.builds(
    LiteralExp,
)
XPath::StringExp_strategy = st.builds(
    XPath::StringExp,
    symbol=
        safe_text
)
XPath::IntegerExp_strategy = st.builds(
    XPath::IntegerExp,
    symbol=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Expression_strategy = st.builds(
    Expression,
)
XPath::LiteralExp_strategy = st.builds(
    XPath::LiteralExp,
)
XPath::VariableExp_strategy = st.builds(
    XPath::VariableExp,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
XPath::OperatorCallExp_strategy = st.builds(
    XPath::OperatorCallExp,
)
XPath::Expression_strategy = st.builds(
    XPath::Expression,
)
XPath::NamedElement_strategy = st.builds(
    XPath::NamedElement,
    name=
        safe_text
)
XPath::LocatedElement_strategy = st.builds(
    XPath::LocatedElement,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text,
    location=
        safe_text
)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=XPath::StringExp_strategy)
@settings(max_examples=50)
def test_xpath::stringexp_instantiation(instance):
    assert isinstance(instance, XPath::StringExp)

@given(instance=XPath::StringExp_strategy)
def test_xpath::stringexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=XPath::StringExp_strategy)
def test_xpath::stringexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=XPath::IntegerExp_strategy)
@settings(max_examples=50)
def test_xpath::integerexp_instantiation(instance):
    assert isinstance(instance, XPath::IntegerExp)

@given(instance=XPath::IntegerExp_strategy)
def test_xpath::integerexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=XPath::IntegerExp_strategy)
def test_xpath::integerexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=XPath::LiteralExp_strategy)
@settings(max_examples=50)
def test_xpath::literalexp_instantiation(instance):
    assert isinstance(instance, XPath::LiteralExp)

@given(instance=XPath::VariableExp_strategy)
@settings(max_examples=50)
def test_xpath::variableexp_instantiation(instance):
    assert isinstance(instance, XPath::VariableExp)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=XPath::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_xpath::operatorcallexp_instantiation(instance):
    assert isinstance(instance, XPath::OperatorCallExp)

@given(instance=XPath::Expression_strategy)
@settings(max_examples=50)
def test_xpath::expression_instantiation(instance):
    assert isinstance(instance, XPath::Expression)

@given(instance=XPath::NamedElement_strategy)
@settings(max_examples=50)
def test_xpath::namedelement_instantiation(instance):
    assert isinstance(instance, XPath::NamedElement)

@given(instance=XPath::NamedElement_strategy)
def test_xpath::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=XPath::NamedElement_strategy)
def test_xpath::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=XPath::LocatedElement_strategy)
@settings(max_examples=50)
def test_xpath::locatedelement_instantiation(instance):
    assert isinstance(instance, XPath::LocatedElement)

@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=XPath::LocatedElement_strategy)
def test_xpath::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

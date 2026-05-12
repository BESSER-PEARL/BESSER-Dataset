import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    LiteralExp,
    XPath_StringExp,
    XPath_IntegerExp,
    NamedElement,
    Expression,
    XPath_LiteralExp,
    XPath_VariableExp,
    LocatedElement,
    XPath_Expression,
    XPath_OperatorCallExp,
    XPath_NamedElement,
    XPath_LocatedElement,
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



def test_xpath_stringexp_is_not_abstract():
    assert not inspect.isabstract(XPath_StringExp)


def test_xpath_stringexp_constructor_exists():
    assert callable(XPath_StringExp.__init__)


def test_xpath_stringexp_constructor_args():
    sig = inspect.signature(XPath_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_xpath_stringexp_has_symbol():
    assert hasattr(XPath_StringExp, "symbol")
    descriptor = None
    for klass in XPath_StringExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_xpath_integerexp_is_not_abstract():
    assert not inspect.isabstract(XPath_IntegerExp)


def test_xpath_integerexp_constructor_exists():
    assert callable(XPath_IntegerExp.__init__)


def test_xpath_integerexp_constructor_args():
    sig = inspect.signature(XPath_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_xpath_integerexp_has_symbol():
    assert hasattr(XPath_IntegerExp, "symbol")
    descriptor = None
    for klass in XPath_IntegerExp.__mro__:
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



def test_xpath_literalexp_is_not_abstract():
    assert not inspect.isabstract(XPath_LiteralExp)


def test_xpath_literalexp_constructor_exists():
    assert callable(XPath_LiteralExp.__init__)


def test_xpath_literalexp_constructor_args():
    sig = inspect.signature(XPath_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath_variableexp_is_not_abstract():
    assert not inspect.isabstract(XPath_VariableExp)


def test_xpath_variableexp_constructor_exists():
    assert callable(XPath_VariableExp.__init__)


def test_xpath_variableexp_constructor_args():
    sig = inspect.signature(XPath_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_xpath_expression_is_not_abstract():
    assert not inspect.isabstract(XPath_Expression)


def test_xpath_expression_constructor_exists():
    assert callable(XPath_Expression.__init__)


def test_xpath_expression_constructor_args():
    sig = inspect.signature(XPath_Expression.__init__)
    params = list(sig.parameters.keys())



def test_xpath_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(XPath_OperatorCallExp)


def test_xpath_operatorcallexp_constructor_exists():
    assert callable(XPath_OperatorCallExp.__init__)


def test_xpath_operatorcallexp_constructor_args():
    sig = inspect.signature(XPath_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_xpath_namedelement_is_not_abstract():
    assert not inspect.isabstract(XPath_NamedElement)


def test_xpath_namedelement_constructor_exists():
    assert callable(XPath_NamedElement.__init__)


def test_xpath_namedelement_constructor_args():
    sig = inspect.signature(XPath_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xpath_namedelement_has_name():
    assert hasattr(XPath_NamedElement, "name")
    descriptor = None
    for klass in XPath_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpath_locatedelement_is_not_abstract():
    assert not inspect.isabstract(XPath_LocatedElement)


def test_xpath_locatedelement_constructor_exists():
    assert callable(XPath_LocatedElement.__init__)


def test_xpath_locatedelement_constructor_args():
    sig = inspect.signature(XPath_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"

def test_xpath_locatedelement_has_commentsAfter():
    assert hasattr(XPath_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in XPath_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_xpath_locatedelement_has_commentsBefore():
    assert hasattr(XPath_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in XPath_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_xpath_locatedelement_has_location():
    assert hasattr(XPath_LocatedElement, "location")
    descriptor = None
    for klass in XPath_LocatedElement.__mro__:
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
XPath_StringExp_strategy = st.builds(
    XPath_StringExp,
    symbol=
        safe_text
)
XPath_IntegerExp_strategy = st.builds(
    XPath_IntegerExp,
    symbol=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Expression_strategy = st.builds(
    Expression,
)
XPath_LiteralExp_strategy = st.builds(
    XPath_LiteralExp,
)
XPath_VariableExp_strategy = st.builds(
    XPath_VariableExp,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
XPath_Expression_strategy = st.builds(
    XPath_Expression,
)
XPath_OperatorCallExp_strategy = st.builds(
    XPath_OperatorCallExp,
)
XPath_NamedElement_strategy = st.builds(
    XPath_NamedElement,
    name=
        safe_text
)
XPath_LocatedElement_strategy = st.builds(
    XPath_LocatedElement,
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

@given(instance=XPath_StringExp_strategy)
@settings(max_examples=50)
def test_xpath_stringexp_instantiation(instance):
    assert isinstance(instance, XPath_StringExp)



@given(instance=XPath_StringExp_strategy)
def test_xpath_stringexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=XPath_IntegerExp_strategy)
@settings(max_examples=50)
def test_xpath_integerexp_instantiation(instance):
    assert isinstance(instance, XPath_IntegerExp)



@given(instance=XPath_IntegerExp_strategy)
def test_xpath_integerexp_symbol_setter(instance):
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

@given(instance=XPath_LiteralExp_strategy)
@settings(max_examples=50)
def test_xpath_literalexp_instantiation(instance):
    assert isinstance(instance, XPath_LiteralExp)

@given(instance=XPath_VariableExp_strategy)
@settings(max_examples=50)
def test_xpath_variableexp_instantiation(instance):
    assert isinstance(instance, XPath_VariableExp)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=XPath_Expression_strategy)
@settings(max_examples=50)
def test_xpath_expression_instantiation(instance):
    assert isinstance(instance, XPath_Expression)

@given(instance=XPath_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_xpath_operatorcallexp_instantiation(instance):
    assert isinstance(instance, XPath_OperatorCallExp)

@given(instance=XPath_NamedElement_strategy)
@settings(max_examples=50)
def test_xpath_namedelement_instantiation(instance):
    assert isinstance(instance, XPath_NamedElement)



@given(instance=XPath_NamedElement_strategy)
def test_xpath_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=XPath_LocatedElement_strategy)
@settings(max_examples=50)
def test_xpath_locatedelement_instantiation(instance):
    assert isinstance(instance, XPath_LocatedElement)



@given(instance=XPath_LocatedElement_strategy)
def test_xpath_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original



@given(instance=XPath_LocatedElement_strategy)
def test_xpath_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=XPath_LocatedElement_strategy)
def test_xpath_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

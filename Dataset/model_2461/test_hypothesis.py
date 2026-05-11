import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OclExpression,
    operators::OperatorCallExp,
    operators::OclExpression,
    NumericExp,
    operators::RealExp,
    PrimitiveExp,
    operators::BooleanExp,
    operators::NumericExp,
    operators::StringExp,
    operators::PrimitiveExp,
    operators::IntegerExp,
    OperatorCallExp,
    operators::BinaryOperatorCallExp,
    operators::UnaryOperatorCallExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_operators::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(operators::OperatorCallExp)


def test_operators::operatorcallexp_constructor_exists():
    assert callable(operators::OperatorCallExp.__init__)


def test_operators::operatorcallexp_constructor_args():
    sig = inspect.signature(operators::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_operators::operatorcallexp_has_name():
    assert hasattr(operators::OperatorCallExp, "name")
    descriptor = None
    for klass in operators::OperatorCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_operators::oclexpression_is_not_abstract():
    assert not inspect.isabstract(operators::OclExpression)


def test_operators::oclexpression_constructor_exists():
    assert callable(operators::OclExpression.__init__)


def test_operators::oclexpression_constructor_args():
    sig = inspect.signature(operators::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_operators::realexp_is_not_abstract():
    assert not inspect.isabstract(operators::RealExp)


def test_operators::realexp_constructor_exists():
    assert callable(operators::RealExp.__init__)


def test_operators::realexp_constructor_args():
    sig = inspect.signature(operators::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_operators::realexp_has_realSymbol():
    assert hasattr(operators::RealExp, "realSymbol")
    descriptor = None
    for klass in operators::RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_operators::booleanexp_is_not_abstract():
    assert not inspect.isabstract(operators::BooleanExp)


def test_operators::booleanexp_constructor_exists():
    assert callable(operators::BooleanExp.__init__)


def test_operators::booleanexp_constructor_args():
    sig = inspect.signature(operators::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_operators::booleanexp_has_booleanSymbol():
    assert hasattr(operators::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in operators::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_operators::numericexp_is_not_abstract():
    assert not inspect.isabstract(operators::NumericExp)


def test_operators::numericexp_constructor_exists():
    assert callable(operators::NumericExp.__init__)


def test_operators::numericexp_constructor_args():
    sig = inspect.signature(operators::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_operators::stringexp_is_not_abstract():
    assert not inspect.isabstract(operators::StringExp)


def test_operators::stringexp_constructor_exists():
    assert callable(operators::StringExp.__init__)


def test_operators::stringexp_constructor_args():
    sig = inspect.signature(operators::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_operators::stringexp_has_stringSymbol():
    assert hasattr(operators::StringExp, "stringSymbol")
    descriptor = None
    for klass in operators::StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_operators::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(operators::PrimitiveExp)


def test_operators::primitiveexp_constructor_exists():
    assert callable(operators::PrimitiveExp.__init__)


def test_operators::primitiveexp_constructor_args():
    sig = inspect.signature(operators::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_operators::integerexp_is_not_abstract():
    assert not inspect.isabstract(operators::IntegerExp)


def test_operators::integerexp_constructor_exists():
    assert callable(operators::IntegerExp.__init__)


def test_operators::integerexp_constructor_args():
    sig = inspect.signature(operators::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_operators::integerexp_has_integerSymbol():
    assert hasattr(operators::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in operators::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_operators::binaryoperatorcallexp_is_not_abstract():
    assert not inspect.isabstract(operators::BinaryOperatorCallExp)


def test_operators::binaryoperatorcallexp_constructor_exists():
    assert callable(operators::BinaryOperatorCallExp.__init__)


def test_operators::binaryoperatorcallexp_constructor_args():
    sig = inspect.signature(operators::BinaryOperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_operators::unaryoperatorcallexp_is_not_abstract():
    assert not inspect.isabstract(operators::UnaryOperatorCallExp)


def test_operators::unaryoperatorcallexp_constructor_exists():
    assert callable(operators::UnaryOperatorCallExp.__init__)


def test_operators::unaryoperatorcallexp_constructor_args():
    sig = inspect.signature(operators::UnaryOperatorCallExp.__init__)
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
OclExpression_strategy = st.builds(
    OclExpression,
)
operators::OperatorCallExp_strategy = st.builds(
    operators::OperatorCallExp,
    name=
        safe_text
)
operators::OclExpression_strategy = st.builds(
    operators::OclExpression,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
operators::RealExp_strategy = st.builds(
    operators::RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
operators::BooleanExp_strategy = st.builds(
    operators::BooleanExp,
    booleanSymbol=
        safe_text
)
operators::NumericExp_strategy = st.builds(
    operators::NumericExp,
)
operators::StringExp_strategy = st.builds(
    operators::StringExp,
    stringSymbol=
        safe_text
)
operators::PrimitiveExp_strategy = st.builds(
    operators::PrimitiveExp,
)
operators::IntegerExp_strategy = st.builds(
    operators::IntegerExp,
    integerSymbol=
        safe_text
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
operators::BinaryOperatorCallExp_strategy = st.builds(
    operators::BinaryOperatorCallExp,
)
operators::UnaryOperatorCallExp_strategy = st.builds(
    operators::UnaryOperatorCallExp,
)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=operators::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operators::operatorcallexp_instantiation(instance):
    assert isinstance(instance, operators::OperatorCallExp)

@given(instance=operators::OperatorCallExp_strategy)
def test_operators::operatorcallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=operators::OperatorCallExp_strategy)
def test_operators::operatorcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=operators::OclExpression_strategy)
@settings(max_examples=50)
def test_operators::oclexpression_instantiation(instance):
    assert isinstance(instance, operators::OclExpression)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=operators::RealExp_strategy)
@settings(max_examples=50)
def test_operators::realexp_instantiation(instance):
    assert isinstance(instance, operators::RealExp)

@given(instance=operators::RealExp_strategy)
def test_operators::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=operators::RealExp_strategy)
def test_operators::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=operators::BooleanExp_strategy)
@settings(max_examples=50)
def test_operators::booleanexp_instantiation(instance):
    assert isinstance(instance, operators::BooleanExp)

@given(instance=operators::BooleanExp_strategy)
def test_operators::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=operators::BooleanExp_strategy)
def test_operators::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=operators::NumericExp_strategy)
@settings(max_examples=50)
def test_operators::numericexp_instantiation(instance):
    assert isinstance(instance, operators::NumericExp)

@given(instance=operators::StringExp_strategy)
@settings(max_examples=50)
def test_operators::stringexp_instantiation(instance):
    assert isinstance(instance, operators::StringExp)

@given(instance=operators::StringExp_strategy)
def test_operators::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=operators::StringExp_strategy)
def test_operators::stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=operators::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_operators::primitiveexp_instantiation(instance):
    assert isinstance(instance, operators::PrimitiveExp)

@given(instance=operators::IntegerExp_strategy)
@settings(max_examples=50)
def test_operators::integerexp_instantiation(instance):
    assert isinstance(instance, operators::IntegerExp)

@given(instance=operators::IntegerExp_strategy)
def test_operators::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=operators::IntegerExp_strategy)
def test_operators::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=operators::BinaryOperatorCallExp_strategy)
@settings(max_examples=50)
def test_operators::binaryoperatorcallexp_instantiation(instance):
    assert isinstance(instance, operators::BinaryOperatorCallExp)

@given(instance=operators::UnaryOperatorCallExp_strategy)
@settings(max_examples=50)
def test_operators::unaryoperatorcallexp_instantiation(instance):
    assert isinstance(instance, operators::UnaryOperatorCallExp)

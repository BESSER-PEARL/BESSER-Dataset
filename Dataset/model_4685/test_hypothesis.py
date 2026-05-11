import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryExp,
    rules::core::Minus,
    rules::core::Equals,
    rules::core::Mult,
    rules::core::Div,
    rules::core::Greater,
    rules::core::Min,
    rules::core::Lower,
    rules::core::Max,
    rules::core::Plus,
    Expression,
    rules::core::Constant,
    rules::core::If,
    rules::core::BinaryExp,
    rules::core::Filter,
    rules::core::Rule,
    rules::core::Expression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::minus_is_not_abstract():
    assert not inspect.isabstract(rules::core::Minus)


def test_rules::core::minus_constructor_exists():
    assert callable(rules::core::Minus.__init__)


def test_rules::core::minus_constructor_args():
    sig = inspect.signature(rules::core::Minus.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::equals_is_not_abstract():
    assert not inspect.isabstract(rules::core::Equals)


def test_rules::core::equals_constructor_exists():
    assert callable(rules::core::Equals.__init__)


def test_rules::core::equals_constructor_args():
    sig = inspect.signature(rules::core::Equals.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::mult_is_not_abstract():
    assert not inspect.isabstract(rules::core::Mult)


def test_rules::core::mult_constructor_exists():
    assert callable(rules::core::Mult.__init__)


def test_rules::core::mult_constructor_args():
    sig = inspect.signature(rules::core::Mult.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::div_is_not_abstract():
    assert not inspect.isabstract(rules::core::Div)


def test_rules::core::div_constructor_exists():
    assert callable(rules::core::Div.__init__)


def test_rules::core::div_constructor_args():
    sig = inspect.signature(rules::core::Div.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::greater_is_not_abstract():
    assert not inspect.isabstract(rules::core::Greater)


def test_rules::core::greater_constructor_exists():
    assert callable(rules::core::Greater.__init__)


def test_rules::core::greater_constructor_args():
    sig = inspect.signature(rules::core::Greater.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::min_is_not_abstract():
    assert not inspect.isabstract(rules::core::Min)


def test_rules::core::min_constructor_exists():
    assert callable(rules::core::Min.__init__)


def test_rules::core::min_constructor_args():
    sig = inspect.signature(rules::core::Min.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::lower_is_not_abstract():
    assert not inspect.isabstract(rules::core::Lower)


def test_rules::core::lower_constructor_exists():
    assert callable(rules::core::Lower.__init__)


def test_rules::core::lower_constructor_args():
    sig = inspect.signature(rules::core::Lower.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::max_is_not_abstract():
    assert not inspect.isabstract(rules::core::Max)


def test_rules::core::max_constructor_exists():
    assert callable(rules::core::Max.__init__)


def test_rules::core::max_constructor_args():
    sig = inspect.signature(rules::core::Max.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::plus_is_not_abstract():
    assert not inspect.isabstract(rules::core::Plus)


def test_rules::core::plus_constructor_exists():
    assert callable(rules::core::Plus.__init__)


def test_rules::core::plus_constructor_args():
    sig = inspect.signature(rules::core::Plus.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::constant_is_not_abstract():
    assert not inspect.isabstract(rules::core::Constant)


def test_rules::core::constant_constructor_exists():
    assert callable(rules::core::Constant.__init__)


def test_rules::core::constant_constructor_args():
    sig = inspect.signature(rules::core::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_rules::core::constant_has_integerValue():
    assert hasattr(rules::core::Constant, "integerValue")
    descriptor = None
    for klass in rules::core::Constant.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)



def test_rules::core::if_is_not_abstract():
    assert not inspect.isabstract(rules::core::If)


def test_rules::core::if_constructor_exists():
    assert callable(rules::core::If.__init__)


def test_rules::core::if_constructor_args():
    sig = inspect.signature(rules::core::If.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::binaryexp_is_not_abstract():
    assert not inspect.isabstract(rules::core::BinaryExp)


def test_rules::core::binaryexp_constructor_exists():
    assert callable(rules::core::BinaryExp.__init__)


def test_rules::core::binaryexp_constructor_args():
    sig = inspect.signature(rules::core::BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::filter_is_not_abstract():
    assert not inspect.isabstract(rules::core::Filter)


def test_rules::core::filter_constructor_exists():
    assert callable(rules::core::Filter.__init__)


def test_rules::core::filter_constructor_args():
    sig = inspect.signature(rules::core::Filter.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::rule_is_not_abstract():
    assert not inspect.isabstract(rules::core::Rule)


def test_rules::core::rule_constructor_exists():
    assert callable(rules::core::Rule.__init__)


def test_rules::core::rule_constructor_args():
    sig = inspect.signature(rules::core::Rule.__init__)
    params = list(sig.parameters.keys())



def test_rules::core::expression_is_not_abstract():
    assert not inspect.isabstract(rules::core::Expression)


def test_rules::core::expression_constructor_exists():
    assert callable(rules::core::Expression.__init__)


def test_rules::core::expression_constructor_args():
    sig = inspect.signature(rules::core::Expression.__init__)
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
BinaryExp_strategy = st.builds(
    BinaryExp,
)
rules::core::Minus_strategy = st.builds(
    rules::core::Minus,
)
rules::core::Equals_strategy = st.builds(
    rules::core::Equals,
)
rules::core::Mult_strategy = st.builds(
    rules::core::Mult,
)
rules::core::Div_strategy = st.builds(
    rules::core::Div,
)
rules::core::Greater_strategy = st.builds(
    rules::core::Greater,
)
rules::core::Min_strategy = st.builds(
    rules::core::Min,
)
rules::core::Lower_strategy = st.builds(
    rules::core::Lower,
)
rules::core::Max_strategy = st.builds(
    rules::core::Max,
)
rules::core::Plus_strategy = st.builds(
    rules::core::Plus,
)
Expression_strategy = st.builds(
    Expression,
)
rules::core::Constant_strategy = st.builds(
    rules::core::Constant,
    integerValue=
        st.integers()
)
rules::core::If_strategy = st.builds(
    rules::core::If,
)
rules::core::BinaryExp_strategy = st.builds(
    rules::core::BinaryExp,
)
rules::core::Filter_strategy = st.builds(
    rules::core::Filter,
)
rules::core::Rule_strategy = st.builds(
    rules::core::Rule,
)
rules::core::Expression_strategy = st.builds(
    rules::core::Expression,
)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=rules::core::Minus_strategy)
@settings(max_examples=50)
def test_rules::core::minus_instantiation(instance):
    assert isinstance(instance, rules::core::Minus)

@given(instance=rules::core::Equals_strategy)
@settings(max_examples=50)
def test_rules::core::equals_instantiation(instance):
    assert isinstance(instance, rules::core::Equals)

@given(instance=rules::core::Mult_strategy)
@settings(max_examples=50)
def test_rules::core::mult_instantiation(instance):
    assert isinstance(instance, rules::core::Mult)

@given(instance=rules::core::Div_strategy)
@settings(max_examples=50)
def test_rules::core::div_instantiation(instance):
    assert isinstance(instance, rules::core::Div)

@given(instance=rules::core::Greater_strategy)
@settings(max_examples=50)
def test_rules::core::greater_instantiation(instance):
    assert isinstance(instance, rules::core::Greater)

@given(instance=rules::core::Min_strategy)
@settings(max_examples=50)
def test_rules::core::min_instantiation(instance):
    assert isinstance(instance, rules::core::Min)

@given(instance=rules::core::Lower_strategy)
@settings(max_examples=50)
def test_rules::core::lower_instantiation(instance):
    assert isinstance(instance, rules::core::Lower)

@given(instance=rules::core::Max_strategy)
@settings(max_examples=50)
def test_rules::core::max_instantiation(instance):
    assert isinstance(instance, rules::core::Max)

@given(instance=rules::core::Plus_strategy)
@settings(max_examples=50)
def test_rules::core::plus_instantiation(instance):
    assert isinstance(instance, rules::core::Plus)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=rules::core::Constant_strategy)
@settings(max_examples=50)
def test_rules::core::constant_instantiation(instance):
    assert isinstance(instance, rules::core::Constant)

@given(instance=rules::core::Constant_strategy)
def test_rules::core::constant_integerValue_type(instance):
    assert isinstance(instance.integerValue, int)


@given(instance=rules::core::Constant_strategy)
def test_rules::core::constant_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=rules::core::If_strategy)
@settings(max_examples=50)
def test_rules::core::if_instantiation(instance):
    assert isinstance(instance, rules::core::If)

@given(instance=rules::core::BinaryExp_strategy)
@settings(max_examples=50)
def test_rules::core::binaryexp_instantiation(instance):
    assert isinstance(instance, rules::core::BinaryExp)

@given(instance=rules::core::Filter_strategy)
@settings(max_examples=50)
def test_rules::core::filter_instantiation(instance):
    assert isinstance(instance, rules::core::Filter)

@given(instance=rules::core::Rule_strategy)
@settings(max_examples=50)
def test_rules::core::rule_instantiation(instance):
    assert isinstance(instance, rules::core::Rule)

@given(instance=rules::core::Expression_strategy)
@settings(max_examples=50)
def test_rules::core::expression_instantiation(instance):
    assert isinstance(instance, rules::core::Expression)

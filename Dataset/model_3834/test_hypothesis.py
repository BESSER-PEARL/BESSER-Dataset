import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    realop::NotExp,
    realop::XorExp,
    realop::IsPositive,
    realop::AndExp,
    realop::IsNegative,
    realop::OrExp,
    realop::Expression,
    realop::Operator,
    realop::Realop,
    realop::IsRealised,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_realop::notexp_is_not_abstract():
    assert not inspect.isabstract(realop::NotExp)


def test_realop::notexp_constructor_exists():
    assert callable(realop::NotExp.__init__)


def test_realop::notexp_constructor_args():
    sig = inspect.signature(realop::NotExp.__init__)
    params = list(sig.parameters.keys())



def test_realop::xorexp_is_not_abstract():
    assert not inspect.isabstract(realop::XorExp)


def test_realop::xorexp_constructor_exists():
    assert callable(realop::XorExp.__init__)


def test_realop::xorexp_constructor_args():
    sig = inspect.signature(realop::XorExp.__init__)
    params = list(sig.parameters.keys())



def test_realop::ispositive_is_not_abstract():
    assert not inspect.isabstract(realop::IsPositive)


def test_realop::ispositive_constructor_exists():
    assert callable(realop::IsPositive.__init__)


def test_realop::ispositive_constructor_args():
    sig = inspect.signature(realop::IsPositive.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_realop::ispositive_has_featureName():
    assert hasattr(realop::IsPositive, "featureName")
    descriptor = None
    for klass in realop::IsPositive.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_realop::andexp_is_not_abstract():
    assert not inspect.isabstract(realop::AndExp)


def test_realop::andexp_constructor_exists():
    assert callable(realop::AndExp.__init__)


def test_realop::andexp_constructor_args():
    sig = inspect.signature(realop::AndExp.__init__)
    params = list(sig.parameters.keys())



def test_realop::isnegative_is_not_abstract():
    assert not inspect.isabstract(realop::IsNegative)


def test_realop::isnegative_constructor_exists():
    assert callable(realop::IsNegative.__init__)


def test_realop::isnegative_constructor_args():
    sig = inspect.signature(realop::IsNegative.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_realop::isnegative_has_featureName():
    assert hasattr(realop::IsNegative, "featureName")
    descriptor = None
    for klass in realop::IsNegative.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_realop::orexp_is_not_abstract():
    assert not inspect.isabstract(realop::OrExp)


def test_realop::orexp_constructor_exists():
    assert callable(realop::OrExp.__init__)


def test_realop::orexp_constructor_args():
    sig = inspect.signature(realop::OrExp.__init__)
    params = list(sig.parameters.keys())



def test_realop::expression_is_not_abstract():
    assert not inspect.isabstract(realop::Expression)


def test_realop::expression_constructor_exists():
    assert callable(realop::Expression.__init__)


def test_realop::expression_constructor_args():
    sig = inspect.signature(realop::Expression.__init__)
    params = list(sig.parameters.keys())



def test_realop::operator_is_not_abstract():
    assert not inspect.isabstract(realop::Operator)


def test_realop::operator_constructor_exists():
    assert callable(realop::Operator.__init__)


def test_realop::operator_constructor_args():
    sig = inspect.signature(realop::Operator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_realop::operator_has_name():
    assert hasattr(realop::Operator, "name")
    descriptor = None
    for klass in realop::Operator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_realop::realop_is_not_abstract():
    assert not inspect.isabstract(realop::Realop)


def test_realop::realop_constructor_exists():
    assert callable(realop::Realop.__init__)


def test_realop::realop_constructor_args():
    sig = inspect.signature(realop::Realop.__init__)
    params = list(sig.parameters.keys())



def test_realop::isrealised_is_not_abstract():
    assert not inspect.isabstract(realop::IsRealised)


def test_realop::isrealised_constructor_exists():
    assert callable(realop::IsRealised.__init__)


def test_realop::isrealised_constructor_args():
    sig = inspect.signature(realop::IsRealised.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_realop::isrealised_has_featureName():
    assert hasattr(realop::IsRealised, "featureName")
    descriptor = None
    for klass in realop::IsRealised.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
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
Expression_strategy = st.builds(
    Expression,
)
realop::NotExp_strategy = st.builds(
    realop::NotExp,
)
realop::XorExp_strategy = st.builds(
    realop::XorExp,
)
realop::IsPositive_strategy = st.builds(
    realop::IsPositive,
    featureName=
        safe_text
)
realop::AndExp_strategy = st.builds(
    realop::AndExp,
)
realop::IsNegative_strategy = st.builds(
    realop::IsNegative,
    featureName=
        safe_text
)
realop::OrExp_strategy = st.builds(
    realop::OrExp,
)
realop::Expression_strategy = st.builds(
    realop::Expression,
)
realop::Operator_strategy = st.builds(
    realop::Operator,
    name=
        safe_text
)
realop::Realop_strategy = st.builds(
    realop::Realop,
)
realop::IsRealised_strategy = st.builds(
    realop::IsRealised,
    featureName=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=realop::NotExp_strategy)
@settings(max_examples=50)
def test_realop::notexp_instantiation(instance):
    assert isinstance(instance, realop::NotExp)

@given(instance=realop::XorExp_strategy)
@settings(max_examples=50)
def test_realop::xorexp_instantiation(instance):
    assert isinstance(instance, realop::XorExp)

@given(instance=realop::IsPositive_strategy)
@settings(max_examples=50)
def test_realop::ispositive_instantiation(instance):
    assert isinstance(instance, realop::IsPositive)

@given(instance=realop::IsPositive_strategy)
def test_realop::ispositive_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=realop::IsPositive_strategy)
def test_realop::ispositive_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=realop::AndExp_strategy)
@settings(max_examples=50)
def test_realop::andexp_instantiation(instance):
    assert isinstance(instance, realop::AndExp)

@given(instance=realop::IsNegative_strategy)
@settings(max_examples=50)
def test_realop::isnegative_instantiation(instance):
    assert isinstance(instance, realop::IsNegative)

@given(instance=realop::IsNegative_strategy)
def test_realop::isnegative_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=realop::IsNegative_strategy)
def test_realop::isnegative_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=realop::OrExp_strategy)
@settings(max_examples=50)
def test_realop::orexp_instantiation(instance):
    assert isinstance(instance, realop::OrExp)

@given(instance=realop::Expression_strategy)
@settings(max_examples=50)
def test_realop::expression_instantiation(instance):
    assert isinstance(instance, realop::Expression)

@given(instance=realop::Operator_strategy)
@settings(max_examples=50)
def test_realop::operator_instantiation(instance):
    assert isinstance(instance, realop::Operator)

@given(instance=realop::Operator_strategy)
def test_realop::operator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=realop::Operator_strategy)
def test_realop::operator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=realop::Realop_strategy)
@settings(max_examples=50)
def test_realop::realop_instantiation(instance):
    assert isinstance(instance, realop::Realop)

@given(instance=realop::IsRealised_strategy)
@settings(max_examples=50)
def test_realop::isrealised_instantiation(instance):
    assert isinstance(instance, realop::IsRealised)

@given(instance=realop::IsRealised_strategy)
def test_realop::isrealised_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=realop::IsRealised_strategy)
def test_realop::isrealised_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

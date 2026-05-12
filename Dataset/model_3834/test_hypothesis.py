import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    realop_NotExp,
    realop_XorExp,
    realop_IsNegative,
    realop_IsPositive,
    realop_AndExp,
    realop_OrExp,
    realop_Expression,
    realop_Operator,
    realop_Realop,
    realop_IsRealised,
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



def test_realop_notexp_is_not_abstract():
    assert not inspect.isabstract(realop_NotExp)


def test_realop_notexp_constructor_exists():
    assert callable(realop_NotExp.__init__)


def test_realop_notexp_constructor_args():
    sig = inspect.signature(realop_NotExp.__init__)
    params = list(sig.parameters.keys())



def test_realop_xorexp_is_not_abstract():
    assert not inspect.isabstract(realop_XorExp)


def test_realop_xorexp_constructor_exists():
    assert callable(realop_XorExp.__init__)


def test_realop_xorexp_constructor_args():
    sig = inspect.signature(realop_XorExp.__init__)
    params = list(sig.parameters.keys())



def test_realop_isnegative_is_not_abstract():
    assert not inspect.isabstract(realop_IsNegative)


def test_realop_isnegative_constructor_exists():
    assert callable(realop_IsNegative.__init__)


def test_realop_isnegative_constructor_args():
    sig = inspect.signature(realop_IsNegative.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_realop_isnegative_has_featureName():
    assert hasattr(realop_IsNegative, "featureName")
    descriptor = None
    for klass in realop_IsNegative.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_realop_ispositive_is_not_abstract():
    assert not inspect.isabstract(realop_IsPositive)


def test_realop_ispositive_constructor_exists():
    assert callable(realop_IsPositive.__init__)


def test_realop_ispositive_constructor_args():
    sig = inspect.signature(realop_IsPositive.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_realop_ispositive_has_featureName():
    assert hasattr(realop_IsPositive, "featureName")
    descriptor = None
    for klass in realop_IsPositive.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_realop_andexp_is_not_abstract():
    assert not inspect.isabstract(realop_AndExp)


def test_realop_andexp_constructor_exists():
    assert callable(realop_AndExp.__init__)


def test_realop_andexp_constructor_args():
    sig = inspect.signature(realop_AndExp.__init__)
    params = list(sig.parameters.keys())



def test_realop_orexp_is_not_abstract():
    assert not inspect.isabstract(realop_OrExp)


def test_realop_orexp_constructor_exists():
    assert callable(realop_OrExp.__init__)


def test_realop_orexp_constructor_args():
    sig = inspect.signature(realop_OrExp.__init__)
    params = list(sig.parameters.keys())



def test_realop_expression_is_not_abstract():
    assert not inspect.isabstract(realop_Expression)


def test_realop_expression_constructor_exists():
    assert callable(realop_Expression.__init__)


def test_realop_expression_constructor_args():
    sig = inspect.signature(realop_Expression.__init__)
    params = list(sig.parameters.keys())



def test_realop_operator_is_not_abstract():
    assert not inspect.isabstract(realop_Operator)


def test_realop_operator_constructor_exists():
    assert callable(realop_Operator.__init__)


def test_realop_operator_constructor_args():
    sig = inspect.signature(realop_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_realop_operator_has_name():
    assert hasattr(realop_Operator, "name")
    descriptor = None
    for klass in realop_Operator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_realop_realop_is_not_abstract():
    assert not inspect.isabstract(realop_Realop)


def test_realop_realop_constructor_exists():
    assert callable(realop_Realop.__init__)


def test_realop_realop_constructor_args():
    sig = inspect.signature(realop_Realop.__init__)
    params = list(sig.parameters.keys())



def test_realop_isrealised_is_not_abstract():
    assert not inspect.isabstract(realop_IsRealised)


def test_realop_isrealised_constructor_exists():
    assert callable(realop_IsRealised.__init__)


def test_realop_isrealised_constructor_args():
    sig = inspect.signature(realop_IsRealised.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_realop_isrealised_has_featureName():
    assert hasattr(realop_IsRealised, "featureName")
    descriptor = None
    for klass in realop_IsRealised.__mro__:
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
realop_NotExp_strategy = st.builds(
    realop_NotExp,
)
realop_XorExp_strategy = st.builds(
    realop_XorExp,
)
realop_IsNegative_strategy = st.builds(
    realop_IsNegative,
    featureName=
        safe_text
)
realop_IsPositive_strategy = st.builds(
    realop_IsPositive,
    featureName=
        safe_text
)
realop_AndExp_strategy = st.builds(
    realop_AndExp,
)
realop_OrExp_strategy = st.builds(
    realop_OrExp,
)
realop_Expression_strategy = st.builds(
    realop_Expression,
)
realop_Operator_strategy = st.builds(
    realop_Operator,
    name=
        safe_text
)
realop_Realop_strategy = st.builds(
    realop_Realop,
)
realop_IsRealised_strategy = st.builds(
    realop_IsRealised,
    featureName=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=realop_NotExp_strategy)
@settings(max_examples=50)
def test_realop_notexp_instantiation(instance):
    assert isinstance(instance, realop_NotExp)

@given(instance=realop_XorExp_strategy)
@settings(max_examples=50)
def test_realop_xorexp_instantiation(instance):
    assert isinstance(instance, realop_XorExp)

@given(instance=realop_IsNegative_strategy)
@settings(max_examples=50)
def test_realop_isnegative_instantiation(instance):
    assert isinstance(instance, realop_IsNegative)



@given(instance=realop_IsNegative_strategy)
def test_realop_isnegative_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=realop_IsPositive_strategy)
@settings(max_examples=50)
def test_realop_ispositive_instantiation(instance):
    assert isinstance(instance, realop_IsPositive)



@given(instance=realop_IsPositive_strategy)
def test_realop_ispositive_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=realop_AndExp_strategy)
@settings(max_examples=50)
def test_realop_andexp_instantiation(instance):
    assert isinstance(instance, realop_AndExp)

@given(instance=realop_OrExp_strategy)
@settings(max_examples=50)
def test_realop_orexp_instantiation(instance):
    assert isinstance(instance, realop_OrExp)

@given(instance=realop_Expression_strategy)
@settings(max_examples=50)
def test_realop_expression_instantiation(instance):
    assert isinstance(instance, realop_Expression)

@given(instance=realop_Operator_strategy)
@settings(max_examples=50)
def test_realop_operator_instantiation(instance):
    assert isinstance(instance, realop_Operator)



@given(instance=realop_Operator_strategy)
def test_realop_operator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=realop_Realop_strategy)
@settings(max_examples=50)
def test_realop_realop_instantiation(instance):
    assert isinstance(instance, realop_Realop)

@given(instance=realop_IsRealised_strategy)
@settings(max_examples=50)
def test_realop_isrealised_instantiation(instance):
    assert isinstance(instance, realop_IsRealised)



@given(instance=realop_IsRealised_strategy)
def test_realop_isrealised_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

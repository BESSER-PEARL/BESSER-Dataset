import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    asso::Variable,
    asso::Model,
    Expression,
    asso::Plus,
    asso::Div,
    asso::Mult,
    asso::Minus,
    asso::VariableRef,
    asso::NegFloatConstant,
    asso::FloatConstant,
    asso::Expression,
    asso::EvalExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_asso::variable_is_not_abstract():
    assert not inspect.isabstract(asso::Variable)


def test_asso::variable_constructor_exists():
    assert callable(asso::Variable.__init__)


def test_asso::variable_constructor_args():
    sig = inspect.signature(asso::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asso::variable_has_name():
    assert hasattr(asso::Variable, "name")
    descriptor = None
    for klass in asso::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asso::model_is_not_abstract():
    assert not inspect.isabstract(asso::Model)


def test_asso::model_constructor_exists():
    assert callable(asso::Model.__init__)


def test_asso::model_constructor_args():
    sig = inspect.signature(asso::Model.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_asso::plus_is_not_abstract():
    assert not inspect.isabstract(asso::Plus)


def test_asso::plus_constructor_exists():
    assert callable(asso::Plus.__init__)


def test_asso::plus_constructor_args():
    sig = inspect.signature(asso::Plus.__init__)
    params = list(sig.parameters.keys())



def test_asso::div_is_not_abstract():
    assert not inspect.isabstract(asso::Div)


def test_asso::div_constructor_exists():
    assert callable(asso::Div.__init__)


def test_asso::div_constructor_args():
    sig = inspect.signature(asso::Div.__init__)
    params = list(sig.parameters.keys())



def test_asso::mult_is_not_abstract():
    assert not inspect.isabstract(asso::Mult)


def test_asso::mult_constructor_exists():
    assert callable(asso::Mult.__init__)


def test_asso::mult_constructor_args():
    sig = inspect.signature(asso::Mult.__init__)
    params = list(sig.parameters.keys())



def test_asso::minus_is_not_abstract():
    assert not inspect.isabstract(asso::Minus)


def test_asso::minus_constructor_exists():
    assert callable(asso::Minus.__init__)


def test_asso::minus_constructor_args():
    sig = inspect.signature(asso::Minus.__init__)
    params = list(sig.parameters.keys())



def test_asso::variableref_is_not_abstract():
    assert not inspect.isabstract(asso::VariableRef)


def test_asso::variableref_constructor_exists():
    assert callable(asso::VariableRef.__init__)


def test_asso::variableref_constructor_args():
    sig = inspect.signature(asso::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_asso::negfloatconstant_is_not_abstract():
    assert not inspect.isabstract(asso::NegFloatConstant)


def test_asso::negfloatconstant_constructor_exists():
    assert callable(asso::NegFloatConstant.__init__)


def test_asso::negfloatconstant_constructor_args():
    sig = inspect.signature(asso::NegFloatConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_asso::negfloatconstant_has_value():
    assert hasattr(asso::NegFloatConstant, "value")
    descriptor = None
    for klass in asso::NegFloatConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_asso::floatconstant_is_not_abstract():
    assert not inspect.isabstract(asso::FloatConstant)


def test_asso::floatconstant_constructor_exists():
    assert callable(asso::FloatConstant.__init__)


def test_asso::floatconstant_constructor_args():
    sig = inspect.signature(asso::FloatConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_asso::floatconstant_has_value():
    assert hasattr(asso::FloatConstant, "value")
    descriptor = None
    for klass in asso::FloatConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_asso::expression_is_not_abstract():
    assert not inspect.isabstract(asso::Expression)


def test_asso::expression_constructor_exists():
    assert callable(asso::Expression.__init__)


def test_asso::expression_constructor_args():
    sig = inspect.signature(asso::Expression.__init__)
    params = list(sig.parameters.keys())



def test_asso::evalexpression_is_not_abstract():
    assert not inspect.isabstract(asso::EvalExpression)


def test_asso::evalexpression_constructor_exists():
    assert callable(asso::EvalExpression.__init__)


def test_asso::evalexpression_constructor_args():
    sig = inspect.signature(asso::EvalExpression.__init__)
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
asso::Variable_strategy = st.builds(
    asso::Variable,
    name=
        safe_text
)
asso::Model_strategy = st.builds(
    asso::Model,
)
Expression_strategy = st.builds(
    Expression,
)
asso::Plus_strategy = st.builds(
    asso::Plus,
)
asso::Div_strategy = st.builds(
    asso::Div,
)
asso::Mult_strategy = st.builds(
    asso::Mult,
)
asso::Minus_strategy = st.builds(
    asso::Minus,
)
asso::VariableRef_strategy = st.builds(
    asso::VariableRef,
)
asso::NegFloatConstant_strategy = st.builds(
    asso::NegFloatConstant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
asso::FloatConstant_strategy = st.builds(
    asso::FloatConstant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
asso::Expression_strategy = st.builds(
    asso::Expression,
)
asso::EvalExpression_strategy = st.builds(
    asso::EvalExpression,
)

@given(instance=asso::Variable_strategy)
@settings(max_examples=50)
def test_asso::variable_instantiation(instance):
    assert isinstance(instance, asso::Variable)

@given(instance=asso::Variable_strategy)
def test_asso::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=asso::Variable_strategy)
def test_asso::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=asso::Model_strategy)
@settings(max_examples=50)
def test_asso::model_instantiation(instance):
    assert isinstance(instance, asso::Model)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=asso::Plus_strategy)
@settings(max_examples=50)
def test_asso::plus_instantiation(instance):
    assert isinstance(instance, asso::Plus)

@given(instance=asso::Div_strategy)
@settings(max_examples=50)
def test_asso::div_instantiation(instance):
    assert isinstance(instance, asso::Div)

@given(instance=asso::Mult_strategy)
@settings(max_examples=50)
def test_asso::mult_instantiation(instance):
    assert isinstance(instance, asso::Mult)

@given(instance=asso::Minus_strategy)
@settings(max_examples=50)
def test_asso::minus_instantiation(instance):
    assert isinstance(instance, asso::Minus)

@given(instance=asso::VariableRef_strategy)
@settings(max_examples=50)
def test_asso::variableref_instantiation(instance):
    assert isinstance(instance, asso::VariableRef)

@given(instance=asso::NegFloatConstant_strategy)
@settings(max_examples=50)
def test_asso::negfloatconstant_instantiation(instance):
    assert isinstance(instance, asso::NegFloatConstant)

@given(instance=asso::NegFloatConstant_strategy)
def test_asso::negfloatconstant_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=asso::NegFloatConstant_strategy)
def test_asso::negfloatconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=asso::FloatConstant_strategy)
@settings(max_examples=50)
def test_asso::floatconstant_instantiation(instance):
    assert isinstance(instance, asso::FloatConstant)

@given(instance=asso::FloatConstant_strategy)
def test_asso::floatconstant_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=asso::FloatConstant_strategy)
def test_asso::floatconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=asso::Expression_strategy)
@settings(max_examples=50)
def test_asso::expression_instantiation(instance):
    assert isinstance(instance, asso::Expression)

@given(instance=asso::EvalExpression_strategy)
@settings(max_examples=50)
def test_asso::evalexpression_instantiation(instance):
    assert isinstance(instance, asso::EvalExpression)

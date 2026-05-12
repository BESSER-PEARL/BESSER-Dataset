import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    asso_Variable,
    asso_Model,
    Expression,
    asso_Mult,
    asso_NegFloatConstant,
    asso_Div,
    asso_Plus,
    asso_Minus,
    asso_VariableRef,
    asso_FloatConstant,
    asso_Expression,
    asso_EvalExpression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_asso_variable_is_not_abstract():
    assert not inspect.isabstract(asso_Variable)


def test_asso_variable_constructor_exists():
    assert callable(asso_Variable.__init__)


def test_asso_variable_constructor_args():
    sig = inspect.signature(asso_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asso_variable_has_name():
    assert hasattr(asso_Variable, "name")
    descriptor = None
    for klass in asso_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_asso_model_is_not_abstract():
    assert not inspect.isabstract(asso_Model)


def test_asso_model_constructor_exists():
    assert callable(asso_Model.__init__)


def test_asso_model_constructor_args():
    sig = inspect.signature(asso_Model.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_asso_mult_is_not_abstract():
    assert not inspect.isabstract(asso_Mult)


def test_asso_mult_constructor_exists():
    assert callable(asso_Mult.__init__)


def test_asso_mult_constructor_args():
    sig = inspect.signature(asso_Mult.__init__)
    params = list(sig.parameters.keys())



def test_asso_negfloatconstant_is_not_abstract():
    assert not inspect.isabstract(asso_NegFloatConstant)


def test_asso_negfloatconstant_constructor_exists():
    assert callable(asso_NegFloatConstant.__init__)


def test_asso_negfloatconstant_constructor_args():
    sig = inspect.signature(asso_NegFloatConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_asso_negfloatconstant_has_value():
    assert hasattr(asso_NegFloatConstant, "value")
    descriptor = None
    for klass in asso_NegFloatConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_asso_div_is_not_abstract():
    assert not inspect.isabstract(asso_Div)


def test_asso_div_constructor_exists():
    assert callable(asso_Div.__init__)


def test_asso_div_constructor_args():
    sig = inspect.signature(asso_Div.__init__)
    params = list(sig.parameters.keys())



def test_asso_plus_is_not_abstract():
    assert not inspect.isabstract(asso_Plus)


def test_asso_plus_constructor_exists():
    assert callable(asso_Plus.__init__)


def test_asso_plus_constructor_args():
    sig = inspect.signature(asso_Plus.__init__)
    params = list(sig.parameters.keys())



def test_asso_minus_is_not_abstract():
    assert not inspect.isabstract(asso_Minus)


def test_asso_minus_constructor_exists():
    assert callable(asso_Minus.__init__)


def test_asso_minus_constructor_args():
    sig = inspect.signature(asso_Minus.__init__)
    params = list(sig.parameters.keys())



def test_asso_variableref_is_not_abstract():
    assert not inspect.isabstract(asso_VariableRef)


def test_asso_variableref_constructor_exists():
    assert callable(asso_VariableRef.__init__)


def test_asso_variableref_constructor_args():
    sig = inspect.signature(asso_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_asso_floatconstant_is_not_abstract():
    assert not inspect.isabstract(asso_FloatConstant)


def test_asso_floatconstant_constructor_exists():
    assert callable(asso_FloatConstant.__init__)


def test_asso_floatconstant_constructor_args():
    sig = inspect.signature(asso_FloatConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_asso_floatconstant_has_value():
    assert hasattr(asso_FloatConstant, "value")
    descriptor = None
    for klass in asso_FloatConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_asso_expression_is_not_abstract():
    assert not inspect.isabstract(asso_Expression)


def test_asso_expression_constructor_exists():
    assert callable(asso_Expression.__init__)


def test_asso_expression_constructor_args():
    sig = inspect.signature(asso_Expression.__init__)
    params = list(sig.parameters.keys())



def test_asso_evalexpression_is_not_abstract():
    assert not inspect.isabstract(asso_EvalExpression)


def test_asso_evalexpression_constructor_exists():
    assert callable(asso_EvalExpression.__init__)


def test_asso_evalexpression_constructor_args():
    sig = inspect.signature(asso_EvalExpression.__init__)
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
asso_Variable_strategy = st.builds(
    asso_Variable,
    name=
        safe_text
)
asso_Model_strategy = st.builds(
    asso_Model,
)
Expression_strategy = st.builds(
    Expression,
)
asso_Mult_strategy = st.builds(
    asso_Mult,
)
asso_NegFloatConstant_strategy = st.builds(
    asso_NegFloatConstant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
asso_Div_strategy = st.builds(
    asso_Div,
)
asso_Plus_strategy = st.builds(
    asso_Plus,
)
asso_Minus_strategy = st.builds(
    asso_Minus,
)
asso_VariableRef_strategy = st.builds(
    asso_VariableRef,
)
asso_FloatConstant_strategy = st.builds(
    asso_FloatConstant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
asso_Expression_strategy = st.builds(
    asso_Expression,
)
asso_EvalExpression_strategy = st.builds(
    asso_EvalExpression,
)

@given(instance=asso_Variable_strategy)
@settings(max_examples=50)
def test_asso_variable_instantiation(instance):
    assert isinstance(instance, asso_Variable)



@given(instance=asso_Variable_strategy)
def test_asso_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=asso_Model_strategy)
@settings(max_examples=50)
def test_asso_model_instantiation(instance):
    assert isinstance(instance, asso_Model)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=asso_Mult_strategy)
@settings(max_examples=50)
def test_asso_mult_instantiation(instance):
    assert isinstance(instance, asso_Mult)

@given(instance=asso_NegFloatConstant_strategy)
@settings(max_examples=50)
def test_asso_negfloatconstant_instantiation(instance):
    assert isinstance(instance, asso_NegFloatConstant)



@given(instance=asso_NegFloatConstant_strategy)
def test_asso_negfloatconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=asso_Div_strategy)
@settings(max_examples=50)
def test_asso_div_instantiation(instance):
    assert isinstance(instance, asso_Div)

@given(instance=asso_Plus_strategy)
@settings(max_examples=50)
def test_asso_plus_instantiation(instance):
    assert isinstance(instance, asso_Plus)

@given(instance=asso_Minus_strategy)
@settings(max_examples=50)
def test_asso_minus_instantiation(instance):
    assert isinstance(instance, asso_Minus)

@given(instance=asso_VariableRef_strategy)
@settings(max_examples=50)
def test_asso_variableref_instantiation(instance):
    assert isinstance(instance, asso_VariableRef)

@given(instance=asso_FloatConstant_strategy)
@settings(max_examples=50)
def test_asso_floatconstant_instantiation(instance):
    assert isinstance(instance, asso_FloatConstant)



@given(instance=asso_FloatConstant_strategy)
def test_asso_floatconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=asso_Expression_strategy)
@settings(max_examples=50)
def test_asso_expression_instantiation(instance):
    assert isinstance(instance, asso_Expression)

@given(instance=asso_EvalExpression_strategy)
@settings(max_examples=50)
def test_asso_evalexpression_instantiation(instance):
    assert isinstance(instance, asso_EvalExpression)

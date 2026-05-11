import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryOperator,
    expressions::Plus,
    expressions::Model,
    UnaryOperator,
    expressions::Neg,
    expressions::Div,
    expressions::Mul,
    expressions::Minus,
    Expression,
    expressions::UnaryOperator,
    expressions::ParameterAccess,
    expressions::BinaryOperator,
    expressions::FunctionCall,
    expressions::Number,
    expressions::Expression,
    expressions::Parameter,
    expressions::Function,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_expressions::plus_is_not_abstract():
    assert not inspect.isabstract(expressions::Plus)


def test_expressions::plus_constructor_exists():
    assert callable(expressions::Plus.__init__)


def test_expressions::plus_constructor_args():
    sig = inspect.signature(expressions::Plus.__init__)
    params = list(sig.parameters.keys())



def test_expressions::model_is_not_abstract():
    assert not inspect.isabstract(expressions::Model)


def test_expressions::model_constructor_exists():
    assert callable(expressions::Model.__init__)


def test_expressions::model_constructor_args():
    sig = inspect.signature(expressions::Model.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_expressions::neg_is_not_abstract():
    assert not inspect.isabstract(expressions::Neg)


def test_expressions::neg_constructor_exists():
    assert callable(expressions::Neg.__init__)


def test_expressions::neg_constructor_args():
    sig = inspect.signature(expressions::Neg.__init__)
    params = list(sig.parameters.keys())



def test_expressions::div_is_not_abstract():
    assert not inspect.isabstract(expressions::Div)


def test_expressions::div_constructor_exists():
    assert callable(expressions::Div.__init__)


def test_expressions::div_constructor_args():
    sig = inspect.signature(expressions::Div.__init__)
    params = list(sig.parameters.keys())



def test_expressions::mul_is_not_abstract():
    assert not inspect.isabstract(expressions::Mul)


def test_expressions::mul_constructor_exists():
    assert callable(expressions::Mul.__init__)


def test_expressions::mul_constructor_args():
    sig = inspect.signature(expressions::Mul.__init__)
    params = list(sig.parameters.keys())



def test_expressions::minus_is_not_abstract():
    assert not inspect.isabstract(expressions::Minus)


def test_expressions::minus_constructor_exists():
    assert callable(expressions::Minus.__init__)


def test_expressions::minus_constructor_args():
    sig = inspect.signature(expressions::Minus.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(expressions::UnaryOperator)


def test_expressions::unaryoperator_constructor_exists():
    assert callable(expressions::UnaryOperator.__init__)


def test_expressions::unaryoperator_constructor_args():
    sig = inspect.signature(expressions::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_expressions::parameteraccess_is_not_abstract():
    assert not inspect.isabstract(expressions::ParameterAccess)


def test_expressions::parameteraccess_constructor_exists():
    assert callable(expressions::ParameterAccess.__init__)


def test_expressions::parameteraccess_constructor_args():
    sig = inspect.signature(expressions::ParameterAccess.__init__)
    params = list(sig.parameters.keys())



def test_expressions::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(expressions::BinaryOperator)


def test_expressions::binaryoperator_constructor_exists():
    assert callable(expressions::BinaryOperator.__init__)


def test_expressions::binaryoperator_constructor_args():
    sig = inspect.signature(expressions::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_expressions::functioncall_is_not_abstract():
    assert not inspect.isabstract(expressions::FunctionCall)


def test_expressions::functioncall_constructor_exists():
    assert callable(expressions::FunctionCall.__init__)


def test_expressions::functioncall_constructor_args():
    sig = inspect.signature(expressions::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_expressions::number_is_not_abstract():
    assert not inspect.isabstract(expressions::Number)


def test_expressions::number_constructor_exists():
    assert callable(expressions::Number.__init__)


def test_expressions::number_constructor_args():
    sig = inspect.signature(expressions::Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions::number_has_value():
    assert hasattr(expressions::Number, "value")
    descriptor = None
    for klass in expressions::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions::expression_is_not_abstract():
    assert not inspect.isabstract(expressions::Expression)


def test_expressions::expression_constructor_exists():
    assert callable(expressions::Expression.__init__)


def test_expressions::expression_constructor_args():
    sig = inspect.signature(expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::parameter_is_not_abstract():
    assert not inspect.isabstract(expressions::Parameter)


def test_expressions::parameter_constructor_exists():
    assert callable(expressions::Parameter.__init__)


def test_expressions::parameter_constructor_args():
    sig = inspect.signature(expressions::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_expressions::parameter_has_name():
    assert hasattr(expressions::Parameter, "name")
    descriptor = None
    for klass in expressions::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expressions::function_is_not_abstract():
    assert not inspect.isabstract(expressions::Function)


def test_expressions::function_constructor_exists():
    assert callable(expressions::Function.__init__)


def test_expressions::function_constructor_args():
    sig = inspect.signature(expressions::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_expressions::function_has_name():
    assert hasattr(expressions::Function, "name")
    descriptor = None
    for klass in expressions::Function.__mro__:
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
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
expressions::Plus_strategy = st.builds(
    expressions::Plus,
)
expressions::Model_strategy = st.builds(
    expressions::Model,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
expressions::Neg_strategy = st.builds(
    expressions::Neg,
)
expressions::Div_strategy = st.builds(
    expressions::Div,
)
expressions::Mul_strategy = st.builds(
    expressions::Mul,
)
expressions::Minus_strategy = st.builds(
    expressions::Minus,
)
Expression_strategy = st.builds(
    Expression,
)
expressions::UnaryOperator_strategy = st.builds(
    expressions::UnaryOperator,
)
expressions::ParameterAccess_strategy = st.builds(
    expressions::ParameterAccess,
)
expressions::BinaryOperator_strategy = st.builds(
    expressions::BinaryOperator,
)
expressions::FunctionCall_strategy = st.builds(
    expressions::FunctionCall,
)
expressions::Number_strategy = st.builds(
    expressions::Number,
    value=
        st.integers()
)
expressions::Expression_strategy = st.builds(
    expressions::Expression,
)
expressions::Parameter_strategy = st.builds(
    expressions::Parameter,
    name=
        safe_text
)
expressions::Function_strategy = st.builds(
    expressions::Function,
    name=
        safe_text
)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=expressions::Plus_strategy)
@settings(max_examples=50)
def test_expressions::plus_instantiation(instance):
    assert isinstance(instance, expressions::Plus)

@given(instance=expressions::Model_strategy)
@settings(max_examples=50)
def test_expressions::model_instantiation(instance):
    assert isinstance(instance, expressions::Model)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=expressions::Neg_strategy)
@settings(max_examples=50)
def test_expressions::neg_instantiation(instance):
    assert isinstance(instance, expressions::Neg)

@given(instance=expressions::Div_strategy)
@settings(max_examples=50)
def test_expressions::div_instantiation(instance):
    assert isinstance(instance, expressions::Div)

@given(instance=expressions::Mul_strategy)
@settings(max_examples=50)
def test_expressions::mul_instantiation(instance):
    assert isinstance(instance, expressions::Mul)

@given(instance=expressions::Minus_strategy)
@settings(max_examples=50)
def test_expressions::minus_instantiation(instance):
    assert isinstance(instance, expressions::Minus)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expressions::UnaryOperator_strategy)
@settings(max_examples=50)
def test_expressions::unaryoperator_instantiation(instance):
    assert isinstance(instance, expressions::UnaryOperator)

@given(instance=expressions::ParameterAccess_strategy)
@settings(max_examples=50)
def test_expressions::parameteraccess_instantiation(instance):
    assert isinstance(instance, expressions::ParameterAccess)

@given(instance=expressions::BinaryOperator_strategy)
@settings(max_examples=50)
def test_expressions::binaryoperator_instantiation(instance):
    assert isinstance(instance, expressions::BinaryOperator)

@given(instance=expressions::FunctionCall_strategy)
@settings(max_examples=50)
def test_expressions::functioncall_instantiation(instance):
    assert isinstance(instance, expressions::FunctionCall)

@given(instance=expressions::Number_strategy)
@settings(max_examples=50)
def test_expressions::number_instantiation(instance):
    assert isinstance(instance, expressions::Number)

@given(instance=expressions::Number_strategy)
def test_expressions::number_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=expressions::Number_strategy)
def test_expressions::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions::Expression_strategy)
@settings(max_examples=50)
def test_expressions::expression_instantiation(instance):
    assert isinstance(instance, expressions::Expression)

@given(instance=expressions::Parameter_strategy)
@settings(max_examples=50)
def test_expressions::parameter_instantiation(instance):
    assert isinstance(instance, expressions::Parameter)

@given(instance=expressions::Parameter_strategy)
def test_expressions::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=expressions::Parameter_strategy)
def test_expressions::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=expressions::Function_strategy)
@settings(max_examples=50)
def test_expressions::function_instantiation(instance):
    assert isinstance(instance, expressions::Function)

@given(instance=expressions::Function_strategy)
def test_expressions::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=expressions::Function_strategy)
def test_expressions::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

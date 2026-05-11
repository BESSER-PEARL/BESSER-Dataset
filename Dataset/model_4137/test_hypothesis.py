import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Primary,
    mathInterpreter::VariableRef,
    mathInterpreter::Bracket,
    mathInterpreter::Num,
    MultiplyOrDivide,
    mathInterpreter::Divide,
    mathInterpreter::Multiply,
    PlusOrMinus,
    mathInterpreter::Minus,
    mathInterpreter::Plus,
    mathInterpreter::Primary,
    mathInterpreter::MultiplyOrDivide,
    mathInterpreter::EObject,
    mathInterpreter::PlusOrMinus,
    mathInterpreter::Expression,
    mathInterpreter::Variable,
    mathInterpreter::Solution,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::variableref_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::VariableRef)


def test_mathinterpreter::variableref_constructor_exists():
    assert callable(mathInterpreter::VariableRef.__init__)


def test_mathinterpreter::variableref_constructor_args():
    sig = inspect.signature(mathInterpreter::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::bracket_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Bracket)


def test_mathinterpreter::bracket_constructor_exists():
    assert callable(mathInterpreter::Bracket.__init__)


def test_mathinterpreter::bracket_constructor_args():
    sig = inspect.signature(mathInterpreter::Bracket.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::num_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Num)


def test_mathinterpreter::num_constructor_exists():
    assert callable(mathInterpreter::Num.__init__)


def test_mathinterpreter::num_constructor_args():
    sig = inspect.signature(mathInterpreter::Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathinterpreter::num_has_value():
    assert hasattr(mathInterpreter::Num, "value")
    descriptor = None
    for klass in mathInterpreter::Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_multiplyordivide_is_not_abstract():
    assert not inspect.isabstract(MultiplyOrDivide)


def test_multiplyordivide_constructor_exists():
    assert callable(MultiplyOrDivide.__init__)


def test_multiplyordivide_constructor_args():
    sig = inspect.signature(MultiplyOrDivide.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::divide_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Divide)


def test_mathinterpreter::divide_constructor_exists():
    assert callable(mathInterpreter::Divide.__init__)


def test_mathinterpreter::divide_constructor_args():
    sig = inspect.signature(mathInterpreter::Divide.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::multiply_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Multiply)


def test_mathinterpreter::multiply_constructor_exists():
    assert callable(mathInterpreter::Multiply.__init__)


def test_mathinterpreter::multiply_constructor_args():
    sig = inspect.signature(mathInterpreter::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_plusorminus_is_not_abstract():
    assert not inspect.isabstract(PlusOrMinus)


def test_plusorminus_constructor_exists():
    assert callable(PlusOrMinus.__init__)


def test_plusorminus_constructor_args():
    sig = inspect.signature(PlusOrMinus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::minus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Minus)


def test_mathinterpreter::minus_constructor_exists():
    assert callable(mathInterpreter::Minus.__init__)


def test_mathinterpreter::minus_constructor_args():
    sig = inspect.signature(mathInterpreter::Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::plus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Plus)


def test_mathinterpreter::plus_constructor_exists():
    assert callable(mathInterpreter::Plus.__init__)


def test_mathinterpreter::plus_constructor_args():
    sig = inspect.signature(mathInterpreter::Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::primary_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Primary)


def test_mathinterpreter::primary_constructor_exists():
    assert callable(mathInterpreter::Primary.__init__)


def test_mathinterpreter::primary_constructor_args():
    sig = inspect.signature(mathInterpreter::Primary.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::multiplyordivide_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::MultiplyOrDivide)


def test_mathinterpreter::multiplyordivide_constructor_exists():
    assert callable(mathInterpreter::MultiplyOrDivide.__init__)


def test_mathinterpreter::multiplyordivide_constructor_args():
    sig = inspect.signature(mathInterpreter::MultiplyOrDivide.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mathinterpreter::multiplyordivide_has_operator():
    assert hasattr(mathInterpreter::MultiplyOrDivide, "operator")
    descriptor = None
    for klass in mathInterpreter::MultiplyOrDivide.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpreter::eobject_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::EObject)


def test_mathinterpreter::eobject_constructor_exists():
    assert callable(mathInterpreter::EObject.__init__)


def test_mathinterpreter::eobject_constructor_args():
    sig = inspect.signature(mathInterpreter::EObject.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::plusorminus_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::PlusOrMinus)


def test_mathinterpreter::plusorminus_constructor_exists():
    assert callable(mathInterpreter::PlusOrMinus.__init__)


def test_mathinterpreter::plusorminus_constructor_args():
    sig = inspect.signature(mathInterpreter::PlusOrMinus.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mathinterpreter::plusorminus_has_operator():
    assert hasattr(mathInterpreter::PlusOrMinus, "operator")
    descriptor = None
    for klass in mathInterpreter::PlusOrMinus.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpreter::expression_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Expression)


def test_mathinterpreter::expression_constructor_exists():
    assert callable(mathInterpreter::Expression.__init__)


def test_mathinterpreter::expression_constructor_args():
    sig = inspect.signature(mathInterpreter::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mathinterpreter::variable_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Variable)


def test_mathinterpreter::variable_constructor_exists():
    assert callable(mathInterpreter::Variable.__init__)


def test_mathinterpreter::variable_constructor_args():
    sig = inspect.signature(mathInterpreter::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mathinterpreter::variable_has_name():
    assert hasattr(mathInterpreter::Variable, "name")
    descriptor = None
    for klass in mathInterpreter::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mathinterpreter::solution_is_not_abstract():
    assert not inspect.isabstract(mathInterpreter::Solution)


def test_mathinterpreter::solution_constructor_exists():
    assert callable(mathInterpreter::Solution.__init__)


def test_mathinterpreter::solution_constructor_args():
    sig = inspect.signature(mathInterpreter::Solution.__init__)
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
Primary_strategy = st.builds(
    Primary,
)
mathInterpreter::VariableRef_strategy = st.builds(
    mathInterpreter::VariableRef,
)
mathInterpreter::Bracket_strategy = st.builds(
    mathInterpreter::Bracket,
)
mathInterpreter::Num_strategy = st.builds(
    mathInterpreter::Num,
    value=
        st.integers()
)
MultiplyOrDivide_strategy = st.builds(
    MultiplyOrDivide,
)
mathInterpreter::Divide_strategy = st.builds(
    mathInterpreter::Divide,
)
mathInterpreter::Multiply_strategy = st.builds(
    mathInterpreter::Multiply,
)
PlusOrMinus_strategy = st.builds(
    PlusOrMinus,
)
mathInterpreter::Minus_strategy = st.builds(
    mathInterpreter::Minus,
)
mathInterpreter::Plus_strategy = st.builds(
    mathInterpreter::Plus,
)
mathInterpreter::Primary_strategy = st.builds(
    mathInterpreter::Primary,
)
mathInterpreter::MultiplyOrDivide_strategy = st.builds(
    mathInterpreter::MultiplyOrDivide,
    operator=
        safe_text
)
mathInterpreter::EObject_strategy = st.builds(
    mathInterpreter::EObject,
)
mathInterpreter::PlusOrMinus_strategy = st.builds(
    mathInterpreter::PlusOrMinus,
    operator=
        safe_text
)
mathInterpreter::Expression_strategy = st.builds(
    mathInterpreter::Expression,
)
mathInterpreter::Variable_strategy = st.builds(
    mathInterpreter::Variable,
    name=
        safe_text
)
mathInterpreter::Solution_strategy = st.builds(
    mathInterpreter::Solution,
)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=mathInterpreter::VariableRef_strategy)
@settings(max_examples=50)
def test_mathinterpreter::variableref_instantiation(instance):
    assert isinstance(instance, mathInterpreter::VariableRef)

@given(instance=mathInterpreter::Bracket_strategy)
@settings(max_examples=50)
def test_mathinterpreter::bracket_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Bracket)

@given(instance=mathInterpreter::Num_strategy)
@settings(max_examples=50)
def test_mathinterpreter::num_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Num)

@given(instance=mathInterpreter::Num_strategy)
def test_mathinterpreter::num_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=mathInterpreter::Num_strategy)
def test_mathinterpreter::num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MultiplyOrDivide_strategy)
@settings(max_examples=50)
def test_multiplyordivide_instantiation(instance):
    assert isinstance(instance, MultiplyOrDivide)

@given(instance=mathInterpreter::Divide_strategy)
@settings(max_examples=50)
def test_mathinterpreter::divide_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Divide)

@given(instance=mathInterpreter::Multiply_strategy)
@settings(max_examples=50)
def test_mathinterpreter::multiply_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Multiply)

@given(instance=PlusOrMinus_strategy)
@settings(max_examples=50)
def test_plusorminus_instantiation(instance):
    assert isinstance(instance, PlusOrMinus)

@given(instance=mathInterpreter::Minus_strategy)
@settings(max_examples=50)
def test_mathinterpreter::minus_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Minus)

@given(instance=mathInterpreter::Plus_strategy)
@settings(max_examples=50)
def test_mathinterpreter::plus_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Plus)

@given(instance=mathInterpreter::Primary_strategy)
@settings(max_examples=50)
def test_mathinterpreter::primary_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Primary)

@given(instance=mathInterpreter::MultiplyOrDivide_strategy)
@settings(max_examples=50)
def test_mathinterpreter::multiplyordivide_instantiation(instance):
    assert isinstance(instance, mathInterpreter::MultiplyOrDivide)

@given(instance=mathInterpreter::MultiplyOrDivide_strategy)
def test_mathinterpreter::multiplyordivide_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=mathInterpreter::MultiplyOrDivide_strategy)
def test_mathinterpreter::multiplyordivide_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=mathInterpreter::EObject_strategy)
@settings(max_examples=50)
def test_mathinterpreter::eobject_instantiation(instance):
    assert isinstance(instance, mathInterpreter::EObject)

@given(instance=mathInterpreter::PlusOrMinus_strategy)
@settings(max_examples=50)
def test_mathinterpreter::plusorminus_instantiation(instance):
    assert isinstance(instance, mathInterpreter::PlusOrMinus)

@given(instance=mathInterpreter::PlusOrMinus_strategy)
def test_mathinterpreter::plusorminus_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=mathInterpreter::PlusOrMinus_strategy)
def test_mathinterpreter::plusorminus_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=mathInterpreter::Expression_strategy)
@settings(max_examples=50)
def test_mathinterpreter::expression_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Expression)

@given(instance=mathInterpreter::Variable_strategy)
@settings(max_examples=50)
def test_mathinterpreter::variable_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Variable)

@given(instance=mathInterpreter::Variable_strategy)
def test_mathinterpreter::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mathInterpreter::Variable_strategy)
def test_mathinterpreter::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mathInterpreter::Solution_strategy)
@settings(max_examples=50)
def test_mathinterpreter::solution_instantiation(instance):
    assert isinstance(instance, mathInterpreter::Solution)

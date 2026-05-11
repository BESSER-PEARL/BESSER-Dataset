import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    expressions::VariableRef,
    expressions::Minus,
    expressions::IntConstant,
    expressions::StringConstant,
    expressions::Not,
    expressions::MulOrDiv,
    expressions::Plus,
    expressions::BoolConstant,
    expressions::Or,
    AbstractElement,
    expressions::EvalExpression,
    expressions::Variable,
    expressions::Expression,
    expressions::AbstractElement,
    expressions::ExpressionsModel,
    expressions::Comparison,
    expressions::Equality,
    expressions::And,
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



def test_expressions::variableref_is_not_abstract():
    assert not inspect.isabstract(expressions::VariableRef)


def test_expressions::variableref_constructor_exists():
    assert callable(expressions::VariableRef.__init__)


def test_expressions::variableref_constructor_args():
    sig = inspect.signature(expressions::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_expressions::minus_is_not_abstract():
    assert not inspect.isabstract(expressions::Minus)


def test_expressions::minus_constructor_exists():
    assert callable(expressions::Minus.__init__)


def test_expressions::minus_constructor_args():
    sig = inspect.signature(expressions::Minus.__init__)
    params = list(sig.parameters.keys())



def test_expressions::intconstant_is_not_abstract():
    assert not inspect.isabstract(expressions::IntConstant)


def test_expressions::intconstant_constructor_exists():
    assert callable(expressions::IntConstant.__init__)


def test_expressions::intconstant_constructor_args():
    sig = inspect.signature(expressions::IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions::intconstant_has_value():
    assert hasattr(expressions::IntConstant, "value")
    descriptor = None
    for klass in expressions::IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions::stringconstant_is_not_abstract():
    assert not inspect.isabstract(expressions::StringConstant)


def test_expressions::stringconstant_constructor_exists():
    assert callable(expressions::StringConstant.__init__)


def test_expressions::stringconstant_constructor_args():
    sig = inspect.signature(expressions::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions::stringconstant_has_value():
    assert hasattr(expressions::StringConstant, "value")
    descriptor = None
    for klass in expressions::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions::not_is_not_abstract():
    assert not inspect.isabstract(expressions::Not)


def test_expressions::not_constructor_exists():
    assert callable(expressions::Not.__init__)


def test_expressions::not_constructor_args():
    sig = inspect.signature(expressions::Not.__init__)
    params = list(sig.parameters.keys())



def test_expressions::mulordiv_is_not_abstract():
    assert not inspect.isabstract(expressions::MulOrDiv)


def test_expressions::mulordiv_constructor_exists():
    assert callable(expressions::MulOrDiv.__init__)


def test_expressions::mulordiv_constructor_args():
    sig = inspect.signature(expressions::MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expressions::mulordiv_has_op():
    assert hasattr(expressions::MulOrDiv, "op")
    descriptor = None
    for klass in expressions::MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expressions::plus_is_not_abstract():
    assert not inspect.isabstract(expressions::Plus)


def test_expressions::plus_constructor_exists():
    assert callable(expressions::Plus.__init__)


def test_expressions::plus_constructor_args():
    sig = inspect.signature(expressions::Plus.__init__)
    params = list(sig.parameters.keys())



def test_expressions::boolconstant_is_not_abstract():
    assert not inspect.isabstract(expressions::BoolConstant)


def test_expressions::boolconstant_constructor_exists():
    assert callable(expressions::BoolConstant.__init__)


def test_expressions::boolconstant_constructor_args():
    sig = inspect.signature(expressions::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions::boolconstant_has_value():
    assert hasattr(expressions::BoolConstant, "value")
    descriptor = None
    for klass in expressions::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions::or_is_not_abstract():
    assert not inspect.isabstract(expressions::Or)


def test_expressions::or_constructor_exists():
    assert callable(expressions::Or.__init__)


def test_expressions::or_constructor_args():
    sig = inspect.signature(expressions::Or.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_expressions::evalexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::EvalExpression)


def test_expressions::evalexpression_constructor_exists():
    assert callable(expressions::EvalExpression.__init__)


def test_expressions::evalexpression_constructor_args():
    sig = inspect.signature(expressions::EvalExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::variable_is_not_abstract():
    assert not inspect.isabstract(expressions::Variable)


def test_expressions::variable_constructor_exists():
    assert callable(expressions::Variable.__init__)


def test_expressions::variable_constructor_args():
    sig = inspect.signature(expressions::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_expressions::variable_has_name():
    assert hasattr(expressions::Variable, "name")
    descriptor = None
    for klass in expressions::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expressions::expression_is_not_abstract():
    assert not inspect.isabstract(expressions::Expression)


def test_expressions::expression_constructor_exists():
    assert callable(expressions::Expression.__init__)


def test_expressions::expression_constructor_args():
    sig = inspect.signature(expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::abstractelement_is_not_abstract():
    assert not inspect.isabstract(expressions::AbstractElement)


def test_expressions::abstractelement_constructor_exists():
    assert callable(expressions::AbstractElement.__init__)


def test_expressions::abstractelement_constructor_args():
    sig = inspect.signature(expressions::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_expressions::expressionsmodel_is_not_abstract():
    assert not inspect.isabstract(expressions::ExpressionsModel)


def test_expressions::expressionsmodel_constructor_exists():
    assert callable(expressions::ExpressionsModel.__init__)


def test_expressions::expressionsmodel_constructor_args():
    sig = inspect.signature(expressions::ExpressionsModel.__init__)
    params = list(sig.parameters.keys())



def test_expressions::comparison_is_not_abstract():
    assert not inspect.isabstract(expressions::Comparison)


def test_expressions::comparison_constructor_exists():
    assert callable(expressions::Comparison.__init__)


def test_expressions::comparison_constructor_args():
    sig = inspect.signature(expressions::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expressions::comparison_has_op():
    assert hasattr(expressions::Comparison, "op")
    descriptor = None
    for klass in expressions::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expressions::equality_is_not_abstract():
    assert not inspect.isabstract(expressions::Equality)


def test_expressions::equality_constructor_exists():
    assert callable(expressions::Equality.__init__)


def test_expressions::equality_constructor_args():
    sig = inspect.signature(expressions::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expressions::equality_has_op():
    assert hasattr(expressions::Equality, "op")
    descriptor = None
    for klass in expressions::Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expressions::and_is_not_abstract():
    assert not inspect.isabstract(expressions::And)


def test_expressions::and_constructor_exists():
    assert callable(expressions::And.__init__)


def test_expressions::and_constructor_args():
    sig = inspect.signature(expressions::And.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
expressions::VariableRef_strategy = st.builds(
    expressions::VariableRef,
)
expressions::Minus_strategy = st.builds(
    expressions::Minus,
)
expressions::IntConstant_strategy = st.builds(
    expressions::IntConstant,
    value=
        st.integers()
)
expressions::StringConstant_strategy = st.builds(
    expressions::StringConstant,
    value=
        safe_text
)
expressions::Not_strategy = st.builds(
    expressions::Not,
)
expressions::MulOrDiv_strategy = st.builds(
    expressions::MulOrDiv,
    op=
        safe_text
)
expressions::Plus_strategy = st.builds(
    expressions::Plus,
)
expressions::BoolConstant_strategy = st.builds(
    expressions::BoolConstant,
    value=
        safe_text
)
expressions::Or_strategy = st.builds(
    expressions::Or,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
expressions::EvalExpression_strategy = st.builds(
    expressions::EvalExpression,
)
expressions::Variable_strategy = st.builds(
    expressions::Variable,
    name=
        safe_text
)
expressions::Expression_strategy = st.builds(
    expressions::Expression,
)
expressions::AbstractElement_strategy = st.builds(
    expressions::AbstractElement,
)
expressions::ExpressionsModel_strategy = st.builds(
    expressions::ExpressionsModel,
)
expressions::Comparison_strategy = st.builds(
    expressions::Comparison,
    op=
        safe_text
)
expressions::Equality_strategy = st.builds(
    expressions::Equality,
    op=
        safe_text
)
expressions::And_strategy = st.builds(
    expressions::And,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expressions::VariableRef_strategy)
@settings(max_examples=50)
def test_expressions::variableref_instantiation(instance):
    assert isinstance(instance, expressions::VariableRef)

@given(instance=expressions::Minus_strategy)
@settings(max_examples=50)
def test_expressions::minus_instantiation(instance):
    assert isinstance(instance, expressions::Minus)

@given(instance=expressions::IntConstant_strategy)
@settings(max_examples=50)
def test_expressions::intconstant_instantiation(instance):
    assert isinstance(instance, expressions::IntConstant)

@given(instance=expressions::IntConstant_strategy)
def test_expressions::intconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=expressions::IntConstant_strategy)
def test_expressions::intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions::StringConstant_strategy)
@settings(max_examples=50)
def test_expressions::stringconstant_instantiation(instance):
    assert isinstance(instance, expressions::StringConstant)

@given(instance=expressions::StringConstant_strategy)
def test_expressions::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expressions::StringConstant_strategy)
def test_expressions::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions::Not_strategy)
@settings(max_examples=50)
def test_expressions::not_instantiation(instance):
    assert isinstance(instance, expressions::Not)

@given(instance=expressions::MulOrDiv_strategy)
@settings(max_examples=50)
def test_expressions::mulordiv_instantiation(instance):
    assert isinstance(instance, expressions::MulOrDiv)

@given(instance=expressions::MulOrDiv_strategy)
def test_expressions::mulordiv_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expressions::MulOrDiv_strategy)
def test_expressions::mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expressions::Plus_strategy)
@settings(max_examples=50)
def test_expressions::plus_instantiation(instance):
    assert isinstance(instance, expressions::Plus)

@given(instance=expressions::BoolConstant_strategy)
@settings(max_examples=50)
def test_expressions::boolconstant_instantiation(instance):
    assert isinstance(instance, expressions::BoolConstant)

@given(instance=expressions::BoolConstant_strategy)
def test_expressions::boolconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expressions::BoolConstant_strategy)
def test_expressions::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions::Or_strategy)
@settings(max_examples=50)
def test_expressions::or_instantiation(instance):
    assert isinstance(instance, expressions::Or)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=expressions::EvalExpression_strategy)
@settings(max_examples=50)
def test_expressions::evalexpression_instantiation(instance):
    assert isinstance(instance, expressions::EvalExpression)

@given(instance=expressions::Variable_strategy)
@settings(max_examples=50)
def test_expressions::variable_instantiation(instance):
    assert isinstance(instance, expressions::Variable)

@given(instance=expressions::Variable_strategy)
def test_expressions::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=expressions::Variable_strategy)
def test_expressions::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=expressions::Expression_strategy)
@settings(max_examples=50)
def test_expressions::expression_instantiation(instance):
    assert isinstance(instance, expressions::Expression)

@given(instance=expressions::AbstractElement_strategy)
@settings(max_examples=50)
def test_expressions::abstractelement_instantiation(instance):
    assert isinstance(instance, expressions::AbstractElement)

@given(instance=expressions::ExpressionsModel_strategy)
@settings(max_examples=50)
def test_expressions::expressionsmodel_instantiation(instance):
    assert isinstance(instance, expressions::ExpressionsModel)

@given(instance=expressions::Comparison_strategy)
@settings(max_examples=50)
def test_expressions::comparison_instantiation(instance):
    assert isinstance(instance, expressions::Comparison)

@given(instance=expressions::Comparison_strategy)
def test_expressions::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expressions::Comparison_strategy)
def test_expressions::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expressions::Equality_strategy)
@settings(max_examples=50)
def test_expressions::equality_instantiation(instance):
    assert isinstance(instance, expressions::Equality)

@given(instance=expressions::Equality_strategy)
def test_expressions::equality_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expressions::Equality_strategy)
def test_expressions::equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expressions::And_strategy)
@settings(max_examples=50)
def test_expressions::and_instantiation(instance):
    assert isinstance(instance, expressions::And)

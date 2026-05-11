import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    expressions::Model,
    UnaryOperator,
    expressions::All,
    expressions::Any,
    expressions::Number,
    expressions::Neg,
    BinaryOperator,
    expressions::And,
    expressions::Or,
    expressions::Implies,
    Expression,
    expressions::UnaryOperator,
    expressions::Feature,
    expressions::BinaryOperator,
    expressions::Expression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_expressions::all_is_not_abstract():
    assert not inspect.isabstract(expressions::All)


def test_expressions::all_constructor_exists():
    assert callable(expressions::All.__init__)


def test_expressions::all_constructor_args():
    sig = inspect.signature(expressions::All.__init__)
    params = list(sig.parameters.keys())



def test_expressions::any_is_not_abstract():
    assert not inspect.isabstract(expressions::Any)


def test_expressions::any_constructor_exists():
    assert callable(expressions::Any.__init__)


def test_expressions::any_constructor_args():
    sig = inspect.signature(expressions::Any.__init__)
    params = list(sig.parameters.keys())



def test_expressions::number_is_not_abstract():
    assert not inspect.isabstract(expressions::Number)


def test_expressions::number_constructor_exists():
    assert callable(expressions::Number.__init__)


def test_expressions::number_constructor_args():
    sig = inspect.signature(expressions::Number.__init__)
    params = list(sig.parameters.keys())



def test_expressions::neg_is_not_abstract():
    assert not inspect.isabstract(expressions::Neg)


def test_expressions::neg_constructor_exists():
    assert callable(expressions::Neg.__init__)


def test_expressions::neg_constructor_args():
    sig = inspect.signature(expressions::Neg.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_expressions::and_is_not_abstract():
    assert not inspect.isabstract(expressions::And)


def test_expressions::and_constructor_exists():
    assert callable(expressions::And.__init__)


def test_expressions::and_constructor_args():
    sig = inspect.signature(expressions::And.__init__)
    params = list(sig.parameters.keys())



def test_expressions::or_is_not_abstract():
    assert not inspect.isabstract(expressions::Or)


def test_expressions::or_constructor_exists():
    assert callable(expressions::Or.__init__)


def test_expressions::or_constructor_args():
    sig = inspect.signature(expressions::Or.__init__)
    params = list(sig.parameters.keys())



def test_expressions::implies_is_not_abstract():
    assert not inspect.isabstract(expressions::Implies)


def test_expressions::implies_constructor_exists():
    assert callable(expressions::Implies.__init__)


def test_expressions::implies_constructor_args():
    sig = inspect.signature(expressions::Implies.__init__)
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



def test_expressions::feature_is_not_abstract():
    assert not inspect.isabstract(expressions::Feature)


def test_expressions::feature_constructor_exists():
    assert callable(expressions::Feature.__init__)


def test_expressions::feature_constructor_args():
    sig = inspect.signature(expressions::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_expressions::feature_has_name():
    assert hasattr(expressions::Feature, "name")
    descriptor = None
    for klass in expressions::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expressions::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(expressions::BinaryOperator)


def test_expressions::binaryoperator_constructor_exists():
    assert callable(expressions::BinaryOperator.__init__)


def test_expressions::binaryoperator_constructor_args():
    sig = inspect.signature(expressions::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_expressions::expression_is_not_abstract():
    assert not inspect.isabstract(expressions::Expression)


def test_expressions::expression_constructor_exists():
    assert callable(expressions::Expression.__init__)


def test_expressions::expression_constructor_args():
    sig = inspect.signature(expressions::Expression.__init__)
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
expressions::Model_strategy = st.builds(
    expressions::Model,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
expressions::All_strategy = st.builds(
    expressions::All,
)
expressions::Any_strategy = st.builds(
    expressions::Any,
)
expressions::Number_strategy = st.builds(
    expressions::Number,
)
expressions::Neg_strategy = st.builds(
    expressions::Neg,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
expressions::And_strategy = st.builds(
    expressions::And,
)
expressions::Or_strategy = st.builds(
    expressions::Or,
)
expressions::Implies_strategy = st.builds(
    expressions::Implies,
)
Expression_strategy = st.builds(
    Expression,
)
expressions::UnaryOperator_strategy = st.builds(
    expressions::UnaryOperator,
)
expressions::Feature_strategy = st.builds(
    expressions::Feature,
    name=
        safe_text
)
expressions::BinaryOperator_strategy = st.builds(
    expressions::BinaryOperator,
)
expressions::Expression_strategy = st.builds(
    expressions::Expression,
)

@given(instance=expressions::Model_strategy)
@settings(max_examples=50)
def test_expressions::model_instantiation(instance):
    assert isinstance(instance, expressions::Model)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=expressions::All_strategy)
@settings(max_examples=50)
def test_expressions::all_instantiation(instance):
    assert isinstance(instance, expressions::All)

@given(instance=expressions::Any_strategy)
@settings(max_examples=50)
def test_expressions::any_instantiation(instance):
    assert isinstance(instance, expressions::Any)

@given(instance=expressions::Number_strategy)
@settings(max_examples=50)
def test_expressions::number_instantiation(instance):
    assert isinstance(instance, expressions::Number)

@given(instance=expressions::Neg_strategy)
@settings(max_examples=50)
def test_expressions::neg_instantiation(instance):
    assert isinstance(instance, expressions::Neg)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=expressions::And_strategy)
@settings(max_examples=50)
def test_expressions::and_instantiation(instance):
    assert isinstance(instance, expressions::And)

@given(instance=expressions::Or_strategy)
@settings(max_examples=50)
def test_expressions::or_instantiation(instance):
    assert isinstance(instance, expressions::Or)

@given(instance=expressions::Implies_strategy)
@settings(max_examples=50)
def test_expressions::implies_instantiation(instance):
    assert isinstance(instance, expressions::Implies)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expressions::UnaryOperator_strategy)
@settings(max_examples=50)
def test_expressions::unaryoperator_instantiation(instance):
    assert isinstance(instance, expressions::UnaryOperator)

@given(instance=expressions::Feature_strategy)
@settings(max_examples=50)
def test_expressions::feature_instantiation(instance):
    assert isinstance(instance, expressions::Feature)

@given(instance=expressions::Feature_strategy)
def test_expressions::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=expressions::Feature_strategy)
def test_expressions::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=expressions::BinaryOperator_strategy)
@settings(max_examples=50)
def test_expressions::binaryoperator_instantiation(instance):
    assert isinstance(instance, expressions::BinaryOperator)

@given(instance=expressions::Expression_strategy)
@settings(max_examples=50)
def test_expressions::expression_instantiation(instance):
    assert isinstance(instance, expressions::Expression)

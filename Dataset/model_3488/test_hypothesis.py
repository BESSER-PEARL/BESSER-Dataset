import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    model::ExistsContextualExpression,
    model::Negation,
    model::PrimaryExpression,
    model::ForAllContextualExpression,
    model::Expression,
    model::Conjunction,
    model::Disjunction,
    model::Implication,
    model::Equation,
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



def test_model::existscontextualexpression_is_not_abstract():
    assert not inspect.isabstract(model::ExistsContextualExpression)


def test_model::existscontextualexpression_constructor_exists():
    assert callable(model::ExistsContextualExpression.__init__)


def test_model::existscontextualexpression_constructor_args():
    sig = inspect.signature(model::ExistsContextualExpression.__init__)
    params = list(sig.parameters.keys())
    assert "contextId" in params, "Missing parameter 'contextId'"

def test_model::existscontextualexpression_has_contextId():
    assert hasattr(model::ExistsContextualExpression, "contextId")
    descriptor = None
    for klass in model::ExistsContextualExpression.__mro__:
        if "contextId" in klass.__dict__:
            descriptor = klass.__dict__["contextId"]
            break
    assert isinstance(descriptor, property)



def test_model::negation_is_not_abstract():
    assert not inspect.isabstract(model::Negation)


def test_model::negation_constructor_exists():
    assert callable(model::Negation.__init__)


def test_model::negation_constructor_args():
    sig = inspect.signature(model::Negation.__init__)
    params = list(sig.parameters.keys())



def test_model::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(model::PrimaryExpression)


def test_model::primaryexpression_constructor_exists():
    assert callable(model::PrimaryExpression.__init__)


def test_model::primaryexpression_constructor_args():
    sig = inspect.signature(model::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "featureId" in params, "Missing parameter 'featureId'"

def test_model::primaryexpression_has_featureId():
    assert hasattr(model::PrimaryExpression, "featureId")
    descriptor = None
    for klass in model::PrimaryExpression.__mro__:
        if "featureId" in klass.__dict__:
            descriptor = klass.__dict__["featureId"]
            break
    assert isinstance(descriptor, property)



def test_model::forallcontextualexpression_is_not_abstract():
    assert not inspect.isabstract(model::ForAllContextualExpression)


def test_model::forallcontextualexpression_constructor_exists():
    assert callable(model::ForAllContextualExpression.__init__)


def test_model::forallcontextualexpression_constructor_args():
    sig = inspect.signature(model::ForAllContextualExpression.__init__)
    params = list(sig.parameters.keys())
    assert "contextId" in params, "Missing parameter 'contextId'"

def test_model::forallcontextualexpression_has_contextId():
    assert hasattr(model::ForAllContextualExpression, "contextId")
    descriptor = None
    for klass in model::ForAllContextualExpression.__mro__:
        if "contextId" in klass.__dict__:
            descriptor = klass.__dict__["contextId"]
            break
    assert isinstance(descriptor, property)



def test_model::expression_is_not_abstract():
    assert not inspect.isabstract(model::Expression)


def test_model::expression_constructor_exists():
    assert callable(model::Expression.__init__)


def test_model::expression_constructor_args():
    sig = inspect.signature(model::Expression.__init__)
    params = list(sig.parameters.keys())



def test_model::conjunction_is_not_abstract():
    assert not inspect.isabstract(model::Conjunction)


def test_model::conjunction_constructor_exists():
    assert callable(model::Conjunction.__init__)


def test_model::conjunction_constructor_args():
    sig = inspect.signature(model::Conjunction.__init__)
    params = list(sig.parameters.keys())



def test_model::disjunction_is_not_abstract():
    assert not inspect.isabstract(model::Disjunction)


def test_model::disjunction_constructor_exists():
    assert callable(model::Disjunction.__init__)


def test_model::disjunction_constructor_args():
    sig = inspect.signature(model::Disjunction.__init__)
    params = list(sig.parameters.keys())



def test_model::implication_is_not_abstract():
    assert not inspect.isabstract(model::Implication)


def test_model::implication_constructor_exists():
    assert callable(model::Implication.__init__)


def test_model::implication_constructor_args():
    sig = inspect.signature(model::Implication.__init__)
    params = list(sig.parameters.keys())



def test_model::equation_is_not_abstract():
    assert not inspect.isabstract(model::Equation)


def test_model::equation_constructor_exists():
    assert callable(model::Equation.__init__)


def test_model::equation_constructor_args():
    sig = inspect.signature(model::Equation.__init__)
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
model::ExistsContextualExpression_strategy = st.builds(
    model::ExistsContextualExpression,
    contextId=
        safe_text
)
model::Negation_strategy = st.builds(
    model::Negation,
)
model::PrimaryExpression_strategy = st.builds(
    model::PrimaryExpression,
    featureId=
        safe_text
)
model::ForAllContextualExpression_strategy = st.builds(
    model::ForAllContextualExpression,
    contextId=
        safe_text
)
model::Expression_strategy = st.builds(
    model::Expression,
)
model::Conjunction_strategy = st.builds(
    model::Conjunction,
)
model::Disjunction_strategy = st.builds(
    model::Disjunction,
)
model::Implication_strategy = st.builds(
    model::Implication,
)
model::Equation_strategy = st.builds(
    model::Equation,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=model::ExistsContextualExpression_strategy)
@settings(max_examples=50)
def test_model::existscontextualexpression_instantiation(instance):
    assert isinstance(instance, model::ExistsContextualExpression)

@given(instance=model::ExistsContextualExpression_strategy)
def test_model::existscontextualexpression_contextId_type(instance):
    assert isinstance(instance.contextId, str)


@given(instance=model::ExistsContextualExpression_strategy)
def test_model::existscontextualexpression_contextId_setter(instance):
    original = instance.contextId
    instance.contextId = original
    assert instance.contextId == original

@given(instance=model::Negation_strategy)
@settings(max_examples=50)
def test_model::negation_instantiation(instance):
    assert isinstance(instance, model::Negation)

@given(instance=model::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_model::primaryexpression_instantiation(instance):
    assert isinstance(instance, model::PrimaryExpression)

@given(instance=model::PrimaryExpression_strategy)
def test_model::primaryexpression_featureId_type(instance):
    assert isinstance(instance.featureId, str)


@given(instance=model::PrimaryExpression_strategy)
def test_model::primaryexpression_featureId_setter(instance):
    original = instance.featureId
    instance.featureId = original
    assert instance.featureId == original

@given(instance=model::ForAllContextualExpression_strategy)
@settings(max_examples=50)
def test_model::forallcontextualexpression_instantiation(instance):
    assert isinstance(instance, model::ForAllContextualExpression)

@given(instance=model::ForAllContextualExpression_strategy)
def test_model::forallcontextualexpression_contextId_type(instance):
    assert isinstance(instance.contextId, str)


@given(instance=model::ForAllContextualExpression_strategy)
def test_model::forallcontextualexpression_contextId_setter(instance):
    original = instance.contextId
    instance.contextId = original
    assert instance.contextId == original

@given(instance=model::Expression_strategy)
@settings(max_examples=50)
def test_model::expression_instantiation(instance):
    assert isinstance(instance, model::Expression)

@given(instance=model::Conjunction_strategy)
@settings(max_examples=50)
def test_model::conjunction_instantiation(instance):
    assert isinstance(instance, model::Conjunction)

@given(instance=model::Disjunction_strategy)
@settings(max_examples=50)
def test_model::disjunction_instantiation(instance):
    assert isinstance(instance, model::Disjunction)

@given(instance=model::Implication_strategy)
@settings(max_examples=50)
def test_model::implication_instantiation(instance):
    assert isinstance(instance, model::Implication)

@given(instance=model::Equation_strategy)
@settings(max_examples=50)
def test_model::equation_instantiation(instance):
    assert isinstance(instance, model::Equation)

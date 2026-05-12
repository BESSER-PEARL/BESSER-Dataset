import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    model_PrimaryExpression,
    model_ExistsContextualExpression,
    model_Negation,
    model_ForAllContextualExpression,
    model_Expression,
    model_Equation,
    model_Conjunction,
    model_Disjunction,
    model_Implication,
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



def test_model_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(model_PrimaryExpression)


def test_model_primaryexpression_constructor_exists():
    assert callable(model_PrimaryExpression.__init__)


def test_model_primaryexpression_constructor_args():
    sig = inspect.signature(model_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "featureId" in params, "Missing parameter 'featureId'"

def test_model_primaryexpression_has_featureId():
    assert hasattr(model_PrimaryExpression, "featureId")
    descriptor = None
    for klass in model_PrimaryExpression.__mro__:
        if "featureId" in klass.__dict__:
            descriptor = klass.__dict__["featureId"]
            break
    assert isinstance(descriptor, property)



def test_model_existscontextualexpression_is_not_abstract():
    assert not inspect.isabstract(model_ExistsContextualExpression)


def test_model_existscontextualexpression_constructor_exists():
    assert callable(model_ExistsContextualExpression.__init__)


def test_model_existscontextualexpression_constructor_args():
    sig = inspect.signature(model_ExistsContextualExpression.__init__)
    params = list(sig.parameters.keys())
    assert "contextId" in params, "Missing parameter 'contextId'"

def test_model_existscontextualexpression_has_contextId():
    assert hasattr(model_ExistsContextualExpression, "contextId")
    descriptor = None
    for klass in model_ExistsContextualExpression.__mro__:
        if "contextId" in klass.__dict__:
            descriptor = klass.__dict__["contextId"]
            break
    assert isinstance(descriptor, property)



def test_model_negation_is_not_abstract():
    assert not inspect.isabstract(model_Negation)


def test_model_negation_constructor_exists():
    assert callable(model_Negation.__init__)


def test_model_negation_constructor_args():
    sig = inspect.signature(model_Negation.__init__)
    params = list(sig.parameters.keys())



def test_model_forallcontextualexpression_is_not_abstract():
    assert not inspect.isabstract(model_ForAllContextualExpression)


def test_model_forallcontextualexpression_constructor_exists():
    assert callable(model_ForAllContextualExpression.__init__)


def test_model_forallcontextualexpression_constructor_args():
    sig = inspect.signature(model_ForAllContextualExpression.__init__)
    params = list(sig.parameters.keys())
    assert "contextId" in params, "Missing parameter 'contextId'"

def test_model_forallcontextualexpression_has_contextId():
    assert hasattr(model_ForAllContextualExpression, "contextId")
    descriptor = None
    for klass in model_ForAllContextualExpression.__mro__:
        if "contextId" in klass.__dict__:
            descriptor = klass.__dict__["contextId"]
            break
    assert isinstance(descriptor, property)



def test_model_expression_is_not_abstract():
    assert not inspect.isabstract(model_Expression)


def test_model_expression_constructor_exists():
    assert callable(model_Expression.__init__)


def test_model_expression_constructor_args():
    sig = inspect.signature(model_Expression.__init__)
    params = list(sig.parameters.keys())



def test_model_equation_is_not_abstract():
    assert not inspect.isabstract(model_Equation)


def test_model_equation_constructor_exists():
    assert callable(model_Equation.__init__)


def test_model_equation_constructor_args():
    sig = inspect.signature(model_Equation.__init__)
    params = list(sig.parameters.keys())



def test_model_conjunction_is_not_abstract():
    assert not inspect.isabstract(model_Conjunction)


def test_model_conjunction_constructor_exists():
    assert callable(model_Conjunction.__init__)


def test_model_conjunction_constructor_args():
    sig = inspect.signature(model_Conjunction.__init__)
    params = list(sig.parameters.keys())



def test_model_disjunction_is_not_abstract():
    assert not inspect.isabstract(model_Disjunction)


def test_model_disjunction_constructor_exists():
    assert callable(model_Disjunction.__init__)


def test_model_disjunction_constructor_args():
    sig = inspect.signature(model_Disjunction.__init__)
    params = list(sig.parameters.keys())



def test_model_implication_is_not_abstract():
    assert not inspect.isabstract(model_Implication)


def test_model_implication_constructor_exists():
    assert callable(model_Implication.__init__)


def test_model_implication_constructor_args():
    sig = inspect.signature(model_Implication.__init__)
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
model_PrimaryExpression_strategy = st.builds(
    model_PrimaryExpression,
    featureId=
        safe_text
)
model_ExistsContextualExpression_strategy = st.builds(
    model_ExistsContextualExpression,
    contextId=
        safe_text
)
model_Negation_strategy = st.builds(
    model_Negation,
)
model_ForAllContextualExpression_strategy = st.builds(
    model_ForAllContextualExpression,
    contextId=
        safe_text
)
model_Expression_strategy = st.builds(
    model_Expression,
)
model_Equation_strategy = st.builds(
    model_Equation,
)
model_Conjunction_strategy = st.builds(
    model_Conjunction,
)
model_Disjunction_strategy = st.builds(
    model_Disjunction,
)
model_Implication_strategy = st.builds(
    model_Implication,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=model_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_model_primaryexpression_instantiation(instance):
    assert isinstance(instance, model_PrimaryExpression)



@given(instance=model_PrimaryExpression_strategy)
def test_model_primaryexpression_featureId_setter(instance):
    original = instance.featureId
    instance.featureId = original
    assert instance.featureId == original

@given(instance=model_ExistsContextualExpression_strategy)
@settings(max_examples=50)
def test_model_existscontextualexpression_instantiation(instance):
    assert isinstance(instance, model_ExistsContextualExpression)



@given(instance=model_ExistsContextualExpression_strategy)
def test_model_existscontextualexpression_contextId_setter(instance):
    original = instance.contextId
    instance.contextId = original
    assert instance.contextId == original

@given(instance=model_Negation_strategy)
@settings(max_examples=50)
def test_model_negation_instantiation(instance):
    assert isinstance(instance, model_Negation)

@given(instance=model_ForAllContextualExpression_strategy)
@settings(max_examples=50)
def test_model_forallcontextualexpression_instantiation(instance):
    assert isinstance(instance, model_ForAllContextualExpression)



@given(instance=model_ForAllContextualExpression_strategy)
def test_model_forallcontextualexpression_contextId_setter(instance):
    original = instance.contextId
    instance.contextId = original
    assert instance.contextId == original

@given(instance=model_Expression_strategy)
@settings(max_examples=50)
def test_model_expression_instantiation(instance):
    assert isinstance(instance, model_Expression)

@given(instance=model_Equation_strategy)
@settings(max_examples=50)
def test_model_equation_instantiation(instance):
    assert isinstance(instance, model_Equation)

@given(instance=model_Conjunction_strategy)
@settings(max_examples=50)
def test_model_conjunction_instantiation(instance):
    assert isinstance(instance, model_Conjunction)

@given(instance=model_Disjunction_strategy)
@settings(max_examples=50)
def test_model_disjunction_instantiation(instance):
    assert isinstance(instance, model_Disjunction)

@given(instance=model_Implication_strategy)
@settings(max_examples=50)
def test_model_implication_instantiation(instance):
    assert isinstance(instance, model_Implication)

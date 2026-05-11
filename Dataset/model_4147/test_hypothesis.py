import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractDefinition,
    rankPL::Definition,
    rankPL::AbstractDefinition,
    rankPL::Model,
    Expression,
    rankPL::Multi,
    rankPL::FunctionCall,
    rankPL::Minus,
    rankPL::Div,
    rankPL::NumberLiteral,
    rankPL::Plus,
    rankPL::DeclaredParameter,
    rankPL::Expression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractdefinition_is_not_abstract():
    assert not inspect.isabstract(AbstractDefinition)


def test_abstractdefinition_constructor_exists():
    assert callable(AbstractDefinition.__init__)


def test_abstractdefinition_constructor_args():
    sig = inspect.signature(AbstractDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rankpl::definition_is_not_abstract():
    assert not inspect.isabstract(rankPL::Definition)


def test_rankpl::definition_constructor_exists():
    assert callable(rankPL::Definition.__init__)


def test_rankpl::definition_constructor_args():
    sig = inspect.signature(rankPL::Definition.__init__)
    params = list(sig.parameters.keys())



def test_rankpl::abstractdefinition_is_not_abstract():
    assert not inspect.isabstract(rankPL::AbstractDefinition)


def test_rankpl::abstractdefinition_constructor_exists():
    assert callable(rankPL::AbstractDefinition.__init__)


def test_rankpl::abstractdefinition_constructor_args():
    sig = inspect.signature(rankPL::AbstractDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rankpl::abstractdefinition_has_name():
    assert hasattr(rankPL::AbstractDefinition, "name")
    descriptor = None
    for klass in rankPL::AbstractDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rankpl::model_is_not_abstract():
    assert not inspect.isabstract(rankPL::Model)


def test_rankpl::model_constructor_exists():
    assert callable(rankPL::Model.__init__)


def test_rankpl::model_constructor_args():
    sig = inspect.signature(rankPL::Model.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_rankpl::multi_is_not_abstract():
    assert not inspect.isabstract(rankPL::Multi)


def test_rankpl::multi_constructor_exists():
    assert callable(rankPL::Multi.__init__)


def test_rankpl::multi_constructor_args():
    sig = inspect.signature(rankPL::Multi.__init__)
    params = list(sig.parameters.keys())



def test_rankpl::functioncall_is_not_abstract():
    assert not inspect.isabstract(rankPL::FunctionCall)


def test_rankpl::functioncall_constructor_exists():
    assert callable(rankPL::FunctionCall.__init__)


def test_rankpl::functioncall_constructor_args():
    sig = inspect.signature(rankPL::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_rankpl::minus_is_not_abstract():
    assert not inspect.isabstract(rankPL::Minus)


def test_rankpl::minus_constructor_exists():
    assert callable(rankPL::Minus.__init__)


def test_rankpl::minus_constructor_args():
    sig = inspect.signature(rankPL::Minus.__init__)
    params = list(sig.parameters.keys())



def test_rankpl::div_is_not_abstract():
    assert not inspect.isabstract(rankPL::Div)


def test_rankpl::div_constructor_exists():
    assert callable(rankPL::Div.__init__)


def test_rankpl::div_constructor_args():
    sig = inspect.signature(rankPL::Div.__init__)
    params = list(sig.parameters.keys())



def test_rankpl::numberliteral_is_not_abstract():
    assert not inspect.isabstract(rankPL::NumberLiteral)


def test_rankpl::numberliteral_constructor_exists():
    assert callable(rankPL::NumberLiteral.__init__)


def test_rankpl::numberliteral_constructor_args():
    sig = inspect.signature(rankPL::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rankpl::numberliteral_has_value():
    assert hasattr(rankPL::NumberLiteral, "value")
    descriptor = None
    for klass in rankPL::NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rankpl::plus_is_not_abstract():
    assert not inspect.isabstract(rankPL::Plus)


def test_rankpl::plus_constructor_exists():
    assert callable(rankPL::Plus.__init__)


def test_rankpl::plus_constructor_args():
    sig = inspect.signature(rankPL::Plus.__init__)
    params = list(sig.parameters.keys())



def test_rankpl::declaredparameter_is_not_abstract():
    assert not inspect.isabstract(rankPL::DeclaredParameter)


def test_rankpl::declaredparameter_constructor_exists():
    assert callable(rankPL::DeclaredParameter.__init__)


def test_rankpl::declaredparameter_constructor_args():
    sig = inspect.signature(rankPL::DeclaredParameter.__init__)
    params = list(sig.parameters.keys())



def test_rankpl::expression_is_not_abstract():
    assert not inspect.isabstract(rankPL::Expression)


def test_rankpl::expression_constructor_exists():
    assert callable(rankPL::Expression.__init__)


def test_rankpl::expression_constructor_args():
    sig = inspect.signature(rankPL::Expression.__init__)
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
AbstractDefinition_strategy = st.builds(
    AbstractDefinition,
)
rankPL::Definition_strategy = st.builds(
    rankPL::Definition,
)
rankPL::AbstractDefinition_strategy = st.builds(
    rankPL::AbstractDefinition,
    name=
        safe_text
)
rankPL::Model_strategy = st.builds(
    rankPL::Model,
)
Expression_strategy = st.builds(
    Expression,
)
rankPL::Multi_strategy = st.builds(
    rankPL::Multi,
)
rankPL::FunctionCall_strategy = st.builds(
    rankPL::FunctionCall,
)
rankPL::Minus_strategy = st.builds(
    rankPL::Minus,
)
rankPL::Div_strategy = st.builds(
    rankPL::Div,
)
rankPL::NumberLiteral_strategy = st.builds(
    rankPL::NumberLiteral,
    value=
        safe_text
)
rankPL::Plus_strategy = st.builds(
    rankPL::Plus,
)
rankPL::DeclaredParameter_strategy = st.builds(
    rankPL::DeclaredParameter,
)
rankPL::Expression_strategy = st.builds(
    rankPL::Expression,
)

@given(instance=AbstractDefinition_strategy)
@settings(max_examples=50)
def test_abstractdefinition_instantiation(instance):
    assert isinstance(instance, AbstractDefinition)

@given(instance=rankPL::Definition_strategy)
@settings(max_examples=50)
def test_rankpl::definition_instantiation(instance):
    assert isinstance(instance, rankPL::Definition)

@given(instance=rankPL::AbstractDefinition_strategy)
@settings(max_examples=50)
def test_rankpl::abstractdefinition_instantiation(instance):
    assert isinstance(instance, rankPL::AbstractDefinition)

@given(instance=rankPL::AbstractDefinition_strategy)
def test_rankpl::abstractdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rankPL::AbstractDefinition_strategy)
def test_rankpl::abstractdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rankPL::Model_strategy)
@settings(max_examples=50)
def test_rankpl::model_instantiation(instance):
    assert isinstance(instance, rankPL::Model)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=rankPL::Multi_strategy)
@settings(max_examples=50)
def test_rankpl::multi_instantiation(instance):
    assert isinstance(instance, rankPL::Multi)

@given(instance=rankPL::FunctionCall_strategy)
@settings(max_examples=50)
def test_rankpl::functioncall_instantiation(instance):
    assert isinstance(instance, rankPL::FunctionCall)

@given(instance=rankPL::Minus_strategy)
@settings(max_examples=50)
def test_rankpl::minus_instantiation(instance):
    assert isinstance(instance, rankPL::Minus)

@given(instance=rankPL::Div_strategy)
@settings(max_examples=50)
def test_rankpl::div_instantiation(instance):
    assert isinstance(instance, rankPL::Div)

@given(instance=rankPL::NumberLiteral_strategy)
@settings(max_examples=50)
def test_rankpl::numberliteral_instantiation(instance):
    assert isinstance(instance, rankPL::NumberLiteral)

@given(instance=rankPL::NumberLiteral_strategy)
def test_rankpl::numberliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=rankPL::NumberLiteral_strategy)
def test_rankpl::numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rankPL::Plus_strategy)
@settings(max_examples=50)
def test_rankpl::plus_instantiation(instance):
    assert isinstance(instance, rankPL::Plus)

@given(instance=rankPL::DeclaredParameter_strategy)
@settings(max_examples=50)
def test_rankpl::declaredparameter_instantiation(instance):
    assert isinstance(instance, rankPL::DeclaredParameter)

@given(instance=rankPL::Expression_strategy)
@settings(max_examples=50)
def test_rankpl::expression_instantiation(instance):
    assert isinstance(instance, rankPL::Expression)

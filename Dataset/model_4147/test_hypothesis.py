import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    rankPL_NumberLiteral,
    rankPL_Minus,
    rankPL_Div,
    rankPL_FunctionCall,
    rankPL_Multi,
    rankPL_Plus,
    rankPL_Expression,
    AbstractDefinition,
    rankPL_DeclaredParameter,
    rankPL_Definition,
    rankPL_AbstractDefinition,
    rankPL_Model,
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



def test_rankpl_numberliteral_is_not_abstract():
    assert not inspect.isabstract(rankPL_NumberLiteral)


def test_rankpl_numberliteral_constructor_exists():
    assert callable(rankPL_NumberLiteral.__init__)


def test_rankpl_numberliteral_constructor_args():
    sig = inspect.signature(rankPL_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rankpl_numberliteral_has_value():
    assert hasattr(rankPL_NumberLiteral, "value")
    descriptor = None
    for klass in rankPL_NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rankpl_minus_is_not_abstract():
    assert not inspect.isabstract(rankPL_Minus)


def test_rankpl_minus_constructor_exists():
    assert callable(rankPL_Minus.__init__)


def test_rankpl_minus_constructor_args():
    sig = inspect.signature(rankPL_Minus.__init__)
    params = list(sig.parameters.keys())



def test_rankpl_div_is_not_abstract():
    assert not inspect.isabstract(rankPL_Div)


def test_rankpl_div_constructor_exists():
    assert callable(rankPL_Div.__init__)


def test_rankpl_div_constructor_args():
    sig = inspect.signature(rankPL_Div.__init__)
    params = list(sig.parameters.keys())



def test_rankpl_functioncall_is_not_abstract():
    assert not inspect.isabstract(rankPL_FunctionCall)


def test_rankpl_functioncall_constructor_exists():
    assert callable(rankPL_FunctionCall.__init__)


def test_rankpl_functioncall_constructor_args():
    sig = inspect.signature(rankPL_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_rankpl_multi_is_not_abstract():
    assert not inspect.isabstract(rankPL_Multi)


def test_rankpl_multi_constructor_exists():
    assert callable(rankPL_Multi.__init__)


def test_rankpl_multi_constructor_args():
    sig = inspect.signature(rankPL_Multi.__init__)
    params = list(sig.parameters.keys())



def test_rankpl_plus_is_not_abstract():
    assert not inspect.isabstract(rankPL_Plus)


def test_rankpl_plus_constructor_exists():
    assert callable(rankPL_Plus.__init__)


def test_rankpl_plus_constructor_args():
    sig = inspect.signature(rankPL_Plus.__init__)
    params = list(sig.parameters.keys())



def test_rankpl_expression_is_not_abstract():
    assert not inspect.isabstract(rankPL_Expression)


def test_rankpl_expression_constructor_exists():
    assert callable(rankPL_Expression.__init__)


def test_rankpl_expression_constructor_args():
    sig = inspect.signature(rankPL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_abstractdefinition_is_not_abstract():
    assert not inspect.isabstract(AbstractDefinition)


def test_abstractdefinition_constructor_exists():
    assert callable(AbstractDefinition.__init__)


def test_abstractdefinition_constructor_args():
    sig = inspect.signature(AbstractDefinition.__init__)
    params = list(sig.parameters.keys())



def test_rankpl_declaredparameter_is_not_abstract():
    assert not inspect.isabstract(rankPL_DeclaredParameter)


def test_rankpl_declaredparameter_constructor_exists():
    assert callable(rankPL_DeclaredParameter.__init__)


def test_rankpl_declaredparameter_constructor_args():
    sig = inspect.signature(rankPL_DeclaredParameter.__init__)
    params = list(sig.parameters.keys())



def test_rankpl_definition_is_not_abstract():
    assert not inspect.isabstract(rankPL_Definition)


def test_rankpl_definition_constructor_exists():
    assert callable(rankPL_Definition.__init__)


def test_rankpl_definition_constructor_args():
    sig = inspect.signature(rankPL_Definition.__init__)
    params = list(sig.parameters.keys())



def test_rankpl_abstractdefinition_is_not_abstract():
    assert not inspect.isabstract(rankPL_AbstractDefinition)


def test_rankpl_abstractdefinition_constructor_exists():
    assert callable(rankPL_AbstractDefinition.__init__)


def test_rankpl_abstractdefinition_constructor_args():
    sig = inspect.signature(rankPL_AbstractDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rankpl_abstractdefinition_has_name():
    assert hasattr(rankPL_AbstractDefinition, "name")
    descriptor = None
    for klass in rankPL_AbstractDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rankpl_model_is_not_abstract():
    assert not inspect.isabstract(rankPL_Model)


def test_rankpl_model_constructor_exists():
    assert callable(rankPL_Model.__init__)


def test_rankpl_model_constructor_args():
    sig = inspect.signature(rankPL_Model.__init__)
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
rankPL_NumberLiteral_strategy = st.builds(
    rankPL_NumberLiteral,
    value=
        safe_text
)
rankPL_Minus_strategy = st.builds(
    rankPL_Minus,
)
rankPL_Div_strategy = st.builds(
    rankPL_Div,
)
rankPL_FunctionCall_strategy = st.builds(
    rankPL_FunctionCall,
)
rankPL_Multi_strategy = st.builds(
    rankPL_Multi,
)
rankPL_Plus_strategy = st.builds(
    rankPL_Plus,
)
rankPL_Expression_strategy = st.builds(
    rankPL_Expression,
)
AbstractDefinition_strategy = st.builds(
    AbstractDefinition,
)
rankPL_DeclaredParameter_strategy = st.builds(
    rankPL_DeclaredParameter,
)
rankPL_Definition_strategy = st.builds(
    rankPL_Definition,
)
rankPL_AbstractDefinition_strategy = st.builds(
    rankPL_AbstractDefinition,
    name=
        safe_text
)
rankPL_Model_strategy = st.builds(
    rankPL_Model,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=rankPL_NumberLiteral_strategy)
@settings(max_examples=50)
def test_rankpl_numberliteral_instantiation(instance):
    assert isinstance(instance, rankPL_NumberLiteral)



@given(instance=rankPL_NumberLiteral_strategy)
def test_rankpl_numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rankPL_Minus_strategy)
@settings(max_examples=50)
def test_rankpl_minus_instantiation(instance):
    assert isinstance(instance, rankPL_Minus)

@given(instance=rankPL_Div_strategy)
@settings(max_examples=50)
def test_rankpl_div_instantiation(instance):
    assert isinstance(instance, rankPL_Div)

@given(instance=rankPL_FunctionCall_strategy)
@settings(max_examples=50)
def test_rankpl_functioncall_instantiation(instance):
    assert isinstance(instance, rankPL_FunctionCall)

@given(instance=rankPL_Multi_strategy)
@settings(max_examples=50)
def test_rankpl_multi_instantiation(instance):
    assert isinstance(instance, rankPL_Multi)

@given(instance=rankPL_Plus_strategy)
@settings(max_examples=50)
def test_rankpl_plus_instantiation(instance):
    assert isinstance(instance, rankPL_Plus)

@given(instance=rankPL_Expression_strategy)
@settings(max_examples=50)
def test_rankpl_expression_instantiation(instance):
    assert isinstance(instance, rankPL_Expression)

@given(instance=AbstractDefinition_strategy)
@settings(max_examples=50)
def test_abstractdefinition_instantiation(instance):
    assert isinstance(instance, AbstractDefinition)

@given(instance=rankPL_DeclaredParameter_strategy)
@settings(max_examples=50)
def test_rankpl_declaredparameter_instantiation(instance):
    assert isinstance(instance, rankPL_DeclaredParameter)

@given(instance=rankPL_Definition_strategy)
@settings(max_examples=50)
def test_rankpl_definition_instantiation(instance):
    assert isinstance(instance, rankPL_Definition)

@given(instance=rankPL_AbstractDefinition_strategy)
@settings(max_examples=50)
def test_rankpl_abstractdefinition_instantiation(instance):
    assert isinstance(instance, rankPL_AbstractDefinition)



@given(instance=rankPL_AbstractDefinition_strategy)
def test_rankpl_abstractdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rankPL_Model_strategy)
@settings(max_examples=50)
def test_rankpl_model_instantiation(instance):
    assert isinstance(instance, rankPL_Model)

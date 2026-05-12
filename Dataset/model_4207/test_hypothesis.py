import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Greeting,
    myDsl_Selecao,
    myDsl_Define,
    myDsl_Expressao,
    myDsl_Greeting,
    myDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_greeting_is_not_abstract():
    assert not inspect.isabstract(Greeting)


def test_greeting_constructor_exists():
    assert callable(Greeting.__init__)


def test_greeting_constructor_args():
    sig = inspect.signature(Greeting.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_selecao_is_not_abstract():
    assert not inspect.isabstract(myDsl_Selecao)


def test_mydsl_selecao_constructor_exists():
    assert callable(myDsl_Selecao.__init__)


def test_mydsl_selecao_constructor_args():
    sig = inspect.signature(myDsl_Selecao.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_define_is_not_abstract():
    assert not inspect.isabstract(myDsl_Define)


def test_mydsl_define_constructor_exists():
    assert callable(myDsl_Define.__init__)


def test_mydsl_define_constructor_args():
    sig = inspect.signature(myDsl_Define.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expressao_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expressao)


def test_mydsl_expressao_constructor_exists():
    assert callable(myDsl_Expressao.__init__)


def test_mydsl_expressao_constructor_args():
    sig = inspect.signature(myDsl_Expressao.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_expressao_has_name():
    assert hasattr(myDsl_Expressao, "name")
    descriptor = None
    for klass in myDsl_Expressao.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl_Greeting)


def test_mydsl_greeting_constructor_exists():
    assert callable(myDsl_Greeting.__init__)


def test_mydsl_greeting_constructor_args():
    sig = inspect.signature(myDsl_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_greeting_has_value():
    assert hasattr(myDsl_Greeting, "value")
    descriptor = None
    for klass in myDsl_Greeting.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
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
Greeting_strategy = st.builds(
    Greeting,
)
myDsl_Selecao_strategy = st.builds(
    myDsl_Selecao,
)
myDsl_Define_strategy = st.builds(
    myDsl_Define,
)
myDsl_Expressao_strategy = st.builds(
    myDsl_Expressao,
    name=
        safe_text
)
myDsl_Greeting_strategy = st.builds(
    myDsl_Greeting,
    value=
        st.integers()
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)

@given(instance=Greeting_strategy)
@settings(max_examples=50)
def test_greeting_instantiation(instance):
    assert isinstance(instance, Greeting)

@given(instance=myDsl_Selecao_strategy)
@settings(max_examples=50)
def test_mydsl_selecao_instantiation(instance):
    assert isinstance(instance, myDsl_Selecao)

@given(instance=myDsl_Define_strategy)
@settings(max_examples=50)
def test_mydsl_define_instantiation(instance):
    assert isinstance(instance, myDsl_Define)

@given(instance=myDsl_Expressao_strategy)
@settings(max_examples=50)
def test_mydsl_expressao_instantiation(instance):
    assert isinstance(instance, myDsl_Expressao)



@given(instance=myDsl_Expressao_strategy)
def test_mydsl_expressao_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Greeting_strategy)
@settings(max_examples=50)
def test_mydsl_greeting_instantiation(instance):
    assert isinstance(instance, myDsl_Greeting)



@given(instance=myDsl_Greeting_strategy)
def test_mydsl_greeting_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)

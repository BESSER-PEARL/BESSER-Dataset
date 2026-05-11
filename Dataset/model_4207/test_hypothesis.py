import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Greeting,
    myDsl::Selecao,
    myDsl::Define,
    myDsl::Expressao,
    myDsl::Greeting,
    myDsl::Model,
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



def test_mydsl::selecao_is_not_abstract():
    assert not inspect.isabstract(myDsl::Selecao)


def test_mydsl::selecao_constructor_exists():
    assert callable(myDsl::Selecao.__init__)


def test_mydsl::selecao_constructor_args():
    sig = inspect.signature(myDsl::Selecao.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::define_is_not_abstract():
    assert not inspect.isabstract(myDsl::Define)


def test_mydsl::define_constructor_exists():
    assert callable(myDsl::Define.__init__)


def test_mydsl::define_constructor_args():
    sig = inspect.signature(myDsl::Define.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expressao_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expressao)


def test_mydsl::expressao_constructor_exists():
    assert callable(myDsl::Expressao.__init__)


def test_mydsl::expressao_constructor_args():
    sig = inspect.signature(myDsl::Expressao.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::expressao_has_name():
    assert hasattr(myDsl::Expressao, "name")
    descriptor = None
    for klass in myDsl::Expressao.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl::Greeting)


def test_mydsl::greeting_constructor_exists():
    assert callable(myDsl::Greeting.__init__)


def test_mydsl::greeting_constructor_args():
    sig = inspect.signature(myDsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl::greeting_has_value():
    assert hasattr(myDsl::Greeting, "value")
    descriptor = None
    for klass in myDsl::Greeting.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
myDsl::Selecao_strategy = st.builds(
    myDsl::Selecao,
)
myDsl::Define_strategy = st.builds(
    myDsl::Define,
)
myDsl::Expressao_strategy = st.builds(
    myDsl::Expressao,
    name=
        safe_text
)
myDsl::Greeting_strategy = st.builds(
    myDsl::Greeting,
    value=
        st.integers()
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=Greeting_strategy)
@settings(max_examples=50)
def test_greeting_instantiation(instance):
    assert isinstance(instance, Greeting)

@given(instance=myDsl::Selecao_strategy)
@settings(max_examples=50)
def test_mydsl::selecao_instantiation(instance):
    assert isinstance(instance, myDsl::Selecao)

@given(instance=myDsl::Define_strategy)
@settings(max_examples=50)
def test_mydsl::define_instantiation(instance):
    assert isinstance(instance, myDsl::Define)

@given(instance=myDsl::Expressao_strategy)
@settings(max_examples=50)
def test_mydsl::expressao_instantiation(instance):
    assert isinstance(instance, myDsl::Expressao)

@given(instance=myDsl::Expressao_strategy)
def test_mydsl::expressao_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Expressao_strategy)
def test_mydsl::expressao_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl::greeting_instantiation(instance):
    assert isinstance(instance, myDsl::Greeting)

@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)

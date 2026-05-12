import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    y4fsm_Bar,
    y4fsm_Foo,
    y4fsm_State,
    State,
    y4fsm_Region,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_y4fsm_bar_is_not_abstract():
    assert not inspect.isabstract(y4fsm_Bar)


def test_y4fsm_bar_constructor_exists():
    assert callable(y4fsm_Bar.__init__)


def test_y4fsm_bar_constructor_args():
    sig = inspect.signature(y4fsm_Bar.__init__)
    params = list(sig.parameters.keys())
    assert "baz" in params, "Missing parameter 'baz'"

def test_y4fsm_bar_has_baz():
    assert hasattr(y4fsm_Bar, "baz")
    descriptor = None
    for klass in y4fsm_Bar.__mro__:
        if "baz" in klass.__dict__:
            descriptor = klass.__dict__["baz"]
            break
    assert isinstance(descriptor, property)



def test_y4fsm_foo_is_not_abstract():
    assert not inspect.isabstract(y4fsm_Foo)


def test_y4fsm_foo_constructor_exists():
    assert callable(y4fsm_Foo.__init__)


def test_y4fsm_foo_constructor_args():
    sig = inspect.signature(y4fsm_Foo.__init__)
    params = list(sig.parameters.keys())
    assert "zoo" in params, "Missing parameter 'zoo'"

def test_y4fsm_foo_has_zoo():
    assert hasattr(y4fsm_Foo, "zoo")
    descriptor = None
    for klass in y4fsm_Foo.__mro__:
        if "zoo" in klass.__dict__:
            descriptor = klass.__dict__["zoo"]
            break
    assert isinstance(descriptor, property)



def test_y4fsm_state_is_not_abstract():
    assert not inspect.isabstract(y4fsm_State)


def test_y4fsm_state_constructor_exists():
    assert callable(y4fsm_State.__init__)


def test_y4fsm_state_constructor_args():
    sig = inspect.signature(y4fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_y4fsm_state_has_id():
    assert hasattr(y4fsm_State, "id")
    descriptor = None
    for klass in y4fsm_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_y4fsm_region_is_not_abstract():
    assert not inspect.isabstract(y4fsm_Region)


def test_y4fsm_region_constructor_exists():
    assert callable(y4fsm_Region.__init__)


def test_y4fsm_region_constructor_args():
    sig = inspect.signature(y4fsm_Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_y4fsm_region_has_name():
    assert hasattr(y4fsm_Region, "name")
    descriptor = None
    for klass in y4fsm_Region.__mro__:
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
y4fsm_Bar_strategy = st.builds(
    y4fsm_Bar,
    baz=
        safe_text
)
y4fsm_Foo_strategy = st.builds(
    y4fsm_Foo,
    zoo=
        safe_text
)
y4fsm_State_strategy = st.builds(
    y4fsm_State,
    id=
        safe_text
)
State_strategy = st.builds(
    State,
)
y4fsm_Region_strategy = st.builds(
    y4fsm_Region,
    name=
        safe_text
)

@given(instance=y4fsm_Bar_strategy)
@settings(max_examples=50)
def test_y4fsm_bar_instantiation(instance):
    assert isinstance(instance, y4fsm_Bar)



@given(instance=y4fsm_Bar_strategy)
def test_y4fsm_bar_baz_setter(instance):
    original = instance.baz
    instance.baz = original
    assert instance.baz == original

@given(instance=y4fsm_Foo_strategy)
@settings(max_examples=50)
def test_y4fsm_foo_instantiation(instance):
    assert isinstance(instance, y4fsm_Foo)



@given(instance=y4fsm_Foo_strategy)
def test_y4fsm_foo_zoo_setter(instance):
    original = instance.zoo
    instance.zoo = original
    assert instance.zoo == original

@given(instance=y4fsm_State_strategy)
@settings(max_examples=50)
def test_y4fsm_state_instantiation(instance):
    assert isinstance(instance, y4fsm_State)



@given(instance=y4fsm_State_strategy)
def test_y4fsm_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=y4fsm_Region_strategy)
@settings(max_examples=50)
def test_y4fsm_region_instantiation(instance):
    assert isinstance(instance, y4fsm_Region)



@given(instance=y4fsm_Region_strategy)
def test_y4fsm_region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

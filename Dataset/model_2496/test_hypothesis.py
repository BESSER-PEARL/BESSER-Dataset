import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    y5fsm_Bar,
    y5fsm_Foo,
    y5fsm_State,
    y5fsm_Region,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_y5fsm_bar_is_not_abstract():
    assert not inspect.isabstract(y5fsm_Bar)


def test_y5fsm_bar_constructor_exists():
    assert callable(y5fsm_Bar.__init__)


def test_y5fsm_bar_constructor_args():
    sig = inspect.signature(y5fsm_Bar.__init__)
    params = list(sig.parameters.keys())
    assert "baz" in params, "Missing parameter 'baz'"

def test_y5fsm_bar_has_baz():
    assert hasattr(y5fsm_Bar, "baz")
    descriptor = None
    for klass in y5fsm_Bar.__mro__:
        if "baz" in klass.__dict__:
            descriptor = klass.__dict__["baz"]
            break
    assert isinstance(descriptor, property)



def test_y5fsm_foo_is_not_abstract():
    assert not inspect.isabstract(y5fsm_Foo)


def test_y5fsm_foo_constructor_exists():
    assert callable(y5fsm_Foo.__init__)


def test_y5fsm_foo_constructor_args():
    sig = inspect.signature(y5fsm_Foo.__init__)
    params = list(sig.parameters.keys())
    assert "zoo" in params, "Missing parameter 'zoo'"

def test_y5fsm_foo_has_zoo():
    assert hasattr(y5fsm_Foo, "zoo")
    descriptor = None
    for klass in y5fsm_Foo.__mro__:
        if "zoo" in klass.__dict__:
            descriptor = klass.__dict__["zoo"]
            break
    assert isinstance(descriptor, property)



def test_y5fsm_state_is_not_abstract():
    assert not inspect.isabstract(y5fsm_State)


def test_y5fsm_state_constructor_exists():
    assert callable(y5fsm_State.__init__)


def test_y5fsm_state_constructor_args():
    sig = inspect.signature(y5fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_y5fsm_state_has_id():
    assert hasattr(y5fsm_State, "id")
    descriptor = None
    for klass in y5fsm_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_y5fsm_region_is_not_abstract():
    assert not inspect.isabstract(y5fsm_Region)


def test_y5fsm_region_constructor_exists():
    assert callable(y5fsm_Region.__init__)


def test_y5fsm_region_constructor_args():
    sig = inspect.signature(y5fsm_Region.__init__)
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
y5fsm_Bar_strategy = st.builds(
    y5fsm_Bar,
    baz=
        safe_text
)
y5fsm_Foo_strategy = st.builds(
    y5fsm_Foo,
    zoo=
        safe_text
)
y5fsm_State_strategy = st.builds(
    y5fsm_State,
    id=
        safe_text
)
y5fsm_Region_strategy = st.builds(
    y5fsm_Region,
)

@given(instance=y5fsm_Bar_strategy)
@settings(max_examples=50)
def test_y5fsm_bar_instantiation(instance):
    assert isinstance(instance, y5fsm_Bar)



@given(instance=y5fsm_Bar_strategy)
def test_y5fsm_bar_baz_setter(instance):
    original = instance.baz
    instance.baz = original
    assert instance.baz == original

@given(instance=y5fsm_Foo_strategy)
@settings(max_examples=50)
def test_y5fsm_foo_instantiation(instance):
    assert isinstance(instance, y5fsm_Foo)



@given(instance=y5fsm_Foo_strategy)
def test_y5fsm_foo_zoo_setter(instance):
    original = instance.zoo
    instance.zoo = original
    assert instance.zoo == original

@given(instance=y5fsm_State_strategy)
@settings(max_examples=50)
def test_y5fsm_state_instantiation(instance):
    assert isinstance(instance, y5fsm_State)



@given(instance=y5fsm_State_strategy)
def test_y5fsm_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=y5fsm_Region_strategy)
@settings(max_examples=50)
def test_y5fsm_region_instantiation(instance):
    assert isinstance(instance, y5fsm_Region)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractState,
    z2fsm_Foo,
    z2fsm_State,
    z2fsm_AbstractState,
    z2fsm_Region,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_z2fsm_foo_is_not_abstract():
    assert not inspect.isabstract(z2fsm_Foo)


def test_z2fsm_foo_constructor_exists():
    assert callable(z2fsm_Foo.__init__)


def test_z2fsm_foo_constructor_args():
    sig = inspect.signature(z2fsm_Foo.__init__)
    params = list(sig.parameters.keys())



def test_z2fsm_state_is_not_abstract():
    assert not inspect.isabstract(z2fsm_State)


def test_z2fsm_state_constructor_exists():
    assert callable(z2fsm_State.__init__)


def test_z2fsm_state_constructor_args():
    sig = inspect.signature(z2fsm_State.__init__)
    params = list(sig.parameters.keys())



def test_z2fsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(z2fsm_AbstractState)


def test_z2fsm_abstractstate_constructor_exists():
    assert callable(z2fsm_AbstractState.__init__)


def test_z2fsm_abstractstate_constructor_args():
    sig = inspect.signature(z2fsm_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_z2fsm_abstractstate_has_id():
    assert hasattr(z2fsm_AbstractState, "id")
    descriptor = None
    for klass in z2fsm_AbstractState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_z2fsm_region_is_not_abstract():
    assert not inspect.isabstract(z2fsm_Region)


def test_z2fsm_region_constructor_exists():
    assert callable(z2fsm_Region.__init__)


def test_z2fsm_region_constructor_args():
    sig = inspect.signature(z2fsm_Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_z2fsm_region_has_name():
    assert hasattr(z2fsm_Region, "name")
    descriptor = None
    for klass in z2fsm_Region.__mro__:
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
AbstractState_strategy = st.builds(
    AbstractState,
)
z2fsm_Foo_strategy = st.builds(
    z2fsm_Foo,
)
z2fsm_State_strategy = st.builds(
    z2fsm_State,
)
z2fsm_AbstractState_strategy = st.builds(
    z2fsm_AbstractState,
    id=
        safe_text
)
z2fsm_Region_strategy = st.builds(
    z2fsm_Region,
    name=
        safe_text
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=z2fsm_Foo_strategy)
@settings(max_examples=50)
def test_z2fsm_foo_instantiation(instance):
    assert isinstance(instance, z2fsm_Foo)

@given(instance=z2fsm_State_strategy)
@settings(max_examples=50)
def test_z2fsm_state_instantiation(instance):
    assert isinstance(instance, z2fsm_State)

@given(instance=z2fsm_AbstractState_strategy)
@settings(max_examples=50)
def test_z2fsm_abstractstate_instantiation(instance):
    assert isinstance(instance, z2fsm_AbstractState)



@given(instance=z2fsm_AbstractState_strategy)
def test_z2fsm_abstractstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=z2fsm_Region_strategy)
@settings(max_examples=50)
def test_z2fsm_region_instantiation(instance):
    assert isinstance(instance, z2fsm_Region)



@given(instance=z2fsm_Region_strategy)
def test_z2fsm_region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

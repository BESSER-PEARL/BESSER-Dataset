import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    z3fsm::AbstractState,
    AbstractState,
    z3fsm::State,
    z3fsm::Region,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_z3fsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(z3fsm::AbstractState)


def test_z3fsm::abstractstate_constructor_exists():
    assert callable(z3fsm::AbstractState.__init__)


def test_z3fsm::abstractstate_constructor_args():
    sig = inspect.signature(z3fsm::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_z3fsm::abstractstate_has_id():
    assert hasattr(z3fsm::AbstractState, "id")
    descriptor = None
    for klass in z3fsm::AbstractState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_z3fsm::state_is_not_abstract():
    assert not inspect.isabstract(z3fsm::State)


def test_z3fsm::state_constructor_exists():
    assert callable(z3fsm::State.__init__)


def test_z3fsm::state_constructor_args():
    sig = inspect.signature(z3fsm::State.__init__)
    params = list(sig.parameters.keys())



def test_z3fsm::region_is_not_abstract():
    assert not inspect.isabstract(z3fsm::Region)


def test_z3fsm::region_constructor_exists():
    assert callable(z3fsm::Region.__init__)


def test_z3fsm::region_constructor_args():
    sig = inspect.signature(z3fsm::Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_z3fsm::region_has_name():
    assert hasattr(z3fsm::Region, "name")
    descriptor = None
    for klass in z3fsm::Region.__mro__:
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
z3fsm::AbstractState_strategy = st.builds(
    z3fsm::AbstractState,
    id=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
z3fsm::State_strategy = st.builds(
    z3fsm::State,
)
z3fsm::Region_strategy = st.builds(
    z3fsm::Region,
    name=
        safe_text
)

@given(instance=z3fsm::AbstractState_strategy)
@settings(max_examples=50)
def test_z3fsm::abstractstate_instantiation(instance):
    assert isinstance(instance, z3fsm::AbstractState)

@given(instance=z3fsm::AbstractState_strategy)
def test_z3fsm::abstractstate_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=z3fsm::AbstractState_strategy)
def test_z3fsm::abstractstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=z3fsm::State_strategy)
@settings(max_examples=50)
def test_z3fsm::state_instantiation(instance):
    assert isinstance(instance, z3fsm::State)

@given(instance=z3fsm::Region_strategy)
@settings(max_examples=50)
def test_z3fsm::region_instantiation(instance):
    assert isinstance(instance, z3fsm::Region)

@given(instance=z3fsm::Region_strategy)
def test_z3fsm::region_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=z3fsm::Region_strategy)
def test_z3fsm::region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

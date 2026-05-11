import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    z8fsm::AbstractState,
    AbstractState,
    z8fsm::Region,
    z8fsm::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_z8fsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(z8fsm::AbstractState)


def test_z8fsm::abstractstate_constructor_exists():
    assert callable(z8fsm::AbstractState.__init__)


def test_z8fsm::abstractstate_constructor_args():
    sig = inspect.signature(z8fsm::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_z8fsm::abstractstate_has_id():
    assert hasattr(z8fsm::AbstractState, "id")
    descriptor = None
    for klass in z8fsm::AbstractState.__mro__:
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



def test_z8fsm::region_is_not_abstract():
    assert not inspect.isabstract(z8fsm::Region)


def test_z8fsm::region_constructor_exists():
    assert callable(z8fsm::Region.__init__)


def test_z8fsm::region_constructor_args():
    sig = inspect.signature(z8fsm::Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_z8fsm::region_has_name():
    assert hasattr(z8fsm::Region, "name")
    descriptor = None
    for klass in z8fsm::Region.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_z8fsm::state_is_not_abstract():
    assert not inspect.isabstract(z8fsm::State)


def test_z8fsm::state_constructor_exists():
    assert callable(z8fsm::State.__init__)


def test_z8fsm::state_constructor_args():
    sig = inspect.signature(z8fsm::State.__init__)
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
z8fsm::AbstractState_strategy = st.builds(
    z8fsm::AbstractState,
    id=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
z8fsm::Region_strategy = st.builds(
    z8fsm::Region,
    name=
        safe_text
)
z8fsm::State_strategy = st.builds(
    z8fsm::State,
)

@given(instance=z8fsm::AbstractState_strategy)
@settings(max_examples=50)
def test_z8fsm::abstractstate_instantiation(instance):
    assert isinstance(instance, z8fsm::AbstractState)

@given(instance=z8fsm::AbstractState_strategy)
def test_z8fsm::abstractstate_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=z8fsm::AbstractState_strategy)
def test_z8fsm::abstractstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=z8fsm::Region_strategy)
@settings(max_examples=50)
def test_z8fsm::region_instantiation(instance):
    assert isinstance(instance, z8fsm::Region)

@given(instance=z8fsm::Region_strategy)
def test_z8fsm::region_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=z8fsm::Region_strategy)
def test_z8fsm::region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=z8fsm::State_strategy)
@settings(max_examples=50)
def test_z8fsm::state_instantiation(instance):
    assert isinstance(instance, z8fsm::State)

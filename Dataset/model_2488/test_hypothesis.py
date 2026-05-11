import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractState,
    z2fsm::Foo,
    z2fsm::State,
    z2fsm::AbstractState,
    z2fsm::Region,
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



def test_z2fsm::foo_is_not_abstract():
    assert not inspect.isabstract(z2fsm::Foo)


def test_z2fsm::foo_constructor_exists():
    assert callable(z2fsm::Foo.__init__)


def test_z2fsm::foo_constructor_args():
    sig = inspect.signature(z2fsm::Foo.__init__)
    params = list(sig.parameters.keys())



def test_z2fsm::state_is_not_abstract():
    assert not inspect.isabstract(z2fsm::State)


def test_z2fsm::state_constructor_exists():
    assert callable(z2fsm::State.__init__)


def test_z2fsm::state_constructor_args():
    sig = inspect.signature(z2fsm::State.__init__)
    params = list(sig.parameters.keys())



def test_z2fsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(z2fsm::AbstractState)


def test_z2fsm::abstractstate_constructor_exists():
    assert callable(z2fsm::AbstractState.__init__)


def test_z2fsm::abstractstate_constructor_args():
    sig = inspect.signature(z2fsm::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_z2fsm::abstractstate_has_id():
    assert hasattr(z2fsm::AbstractState, "id")
    descriptor = None
    for klass in z2fsm::AbstractState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_z2fsm::region_is_not_abstract():
    assert not inspect.isabstract(z2fsm::Region)


def test_z2fsm::region_constructor_exists():
    assert callable(z2fsm::Region.__init__)


def test_z2fsm::region_constructor_args():
    sig = inspect.signature(z2fsm::Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_z2fsm::region_has_name():
    assert hasattr(z2fsm::Region, "name")
    descriptor = None
    for klass in z2fsm::Region.__mro__:
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
z2fsm::Foo_strategy = st.builds(
    z2fsm::Foo,
)
z2fsm::State_strategy = st.builds(
    z2fsm::State,
)
z2fsm::AbstractState_strategy = st.builds(
    z2fsm::AbstractState,
    id=
        safe_text
)
z2fsm::Region_strategy = st.builds(
    z2fsm::Region,
    name=
        safe_text
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=z2fsm::Foo_strategy)
@settings(max_examples=50)
def test_z2fsm::foo_instantiation(instance):
    assert isinstance(instance, z2fsm::Foo)

@given(instance=z2fsm::State_strategy)
@settings(max_examples=50)
def test_z2fsm::state_instantiation(instance):
    assert isinstance(instance, z2fsm::State)

@given(instance=z2fsm::AbstractState_strategy)
@settings(max_examples=50)
def test_z2fsm::abstractstate_instantiation(instance):
    assert isinstance(instance, z2fsm::AbstractState)

@given(instance=z2fsm::AbstractState_strategy)
def test_z2fsm::abstractstate_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=z2fsm::AbstractState_strategy)
def test_z2fsm::abstractstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=z2fsm::Region_strategy)
@settings(max_examples=50)
def test_z2fsm::region_instantiation(instance):
    assert isinstance(instance, z2fsm::Region)

@given(instance=z2fsm::Region_strategy)
def test_z2fsm::region_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=z2fsm::Region_strategy)
def test_z2fsm::region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

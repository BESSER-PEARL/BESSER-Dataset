import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    y3fsm::Foo,
    y3fsm::AbstractState,
    AbstractState,
    y3fsm::Region,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_y3fsm::foo_is_not_abstract():
    assert not inspect.isabstract(y3fsm::Foo)


def test_y3fsm::foo_constructor_exists():
    assert callable(y3fsm::Foo.__init__)


def test_y3fsm::foo_constructor_args():
    sig = inspect.signature(y3fsm::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "zoo" in params, "Missing parameter 'zoo'"

def test_y3fsm::foo_has_zoo():
    assert hasattr(y3fsm::Foo, "zoo")
    descriptor = None
    for klass in y3fsm::Foo.__mro__:
        if "zoo" in klass.__dict__:
            descriptor = klass.__dict__["zoo"]
            break
    assert isinstance(descriptor, property)



def test_y3fsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(y3fsm::AbstractState)


def test_y3fsm::abstractstate_constructor_exists():
    assert callable(y3fsm::AbstractState.__init__)


def test_y3fsm::abstractstate_constructor_args():
    sig = inspect.signature(y3fsm::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_y3fsm::abstractstate_has_id():
    assert hasattr(y3fsm::AbstractState, "id")
    descriptor = None
    for klass in y3fsm::AbstractState.__mro__:
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



def test_y3fsm::region_is_not_abstract():
    assert not inspect.isabstract(y3fsm::Region)


def test_y3fsm::region_constructor_exists():
    assert callable(y3fsm::Region.__init__)


def test_y3fsm::region_constructor_args():
    sig = inspect.signature(y3fsm::Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_y3fsm::region_has_name():
    assert hasattr(y3fsm::Region, "name")
    descriptor = None
    for klass in y3fsm::Region.__mro__:
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
y3fsm::Foo_strategy = st.builds(
    y3fsm::Foo,
    zoo=
        safe_text
)
y3fsm::AbstractState_strategy = st.builds(
    y3fsm::AbstractState,
    id=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
y3fsm::Region_strategy = st.builds(
    y3fsm::Region,
    name=
        safe_text
)

@given(instance=y3fsm::Foo_strategy)
@settings(max_examples=50)
def test_y3fsm::foo_instantiation(instance):
    assert isinstance(instance, y3fsm::Foo)

@given(instance=y3fsm::Foo_strategy)
def test_y3fsm::foo_zoo_type(instance):
    assert isinstance(instance.zoo, str)


@given(instance=y3fsm::Foo_strategy)
def test_y3fsm::foo_zoo_setter(instance):
    original = instance.zoo
    instance.zoo = original
    assert instance.zoo == original

@given(instance=y3fsm::AbstractState_strategy)
@settings(max_examples=50)
def test_y3fsm::abstractstate_instantiation(instance):
    assert isinstance(instance, y3fsm::AbstractState)

@given(instance=y3fsm::AbstractState_strategy)
def test_y3fsm::abstractstate_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=y3fsm::AbstractState_strategy)
def test_y3fsm::abstractstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=y3fsm::Region_strategy)
@settings(max_examples=50)
def test_y3fsm::region_instantiation(instance):
    assert isinstance(instance, y3fsm::Region)

@given(instance=y3fsm::Region_strategy)
def test_y3fsm::region_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=y3fsm::Region_strategy)
def test_y3fsm::region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    y5fsm::Bar,
    y5fsm::Foo,
    y5fsm::State,
    y5fsm::Region,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_y5fsm::bar_is_not_abstract():
    assert not inspect.isabstract(y5fsm::Bar)


def test_y5fsm::bar_constructor_exists():
    assert callable(y5fsm::Bar.__init__)


def test_y5fsm::bar_constructor_args():
    sig = inspect.signature(y5fsm::Bar.__init__)
    params = list(sig.parameters.keys())
    assert "baz" in params, "Missing parameter 'baz'"

def test_y5fsm::bar_has_baz():
    assert hasattr(y5fsm::Bar, "baz")
    descriptor = None
    for klass in y5fsm::Bar.__mro__:
        if "baz" in klass.__dict__:
            descriptor = klass.__dict__["baz"]
            break
    assert isinstance(descriptor, property)



def test_y5fsm::foo_is_not_abstract():
    assert not inspect.isabstract(y5fsm::Foo)


def test_y5fsm::foo_constructor_exists():
    assert callable(y5fsm::Foo.__init__)


def test_y5fsm::foo_constructor_args():
    sig = inspect.signature(y5fsm::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "zoo" in params, "Missing parameter 'zoo'"

def test_y5fsm::foo_has_zoo():
    assert hasattr(y5fsm::Foo, "zoo")
    descriptor = None
    for klass in y5fsm::Foo.__mro__:
        if "zoo" in klass.__dict__:
            descriptor = klass.__dict__["zoo"]
            break
    assert isinstance(descriptor, property)



def test_y5fsm::state_is_not_abstract():
    assert not inspect.isabstract(y5fsm::State)


def test_y5fsm::state_constructor_exists():
    assert callable(y5fsm::State.__init__)


def test_y5fsm::state_constructor_args():
    sig = inspect.signature(y5fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_y5fsm::state_has_id():
    assert hasattr(y5fsm::State, "id")
    descriptor = None
    for klass in y5fsm::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_y5fsm::region_is_not_abstract():
    assert not inspect.isabstract(y5fsm::Region)


def test_y5fsm::region_constructor_exists():
    assert callable(y5fsm::Region.__init__)


def test_y5fsm::region_constructor_args():
    sig = inspect.signature(y5fsm::Region.__init__)
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
y5fsm::Bar_strategy = st.builds(
    y5fsm::Bar,
    baz=
        safe_text
)
y5fsm::Foo_strategy = st.builds(
    y5fsm::Foo,
    zoo=
        safe_text
)
y5fsm::State_strategy = st.builds(
    y5fsm::State,
    id=
        safe_text
)
y5fsm::Region_strategy = st.builds(
    y5fsm::Region,
)

@given(instance=y5fsm::Bar_strategy)
@settings(max_examples=50)
def test_y5fsm::bar_instantiation(instance):
    assert isinstance(instance, y5fsm::Bar)

@given(instance=y5fsm::Bar_strategy)
def test_y5fsm::bar_baz_type(instance):
    assert isinstance(instance.baz, str)


@given(instance=y5fsm::Bar_strategy)
def test_y5fsm::bar_baz_setter(instance):
    original = instance.baz
    instance.baz = original
    assert instance.baz == original

@given(instance=y5fsm::Foo_strategy)
@settings(max_examples=50)
def test_y5fsm::foo_instantiation(instance):
    assert isinstance(instance, y5fsm::Foo)

@given(instance=y5fsm::Foo_strategy)
def test_y5fsm::foo_zoo_type(instance):
    assert isinstance(instance.zoo, str)


@given(instance=y5fsm::Foo_strategy)
def test_y5fsm::foo_zoo_setter(instance):
    original = instance.zoo
    instance.zoo = original
    assert instance.zoo == original

@given(instance=y5fsm::State_strategy)
@settings(max_examples=50)
def test_y5fsm::state_instantiation(instance):
    assert isinstance(instance, y5fsm::State)

@given(instance=y5fsm::State_strategy)
def test_y5fsm::state_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=y5fsm::State_strategy)
def test_y5fsm::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=y5fsm::Region_strategy)
@settings(max_examples=50)
def test_y5fsm::region_instantiation(instance):
    assert isinstance(instance, y5fsm::Region)

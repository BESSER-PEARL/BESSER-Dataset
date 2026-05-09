import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lit::petriNets::Transition,
    lit::petriNets::Place,
    lit::petriNets::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lit::petrinets::transition_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::Transition)


def test_lit::petrinets::transition_constructor_exists():
    assert callable(lit::petriNets::Transition.__init__)


def test_lit::petrinets::transition_constructor_args():
    sig = inspect.signature(lit::petriNets::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lit::petrinets::transition_has_name():
    assert hasattr(lit::petriNets::Transition, "name")
    descriptor = None
    for klass in lit::petriNets::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lit::petrinets::place_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::Place)


def test_lit::petrinets::place_constructor_exists():
    assert callable(lit::petriNets::Place.__init__)


def test_lit::petrinets::place_constructor_args():
    sig = inspect.signature(lit::petriNets::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lit::petrinets::place_has_name():
    assert hasattr(lit::petriNets::Place, "name")
    descriptor = None
    for klass in lit::petriNets::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lit::petrinets::net_is_not_abstract():
    assert not inspect.isabstract(lit::petriNets::Net)


def test_lit::petrinets::net_constructor_exists():
    assert callable(lit::petriNets::Net.__init__)


def test_lit::petrinets::net_constructor_args():
    sig = inspect.signature(lit::petriNets::Net.__init__)
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
lit::petriNets::Transition_strategy = st.builds(
    lit::petriNets::Transition,
    name=
        safe_text
)
lit::petriNets::Place_strategy = st.builds(
    lit::petriNets::Place,
    name=
        safe_text
)
lit::petriNets::Net_strategy = st.builds(
    lit::petriNets::Net,
)

@given(instance=lit::petriNets::Transition_strategy)
@settings(max_examples=50)
def test_lit::petrinets::transition_instantiation(instance):
    assert isinstance(instance, lit::petriNets::Transition)

@given(instance=lit::petriNets::Transition_strategy)
def test_lit::petrinets::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lit::petriNets::Transition_strategy)
def test_lit::petrinets::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lit::petriNets::Place_strategy)
@settings(max_examples=50)
def test_lit::petrinets::place_instantiation(instance):
    assert isinstance(instance, lit::petriNets::Place)

@given(instance=lit::petriNets::Place_strategy)
def test_lit::petrinets::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lit::petriNets::Place_strategy)
def test_lit::petrinets::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lit::petriNets::Net_strategy)
@settings(max_examples=50)
def test_lit::petrinets::net_instantiation(instance):
    assert isinstance(instance, lit::petriNets::Net)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PN::Transition,
    PN::Place,
    PN::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pn::transition_is_not_abstract():
    assert not inspect.isabstract(PN::Transition)


def test_pn::transition_constructor_exists():
    assert callable(PN::Transition.__init__)


def test_pn::transition_constructor_args():
    sig = inspect.signature(PN::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_pn::transition_has_input():
    assert hasattr(PN::Transition, "input")
    descriptor = None
    for klass in PN::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_pn::place_is_not_abstract():
    assert not inspect.isabstract(PN::Place)


def test_pn::place_constructor_exists():
    assert callable(PN::Place.__init__)


def test_pn::place_constructor_args():
    sig = inspect.signature(PN::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pn::place_has_name():
    assert hasattr(PN::Place, "name")
    descriptor = None
    for klass in PN::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pn::net_is_not_abstract():
    assert not inspect.isabstract(PN::Net)


def test_pn::net_constructor_exists():
    assert callable(PN::Net.__init__)


def test_pn::net_constructor_args():
    sig = inspect.signature(PN::Net.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pn::net_has_name():
    assert hasattr(PN::Net, "name")
    descriptor = None
    for klass in PN::Net.__mro__:
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
PN::Transition_strategy = st.builds(
    PN::Transition,
    input=
        safe_text
)
PN::Place_strategy = st.builds(
    PN::Place,
    name=
        safe_text
)
PN::Net_strategy = st.builds(
    PN::Net,
    name=
        safe_text
)

@given(instance=PN::Transition_strategy)
@settings(max_examples=50)
def test_pn::transition_instantiation(instance):
    assert isinstance(instance, PN::Transition)

@given(instance=PN::Transition_strategy)
def test_pn::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=PN::Transition_strategy)
def test_pn::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=PN::Place_strategy)
@settings(max_examples=50)
def test_pn::place_instantiation(instance):
    assert isinstance(instance, PN::Place)

@given(instance=PN::Place_strategy)
def test_pn::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PN::Place_strategy)
def test_pn::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PN::Net_strategy)
@settings(max_examples=50)
def test_pn::net_instantiation(instance):
    assert isinstance(instance, PN::Net)

@given(instance=PN::Net_strategy)
def test_pn::net_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PN::Net_strategy)
def test_pn::net_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

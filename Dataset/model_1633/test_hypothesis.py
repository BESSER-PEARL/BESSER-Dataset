import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PN_Transition,
    PN_Place,
    PN_Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pn_transition_is_not_abstract():
    assert not inspect.isabstract(PN_Transition)


def test_pn_transition_constructor_exists():
    assert callable(PN_Transition.__init__)


def test_pn_transition_constructor_args():
    sig = inspect.signature(PN_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_pn_transition_has_input():
    assert hasattr(PN_Transition, "input")
    descriptor = None
    for klass in PN_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_pn_place_is_not_abstract():
    assert not inspect.isabstract(PN_Place)


def test_pn_place_constructor_exists():
    assert callable(PN_Place.__init__)


def test_pn_place_constructor_args():
    sig = inspect.signature(PN_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pn_place_has_name():
    assert hasattr(PN_Place, "name")
    descriptor = None
    for klass in PN_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pn_net_is_not_abstract():
    assert not inspect.isabstract(PN_Net)


def test_pn_net_constructor_exists():
    assert callable(PN_Net.__init__)


def test_pn_net_constructor_args():
    sig = inspect.signature(PN_Net.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pn_net_has_name():
    assert hasattr(PN_Net, "name")
    descriptor = None
    for klass in PN_Net.__mro__:
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
PN_Transition_strategy = st.builds(
    PN_Transition,
    input=
        safe_text
)
PN_Place_strategy = st.builds(
    PN_Place,
    name=
        safe_text
)
PN_Net_strategy = st.builds(
    PN_Net,
    name=
        safe_text
)

@given(instance=PN_Transition_strategy)
@settings(max_examples=50)
def test_pn_transition_instantiation(instance):
    assert isinstance(instance, PN_Transition)



@given(instance=PN_Transition_strategy)
def test_pn_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=PN_Place_strategy)
@settings(max_examples=50)
def test_pn_place_instantiation(instance):
    assert isinstance(instance, PN_Place)



@given(instance=PN_Place_strategy)
def test_pn_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PN_Net_strategy)
@settings(max_examples=50)
def test_pn_net_instantiation(instance):
    assert isinstance(instance, PN_Net)



@given(instance=PN_Net_strategy)
def test_pn_net_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

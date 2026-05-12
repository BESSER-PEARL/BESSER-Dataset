import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lit_petriNets_Transition,
    lit_petriNets_Place,
    lit_petriNets_Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lit_petrinets_transition_is_not_abstract():
    assert not inspect.isabstract(lit_petriNets_Transition)


def test_lit_petrinets_transition_constructor_exists():
    assert callable(lit_petriNets_Transition.__init__)


def test_lit_petrinets_transition_constructor_args():
    sig = inspect.signature(lit_petriNets_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lit_petrinets_transition_has_name():
    assert hasattr(lit_petriNets_Transition, "name")
    descriptor = None
    for klass in lit_petriNets_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lit_petrinets_place_is_not_abstract():
    assert not inspect.isabstract(lit_petriNets_Place)


def test_lit_petrinets_place_constructor_exists():
    assert callable(lit_petriNets_Place.__init__)


def test_lit_petrinets_place_constructor_args():
    sig = inspect.signature(lit_petriNets_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lit_petrinets_place_has_name():
    assert hasattr(lit_petriNets_Place, "name")
    descriptor = None
    for klass in lit_petriNets_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lit_petrinets_net_is_not_abstract():
    assert not inspect.isabstract(lit_petriNets_Net)


def test_lit_petrinets_net_constructor_exists():
    assert callable(lit_petriNets_Net.__init__)


def test_lit_petrinets_net_constructor_args():
    sig = inspect.signature(lit_petriNets_Net.__init__)
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
lit_petriNets_Transition_strategy = st.builds(
    lit_petriNets_Transition,
    name=
        safe_text
)
lit_petriNets_Place_strategy = st.builds(
    lit_petriNets_Place,
    name=
        safe_text
)
lit_petriNets_Net_strategy = st.builds(
    lit_petriNets_Net,
)

@given(instance=lit_petriNets_Transition_strategy)
@settings(max_examples=50)
def test_lit_petrinets_transition_instantiation(instance):
    assert isinstance(instance, lit_petriNets_Transition)



@given(instance=lit_petriNets_Transition_strategy)
def test_lit_petrinets_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lit_petriNets_Place_strategy)
@settings(max_examples=50)
def test_lit_petrinets_place_instantiation(instance):
    assert isinstance(instance, lit_petriNets_Place)



@given(instance=lit_petriNets_Place_strategy)
def test_lit_petrinets_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lit_petriNets_Net_strategy)
@settings(max_examples=50)
def test_lit_petrinets_net_instantiation(instance):
    assert isinstance(instance, lit_petriNets_Net)

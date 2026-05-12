import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinet_Net,
    petrinet_Box,
    petrinet_Transition,
    petrinet_Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_net_is_not_abstract():
    assert not inspect.isabstract(petrinet_Net)


def test_petrinet_net_constructor_exists():
    assert callable(petrinet_Net.__init__)


def test_petrinet_net_constructor_args():
    sig = inspect.signature(petrinet_Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_box_is_not_abstract():
    assert not inspect.isabstract(petrinet_Box)


def test_petrinet_box_constructor_exists():
    assert callable(petrinet_Box.__init__)


def test_petrinet_box_constructor_args():
    sig = inspect.signature(petrinet_Box.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_box_has_id():
    assert hasattr(petrinet_Box, "id")
    descriptor = None
    for klass in petrinet_Box.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_box_has_name():
    assert hasattr(petrinet_Box, "name")
    descriptor = None
    for klass in petrinet_Box.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_transition_has_id():
    assert hasattr(petrinet_Transition, "id")
    descriptor = None
    for klass in petrinet_Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_transition_has_name():
    assert hasattr(petrinet_Transition, "name")
    descriptor = None
    for klass in petrinet_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_petrinet_place_has_name():
    assert hasattr(petrinet_Place, "name")
    descriptor = None
    for klass in petrinet_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_place_has_id():
    assert hasattr(petrinet_Place, "id")
    descriptor = None
    for klass in petrinet_Place.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
petrinet_Net_strategy = st.builds(
    petrinet_Net,
)
petrinet_Box_strategy = st.builds(
    petrinet_Box,
    id=
        st.integers(),
    name=
        safe_text
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
    id=
        st.integers(),
    name=
        safe_text
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
    name=
        safe_text,
    id=
        st.integers()
)

@given(instance=petrinet_Net_strategy)
@settings(max_examples=50)
def test_petrinet_net_instantiation(instance):
    assert isinstance(instance, petrinet_Net)

@given(instance=petrinet_Box_strategy)
@settings(max_examples=50)
def test_petrinet_box_instantiation(instance):
    assert isinstance(instance, petrinet_Box)



@given(instance=petrinet_Box_strategy)
def test_petrinet_box_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=petrinet_Box_strategy)
def test_petrinet_box_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)



@given(instance=petrinet_Transition_strategy)
def test_petrinet_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=petrinet_Transition_strategy)
def test_petrinet_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)



@given(instance=petrinet_Place_strategy)
def test_petrinet_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petrinet_Place_strategy)
def test_petrinet_place_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

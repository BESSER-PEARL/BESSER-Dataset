import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petriNetz_Token,
    petriNetz_Arc,
    petriNetz_Transition,
    petriNetz_Place,
    Arc,
    petriNetz_PTArc,
    petriNetz_TPArc,
    petriNetz_Petrinet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetz_token_is_not_abstract():
    assert not inspect.isabstract(petriNetz_Token)


def test_petrinetz_token_constructor_exists():
    assert callable(petriNetz_Token.__init__)


def test_petrinetz_token_constructor_args():
    sig = inspect.signature(petriNetz_Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinetz_arc_is_not_abstract():
    assert not inspect.isabstract(petriNetz_Arc)


def test_petrinetz_arc_constructor_exists():
    assert callable(petriNetz_Arc.__init__)


def test_petrinetz_arc_constructor_args():
    sig = inspect.signature(petriNetz_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinetz_arc_has_weight():
    assert hasattr(petriNetz_Arc, "weight")
    descriptor = None
    for klass in petriNetz_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinetz_transition_is_not_abstract():
    assert not inspect.isabstract(petriNetz_Transition)


def test_petrinetz_transition_constructor_exists():
    assert callable(petriNetz_Transition.__init__)


def test_petrinetz_transition_constructor_args():
    sig = inspect.signature(petriNetz_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetz_transition_has_name():
    assert hasattr(petriNetz_Transition, "name")
    descriptor = None
    for klass in petriNetz_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetz_place_is_not_abstract():
    assert not inspect.isabstract(petriNetz_Place)


def test_petrinetz_place_constructor_exists():
    assert callable(petriNetz_Place.__init__)


def test_petrinetz_place_constructor_args():
    sig = inspect.signature(petriNetz_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetz_place_has_name():
    assert hasattr(petriNetz_Place, "name")
    descriptor = None
    for klass in petriNetz_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetz_ptarc_is_not_abstract():
    assert not inspect.isabstract(petriNetz_PTArc)


def test_petrinetz_ptarc_constructor_exists():
    assert callable(petriNetz_PTArc.__init__)


def test_petrinetz_ptarc_constructor_args():
    sig = inspect.signature(petriNetz_PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetz_tparc_is_not_abstract():
    assert not inspect.isabstract(petriNetz_TPArc)


def test_petrinetz_tparc_constructor_exists():
    assert callable(petriNetz_TPArc.__init__)


def test_petrinetz_tparc_constructor_args():
    sig = inspect.signature(petriNetz_TPArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetz_petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNetz_Petrinet)


def test_petrinetz_petrinet_constructor_exists():
    assert callable(petriNetz_Petrinet.__init__)


def test_petrinetz_petrinet_constructor_args():
    sig = inspect.signature(petriNetz_Petrinet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetz_petrinet_has_name():
    assert hasattr(petriNetz_Petrinet, "name")
    descriptor = None
    for klass in petriNetz_Petrinet.__mro__:
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
petriNetz_Token_strategy = st.builds(
    petriNetz_Token,
)
petriNetz_Arc_strategy = st.builds(
    petriNetz_Arc,
    weight=
        st.integers()
)
petriNetz_Transition_strategy = st.builds(
    petriNetz_Transition,
    name=
        safe_text
)
petriNetz_Place_strategy = st.builds(
    petriNetz_Place,
    name=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
petriNetz_PTArc_strategy = st.builds(
    petriNetz_PTArc,
)
petriNetz_TPArc_strategy = st.builds(
    petriNetz_TPArc,
)
petriNetz_Petrinet_strategy = st.builds(
    petriNetz_Petrinet,
    name=
        safe_text
)

@given(instance=petriNetz_Token_strategy)
@settings(max_examples=50)
def test_petrinetz_token_instantiation(instance):
    assert isinstance(instance, petriNetz_Token)

@given(instance=petriNetz_Arc_strategy)
@settings(max_examples=50)
def test_petrinetz_arc_instantiation(instance):
    assert isinstance(instance, petriNetz_Arc)



@given(instance=petriNetz_Arc_strategy)
def test_petrinetz_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petriNetz_Transition_strategy)
@settings(max_examples=50)
def test_petrinetz_transition_instantiation(instance):
    assert isinstance(instance, petriNetz_Transition)



@given(instance=petriNetz_Transition_strategy)
def test_petrinetz_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNetz_Place_strategy)
@settings(max_examples=50)
def test_petrinetz_place_instantiation(instance):
    assert isinstance(instance, petriNetz_Place)



@given(instance=petriNetz_Place_strategy)
def test_petrinetz_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petriNetz_PTArc_strategy)
@settings(max_examples=50)
def test_petrinetz_ptarc_instantiation(instance):
    assert isinstance(instance, petriNetz_PTArc)

@given(instance=petriNetz_TPArc_strategy)
@settings(max_examples=50)
def test_petrinetz_tparc_instantiation(instance):
    assert isinstance(instance, petriNetz_TPArc)

@given(instance=petriNetz_Petrinet_strategy)
@settings(max_examples=50)
def test_petrinetz_petrinet_instantiation(instance):
    assert isinstance(instance, petriNetz_Petrinet)



@given(instance=petriNetz_Petrinet_strategy)
def test_petrinetz_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

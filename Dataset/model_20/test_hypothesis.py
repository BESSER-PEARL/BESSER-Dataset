import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petriNetz::Token,
    petriNetz::Arc,
    petriNetz::Transition,
    petriNetz::Place,
    Arc,
    petriNetz::PTArc,
    petriNetz::TPArc,
    petriNetz::Petrinet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetz::token_is_not_abstract():
    assert not inspect.isabstract(petriNetz::Token)


def test_petrinetz::token_constructor_exists():
    assert callable(petriNetz::Token.__init__)


def test_petrinetz::token_constructor_args():
    sig = inspect.signature(petriNetz::Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinetz::arc_is_not_abstract():
    assert not inspect.isabstract(petriNetz::Arc)


def test_petrinetz::arc_constructor_exists():
    assert callable(petriNetz::Arc.__init__)


def test_petrinetz::arc_constructor_args():
    sig = inspect.signature(petriNetz::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinetz::arc_has_weight():
    assert hasattr(petriNetz::Arc, "weight")
    descriptor = None
    for klass in petriNetz::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinetz::transition_is_not_abstract():
    assert not inspect.isabstract(petriNetz::Transition)


def test_petrinetz::transition_constructor_exists():
    assert callable(petriNetz::Transition.__init__)


def test_petrinetz::transition_constructor_args():
    sig = inspect.signature(petriNetz::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetz::transition_has_name():
    assert hasattr(petriNetz::Transition, "name")
    descriptor = None
    for klass in petriNetz::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetz::place_is_not_abstract():
    assert not inspect.isabstract(petriNetz::Place)


def test_petrinetz::place_constructor_exists():
    assert callable(petriNetz::Place.__init__)


def test_petrinetz::place_constructor_args():
    sig = inspect.signature(petriNetz::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetz::place_has_name():
    assert hasattr(petriNetz::Place, "name")
    descriptor = None
    for klass in petriNetz::Place.__mro__:
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



def test_petrinetz::ptarc_is_not_abstract():
    assert not inspect.isabstract(petriNetz::PTArc)


def test_petrinetz::ptarc_constructor_exists():
    assert callable(petriNetz::PTArc.__init__)


def test_petrinetz::ptarc_constructor_args():
    sig = inspect.signature(petriNetz::PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetz::tparc_is_not_abstract():
    assert not inspect.isabstract(petriNetz::TPArc)


def test_petrinetz::tparc_constructor_exists():
    assert callable(petriNetz::TPArc.__init__)


def test_petrinetz::tparc_constructor_args():
    sig = inspect.signature(petriNetz::TPArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetz::petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNetz::Petrinet)


def test_petrinetz::petrinet_constructor_exists():
    assert callable(petriNetz::Petrinet.__init__)


def test_petrinetz::petrinet_constructor_args():
    sig = inspect.signature(petriNetz::Petrinet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetz::petrinet_has_name():
    assert hasattr(petriNetz::Petrinet, "name")
    descriptor = None
    for klass in petriNetz::Petrinet.__mro__:
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
petriNetz::Token_strategy = st.builds(
    petriNetz::Token,
)
petriNetz::Arc_strategy = st.builds(
    petriNetz::Arc,
    weight=
        st.integers()
)
petriNetz::Transition_strategy = st.builds(
    petriNetz::Transition,
    name=
        safe_text
)
petriNetz::Place_strategy = st.builds(
    petriNetz::Place,
    name=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
petriNetz::PTArc_strategy = st.builds(
    petriNetz::PTArc,
)
petriNetz::TPArc_strategy = st.builds(
    petriNetz::TPArc,
)
petriNetz::Petrinet_strategy = st.builds(
    petriNetz::Petrinet,
    name=
        safe_text
)

@given(instance=petriNetz::Token_strategy)
@settings(max_examples=50)
def test_petrinetz::token_instantiation(instance):
    assert isinstance(instance, petriNetz::Token)

@given(instance=petriNetz::Arc_strategy)
@settings(max_examples=50)
def test_petrinetz::arc_instantiation(instance):
    assert isinstance(instance, petriNetz::Arc)

@given(instance=petriNetz::Arc_strategy)
def test_petrinetz::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petriNetz::Arc_strategy)
def test_petrinetz::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petriNetz::Transition_strategy)
@settings(max_examples=50)
def test_petrinetz::transition_instantiation(instance):
    assert isinstance(instance, petriNetz::Transition)

@given(instance=petriNetz::Transition_strategy)
def test_petrinetz::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNetz::Transition_strategy)
def test_petrinetz::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNetz::Place_strategy)
@settings(max_examples=50)
def test_petrinetz::place_instantiation(instance):
    assert isinstance(instance, petriNetz::Place)

@given(instance=petriNetz::Place_strategy)
def test_petrinetz::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNetz::Place_strategy)
def test_petrinetz::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petriNetz::PTArc_strategy)
@settings(max_examples=50)
def test_petrinetz::ptarc_instantiation(instance):
    assert isinstance(instance, petriNetz::PTArc)

@given(instance=petriNetz::TPArc_strategy)
@settings(max_examples=50)
def test_petrinetz::tparc_instantiation(instance):
    assert isinstance(instance, petriNetz::TPArc)

@given(instance=petriNetz::Petrinet_strategy)
@settings(max_examples=50)
def test_petrinetz::petrinet_instantiation(instance):
    assert isinstance(instance, petriNetz::Petrinet)

@given(instance=petriNetz::Petrinet_strategy)
def test_petrinetz::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNetz::Petrinet_strategy)
def test_petrinetz::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

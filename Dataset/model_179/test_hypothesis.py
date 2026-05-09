import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinets::Arc,
    Arc,
    petrinets::TPArc,
    petrinets::PTArc,
    petrinets::Transition,
    petrinets::Place,
    petrinets::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinets::arc_is_not_abstract():
    assert not inspect.isabstract(petrinets::Arc)


def test_petrinets::arc_constructor_exists():
    assert callable(petrinets::Arc.__init__)


def test_petrinets::arc_constructor_args():
    sig = inspect.signature(petrinets::Arc.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::tparc_is_not_abstract():
    assert not inspect.isabstract(petrinets::TPArc)


def test_petrinets::tparc_constructor_exists():
    assert callable(petrinets::TPArc.__init__)


def test_petrinets::tparc_constructor_args():
    sig = inspect.signature(petrinets::TPArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::ptarc_is_not_abstract():
    assert not inspect.isabstract(petrinets::PTArc)


def test_petrinets::ptarc_constructor_exists():
    assert callable(petrinets::PTArc.__init__)


def test_petrinets::ptarc_constructor_args():
    sig = inspect.signature(petrinets::PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::transition_is_not_abstract():
    assert not inspect.isabstract(petrinets::Transition)


def test_petrinets::transition_constructor_exists():
    assert callable(petrinets::Transition.__init__)


def test_petrinets::transition_constructor_args():
    sig = inspect.signature(petrinets::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets::transition_has_name():
    assert hasattr(petrinets::Transition, "name")
    descriptor = None
    for klass in petrinets::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::place_is_not_abstract():
    assert not inspect.isabstract(petrinets::Place)


def test_petrinets::place_constructor_exists():
    assert callable(petrinets::Place.__init__)


def test_petrinets::place_constructor_args():
    sig = inspect.signature(petrinets::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets::place_has_name():
    assert hasattr(petrinets::Place, "name")
    descriptor = None
    for klass in petrinets::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::net_is_not_abstract():
    assert not inspect.isabstract(petrinets::Net)


def test_petrinets::net_constructor_exists():
    assert callable(petrinets::Net.__init__)


def test_petrinets::net_constructor_args():
    sig = inspect.signature(petrinets::Net.__init__)
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
petrinets::Arc_strategy = st.builds(
    petrinets::Arc,
)
Arc_strategy = st.builds(
    Arc,
)
petrinets::TPArc_strategy = st.builds(
    petrinets::TPArc,
)
petrinets::PTArc_strategy = st.builds(
    petrinets::PTArc,
)
petrinets::Transition_strategy = st.builds(
    petrinets::Transition,
    name=
        safe_text
)
petrinets::Place_strategy = st.builds(
    petrinets::Place,
    name=
        safe_text
)
petrinets::Net_strategy = st.builds(
    petrinets::Net,
)

@given(instance=petrinets::Arc_strategy)
@settings(max_examples=50)
def test_petrinets::arc_instantiation(instance):
    assert isinstance(instance, petrinets::Arc)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinets::TPArc_strategy)
@settings(max_examples=50)
def test_petrinets::tparc_instantiation(instance):
    assert isinstance(instance, petrinets::TPArc)

@given(instance=petrinets::PTArc_strategy)
@settings(max_examples=50)
def test_petrinets::ptarc_instantiation(instance):
    assert isinstance(instance, petrinets::PTArc)

@given(instance=petrinets::Transition_strategy)
@settings(max_examples=50)
def test_petrinets::transition_instantiation(instance):
    assert isinstance(instance, petrinets::Transition)

@given(instance=petrinets::Transition_strategy)
def test_petrinets::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinets::Transition_strategy)
def test_petrinets::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinets::Place_strategy)
@settings(max_examples=50)
def test_petrinets::place_instantiation(instance):
    assert isinstance(instance, petrinets::Place)

@given(instance=petrinets::Place_strategy)
def test_petrinets::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinets::Place_strategy)
def test_petrinets::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinets::Net_strategy)
@settings(max_examples=50)
def test_petrinets::net_instantiation(instance):
    assert isinstance(instance, petrinets::Net)

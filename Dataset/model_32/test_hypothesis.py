import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    petrinet::Arc,
    petrinet::Named,
    petrinet::OutArc,
    petrinet::InArc,
    Named,
    petrinet::Transition,
    petrinet::Place,
    petrinet::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::arc_has_weight():
    assert hasattr(petrinet::Arc, "weight")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::named_is_not_abstract():
    assert not inspect.isabstract(petrinet::Named)


def test_petrinet::named_constructor_exists():
    assert callable(petrinet::Named.__init__)


def test_petrinet::named_constructor_args():
    sig = inspect.signature(petrinet::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::named_has_name():
    assert hasattr(petrinet::Named, "name")
    descriptor = None
    for klass in petrinet::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::outarc_is_not_abstract():
    assert not inspect.isabstract(petrinet::OutArc)


def test_petrinet::outarc_constructor_exists():
    assert callable(petrinet::OutArc.__init__)


def test_petrinet::outarc_constructor_args():
    sig = inspect.signature(petrinet::OutArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::inarc_is_not_abstract():
    assert not inspect.isabstract(petrinet::InArc)


def test_petrinet::inarc_constructor_exists():
    assert callable(petrinet::InArc.__init__)


def test_petrinet::inarc_constructor_args():
    sig = inspect.signature(petrinet::InArc.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_petrinet::place_has_token():
    assert hasattr(petrinet::Place, "token")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petrinet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinet::PetriNet.__init__)
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
Arc_strategy = st.builds(
    Arc,
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
    weight=
        st.integers()
)
petrinet::Named_strategy = st.builds(
    petrinet::Named,
    name=
        safe_text
)
petrinet::OutArc_strategy = st.builds(
    petrinet::OutArc,
)
petrinet::InArc_strategy = st.builds(
    petrinet::InArc,
)
Named_strategy = st.builds(
    Named,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
    token=
        st.integers()
)
petrinet::PetriNet_strategy = st.builds(
    petrinet::PetriNet,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petrinet::Named_strategy)
@settings(max_examples=50)
def test_petrinet::named_instantiation(instance):
    assert isinstance(instance, petrinet::Named)

@given(instance=petrinet::Named_strategy)
def test_petrinet::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Named_strategy)
def test_petrinet::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::OutArc_strategy)
@settings(max_examples=50)
def test_petrinet::outarc_instantiation(instance):
    assert isinstance(instance, petrinet::OutArc)

@given(instance=petrinet::InArc_strategy)
@settings(max_examples=50)
def test_petrinet::inarc_instantiation(instance):
    assert isinstance(instance, petrinet::InArc)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_token_type(instance):
    assert isinstance(instance.token, int)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=petrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::PetriNet)

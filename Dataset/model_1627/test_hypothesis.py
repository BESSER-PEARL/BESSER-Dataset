import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    petri_Transition,
    petri_Place,
    petri_NamedElement,
    petri_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_petri_transition_is_not_abstract():
    assert not inspect.isabstract(petri_Transition)


def test_petri_transition_constructor_exists():
    assert callable(petri_Transition.__init__)


def test_petri_transition_constructor_args():
    sig = inspect.signature(petri_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petri_place_is_not_abstract():
    assert not inspect.isabstract(petri_Place)


def test_petri_place_constructor_exists():
    assert callable(petri_Place.__init__)


def test_petri_place_constructor_args():
    sig = inspect.signature(petri_Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petri_place_has_tokens():
    assert hasattr(petri_Place, "tokens")
    descriptor = None
    for klass in petri_Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_petri_namedelement_is_not_abstract():
    assert not inspect.isabstract(petri_NamedElement)


def test_petri_namedelement_constructor_exists():
    assert callable(petri_NamedElement.__init__)


def test_petri_namedelement_constructor_args():
    sig = inspect.signature(petri_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri_namedelement_has_name():
    assert hasattr(petri_NamedElement, "name")
    descriptor = None
    for klass in petri_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri_petrinet_is_not_abstract():
    assert not inspect.isabstract(petri_PetriNet)


def test_petri_petrinet_constructor_exists():
    assert callable(petri_PetriNet.__init__)


def test_petri_petrinet_constructor_args():
    sig = inspect.signature(petri_PetriNet.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
petri_Transition_strategy = st.builds(
    petri_Transition,
)
petri_Place_strategy = st.builds(
    petri_Place,
    tokens=
        st.integers()
)
petri_NamedElement_strategy = st.builds(
    petri_NamedElement,
    name=
        safe_text
)
petri_PetriNet_strategy = st.builds(
    petri_PetriNet,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=petri_Transition_strategy)
@settings(max_examples=50)
def test_petri_transition_instantiation(instance):
    assert isinstance(instance, petri_Transition)

@given(instance=petri_Place_strategy)
@settings(max_examples=50)
def test_petri_place_instantiation(instance):
    assert isinstance(instance, petri_Place)



@given(instance=petri_Place_strategy)
def test_petri_place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=petri_NamedElement_strategy)
@settings(max_examples=50)
def test_petri_namedelement_instantiation(instance):
    assert isinstance(instance, petri_NamedElement)



@given(instance=petri_NamedElement_strategy)
def test_petri_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petri_PetriNet_strategy)
@settings(max_examples=50)
def test_petri_petrinet_instantiation(instance):
    assert isinstance(instance, petri_PetriNet)

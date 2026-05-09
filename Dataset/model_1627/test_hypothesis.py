import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    petri::Transition,
    petri::Place,
    petri::NamedElement,
    petri::PetriNet,
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



def test_petri::transition_is_not_abstract():
    assert not inspect.isabstract(petri::Transition)


def test_petri::transition_constructor_exists():
    assert callable(petri::Transition.__init__)


def test_petri::transition_constructor_args():
    sig = inspect.signature(petri::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petri::place_is_not_abstract():
    assert not inspect.isabstract(petri::Place)


def test_petri::place_constructor_exists():
    assert callable(petri::Place.__init__)


def test_petri::place_constructor_args():
    sig = inspect.signature(petri::Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petri::place_has_tokens():
    assert hasattr(petri::Place, "tokens")
    descriptor = None
    for klass in petri::Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_petri::namedelement_is_not_abstract():
    assert not inspect.isabstract(petri::NamedElement)


def test_petri::namedelement_constructor_exists():
    assert callable(petri::NamedElement.__init__)


def test_petri::namedelement_constructor_args():
    sig = inspect.signature(petri::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri::namedelement_has_name():
    assert hasattr(petri::NamedElement, "name")
    descriptor = None
    for klass in petri::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri::petrinet_is_not_abstract():
    assert not inspect.isabstract(petri::PetriNet)


def test_petri::petrinet_constructor_exists():
    assert callable(petri::PetriNet.__init__)


def test_petri::petrinet_constructor_args():
    sig = inspect.signature(petri::PetriNet.__init__)
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
petri::Transition_strategy = st.builds(
    petri::Transition,
)
petri::Place_strategy = st.builds(
    petri::Place,
    tokens=
        st.integers()
)
petri::NamedElement_strategy = st.builds(
    petri::NamedElement,
    name=
        safe_text
)
petri::PetriNet_strategy = st.builds(
    petri::PetriNet,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=petri::Transition_strategy)
@settings(max_examples=50)
def test_petri::transition_instantiation(instance):
    assert isinstance(instance, petri::Transition)

@given(instance=petri::Place_strategy)
@settings(max_examples=50)
def test_petri::place_instantiation(instance):
    assert isinstance(instance, petri::Place)

@given(instance=petri::Place_strategy)
def test_petri::place_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=petri::Place_strategy)
def test_petri::place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=petri::NamedElement_strategy)
@settings(max_examples=50)
def test_petri::namedelement_instantiation(instance):
    assert isinstance(instance, petri::NamedElement)

@given(instance=petri::NamedElement_strategy)
def test_petri::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petri::NamedElement_strategy)
def test_petri::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petri::PetriNet_strategy)
@settings(max_examples=50)
def test_petri::petrinet_instantiation(instance):
    assert isinstance(instance, petri::PetriNet)

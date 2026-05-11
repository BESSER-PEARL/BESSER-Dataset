import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Behavior::NamedElement,
    NamedElement,
    Behavior::System,
    Behavior::Transition,
    Behavior::State,
    Behavior::Event,
    Behavior::Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_behavior::namedelement_is_not_abstract():
    assert not inspect.isabstract(Behavior::NamedElement)


def test_behavior::namedelement_constructor_exists():
    assert callable(Behavior::NamedElement.__init__)


def test_behavior::namedelement_constructor_args():
    sig = inspect.signature(Behavior::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behavior::namedelement_has_name():
    assert hasattr(Behavior::NamedElement, "name")
    descriptor = None
    for klass in Behavior::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_behavior::system_is_not_abstract():
    assert not inspect.isabstract(Behavior::System)


def test_behavior::system_constructor_exists():
    assert callable(Behavior::System.__init__)


def test_behavior::system_constructor_args():
    sig = inspect.signature(Behavior::System.__init__)
    params = list(sig.parameters.keys())



def test_behavior::transition_is_not_abstract():
    assert not inspect.isabstract(Behavior::Transition)


def test_behavior::transition_constructor_exists():
    assert callable(Behavior::Transition.__init__)


def test_behavior::transition_constructor_args():
    sig = inspect.signature(Behavior::Transition.__init__)
    params = list(sig.parameters.keys())



def test_behavior::state_is_not_abstract():
    assert not inspect.isabstract(Behavior::State)


def test_behavior::state_constructor_exists():
    assert callable(Behavior::State.__init__)


def test_behavior::state_constructor_args():
    sig = inspect.signature(Behavior::State.__init__)
    params = list(sig.parameters.keys())



def test_behavior::event_is_not_abstract():
    assert not inspect.isabstract(Behavior::Event)


def test_behavior::event_constructor_exists():
    assert callable(Behavior::Event.__init__)


def test_behavior::event_constructor_args():
    sig = inspect.signature(Behavior::Event.__init__)
    params = list(sig.parameters.keys())



def test_behavior::component_is_not_abstract():
    assert not inspect.isabstract(Behavior::Component)


def test_behavior::component_constructor_exists():
    assert callable(Behavior::Component.__init__)


def test_behavior::component_constructor_args():
    sig = inspect.signature(Behavior::Component.__init__)
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
Behavior::NamedElement_strategy = st.builds(
    Behavior::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Behavior::System_strategy = st.builds(
    Behavior::System,
)
Behavior::Transition_strategy = st.builds(
    Behavior::Transition,
)
Behavior::State_strategy = st.builds(
    Behavior::State,
)
Behavior::Event_strategy = st.builds(
    Behavior::Event,
)
Behavior::Component_strategy = st.builds(
    Behavior::Component,
)

@given(instance=Behavior::NamedElement_strategy)
@settings(max_examples=50)
def test_behavior::namedelement_instantiation(instance):
    assert isinstance(instance, Behavior::NamedElement)

@given(instance=Behavior::NamedElement_strategy)
def test_behavior::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Behavior::NamedElement_strategy)
def test_behavior::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Behavior::System_strategy)
@settings(max_examples=50)
def test_behavior::system_instantiation(instance):
    assert isinstance(instance, Behavior::System)

@given(instance=Behavior::Transition_strategy)
@settings(max_examples=50)
def test_behavior::transition_instantiation(instance):
    assert isinstance(instance, Behavior::Transition)

@given(instance=Behavior::State_strategy)
@settings(max_examples=50)
def test_behavior::state_instantiation(instance):
    assert isinstance(instance, Behavior::State)

@given(instance=Behavior::Event_strategy)
@settings(max_examples=50)
def test_behavior::event_instantiation(instance):
    assert isinstance(instance, Behavior::Event)

@given(instance=Behavior::Component_strategy)
@settings(max_examples=50)
def test_behavior::component_instantiation(instance):
    assert isinstance(instance, Behavior::Component)

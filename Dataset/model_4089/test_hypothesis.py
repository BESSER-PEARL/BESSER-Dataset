import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Behavior_NamedElement,
    NamedElement,
    Behavior_System,
    Behavior_Transition,
    Behavior_State,
    Behavior_Event,
    Behavior_Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_behavior_namedelement_is_not_abstract():
    assert not inspect.isabstract(Behavior_NamedElement)


def test_behavior_namedelement_constructor_exists():
    assert callable(Behavior_NamedElement.__init__)


def test_behavior_namedelement_constructor_args():
    sig = inspect.signature(Behavior_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behavior_namedelement_has_name():
    assert hasattr(Behavior_NamedElement, "name")
    descriptor = None
    for klass in Behavior_NamedElement.__mro__:
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



def test_behavior_system_is_not_abstract():
    assert not inspect.isabstract(Behavior_System)


def test_behavior_system_constructor_exists():
    assert callable(Behavior_System.__init__)


def test_behavior_system_constructor_args():
    sig = inspect.signature(Behavior_System.__init__)
    params = list(sig.parameters.keys())



def test_behavior_transition_is_not_abstract():
    assert not inspect.isabstract(Behavior_Transition)


def test_behavior_transition_constructor_exists():
    assert callable(Behavior_Transition.__init__)


def test_behavior_transition_constructor_args():
    sig = inspect.signature(Behavior_Transition.__init__)
    params = list(sig.parameters.keys())



def test_behavior_state_is_not_abstract():
    assert not inspect.isabstract(Behavior_State)


def test_behavior_state_constructor_exists():
    assert callable(Behavior_State.__init__)


def test_behavior_state_constructor_args():
    sig = inspect.signature(Behavior_State.__init__)
    params = list(sig.parameters.keys())



def test_behavior_event_is_not_abstract():
    assert not inspect.isabstract(Behavior_Event)


def test_behavior_event_constructor_exists():
    assert callable(Behavior_Event.__init__)


def test_behavior_event_constructor_args():
    sig = inspect.signature(Behavior_Event.__init__)
    params = list(sig.parameters.keys())



def test_behavior_component_is_not_abstract():
    assert not inspect.isabstract(Behavior_Component)


def test_behavior_component_constructor_exists():
    assert callable(Behavior_Component.__init__)


def test_behavior_component_constructor_args():
    sig = inspect.signature(Behavior_Component.__init__)
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
Behavior_NamedElement_strategy = st.builds(
    Behavior_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Behavior_System_strategy = st.builds(
    Behavior_System,
)
Behavior_Transition_strategy = st.builds(
    Behavior_Transition,
)
Behavior_State_strategy = st.builds(
    Behavior_State,
)
Behavior_Event_strategy = st.builds(
    Behavior_Event,
)
Behavior_Component_strategy = st.builds(
    Behavior_Component,
)

@given(instance=Behavior_NamedElement_strategy)
@settings(max_examples=50)
def test_behavior_namedelement_instantiation(instance):
    assert isinstance(instance, Behavior_NamedElement)



@given(instance=Behavior_NamedElement_strategy)
def test_behavior_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Behavior_System_strategy)
@settings(max_examples=50)
def test_behavior_system_instantiation(instance):
    assert isinstance(instance, Behavior_System)

@given(instance=Behavior_Transition_strategy)
@settings(max_examples=50)
def test_behavior_transition_instantiation(instance):
    assert isinstance(instance, Behavior_Transition)

@given(instance=Behavior_State_strategy)
@settings(max_examples=50)
def test_behavior_state_instantiation(instance):
    assert isinstance(instance, Behavior_State)

@given(instance=Behavior_Event_strategy)
@settings(max_examples=50)
def test_behavior_event_instantiation(instance):
    assert isinstance(instance, Behavior_Event)

@given(instance=Behavior_Component_strategy)
@settings(max_examples=50)
def test_behavior_component_instantiation(instance):
    assert isinstance(instance, Behavior_Component)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    states::Trace,
    states::Transition,
    states::State,
    states::StateSystem,
    states::ActionExecution,
    states::Event,
    states::EObject,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_states::trace_is_not_abstract():
    assert not inspect.isabstract(states::Trace)


def test_states::trace_constructor_exists():
    assert callable(states::Trace.__init__)


def test_states::trace_constructor_args():
    sig = inspect.signature(states::Trace.__init__)
    params = list(sig.parameters.keys())



def test_states::transition_is_not_abstract():
    assert not inspect.isabstract(states::Transition)


def test_states::transition_constructor_exists():
    assert callable(states::Transition.__init__)


def test_states::transition_constructor_args():
    sig = inspect.signature(states::Transition.__init__)
    params = list(sig.parameters.keys())



def test_states::state_is_not_abstract():
    assert not inspect.isabstract(states::State)


def test_states::state_constructor_exists():
    assert callable(states::State.__init__)


def test_states::state_constructor_args():
    sig = inspect.signature(states::State.__init__)
    params = list(sig.parameters.keys())



def test_states::statesystem_is_not_abstract():
    assert not inspect.isabstract(states::StateSystem)


def test_states::statesystem_constructor_exists():
    assert callable(states::StateSystem.__init__)


def test_states::statesystem_constructor_args():
    sig = inspect.signature(states::StateSystem.__init__)
    params = list(sig.parameters.keys())



def test_states::actionexecution_is_not_abstract():
    assert not inspect.isabstract(states::ActionExecution)


def test_states::actionexecution_constructor_exists():
    assert callable(states::ActionExecution.__init__)


def test_states::actionexecution_constructor_args():
    sig = inspect.signature(states::ActionExecution.__init__)
    params = list(sig.parameters.keys())



def test_states::event_is_not_abstract():
    assert not inspect.isabstract(states::Event)


def test_states::event_constructor_exists():
    assert callable(states::Event.__init__)


def test_states::event_constructor_args():
    sig = inspect.signature(states::Event.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_states::event_has_qualifiedName():
    assert hasattr(states::Event, "qualifiedName")
    descriptor = None
    for klass in states::Event.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_states::eobject_is_not_abstract():
    assert not inspect.isabstract(states::EObject)


def test_states::eobject_constructor_exists():
    assert callable(states::EObject.__init__)


def test_states::eobject_constructor_args():
    sig = inspect.signature(states::EObject.__init__)
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
states::Trace_strategy = st.builds(
    states::Trace,
)
states::Transition_strategy = st.builds(
    states::Transition,
)
states::State_strategy = st.builds(
    states::State,
)
states::StateSystem_strategy = st.builds(
    states::StateSystem,
)
states::ActionExecution_strategy = st.builds(
    states::ActionExecution,
)
states::Event_strategy = st.builds(
    states::Event,
    qualifiedName=
        safe_text
)
states::EObject_strategy = st.builds(
    states::EObject,
)

@given(instance=states::Trace_strategy)
@settings(max_examples=50)
def test_states::trace_instantiation(instance):
    assert isinstance(instance, states::Trace)

@given(instance=states::Transition_strategy)
@settings(max_examples=50)
def test_states::transition_instantiation(instance):
    assert isinstance(instance, states::Transition)

@given(instance=states::State_strategy)
@settings(max_examples=50)
def test_states::state_instantiation(instance):
    assert isinstance(instance, states::State)

@given(instance=states::StateSystem_strategy)
@settings(max_examples=50)
def test_states::statesystem_instantiation(instance):
    assert isinstance(instance, states::StateSystem)

@given(instance=states::ActionExecution_strategy)
@settings(max_examples=50)
def test_states::actionexecution_instantiation(instance):
    assert isinstance(instance, states::ActionExecution)

@given(instance=states::Event_strategy)
@settings(max_examples=50)
def test_states::event_instantiation(instance):
    assert isinstance(instance, states::Event)

@given(instance=states::Event_strategy)
def test_states::event_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=states::Event_strategy)
def test_states::event_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=states::EObject_strategy)
@settings(max_examples=50)
def test_states::eobject_instantiation(instance):
    assert isinstance(instance, states::EObject)

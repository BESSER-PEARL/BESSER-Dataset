import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Transition,
    devs_InternalTransition,
    devs_ExternalTransition,
    Event,
    devs_OutputEvent,
    devs_InputEvent,
    devs_OutputFunction,
    devs_Transition,
    devs_Event,
    devs_State,
    devs_AtomicModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_devs_internaltransition_is_not_abstract():
    assert not inspect.isabstract(devs_InternalTransition)


def test_devs_internaltransition_constructor_exists():
    assert callable(devs_InternalTransition.__init__)


def test_devs_internaltransition_constructor_args():
    sig = inspect.signature(devs_InternalTransition.__init__)
    params = list(sig.parameters.keys())



def test_devs_externaltransition_is_not_abstract():
    assert not inspect.isabstract(devs_ExternalTransition)


def test_devs_externaltransition_constructor_exists():
    assert callable(devs_ExternalTransition.__init__)


def test_devs_externaltransition_constructor_args():
    sig = inspect.signature(devs_ExternalTransition.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_devs_outputevent_is_not_abstract():
    assert not inspect.isabstract(devs_OutputEvent)


def test_devs_outputevent_constructor_exists():
    assert callable(devs_OutputEvent.__init__)


def test_devs_outputevent_constructor_args():
    sig = inspect.signature(devs_OutputEvent.__init__)
    params = list(sig.parameters.keys())



def test_devs_inputevent_is_not_abstract():
    assert not inspect.isabstract(devs_InputEvent)


def test_devs_inputevent_constructor_exists():
    assert callable(devs_InputEvent.__init__)


def test_devs_inputevent_constructor_args():
    sig = inspect.signature(devs_InputEvent.__init__)
    params = list(sig.parameters.keys())



def test_devs_outputfunction_is_not_abstract():
    assert not inspect.isabstract(devs_OutputFunction)


def test_devs_outputfunction_constructor_exists():
    assert callable(devs_OutputFunction.__init__)


def test_devs_outputfunction_constructor_args():
    sig = inspect.signature(devs_OutputFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devs_outputfunction_has_name():
    assert hasattr(devs_OutputFunction, "name")
    descriptor = None
    for klass in devs_OutputFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devs_transition_is_not_abstract():
    assert not inspect.isabstract(devs_Transition)


def test_devs_transition_constructor_exists():
    assert callable(devs_Transition.__init__)


def test_devs_transition_constructor_args():
    sig = inspect.signature(devs_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devs_transition_has_name():
    assert hasattr(devs_Transition, "name")
    descriptor = None
    for klass in devs_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devs_event_is_not_abstract():
    assert not inspect.isabstract(devs_Event)


def test_devs_event_constructor_exists():
    assert callable(devs_Event.__init__)


def test_devs_event_constructor_args():
    sig = inspect.signature(devs_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devs_event_has_name():
    assert hasattr(devs_Event, "name")
    descriptor = None
    for klass in devs_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devs_state_is_not_abstract():
    assert not inspect.isabstract(devs_State)


def test_devs_state_constructor_exists():
    assert callable(devs_State.__init__)


def test_devs_state_constructor_args():
    sig = inspect.signature(devs_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "lifeTime" in params, "Missing parameter 'lifeTime'"

def test_devs_state_has_name():
    assert hasattr(devs_State, "name")
    descriptor = None
    for klass in devs_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_devs_state_has_lifeTime():
    assert hasattr(devs_State, "lifeTime")
    descriptor = None
    for klass in devs_State.__mro__:
        if "lifeTime" in klass.__dict__:
            descriptor = klass.__dict__["lifeTime"]
            break
    assert isinstance(descriptor, property)



def test_devs_atomicmodel_is_not_abstract():
    assert not inspect.isabstract(devs_AtomicModel)


def test_devs_atomicmodel_constructor_exists():
    assert callable(devs_AtomicModel.__init__)


def test_devs_atomicmodel_constructor_args():
    sig = inspect.signature(devs_AtomicModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devs_atomicmodel_has_name():
    assert hasattr(devs_AtomicModel, "name")
    descriptor = None
    for klass in devs_AtomicModel.__mro__:
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
Transition_strategy = st.builds(
    Transition,
)
devs_InternalTransition_strategy = st.builds(
    devs_InternalTransition,
)
devs_ExternalTransition_strategy = st.builds(
    devs_ExternalTransition,
)
Event_strategy = st.builds(
    Event,
)
devs_OutputEvent_strategy = st.builds(
    devs_OutputEvent,
)
devs_InputEvent_strategy = st.builds(
    devs_InputEvent,
)
devs_OutputFunction_strategy = st.builds(
    devs_OutputFunction,
    name=
        safe_text
)
devs_Transition_strategy = st.builds(
    devs_Transition,
    name=
        safe_text
)
devs_Event_strategy = st.builds(
    devs_Event,
    name=
        safe_text
)
devs_State_strategy = st.builds(
    devs_State,
    name=
        safe_text,
    lifeTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
devs_AtomicModel_strategy = st.builds(
    devs_AtomicModel,
    name=
        safe_text
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=devs_InternalTransition_strategy)
@settings(max_examples=50)
def test_devs_internaltransition_instantiation(instance):
    assert isinstance(instance, devs_InternalTransition)

@given(instance=devs_ExternalTransition_strategy)
@settings(max_examples=50)
def test_devs_externaltransition_instantiation(instance):
    assert isinstance(instance, devs_ExternalTransition)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=devs_OutputEvent_strategy)
@settings(max_examples=50)
def test_devs_outputevent_instantiation(instance):
    assert isinstance(instance, devs_OutputEvent)

@given(instance=devs_InputEvent_strategy)
@settings(max_examples=50)
def test_devs_inputevent_instantiation(instance):
    assert isinstance(instance, devs_InputEvent)

@given(instance=devs_OutputFunction_strategy)
@settings(max_examples=50)
def test_devs_outputfunction_instantiation(instance):
    assert isinstance(instance, devs_OutputFunction)



@given(instance=devs_OutputFunction_strategy)
def test_devs_outputfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=devs_Transition_strategy)
@settings(max_examples=50)
def test_devs_transition_instantiation(instance):
    assert isinstance(instance, devs_Transition)



@given(instance=devs_Transition_strategy)
def test_devs_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=devs_Event_strategy)
@settings(max_examples=50)
def test_devs_event_instantiation(instance):
    assert isinstance(instance, devs_Event)



@given(instance=devs_Event_strategy)
def test_devs_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=devs_State_strategy)
@settings(max_examples=50)
def test_devs_state_instantiation(instance):
    assert isinstance(instance, devs_State)



@given(instance=devs_State_strategy)
def test_devs_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=devs_State_strategy)
def test_devs_state_lifeTime_setter(instance):
    original = instance.lifeTime
    instance.lifeTime = original
    assert instance.lifeTime == original

@given(instance=devs_AtomicModel_strategy)
@settings(max_examples=50)
def test_devs_atomicmodel_instantiation(instance):
    assert isinstance(instance, devs_AtomicModel)



@given(instance=devs_AtomicModel_strategy)
def test_devs_atomicmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

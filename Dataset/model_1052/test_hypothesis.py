import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Transition,
    devs::InternalTransition,
    devs::ExternalTransition,
    Event,
    devs::OutputEvent,
    devs::InputEvent,
    devs::OutputFunction,
    devs::Transition,
    devs::Event,
    devs::State,
    devs::AtomicModel,
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



def test_devs::internaltransition_is_not_abstract():
    assert not inspect.isabstract(devs::InternalTransition)


def test_devs::internaltransition_constructor_exists():
    assert callable(devs::InternalTransition.__init__)


def test_devs::internaltransition_constructor_args():
    sig = inspect.signature(devs::InternalTransition.__init__)
    params = list(sig.parameters.keys())



def test_devs::externaltransition_is_not_abstract():
    assert not inspect.isabstract(devs::ExternalTransition)


def test_devs::externaltransition_constructor_exists():
    assert callable(devs::ExternalTransition.__init__)


def test_devs::externaltransition_constructor_args():
    sig = inspect.signature(devs::ExternalTransition.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_devs::outputevent_is_not_abstract():
    assert not inspect.isabstract(devs::OutputEvent)


def test_devs::outputevent_constructor_exists():
    assert callable(devs::OutputEvent.__init__)


def test_devs::outputevent_constructor_args():
    sig = inspect.signature(devs::OutputEvent.__init__)
    params = list(sig.parameters.keys())



def test_devs::inputevent_is_not_abstract():
    assert not inspect.isabstract(devs::InputEvent)


def test_devs::inputevent_constructor_exists():
    assert callable(devs::InputEvent.__init__)


def test_devs::inputevent_constructor_args():
    sig = inspect.signature(devs::InputEvent.__init__)
    params = list(sig.parameters.keys())



def test_devs::outputfunction_is_not_abstract():
    assert not inspect.isabstract(devs::OutputFunction)


def test_devs::outputfunction_constructor_exists():
    assert callable(devs::OutputFunction.__init__)


def test_devs::outputfunction_constructor_args():
    sig = inspect.signature(devs::OutputFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devs::outputfunction_has_name():
    assert hasattr(devs::OutputFunction, "name")
    descriptor = None
    for klass in devs::OutputFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devs::transition_is_not_abstract():
    assert not inspect.isabstract(devs::Transition)


def test_devs::transition_constructor_exists():
    assert callable(devs::Transition.__init__)


def test_devs::transition_constructor_args():
    sig = inspect.signature(devs::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devs::transition_has_name():
    assert hasattr(devs::Transition, "name")
    descriptor = None
    for klass in devs::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devs::event_is_not_abstract():
    assert not inspect.isabstract(devs::Event)


def test_devs::event_constructor_exists():
    assert callable(devs::Event.__init__)


def test_devs::event_constructor_args():
    sig = inspect.signature(devs::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devs::event_has_name():
    assert hasattr(devs::Event, "name")
    descriptor = None
    for klass in devs::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devs::state_is_not_abstract():
    assert not inspect.isabstract(devs::State)


def test_devs::state_constructor_exists():
    assert callable(devs::State.__init__)


def test_devs::state_constructor_args():
    sig = inspect.signature(devs::State.__init__)
    params = list(sig.parameters.keys())
    assert "lifeTime" in params, "Missing parameter 'lifeTime'"
    assert "name" in params, "Missing parameter 'name'"

def test_devs::state_has_lifeTime():
    assert hasattr(devs::State, "lifeTime")
    descriptor = None
    for klass in devs::State.__mro__:
        if "lifeTime" in klass.__dict__:
            descriptor = klass.__dict__["lifeTime"]
            break
    assert isinstance(descriptor, property)

def test_devs::state_has_name():
    assert hasattr(devs::State, "name")
    descriptor = None
    for klass in devs::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devs::atomicmodel_is_not_abstract():
    assert not inspect.isabstract(devs::AtomicModel)


def test_devs::atomicmodel_constructor_exists():
    assert callable(devs::AtomicModel.__init__)


def test_devs::atomicmodel_constructor_args():
    sig = inspect.signature(devs::AtomicModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devs::atomicmodel_has_name():
    assert hasattr(devs::AtomicModel, "name")
    descriptor = None
    for klass in devs::AtomicModel.__mro__:
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
devs::InternalTransition_strategy = st.builds(
    devs::InternalTransition,
)
devs::ExternalTransition_strategy = st.builds(
    devs::ExternalTransition,
)
Event_strategy = st.builds(
    Event,
)
devs::OutputEvent_strategy = st.builds(
    devs::OutputEvent,
)
devs::InputEvent_strategy = st.builds(
    devs::InputEvent,
)
devs::OutputFunction_strategy = st.builds(
    devs::OutputFunction,
    name=
        safe_text
)
devs::Transition_strategy = st.builds(
    devs::Transition,
    name=
        safe_text
)
devs::Event_strategy = st.builds(
    devs::Event,
    name=
        safe_text
)
devs::State_strategy = st.builds(
    devs::State,
    lifeTime=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
devs::AtomicModel_strategy = st.builds(
    devs::AtomicModel,
    name=
        safe_text
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=devs::InternalTransition_strategy)
@settings(max_examples=50)
def test_devs::internaltransition_instantiation(instance):
    assert isinstance(instance, devs::InternalTransition)

@given(instance=devs::ExternalTransition_strategy)
@settings(max_examples=50)
def test_devs::externaltransition_instantiation(instance):
    assert isinstance(instance, devs::ExternalTransition)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=devs::OutputEvent_strategy)
@settings(max_examples=50)
def test_devs::outputevent_instantiation(instance):
    assert isinstance(instance, devs::OutputEvent)

@given(instance=devs::InputEvent_strategy)
@settings(max_examples=50)
def test_devs::inputevent_instantiation(instance):
    assert isinstance(instance, devs::InputEvent)

@given(instance=devs::OutputFunction_strategy)
@settings(max_examples=50)
def test_devs::outputfunction_instantiation(instance):
    assert isinstance(instance, devs::OutputFunction)

@given(instance=devs::OutputFunction_strategy)
def test_devs::outputfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=devs::OutputFunction_strategy)
def test_devs::outputfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=devs::Transition_strategy)
@settings(max_examples=50)
def test_devs::transition_instantiation(instance):
    assert isinstance(instance, devs::Transition)

@given(instance=devs::Transition_strategy)
def test_devs::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=devs::Transition_strategy)
def test_devs::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=devs::Event_strategy)
@settings(max_examples=50)
def test_devs::event_instantiation(instance):
    assert isinstance(instance, devs::Event)

@given(instance=devs::Event_strategy)
def test_devs::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=devs::Event_strategy)
def test_devs::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=devs::State_strategy)
@settings(max_examples=50)
def test_devs::state_instantiation(instance):
    assert isinstance(instance, devs::State)

@given(instance=devs::State_strategy)
def test_devs::state_lifeTime_type(instance):
    assert isinstance(instance.lifeTime, float)


@given(instance=devs::State_strategy)
def test_devs::state_lifeTime_setter(instance):
    original = instance.lifeTime
    instance.lifeTime = original
    assert instance.lifeTime == original

@given(instance=devs::State_strategy)
def test_devs::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=devs::State_strategy)
def test_devs::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=devs::AtomicModel_strategy)
@settings(max_examples=50)
def test_devs::atomicmodel_instantiation(instance):
    assert isinstance(instance, devs::AtomicModel)

@given(instance=devs::AtomicModel_strategy)
def test_devs::atomicmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=devs::AtomicModel_strategy)
def test_devs::atomicmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

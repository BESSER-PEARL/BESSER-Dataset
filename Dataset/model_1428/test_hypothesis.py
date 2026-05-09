import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractEvent,
    martinfowlerdsl::Event,
    martinfowlerdsl::Transition,
    martinfowlerdsl::Command,
    martinfowlerdsl::AbstractEvent,
    martinfowlerdsl::StateMachine,
    martinfowlerdsl::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractevent_is_not_abstract():
    assert not inspect.isabstract(AbstractEvent)


def test_abstractevent_constructor_exists():
    assert callable(AbstractEvent.__init__)


def test_abstractevent_constructor_args():
    sig = inspect.signature(AbstractEvent.__init__)
    params = list(sig.parameters.keys())



def test_martinfowlerdsl::event_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl::Event)


def test_martinfowlerdsl::event_constructor_exists():
    assert callable(martinfowlerdsl::Event.__init__)


def test_martinfowlerdsl::event_constructor_args():
    sig = inspect.signature(martinfowlerdsl::Event.__init__)
    params = list(sig.parameters.keys())
    assert "resetting" in params, "Missing parameter 'resetting'"

def test_martinfowlerdsl::event_has_resetting():
    assert hasattr(martinfowlerdsl::Event, "resetting")
    descriptor = None
    for klass in martinfowlerdsl::Event.__mro__:
        if "resetting" in klass.__dict__:
            descriptor = klass.__dict__["resetting"]
            break
    assert isinstance(descriptor, property)



def test_martinfowlerdsl::transition_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl::Transition)


def test_martinfowlerdsl::transition_constructor_exists():
    assert callable(martinfowlerdsl::Transition.__init__)


def test_martinfowlerdsl::transition_constructor_args():
    sig = inspect.signature(martinfowlerdsl::Transition.__init__)
    params = list(sig.parameters.keys())



def test_martinfowlerdsl::command_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl::Command)


def test_martinfowlerdsl::command_constructor_exists():
    assert callable(martinfowlerdsl::Command.__init__)


def test_martinfowlerdsl::command_constructor_args():
    sig = inspect.signature(martinfowlerdsl::Command.__init__)
    params = list(sig.parameters.keys())



def test_martinfowlerdsl::abstractevent_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl::AbstractEvent)


def test_martinfowlerdsl::abstractevent_constructor_exists():
    assert callable(martinfowlerdsl::AbstractEvent.__init__)


def test_martinfowlerdsl::abstractevent_constructor_args():
    sig = inspect.signature(martinfowlerdsl::AbstractEvent.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"

def test_martinfowlerdsl::abstractevent_has_code():
    assert hasattr(martinfowlerdsl::AbstractEvent, "code")
    descriptor = None
    for klass in martinfowlerdsl::AbstractEvent.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_martinfowlerdsl::abstractevent_has_name():
    assert hasattr(martinfowlerdsl::AbstractEvent, "name")
    descriptor = None
    for klass in martinfowlerdsl::AbstractEvent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_martinfowlerdsl::statemachine_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl::StateMachine)


def test_martinfowlerdsl::statemachine_constructor_exists():
    assert callable(martinfowlerdsl::StateMachine.__init__)


def test_martinfowlerdsl::statemachine_constructor_args():
    sig = inspect.signature(martinfowlerdsl::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_martinfowlerdsl::state_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl::State)


def test_martinfowlerdsl::state_constructor_exists():
    assert callable(martinfowlerdsl::State.__init__)


def test_martinfowlerdsl::state_constructor_args():
    sig = inspect.signature(martinfowlerdsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_martinfowlerdsl::state_has_name():
    assert hasattr(martinfowlerdsl::State, "name")
    descriptor = None
    for klass in martinfowlerdsl::State.__mro__:
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
AbstractEvent_strategy = st.builds(
    AbstractEvent,
)
martinfowlerdsl::Event_strategy = st.builds(
    martinfowlerdsl::Event,
    resetting=
        st.booleans()
)
martinfowlerdsl::Transition_strategy = st.builds(
    martinfowlerdsl::Transition,
)
martinfowlerdsl::Command_strategy = st.builds(
    martinfowlerdsl::Command,
)
martinfowlerdsl::AbstractEvent_strategy = st.builds(
    martinfowlerdsl::AbstractEvent,
    code=
        safe_text,
    name=
        safe_text
)
martinfowlerdsl::StateMachine_strategy = st.builds(
    martinfowlerdsl::StateMachine,
)
martinfowlerdsl::State_strategy = st.builds(
    martinfowlerdsl::State,
    name=
        safe_text
)

@given(instance=AbstractEvent_strategy)
@settings(max_examples=50)
def test_abstractevent_instantiation(instance):
    assert isinstance(instance, AbstractEvent)

@given(instance=martinfowlerdsl::Event_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl::event_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl::Event)

@given(instance=martinfowlerdsl::Event_strategy)
def test_martinfowlerdsl::event_resetting_type(instance):
    assert isinstance(instance.resetting, bool)


@given(instance=martinfowlerdsl::Event_strategy)
def test_martinfowlerdsl::event_resetting_setter(instance):
    original = instance.resetting
    instance.resetting = original
    assert instance.resetting == original

@given(instance=martinfowlerdsl::Transition_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl::transition_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl::Transition)

@given(instance=martinfowlerdsl::Command_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl::command_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl::Command)

@given(instance=martinfowlerdsl::AbstractEvent_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl::abstractevent_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl::AbstractEvent)

@given(instance=martinfowlerdsl::AbstractEvent_strategy)
def test_martinfowlerdsl::abstractevent_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=martinfowlerdsl::AbstractEvent_strategy)
def test_martinfowlerdsl::abstractevent_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=martinfowlerdsl::AbstractEvent_strategy)
def test_martinfowlerdsl::abstractevent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=martinfowlerdsl::AbstractEvent_strategy)
def test_martinfowlerdsl::abstractevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=martinfowlerdsl::StateMachine_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl::statemachine_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl::StateMachine)

@given(instance=martinfowlerdsl::State_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl::state_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl::State)

@given(instance=martinfowlerdsl::State_strategy)
def test_martinfowlerdsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=martinfowlerdsl::State_strategy)
def test_martinfowlerdsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

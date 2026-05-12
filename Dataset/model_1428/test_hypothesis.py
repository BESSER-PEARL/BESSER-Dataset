import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractEvent,
    martinfowlerdsl_Event,
    martinfowlerdsl_Transition,
    martinfowlerdsl_Command,
    martinfowlerdsl_AbstractEvent,
    martinfowlerdsl_StateMachine,
    martinfowlerdsl_State,
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



def test_martinfowlerdsl_event_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl_Event)


def test_martinfowlerdsl_event_constructor_exists():
    assert callable(martinfowlerdsl_Event.__init__)


def test_martinfowlerdsl_event_constructor_args():
    sig = inspect.signature(martinfowlerdsl_Event.__init__)
    params = list(sig.parameters.keys())
    assert "resetting" in params, "Missing parameter 'resetting'"

def test_martinfowlerdsl_event_has_resetting():
    assert hasattr(martinfowlerdsl_Event, "resetting")
    descriptor = None
    for klass in martinfowlerdsl_Event.__mro__:
        if "resetting" in klass.__dict__:
            descriptor = klass.__dict__["resetting"]
            break
    assert isinstance(descriptor, property)



def test_martinfowlerdsl_transition_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl_Transition)


def test_martinfowlerdsl_transition_constructor_exists():
    assert callable(martinfowlerdsl_Transition.__init__)


def test_martinfowlerdsl_transition_constructor_args():
    sig = inspect.signature(martinfowlerdsl_Transition.__init__)
    params = list(sig.parameters.keys())



def test_martinfowlerdsl_command_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl_Command)


def test_martinfowlerdsl_command_constructor_exists():
    assert callable(martinfowlerdsl_Command.__init__)


def test_martinfowlerdsl_command_constructor_args():
    sig = inspect.signature(martinfowlerdsl_Command.__init__)
    params = list(sig.parameters.keys())



def test_martinfowlerdsl_abstractevent_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl_AbstractEvent)


def test_martinfowlerdsl_abstractevent_constructor_exists():
    assert callable(martinfowlerdsl_AbstractEvent.__init__)


def test_martinfowlerdsl_abstractevent_constructor_args():
    sig = inspect.signature(martinfowlerdsl_AbstractEvent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "code" in params, "Missing parameter 'code'"

def test_martinfowlerdsl_abstractevent_has_name():
    assert hasattr(martinfowlerdsl_AbstractEvent, "name")
    descriptor = None
    for klass in martinfowlerdsl_AbstractEvent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_martinfowlerdsl_abstractevent_has_code():
    assert hasattr(martinfowlerdsl_AbstractEvent, "code")
    descriptor = None
    for klass in martinfowlerdsl_AbstractEvent.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_martinfowlerdsl_statemachine_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl_StateMachine)


def test_martinfowlerdsl_statemachine_constructor_exists():
    assert callable(martinfowlerdsl_StateMachine.__init__)


def test_martinfowlerdsl_statemachine_constructor_args():
    sig = inspect.signature(martinfowlerdsl_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_martinfowlerdsl_state_is_not_abstract():
    assert not inspect.isabstract(martinfowlerdsl_State)


def test_martinfowlerdsl_state_constructor_exists():
    assert callable(martinfowlerdsl_State.__init__)


def test_martinfowlerdsl_state_constructor_args():
    sig = inspect.signature(martinfowlerdsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_martinfowlerdsl_state_has_name():
    assert hasattr(martinfowlerdsl_State, "name")
    descriptor = None
    for klass in martinfowlerdsl_State.__mro__:
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
martinfowlerdsl_Event_strategy = st.builds(
    martinfowlerdsl_Event,
    resetting=
        st.booleans()
)
martinfowlerdsl_Transition_strategy = st.builds(
    martinfowlerdsl_Transition,
)
martinfowlerdsl_Command_strategy = st.builds(
    martinfowlerdsl_Command,
)
martinfowlerdsl_AbstractEvent_strategy = st.builds(
    martinfowlerdsl_AbstractEvent,
    name=
        safe_text,
    code=
        safe_text
)
martinfowlerdsl_StateMachine_strategy = st.builds(
    martinfowlerdsl_StateMachine,
)
martinfowlerdsl_State_strategy = st.builds(
    martinfowlerdsl_State,
    name=
        safe_text
)

@given(instance=AbstractEvent_strategy)
@settings(max_examples=50)
def test_abstractevent_instantiation(instance):
    assert isinstance(instance, AbstractEvent)

@given(instance=martinfowlerdsl_Event_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl_event_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl_Event)



@given(instance=martinfowlerdsl_Event_strategy)
def test_martinfowlerdsl_event_resetting_setter(instance):
    original = instance.resetting
    instance.resetting = original
    assert instance.resetting == original

@given(instance=martinfowlerdsl_Transition_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl_transition_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl_Transition)

@given(instance=martinfowlerdsl_Command_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl_command_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl_Command)

@given(instance=martinfowlerdsl_AbstractEvent_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl_abstractevent_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl_AbstractEvent)



@given(instance=martinfowlerdsl_AbstractEvent_strategy)
def test_martinfowlerdsl_abstractevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=martinfowlerdsl_AbstractEvent_strategy)
def test_martinfowlerdsl_abstractevent_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=martinfowlerdsl_StateMachine_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl_statemachine_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl_StateMachine)

@given(instance=martinfowlerdsl_State_strategy)
@settings(max_examples=50)
def test_martinfowlerdsl_state_instantiation(instance):
    assert isinstance(instance, martinfowlerdsl_State)



@given(instance=martinfowlerdsl_State_strategy)
def test_martinfowlerdsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

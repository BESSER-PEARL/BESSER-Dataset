import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_State,
    myDsl_Transition,
    myDsl_XExpression,
    myDsl_JvmTypeReference,
    myDsl_Service,
    myDsl_Event,
    myDsl_Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_state_is_not_abstract():
    assert not inspect.isabstract(myDsl_State)


def test_mydsl_state_constructor_exists():
    assert callable(myDsl_State.__init__)


def test_mydsl_state_constructor_args():
    sig = inspect.signature(myDsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_state_has_name():
    assert hasattr(myDsl_State, "name")
    descriptor = None
    for klass in myDsl_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_transition_is_not_abstract():
    assert not inspect.isabstract(myDsl_Transition)


def test_mydsl_transition_constructor_exists():
    assert callable(myDsl_Transition.__init__)


def test_mydsl_transition_constructor_args():
    sig = inspect.signature(myDsl_Transition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_xexpression_is_not_abstract():
    assert not inspect.isabstract(myDsl_XExpression)


def test_mydsl_xexpression_constructor_exists():
    assert callable(myDsl_XExpression.__init__)


def test_mydsl_xexpression_constructor_args():
    sig = inspect.signature(myDsl_XExpression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_jvmtypereference_is_not_abstract():
    assert not inspect.isabstract(myDsl_JvmTypeReference)


def test_mydsl_jvmtypereference_constructor_exists():
    assert callable(myDsl_JvmTypeReference.__init__)


def test_mydsl_jvmtypereference_constructor_args():
    sig = inspect.signature(myDsl_JvmTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_service_is_not_abstract():
    assert not inspect.isabstract(myDsl_Service)


def test_mydsl_service_constructor_exists():
    assert callable(myDsl_Service.__init__)


def test_mydsl_service_constructor_args():
    sig = inspect.signature(myDsl_Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_service_has_name():
    assert hasattr(myDsl_Service, "name")
    descriptor = None
    for klass in myDsl_Service.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_event_is_not_abstract():
    assert not inspect.isabstract(myDsl_Event)


def test_mydsl_event_constructor_exists():
    assert callable(myDsl_Event.__init__)


def test_mydsl_event_constructor_args():
    sig = inspect.signature(myDsl_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "resetEvent" in params, "Missing parameter 'resetEvent'"

def test_mydsl_event_has_name():
    assert hasattr(myDsl_Event, "name")
    descriptor = None
    for klass in myDsl_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_event_has_resetEvent():
    assert hasattr(myDsl_Event, "resetEvent")
    descriptor = None
    for klass in myDsl_Event.__mro__:
        if "resetEvent" in klass.__dict__:
            descriptor = klass.__dict__["resetEvent"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_statemachine_is_not_abstract():
    assert not inspect.isabstract(myDsl_Statemachine)


def test_mydsl_statemachine_constructor_exists():
    assert callable(myDsl_Statemachine.__init__)


def test_mydsl_statemachine_constructor_args():
    sig = inspect.signature(myDsl_Statemachine.__init__)
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
myDsl_State_strategy = st.builds(
    myDsl_State,
    name=
        safe_text
)
myDsl_Transition_strategy = st.builds(
    myDsl_Transition,
)
myDsl_XExpression_strategy = st.builds(
    myDsl_XExpression,
)
myDsl_JvmTypeReference_strategy = st.builds(
    myDsl_JvmTypeReference,
)
myDsl_Service_strategy = st.builds(
    myDsl_Service,
    name=
        safe_text
)
myDsl_Event_strategy = st.builds(
    myDsl_Event,
    name=
        safe_text,
    resetEvent=
        st.booleans()
)
myDsl_Statemachine_strategy = st.builds(
    myDsl_Statemachine,
)

@given(instance=myDsl_State_strategy)
@settings(max_examples=50)
def test_mydsl_state_instantiation(instance):
    assert isinstance(instance, myDsl_State)



@given(instance=myDsl_State_strategy)
def test_mydsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Transition_strategy)
@settings(max_examples=50)
def test_mydsl_transition_instantiation(instance):
    assert isinstance(instance, myDsl_Transition)

@given(instance=myDsl_XExpression_strategy)
@settings(max_examples=50)
def test_mydsl_xexpression_instantiation(instance):
    assert isinstance(instance, myDsl_XExpression)

@given(instance=myDsl_JvmTypeReference_strategy)
@settings(max_examples=50)
def test_mydsl_jvmtypereference_instantiation(instance):
    assert isinstance(instance, myDsl_JvmTypeReference)

@given(instance=myDsl_Service_strategy)
@settings(max_examples=50)
def test_mydsl_service_instantiation(instance):
    assert isinstance(instance, myDsl_Service)



@given(instance=myDsl_Service_strategy)
def test_mydsl_service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Event_strategy)
@settings(max_examples=50)
def test_mydsl_event_instantiation(instance):
    assert isinstance(instance, myDsl_Event)



@given(instance=myDsl_Event_strategy)
def test_mydsl_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Event_strategy)
def test_mydsl_event_resetEvent_setter(instance):
    original = instance.resetEvent
    instance.resetEvent = original
    assert instance.resetEvent == original

@given(instance=myDsl_Statemachine_strategy)
@settings(max_examples=50)
def test_mydsl_statemachine_instantiation(instance):
    assert isinstance(instance, myDsl_Statemachine)

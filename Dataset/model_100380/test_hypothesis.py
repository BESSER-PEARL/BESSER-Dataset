import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::State,
    myDsl::Transition,
    myDsl::XExpression,
    myDsl::JvmTypeReference,
    myDsl::Service,
    myDsl::Event,
    myDsl::Statemachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::state_is_not_abstract():
    assert not inspect.isabstract(myDsl::State)


def test_mydsl::state_constructor_exists():
    assert callable(myDsl::State.__init__)


def test_mydsl::state_constructor_args():
    sig = inspect.signature(myDsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::state_has_name():
    assert hasattr(myDsl::State, "name")
    descriptor = None
    for klass in myDsl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::transition_is_not_abstract():
    assert not inspect.isabstract(myDsl::Transition)


def test_mydsl::transition_constructor_exists():
    assert callable(myDsl::Transition.__init__)


def test_mydsl::transition_constructor_args():
    sig = inspect.signature(myDsl::Transition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::xexpression_is_not_abstract():
    assert not inspect.isabstract(myDsl::XExpression)


def test_mydsl::xexpression_constructor_exists():
    assert callable(myDsl::XExpression.__init__)


def test_mydsl::xexpression_constructor_args():
    sig = inspect.signature(myDsl::XExpression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::jvmtypereference_is_not_abstract():
    assert not inspect.isabstract(myDsl::JvmTypeReference)


def test_mydsl::jvmtypereference_constructor_exists():
    assert callable(myDsl::JvmTypeReference.__init__)


def test_mydsl::jvmtypereference_constructor_args():
    sig = inspect.signature(myDsl::JvmTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::service_is_not_abstract():
    assert not inspect.isabstract(myDsl::Service)


def test_mydsl::service_constructor_exists():
    assert callable(myDsl::Service.__init__)


def test_mydsl::service_constructor_args():
    sig = inspect.signature(myDsl::Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::service_has_name():
    assert hasattr(myDsl::Service, "name")
    descriptor = None
    for klass in myDsl::Service.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::event_is_not_abstract():
    assert not inspect.isabstract(myDsl::Event)


def test_mydsl::event_constructor_exists():
    assert callable(myDsl::Event.__init__)


def test_mydsl::event_constructor_args():
    sig = inspect.signature(myDsl::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "resetEvent" in params, "Missing parameter 'resetEvent'"

def test_mydsl::event_has_name():
    assert hasattr(myDsl::Event, "name")
    descriptor = None
    for klass in myDsl::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::event_has_resetEvent():
    assert hasattr(myDsl::Event, "resetEvent")
    descriptor = None
    for klass in myDsl::Event.__mro__:
        if "resetEvent" in klass.__dict__:
            descriptor = klass.__dict__["resetEvent"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::statemachine_is_not_abstract():
    assert not inspect.isabstract(myDsl::Statemachine)


def test_mydsl::statemachine_constructor_exists():
    assert callable(myDsl::Statemachine.__init__)


def test_mydsl::statemachine_constructor_args():
    sig = inspect.signature(myDsl::Statemachine.__init__)
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
myDsl::State_strategy = st.builds(
    myDsl::State,
    name=
        safe_text
)
myDsl::Transition_strategy = st.builds(
    myDsl::Transition,
)
myDsl::XExpression_strategy = st.builds(
    myDsl::XExpression,
)
myDsl::JvmTypeReference_strategy = st.builds(
    myDsl::JvmTypeReference,
)
myDsl::Service_strategy = st.builds(
    myDsl::Service,
    name=
        safe_text
)
myDsl::Event_strategy = st.builds(
    myDsl::Event,
    name=
        safe_text,
    resetEvent=
        st.booleans()
)
myDsl::Statemachine_strategy = st.builds(
    myDsl::Statemachine,
)

@given(instance=myDsl::State_strategy)
@settings(max_examples=50)
def test_mydsl::state_instantiation(instance):
    assert isinstance(instance, myDsl::State)

@given(instance=myDsl::State_strategy)
def test_mydsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::State_strategy)
def test_mydsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Transition_strategy)
@settings(max_examples=50)
def test_mydsl::transition_instantiation(instance):
    assert isinstance(instance, myDsl::Transition)

@given(instance=myDsl::XExpression_strategy)
@settings(max_examples=50)
def test_mydsl::xexpression_instantiation(instance):
    assert isinstance(instance, myDsl::XExpression)

@given(instance=myDsl::JvmTypeReference_strategy)
@settings(max_examples=50)
def test_mydsl::jvmtypereference_instantiation(instance):
    assert isinstance(instance, myDsl::JvmTypeReference)

@given(instance=myDsl::Service_strategy)
@settings(max_examples=50)
def test_mydsl::service_instantiation(instance):
    assert isinstance(instance, myDsl::Service)

@given(instance=myDsl::Service_strategy)
def test_mydsl::service_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Service_strategy)
def test_mydsl::service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Event_strategy)
@settings(max_examples=50)
def test_mydsl::event_instantiation(instance):
    assert isinstance(instance, myDsl::Event)

@given(instance=myDsl::Event_strategy)
def test_mydsl::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Event_strategy)
def test_mydsl::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Event_strategy)
def test_mydsl::event_resetEvent_type(instance):
    assert isinstance(instance.resetEvent, bool)


@given(instance=myDsl::Event_strategy)
def test_mydsl::event_resetEvent_setter(instance):
    original = instance.resetEvent
    instance.resetEvent = original
    assert instance.resetEvent == original

@given(instance=myDsl::Statemachine_strategy)
@settings(max_examples=50)
def test_mydsl::statemachine_instantiation(instance):
    assert isinstance(instance, myDsl::Statemachine)

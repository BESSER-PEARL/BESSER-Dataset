import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    StateMachineDiagram::meta::Event,
    StateMachineDiagram::meta::Fragment,
    StateMachineDiagram::meta::Activity,
    Vertex,
    StateMachineDiagram::meta::State,
    StateMachineDiagram::meta::Pseudostate,
    StateMachineDiagram::meta::Transition,
    StateMachineDiagram::meta::Vertex,
    StateMachineDiagram::meta::StateMachine,
    StateMachineDiagram::meta::Application,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachinediagram::meta::event_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::meta::Event)


def test_statemachinediagram::meta::event_constructor_exists():
    assert callable(StateMachineDiagram::meta::Event.__init__)


def test_statemachinediagram::meta::event_constructor_args():
    sig = inspect.signature(StateMachineDiagram::meta::Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachinediagram::meta::fragment_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::meta::Fragment)


def test_statemachinediagram::meta::fragment_constructor_exists():
    assert callable(StateMachineDiagram::meta::Fragment.__init__)


def test_statemachinediagram::meta::fragment_constructor_args():
    sig = inspect.signature(StateMachineDiagram::meta::Fragment.__init__)
    params = list(sig.parameters.keys())



def test_statemachinediagram::meta::activity_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::meta::Activity)


def test_statemachinediagram::meta::activity_constructor_exists():
    assert callable(StateMachineDiagram::meta::Activity.__init__)


def test_statemachinediagram::meta::activity_constructor_args():
    sig = inspect.signature(StateMachineDiagram::meta::Activity.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachinediagram::meta::state_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::meta::State)


def test_statemachinediagram::meta::state_constructor_exists():
    assert callable(StateMachineDiagram::meta::State.__init__)


def test_statemachinediagram::meta::state_constructor_args():
    sig = inspect.signature(StateMachineDiagram::meta::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinediagram::meta::state_has_name():
    assert hasattr(StateMachineDiagram::meta::State, "name")
    descriptor = None
    for klass in StateMachineDiagram::meta::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinediagram::meta::pseudostate_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::meta::Pseudostate)


def test_statemachinediagram::meta::pseudostate_constructor_exists():
    assert callable(StateMachineDiagram::meta::Pseudostate.__init__)


def test_statemachinediagram::meta::pseudostate_constructor_args():
    sig = inspect.signature(StateMachineDiagram::meta::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_statemachinediagram::meta::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::meta::Transition)


def test_statemachinediagram::meta::transition_constructor_exists():
    assert callable(StateMachineDiagram::meta::Transition.__init__)


def test_statemachinediagram::meta::transition_constructor_args():
    sig = inspect.signature(StateMachineDiagram::meta::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_statemachinediagram::meta::transition_has_name():
    assert hasattr(StateMachineDiagram::meta::Transition, "name")
    descriptor = None
    for klass in StateMachineDiagram::meta::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statemachinediagram::meta::transition_has_trigger():
    assert hasattr(StateMachineDiagram::meta::Transition, "trigger")
    descriptor = None
    for klass in StateMachineDiagram::meta::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_statemachinediagram::meta::vertex_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::meta::Vertex)


def test_statemachinediagram::meta::vertex_constructor_exists():
    assert callable(StateMachineDiagram::meta::Vertex.__init__)


def test_statemachinediagram::meta::vertex_constructor_args():
    sig = inspect.signature(StateMachineDiagram::meta::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachinediagram::meta::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::meta::StateMachine)


def test_statemachinediagram::meta::statemachine_constructor_exists():
    assert callable(StateMachineDiagram::meta::StateMachine.__init__)


def test_statemachinediagram::meta::statemachine_constructor_args():
    sig = inspect.signature(StateMachineDiagram::meta::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinediagram::meta::statemachine_has_name():
    assert hasattr(StateMachineDiagram::meta::StateMachine, "name")
    descriptor = None
    for klass in StateMachineDiagram::meta::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinediagram::meta::application_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::meta::Application)


def test_statemachinediagram::meta::application_constructor_exists():
    assert callable(StateMachineDiagram::meta::Application.__init__)


def test_statemachinediagram::meta::application_constructor_args():
    sig = inspect.signature(StateMachineDiagram::meta::Application.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinediagram::meta::application_has_name():
    assert hasattr(StateMachineDiagram::meta::Application, "name")
    descriptor = None
    for klass in StateMachineDiagram::meta::Application.__mro__:
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
State_strategy = st.builds(
    State,
)
StateMachineDiagram::meta::Event_strategy = st.builds(
    StateMachineDiagram::meta::Event,
)
StateMachineDiagram::meta::Fragment_strategy = st.builds(
    StateMachineDiagram::meta::Fragment,
)
StateMachineDiagram::meta::Activity_strategy = st.builds(
    StateMachineDiagram::meta::Activity,
)
Vertex_strategy = st.builds(
    Vertex,
)
StateMachineDiagram::meta::State_strategy = st.builds(
    StateMachineDiagram::meta::State,
    name=
        safe_text
)
StateMachineDiagram::meta::Pseudostate_strategy = st.builds(
    StateMachineDiagram::meta::Pseudostate,
)
StateMachineDiagram::meta::Transition_strategy = st.builds(
    StateMachineDiagram::meta::Transition,
    name=
        safe_text,
    trigger=
        safe_text
)
StateMachineDiagram::meta::Vertex_strategy = st.builds(
    StateMachineDiagram::meta::Vertex,
)
StateMachineDiagram::meta::StateMachine_strategy = st.builds(
    StateMachineDiagram::meta::StateMachine,
    name=
        safe_text
)
StateMachineDiagram::meta::Application_strategy = st.builds(
    StateMachineDiagram::meta::Application,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachineDiagram::meta::Event_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::event_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::meta::Event)

@given(instance=StateMachineDiagram::meta::Fragment_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::fragment_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::meta::Fragment)

@given(instance=StateMachineDiagram::meta::Activity_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::activity_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::meta::Activity)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=StateMachineDiagram::meta::State_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::state_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::meta::State)

@given(instance=StateMachineDiagram::meta::State_strategy)
def test_statemachinediagram::meta::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineDiagram::meta::State_strategy)
def test_statemachinediagram::meta::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineDiagram::meta::Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::pseudostate_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::meta::Pseudostate)

@given(instance=StateMachineDiagram::meta::Transition_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::transition_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::meta::Transition)

@given(instance=StateMachineDiagram::meta::Transition_strategy)
def test_statemachinediagram::meta::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineDiagram::meta::Transition_strategy)
def test_statemachinediagram::meta::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineDiagram::meta::Transition_strategy)
def test_statemachinediagram::meta::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=StateMachineDiagram::meta::Transition_strategy)
def test_statemachinediagram::meta::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=StateMachineDiagram::meta::Vertex_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::vertex_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::meta::Vertex)

@given(instance=StateMachineDiagram::meta::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::meta::StateMachine)

@given(instance=StateMachineDiagram::meta::StateMachine_strategy)
def test_statemachinediagram::meta::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineDiagram::meta::StateMachine_strategy)
def test_statemachinediagram::meta::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineDiagram::meta::Application_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::application_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::meta::Application)

@given(instance=StateMachineDiagram::meta::Application_strategy)
def test_statemachinediagram::meta::application_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineDiagram::meta::Application_strategy)
def test_statemachinediagram::meta::application_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

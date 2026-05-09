import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    StateMachineDiagram::Meta::Event,
    StateMachineDiagram::Meta::Screen,
    Vertex,
    StateMachineDiagram::Meta::State,
    StateMachineDiagram::Meta::Pseudostate,
    StateMachineDiagram::Meta::Transition,
    StateMachineDiagram::Meta::Vertex,
    StateMachineDiagram::Meta::StateMachine,
    StateMachineDiagram::Meta::Application,
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
    assert not inspect.isabstract(StateMachineDiagram::Meta::Event)


def test_statemachinediagram::meta::event_constructor_exists():
    assert callable(StateMachineDiagram::Meta::Event.__init__)


def test_statemachinediagram::meta::event_constructor_args():
    sig = inspect.signature(StateMachineDiagram::Meta::Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachinediagram::meta::screen_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::Meta::Screen)


def test_statemachinediagram::meta::screen_constructor_exists():
    assert callable(StateMachineDiagram::Meta::Screen.__init__)


def test_statemachinediagram::meta::screen_constructor_args():
    sig = inspect.signature(StateMachineDiagram::Meta::Screen.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachinediagram::meta::state_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::Meta::State)


def test_statemachinediagram::meta::state_constructor_exists():
    assert callable(StateMachineDiagram::Meta::State.__init__)


def test_statemachinediagram::meta::state_constructor_args():
    sig = inspect.signature(StateMachineDiagram::Meta::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinediagram::meta::state_has_name():
    assert hasattr(StateMachineDiagram::Meta::State, "name")
    descriptor = None
    for klass in StateMachineDiagram::Meta::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinediagram::meta::pseudostate_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::Meta::Pseudostate)


def test_statemachinediagram::meta::pseudostate_constructor_exists():
    assert callable(StateMachineDiagram::Meta::Pseudostate.__init__)


def test_statemachinediagram::meta::pseudostate_constructor_args():
    sig = inspect.signature(StateMachineDiagram::Meta::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_statemachinediagram::meta::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::Meta::Transition)


def test_statemachinediagram::meta::transition_constructor_exists():
    assert callable(StateMachineDiagram::Meta::Transition.__init__)


def test_statemachinediagram::meta::transition_constructor_args():
    sig = inspect.signature(StateMachineDiagram::Meta::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinediagram::meta::transition_has_trigger():
    assert hasattr(StateMachineDiagram::Meta::Transition, "trigger")
    descriptor = None
    for klass in StateMachineDiagram::Meta::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_statemachinediagram::meta::transition_has_name():
    assert hasattr(StateMachineDiagram::Meta::Transition, "name")
    descriptor = None
    for klass in StateMachineDiagram::Meta::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinediagram::meta::vertex_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::Meta::Vertex)


def test_statemachinediagram::meta::vertex_constructor_exists():
    assert callable(StateMachineDiagram::Meta::Vertex.__init__)


def test_statemachinediagram::meta::vertex_constructor_args():
    sig = inspect.signature(StateMachineDiagram::Meta::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachinediagram::meta::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::Meta::StateMachine)


def test_statemachinediagram::meta::statemachine_constructor_exists():
    assert callable(StateMachineDiagram::Meta::StateMachine.__init__)


def test_statemachinediagram::meta::statemachine_constructor_args():
    sig = inspect.signature(StateMachineDiagram::Meta::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinediagram::meta::statemachine_has_name():
    assert hasattr(StateMachineDiagram::Meta::StateMachine, "name")
    descriptor = None
    for klass in StateMachineDiagram::Meta::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachinediagram::meta::application_is_not_abstract():
    assert not inspect.isabstract(StateMachineDiagram::Meta::Application)


def test_statemachinediagram::meta::application_constructor_exists():
    assert callable(StateMachineDiagram::Meta::Application.__init__)


def test_statemachinediagram::meta::application_constructor_args():
    sig = inspect.signature(StateMachineDiagram::Meta::Application.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachinediagram::meta::application_has_name():
    assert hasattr(StateMachineDiagram::Meta::Application, "name")
    descriptor = None
    for klass in StateMachineDiagram::Meta::Application.__mro__:
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
StateMachineDiagram::Meta::Event_strategy = st.builds(
    StateMachineDiagram::Meta::Event,
)
StateMachineDiagram::Meta::Screen_strategy = st.builds(
    StateMachineDiagram::Meta::Screen,
)
Vertex_strategy = st.builds(
    Vertex,
)
StateMachineDiagram::Meta::State_strategy = st.builds(
    StateMachineDiagram::Meta::State,
    name=
        safe_text
)
StateMachineDiagram::Meta::Pseudostate_strategy = st.builds(
    StateMachineDiagram::Meta::Pseudostate,
)
StateMachineDiagram::Meta::Transition_strategy = st.builds(
    StateMachineDiagram::Meta::Transition,
    trigger=
        safe_text,
    name=
        safe_text
)
StateMachineDiagram::Meta::Vertex_strategy = st.builds(
    StateMachineDiagram::Meta::Vertex,
)
StateMachineDiagram::Meta::StateMachine_strategy = st.builds(
    StateMachineDiagram::Meta::StateMachine,
    name=
        safe_text
)
StateMachineDiagram::Meta::Application_strategy = st.builds(
    StateMachineDiagram::Meta::Application,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachineDiagram::Meta::Event_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::event_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::Meta::Event)

@given(instance=StateMachineDiagram::Meta::Screen_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::screen_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::Meta::Screen)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=StateMachineDiagram::Meta::State_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::state_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::Meta::State)

@given(instance=StateMachineDiagram::Meta::State_strategy)
def test_statemachinediagram::meta::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineDiagram::Meta::State_strategy)
def test_statemachinediagram::meta::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineDiagram::Meta::Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::pseudostate_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::Meta::Pseudostate)

@given(instance=StateMachineDiagram::Meta::Transition_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::transition_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::Meta::Transition)

@given(instance=StateMachineDiagram::Meta::Transition_strategy)
def test_statemachinediagram::meta::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=StateMachineDiagram::Meta::Transition_strategy)
def test_statemachinediagram::meta::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=StateMachineDiagram::Meta::Transition_strategy)
def test_statemachinediagram::meta::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineDiagram::Meta::Transition_strategy)
def test_statemachinediagram::meta::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineDiagram::Meta::Vertex_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::vertex_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::Meta::Vertex)

@given(instance=StateMachineDiagram::Meta::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::Meta::StateMachine)

@given(instance=StateMachineDiagram::Meta::StateMachine_strategy)
def test_statemachinediagram::meta::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineDiagram::Meta::StateMachine_strategy)
def test_statemachinediagram::meta::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachineDiagram::Meta::Application_strategy)
@settings(max_examples=50)
def test_statemachinediagram::meta::application_instantiation(instance):
    assert isinstance(instance, StateMachineDiagram::Meta::Application)

@given(instance=StateMachineDiagram::Meta::Application_strategy)
def test_statemachinediagram::meta::application_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachineDiagram::Meta::Application_strategy)
def test_statemachinediagram::meta::application_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

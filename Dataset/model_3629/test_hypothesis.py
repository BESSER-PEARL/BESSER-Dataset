import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateChart::Transient,
    stateChart::Region,
    State,
    stateChart::CompositeState,
    stateChart::FinalState,
    stateChart::SimpleState,
    Vertex,
    stateChart::State,
    stateChart::PseudoState,
    stateChart::Vertex,
    stateChart::StateMachine,
    PseudoStateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechart::transient_is_not_abstract():
    assert not inspect.isabstract(stateChart::Transient)


def test_statechart::transient_constructor_exists():
    assert callable(stateChart::Transient.__init__)


def test_statechart::transient_constructor_args():
    sig = inspect.signature(stateChart::Transient.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"
    assert "name" in params, "Missing parameter 'name'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_statechart::transient_has_guard():
    assert hasattr(stateChart::Transient, "guard")
    descriptor = None
    for klass in stateChart::Transient.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_statechart::transient_has_name():
    assert hasattr(stateChart::Transient, "name")
    descriptor = None
    for klass in stateChart::Transient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart::transient_has_priority():
    assert hasattr(stateChart::Transient, "priority")
    descriptor = None
    for klass in stateChart::Transient.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_statechart::transient_has_effect():
    assert hasattr(stateChart::Transient, "effect")
    descriptor = None
    for klass in stateChart::Transient.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_statechart::transient_has_trigger():
    assert hasattr(stateChart::Transient, "trigger")
    descriptor = None
    for klass in stateChart::Transient.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_statechart::region_is_not_abstract():
    assert not inspect.isabstract(stateChart::Region)


def test_statechart::region_constructor_exists():
    assert callable(stateChart::Region.__init__)


def test_statechart::region_constructor_args():
    sig = inspect.signature(stateChart::Region.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"
    assert "name" in params, "Missing parameter 'name'"

def test_statechart::region_has_note():
    assert hasattr(stateChart::Region, "note")
    descriptor = None
    for klass in stateChart::Region.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_statechart::region_has_name():
    assert hasattr(stateChart::Region, "name")
    descriptor = None
    for klass in stateChart::Region.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statechart::compositestate_is_not_abstract():
    assert not inspect.isabstract(stateChart::CompositeState)


def test_statechart::compositestate_constructor_exists():
    assert callable(stateChart::CompositeState.__init__)


def test_statechart::compositestate_constructor_args():
    sig = inspect.signature(stateChart::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statechart::finalstate_is_not_abstract():
    assert not inspect.isabstract(stateChart::FinalState)


def test_statechart::finalstate_constructor_exists():
    assert callable(stateChart::FinalState.__init__)


def test_statechart::finalstate_constructor_args():
    sig = inspect.signature(stateChart::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statechart::simplestate_is_not_abstract():
    assert not inspect.isabstract(stateChart::SimpleState)


def test_statechart::simplestate_constructor_exists():
    assert callable(stateChart::SimpleState.__init__)


def test_statechart::simplestate_constructor_args():
    sig = inspect.signature(stateChart::SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statechart::state_is_not_abstract():
    assert not inspect.isabstract(stateChart::State)


def test_statechart::state_constructor_exists():
    assert callable(stateChart::State.__init__)


def test_statechart::state_constructor_args():
    sig = inspect.signature(stateChart::State.__init__)
    params = list(sig.parameters.keys())
    assert "exit" in params, "Missing parameter 'exit'"
    assert "action" in params, "Missing parameter 'action'"
    assert "entry" in params, "Missing parameter 'entry'"

def test_statechart::state_has_exit():
    assert hasattr(stateChart::State, "exit")
    descriptor = None
    for klass in stateChart::State.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)

def test_statechart::state_has_action():
    assert hasattr(stateChart::State, "action")
    descriptor = None
    for klass in stateChart::State.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_statechart::state_has_entry():
    assert hasattr(stateChart::State, "entry")
    descriptor = None
    for klass in stateChart::State.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)



def test_statechart::pseudostate_is_not_abstract():
    assert not inspect.isabstract(stateChart::PseudoState)


def test_statechart::pseudostate_constructor_exists():
    assert callable(stateChart::PseudoState.__init__)


def test_statechart::pseudostate_constructor_args():
    sig = inspect.signature(stateChart::PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "PseudoStateType" in params, "Missing parameter 'PseudoStateType'"

def test_statechart::pseudostate_has_PseudoStateType():
    assert hasattr(stateChart::PseudoState, "PseudoStateType")
    descriptor = None
    for klass in stateChart::PseudoState.__mro__:
        if "PseudoStateType" in klass.__dict__:
            descriptor = klass.__dict__["PseudoStateType"]
            break
    assert isinstance(descriptor, property)



def test_statechart::vertex_is_not_abstract():
    assert not inspect.isabstract(stateChart::Vertex)


def test_statechart::vertex_constructor_exists():
    assert callable(stateChart::Vertex.__init__)


def test_statechart::vertex_constructor_args():
    sig = inspect.signature(stateChart::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "note" in params, "Missing parameter 'note'"
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_statechart::vertex_has_name():
    assert hasattr(stateChart::Vertex, "name")
    descriptor = None
    for klass in stateChart::Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart::vertex_has_note():
    assert hasattr(stateChart::Vertex, "note")
    descriptor = None
    for klass in stateChart::Vertex.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_statechart::vertex_has_isActive():
    assert hasattr(stateChart::Vertex, "isActive")
    descriptor = None
    for klass in stateChart::Vertex.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_statechart::statemachine_is_not_abstract():
    assert not inspect.isabstract(stateChart::StateMachine)


def test_statechart::statemachine_constructor_exists():
    assert callable(stateChart::StateMachine.__init__)


def test_statechart::statemachine_constructor_args():
    sig = inspect.signature(stateChart::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart::statemachine_has_name():
    assert hasattr(stateChart::StateMachine, "name")
    descriptor = None
    for klass in stateChart::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pseudostatetype_exists():
    # Check that the Enumeration exists
    assert PseudoStateType is not None

def test_pseudostatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoStateType]
    expected_literals = [
        "Fork",
        "EntryPoint",
        "Join",
        "ShadowHistory",
        "Terminate",
        "Initial",
        "Junction",
        "DeepHistory",
        "Choice",
        "ExitPoint",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudoStateType"


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
stateChart::Transient_strategy = st.builds(
    stateChart::Transient,
    guard=
        safe_text,
    name=
        safe_text,
    priority=
        st.integers(),
    effect=
        safe_text,
    trigger=
        safe_text
)
stateChart::Region_strategy = st.builds(
    stateChart::Region,
    note=
        safe_text,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
stateChart::CompositeState_strategy = st.builds(
    stateChart::CompositeState,
)
stateChart::FinalState_strategy = st.builds(
    stateChart::FinalState,
)
stateChart::SimpleState_strategy = st.builds(
    stateChart::SimpleState,
)
Vertex_strategy = st.builds(
    Vertex,
)
stateChart::State_strategy = st.builds(
    stateChart::State,
    exit=
        safe_text,
    action=
        safe_text,
    entry=
        safe_text
)
stateChart::PseudoState_strategy = st.builds(
    stateChart::PseudoState,
    PseudoStateType=
        safe_text
)
stateChart::Vertex_strategy = st.builds(
    stateChart::Vertex,
    name=
        safe_text,
    note=
        safe_text,
    isActive=
        st.booleans()
)
stateChart::StateMachine_strategy = st.builds(
    stateChart::StateMachine,
    name=
        safe_text
)

@given(instance=stateChart::Transient_strategy)
@settings(max_examples=50)
def test_statechart::transient_instantiation(instance):
    assert isinstance(instance, stateChart::Transient)

@given(instance=stateChart::Transient_strategy)
def test_statechart::transient_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=stateChart::Transient_strategy)
def test_statechart::transient_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=stateChart::Transient_strategy)
def test_statechart::transient_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateChart::Transient_strategy)
def test_statechart::transient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateChart::Transient_strategy)
def test_statechart::transient_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=stateChart::Transient_strategy)
def test_statechart::transient_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=stateChart::Transient_strategy)
def test_statechart::transient_effect_type(instance):
    assert isinstance(instance.effect, str)


@given(instance=stateChart::Transient_strategy)
def test_statechart::transient_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original

@given(instance=stateChart::Transient_strategy)
def test_statechart::transient_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=stateChart::Transient_strategy)
def test_statechart::transient_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=stateChart::Region_strategy)
@settings(max_examples=50)
def test_statechart::region_instantiation(instance):
    assert isinstance(instance, stateChart::Region)

@given(instance=stateChart::Region_strategy)
def test_statechart::region_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=stateChart::Region_strategy)
def test_statechart::region_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=stateChart::Region_strategy)
def test_statechart::region_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateChart::Region_strategy)
def test_statechart::region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=stateChart::CompositeState_strategy)
@settings(max_examples=50)
def test_statechart::compositestate_instantiation(instance):
    assert isinstance(instance, stateChart::CompositeState)

@given(instance=stateChart::FinalState_strategy)
@settings(max_examples=50)
def test_statechart::finalstate_instantiation(instance):
    assert isinstance(instance, stateChart::FinalState)

@given(instance=stateChart::SimpleState_strategy)
@settings(max_examples=50)
def test_statechart::simplestate_instantiation(instance):
    assert isinstance(instance, stateChart::SimpleState)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=stateChart::State_strategy)
@settings(max_examples=50)
def test_statechart::state_instantiation(instance):
    assert isinstance(instance, stateChart::State)

@given(instance=stateChart::State_strategy)
def test_statechart::state_exit_type(instance):
    assert isinstance(instance.exit, str)


@given(instance=stateChart::State_strategy)
def test_statechart::state_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original

@given(instance=stateChart::State_strategy)
def test_statechart::state_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=stateChart::State_strategy)
def test_statechart::state_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=stateChart::State_strategy)
def test_statechart::state_entry_type(instance):
    assert isinstance(instance.entry, str)


@given(instance=stateChart::State_strategy)
def test_statechart::state_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original

@given(instance=stateChart::PseudoState_strategy)
@settings(max_examples=50)
def test_statechart::pseudostate_instantiation(instance):
    assert isinstance(instance, stateChart::PseudoState)

@given(instance=stateChart::PseudoState_strategy)
def test_statechart::pseudostate_PseudoStateType_type(instance):
    assert isinstance(instance.PseudoStateType, str)


@given(instance=stateChart::PseudoState_strategy)
def test_statechart::pseudostate_PseudoStateType_setter(instance):
    original = instance.PseudoStateType
    instance.PseudoStateType = original
    assert instance.PseudoStateType == original

@given(instance=stateChart::Vertex_strategy)
@settings(max_examples=50)
def test_statechart::vertex_instantiation(instance):
    assert isinstance(instance, stateChart::Vertex)

@given(instance=stateChart::Vertex_strategy)
def test_statechart::vertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateChart::Vertex_strategy)
def test_statechart::vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateChart::Vertex_strategy)
def test_statechart::vertex_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=stateChart::Vertex_strategy)
def test_statechart::vertex_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=stateChart::Vertex_strategy)
def test_statechart::vertex_isActive_type(instance):
    assert isinstance(instance.isActive, bool)


@given(instance=stateChart::Vertex_strategy)
def test_statechart::vertex_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=stateChart::StateMachine_strategy)
@settings(max_examples=50)
def test_statechart::statemachine_instantiation(instance):
    assert isinstance(instance, stateChart::StateMachine)

@given(instance=stateChart::StateMachine_strategy)
def test_statechart::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateChart::StateMachine_strategy)
def test_statechart::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

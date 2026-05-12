import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stateChart_Transient,
    stateChart_Region,
    State,
    stateChart_CompositeState,
    stateChart_FinalState,
    stateChart_SimpleState,
    Vertex,
    stateChart_State,
    stateChart_PseudoState,
    stateChart_Vertex,
    stateChart_StateMachine,
    PseudoStateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechart_transient_is_not_abstract():
    assert not inspect.isabstract(stateChart_Transient)


def test_statechart_transient_constructor_exists():
    assert callable(stateChart_Transient.__init__)


def test_statechart_transient_constructor_args():
    sig = inspect.signature(stateChart_Transient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_statechart_transient_has_name():
    assert hasattr(stateChart_Transient, "name")
    descriptor = None
    for klass in stateChart_Transient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart_transient_has_guard():
    assert hasattr(stateChart_Transient, "guard")
    descriptor = None
    for klass in stateChart_Transient.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_statechart_transient_has_priority():
    assert hasattr(stateChart_Transient, "priority")
    descriptor = None
    for klass in stateChart_Transient.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_statechart_transient_has_effect():
    assert hasattr(stateChart_Transient, "effect")
    descriptor = None
    for klass in stateChart_Transient.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_statechart_transient_has_trigger():
    assert hasattr(stateChart_Transient, "trigger")
    descriptor = None
    for klass in stateChart_Transient.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_statechart_region_is_not_abstract():
    assert not inspect.isabstract(stateChart_Region)


def test_statechart_region_constructor_exists():
    assert callable(stateChart_Region.__init__)


def test_statechart_region_constructor_args():
    sig = inspect.signature(stateChart_Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "note" in params, "Missing parameter 'note'"

def test_statechart_region_has_name():
    assert hasattr(stateChart_Region, "name")
    descriptor = None
    for klass in stateChart_Region.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart_region_has_note():
    assert hasattr(stateChart_Region, "note")
    descriptor = None
    for klass in stateChart_Region.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statechart_compositestate_is_not_abstract():
    assert not inspect.isabstract(stateChart_CompositeState)


def test_statechart_compositestate_constructor_exists():
    assert callable(stateChart_CompositeState.__init__)


def test_statechart_compositestate_constructor_args():
    sig = inspect.signature(stateChart_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statechart_finalstate_is_not_abstract():
    assert not inspect.isabstract(stateChart_FinalState)


def test_statechart_finalstate_constructor_exists():
    assert callable(stateChart_FinalState.__init__)


def test_statechart_finalstate_constructor_args():
    sig = inspect.signature(stateChart_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statechart_simplestate_is_not_abstract():
    assert not inspect.isabstract(stateChart_SimpleState)


def test_statechart_simplestate_constructor_exists():
    assert callable(stateChart_SimpleState.__init__)


def test_statechart_simplestate_constructor_args():
    sig = inspect.signature(stateChart_SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statechart_state_is_not_abstract():
    assert not inspect.isabstract(stateChart_State)


def test_statechart_state_constructor_exists():
    assert callable(stateChart_State.__init__)


def test_statechart_state_constructor_args():
    sig = inspect.signature(stateChart_State.__init__)
    params = list(sig.parameters.keys())
    assert "entry" in params, "Missing parameter 'entry'"
    assert "exit" in params, "Missing parameter 'exit'"
    assert "action" in params, "Missing parameter 'action'"

def test_statechart_state_has_entry():
    assert hasattr(stateChart_State, "entry")
    descriptor = None
    for klass in stateChart_State.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)

def test_statechart_state_has_exit():
    assert hasattr(stateChart_State, "exit")
    descriptor = None
    for klass in stateChart_State.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)

def test_statechart_state_has_action():
    assert hasattr(stateChart_State, "action")
    descriptor = None
    for klass in stateChart_State.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_statechart_pseudostate_is_not_abstract():
    assert not inspect.isabstract(stateChart_PseudoState)


def test_statechart_pseudostate_constructor_exists():
    assert callable(stateChart_PseudoState.__init__)


def test_statechart_pseudostate_constructor_args():
    sig = inspect.signature(stateChart_PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "PseudoStateType" in params, "Missing parameter 'PseudoStateType'"

def test_statechart_pseudostate_has_PseudoStateType():
    assert hasattr(stateChart_PseudoState, "PseudoStateType")
    descriptor = None
    for klass in stateChart_PseudoState.__mro__:
        if "PseudoStateType" in klass.__dict__:
            descriptor = klass.__dict__["PseudoStateType"]
            break
    assert isinstance(descriptor, property)



def test_statechart_vertex_is_not_abstract():
    assert not inspect.isabstract(stateChart_Vertex)


def test_statechart_vertex_constructor_exists():
    assert callable(stateChart_Vertex.__init__)


def test_statechart_vertex_constructor_args():
    sig = inspect.signature(stateChart_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_statechart_vertex_has_note():
    assert hasattr(stateChart_Vertex, "note")
    descriptor = None
    for klass in stateChart_Vertex.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_statechart_vertex_has_name():
    assert hasattr(stateChart_Vertex, "name")
    descriptor = None
    for klass in stateChart_Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart_vertex_has_isActive():
    assert hasattr(stateChart_Vertex, "isActive")
    descriptor = None
    for klass in stateChart_Vertex.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_statechart_statemachine_is_not_abstract():
    assert not inspect.isabstract(stateChart_StateMachine)


def test_statechart_statemachine_constructor_exists():
    assert callable(stateChart_StateMachine.__init__)


def test_statechart_statemachine_constructor_args():
    sig = inspect.signature(stateChart_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart_statemachine_has_name():
    assert hasattr(stateChart_StateMachine, "name")
    descriptor = None
    for klass in stateChart_StateMachine.__mro__:
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
        "Choice",
        "Terminate",
        "EntryPoint",
        "ShadowHistory",
        "Junction",
        "Initial",
        "ExitPoint",
        "Join",
        "DeepHistory",
        "Fork",
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
stateChart_Transient_strategy = st.builds(
    stateChart_Transient,
    name=
        safe_text,
    guard=
        safe_text,
    priority=
        st.integers(),
    effect=
        safe_text,
    trigger=
        safe_text
)
stateChart_Region_strategy = st.builds(
    stateChart_Region,
    name=
        safe_text,
    note=
        safe_text
)
State_strategy = st.builds(
    State,
)
stateChart_CompositeState_strategy = st.builds(
    stateChart_CompositeState,
)
stateChart_FinalState_strategy = st.builds(
    stateChart_FinalState,
)
stateChart_SimpleState_strategy = st.builds(
    stateChart_SimpleState,
)
Vertex_strategy = st.builds(
    Vertex,
)
stateChart_State_strategy = st.builds(
    stateChart_State,
    entry=
        safe_text,
    exit=
        safe_text,
    action=
        safe_text
)
stateChart_PseudoState_strategy = st.builds(
    stateChart_PseudoState,
    PseudoStateType=
        safe_text
)
stateChart_Vertex_strategy = st.builds(
    stateChart_Vertex,
    note=
        safe_text,
    name=
        safe_text,
    isActive=
        st.booleans()
)
stateChart_StateMachine_strategy = st.builds(
    stateChart_StateMachine,
    name=
        safe_text
)

@given(instance=stateChart_Transient_strategy)
@settings(max_examples=50)
def test_statechart_transient_instantiation(instance):
    assert isinstance(instance, stateChart_Transient)



@given(instance=stateChart_Transient_strategy)
def test_statechart_transient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=stateChart_Transient_strategy)
def test_statechart_transient_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=stateChart_Transient_strategy)
def test_statechart_transient_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=stateChart_Transient_strategy)
def test_statechart_transient_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=stateChart_Transient_strategy)
def test_statechart_transient_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=stateChart_Region_strategy)
@settings(max_examples=50)
def test_statechart_region_instantiation(instance):
    assert isinstance(instance, stateChart_Region)



@given(instance=stateChart_Region_strategy)
def test_statechart_region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=stateChart_Region_strategy)
def test_statechart_region_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=stateChart_CompositeState_strategy)
@settings(max_examples=50)
def test_statechart_compositestate_instantiation(instance):
    assert isinstance(instance, stateChart_CompositeState)

@given(instance=stateChart_FinalState_strategy)
@settings(max_examples=50)
def test_statechart_finalstate_instantiation(instance):
    assert isinstance(instance, stateChart_FinalState)

@given(instance=stateChart_SimpleState_strategy)
@settings(max_examples=50)
def test_statechart_simplestate_instantiation(instance):
    assert isinstance(instance, stateChart_SimpleState)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=stateChart_State_strategy)
@settings(max_examples=50)
def test_statechart_state_instantiation(instance):
    assert isinstance(instance, stateChart_State)



@given(instance=stateChart_State_strategy)
def test_statechart_state_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original



@given(instance=stateChart_State_strategy)
def test_statechart_state_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original



@given(instance=stateChart_State_strategy)
def test_statechart_state_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=stateChart_PseudoState_strategy)
@settings(max_examples=50)
def test_statechart_pseudostate_instantiation(instance):
    assert isinstance(instance, stateChart_PseudoState)



@given(instance=stateChart_PseudoState_strategy)
def test_statechart_pseudostate_PseudoStateType_setter(instance):
    original = instance.PseudoStateType
    instance.PseudoStateType = original
    assert instance.PseudoStateType == original

@given(instance=stateChart_Vertex_strategy)
@settings(max_examples=50)
def test_statechart_vertex_instantiation(instance):
    assert isinstance(instance, stateChart_Vertex)



@given(instance=stateChart_Vertex_strategy)
def test_statechart_vertex_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original



@given(instance=stateChart_Vertex_strategy)
def test_statechart_vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=stateChart_Vertex_strategy)
def test_statechart_vertex_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=stateChart_StateMachine_strategy)
@settings(max_examples=50)
def test_statechart_statemachine_instantiation(instance):
    assert isinstance(instance, stateChart_StateMachine)



@given(instance=stateChart_StateMachine_strategy)
def test_statechart_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

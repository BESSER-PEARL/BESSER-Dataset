import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    statemachines::almostuml::Pseudostate,
    statemachines::almostuml::FinalState,
    statemachines::almostuml::NamedElement,
    statemachines::almostuml::Constraint,
    Constraint,
    Behavior,
    almostuml::Vertex,
    almostuml::NamedElement,
    statemachines::almostuml::State,
    Transition,
    Vertex,
    Trigger,
    Region,
    NamedElement,
    statemachines::almostuml::Behavior,
    statemachines::almostuml::Transition,
    statemachines::almostuml::Region,
    statemachines::almostuml::Vertex,
    statemachines::almostuml::Event,
    statemachines::almostuml::Trigger,
    statemachines::almostuml::StateMachine,
    Event,
    statemachines::CustomEvent,
    StateMachine,
    statemachines::CustomSystem,
    PseudostateKind,
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



def test_statemachines::almostuml::pseudostate_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::Pseudostate)


def test_statemachines::almostuml::pseudostate_constructor_exists():
    assert callable(statemachines::almostuml::Pseudostate.__init__)


def test_statemachines::almostuml::pseudostate_constructor_args():
    sig = inspect.signature(statemachines::almostuml::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachines::almostuml::pseudostate_has_kind():
    assert hasattr(statemachines::almostuml::Pseudostate, "kind")
    descriptor = None
    for klass in statemachines::almostuml::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachines::almostuml::finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::FinalState)


def test_statemachines::almostuml::finalstate_constructor_exists():
    assert callable(statemachines::almostuml::FinalState.__init__)


def test_statemachines::almostuml::finalstate_constructor_args():
    sig = inspect.signature(statemachines::almostuml::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::almostuml::namedelement_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::NamedElement)


def test_statemachines::almostuml::namedelement_constructor_exists():
    assert callable(statemachines::almostuml::NamedElement.__init__)


def test_statemachines::almostuml::namedelement_constructor_args():
    sig = inspect.signature(statemachines::almostuml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachines::almostuml::namedelement_has_name():
    assert hasattr(statemachines::almostuml::NamedElement, "name")
    descriptor = None
    for klass in statemachines::almostuml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachines::almostuml::constraint_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::Constraint)


def test_statemachines::almostuml::constraint_constructor_exists():
    assert callable(statemachines::almostuml::Constraint.__init__)


def test_statemachines::almostuml::constraint_constructor_args():
    sig = inspect.signature(statemachines::almostuml::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_almostuml::vertex_is_not_abstract():
    assert not inspect.isabstract(almostuml::Vertex)


def test_almostuml::vertex_constructor_exists():
    assert callable(almostuml::Vertex.__init__)


def test_almostuml::vertex_constructor_args():
    sig = inspect.signature(almostuml::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_almostuml::namedelement_is_not_abstract():
    assert not inspect.isabstract(almostuml::NamedElement)


def test_almostuml::namedelement_constructor_exists():
    assert callable(almostuml::NamedElement.__init__)


def test_almostuml::namedelement_constructor_args():
    sig = inspect.signature(almostuml::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::almostuml::state_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::State)


def test_statemachines::almostuml::state_constructor_exists():
    assert callable(statemachines::almostuml::State.__init__)


def test_statemachines::almostuml::state_constructor_args():
    sig = inspect.signature(statemachines::almostuml::State.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_region_is_not_abstract():
    assert not inspect.isabstract(Region)


def test_region_constructor_exists():
    assert callable(Region.__init__)


def test_region_constructor_args():
    sig = inspect.signature(Region.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::almostuml::behavior_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::Behavior)


def test_statemachines::almostuml::behavior_constructor_exists():
    assert callable(statemachines::almostuml::Behavior.__init__)


def test_statemachines::almostuml::behavior_constructor_args():
    sig = inspect.signature(statemachines::almostuml::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::almostuml::transition_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::Transition)


def test_statemachines::almostuml::transition_constructor_exists():
    assert callable(statemachines::almostuml::Transition.__init__)


def test_statemachines::almostuml::transition_constructor_args():
    sig = inspect.signature(statemachines::almostuml::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::almostuml::region_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::Region)


def test_statemachines::almostuml::region_constructor_exists():
    assert callable(statemachines::almostuml::Region.__init__)


def test_statemachines::almostuml::region_constructor_args():
    sig = inspect.signature(statemachines::almostuml::Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::almostuml::vertex_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::Vertex)


def test_statemachines::almostuml::vertex_constructor_exists():
    assert callable(statemachines::almostuml::Vertex.__init__)


def test_statemachines::almostuml::vertex_constructor_args():
    sig = inspect.signature(statemachines::almostuml::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::almostuml::event_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::Event)


def test_statemachines::almostuml::event_constructor_exists():
    assert callable(statemachines::almostuml::Event.__init__)


def test_statemachines::almostuml::event_constructor_args():
    sig = inspect.signature(statemachines::almostuml::Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::almostuml::trigger_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::Trigger)


def test_statemachines::almostuml::trigger_constructor_exists():
    assert callable(statemachines::almostuml::Trigger.__init__)


def test_statemachines::almostuml::trigger_constructor_args():
    sig = inspect.signature(statemachines::almostuml::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::almostuml::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachines::almostuml::StateMachine)


def test_statemachines::almostuml::statemachine_constructor_exists():
    assert callable(statemachines::almostuml::StateMachine.__init__)


def test_statemachines::almostuml::statemachine_constructor_args():
    sig = inspect.signature(statemachines::almostuml::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::customevent_is_not_abstract():
    assert not inspect.isabstract(statemachines::CustomEvent)


def test_statemachines::customevent_constructor_exists():
    assert callable(statemachines::CustomEvent.__init__)


def test_statemachines::customevent_constructor_args():
    sig = inspect.signature(statemachines::CustomEvent.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachines::customsystem_is_not_abstract():
    assert not inspect.isabstract(statemachines::CustomSystem)


def test_statemachines::customsystem_constructor_exists():
    assert callable(statemachines::CustomSystem.__init__)


def test_statemachines::customsystem_constructor_args():
    sig = inspect.signature(statemachines::CustomSystem.__init__)
    params = list(sig.parameters.keys())

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "join",
        "fork",
        "junction",
        "choice",
        "initial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"


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
statemachines::almostuml::Pseudostate_strategy = st.builds(
    statemachines::almostuml::Pseudostate,
    kind=
        safe_text
)
statemachines::almostuml::FinalState_strategy = st.builds(
    statemachines::almostuml::FinalState,
)
statemachines::almostuml::NamedElement_strategy = st.builds(
    statemachines::almostuml::NamedElement,
    name=
        safe_text
)
statemachines::almostuml::Constraint_strategy = st.builds(
    statemachines::almostuml::Constraint,
)
Constraint_strategy = st.builds(
    Constraint,
)
Behavior_strategy = st.builds(
    Behavior,
)
almostuml::Vertex_strategy = st.builds(
    almostuml::Vertex,
)
almostuml::NamedElement_strategy = st.builds(
    almostuml::NamedElement,
)
statemachines::almostuml::State_strategy = st.builds(
    statemachines::almostuml::State,
)
Transition_strategy = st.builds(
    Transition,
)
Vertex_strategy = st.builds(
    Vertex,
)
Trigger_strategy = st.builds(
    Trigger,
)
Region_strategy = st.builds(
    Region,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
statemachines::almostuml::Behavior_strategy = st.builds(
    statemachines::almostuml::Behavior,
)
statemachines::almostuml::Transition_strategy = st.builds(
    statemachines::almostuml::Transition,
)
statemachines::almostuml::Region_strategy = st.builds(
    statemachines::almostuml::Region,
)
statemachines::almostuml::Vertex_strategy = st.builds(
    statemachines::almostuml::Vertex,
)
statemachines::almostuml::Event_strategy = st.builds(
    statemachines::almostuml::Event,
)
statemachines::almostuml::Trigger_strategy = st.builds(
    statemachines::almostuml::Trigger,
)
statemachines::almostuml::StateMachine_strategy = st.builds(
    statemachines::almostuml::StateMachine,
)
Event_strategy = st.builds(
    Event,
)
statemachines::CustomEvent_strategy = st.builds(
    statemachines::CustomEvent,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
statemachines::CustomSystem_strategy = st.builds(
    statemachines::CustomSystem,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachines::almostuml::Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::pseudostate_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::Pseudostate)

@given(instance=statemachines::almostuml::Pseudostate_strategy)
def test_statemachines::almostuml::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=statemachines::almostuml::Pseudostate_strategy)
def test_statemachines::almostuml::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=statemachines::almostuml::FinalState_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::finalstate_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::FinalState)

@given(instance=statemachines::almostuml::NamedElement_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::namedelement_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::NamedElement)

@given(instance=statemachines::almostuml::NamedElement_strategy)
def test_statemachines::almostuml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachines::almostuml::NamedElement_strategy)
def test_statemachines::almostuml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachines::almostuml::Constraint_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::constraint_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::Constraint)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=almostuml::Vertex_strategy)
@settings(max_examples=50)
def test_almostuml::vertex_instantiation(instance):
    assert isinstance(instance, almostuml::Vertex)

@given(instance=almostuml::NamedElement_strategy)
@settings(max_examples=50)
def test_almostuml::namedelement_instantiation(instance):
    assert isinstance(instance, almostuml::NamedElement)

@given(instance=statemachines::almostuml::State_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::state_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::State)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=statemachines::almostuml::Behavior_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::behavior_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::Behavior)

@given(instance=statemachines::almostuml::Transition_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::transition_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::Transition)

@given(instance=statemachines::almostuml::Region_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::region_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::Region)

@given(instance=statemachines::almostuml::Vertex_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::vertex_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::Vertex)

@given(instance=statemachines::almostuml::Event_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::event_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::Event)

@given(instance=statemachines::almostuml::Trigger_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::trigger_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::Trigger)

@given(instance=statemachines::almostuml::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachines::almostuml::statemachine_instantiation(instance):
    assert isinstance(instance, statemachines::almostuml::StateMachine)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=statemachines::CustomEvent_strategy)
@settings(max_examples=50)
def test_statemachines::customevent_instantiation(instance):
    assert isinstance(instance, statemachines::CustomEvent)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=statemachines::CustomSystem_strategy)
@settings(max_examples=50)
def test_statemachines::customsystem_instantiation(instance):
    assert isinstance(instance, statemachines::CustomSystem)

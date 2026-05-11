import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    umlstatemachineselect::Vertex,
    umlstatemachineselect::Trigger,
    umlstatemachineselect::Constraint,
    umlstatemachineselect::Behavior,
    umlstatemachineselect::Transition,
    umlstatemachineselect::Region,
    Behavior,
    umlstatemachineselect::Event,
    Vertex,
    umlstatemachineselect::State,
    umlstatemachineselect::PseudoState,
    State,
    umlstatemachineselect::FinalState,
    umlstatemachineselect::ConnectionPointReference,
    umlstatemachineselect::StateMachine,
    PseudostateKind,
    TransitionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlstatemachineselect::vertex_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::Vertex)


def test_umlstatemachineselect::vertex_constructor_exists():
    assert callable(umlstatemachineselect::Vertex.__init__)


def test_umlstatemachineselect::vertex_constructor_args():
    sig = inspect.signature(umlstatemachineselect::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect::trigger_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::Trigger)


def test_umlstatemachineselect::trigger_constructor_exists():
    assert callable(umlstatemachineselect::Trigger.__init__)


def test_umlstatemachineselect::trigger_constructor_args():
    sig = inspect.signature(umlstatemachineselect::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect::constraint_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::Constraint)


def test_umlstatemachineselect::constraint_constructor_exists():
    assert callable(umlstatemachineselect::Constraint.__init__)


def test_umlstatemachineselect::constraint_constructor_args():
    sig = inspect.signature(umlstatemachineselect::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect::behavior_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::Behavior)


def test_umlstatemachineselect::behavior_constructor_exists():
    assert callable(umlstatemachineselect::Behavior.__init__)


def test_umlstatemachineselect::behavior_constructor_args():
    sig = inspect.signature(umlstatemachineselect::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect::transition_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::Transition)


def test_umlstatemachineselect::transition_constructor_exists():
    assert callable(umlstatemachineselect::Transition.__init__)


def test_umlstatemachineselect::transition_constructor_args():
    sig = inspect.signature(umlstatemachineselect::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlstatemachineselect::transition_has_kind():
    assert hasattr(umlstatemachineselect::Transition, "kind")
    descriptor = None
    for klass in umlstatemachineselect::Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_umlstatemachineselect::region_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::Region)


def test_umlstatemachineselect::region_constructor_exists():
    assert callable(umlstatemachineselect::Region.__init__)


def test_umlstatemachineselect::region_constructor_args():
    sig = inspect.signature(umlstatemachineselect::Region.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect::event_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::Event)


def test_umlstatemachineselect::event_constructor_exists():
    assert callable(umlstatemachineselect::Event.__init__)


def test_umlstatemachineselect::event_constructor_args():
    sig = inspect.signature(umlstatemachineselect::Event.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect::state_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::State)


def test_umlstatemachineselect::state_constructor_exists():
    assert callable(umlstatemachineselect::State.__init__)


def test_umlstatemachineselect::state_constructor_args():
    sig = inspect.signature(umlstatemachineselect::State.__init__)
    params = list(sig.parameters.keys())
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isSimple" in params, "Missing parameter 'isSimple'"

def test_umlstatemachineselect::state_has_isOrthogonal():
    assert hasattr(umlstatemachineselect::State, "isOrthogonal")
    descriptor = None
    for klass in umlstatemachineselect::State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_umlstatemachineselect::state_has_isSubmachineState():
    assert hasattr(umlstatemachineselect::State, "isSubmachineState")
    descriptor = None
    for klass in umlstatemachineselect::State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_umlstatemachineselect::state_has_isComposite():
    assert hasattr(umlstatemachineselect::State, "isComposite")
    descriptor = None
    for klass in umlstatemachineselect::State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_umlstatemachineselect::state_has_isSimple():
    assert hasattr(umlstatemachineselect::State, "isSimple")
    descriptor = None
    for klass in umlstatemachineselect::State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)



def test_umlstatemachineselect::pseudostate_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::PseudoState)


def test_umlstatemachineselect::pseudostate_constructor_exists():
    assert callable(umlstatemachineselect::PseudoState.__init__)


def test_umlstatemachineselect::pseudostate_constructor_args():
    sig = inspect.signature(umlstatemachineselect::PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlstatemachineselect::pseudostate_has_kind():
    assert hasattr(umlstatemachineselect::PseudoState, "kind")
    descriptor = None
    for klass in umlstatemachineselect::PseudoState.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect::finalstate_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::FinalState)


def test_umlstatemachineselect::finalstate_constructor_exists():
    assert callable(umlstatemachineselect::FinalState.__init__)


def test_umlstatemachineselect::finalstate_constructor_args():
    sig = inspect.signature(umlstatemachineselect::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect::connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::ConnectionPointReference)


def test_umlstatemachineselect::connectionpointreference_constructor_exists():
    assert callable(umlstatemachineselect::ConnectionPointReference.__init__)


def test_umlstatemachineselect::connectionpointreference_constructor_args():
    sig = inspect.signature(umlstatemachineselect::ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect::statemachine_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect::StateMachine)


def test_umlstatemachineselect::statemachine_constructor_exists():
    assert callable(umlstatemachineselect::StateMachine.__init__)


def test_umlstatemachineselect::statemachine_constructor_args():
    sig = inspect.signature(umlstatemachineselect::StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "deepHistory",
        "junction",
        "fork",
        "join",
        "terminate",
        "exitPoint",
        "choice",
        "shallowHistory",
        "entryPoint",
        "initial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "internal",
        "external",
        "local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"


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
umlstatemachineselect::Vertex_strategy = st.builds(
    umlstatemachineselect::Vertex,
)
umlstatemachineselect::Trigger_strategy = st.builds(
    umlstatemachineselect::Trigger,
)
umlstatemachineselect::Constraint_strategy = st.builds(
    umlstatemachineselect::Constraint,
)
umlstatemachineselect::Behavior_strategy = st.builds(
    umlstatemachineselect::Behavior,
)
umlstatemachineselect::Transition_strategy = st.builds(
    umlstatemachineselect::Transition,
    kind=
        safe_text
)
umlstatemachineselect::Region_strategy = st.builds(
    umlstatemachineselect::Region,
)
Behavior_strategy = st.builds(
    Behavior,
)
umlstatemachineselect::Event_strategy = st.builds(
    umlstatemachineselect::Event,
)
Vertex_strategy = st.builds(
    Vertex,
)
umlstatemachineselect::State_strategy = st.builds(
    umlstatemachineselect::State,
    isOrthogonal=
        st.booleans(),
    isSubmachineState=
        st.booleans(),
    isComposite=
        st.booleans(),
    isSimple=
        st.booleans()
)
umlstatemachineselect::PseudoState_strategy = st.builds(
    umlstatemachineselect::PseudoState,
    kind=
        safe_text
)
State_strategy = st.builds(
    State,
)
umlstatemachineselect::FinalState_strategy = st.builds(
    umlstatemachineselect::FinalState,
)
umlstatemachineselect::ConnectionPointReference_strategy = st.builds(
    umlstatemachineselect::ConnectionPointReference,
)
umlstatemachineselect::StateMachine_strategy = st.builds(
    umlstatemachineselect::StateMachine,
)

@given(instance=umlstatemachineselect::Vertex_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::vertex_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::Vertex)

@given(instance=umlstatemachineselect::Trigger_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::trigger_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::Trigger)

@given(instance=umlstatemachineselect::Constraint_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::constraint_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::Constraint)

@given(instance=umlstatemachineselect::Behavior_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::behavior_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::Behavior)

@given(instance=umlstatemachineselect::Transition_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::transition_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::Transition)

@given(instance=umlstatemachineselect::Transition_strategy)
def test_umlstatemachineselect::transition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=umlstatemachineselect::Transition_strategy)
def test_umlstatemachineselect::transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlstatemachineselect::Region_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::region_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::Region)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=umlstatemachineselect::Event_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::event_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::Event)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=umlstatemachineselect::State_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::state_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::State)

@given(instance=umlstatemachineselect::State_strategy)
def test_umlstatemachineselect::state_isOrthogonal_type(instance):
    assert isinstance(instance.isOrthogonal, bool)


@given(instance=umlstatemachineselect::State_strategy)
def test_umlstatemachineselect::state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original

@given(instance=umlstatemachineselect::State_strategy)
def test_umlstatemachineselect::state_isSubmachineState_type(instance):
    assert isinstance(instance.isSubmachineState, bool)


@given(instance=umlstatemachineselect::State_strategy)
def test_umlstatemachineselect::state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original

@given(instance=umlstatemachineselect::State_strategy)
def test_umlstatemachineselect::state_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=umlstatemachineselect::State_strategy)
def test_umlstatemachineselect::state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=umlstatemachineselect::State_strategy)
def test_umlstatemachineselect::state_isSimple_type(instance):
    assert isinstance(instance.isSimple, bool)


@given(instance=umlstatemachineselect::State_strategy)
def test_umlstatemachineselect::state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original

@given(instance=umlstatemachineselect::PseudoState_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::pseudostate_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::PseudoState)

@given(instance=umlstatemachineselect::PseudoState_strategy)
def test_umlstatemachineselect::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=umlstatemachineselect::PseudoState_strategy)
def test_umlstatemachineselect::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=umlstatemachineselect::FinalState_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::finalstate_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::FinalState)

@given(instance=umlstatemachineselect::ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::connectionpointreference_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::ConnectionPointReference)

@given(instance=umlstatemachineselect::StateMachine_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect::statemachine_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect::StateMachine)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    umlstatemachineselect_Region,
    Behavior,
    umlstatemachineselect_Event,
    Vertex,
    umlstatemachineselect_PseudoState,
    umlstatemachineselect_State,
    State,
    umlstatemachineselect_FinalState,
    umlstatemachineselect_ConnectionPointReference,
    umlstatemachineselect_Vertex,
    umlstatemachineselect_Trigger,
    umlstatemachineselect_Constraint,
    umlstatemachineselect_Behavior,
    umlstatemachineselect_Transition,
    umlstatemachineselect_StateMachine,
    TransitionKind,
    PseudostateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlstatemachineselect_region_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_Region)


def test_umlstatemachineselect_region_constructor_exists():
    assert callable(umlstatemachineselect_Region.__init__)


def test_umlstatemachineselect_region_constructor_args():
    sig = inspect.signature(umlstatemachineselect_Region.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect_event_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_Event)


def test_umlstatemachineselect_event_constructor_exists():
    assert callable(umlstatemachineselect_Event.__init__)


def test_umlstatemachineselect_event_constructor_args():
    sig = inspect.signature(umlstatemachineselect_Event.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect_pseudostate_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_PseudoState)


def test_umlstatemachineselect_pseudostate_constructor_exists():
    assert callable(umlstatemachineselect_PseudoState.__init__)


def test_umlstatemachineselect_pseudostate_constructor_args():
    sig = inspect.signature(umlstatemachineselect_PseudoState.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlstatemachineselect_pseudostate_has_kind():
    assert hasattr(umlstatemachineselect_PseudoState, "kind")
    descriptor = None
    for klass in umlstatemachineselect_PseudoState.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_umlstatemachineselect_state_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_State)


def test_umlstatemachineselect_state_constructor_exists():
    assert callable(umlstatemachineselect_State.__init__)


def test_umlstatemachineselect_state_constructor_args():
    sig = inspect.signature(umlstatemachineselect_State.__init__)
    params = list(sig.parameters.keys())
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_umlstatemachineselect_state_has_isSimple():
    assert hasattr(umlstatemachineselect_State, "isSimple")
    descriptor = None
    for klass in umlstatemachineselect_State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_umlstatemachineselect_state_has_isOrthogonal():
    assert hasattr(umlstatemachineselect_State, "isOrthogonal")
    descriptor = None
    for klass in umlstatemachineselect_State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_umlstatemachineselect_state_has_isSubmachineState():
    assert hasattr(umlstatemachineselect_State, "isSubmachineState")
    descriptor = None
    for klass in umlstatemachineselect_State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_umlstatemachineselect_state_has_isComposite():
    assert hasattr(umlstatemachineselect_State, "isComposite")
    descriptor = None
    for klass in umlstatemachineselect_State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect_finalstate_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_FinalState)


def test_umlstatemachineselect_finalstate_constructor_exists():
    assert callable(umlstatemachineselect_FinalState.__init__)


def test_umlstatemachineselect_finalstate_constructor_args():
    sig = inspect.signature(umlstatemachineselect_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_ConnectionPointReference)


def test_umlstatemachineselect_connectionpointreference_constructor_exists():
    assert callable(umlstatemachineselect_ConnectionPointReference.__init__)


def test_umlstatemachineselect_connectionpointreference_constructor_args():
    sig = inspect.signature(umlstatemachineselect_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect_vertex_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_Vertex)


def test_umlstatemachineselect_vertex_constructor_exists():
    assert callable(umlstatemachineselect_Vertex.__init__)


def test_umlstatemachineselect_vertex_constructor_args():
    sig = inspect.signature(umlstatemachineselect_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect_trigger_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_Trigger)


def test_umlstatemachineselect_trigger_constructor_exists():
    assert callable(umlstatemachineselect_Trigger.__init__)


def test_umlstatemachineselect_trigger_constructor_args():
    sig = inspect.signature(umlstatemachineselect_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect_constraint_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_Constraint)


def test_umlstatemachineselect_constraint_constructor_exists():
    assert callable(umlstatemachineselect_Constraint.__init__)


def test_umlstatemachineselect_constraint_constructor_args():
    sig = inspect.signature(umlstatemachineselect_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect_behavior_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_Behavior)


def test_umlstatemachineselect_behavior_constructor_exists():
    assert callable(umlstatemachineselect_Behavior.__init__)


def test_umlstatemachineselect_behavior_constructor_args():
    sig = inspect.signature(umlstatemachineselect_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_umlstatemachineselect_transition_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_Transition)


def test_umlstatemachineselect_transition_constructor_exists():
    assert callable(umlstatemachineselect_Transition.__init__)


def test_umlstatemachineselect_transition_constructor_args():
    sig = inspect.signature(umlstatemachineselect_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_umlstatemachineselect_transition_has_kind():
    assert hasattr(umlstatemachineselect_Transition, "kind")
    descriptor = None
    for klass in umlstatemachineselect_Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_umlstatemachineselect_statemachine_is_not_abstract():
    assert not inspect.isabstract(umlstatemachineselect_StateMachine)


def test_umlstatemachineselect_statemachine_constructor_exists():
    assert callable(umlstatemachineselect_StateMachine.__init__)


def test_umlstatemachineselect_statemachine_constructor_args():
    sig = inspect.signature(umlstatemachineselect_StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "local",
        "external",
        "internal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "choice",
        "exitPoint",
        "terminate",
        "join",
        "entryPoint",
        "deepHistory",
        "shallowHistory",
        "fork",
        "junction",
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
umlstatemachineselect_Region_strategy = st.builds(
    umlstatemachineselect_Region,
)
Behavior_strategy = st.builds(
    Behavior,
)
umlstatemachineselect_Event_strategy = st.builds(
    umlstatemachineselect_Event,
)
Vertex_strategy = st.builds(
    Vertex,
)
umlstatemachineselect_PseudoState_strategy = st.builds(
    umlstatemachineselect_PseudoState,
    kind=
        safe_text
)
umlstatemachineselect_State_strategy = st.builds(
    umlstatemachineselect_State,
    isSimple=
        st.booleans(),
    isOrthogonal=
        st.booleans(),
    isSubmachineState=
        st.booleans(),
    isComposite=
        st.booleans()
)
State_strategy = st.builds(
    State,
)
umlstatemachineselect_FinalState_strategy = st.builds(
    umlstatemachineselect_FinalState,
)
umlstatemachineselect_ConnectionPointReference_strategy = st.builds(
    umlstatemachineselect_ConnectionPointReference,
)
umlstatemachineselect_Vertex_strategy = st.builds(
    umlstatemachineselect_Vertex,
)
umlstatemachineselect_Trigger_strategy = st.builds(
    umlstatemachineselect_Trigger,
)
umlstatemachineselect_Constraint_strategy = st.builds(
    umlstatemachineselect_Constraint,
)
umlstatemachineselect_Behavior_strategy = st.builds(
    umlstatemachineselect_Behavior,
)
umlstatemachineselect_Transition_strategy = st.builds(
    umlstatemachineselect_Transition,
    kind=
        safe_text
)
umlstatemachineselect_StateMachine_strategy = st.builds(
    umlstatemachineselect_StateMachine,
)

@given(instance=umlstatemachineselect_Region_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_region_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_Region)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=umlstatemachineselect_Event_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_event_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_Event)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=umlstatemachineselect_PseudoState_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_pseudostate_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_PseudoState)



@given(instance=umlstatemachineselect_PseudoState_strategy)
def test_umlstatemachineselect_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlstatemachineselect_State_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_state_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_State)



@given(instance=umlstatemachineselect_State_strategy)
def test_umlstatemachineselect_state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original



@given(instance=umlstatemachineselect_State_strategy)
def test_umlstatemachineselect_state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original



@given(instance=umlstatemachineselect_State_strategy)
def test_umlstatemachineselect_state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original



@given(instance=umlstatemachineselect_State_strategy)
def test_umlstatemachineselect_state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=umlstatemachineselect_FinalState_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_finalstate_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_FinalState)

@given(instance=umlstatemachineselect_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_connectionpointreference_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_ConnectionPointReference)

@given(instance=umlstatemachineselect_Vertex_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_vertex_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_Vertex)

@given(instance=umlstatemachineselect_Trigger_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_trigger_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_Trigger)

@given(instance=umlstatemachineselect_Constraint_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_constraint_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_Constraint)

@given(instance=umlstatemachineselect_Behavior_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_behavior_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_Behavior)

@given(instance=umlstatemachineselect_Transition_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_transition_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_Transition)



@given(instance=umlstatemachineselect_Transition_strategy)
def test_umlstatemachineselect_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=umlstatemachineselect_StateMachine_strategy)
@settings(max_examples=50)
def test_umlstatemachineselect_statemachine_instantiation(instance):
    assert isinstance(instance, umlstatemachineselect_StateMachine)

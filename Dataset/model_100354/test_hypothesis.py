import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    uml_FinalState,
    Vertex,
    uml_State,
    uml_Pseudostate,
    uml_Region,
    uml_Vertex,
    uml_Trigger,
    uml_Behavior,
    uml_Transition,
    Behavior,
    uml_Activity,
    uml_StateMachine,
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



def test_uml_finalstate_is_not_abstract():
    assert not inspect.isabstract(uml_FinalState)


def test_uml_finalstate_constructor_exists():
    assert callable(uml_FinalState.__init__)


def test_uml_finalstate_constructor_args():
    sig = inspect.signature(uml_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml_state_is_not_abstract():
    assert not inspect.isabstract(uml_State)


def test_uml_state_constructor_exists():
    assert callable(uml_State.__init__)


def test_uml_state_constructor_args():
    sig = inspect.signature(uml_State.__init__)
    params = list(sig.parameters.keys())



def test_uml_pseudostate_is_not_abstract():
    assert not inspect.isabstract(uml_Pseudostate)


def test_uml_pseudostate_constructor_exists():
    assert callable(uml_Pseudostate.__init__)


def test_uml_pseudostate_constructor_args():
    sig = inspect.signature(uml_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml_pseudostate_has_kind():
    assert hasattr(uml_Pseudostate, "kind")
    descriptor = None
    for klass in uml_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uml_region_is_not_abstract():
    assert not inspect.isabstract(uml_Region)


def test_uml_region_constructor_exists():
    assert callable(uml_Region.__init__)


def test_uml_region_constructor_args():
    sig = inspect.signature(uml_Region.__init__)
    params = list(sig.parameters.keys())



def test_uml_vertex_is_not_abstract():
    assert not inspect.isabstract(uml_Vertex)


def test_uml_vertex_constructor_exists():
    assert callable(uml_Vertex.__init__)


def test_uml_vertex_constructor_args():
    sig = inspect.signature(uml_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml_vertex_has_name():
    assert hasattr(uml_Vertex, "name")
    descriptor = None
    for klass in uml_Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml_trigger_is_not_abstract():
    assert not inspect.isabstract(uml_Trigger)


def test_uml_trigger_constructor_exists():
    assert callable(uml_Trigger.__init__)


def test_uml_trigger_constructor_args():
    sig = inspect.signature(uml_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml_trigger_has_name():
    assert hasattr(uml_Trigger, "name")
    descriptor = None
    for klass in uml_Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml_behavior_is_not_abstract():
    assert not inspect.isabstract(uml_Behavior)


def test_uml_behavior_constructor_exists():
    assert callable(uml_Behavior.__init__)


def test_uml_behavior_constructor_args():
    sig = inspect.signature(uml_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml_behavior_has_name():
    assert hasattr(uml_Behavior, "name")
    descriptor = None
    for klass in uml_Behavior.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml_transition_is_not_abstract():
    assert not inspect.isabstract(uml_Transition)


def test_uml_transition_constructor_exists():
    assert callable(uml_Transition.__init__)


def test_uml_transition_constructor_args():
    sig = inspect.signature(uml_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml_transition_has_name():
    assert hasattr(uml_Transition, "name")
    descriptor = None
    for klass in uml_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml_activity_is_not_abstract():
    assert not inspect.isabstract(uml_Activity)


def test_uml_activity_constructor_exists():
    assert callable(uml_Activity.__init__)


def test_uml_activity_constructor_args():
    sig = inspect.signature(uml_Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml_statemachine_is_not_abstract():
    assert not inspect.isabstract(uml_StateMachine)


def test_uml_statemachine_constructor_exists():
    assert callable(uml_StateMachine.__init__)


def test_uml_statemachine_constructor_args():
    sig = inspect.signature(uml_StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "join",
        "choice",
        "entryPoint",
        "shallowHistory",
        "exitPoint",
        "terminate",
        "fork",
        "junction",
        "deepHistory",
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
uml_FinalState_strategy = st.builds(
    uml_FinalState,
)
Vertex_strategy = st.builds(
    Vertex,
)
uml_State_strategy = st.builds(
    uml_State,
)
uml_Pseudostate_strategy = st.builds(
    uml_Pseudostate,
    kind=
        safe_text
)
uml_Region_strategy = st.builds(
    uml_Region,
)
uml_Vertex_strategy = st.builds(
    uml_Vertex,
    name=
        safe_text
)
uml_Trigger_strategy = st.builds(
    uml_Trigger,
    name=
        safe_text
)
uml_Behavior_strategy = st.builds(
    uml_Behavior,
    name=
        safe_text
)
uml_Transition_strategy = st.builds(
    uml_Transition,
    name=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
uml_Activity_strategy = st.builds(
    uml_Activity,
)
uml_StateMachine_strategy = st.builds(
    uml_StateMachine,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=uml_FinalState_strategy)
@settings(max_examples=50)
def test_uml_finalstate_instantiation(instance):
    assert isinstance(instance, uml_FinalState)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=uml_State_strategy)
@settings(max_examples=50)
def test_uml_state_instantiation(instance):
    assert isinstance(instance, uml_State)

@given(instance=uml_Pseudostate_strategy)
@settings(max_examples=50)
def test_uml_pseudostate_instantiation(instance):
    assert isinstance(instance, uml_Pseudostate)



@given(instance=uml_Pseudostate_strategy)
def test_uml_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=uml_Region_strategy)
@settings(max_examples=50)
def test_uml_region_instantiation(instance):
    assert isinstance(instance, uml_Region)

@given(instance=uml_Vertex_strategy)
@settings(max_examples=50)
def test_uml_vertex_instantiation(instance):
    assert isinstance(instance, uml_Vertex)



@given(instance=uml_Vertex_strategy)
def test_uml_vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml_Trigger_strategy)
@settings(max_examples=50)
def test_uml_trigger_instantiation(instance):
    assert isinstance(instance, uml_Trigger)



@given(instance=uml_Trigger_strategy)
def test_uml_trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml_Behavior_strategy)
@settings(max_examples=50)
def test_uml_behavior_instantiation(instance):
    assert isinstance(instance, uml_Behavior)



@given(instance=uml_Behavior_strategy)
def test_uml_behavior_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml_Transition_strategy)
@settings(max_examples=50)
def test_uml_transition_instantiation(instance):
    assert isinstance(instance, uml_Transition)



@given(instance=uml_Transition_strategy)
def test_uml_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=uml_Activity_strategy)
@settings(max_examples=50)
def test_uml_activity_instantiation(instance):
    assert isinstance(instance, uml_Activity)

@given(instance=uml_StateMachine_strategy)
@settings(max_examples=50)
def test_uml_statemachine_instantiation(instance):
    assert isinstance(instance, uml_StateMachine)

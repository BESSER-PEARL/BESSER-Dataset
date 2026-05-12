import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    uml::FinalState,
    Vertex,
    uml::State,
    uml::Pseudostate,
    uml::Region,
    uml::Vertex,
    uml::Trigger,
    uml::Behavior,
    uml::Transition,
    Behavior,
    uml::Activity,
    uml::StateMachine,
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



def test_uml::finalstate_is_not_abstract():
    assert not inspect.isabstract(uml::FinalState)


def test_uml::finalstate_constructor_exists():
    assert callable(uml::FinalState.__init__)


def test_uml::finalstate_constructor_args():
    sig = inspect.signature(uml::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml::state_is_not_abstract():
    assert not inspect.isabstract(uml::State)


def test_uml::state_constructor_exists():
    assert callable(uml::State.__init__)


def test_uml::state_constructor_args():
    sig = inspect.signature(uml::State.__init__)
    params = list(sig.parameters.keys())



def test_uml::pseudostate_is_not_abstract():
    assert not inspect.isabstract(uml::Pseudostate)


def test_uml::pseudostate_constructor_exists():
    assert callable(uml::Pseudostate.__init__)


def test_uml::pseudostate_constructor_args():
    sig = inspect.signature(uml::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml::pseudostate_has_kind():
    assert hasattr(uml::Pseudostate, "kind")
    descriptor = None
    for klass in uml::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uml::region_is_not_abstract():
    assert not inspect.isabstract(uml::Region)


def test_uml::region_constructor_exists():
    assert callable(uml::Region.__init__)


def test_uml::region_constructor_args():
    sig = inspect.signature(uml::Region.__init__)
    params = list(sig.parameters.keys())



def test_uml::vertex_is_not_abstract():
    assert not inspect.isabstract(uml::Vertex)


def test_uml::vertex_constructor_exists():
    assert callable(uml::Vertex.__init__)


def test_uml::vertex_constructor_args():
    sig = inspect.signature(uml::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::vertex_has_name():
    assert hasattr(uml::Vertex, "name")
    descriptor = None
    for klass in uml::Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml::trigger_is_not_abstract():
    assert not inspect.isabstract(uml::Trigger)


def test_uml::trigger_constructor_exists():
    assert callable(uml::Trigger.__init__)


def test_uml::trigger_constructor_args():
    sig = inspect.signature(uml::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::trigger_has_name():
    assert hasattr(uml::Trigger, "name")
    descriptor = None
    for klass in uml::Trigger.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml::behavior_is_not_abstract():
    assert not inspect.isabstract(uml::Behavior)


def test_uml::behavior_constructor_exists():
    assert callable(uml::Behavior.__init__)


def test_uml::behavior_constructor_args():
    sig = inspect.signature(uml::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::behavior_has_name():
    assert hasattr(uml::Behavior, "name")
    descriptor = None
    for klass in uml::Behavior.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml::transition_is_not_abstract():
    assert not inspect.isabstract(uml::Transition)


def test_uml::transition_constructor_exists():
    assert callable(uml::Transition.__init__)


def test_uml::transition_constructor_args():
    sig = inspect.signature(uml::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::transition_has_name():
    assert hasattr(uml::Transition, "name")
    descriptor = None
    for klass in uml::Transition.__mro__:
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



def test_uml::activity_is_not_abstract():
    assert not inspect.isabstract(uml::Activity)


def test_uml::activity_constructor_exists():
    assert callable(uml::Activity.__init__)


def test_uml::activity_constructor_args():
    sig = inspect.signature(uml::Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml::statemachine_is_not_abstract():
    assert not inspect.isabstract(uml::StateMachine)


def test_uml::statemachine_constructor_exists():
    assert callable(uml::StateMachine.__init__)


def test_uml::statemachine_constructor_args():
    sig = inspect.signature(uml::StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "entryPoint",
        "join",
        "initial",
        "fork",
        "choice",
        "deepHistory",
        "junction",
        "terminate",
        "exitPoint",
        "shallowHistory",
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
uml::FinalState_strategy = st.builds(
    uml::FinalState,
)
Vertex_strategy = st.builds(
    Vertex,
)
uml::State_strategy = st.builds(
    uml::State,
)
uml::Pseudostate_strategy = st.builds(
    uml::Pseudostate,
    kind=
        safe_text
)
uml::Region_strategy = st.builds(
    uml::Region,
)
uml::Vertex_strategy = st.builds(
    uml::Vertex,
    name=
        safe_text
)
uml::Trigger_strategy = st.builds(
    uml::Trigger,
    name=
        safe_text
)
uml::Behavior_strategy = st.builds(
    uml::Behavior,
    name=
        safe_text
)
uml::Transition_strategy = st.builds(
    uml::Transition,
    name=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
uml::Activity_strategy = st.builds(
    uml::Activity,
)
uml::StateMachine_strategy = st.builds(
    uml::StateMachine,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=uml::FinalState_strategy)
@settings(max_examples=50)
def test_uml::finalstate_instantiation(instance):
    assert isinstance(instance, uml::FinalState)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=uml::State_strategy)
@settings(max_examples=50)
def test_uml::state_instantiation(instance):
    assert isinstance(instance, uml::State)

@given(instance=uml::Pseudostate_strategy)
@settings(max_examples=50)
def test_uml::pseudostate_instantiation(instance):
    assert isinstance(instance, uml::Pseudostate)

@given(instance=uml::Pseudostate_strategy)
def test_uml::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=uml::Pseudostate_strategy)
def test_uml::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=uml::Region_strategy)
@settings(max_examples=50)
def test_uml::region_instantiation(instance):
    assert isinstance(instance, uml::Region)

@given(instance=uml::Vertex_strategy)
@settings(max_examples=50)
def test_uml::vertex_instantiation(instance):
    assert isinstance(instance, uml::Vertex)

@given(instance=uml::Vertex_strategy)
def test_uml::vertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::Vertex_strategy)
def test_uml::vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml::Trigger_strategy)
@settings(max_examples=50)
def test_uml::trigger_instantiation(instance):
    assert isinstance(instance, uml::Trigger)

@given(instance=uml::Trigger_strategy)
def test_uml::trigger_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::Trigger_strategy)
def test_uml::trigger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml::Behavior_strategy)
@settings(max_examples=50)
def test_uml::behavior_instantiation(instance):
    assert isinstance(instance, uml::Behavior)

@given(instance=uml::Behavior_strategy)
def test_uml::behavior_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::Behavior_strategy)
def test_uml::behavior_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml::Transition_strategy)
@settings(max_examples=50)
def test_uml::transition_instantiation(instance):
    assert isinstance(instance, uml::Transition)

@given(instance=uml::Transition_strategy)
def test_uml::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::Transition_strategy)
def test_uml::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=uml::Activity_strategy)
@settings(max_examples=50)
def test_uml::activity_instantiation(instance):
    assert isinstance(instance, uml::Activity)

@given(instance=uml::StateMachine_strategy)
@settings(max_examples=50)
def test_uml::statemachine_instantiation(instance):
    assert isinstance(instance, uml::StateMachine)

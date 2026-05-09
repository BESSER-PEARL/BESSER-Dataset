import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Transition,
    statemachine::LabeledTransition,
    statemachine::Action,
    Region,
    statemachine::Statemachine,
    Vertex,
    statemachine::State,
    statemachine::Transition,
    statemachine::Vertex,
    statemachine::Region,
    State,
    statemachine::ComplexState,
    statemachine::Pseudostate,
    PseudostateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::labeledtransition_is_not_abstract():
    assert not inspect.isabstract(statemachine::LabeledTransition)


def test_statemachine::labeledtransition_constructor_exists():
    assert callable(statemachine::LabeledTransition.__init__)


def test_statemachine::labeledtransition_constructor_args():
    sig = inspect.signature(statemachine::LabeledTransition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::action_is_not_abstract():
    assert not inspect.isabstract(statemachine::Action)


def test_statemachine::action_constructor_exists():
    assert callable(statemachine::Action.__init__)


def test_statemachine::action_constructor_args():
    sig = inspect.signature(statemachine::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::action_has_name():
    assert hasattr(statemachine::Action, "name")
    descriptor = None
    for klass in statemachine::Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_region_is_not_abstract():
    assert not inspect.isabstract(Region)


def test_region_constructor_exists():
    assert callable(Region.__init__)


def test_region_constructor_args():
    sig = inspect.signature(Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::Statemachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(statemachine::Statemachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(statemachine::Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachine_has_name():
    assert hasattr(statemachine::Statemachine, "name")
    descriptor = None
    for klass in statemachine::Statemachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::state_has_name():
    assert hasattr(statemachine::State, "name")
    descriptor = None
    for klass in statemachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine::transition_has_id():
    assert hasattr(statemachine::Transition, "id")
    descriptor = None
    for klass in statemachine::Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::vertex_is_not_abstract():
    assert not inspect.isabstract(statemachine::Vertex)


def test_statemachine::vertex_constructor_exists():
    assert callable(statemachine::Vertex.__init__)


def test_statemachine::vertex_constructor_args():
    sig = inspect.signature(statemachine::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::region_is_not_abstract():
    assert not inspect.isabstract(statemachine::Region)


def test_statemachine::region_constructor_exists():
    assert callable(statemachine::Region.__init__)


def test_statemachine::region_constructor_args():
    sig = inspect.signature(statemachine::Region.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::complexstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::ComplexState)


def test_statemachine::complexstate_constructor_exists():
    assert callable(statemachine::ComplexState.__init__)


def test_statemachine::complexstate_constructor_args():
    sig = inspect.signature(statemachine::ComplexState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::pseudostate_is_not_abstract():
    assert not inspect.isabstract(statemachine::Pseudostate)


def test_statemachine::pseudostate_constructor_exists():
    assert callable(statemachine::Pseudostate.__init__)


def test_statemachine::pseudostate_constructor_args():
    sig = inspect.signature(statemachine::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachine::pseudostate_has_id():
    assert hasattr(statemachine::Pseudostate, "id")
    descriptor = None
    for klass in statemachine::Pseudostate.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::pseudostate_has_kind():
    assert hasattr(statemachine::Pseudostate, "kind")
    descriptor = None
    for klass in statemachine::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "final",
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
Transition_strategy = st.builds(
    Transition,
)
statemachine::LabeledTransition_strategy = st.builds(
    statemachine::LabeledTransition,
)
statemachine::Action_strategy = st.builds(
    statemachine::Action,
    name=
        safe_text
)
Region_strategy = st.builds(
    Region,
)
statemachine::Statemachine_strategy = st.builds(
    statemachine::Statemachine,
    name=
        safe_text
)
Vertex_strategy = st.builds(
    Vertex,
)
statemachine::State_strategy = st.builds(
    statemachine::State,
    name=
        safe_text
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
    id=
        safe_text
)
statemachine::Vertex_strategy = st.builds(
    statemachine::Vertex,
)
statemachine::Region_strategy = st.builds(
    statemachine::Region,
)
State_strategy = st.builds(
    State,
)
statemachine::ComplexState_strategy = st.builds(
    statemachine::ComplexState,
)
statemachine::Pseudostate_strategy = st.builds(
    statemachine::Pseudostate,
    id=
        safe_text,
    kind=
        safe_text
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=statemachine::LabeledTransition_strategy)
@settings(max_examples=50)
def test_statemachine::labeledtransition_instantiation(instance):
    assert isinstance(instance, statemachine::LabeledTransition)

@given(instance=statemachine::Action_strategy)
@settings(max_examples=50)
def test_statemachine::action_instantiation(instance):
    assert isinstance(instance, statemachine::Action)

@given(instance=statemachine::Action_strategy)
def test_statemachine::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Action_strategy)
def test_statemachine::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=statemachine::Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::Statemachine)

@given(instance=statemachine::Statemachine_strategy)
def test_statemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Statemachine_strategy)
def test_statemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::State_strategy)
def test_statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::State_strategy)
def test_statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=statemachine::Transition_strategy)
def test_statemachine::transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine::Vertex_strategy)
@settings(max_examples=50)
def test_statemachine::vertex_instantiation(instance):
    assert isinstance(instance, statemachine::Vertex)

@given(instance=statemachine::Region_strategy)
@settings(max_examples=50)
def test_statemachine::region_instantiation(instance):
    assert isinstance(instance, statemachine::Region)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine::ComplexState_strategy)
@settings(max_examples=50)
def test_statemachine::complexstate_instantiation(instance):
    assert isinstance(instance, statemachine::ComplexState)

@given(instance=statemachine::Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachine::pseudostate_instantiation(instance):
    assert isinstance(instance, statemachine::Pseudostate)

@given(instance=statemachine::Pseudostate_strategy)
def test_statemachine::pseudostate_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=statemachine::Pseudostate_strategy)
def test_statemachine::pseudostate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine::Pseudostate_strategy)
def test_statemachine::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=statemachine::Pseudostate_strategy)
def test_statemachine::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

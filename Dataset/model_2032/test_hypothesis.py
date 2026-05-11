import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Vertex,
    MySM::Vertex,
    MySM::Pseudostate,
    MySM::State,
    MySM::Region,
    Transition,
    MySM::LabeledTransition,
    State,
    MySM::ComplexSate,
    MySM::Action,
    MySM::Transition,
    Region,
    MySM::Statemachine,
    Pseudokind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_mysm::vertex_is_not_abstract():
    assert not inspect.isabstract(MySM::Vertex)


def test_mysm::vertex_constructor_exists():
    assert callable(MySM::Vertex.__init__)


def test_mysm::vertex_constructor_args():
    sig = inspect.signature(MySM::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_mysm::pseudostate_is_not_abstract():
    assert not inspect.isabstract(MySM::Pseudostate)


def test_mysm::pseudostate_constructor_exists():
    assert callable(MySM::Pseudostate.__init__)


def test_mysm::pseudostate_constructor_args():
    sig = inspect.signature(MySM::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "psId" in params, "Missing parameter 'psId'"

def test_mysm::pseudostate_has_kind():
    assert hasattr(MySM::Pseudostate, "kind")
    descriptor = None
    for klass in MySM::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_mysm::pseudostate_has_psId():
    assert hasattr(MySM::Pseudostate, "psId")
    descriptor = None
    for klass in MySM::Pseudostate.__mro__:
        if "psId" in klass.__dict__:
            descriptor = klass.__dict__["psId"]
            break
    assert isinstance(descriptor, property)



def test_mysm::state_is_not_abstract():
    assert not inspect.isabstract(MySM::State)


def test_mysm::state_constructor_exists():
    assert callable(MySM::State.__init__)


def test_mysm::state_constructor_args():
    sig = inspect.signature(MySM::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mysm::state_has_name():
    assert hasattr(MySM::State, "name")
    descriptor = None
    for klass in MySM::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mysm::region_is_not_abstract():
    assert not inspect.isabstract(MySM::Region)


def test_mysm::region_constructor_exists():
    assert callable(MySM::Region.__init__)


def test_mysm::region_constructor_args():
    sig = inspect.signature(MySM::Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mysm::region_has_name():
    assert hasattr(MySM::Region, "name")
    descriptor = None
    for klass in MySM::Region.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_mysm::labeledtransition_is_not_abstract():
    assert not inspect.isabstract(MySM::LabeledTransition)


def test_mysm::labeledtransition_constructor_exists():
    assert callable(MySM::LabeledTransition.__init__)


def test_mysm::labeledtransition_constructor_args():
    sig = inspect.signature(MySM::LabeledTransition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_mysm::complexsate_is_not_abstract():
    assert not inspect.isabstract(MySM::ComplexSate)


def test_mysm::complexsate_constructor_exists():
    assert callable(MySM::ComplexSate.__init__)


def test_mysm::complexsate_constructor_args():
    sig = inspect.signature(MySM::ComplexSate.__init__)
    params = list(sig.parameters.keys())



def test_mysm::action_is_not_abstract():
    assert not inspect.isabstract(MySM::Action)


def test_mysm::action_constructor_exists():
    assert callable(MySM::Action.__init__)


def test_mysm::action_constructor_args():
    sig = inspect.signature(MySM::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mysm::action_has_name():
    assert hasattr(MySM::Action, "name")
    descriptor = None
    for klass in MySM::Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mysm::transition_is_not_abstract():
    assert not inspect.isabstract(MySM::Transition)


def test_mysm::transition_constructor_exists():
    assert callable(MySM::Transition.__init__)


def test_mysm::transition_constructor_args():
    sig = inspect.signature(MySM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "tId" in params, "Missing parameter 'tId'"

def test_mysm::transition_has_tId():
    assert hasattr(MySM::Transition, "tId")
    descriptor = None
    for klass in MySM::Transition.__mro__:
        if "tId" in klass.__dict__:
            descriptor = klass.__dict__["tId"]
            break
    assert isinstance(descriptor, property)



def test_region_is_not_abstract():
    assert not inspect.isabstract(Region)


def test_region_constructor_exists():
    assert callable(Region.__init__)


def test_region_constructor_args():
    sig = inspect.signature(Region.__init__)
    params = list(sig.parameters.keys())



def test_mysm::statemachine_is_not_abstract():
    assert not inspect.isabstract(MySM::Statemachine)


def test_mysm::statemachine_constructor_exists():
    assert callable(MySM::Statemachine.__init__)


def test_mysm::statemachine_constructor_args():
    sig = inspect.signature(MySM::Statemachine.__init__)
    params = list(sig.parameters.keys())

def test_pseudokind_exists():
    # Check that the Enumeration exists
    assert Pseudokind is not None

def test_pseudokind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Pseudokind]
    expected_literals = [
        "DeepHistory",
        "Exit",
        "Initial",
        "ShallowHistory",
        "End",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Pseudokind"


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
Vertex_strategy = st.builds(
    Vertex,
)
MySM::Vertex_strategy = st.builds(
    MySM::Vertex,
)
MySM::Pseudostate_strategy = st.builds(
    MySM::Pseudostate,
    kind=
        safe_text,
    psId=
        safe_text
)
MySM::State_strategy = st.builds(
    MySM::State,
    name=
        safe_text
)
MySM::Region_strategy = st.builds(
    MySM::Region,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
MySM::LabeledTransition_strategy = st.builds(
    MySM::LabeledTransition,
)
State_strategy = st.builds(
    State,
)
MySM::ComplexSate_strategy = st.builds(
    MySM::ComplexSate,
)
MySM::Action_strategy = st.builds(
    MySM::Action,
    name=
        safe_text
)
MySM::Transition_strategy = st.builds(
    MySM::Transition,
    tId=
        safe_text
)
Region_strategy = st.builds(
    Region,
)
MySM::Statemachine_strategy = st.builds(
    MySM::Statemachine,
)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=MySM::Vertex_strategy)
@settings(max_examples=50)
def test_mysm::vertex_instantiation(instance):
    assert isinstance(instance, MySM::Vertex)

@given(instance=MySM::Pseudostate_strategy)
@settings(max_examples=50)
def test_mysm::pseudostate_instantiation(instance):
    assert isinstance(instance, MySM::Pseudostate)

@given(instance=MySM::Pseudostate_strategy)
def test_mysm::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MySM::Pseudostate_strategy)
def test_mysm::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MySM::Pseudostate_strategy)
def test_mysm::pseudostate_psId_type(instance):
    assert isinstance(instance.psId, str)


@given(instance=MySM::Pseudostate_strategy)
def test_mysm::pseudostate_psId_setter(instance):
    original = instance.psId
    instance.psId = original
    assert instance.psId == original

@given(instance=MySM::State_strategy)
@settings(max_examples=50)
def test_mysm::state_instantiation(instance):
    assert isinstance(instance, MySM::State)

@given(instance=MySM::State_strategy)
def test_mysm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MySM::State_strategy)
def test_mysm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MySM::Region_strategy)
@settings(max_examples=50)
def test_mysm::region_instantiation(instance):
    assert isinstance(instance, MySM::Region)

@given(instance=MySM::Region_strategy)
def test_mysm::region_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MySM::Region_strategy)
def test_mysm::region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=MySM::LabeledTransition_strategy)
@settings(max_examples=50)
def test_mysm::labeledtransition_instantiation(instance):
    assert isinstance(instance, MySM::LabeledTransition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=MySM::ComplexSate_strategy)
@settings(max_examples=50)
def test_mysm::complexsate_instantiation(instance):
    assert isinstance(instance, MySM::ComplexSate)

@given(instance=MySM::Action_strategy)
@settings(max_examples=50)
def test_mysm::action_instantiation(instance):
    assert isinstance(instance, MySM::Action)

@given(instance=MySM::Action_strategy)
def test_mysm::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MySM::Action_strategy)
def test_mysm::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MySM::Transition_strategy)
@settings(max_examples=50)
def test_mysm::transition_instantiation(instance):
    assert isinstance(instance, MySM::Transition)

@given(instance=MySM::Transition_strategy)
def test_mysm::transition_tId_type(instance):
    assert isinstance(instance.tId, str)


@given(instance=MySM::Transition_strategy)
def test_mysm::transition_tId_setter(instance):
    original = instance.tId
    instance.tId = original
    assert instance.tId == original

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=MySM::Statemachine_strategy)
@settings(max_examples=50)
def test_mysm::statemachine_instantiation(instance):
    assert isinstance(instance, MySM::Statemachine)

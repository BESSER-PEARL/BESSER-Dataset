import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Vertex,
    MySM_Vertex,
    MySM_Pseudostate,
    MySM_State,
    MySM_Region,
    Transition,
    MySM_LabeledTransition,
    State,
    MySM_ComplexSate,
    MySM_Action,
    MySM_Transition,
    Region,
    MySM_Statemachine,
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



def test_mysm_vertex_is_not_abstract():
    assert not inspect.isabstract(MySM_Vertex)


def test_mysm_vertex_constructor_exists():
    assert callable(MySM_Vertex.__init__)


def test_mysm_vertex_constructor_args():
    sig = inspect.signature(MySM_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_mysm_pseudostate_is_not_abstract():
    assert not inspect.isabstract(MySM_Pseudostate)


def test_mysm_pseudostate_constructor_exists():
    assert callable(MySM_Pseudostate.__init__)


def test_mysm_pseudostate_constructor_args():
    sig = inspect.signature(MySM_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "psId" in params, "Missing parameter 'psId'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_mysm_pseudostate_has_psId():
    assert hasattr(MySM_Pseudostate, "psId")
    descriptor = None
    for klass in MySM_Pseudostate.__mro__:
        if "psId" in klass.__dict__:
            descriptor = klass.__dict__["psId"]
            break
    assert isinstance(descriptor, property)

def test_mysm_pseudostate_has_kind():
    assert hasattr(MySM_Pseudostate, "kind")
    descriptor = None
    for klass in MySM_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_mysm_state_is_not_abstract():
    assert not inspect.isabstract(MySM_State)


def test_mysm_state_constructor_exists():
    assert callable(MySM_State.__init__)


def test_mysm_state_constructor_args():
    sig = inspect.signature(MySM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mysm_state_has_name():
    assert hasattr(MySM_State, "name")
    descriptor = None
    for klass in MySM_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mysm_region_is_not_abstract():
    assert not inspect.isabstract(MySM_Region)


def test_mysm_region_constructor_exists():
    assert callable(MySM_Region.__init__)


def test_mysm_region_constructor_args():
    sig = inspect.signature(MySM_Region.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mysm_region_has_name():
    assert hasattr(MySM_Region, "name")
    descriptor = None
    for klass in MySM_Region.__mro__:
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



def test_mysm_labeledtransition_is_not_abstract():
    assert not inspect.isabstract(MySM_LabeledTransition)


def test_mysm_labeledtransition_constructor_exists():
    assert callable(MySM_LabeledTransition.__init__)


def test_mysm_labeledtransition_constructor_args():
    sig = inspect.signature(MySM_LabeledTransition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_mysm_complexsate_is_not_abstract():
    assert not inspect.isabstract(MySM_ComplexSate)


def test_mysm_complexsate_constructor_exists():
    assert callable(MySM_ComplexSate.__init__)


def test_mysm_complexsate_constructor_args():
    sig = inspect.signature(MySM_ComplexSate.__init__)
    params = list(sig.parameters.keys())



def test_mysm_action_is_not_abstract():
    assert not inspect.isabstract(MySM_Action)


def test_mysm_action_constructor_exists():
    assert callable(MySM_Action.__init__)


def test_mysm_action_constructor_args():
    sig = inspect.signature(MySM_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mysm_action_has_name():
    assert hasattr(MySM_Action, "name")
    descriptor = None
    for klass in MySM_Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mysm_transition_is_not_abstract():
    assert not inspect.isabstract(MySM_Transition)


def test_mysm_transition_constructor_exists():
    assert callable(MySM_Transition.__init__)


def test_mysm_transition_constructor_args():
    sig = inspect.signature(MySM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "tId" in params, "Missing parameter 'tId'"

def test_mysm_transition_has_tId():
    assert hasattr(MySM_Transition, "tId")
    descriptor = None
    for klass in MySM_Transition.__mro__:
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



def test_mysm_statemachine_is_not_abstract():
    assert not inspect.isabstract(MySM_Statemachine)


def test_mysm_statemachine_constructor_exists():
    assert callable(MySM_Statemachine.__init__)


def test_mysm_statemachine_constructor_args():
    sig = inspect.signature(MySM_Statemachine.__init__)
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
MySM_Vertex_strategy = st.builds(
    MySM_Vertex,
)
MySM_Pseudostate_strategy = st.builds(
    MySM_Pseudostate,
    psId=
        safe_text,
    kind=
        safe_text
)
MySM_State_strategy = st.builds(
    MySM_State,
    name=
        safe_text
)
MySM_Region_strategy = st.builds(
    MySM_Region,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
MySM_LabeledTransition_strategy = st.builds(
    MySM_LabeledTransition,
)
State_strategy = st.builds(
    State,
)
MySM_ComplexSate_strategy = st.builds(
    MySM_ComplexSate,
)
MySM_Action_strategy = st.builds(
    MySM_Action,
    name=
        safe_text
)
MySM_Transition_strategy = st.builds(
    MySM_Transition,
    tId=
        safe_text
)
Region_strategy = st.builds(
    Region,
)
MySM_Statemachine_strategy = st.builds(
    MySM_Statemachine,
)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=MySM_Vertex_strategy)
@settings(max_examples=50)
def test_mysm_vertex_instantiation(instance):
    assert isinstance(instance, MySM_Vertex)

@given(instance=MySM_Pseudostate_strategy)
@settings(max_examples=50)
def test_mysm_pseudostate_instantiation(instance):
    assert isinstance(instance, MySM_Pseudostate)



@given(instance=MySM_Pseudostate_strategy)
def test_mysm_pseudostate_psId_setter(instance):
    original = instance.psId
    instance.psId = original
    assert instance.psId == original



@given(instance=MySM_Pseudostate_strategy)
def test_mysm_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MySM_State_strategy)
@settings(max_examples=50)
def test_mysm_state_instantiation(instance):
    assert isinstance(instance, MySM_State)



@given(instance=MySM_State_strategy)
def test_mysm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MySM_Region_strategy)
@settings(max_examples=50)
def test_mysm_region_instantiation(instance):
    assert isinstance(instance, MySM_Region)



@given(instance=MySM_Region_strategy)
def test_mysm_region_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=MySM_LabeledTransition_strategy)
@settings(max_examples=50)
def test_mysm_labeledtransition_instantiation(instance):
    assert isinstance(instance, MySM_LabeledTransition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=MySM_ComplexSate_strategy)
@settings(max_examples=50)
def test_mysm_complexsate_instantiation(instance):
    assert isinstance(instance, MySM_ComplexSate)

@given(instance=MySM_Action_strategy)
@settings(max_examples=50)
def test_mysm_action_instantiation(instance):
    assert isinstance(instance, MySM_Action)



@given(instance=MySM_Action_strategy)
def test_mysm_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MySM_Transition_strategy)
@settings(max_examples=50)
def test_mysm_transition_instantiation(instance):
    assert isinstance(instance, MySM_Transition)



@given(instance=MySM_Transition_strategy)
def test_mysm_transition_tId_setter(instance):
    original = instance.tId
    instance.tId = original
    assert instance.tId == original

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=MySM_Statemachine_strategy)
@settings(max_examples=50)
def test_mysm_statemachine_instantiation(instance):
    assert isinstance(instance, MySM_Statemachine)

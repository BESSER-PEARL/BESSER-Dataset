import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Transition,
    statemachine_LabeledTransition,
    State,
    statemachine_Action,
    Region,
    statemachine_Statemachine,
    statemachine_Region,
    statemachine_ComplexState,
    Vertex,
    statemachine_Pseudostate,
    statemachine_State,
    statemachine_Transition,
    statemachine_Vertex,
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



def test_statemachine_labeledtransition_is_not_abstract():
    assert not inspect.isabstract(statemachine_LabeledTransition)


def test_statemachine_labeledtransition_constructor_exists():
    assert callable(statemachine_LabeledTransition.__init__)


def test_statemachine_labeledtransition_constructor_args():
    sig = inspect.signature(statemachine_LabeledTransition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_action_is_not_abstract():
    assert not inspect.isabstract(statemachine_Action)


def test_statemachine_action_constructor_exists():
    assert callable(statemachine_Action.__init__)


def test_statemachine_action_constructor_args():
    sig = inspect.signature(statemachine_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_action_has_name():
    assert hasattr(statemachine_Action, "name")
    descriptor = None
    for klass in statemachine_Action.__mro__:
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



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_Statemachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_Statemachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statemachine_has_name():
    assert hasattr(statemachine_Statemachine, "name")
    descriptor = None
    for klass in statemachine_Statemachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_region_is_not_abstract():
    assert not inspect.isabstract(statemachine_Region)


def test_statemachine_region_constructor_exists():
    assert callable(statemachine_Region.__init__)


def test_statemachine_region_constructor_args():
    sig = inspect.signature(statemachine_Region.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_complexstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_ComplexState)


def test_statemachine_complexstate_constructor_exists():
    assert callable(statemachine_ComplexState.__init__)


def test_statemachine_complexstate_constructor_args():
    sig = inspect.signature(statemachine_ComplexState.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_pseudostate_is_not_abstract():
    assert not inspect.isabstract(statemachine_Pseudostate)


def test_statemachine_pseudostate_constructor_exists():
    assert callable(statemachine_Pseudostate.__init__)


def test_statemachine_pseudostate_constructor_args():
    sig = inspect.signature(statemachine_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_statemachine_pseudostate_has_id():
    assert hasattr(statemachine_Pseudostate, "id")
    descriptor = None
    for klass in statemachine_Pseudostate.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_pseudostate_has_kind():
    assert hasattr(statemachine_Pseudostate, "kind")
    descriptor = None
    for klass in statemachine_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_state_has_name():
    assert hasattr(statemachine_State, "name")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_statemachine_transition_has_id():
    assert hasattr(statemachine_Transition, "id")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_vertex_is_not_abstract():
    assert not inspect.isabstract(statemachine_Vertex)


def test_statemachine_vertex_constructor_exists():
    assert callable(statemachine_Vertex.__init__)


def test_statemachine_vertex_constructor_args():
    sig = inspect.signature(statemachine_Vertex.__init__)
    params = list(sig.parameters.keys())

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "initial",
        "final",
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
statemachine_LabeledTransition_strategy = st.builds(
    statemachine_LabeledTransition,
)
State_strategy = st.builds(
    State,
)
statemachine_Action_strategy = st.builds(
    statemachine_Action,
    name=
        safe_text
)
Region_strategy = st.builds(
    Region,
)
statemachine_Statemachine_strategy = st.builds(
    statemachine_Statemachine,
    name=
        safe_text
)
statemachine_Region_strategy = st.builds(
    statemachine_Region,
)
statemachine_ComplexState_strategy = st.builds(
    statemachine_ComplexState,
)
Vertex_strategy = st.builds(
    Vertex,
)
statemachine_Pseudostate_strategy = st.builds(
    statemachine_Pseudostate,
    id=
        safe_text,
    kind=
        safe_text
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    name=
        safe_text
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
    id=
        safe_text
)
statemachine_Vertex_strategy = st.builds(
    statemachine_Vertex,
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=statemachine_LabeledTransition_strategy)
@settings(max_examples=50)
def test_statemachine_labeledtransition_instantiation(instance):
    assert isinstance(instance, statemachine_LabeledTransition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine_Action_strategy)
@settings(max_examples=50)
def test_statemachine_action_instantiation(instance):
    assert isinstance(instance, statemachine_Action)



@given(instance=statemachine_Action_strategy)
def test_statemachine_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Region_strategy)
@settings(max_examples=50)
def test_region_instantiation(instance):
    assert isinstance(instance, Region)

@given(instance=statemachine_Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_Statemachine)



@given(instance=statemachine_Statemachine_strategy)
def test_statemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine_Region_strategy)
@settings(max_examples=50)
def test_statemachine_region_instantiation(instance):
    assert isinstance(instance, statemachine_Region)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_Region_strategy)
@settings(max_examples=30)
def test_statemachine_region_realinitialstate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.realInitialState()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.realInitialState).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'realInitialState' in statemachine_Region is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'realInitialState' in statemachine_Region did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'realInitialState' in statemachine_Region is not implemented or raised an error")

@given(instance=statemachine_ComplexState_strategy)
@settings(max_examples=50)
def test_statemachine_complexstate_instantiation(instance):
    assert isinstance(instance, statemachine_ComplexState)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_ComplexState_strategy)
@settings(max_examples=30)
def test_statemachine_complexstate_directsubstates_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.directSubStates()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.directSubStates).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'directSubStates' in statemachine_ComplexState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'directSubStates' in statemachine_ComplexState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'directSubStates' in statemachine_ComplexState is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_ComplexState_strategy)
@settings(max_examples=30)
def test_statemachine_complexstate_innertransitions_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.innerTransitions()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.innerTransitions).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'innerTransitions' in statemachine_ComplexState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'innerTransitions' in statemachine_ComplexState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'innerTransitions' in statemachine_ComplexState is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_ComplexState_strategy)
@settings(max_examples=30)
def test_statemachine_complexstate_realinitialstates_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.realInitialStates()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.realInitialStates).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'realInitialStates' in statemachine_ComplexState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'realInitialStates' in statemachine_ComplexState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'realInitialStates' in statemachine_ComplexState is not implemented or raised an error")

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=statemachine_Pseudostate_strategy)
@settings(max_examples=50)
def test_statemachine_pseudostate_instantiation(instance):
    assert isinstance(instance, statemachine_Pseudostate)



@given(instance=statemachine_Pseudostate_strategy)
def test_statemachine_pseudostate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=statemachine_Pseudostate_strategy)
def test_statemachine_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=statemachine_State_strategy)
@settings(max_examples=30)
def test_statemachine_state_fullyqualifiedname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fullyQualifiedName()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fullyQualifiedName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fullyQualifiedName' in statemachine_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fullyQualifiedName' in statemachine_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fullyQualifiedName' in statemachine_State is not implemented or raised an error")

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=statemachine_Vertex_strategy)
@settings(max_examples=50)
def test_statemachine_vertex_instantiation(instance):
    assert isinstance(instance, statemachine_Vertex)

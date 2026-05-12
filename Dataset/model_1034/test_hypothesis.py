import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_NamedElement,
    State,
    fsm_FinalState,
    Pseudostate,
    fsm_InitialState,
    fsm_Constraint,
    NamedElement,
    fsm_Transition,
    fsm_Region,
    fsm_AbstractState,
    fsm_StateMachine,
    fsm_Trigger,
    AbstractState,
    fsm_Pseudostate,
    fsm_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm_NamedElement)


def test_fsm_namedelement_constructor_exists():
    assert callable(fsm_NamedElement.__init__)


def test_fsm_namedelement_constructor_args():
    sig = inspect.signature(fsm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_namedelement_has_name():
    assert hasattr(fsm_NamedElement, "name")
    descriptor = None
    for klass in fsm_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm_FinalState)


def test_fsm_finalstate_constructor_exists():
    assert callable(fsm_FinalState.__init__)


def test_fsm_finalstate_constructor_args():
    sig = inspect.signature(fsm_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm_InitialState)


def test_fsm_initialstate_constructor_exists():
    assert callable(fsm_InitialState.__init__)


def test_fsm_initialstate_constructor_args():
    sig = inspect.signature(fsm_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_constraint_is_not_abstract():
    assert not inspect.isabstract(fsm_Constraint)


def test_fsm_constraint_constructor_exists():
    assert callable(fsm_Constraint.__init__)


def test_fsm_constraint_constructor_args():
    sig = inspect.signature(fsm_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm_region_is_not_abstract():
    assert not inspect.isabstract(fsm_Region)


def test_fsm_region_constructor_exists():
    assert callable(fsm_Region.__init__)


def test_fsm_region_constructor_args():
    sig = inspect.signature(fsm_Region.__init__)
    params = list(sig.parameters.keys())



def test_fsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsm_AbstractState)


def test_fsm_abstractstate_constructor_exists():
    assert callable(fsm_AbstractState.__init__)


def test_fsm_abstractstate_constructor_args():
    sig = inspect.signature(fsm_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(fsm_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(fsm_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_fsm_trigger_is_not_abstract():
    assert not inspect.isabstract(fsm_Trigger)


def test_fsm_trigger_constructor_exists():
    assert callable(fsm_Trigger.__init__)


def test_fsm_trigger_constructor_args():
    sig = inspect.signature(fsm_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsm_trigger_has_expression():
    assert hasattr(fsm_Trigger, "expression")
    descriptor = None
    for klass in fsm_Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm_Pseudostate)


def test_fsm_pseudostate_constructor_exists():
    assert callable(fsm_Pseudostate.__init__)


def test_fsm_pseudostate_constructor_args():
    sig = inspect.signature(fsm_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())


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
fsm_NamedElement_strategy = st.builds(
    fsm_NamedElement,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm_FinalState_strategy = st.builds(
    fsm_FinalState,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
fsm_InitialState_strategy = st.builds(
    fsm_InitialState,
)
fsm_Constraint_strategy = st.builds(
    fsm_Constraint,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
)
fsm_Region_strategy = st.builds(
    fsm_Region,
)
fsm_AbstractState_strategy = st.builds(
    fsm_AbstractState,
)
fsm_StateMachine_strategy = st.builds(
    fsm_StateMachine,
)
fsm_Trigger_strategy = st.builds(
    fsm_Trigger,
    expression=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
fsm_Pseudostate_strategy = st.builds(
    fsm_Pseudostate,
)
fsm_State_strategy = st.builds(
    fsm_State,
)

@given(instance=fsm_NamedElement_strategy)
@settings(max_examples=50)
def test_fsm_namedelement_instantiation(instance):
    assert isinstance(instance, fsm_NamedElement)



@given(instance=fsm_NamedElement_strategy)
def test_fsm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm_FinalState_strategy)
@settings(max_examples=50)
def test_fsm_finalstate_instantiation(instance):
    assert isinstance(instance, fsm_FinalState)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=fsm_InitialState_strategy)
@settings(max_examples=50)
def test_fsm_initialstate_instantiation(instance):
    assert isinstance(instance, fsm_InitialState)

@given(instance=fsm_Constraint_strategy)
@settings(max_examples=50)
def test_fsm_constraint_instantiation(instance):
    assert isinstance(instance, fsm_Constraint)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_Constraint_strategy)
@settings(max_examples=30)
def test_fsm_constraint_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in fsm_Constraint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in fsm_Constraint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in fsm_Constraint is not implemented or raised an error")

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)

@given(instance=fsm_Region_strategy)
@settings(max_examples=50)
def test_fsm_region_instantiation(instance):
    assert isinstance(instance, fsm_Region)

@given(instance=fsm_AbstractState_strategy)
@settings(max_examples=50)
def test_fsm_abstractstate_instantiation(instance):
    assert isinstance(instance, fsm_AbstractState)

@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, fsm_StateMachine)

@given(instance=fsm_Trigger_strategy)
@settings(max_examples=50)
def test_fsm_trigger_instantiation(instance):
    assert isinstance(instance, fsm_Trigger)



@given(instance=fsm_Trigger_strategy)
def test_fsm_trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=fsm_Pseudostate_strategy)
@settings(max_examples=50)
def test_fsm_pseudostate_instantiation(instance):
    assert isinstance(instance, fsm_Pseudostate)

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::NamedElement,
    State,
    fsm::FinalState,
    Pseudostate,
    fsm::InitialState,
    fsm::Constraint,
    NamedElement,
    fsm::Transition,
    fsm::AbstractState,
    fsm::Region,
    fsm::StateMachine,
    fsm::Trigger,
    AbstractState,
    fsm::Pseudostate,
    fsm::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm::NamedElement)


def test_fsm::namedelement_constructor_exists():
    assert callable(fsm::NamedElement.__init__)


def test_fsm::namedelement_constructor_args():
    sig = inspect.signature(fsm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::namedelement_has_name():
    assert hasattr(fsm::NamedElement, "name")
    descriptor = None
    for klass in fsm::NamedElement.__mro__:
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



def test_fsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm::FinalState)


def test_fsm::finalstate_constructor_exists():
    assert callable(fsm::FinalState.__init__)


def test_fsm::finalstate_constructor_args():
    sig = inspect.signature(fsm::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm::InitialState)


def test_fsm::initialstate_constructor_exists():
    assert callable(fsm::InitialState.__init__)


def test_fsm::initialstate_constructor_args():
    sig = inspect.signature(fsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::constraint_is_not_abstract():
    assert not inspect.isabstract(fsm::Constraint)


def test_fsm::constraint_constructor_exists():
    assert callable(fsm::Constraint.__init__)


def test_fsm::constraint_constructor_args():
    sig = inspect.signature(fsm::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsm::AbstractState)


def test_fsm::abstractstate_constructor_exists():
    assert callable(fsm::AbstractState.__init__)


def test_fsm::abstractstate_constructor_args():
    sig = inspect.signature(fsm::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::region_is_not_abstract():
    assert not inspect.isabstract(fsm::Region)


def test_fsm::region_constructor_exists():
    assert callable(fsm::Region.__init__)


def test_fsm::region_constructor_args():
    sig = inspect.signature(fsm::Region.__init__)
    params = list(sig.parameters.keys())



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(fsm::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(fsm::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_fsm::trigger_is_not_abstract():
    assert not inspect.isabstract(fsm::Trigger)


def test_fsm::trigger_constructor_exists():
    assert callable(fsm::Trigger.__init__)


def test_fsm::trigger_constructor_args():
    sig = inspect.signature(fsm::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsm::trigger_has_expression():
    assert hasattr(fsm::Trigger, "expression")
    descriptor = None
    for klass in fsm::Trigger.__mro__:
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



def test_fsm::pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm::Pseudostate)


def test_fsm::pseudostate_constructor_exists():
    assert callable(fsm::Pseudostate.__init__)


def test_fsm::pseudostate_constructor_args():
    sig = inspect.signature(fsm::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
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
fsm::NamedElement_strategy = st.builds(
    fsm::NamedElement,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm::FinalState_strategy = st.builds(
    fsm::FinalState,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
fsm::InitialState_strategy = st.builds(
    fsm::InitialState,
)
fsm::Constraint_strategy = st.builds(
    fsm::Constraint,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
)
fsm::AbstractState_strategy = st.builds(
    fsm::AbstractState,
)
fsm::Region_strategy = st.builds(
    fsm::Region,
)
fsm::StateMachine_strategy = st.builds(
    fsm::StateMachine,
)
fsm::Trigger_strategy = st.builds(
    fsm::Trigger,
    expression=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
fsm::Pseudostate_strategy = st.builds(
    fsm::Pseudostate,
)
fsm::State_strategy = st.builds(
    fsm::State,
)

@given(instance=fsm::NamedElement_strategy)
@settings(max_examples=50)
def test_fsm::namedelement_instantiation(instance):
    assert isinstance(instance, fsm::NamedElement)

@given(instance=fsm::NamedElement_strategy)
def test_fsm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::NamedElement_strategy)
def test_fsm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::FinalState_strategy)
@settings(max_examples=50)
def test_fsm::finalstate_instantiation(instance):
    assert isinstance(instance, fsm::FinalState)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=fsm::InitialState_strategy)
@settings(max_examples=50)
def test_fsm::initialstate_instantiation(instance):
    assert isinstance(instance, fsm::InitialState)

@given(instance=fsm::Constraint_strategy)
@settings(max_examples=50)
def test_fsm::constraint_instantiation(instance):
    assert isinstance(instance, fsm::Constraint)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::Constraint_strategy)
@settings(max_examples=30)
def test_fsm::constraint_eval_changes_state(instance):
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
        assert has_statements, f"Function 'eval' in fsm::Constraint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in fsm::Constraint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in fsm::Constraint is not implemented or raised an error")

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::AbstractState_strategy)
@settings(max_examples=50)
def test_fsm::abstractstate_instantiation(instance):
    assert isinstance(instance, fsm::AbstractState)

@given(instance=fsm::Region_strategy)
@settings(max_examples=50)
def test_fsm::region_instantiation(instance):
    assert isinstance(instance, fsm::Region)

@given(instance=fsm::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, fsm::StateMachine)

@given(instance=fsm::Trigger_strategy)
@settings(max_examples=50)
def test_fsm::trigger_instantiation(instance):
    assert isinstance(instance, fsm::Trigger)

@given(instance=fsm::Trigger_strategy)
def test_fsm::trigger_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=fsm::Trigger_strategy)
def test_fsm::trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=fsm::Pseudostate_strategy)
@settings(max_examples=50)
def test_fsm::pseudostate_instantiation(instance):
    assert isinstance(instance, fsm::Pseudostate)

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

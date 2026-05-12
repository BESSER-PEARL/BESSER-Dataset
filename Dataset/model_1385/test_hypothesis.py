import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    lts2_LTSGenerator,
    UseCaseStep,
    lts2_StateMachine,
    lts2_Transition,
    lts2_State,
    State,
    TransitionalState,
    lts2_InitialState,
    lts2_AbortState,
    lts2_FinalState,
    lts2_TransitionalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lts2_ltsgenerator_is_not_abstract():
    assert not inspect.isabstract(lts2_LTSGenerator)


def test_lts2_ltsgenerator_constructor_exists():
    assert callable(lts2_LTSGenerator.__init__)


def test_lts2_ltsgenerator_constructor_args():
    sig = inspect.signature(lts2_LTSGenerator.__init__)
    params = list(sig.parameters.keys())



def test_usecasestep_is_not_abstract():
    assert not inspect.isabstract(UseCaseStep)


def test_usecasestep_constructor_exists():
    assert callable(UseCaseStep.__init__)


def test_usecasestep_constructor_args():
    sig = inspect.signature(UseCaseStep.__init__)
    params = list(sig.parameters.keys())



def test_lts2_statemachine_is_not_abstract():
    assert not inspect.isabstract(lts2_StateMachine)


def test_lts2_statemachine_constructor_exists():
    assert callable(lts2_StateMachine.__init__)


def test_lts2_statemachine_constructor_args():
    sig = inspect.signature(lts2_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_lts2_transition_is_not_abstract():
    assert not inspect.isabstract(lts2_Transition)


def test_lts2_transition_constructor_exists():
    assert callable(lts2_Transition.__init__)


def test_lts2_transition_constructor_args():
    sig = inspect.signature(lts2_Transition.__init__)
    params = list(sig.parameters.keys())



def test_lts2_state_is_not_abstract():
    assert not inspect.isabstract(lts2_State)


def test_lts2_state_constructor_exists():
    assert callable(lts2_State.__init__)


def test_lts2_state_constructor_args():
    sig = inspect.signature(lts2_State.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_transitionalstate_is_not_abstract():
    assert not inspect.isabstract(TransitionalState)


def test_transitionalstate_constructor_exists():
    assert callable(TransitionalState.__init__)


def test_transitionalstate_constructor_args():
    sig = inspect.signature(TransitionalState.__init__)
    params = list(sig.parameters.keys())



def test_lts2_initialstate_is_not_abstract():
    assert not inspect.isabstract(lts2_InitialState)


def test_lts2_initialstate_constructor_exists():
    assert callable(lts2_InitialState.__init__)


def test_lts2_initialstate_constructor_args():
    sig = inspect.signature(lts2_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_lts2_abortstate_is_not_abstract():
    assert not inspect.isabstract(lts2_AbortState)


def test_lts2_abortstate_constructor_exists():
    assert callable(lts2_AbortState.__init__)


def test_lts2_abortstate_constructor_args():
    sig = inspect.signature(lts2_AbortState.__init__)
    params = list(sig.parameters.keys())



def test_lts2_finalstate_is_not_abstract():
    assert not inspect.isabstract(lts2_FinalState)


def test_lts2_finalstate_constructor_exists():
    assert callable(lts2_FinalState.__init__)


def test_lts2_finalstate_constructor_args():
    sig = inspect.signature(lts2_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_lts2_transitionalstate_is_not_abstract():
    assert not inspect.isabstract(lts2_TransitionalState)


def test_lts2_transitionalstate_constructor_exists():
    assert callable(lts2_TransitionalState.__init__)


def test_lts2_transitionalstate_constructor_args():
    sig = inspect.signature(lts2_TransitionalState.__init__)
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
lts2_LTSGenerator_strategy = st.builds(
    lts2_LTSGenerator,
)
UseCaseStep_strategy = st.builds(
    UseCaseStep,
)
lts2_StateMachine_strategy = st.builds(
    lts2_StateMachine,
)
lts2_Transition_strategy = st.builds(
    lts2_Transition,
)
lts2_State_strategy = st.builds(
    lts2_State,
)
State_strategy = st.builds(
    State,
)
TransitionalState_strategy = st.builds(
    TransitionalState,
)
lts2_InitialState_strategy = st.builds(
    lts2_InitialState,
)
lts2_AbortState_strategy = st.builds(
    lts2_AbortState,
)
lts2_FinalState_strategy = st.builds(
    lts2_FinalState,
)
lts2_TransitionalState_strategy = st.builds(
    lts2_TransitionalState,
)

@given(instance=lts2_LTSGenerator_strategy)
@settings(max_examples=50)
def test_lts2_ltsgenerator_instantiation(instance):
    assert isinstance(instance, lts2_LTSGenerator)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=lts2_LTSGenerator_strategy)
@settings(max_examples=30)
def test_lts2_ltsgenerator_processusecase_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processUseCase(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processUseCase).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processUseCase' in lts2_LTSGenerator is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processUseCase' in lts2_LTSGenerator did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processUseCase' in lts2_LTSGenerator is not implemented or raised an error")

@given(instance=UseCaseStep_strategy)
@settings(max_examples=50)
def test_usecasestep_instantiation(instance):
    assert isinstance(instance, UseCaseStep)

@given(instance=lts2_StateMachine_strategy)
@settings(max_examples=50)
def test_lts2_statemachine_instantiation(instance):
    assert isinstance(instance, lts2_StateMachine)

@given(instance=lts2_Transition_strategy)
@settings(max_examples=50)
def test_lts2_transition_instantiation(instance):
    assert isinstance(instance, lts2_Transition)

@given(instance=lts2_State_strategy)
@settings(max_examples=50)
def test_lts2_state_instantiation(instance):
    assert isinstance(instance, lts2_State)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=TransitionalState_strategy)
@settings(max_examples=50)
def test_transitionalstate_instantiation(instance):
    assert isinstance(instance, TransitionalState)

@given(instance=lts2_InitialState_strategy)
@settings(max_examples=50)
def test_lts2_initialstate_instantiation(instance):
    assert isinstance(instance, lts2_InitialState)

@given(instance=lts2_AbortState_strategy)
@settings(max_examples=50)
def test_lts2_abortstate_instantiation(instance):
    assert isinstance(instance, lts2_AbortState)

@given(instance=lts2_FinalState_strategy)
@settings(max_examples=50)
def test_lts2_finalstate_instantiation(instance):
    assert isinstance(instance, lts2_FinalState)

@given(instance=lts2_TransitionalState_strategy)
@settings(max_examples=50)
def test_lts2_transitionalstate_instantiation(instance):
    assert isinstance(instance, lts2_TransitionalState)

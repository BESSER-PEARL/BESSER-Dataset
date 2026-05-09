import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lts2::LTSGenerator,
    UseCaseStep,
    lts2::StateMachine,
    lts2::Transition,
    lts2::State,
    State,
    TransitionalState,
    lts2::InitialState,
    lts2::AbortState,
    lts2::FinalState,
    lts2::TransitionalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lts2::ltsgenerator_is_not_abstract():
    assert not inspect.isabstract(lts2::LTSGenerator)


def test_lts2::ltsgenerator_constructor_exists():
    assert callable(lts2::LTSGenerator.__init__)


def test_lts2::ltsgenerator_constructor_args():
    sig = inspect.signature(lts2::LTSGenerator.__init__)
    params = list(sig.parameters.keys())



def test_usecasestep_is_not_abstract():
    assert not inspect.isabstract(UseCaseStep)


def test_usecasestep_constructor_exists():
    assert callable(UseCaseStep.__init__)


def test_usecasestep_constructor_args():
    sig = inspect.signature(UseCaseStep.__init__)
    params = list(sig.parameters.keys())



def test_lts2::statemachine_is_not_abstract():
    assert not inspect.isabstract(lts2::StateMachine)


def test_lts2::statemachine_constructor_exists():
    assert callable(lts2::StateMachine.__init__)


def test_lts2::statemachine_constructor_args():
    sig = inspect.signature(lts2::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_lts2::transition_is_not_abstract():
    assert not inspect.isabstract(lts2::Transition)


def test_lts2::transition_constructor_exists():
    assert callable(lts2::Transition.__init__)


def test_lts2::transition_constructor_args():
    sig = inspect.signature(lts2::Transition.__init__)
    params = list(sig.parameters.keys())



def test_lts2::state_is_not_abstract():
    assert not inspect.isabstract(lts2::State)


def test_lts2::state_constructor_exists():
    assert callable(lts2::State.__init__)


def test_lts2::state_constructor_args():
    sig = inspect.signature(lts2::State.__init__)
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



def test_lts2::initialstate_is_not_abstract():
    assert not inspect.isabstract(lts2::InitialState)


def test_lts2::initialstate_constructor_exists():
    assert callable(lts2::InitialState.__init__)


def test_lts2::initialstate_constructor_args():
    sig = inspect.signature(lts2::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_lts2::abortstate_is_not_abstract():
    assert not inspect.isabstract(lts2::AbortState)


def test_lts2::abortstate_constructor_exists():
    assert callable(lts2::AbortState.__init__)


def test_lts2::abortstate_constructor_args():
    sig = inspect.signature(lts2::AbortState.__init__)
    params = list(sig.parameters.keys())



def test_lts2::finalstate_is_not_abstract():
    assert not inspect.isabstract(lts2::FinalState)


def test_lts2::finalstate_constructor_exists():
    assert callable(lts2::FinalState.__init__)


def test_lts2::finalstate_constructor_args():
    sig = inspect.signature(lts2::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_lts2::transitionalstate_is_not_abstract():
    assert not inspect.isabstract(lts2::TransitionalState)


def test_lts2::transitionalstate_constructor_exists():
    assert callable(lts2::TransitionalState.__init__)


def test_lts2::transitionalstate_constructor_args():
    sig = inspect.signature(lts2::TransitionalState.__init__)
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
lts2::LTSGenerator_strategy = st.builds(
    lts2::LTSGenerator,
)
UseCaseStep_strategy = st.builds(
    UseCaseStep,
)
lts2::StateMachine_strategy = st.builds(
    lts2::StateMachine,
)
lts2::Transition_strategy = st.builds(
    lts2::Transition,
)
lts2::State_strategy = st.builds(
    lts2::State,
)
State_strategy = st.builds(
    State,
)
TransitionalState_strategy = st.builds(
    TransitionalState,
)
lts2::InitialState_strategy = st.builds(
    lts2::InitialState,
)
lts2::AbortState_strategy = st.builds(
    lts2::AbortState,
)
lts2::FinalState_strategy = st.builds(
    lts2::FinalState,
)
lts2::TransitionalState_strategy = st.builds(
    lts2::TransitionalState,
)

@given(instance=lts2::LTSGenerator_strategy)
@settings(max_examples=50)
def test_lts2::ltsgenerator_instantiation(instance):
    assert isinstance(instance, lts2::LTSGenerator)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=lts2::LTSGenerator_strategy)
@settings(max_examples=30)
def test_lts2::ltsgenerator_processusecase_changes_state(instance):
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
        assert has_statements, f"Function 'processUseCase' in lts2::LTSGenerator is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processUseCase' in lts2::LTSGenerator did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processUseCase' in lts2::LTSGenerator is not implemented or raised an error")

@given(instance=UseCaseStep_strategy)
@settings(max_examples=50)
def test_usecasestep_instantiation(instance):
    assert isinstance(instance, UseCaseStep)

@given(instance=lts2::StateMachine_strategy)
@settings(max_examples=50)
def test_lts2::statemachine_instantiation(instance):
    assert isinstance(instance, lts2::StateMachine)

@given(instance=lts2::Transition_strategy)
@settings(max_examples=50)
def test_lts2::transition_instantiation(instance):
    assert isinstance(instance, lts2::Transition)

@given(instance=lts2::State_strategy)
@settings(max_examples=50)
def test_lts2::state_instantiation(instance):
    assert isinstance(instance, lts2::State)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=TransitionalState_strategy)
@settings(max_examples=50)
def test_transitionalstate_instantiation(instance):
    assert isinstance(instance, TransitionalState)

@given(instance=lts2::InitialState_strategy)
@settings(max_examples=50)
def test_lts2::initialstate_instantiation(instance):
    assert isinstance(instance, lts2::InitialState)

@given(instance=lts2::AbortState_strategy)
@settings(max_examples=50)
def test_lts2::abortstate_instantiation(instance):
    assert isinstance(instance, lts2::AbortState)

@given(instance=lts2::FinalState_strategy)
@settings(max_examples=50)
def test_lts2::finalstate_instantiation(instance):
    assert isinstance(instance, lts2::FinalState)

@given(instance=lts2::TransitionalState_strategy)
@settings(max_examples=50)
def test_lts2::transitionalstate_instantiation(instance):
    assert isinstance(instance, lts2::TransitionalState)

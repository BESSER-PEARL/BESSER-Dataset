import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FinalState,
    GState,
    gfsm::GFinalState,
    gfsm::IntOperation,
    State,
    gfsm::GState,
    gfsm::BooleanExpression,
    Transition,
    gfsm::GTransition,
    FSM,
    gfsm::GFSM,
    InitialState,
    gfsm::GInitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_finalstate_is_not_abstract():
    assert not inspect.isabstract(FinalState)


def test_finalstate_constructor_exists():
    assert callable(FinalState.__init__)


def test_finalstate_constructor_args():
    sig = inspect.signature(FinalState.__init__)
    params = list(sig.parameters.keys())



def test_gstate_is_not_abstract():
    assert not inspect.isabstract(GState)


def test_gstate_constructor_exists():
    assert callable(GState.__init__)


def test_gstate_constructor_args():
    sig = inspect.signature(GState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::gfinalstate_is_not_abstract():
    assert not inspect.isabstract(gfsm::GFinalState)


def test_gfsm::gfinalstate_constructor_exists():
    assert callable(gfsm::GFinalState.__init__)


def test_gfsm::gfinalstate_constructor_args():
    sig = inspect.signature(gfsm::GFinalState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::intoperation_is_not_abstract():
    assert not inspect.isabstract(gfsm::IntOperation)


def test_gfsm::intoperation_constructor_exists():
    assert callable(gfsm::IntOperation.__init__)


def test_gfsm::intoperation_constructor_args():
    sig = inspect.signature(gfsm::IntOperation.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::gstate_is_not_abstract():
    assert not inspect.isabstract(gfsm::GState)


def test_gfsm::gstate_constructor_exists():
    assert callable(gfsm::GState.__init__)


def test_gfsm::gstate_constructor_args():
    sig = inspect.signature(gfsm::GState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm::BooleanExpression)


def test_gfsm::booleanexpression_constructor_exists():
    assert callable(gfsm::BooleanExpression.__init__)


def test_gfsm::booleanexpression_constructor_args():
    sig = inspect.signature(gfsm::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::gtransition_is_not_abstract():
    assert not inspect.isabstract(gfsm::GTransition)


def test_gfsm::gtransition_constructor_exists():
    assert callable(gfsm::GTransition.__init__)


def test_gfsm::gtransition_constructor_args():
    sig = inspect.signature(gfsm::GTransition.__init__)
    params = list(sig.parameters.keys())



def test_fsm_is_not_abstract():
    assert not inspect.isabstract(FSM)


def test_fsm_constructor_exists():
    assert callable(FSM.__init__)


def test_fsm_constructor_args():
    sig = inspect.signature(FSM.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::gfsm_is_not_abstract():
    assert not inspect.isabstract(gfsm::GFSM)


def test_gfsm::gfsm_constructor_exists():
    assert callable(gfsm::GFSM.__init__)


def test_gfsm::gfsm_constructor_args():
    sig = inspect.signature(gfsm::GFSM.__init__)
    params = list(sig.parameters.keys())



def test_initialstate_is_not_abstract():
    assert not inspect.isabstract(InitialState)


def test_initialstate_constructor_exists():
    assert callable(InitialState.__init__)


def test_initialstate_constructor_args():
    sig = inspect.signature(InitialState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm::ginitialstate_is_not_abstract():
    assert not inspect.isabstract(gfsm::GInitialState)


def test_gfsm::ginitialstate_constructor_exists():
    assert callable(gfsm::GInitialState.__init__)


def test_gfsm::ginitialstate_constructor_args():
    sig = inspect.signature(gfsm::GInitialState.__init__)
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
FinalState_strategy = st.builds(
    FinalState,
)
GState_strategy = st.builds(
    GState,
)
gfsm::GFinalState_strategy = st.builds(
    gfsm::GFinalState,
)
gfsm::IntOperation_strategy = st.builds(
    gfsm::IntOperation,
)
State_strategy = st.builds(
    State,
)
gfsm::GState_strategy = st.builds(
    gfsm::GState,
)
gfsm::BooleanExpression_strategy = st.builds(
    gfsm::BooleanExpression,
)
Transition_strategy = st.builds(
    Transition,
)
gfsm::GTransition_strategy = st.builds(
    gfsm::GTransition,
)
FSM_strategy = st.builds(
    FSM,
)
gfsm::GFSM_strategy = st.builds(
    gfsm::GFSM,
)
InitialState_strategy = st.builds(
    InitialState,
)
gfsm::GInitialState_strategy = st.builds(
    gfsm::GInitialState,
)

@given(instance=FinalState_strategy)
@settings(max_examples=50)
def test_finalstate_instantiation(instance):
    assert isinstance(instance, FinalState)

@given(instance=GState_strategy)
@settings(max_examples=50)
def test_gstate_instantiation(instance):
    assert isinstance(instance, GState)

@given(instance=gfsm::GFinalState_strategy)
@settings(max_examples=50)
def test_gfsm::gfinalstate_instantiation(instance):
    assert isinstance(instance, gfsm::GFinalState)

@given(instance=gfsm::IntOperation_strategy)
@settings(max_examples=50)
def test_gfsm::intoperation_instantiation(instance):
    assert isinstance(instance, gfsm::IntOperation)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=gfsm::GState_strategy)
@settings(max_examples=50)
def test_gfsm::gstate_instantiation(instance):
    assert isinstance(instance, gfsm::GState)

@given(instance=gfsm::BooleanExpression_strategy)
@settings(max_examples=50)
def test_gfsm::booleanexpression_instantiation(instance):
    assert isinstance(instance, gfsm::BooleanExpression)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=gfsm::GTransition_strategy)
@settings(max_examples=50)
def test_gfsm::gtransition_instantiation(instance):
    assert isinstance(instance, gfsm::GTransition)

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=gfsm::GFSM_strategy)
@settings(max_examples=50)
def test_gfsm::gfsm_instantiation(instance):
    assert isinstance(instance, gfsm::GFSM)

@given(instance=InitialState_strategy)
@settings(max_examples=50)
def test_initialstate_instantiation(instance):
    assert isinstance(instance, InitialState)

@given(instance=gfsm::GInitialState_strategy)
@settings(max_examples=50)
def test_gfsm::ginitialstate_instantiation(instance):
    assert isinstance(instance, gfsm::GInitialState)

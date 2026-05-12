import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FinalState,
    GState,
    gfsm_GFinalState,
    gfsm_IntOperation,
    State,
    gfsm_GState,
    gfsm_BooleanExpression,
    Transition,
    gfsm_GTransition,
    FSM,
    gfsm_GFSM,
    InitialState,
    gfsm_GInitialState,
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



def test_gfsm_gfinalstate_is_not_abstract():
    assert not inspect.isabstract(gfsm_GFinalState)


def test_gfsm_gfinalstate_constructor_exists():
    assert callable(gfsm_GFinalState.__init__)


def test_gfsm_gfinalstate_constructor_args():
    sig = inspect.signature(gfsm_GFinalState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_intoperation_is_not_abstract():
    assert not inspect.isabstract(gfsm_IntOperation)


def test_gfsm_intoperation_constructor_exists():
    assert callable(gfsm_IntOperation.__init__)


def test_gfsm_intoperation_constructor_args():
    sig = inspect.signature(gfsm_IntOperation.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_gstate_is_not_abstract():
    assert not inspect.isabstract(gfsm_GState)


def test_gfsm_gstate_constructor_exists():
    assert callable(gfsm_GState.__init__)


def test_gfsm_gstate_constructor_args():
    sig = inspect.signature(gfsm_GState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(gfsm_BooleanExpression)


def test_gfsm_booleanexpression_constructor_exists():
    assert callable(gfsm_BooleanExpression.__init__)


def test_gfsm_booleanexpression_constructor_args():
    sig = inspect.signature(gfsm_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_gtransition_is_not_abstract():
    assert not inspect.isabstract(gfsm_GTransition)


def test_gfsm_gtransition_constructor_exists():
    assert callable(gfsm_GTransition.__init__)


def test_gfsm_gtransition_constructor_args():
    sig = inspect.signature(gfsm_GTransition.__init__)
    params = list(sig.parameters.keys())



def test_fsm_is_not_abstract():
    assert not inspect.isabstract(FSM)


def test_fsm_constructor_exists():
    assert callable(FSM.__init__)


def test_fsm_constructor_args():
    sig = inspect.signature(FSM.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_gfsm_is_not_abstract():
    assert not inspect.isabstract(gfsm_GFSM)


def test_gfsm_gfsm_constructor_exists():
    assert callable(gfsm_GFSM.__init__)


def test_gfsm_gfsm_constructor_args():
    sig = inspect.signature(gfsm_GFSM.__init__)
    params = list(sig.parameters.keys())



def test_initialstate_is_not_abstract():
    assert not inspect.isabstract(InitialState)


def test_initialstate_constructor_exists():
    assert callable(InitialState.__init__)


def test_initialstate_constructor_args():
    sig = inspect.signature(InitialState.__init__)
    params = list(sig.parameters.keys())



def test_gfsm_ginitialstate_is_not_abstract():
    assert not inspect.isabstract(gfsm_GInitialState)


def test_gfsm_ginitialstate_constructor_exists():
    assert callable(gfsm_GInitialState.__init__)


def test_gfsm_ginitialstate_constructor_args():
    sig = inspect.signature(gfsm_GInitialState.__init__)
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
gfsm_GFinalState_strategy = st.builds(
    gfsm_GFinalState,
)
gfsm_IntOperation_strategy = st.builds(
    gfsm_IntOperation,
)
State_strategy = st.builds(
    State,
)
gfsm_GState_strategy = st.builds(
    gfsm_GState,
)
gfsm_BooleanExpression_strategy = st.builds(
    gfsm_BooleanExpression,
)
Transition_strategy = st.builds(
    Transition,
)
gfsm_GTransition_strategy = st.builds(
    gfsm_GTransition,
)
FSM_strategy = st.builds(
    FSM,
)
gfsm_GFSM_strategy = st.builds(
    gfsm_GFSM,
)
InitialState_strategy = st.builds(
    InitialState,
)
gfsm_GInitialState_strategy = st.builds(
    gfsm_GInitialState,
)

@given(instance=FinalState_strategy)
@settings(max_examples=50)
def test_finalstate_instantiation(instance):
    assert isinstance(instance, FinalState)

@given(instance=GState_strategy)
@settings(max_examples=50)
def test_gstate_instantiation(instance):
    assert isinstance(instance, GState)

@given(instance=gfsm_GFinalState_strategy)
@settings(max_examples=50)
def test_gfsm_gfinalstate_instantiation(instance):
    assert isinstance(instance, gfsm_GFinalState)

@given(instance=gfsm_IntOperation_strategy)
@settings(max_examples=50)
def test_gfsm_intoperation_instantiation(instance):
    assert isinstance(instance, gfsm_IntOperation)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=gfsm_GState_strategy)
@settings(max_examples=50)
def test_gfsm_gstate_instantiation(instance):
    assert isinstance(instance, gfsm_GState)

@given(instance=gfsm_BooleanExpression_strategy)
@settings(max_examples=50)
def test_gfsm_booleanexpression_instantiation(instance):
    assert isinstance(instance, gfsm_BooleanExpression)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=gfsm_GTransition_strategy)
@settings(max_examples=50)
def test_gfsm_gtransition_instantiation(instance):
    assert isinstance(instance, gfsm_GTransition)

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=gfsm_GFSM_strategy)
@settings(max_examples=50)
def test_gfsm_gfsm_instantiation(instance):
    assert isinstance(instance, gfsm_GFSM)

@given(instance=InitialState_strategy)
@settings(max_examples=50)
def test_initialstate_instantiation(instance):
    assert isinstance(instance, InitialState)

@given(instance=gfsm_GInitialState_strategy)
@settings(max_examples=50)
def test_gfsm_ginitialstate_instantiation(instance):
    assert isinstance(instance, gfsm_GInitialState)

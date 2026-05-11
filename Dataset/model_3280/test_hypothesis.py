import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metaModelSM::Signal,
    metaModelSM::Guard,
    metaModelSM::NewEClass2,
    metaModelSM::NewEClass1,
    metaModelSM::Transition,
    State,
    metaModelSM::FinalState,
    metaModelSM::InitialState,
    metaModelSM::Triggers,
    metaModelSM::State,
    metaModelSM::Region,
    metaModelSM::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodelsm::signal_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::Signal)


def test_metamodelsm::signal_constructor_exists():
    assert callable(metaModelSM::Signal.__init__)


def test_metamodelsm::signal_constructor_args():
    sig = inspect.signature(metaModelSM::Signal.__init__)
    params = list(sig.parameters.keys())



def test_metamodelsm::guard_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::Guard)


def test_metamodelsm::guard_constructor_exists():
    assert callable(metaModelSM::Guard.__init__)


def test_metamodelsm::guard_constructor_args():
    sig = inspect.signature(metaModelSM::Guard.__init__)
    params = list(sig.parameters.keys())



def test_metamodelsm::neweclass2_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::NewEClass2)


def test_metamodelsm::neweclass2_constructor_exists():
    assert callable(metaModelSM::NewEClass2.__init__)


def test_metamodelsm::neweclass2_constructor_args():
    sig = inspect.signature(metaModelSM::NewEClass2.__init__)
    params = list(sig.parameters.keys())



def test_metamodelsm::neweclass1_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::NewEClass1)


def test_metamodelsm::neweclass1_constructor_exists():
    assert callable(metaModelSM::NewEClass1.__init__)


def test_metamodelsm::neweclass1_constructor_args():
    sig = inspect.signature(metaModelSM::NewEClass1.__init__)
    params = list(sig.parameters.keys())



def test_metamodelsm::transition_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::Transition)


def test_metamodelsm::transition_constructor_exists():
    assert callable(metaModelSM::Transition.__init__)


def test_metamodelsm::transition_constructor_args():
    sig = inspect.signature(metaModelSM::Transition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_metamodelsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::FinalState)


def test_metamodelsm::finalstate_constructor_exists():
    assert callable(metaModelSM::FinalState.__init__)


def test_metamodelsm::finalstate_constructor_args():
    sig = inspect.signature(metaModelSM::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_metamodelsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::InitialState)


def test_metamodelsm::initialstate_constructor_exists():
    assert callable(metaModelSM::InitialState.__init__)


def test_metamodelsm::initialstate_constructor_args():
    sig = inspect.signature(metaModelSM::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_metamodelsm::triggers_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::Triggers)


def test_metamodelsm::triggers_constructor_exists():
    assert callable(metaModelSM::Triggers.__init__)


def test_metamodelsm::triggers_constructor_args():
    sig = inspect.signature(metaModelSM::Triggers.__init__)
    params = list(sig.parameters.keys())



def test_metamodelsm::state_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::State)


def test_metamodelsm::state_constructor_exists():
    assert callable(metaModelSM::State.__init__)


def test_metamodelsm::state_constructor_args():
    sig = inspect.signature(metaModelSM::State.__init__)
    params = list(sig.parameters.keys())



def test_metamodelsm::region_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::Region)


def test_metamodelsm::region_constructor_exists():
    assert callable(metaModelSM::Region.__init__)


def test_metamodelsm::region_constructor_args():
    sig = inspect.signature(metaModelSM::Region.__init__)
    params = list(sig.parameters.keys())



def test_metamodelsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(metaModelSM::StateMachine)


def test_metamodelsm::statemachine_constructor_exists():
    assert callable(metaModelSM::StateMachine.__init__)


def test_metamodelsm::statemachine_constructor_args():
    sig = inspect.signature(metaModelSM::StateMachine.__init__)
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
metaModelSM::Signal_strategy = st.builds(
    metaModelSM::Signal,
)
metaModelSM::Guard_strategy = st.builds(
    metaModelSM::Guard,
)
metaModelSM::NewEClass2_strategy = st.builds(
    metaModelSM::NewEClass2,
)
metaModelSM::NewEClass1_strategy = st.builds(
    metaModelSM::NewEClass1,
)
metaModelSM::Transition_strategy = st.builds(
    metaModelSM::Transition,
)
State_strategy = st.builds(
    State,
)
metaModelSM::FinalState_strategy = st.builds(
    metaModelSM::FinalState,
)
metaModelSM::InitialState_strategy = st.builds(
    metaModelSM::InitialState,
)
metaModelSM::Triggers_strategy = st.builds(
    metaModelSM::Triggers,
)
metaModelSM::State_strategy = st.builds(
    metaModelSM::State,
)
metaModelSM::Region_strategy = st.builds(
    metaModelSM::Region,
)
metaModelSM::StateMachine_strategy = st.builds(
    metaModelSM::StateMachine,
)

@given(instance=metaModelSM::Signal_strategy)
@settings(max_examples=50)
def test_metamodelsm::signal_instantiation(instance):
    assert isinstance(instance, metaModelSM::Signal)

@given(instance=metaModelSM::Guard_strategy)
@settings(max_examples=50)
def test_metamodelsm::guard_instantiation(instance):
    assert isinstance(instance, metaModelSM::Guard)

@given(instance=metaModelSM::NewEClass2_strategy)
@settings(max_examples=50)
def test_metamodelsm::neweclass2_instantiation(instance):
    assert isinstance(instance, metaModelSM::NewEClass2)

@given(instance=metaModelSM::NewEClass1_strategy)
@settings(max_examples=50)
def test_metamodelsm::neweclass1_instantiation(instance):
    assert isinstance(instance, metaModelSM::NewEClass1)

@given(instance=metaModelSM::Transition_strategy)
@settings(max_examples=50)
def test_metamodelsm::transition_instantiation(instance):
    assert isinstance(instance, metaModelSM::Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=metaModelSM::FinalState_strategy)
@settings(max_examples=50)
def test_metamodelsm::finalstate_instantiation(instance):
    assert isinstance(instance, metaModelSM::FinalState)

@given(instance=metaModelSM::InitialState_strategy)
@settings(max_examples=50)
def test_metamodelsm::initialstate_instantiation(instance):
    assert isinstance(instance, metaModelSM::InitialState)

@given(instance=metaModelSM::Triggers_strategy)
@settings(max_examples=50)
def test_metamodelsm::triggers_instantiation(instance):
    assert isinstance(instance, metaModelSM::Triggers)

@given(instance=metaModelSM::State_strategy)
@settings(max_examples=50)
def test_metamodelsm::state_instantiation(instance):
    assert isinstance(instance, metaModelSM::State)

@given(instance=metaModelSM::Region_strategy)
@settings(max_examples=50)
def test_metamodelsm::region_instantiation(instance):
    assert isinstance(instance, metaModelSM::Region)

@given(instance=metaModelSM::StateMachine_strategy)
@settings(max_examples=50)
def test_metamodelsm::statemachine_instantiation(instance):
    assert isinstance(instance, metaModelSM::StateMachine)

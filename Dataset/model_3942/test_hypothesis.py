import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statesmodel::ActivityNodeExecution,
    statesmodel::ValueSnapshot,
    statesmodel::Transition,
    statesmodel::State,
    statesmodel::StatesModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statesmodel::activitynodeexecution_is_not_abstract():
    assert not inspect.isabstract(statesmodel::ActivityNodeExecution)


def test_statesmodel::activitynodeexecution_constructor_exists():
    assert callable(statesmodel::ActivityNodeExecution.__init__)


def test_statesmodel::activitynodeexecution_constructor_args():
    sig = inspect.signature(statesmodel::ActivityNodeExecution.__init__)
    params = list(sig.parameters.keys())



def test_statesmodel::valuesnapshot_is_not_abstract():
    assert not inspect.isabstract(statesmodel::ValueSnapshot)


def test_statesmodel::valuesnapshot_constructor_exists():
    assert callable(statesmodel::ValueSnapshot.__init__)


def test_statesmodel::valuesnapshot_constructor_args():
    sig = inspect.signature(statesmodel::ValueSnapshot.__init__)
    params = list(sig.parameters.keys())



def test_statesmodel::transition_is_not_abstract():
    assert not inspect.isabstract(statesmodel::Transition)


def test_statesmodel::transition_constructor_exists():
    assert callable(statesmodel::Transition.__init__)


def test_statesmodel::transition_constructor_args():
    sig = inspect.signature(statesmodel::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statesmodel::state_is_not_abstract():
    assert not inspect.isabstract(statesmodel::State)


def test_statesmodel::state_constructor_exists():
    assert callable(statesmodel::State.__init__)


def test_statesmodel::state_constructor_args():
    sig = inspect.signature(statesmodel::State.__init__)
    params = list(sig.parameters.keys())



def test_statesmodel::statesmodel_is_not_abstract():
    assert not inspect.isabstract(statesmodel::StatesModel)


def test_statesmodel::statesmodel_constructor_exists():
    assert callable(statesmodel::StatesModel.__init__)


def test_statesmodel::statesmodel_constructor_args():
    sig = inspect.signature(statesmodel::StatesModel.__init__)
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
statesmodel::ActivityNodeExecution_strategy = st.builds(
    statesmodel::ActivityNodeExecution,
)
statesmodel::ValueSnapshot_strategy = st.builds(
    statesmodel::ValueSnapshot,
)
statesmodel::Transition_strategy = st.builds(
    statesmodel::Transition,
)
statesmodel::State_strategy = st.builds(
    statesmodel::State,
)
statesmodel::StatesModel_strategy = st.builds(
    statesmodel::StatesModel,
)

@given(instance=statesmodel::ActivityNodeExecution_strategy)
@settings(max_examples=50)
def test_statesmodel::activitynodeexecution_instantiation(instance):
    assert isinstance(instance, statesmodel::ActivityNodeExecution)

@given(instance=statesmodel::ValueSnapshot_strategy)
@settings(max_examples=50)
def test_statesmodel::valuesnapshot_instantiation(instance):
    assert isinstance(instance, statesmodel::ValueSnapshot)

@given(instance=statesmodel::Transition_strategy)
@settings(max_examples=50)
def test_statesmodel::transition_instantiation(instance):
    assert isinstance(instance, statesmodel::Transition)

@given(instance=statesmodel::State_strategy)
@settings(max_examples=50)
def test_statesmodel::state_instantiation(instance):
    assert isinstance(instance, statesmodel::State)

@given(instance=statesmodel::StatesModel_strategy)
@settings(max_examples=50)
def test_statesmodel::statesmodel_instantiation(instance):
    assert isinstance(instance, statesmodel::StatesModel)

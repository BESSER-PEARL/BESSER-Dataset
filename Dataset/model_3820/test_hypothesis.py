import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ioAutomaton::Actor,
    ioAutomaton::Return,
    ioAutomaton::OutMessage,
    ioAutomaton::Operation,
    State,
    ioAutomaton::Transition,
    ioAutomaton::State,
    ioAutomaton::SystemActor,
    ioAutomaton::Automaton,
    ioAutomaton::AutomatonCollection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ioautomaton::actor_is_not_abstract():
    assert not inspect.isabstract(ioAutomaton::Actor)


def test_ioautomaton::actor_constructor_exists():
    assert callable(ioAutomaton::Actor.__init__)


def test_ioautomaton::actor_constructor_args():
    sig = inspect.signature(ioAutomaton::Actor.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton::return_is_not_abstract():
    assert not inspect.isabstract(ioAutomaton::Return)


def test_ioautomaton::return_constructor_exists():
    assert callable(ioAutomaton::Return.__init__)


def test_ioautomaton::return_constructor_args():
    sig = inspect.signature(ioAutomaton::Return.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton::outmessage_is_not_abstract():
    assert not inspect.isabstract(ioAutomaton::OutMessage)


def test_ioautomaton::outmessage_constructor_exists():
    assert callable(ioAutomaton::OutMessage.__init__)


def test_ioautomaton::outmessage_constructor_args():
    sig = inspect.signature(ioAutomaton::OutMessage.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton::operation_is_not_abstract():
    assert not inspect.isabstract(ioAutomaton::Operation)


def test_ioautomaton::operation_constructor_exists():
    assert callable(ioAutomaton::Operation.__init__)


def test_ioautomaton::operation_constructor_args():
    sig = inspect.signature(ioAutomaton::Operation.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton::transition_is_not_abstract():
    assert not inspect.isabstract(ioAutomaton::Transition)


def test_ioautomaton::transition_constructor_exists():
    assert callable(ioAutomaton::Transition.__init__)


def test_ioautomaton::transition_constructor_args():
    sig = inspect.signature(ioAutomaton::Transition.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton::state_is_not_abstract():
    assert not inspect.isabstract(ioAutomaton::State)


def test_ioautomaton::state_constructor_exists():
    assert callable(ioAutomaton::State.__init__)


def test_ioautomaton::state_constructor_args():
    sig = inspect.signature(ioAutomaton::State.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton::systemactor_is_not_abstract():
    assert not inspect.isabstract(ioAutomaton::SystemActor)


def test_ioautomaton::systemactor_constructor_exists():
    assert callable(ioAutomaton::SystemActor.__init__)


def test_ioautomaton::systemactor_constructor_args():
    sig = inspect.signature(ioAutomaton::SystemActor.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton::automaton_is_not_abstract():
    assert not inspect.isabstract(ioAutomaton::Automaton)


def test_ioautomaton::automaton_constructor_exists():
    assert callable(ioAutomaton::Automaton.__init__)


def test_ioautomaton::automaton_constructor_args():
    sig = inspect.signature(ioAutomaton::Automaton.__init__)
    params = list(sig.parameters.keys())



def test_ioautomaton::automatoncollection_is_not_abstract():
    assert not inspect.isabstract(ioAutomaton::AutomatonCollection)


def test_ioautomaton::automatoncollection_constructor_exists():
    assert callable(ioAutomaton::AutomatonCollection.__init__)


def test_ioautomaton::automatoncollection_constructor_args():
    sig = inspect.signature(ioAutomaton::AutomatonCollection.__init__)
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
ioAutomaton::Actor_strategy = st.builds(
    ioAutomaton::Actor,
)
ioAutomaton::Return_strategy = st.builds(
    ioAutomaton::Return,
)
ioAutomaton::OutMessage_strategy = st.builds(
    ioAutomaton::OutMessage,
)
ioAutomaton::Operation_strategy = st.builds(
    ioAutomaton::Operation,
)
State_strategy = st.builds(
    State,
)
ioAutomaton::Transition_strategy = st.builds(
    ioAutomaton::Transition,
)
ioAutomaton::State_strategy = st.builds(
    ioAutomaton::State,
)
ioAutomaton::SystemActor_strategy = st.builds(
    ioAutomaton::SystemActor,
)
ioAutomaton::Automaton_strategy = st.builds(
    ioAutomaton::Automaton,
)
ioAutomaton::AutomatonCollection_strategy = st.builds(
    ioAutomaton::AutomatonCollection,
)

@given(instance=ioAutomaton::Actor_strategy)
@settings(max_examples=50)
def test_ioautomaton::actor_instantiation(instance):
    assert isinstance(instance, ioAutomaton::Actor)

@given(instance=ioAutomaton::Return_strategy)
@settings(max_examples=50)
def test_ioautomaton::return_instantiation(instance):
    assert isinstance(instance, ioAutomaton::Return)

@given(instance=ioAutomaton::OutMessage_strategy)
@settings(max_examples=50)
def test_ioautomaton::outmessage_instantiation(instance):
    assert isinstance(instance, ioAutomaton::OutMessage)

@given(instance=ioAutomaton::Operation_strategy)
@settings(max_examples=50)
def test_ioautomaton::operation_instantiation(instance):
    assert isinstance(instance, ioAutomaton::Operation)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=ioAutomaton::Transition_strategy)
@settings(max_examples=50)
def test_ioautomaton::transition_instantiation(instance):
    assert isinstance(instance, ioAutomaton::Transition)

@given(instance=ioAutomaton::State_strategy)
@settings(max_examples=50)
def test_ioautomaton::state_instantiation(instance):
    assert isinstance(instance, ioAutomaton::State)

@given(instance=ioAutomaton::SystemActor_strategy)
@settings(max_examples=50)
def test_ioautomaton::systemactor_instantiation(instance):
    assert isinstance(instance, ioAutomaton::SystemActor)

@given(instance=ioAutomaton::Automaton_strategy)
@settings(max_examples=50)
def test_ioautomaton::automaton_instantiation(instance):
    assert isinstance(instance, ioAutomaton::Automaton)

@given(instance=ioAutomaton::AutomatonCollection_strategy)
@settings(max_examples=50)
def test_ioautomaton::automatoncollection_instantiation(instance):
    assert isinstance(instance, ioAutomaton::AutomatonCollection)

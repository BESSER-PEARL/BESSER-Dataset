import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateMachine::OutputState,
    stateMachine::InputState,
    ex::stateMachine::StandardState,
    ex::stateMachine::State,
    InputState,
    ex::stateMachine::TerminalState,
    OutputState,
    ex::stateMachine::InitState,
    ex::stateMachine::Transition,
    Transition,
    State,
    ex::stateMachine::OutputState,
    ex::stateMachine::InputState,
    InitState,
    ex::stateMachine::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::outputstate_is_not_abstract():
    assert not inspect.isabstract(stateMachine::OutputState)


def test_statemachine::outputstate_constructor_exists():
    assert callable(stateMachine::OutputState.__init__)


def test_statemachine::outputstate_constructor_args():
    sig = inspect.signature(stateMachine::OutputState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::inputstate_is_not_abstract():
    assert not inspect.isabstract(stateMachine::InputState)


def test_statemachine::inputstate_constructor_exists():
    assert callable(stateMachine::InputState.__init__)


def test_statemachine::inputstate_constructor_args():
    sig = inspect.signature(stateMachine::InputState.__init__)
    params = list(sig.parameters.keys())



def test_ex::statemachine::standardstate_is_not_abstract():
    assert not inspect.isabstract(ex::stateMachine::StandardState)


def test_ex::statemachine::standardstate_constructor_exists():
    assert callable(ex::stateMachine::StandardState.__init__)


def test_ex::statemachine::standardstate_constructor_args():
    sig = inspect.signature(ex::stateMachine::StandardState.__init__)
    params = list(sig.parameters.keys())



def test_ex::statemachine::state_is_not_abstract():
    assert not inspect.isabstract(ex::stateMachine::State)


def test_ex::statemachine::state_constructor_exists():
    assert callable(ex::stateMachine::State.__init__)


def test_ex::statemachine::state_constructor_args():
    sig = inspect.signature(ex::stateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ex::statemachine::state_has_name():
    assert hasattr(ex::stateMachine::State, "name")
    descriptor = None
    for klass in ex::stateMachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_inputstate_is_not_abstract():
    assert not inspect.isabstract(InputState)


def test_inputstate_constructor_exists():
    assert callable(InputState.__init__)


def test_inputstate_constructor_args():
    sig = inspect.signature(InputState.__init__)
    params = list(sig.parameters.keys())



def test_ex::statemachine::terminalstate_is_not_abstract():
    assert not inspect.isabstract(ex::stateMachine::TerminalState)


def test_ex::statemachine::terminalstate_constructor_exists():
    assert callable(ex::stateMachine::TerminalState.__init__)


def test_ex::statemachine::terminalstate_constructor_args():
    sig = inspect.signature(ex::stateMachine::TerminalState.__init__)
    params = list(sig.parameters.keys())



def test_outputstate_is_not_abstract():
    assert not inspect.isabstract(OutputState)


def test_outputstate_constructor_exists():
    assert callable(OutputState.__init__)


def test_outputstate_constructor_args():
    sig = inspect.signature(OutputState.__init__)
    params = list(sig.parameters.keys())



def test_ex::statemachine::initstate_is_not_abstract():
    assert not inspect.isabstract(ex::stateMachine::InitState)


def test_ex::statemachine::initstate_constructor_exists():
    assert callable(ex::stateMachine::InitState.__init__)


def test_ex::statemachine::initstate_constructor_args():
    sig = inspect.signature(ex::stateMachine::InitState.__init__)
    params = list(sig.parameters.keys())



def test_ex::statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(ex::stateMachine::Transition)


def test_ex::statemachine::transition_constructor_exists():
    assert callable(ex::stateMachine::Transition.__init__)


def test_ex::statemachine::transition_constructor_args():
    sig = inspect.signature(ex::stateMachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_ex::statemachine::outputstate_is_not_abstract():
    assert not inspect.isabstract(ex::stateMachine::OutputState)


def test_ex::statemachine::outputstate_constructor_exists():
    assert callable(ex::stateMachine::OutputState.__init__)


def test_ex::statemachine::outputstate_constructor_args():
    sig = inspect.signature(ex::stateMachine::OutputState.__init__)
    params = list(sig.parameters.keys())



def test_ex::statemachine::inputstate_is_not_abstract():
    assert not inspect.isabstract(ex::stateMachine::InputState)


def test_ex::statemachine::inputstate_constructor_exists():
    assert callable(ex::stateMachine::InputState.__init__)


def test_ex::statemachine::inputstate_constructor_args():
    sig = inspect.signature(ex::stateMachine::InputState.__init__)
    params = list(sig.parameters.keys())



def test_initstate_is_not_abstract():
    assert not inspect.isabstract(InitState)


def test_initstate_constructor_exists():
    assert callable(InitState.__init__)


def test_initstate_constructor_args():
    sig = inspect.signature(InitState.__init__)
    params = list(sig.parameters.keys())



def test_ex::statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(ex::stateMachine::StateMachine)


def test_ex::statemachine::statemachine_constructor_exists():
    assert callable(ex::stateMachine::StateMachine.__init__)


def test_ex::statemachine::statemachine_constructor_args():
    sig = inspect.signature(ex::stateMachine::StateMachine.__init__)
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
stateMachine::OutputState_strategy = st.builds(
    stateMachine::OutputState,
)
stateMachine::InputState_strategy = st.builds(
    stateMachine::InputState,
)
ex::stateMachine::StandardState_strategy = st.builds(
    ex::stateMachine::StandardState,
)
ex::stateMachine::State_strategy = st.builds(
    ex::stateMachine::State,
    name=
        safe_text
)
InputState_strategy = st.builds(
    InputState,
)
ex::stateMachine::TerminalState_strategy = st.builds(
    ex::stateMachine::TerminalState,
)
OutputState_strategy = st.builds(
    OutputState,
)
ex::stateMachine::InitState_strategy = st.builds(
    ex::stateMachine::InitState,
)
ex::stateMachine::Transition_strategy = st.builds(
    ex::stateMachine::Transition,
)
Transition_strategy = st.builds(
    Transition,
)
State_strategy = st.builds(
    State,
)
ex::stateMachine::OutputState_strategy = st.builds(
    ex::stateMachine::OutputState,
)
ex::stateMachine::InputState_strategy = st.builds(
    ex::stateMachine::InputState,
)
InitState_strategy = st.builds(
    InitState,
)
ex::stateMachine::StateMachine_strategy = st.builds(
    ex::stateMachine::StateMachine,
)

@given(instance=stateMachine::OutputState_strategy)
@settings(max_examples=50)
def test_statemachine::outputstate_instantiation(instance):
    assert isinstance(instance, stateMachine::OutputState)

@given(instance=stateMachine::InputState_strategy)
@settings(max_examples=50)
def test_statemachine::inputstate_instantiation(instance):
    assert isinstance(instance, stateMachine::InputState)

@given(instance=ex::stateMachine::StandardState_strategy)
@settings(max_examples=50)
def test_ex::statemachine::standardstate_instantiation(instance):
    assert isinstance(instance, ex::stateMachine::StandardState)

@given(instance=ex::stateMachine::State_strategy)
@settings(max_examples=50)
def test_ex::statemachine::state_instantiation(instance):
    assert isinstance(instance, ex::stateMachine::State)

@given(instance=ex::stateMachine::State_strategy)
def test_ex::statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ex::stateMachine::State_strategy)
def test_ex::statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=InputState_strategy)
@settings(max_examples=50)
def test_inputstate_instantiation(instance):
    assert isinstance(instance, InputState)

@given(instance=ex::stateMachine::TerminalState_strategy)
@settings(max_examples=50)
def test_ex::statemachine::terminalstate_instantiation(instance):
    assert isinstance(instance, ex::stateMachine::TerminalState)

@given(instance=OutputState_strategy)
@settings(max_examples=50)
def test_outputstate_instantiation(instance):
    assert isinstance(instance, OutputState)

@given(instance=ex::stateMachine::InitState_strategy)
@settings(max_examples=50)
def test_ex::statemachine::initstate_instantiation(instance):
    assert isinstance(instance, ex::stateMachine::InitState)

@given(instance=ex::stateMachine::Transition_strategy)
@settings(max_examples=50)
def test_ex::statemachine::transition_instantiation(instance):
    assert isinstance(instance, ex::stateMachine::Transition)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=ex::stateMachine::OutputState_strategy)
@settings(max_examples=50)
def test_ex::statemachine::outputstate_instantiation(instance):
    assert isinstance(instance, ex::stateMachine::OutputState)

@given(instance=ex::stateMachine::InputState_strategy)
@settings(max_examples=50)
def test_ex::statemachine::inputstate_instantiation(instance):
    assert isinstance(instance, ex::stateMachine::InputState)

@given(instance=InitState_strategy)
@settings(max_examples=50)
def test_initstate_instantiation(instance):
    assert isinstance(instance, InitState)

@given(instance=ex::stateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_ex::statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, ex::stateMachine::StateMachine)

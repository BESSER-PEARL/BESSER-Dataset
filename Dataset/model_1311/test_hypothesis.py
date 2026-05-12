import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stateMachine_OutputState,
    stateMachine_InputState,
    ex_stateMachine_StandardState,
    ex_stateMachine_State,
    InputState,
    ex_stateMachine_TerminalState,
    OutputState,
    ex_stateMachine_InitState,
    ex_stateMachine_Transition,
    Transition,
    State,
    ex_stateMachine_InputState,
    ex_stateMachine_OutputState,
    InitState,
    ex_stateMachine_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_outputstate_is_not_abstract():
    assert not inspect.isabstract(stateMachine_OutputState)


def test_statemachine_outputstate_constructor_exists():
    assert callable(stateMachine_OutputState.__init__)


def test_statemachine_outputstate_constructor_args():
    sig = inspect.signature(stateMachine_OutputState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_inputstate_is_not_abstract():
    assert not inspect.isabstract(stateMachine_InputState)


def test_statemachine_inputstate_constructor_exists():
    assert callable(stateMachine_InputState.__init__)


def test_statemachine_inputstate_constructor_args():
    sig = inspect.signature(stateMachine_InputState.__init__)
    params = list(sig.parameters.keys())



def test_ex_statemachine_standardstate_is_not_abstract():
    assert not inspect.isabstract(ex_stateMachine_StandardState)


def test_ex_statemachine_standardstate_constructor_exists():
    assert callable(ex_stateMachine_StandardState.__init__)


def test_ex_statemachine_standardstate_constructor_args():
    sig = inspect.signature(ex_stateMachine_StandardState.__init__)
    params = list(sig.parameters.keys())



def test_ex_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(ex_stateMachine_State)


def test_ex_statemachine_state_constructor_exists():
    assert callable(ex_stateMachine_State.__init__)


def test_ex_statemachine_state_constructor_args():
    sig = inspect.signature(ex_stateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ex_statemachine_state_has_name():
    assert hasattr(ex_stateMachine_State, "name")
    descriptor = None
    for klass in ex_stateMachine_State.__mro__:
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



def test_ex_statemachine_terminalstate_is_not_abstract():
    assert not inspect.isabstract(ex_stateMachine_TerminalState)


def test_ex_statemachine_terminalstate_constructor_exists():
    assert callable(ex_stateMachine_TerminalState.__init__)


def test_ex_statemachine_terminalstate_constructor_args():
    sig = inspect.signature(ex_stateMachine_TerminalState.__init__)
    params = list(sig.parameters.keys())



def test_outputstate_is_not_abstract():
    assert not inspect.isabstract(OutputState)


def test_outputstate_constructor_exists():
    assert callable(OutputState.__init__)


def test_outputstate_constructor_args():
    sig = inspect.signature(OutputState.__init__)
    params = list(sig.parameters.keys())



def test_ex_statemachine_initstate_is_not_abstract():
    assert not inspect.isabstract(ex_stateMachine_InitState)


def test_ex_statemachine_initstate_constructor_exists():
    assert callable(ex_stateMachine_InitState.__init__)


def test_ex_statemachine_initstate_constructor_args():
    sig = inspect.signature(ex_stateMachine_InitState.__init__)
    params = list(sig.parameters.keys())



def test_ex_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(ex_stateMachine_Transition)


def test_ex_statemachine_transition_constructor_exists():
    assert callable(ex_stateMachine_Transition.__init__)


def test_ex_statemachine_transition_constructor_args():
    sig = inspect.signature(ex_stateMachine_Transition.__init__)
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



def test_ex_statemachine_inputstate_is_not_abstract():
    assert not inspect.isabstract(ex_stateMachine_InputState)


def test_ex_statemachine_inputstate_constructor_exists():
    assert callable(ex_stateMachine_InputState.__init__)


def test_ex_statemachine_inputstate_constructor_args():
    sig = inspect.signature(ex_stateMachine_InputState.__init__)
    params = list(sig.parameters.keys())



def test_ex_statemachine_outputstate_is_not_abstract():
    assert not inspect.isabstract(ex_stateMachine_OutputState)


def test_ex_statemachine_outputstate_constructor_exists():
    assert callable(ex_stateMachine_OutputState.__init__)


def test_ex_statemachine_outputstate_constructor_args():
    sig = inspect.signature(ex_stateMachine_OutputState.__init__)
    params = list(sig.parameters.keys())



def test_initstate_is_not_abstract():
    assert not inspect.isabstract(InitState)


def test_initstate_constructor_exists():
    assert callable(InitState.__init__)


def test_initstate_constructor_args():
    sig = inspect.signature(InitState.__init__)
    params = list(sig.parameters.keys())



def test_ex_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(ex_stateMachine_StateMachine)


def test_ex_statemachine_statemachine_constructor_exists():
    assert callable(ex_stateMachine_StateMachine.__init__)


def test_ex_statemachine_statemachine_constructor_args():
    sig = inspect.signature(ex_stateMachine_StateMachine.__init__)
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
stateMachine_OutputState_strategy = st.builds(
    stateMachine_OutputState,
)
stateMachine_InputState_strategy = st.builds(
    stateMachine_InputState,
)
ex_stateMachine_StandardState_strategy = st.builds(
    ex_stateMachine_StandardState,
)
ex_stateMachine_State_strategy = st.builds(
    ex_stateMachine_State,
    name=
        safe_text
)
InputState_strategy = st.builds(
    InputState,
)
ex_stateMachine_TerminalState_strategy = st.builds(
    ex_stateMachine_TerminalState,
)
OutputState_strategy = st.builds(
    OutputState,
)
ex_stateMachine_InitState_strategy = st.builds(
    ex_stateMachine_InitState,
)
ex_stateMachine_Transition_strategy = st.builds(
    ex_stateMachine_Transition,
)
Transition_strategy = st.builds(
    Transition,
)
State_strategy = st.builds(
    State,
)
ex_stateMachine_InputState_strategy = st.builds(
    ex_stateMachine_InputState,
)
ex_stateMachine_OutputState_strategy = st.builds(
    ex_stateMachine_OutputState,
)
InitState_strategy = st.builds(
    InitState,
)
ex_stateMachine_StateMachine_strategy = st.builds(
    ex_stateMachine_StateMachine,
)

@given(instance=stateMachine_OutputState_strategy)
@settings(max_examples=50)
def test_statemachine_outputstate_instantiation(instance):
    assert isinstance(instance, stateMachine_OutputState)

@given(instance=stateMachine_InputState_strategy)
@settings(max_examples=50)
def test_statemachine_inputstate_instantiation(instance):
    assert isinstance(instance, stateMachine_InputState)

@given(instance=ex_stateMachine_StandardState_strategy)
@settings(max_examples=50)
def test_ex_statemachine_standardstate_instantiation(instance):
    assert isinstance(instance, ex_stateMachine_StandardState)

@given(instance=ex_stateMachine_State_strategy)
@settings(max_examples=50)
def test_ex_statemachine_state_instantiation(instance):
    assert isinstance(instance, ex_stateMachine_State)



@given(instance=ex_stateMachine_State_strategy)
def test_ex_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=InputState_strategy)
@settings(max_examples=50)
def test_inputstate_instantiation(instance):
    assert isinstance(instance, InputState)

@given(instance=ex_stateMachine_TerminalState_strategy)
@settings(max_examples=50)
def test_ex_statemachine_terminalstate_instantiation(instance):
    assert isinstance(instance, ex_stateMachine_TerminalState)

@given(instance=OutputState_strategy)
@settings(max_examples=50)
def test_outputstate_instantiation(instance):
    assert isinstance(instance, OutputState)

@given(instance=ex_stateMachine_InitState_strategy)
@settings(max_examples=50)
def test_ex_statemachine_initstate_instantiation(instance):
    assert isinstance(instance, ex_stateMachine_InitState)

@given(instance=ex_stateMachine_Transition_strategy)
@settings(max_examples=50)
def test_ex_statemachine_transition_instantiation(instance):
    assert isinstance(instance, ex_stateMachine_Transition)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=ex_stateMachine_InputState_strategy)
@settings(max_examples=50)
def test_ex_statemachine_inputstate_instantiation(instance):
    assert isinstance(instance, ex_stateMachine_InputState)

@given(instance=ex_stateMachine_OutputState_strategy)
@settings(max_examples=50)
def test_ex_statemachine_outputstate_instantiation(instance):
    assert isinstance(instance, ex_stateMachine_OutputState)

@given(instance=InitState_strategy)
@settings(max_examples=50)
def test_initstate_instantiation(instance):
    assert isinstance(instance, InitState)

@given(instance=ex_stateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_ex_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, ex_stateMachine_StateMachine)

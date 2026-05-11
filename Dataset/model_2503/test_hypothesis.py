import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tfsm::ClockReset,
    Transition,
    tfsm::TimedTransition,
    tfsm::ClockConstraintOperation,
    State,
    tfsm::TimedState,
    tfsm::Clock,
    FSM,
    tfsm::TimedFSM,
    InitialState,
    TimedState,
    tfsm::TimedInitialState,
    FinalState,
    tfsm::TimedFinalState,
    BinaryClockConstraint,
    tfsm::OrClockConstraint,
    tfsm::AndClockConstraint,
    ClockConstraint,
    tfsm::UpperEqualClockConstraint,
    tfsm::LowerEqualClockConstraint,
    tfsm::UpperClockConstraint,
    tfsm::LowerClockConstraint,
    ClockConstraintOperation,
    tfsm::ClockConstraint,
    tfsm::BinaryClockConstraint,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tfsm::clockreset_is_not_abstract():
    assert not inspect.isabstract(tfsm::ClockReset)


def test_tfsm::clockreset_constructor_exists():
    assert callable(tfsm::ClockReset.__init__)


def test_tfsm::clockreset_constructor_args():
    sig = inspect.signature(tfsm::ClockReset.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::timedtransition_is_not_abstract():
    assert not inspect.isabstract(tfsm::TimedTransition)


def test_tfsm::timedtransition_constructor_exists():
    assert callable(tfsm::TimedTransition.__init__)


def test_tfsm::timedtransition_constructor_args():
    sig = inspect.signature(tfsm::TimedTransition.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::clockconstraintoperation_is_not_abstract():
    assert not inspect.isabstract(tfsm::ClockConstraintOperation)


def test_tfsm::clockconstraintoperation_constructor_exists():
    assert callable(tfsm::ClockConstraintOperation.__init__)


def test_tfsm::clockconstraintoperation_constructor_args():
    sig = inspect.signature(tfsm::ClockConstraintOperation.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::timedstate_is_not_abstract():
    assert not inspect.isabstract(tfsm::TimedState)


def test_tfsm::timedstate_constructor_exists():
    assert callable(tfsm::TimedState.__init__)


def test_tfsm::timedstate_constructor_args():
    sig = inspect.signature(tfsm::TimedState.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::clock_is_not_abstract():
    assert not inspect.isabstract(tfsm::Clock)


def test_tfsm::clock_constructor_exists():
    assert callable(tfsm::Clock.__init__)


def test_tfsm::clock_constructor_args():
    sig = inspect.signature(tfsm::Clock.__init__)
    params = list(sig.parameters.keys())
    assert "tick" in params, "Missing parameter 'tick'"
    assert "name" in params, "Missing parameter 'name'"

def test_tfsm::clock_has_tick():
    assert hasattr(tfsm::Clock, "tick")
    descriptor = None
    for klass in tfsm::Clock.__mro__:
        if "tick" in klass.__dict__:
            descriptor = klass.__dict__["tick"]
            break
    assert isinstance(descriptor, property)

def test_tfsm::clock_has_name():
    assert hasattr(tfsm::Clock, "name")
    descriptor = None
    for klass in tfsm::Clock.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_is_not_abstract():
    assert not inspect.isabstract(FSM)


def test_fsm_constructor_exists():
    assert callable(FSM.__init__)


def test_fsm_constructor_args():
    sig = inspect.signature(FSM.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::timedfsm_is_not_abstract():
    assert not inspect.isabstract(tfsm::TimedFSM)


def test_tfsm::timedfsm_constructor_exists():
    assert callable(tfsm::TimedFSM.__init__)


def test_tfsm::timedfsm_constructor_args():
    sig = inspect.signature(tfsm::TimedFSM.__init__)
    params = list(sig.parameters.keys())



def test_initialstate_is_not_abstract():
    assert not inspect.isabstract(InitialState)


def test_initialstate_constructor_exists():
    assert callable(InitialState.__init__)


def test_initialstate_constructor_args():
    sig = inspect.signature(InitialState.__init__)
    params = list(sig.parameters.keys())



def test_timedstate_is_not_abstract():
    assert not inspect.isabstract(TimedState)


def test_timedstate_constructor_exists():
    assert callable(TimedState.__init__)


def test_timedstate_constructor_args():
    sig = inspect.signature(TimedState.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::timedinitialstate_is_not_abstract():
    assert not inspect.isabstract(tfsm::TimedInitialState)


def test_tfsm::timedinitialstate_constructor_exists():
    assert callable(tfsm::TimedInitialState.__init__)


def test_tfsm::timedinitialstate_constructor_args():
    sig = inspect.signature(tfsm::TimedInitialState.__init__)
    params = list(sig.parameters.keys())



def test_finalstate_is_not_abstract():
    assert not inspect.isabstract(FinalState)


def test_finalstate_constructor_exists():
    assert callable(FinalState.__init__)


def test_finalstate_constructor_args():
    sig = inspect.signature(FinalState.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::timedfinalstate_is_not_abstract():
    assert not inspect.isabstract(tfsm::TimedFinalState)


def test_tfsm::timedfinalstate_constructor_exists():
    assert callable(tfsm::TimedFinalState.__init__)


def test_tfsm::timedfinalstate_constructor_args():
    sig = inspect.signature(tfsm::TimedFinalState.__init__)
    params = list(sig.parameters.keys())



def test_binaryclockconstraint_is_not_abstract():
    assert not inspect.isabstract(BinaryClockConstraint)


def test_binaryclockconstraint_constructor_exists():
    assert callable(BinaryClockConstraint.__init__)


def test_binaryclockconstraint_constructor_args():
    sig = inspect.signature(BinaryClockConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::orclockconstraint_is_not_abstract():
    assert not inspect.isabstract(tfsm::OrClockConstraint)


def test_tfsm::orclockconstraint_constructor_exists():
    assert callable(tfsm::OrClockConstraint.__init__)


def test_tfsm::orclockconstraint_constructor_args():
    sig = inspect.signature(tfsm::OrClockConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::andclockconstraint_is_not_abstract():
    assert not inspect.isabstract(tfsm::AndClockConstraint)


def test_tfsm::andclockconstraint_constructor_exists():
    assert callable(tfsm::AndClockConstraint.__init__)


def test_tfsm::andclockconstraint_constructor_args():
    sig = inspect.signature(tfsm::AndClockConstraint.__init__)
    params = list(sig.parameters.keys())



def test_clockconstraint_is_not_abstract():
    assert not inspect.isabstract(ClockConstraint)


def test_clockconstraint_constructor_exists():
    assert callable(ClockConstraint.__init__)


def test_clockconstraint_constructor_args():
    sig = inspect.signature(ClockConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::upperequalclockconstraint_is_not_abstract():
    assert not inspect.isabstract(tfsm::UpperEqualClockConstraint)


def test_tfsm::upperequalclockconstraint_constructor_exists():
    assert callable(tfsm::UpperEqualClockConstraint.__init__)


def test_tfsm::upperequalclockconstraint_constructor_args():
    sig = inspect.signature(tfsm::UpperEqualClockConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::lowerequalclockconstraint_is_not_abstract():
    assert not inspect.isabstract(tfsm::LowerEqualClockConstraint)


def test_tfsm::lowerequalclockconstraint_constructor_exists():
    assert callable(tfsm::LowerEqualClockConstraint.__init__)


def test_tfsm::lowerequalclockconstraint_constructor_args():
    sig = inspect.signature(tfsm::LowerEqualClockConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::upperclockconstraint_is_not_abstract():
    assert not inspect.isabstract(tfsm::UpperClockConstraint)


def test_tfsm::upperclockconstraint_constructor_exists():
    assert callable(tfsm::UpperClockConstraint.__init__)


def test_tfsm::upperclockconstraint_constructor_args():
    sig = inspect.signature(tfsm::UpperClockConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::lowerclockconstraint_is_not_abstract():
    assert not inspect.isabstract(tfsm::LowerClockConstraint)


def test_tfsm::lowerclockconstraint_constructor_exists():
    assert callable(tfsm::LowerClockConstraint.__init__)


def test_tfsm::lowerclockconstraint_constructor_args():
    sig = inspect.signature(tfsm::LowerClockConstraint.__init__)
    params = list(sig.parameters.keys())



def test_clockconstraintoperation_is_not_abstract():
    assert not inspect.isabstract(ClockConstraintOperation)


def test_clockconstraintoperation_constructor_exists():
    assert callable(ClockConstraintOperation.__init__)


def test_clockconstraintoperation_constructor_args():
    sig = inspect.signature(ClockConstraintOperation.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::clockconstraint_is_not_abstract():
    assert not inspect.isabstract(tfsm::ClockConstraint)


def test_tfsm::clockconstraint_constructor_exists():
    assert callable(tfsm::ClockConstraint.__init__)


def test_tfsm::clockconstraint_constructor_args():
    sig = inspect.signature(tfsm::ClockConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "threshold" in params, "Missing parameter 'threshold'"

def test_tfsm::clockconstraint_has_threshold():
    assert hasattr(tfsm::ClockConstraint, "threshold")
    descriptor = None
    for klass in tfsm::ClockConstraint.__mro__:
        if "threshold" in klass.__dict__:
            descriptor = klass.__dict__["threshold"]
            break
    assert isinstance(descriptor, property)



def test_tfsm::binaryclockconstraint_is_not_abstract():
    assert not inspect.isabstract(tfsm::BinaryClockConstraint)


def test_tfsm::binaryclockconstraint_constructor_exists():
    assert callable(tfsm::BinaryClockConstraint.__init__)


def test_tfsm::binaryclockconstraint_constructor_args():
    sig = inspect.signature(tfsm::BinaryClockConstraint.__init__)
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
tfsm::ClockReset_strategy = st.builds(
    tfsm::ClockReset,
)
Transition_strategy = st.builds(
    Transition,
)
tfsm::TimedTransition_strategy = st.builds(
    tfsm::TimedTransition,
)
tfsm::ClockConstraintOperation_strategy = st.builds(
    tfsm::ClockConstraintOperation,
)
State_strategy = st.builds(
    State,
)
tfsm::TimedState_strategy = st.builds(
    tfsm::TimedState,
)
tfsm::Clock_strategy = st.builds(
    tfsm::Clock,
    tick=
        st.integers(),
    name=
        safe_text
)
FSM_strategy = st.builds(
    FSM,
)
tfsm::TimedFSM_strategy = st.builds(
    tfsm::TimedFSM,
)
InitialState_strategy = st.builds(
    InitialState,
)
TimedState_strategy = st.builds(
    TimedState,
)
tfsm::TimedInitialState_strategy = st.builds(
    tfsm::TimedInitialState,
)
FinalState_strategy = st.builds(
    FinalState,
)
tfsm::TimedFinalState_strategy = st.builds(
    tfsm::TimedFinalState,
)
BinaryClockConstraint_strategy = st.builds(
    BinaryClockConstraint,
)
tfsm::OrClockConstraint_strategy = st.builds(
    tfsm::OrClockConstraint,
)
tfsm::AndClockConstraint_strategy = st.builds(
    tfsm::AndClockConstraint,
)
ClockConstraint_strategy = st.builds(
    ClockConstraint,
)
tfsm::UpperEqualClockConstraint_strategy = st.builds(
    tfsm::UpperEqualClockConstraint,
)
tfsm::LowerEqualClockConstraint_strategy = st.builds(
    tfsm::LowerEqualClockConstraint,
)
tfsm::UpperClockConstraint_strategy = st.builds(
    tfsm::UpperClockConstraint,
)
tfsm::LowerClockConstraint_strategy = st.builds(
    tfsm::LowerClockConstraint,
)
ClockConstraintOperation_strategy = st.builds(
    ClockConstraintOperation,
)
tfsm::ClockConstraint_strategy = st.builds(
    tfsm::ClockConstraint,
    threshold=
        st.integers()
)
tfsm::BinaryClockConstraint_strategy = st.builds(
    tfsm::BinaryClockConstraint,
)

@given(instance=tfsm::ClockReset_strategy)
@settings(max_examples=50)
def test_tfsm::clockreset_instantiation(instance):
    assert isinstance(instance, tfsm::ClockReset)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=tfsm::TimedTransition_strategy)
@settings(max_examples=50)
def test_tfsm::timedtransition_instantiation(instance):
    assert isinstance(instance, tfsm::TimedTransition)

@given(instance=tfsm::ClockConstraintOperation_strategy)
@settings(max_examples=50)
def test_tfsm::clockconstraintoperation_instantiation(instance):
    assert isinstance(instance, tfsm::ClockConstraintOperation)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=tfsm::TimedState_strategy)
@settings(max_examples=50)
def test_tfsm::timedstate_instantiation(instance):
    assert isinstance(instance, tfsm::TimedState)

@given(instance=tfsm::Clock_strategy)
@settings(max_examples=50)
def test_tfsm::clock_instantiation(instance):
    assert isinstance(instance, tfsm::Clock)

@given(instance=tfsm::Clock_strategy)
def test_tfsm::clock_tick_type(instance):
    assert isinstance(instance.tick, int)


@given(instance=tfsm::Clock_strategy)
def test_tfsm::clock_tick_setter(instance):
    original = instance.tick
    instance.tick = original
    assert instance.tick == original

@given(instance=tfsm::Clock_strategy)
def test_tfsm::clock_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tfsm::Clock_strategy)
def test_tfsm::clock_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=tfsm::TimedFSM_strategy)
@settings(max_examples=50)
def test_tfsm::timedfsm_instantiation(instance):
    assert isinstance(instance, tfsm::TimedFSM)

@given(instance=InitialState_strategy)
@settings(max_examples=50)
def test_initialstate_instantiation(instance):
    assert isinstance(instance, InitialState)

@given(instance=TimedState_strategy)
@settings(max_examples=50)
def test_timedstate_instantiation(instance):
    assert isinstance(instance, TimedState)

@given(instance=tfsm::TimedInitialState_strategy)
@settings(max_examples=50)
def test_tfsm::timedinitialstate_instantiation(instance):
    assert isinstance(instance, tfsm::TimedInitialState)

@given(instance=FinalState_strategy)
@settings(max_examples=50)
def test_finalstate_instantiation(instance):
    assert isinstance(instance, FinalState)

@given(instance=tfsm::TimedFinalState_strategy)
@settings(max_examples=50)
def test_tfsm::timedfinalstate_instantiation(instance):
    assert isinstance(instance, tfsm::TimedFinalState)

@given(instance=BinaryClockConstraint_strategy)
@settings(max_examples=50)
def test_binaryclockconstraint_instantiation(instance):
    assert isinstance(instance, BinaryClockConstraint)

@given(instance=tfsm::OrClockConstraint_strategy)
@settings(max_examples=50)
def test_tfsm::orclockconstraint_instantiation(instance):
    assert isinstance(instance, tfsm::OrClockConstraint)

@given(instance=tfsm::AndClockConstraint_strategy)
@settings(max_examples=50)
def test_tfsm::andclockconstraint_instantiation(instance):
    assert isinstance(instance, tfsm::AndClockConstraint)

@given(instance=ClockConstraint_strategy)
@settings(max_examples=50)
def test_clockconstraint_instantiation(instance):
    assert isinstance(instance, ClockConstraint)

@given(instance=tfsm::UpperEqualClockConstraint_strategy)
@settings(max_examples=50)
def test_tfsm::upperequalclockconstraint_instantiation(instance):
    assert isinstance(instance, tfsm::UpperEqualClockConstraint)

@given(instance=tfsm::LowerEqualClockConstraint_strategy)
@settings(max_examples=50)
def test_tfsm::lowerequalclockconstraint_instantiation(instance):
    assert isinstance(instance, tfsm::LowerEqualClockConstraint)

@given(instance=tfsm::UpperClockConstraint_strategy)
@settings(max_examples=50)
def test_tfsm::upperclockconstraint_instantiation(instance):
    assert isinstance(instance, tfsm::UpperClockConstraint)

@given(instance=tfsm::LowerClockConstraint_strategy)
@settings(max_examples=50)
def test_tfsm::lowerclockconstraint_instantiation(instance):
    assert isinstance(instance, tfsm::LowerClockConstraint)

@given(instance=ClockConstraintOperation_strategy)
@settings(max_examples=50)
def test_clockconstraintoperation_instantiation(instance):
    assert isinstance(instance, ClockConstraintOperation)

@given(instance=tfsm::ClockConstraint_strategy)
@settings(max_examples=50)
def test_tfsm::clockconstraint_instantiation(instance):
    assert isinstance(instance, tfsm::ClockConstraint)

@given(instance=tfsm::ClockConstraint_strategy)
def test_tfsm::clockconstraint_threshold_type(instance):
    assert isinstance(instance.threshold, int)


@given(instance=tfsm::ClockConstraint_strategy)
def test_tfsm::clockconstraint_threshold_setter(instance):
    original = instance.threshold
    instance.threshold = original
    assert instance.threshold == original

@given(instance=tfsm::BinaryClockConstraint_strategy)
@settings(max_examples=50)
def test_tfsm::binaryclockconstraint_instantiation(instance):
    assert isinstance(instance, tfsm::BinaryClockConstraint)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    automaton::AtomicEventPattern,
    automaton::Guard,
    Transition,
    automaton::EpsilonTransition,
    automaton::TypedTransition,
    TimedZone,
    automaton::HoldsFor,
    automaton::Within,
    State,
    automaton::FinalState,
    automaton::TrapState,
    automaton::InitState,
    automaton::TimedZone,
    automaton::EventToken,
    automaton::EventPattern,
    automaton::State,
    automaton::Transition,
    automaton::Event,
    automaton::Automaton,
    automaton::InternalModel,
    EventContext,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_automaton::atomiceventpattern_is_not_abstract():
    assert not inspect.isabstract(automaton::AtomicEventPattern)


def test_automaton::atomiceventpattern_constructor_exists():
    assert callable(automaton::AtomicEventPattern.__init__)


def test_automaton::atomiceventpattern_constructor_args():
    sig = inspect.signature(automaton::AtomicEventPattern.__init__)
    params = list(sig.parameters.keys())



def test_automaton::guard_is_not_abstract():
    assert not inspect.isabstract(automaton::Guard)


def test_automaton::guard_constructor_exists():
    assert callable(automaton::Guard.__init__)


def test_automaton::guard_constructor_args():
    sig = inspect.signature(automaton::Guard.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_automaton::epsilontransition_is_not_abstract():
    assert not inspect.isabstract(automaton::EpsilonTransition)


def test_automaton::epsilontransition_constructor_exists():
    assert callable(automaton::EpsilonTransition.__init__)


def test_automaton::epsilontransition_constructor_args():
    sig = inspect.signature(automaton::EpsilonTransition.__init__)
    params = list(sig.parameters.keys())



def test_automaton::typedtransition_is_not_abstract():
    assert not inspect.isabstract(automaton::TypedTransition)


def test_automaton::typedtransition_constructor_exists():
    assert callable(automaton::TypedTransition.__init__)


def test_automaton::typedtransition_constructor_args():
    sig = inspect.signature(automaton::TypedTransition.__init__)
    params = list(sig.parameters.keys())



def test_timedzone_is_not_abstract():
    assert not inspect.isabstract(TimedZone)


def test_timedzone_constructor_exists():
    assert callable(TimedZone.__init__)


def test_timedzone_constructor_args():
    sig = inspect.signature(TimedZone.__init__)
    params = list(sig.parameters.keys())



def test_automaton::holdsfor_is_not_abstract():
    assert not inspect.isabstract(automaton::HoldsFor)


def test_automaton::holdsfor_constructor_exists():
    assert callable(automaton::HoldsFor.__init__)


def test_automaton::holdsfor_constructor_args():
    sig = inspect.signature(automaton::HoldsFor.__init__)
    params = list(sig.parameters.keys())



def test_automaton::within_is_not_abstract():
    assert not inspect.isabstract(automaton::Within)


def test_automaton::within_constructor_exists():
    assert callable(automaton::Within.__init__)


def test_automaton::within_constructor_args():
    sig = inspect.signature(automaton::Within.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_automaton::finalstate_is_not_abstract():
    assert not inspect.isabstract(automaton::FinalState)


def test_automaton::finalstate_constructor_exists():
    assert callable(automaton::FinalState.__init__)


def test_automaton::finalstate_constructor_args():
    sig = inspect.signature(automaton::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_automaton::trapstate_is_not_abstract():
    assert not inspect.isabstract(automaton::TrapState)


def test_automaton::trapstate_constructor_exists():
    assert callable(automaton::TrapState.__init__)


def test_automaton::trapstate_constructor_args():
    sig = inspect.signature(automaton::TrapState.__init__)
    params = list(sig.parameters.keys())



def test_automaton::initstate_is_not_abstract():
    assert not inspect.isabstract(automaton::InitState)


def test_automaton::initstate_constructor_exists():
    assert callable(automaton::InitState.__init__)


def test_automaton::initstate_constructor_args():
    sig = inspect.signature(automaton::InitState.__init__)
    params = list(sig.parameters.keys())



def test_automaton::timedzone_is_not_abstract():
    assert not inspect.isabstract(automaton::TimedZone)


def test_automaton::timedzone_constructor_exists():
    assert callable(automaton::TimedZone.__init__)


def test_automaton::timedzone_constructor_args():
    sig = inspect.signature(automaton::TimedZone.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_automaton::timedzone_has_time():
    assert hasattr(automaton::TimedZone, "time")
    descriptor = None
    for klass in automaton::TimedZone.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_automaton::eventtoken_is_not_abstract():
    assert not inspect.isabstract(automaton::EventToken)


def test_automaton::eventtoken_constructor_exists():
    assert callable(automaton::EventToken.__init__)


def test_automaton::eventtoken_constructor_args():
    sig = inspect.signature(automaton::EventToken.__init__)
    params = list(sig.parameters.keys())



def test_automaton::eventpattern_is_not_abstract():
    assert not inspect.isabstract(automaton::EventPattern)


def test_automaton::eventpattern_constructor_exists():
    assert callable(automaton::EventPattern.__init__)


def test_automaton::eventpattern_constructor_args():
    sig = inspect.signature(automaton::EventPattern.__init__)
    params = list(sig.parameters.keys())



def test_automaton::state_is_not_abstract():
    assert not inspect.isabstract(automaton::State)


def test_automaton::state_constructor_exists():
    assert callable(automaton::State.__init__)


def test_automaton::state_constructor_args():
    sig = inspect.signature(automaton::State.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_automaton::state_has_label():
    assert hasattr(automaton::State, "label")
    descriptor = None
    for klass in automaton::State.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_automaton::transition_is_not_abstract():
    assert not inspect.isabstract(automaton::Transition)


def test_automaton::transition_constructor_exists():
    assert callable(automaton::Transition.__init__)


def test_automaton::transition_constructor_args():
    sig = inspect.signature(automaton::Transition.__init__)
    params = list(sig.parameters.keys())



def test_automaton::event_is_not_abstract():
    assert not inspect.isabstract(automaton::Event)


def test_automaton::event_constructor_exists():
    assert callable(automaton::Event.__init__)


def test_automaton::event_constructor_args():
    sig = inspect.signature(automaton::Event.__init__)
    params = list(sig.parameters.keys())



def test_automaton::automaton_is_not_abstract():
    assert not inspect.isabstract(automaton::Automaton)


def test_automaton::automaton_constructor_exists():
    assert callable(automaton::Automaton.__init__)


def test_automaton::automaton_constructor_args():
    sig = inspect.signature(automaton::Automaton.__init__)
    params = list(sig.parameters.keys())



def test_automaton::internalmodel_is_not_abstract():
    assert not inspect.isabstract(automaton::InternalModel)


def test_automaton::internalmodel_constructor_exists():
    assert callable(automaton::InternalModel.__init__)


def test_automaton::internalmodel_constructor_args():
    sig = inspect.signature(automaton::InternalModel.__init__)
    params = list(sig.parameters.keys())
    assert "context" in params, "Missing parameter 'context'"

def test_automaton::internalmodel_has_context():
    assert hasattr(automaton::InternalModel, "context")
    descriptor = None
    for klass in automaton::InternalModel.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_eventcontext_exists():
    # Check that the Enumeration exists
    assert EventContext is not None

def test_eventcontext_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventContext]
    expected_literals = [
        "IMMEDIATE",
        "STRICT_IMMEDIATE",
        "RECENT",
        "CHRONICLE",
        "UNRESTRICTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventContext"


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
automaton::AtomicEventPattern_strategy = st.builds(
    automaton::AtomicEventPattern,
)
automaton::Guard_strategy = st.builds(
    automaton::Guard,
)
Transition_strategy = st.builds(
    Transition,
)
automaton::EpsilonTransition_strategy = st.builds(
    automaton::EpsilonTransition,
)
automaton::TypedTransition_strategy = st.builds(
    automaton::TypedTransition,
)
TimedZone_strategy = st.builds(
    TimedZone,
)
automaton::HoldsFor_strategy = st.builds(
    automaton::HoldsFor,
)
automaton::Within_strategy = st.builds(
    automaton::Within,
)
State_strategy = st.builds(
    State,
)
automaton::FinalState_strategy = st.builds(
    automaton::FinalState,
)
automaton::TrapState_strategy = st.builds(
    automaton::TrapState,
)
automaton::InitState_strategy = st.builds(
    automaton::InitState,
)
automaton::TimedZone_strategy = st.builds(
    automaton::TimedZone,
    time=
        safe_text
)
automaton::EventToken_strategy = st.builds(
    automaton::EventToken,
)
automaton::EventPattern_strategy = st.builds(
    automaton::EventPattern,
)
automaton::State_strategy = st.builds(
    automaton::State,
    label=
        safe_text
)
automaton::Transition_strategy = st.builds(
    automaton::Transition,
)
automaton::Event_strategy = st.builds(
    automaton::Event,
)
automaton::Automaton_strategy = st.builds(
    automaton::Automaton,
)
automaton::InternalModel_strategy = st.builds(
    automaton::InternalModel,
    context=
        safe_text
)

@given(instance=automaton::AtomicEventPattern_strategy)
@settings(max_examples=50)
def test_automaton::atomiceventpattern_instantiation(instance):
    assert isinstance(instance, automaton::AtomicEventPattern)

@given(instance=automaton::Guard_strategy)
@settings(max_examples=50)
def test_automaton::guard_instantiation(instance):
    assert isinstance(instance, automaton::Guard)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=automaton::EpsilonTransition_strategy)
@settings(max_examples=50)
def test_automaton::epsilontransition_instantiation(instance):
    assert isinstance(instance, automaton::EpsilonTransition)

@given(instance=automaton::TypedTransition_strategy)
@settings(max_examples=50)
def test_automaton::typedtransition_instantiation(instance):
    assert isinstance(instance, automaton::TypedTransition)

@given(instance=TimedZone_strategy)
@settings(max_examples=50)
def test_timedzone_instantiation(instance):
    assert isinstance(instance, TimedZone)

@given(instance=automaton::HoldsFor_strategy)
@settings(max_examples=50)
def test_automaton::holdsfor_instantiation(instance):
    assert isinstance(instance, automaton::HoldsFor)

@given(instance=automaton::Within_strategy)
@settings(max_examples=50)
def test_automaton::within_instantiation(instance):
    assert isinstance(instance, automaton::Within)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=automaton::FinalState_strategy)
@settings(max_examples=50)
def test_automaton::finalstate_instantiation(instance):
    assert isinstance(instance, automaton::FinalState)

@given(instance=automaton::TrapState_strategy)
@settings(max_examples=50)
def test_automaton::trapstate_instantiation(instance):
    assert isinstance(instance, automaton::TrapState)

@given(instance=automaton::InitState_strategy)
@settings(max_examples=50)
def test_automaton::initstate_instantiation(instance):
    assert isinstance(instance, automaton::InitState)

@given(instance=automaton::TimedZone_strategy)
@settings(max_examples=50)
def test_automaton::timedzone_instantiation(instance):
    assert isinstance(instance, automaton::TimedZone)

@given(instance=automaton::TimedZone_strategy)
def test_automaton::timedzone_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=automaton::TimedZone_strategy)
def test_automaton::timedzone_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=automaton::EventToken_strategy)
@settings(max_examples=50)
def test_automaton::eventtoken_instantiation(instance):
    assert isinstance(instance, automaton::EventToken)

@given(instance=automaton::EventPattern_strategy)
@settings(max_examples=50)
def test_automaton::eventpattern_instantiation(instance):
    assert isinstance(instance, automaton::EventPattern)

@given(instance=automaton::State_strategy)
@settings(max_examples=50)
def test_automaton::state_instantiation(instance):
    assert isinstance(instance, automaton::State)

@given(instance=automaton::State_strategy)
def test_automaton::state_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=automaton::State_strategy)
def test_automaton::state_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=automaton::Transition_strategy)
@settings(max_examples=50)
def test_automaton::transition_instantiation(instance):
    assert isinstance(instance, automaton::Transition)

@given(instance=automaton::Event_strategy)
@settings(max_examples=50)
def test_automaton::event_instantiation(instance):
    assert isinstance(instance, automaton::Event)

@given(instance=automaton::Automaton_strategy)
@settings(max_examples=50)
def test_automaton::automaton_instantiation(instance):
    assert isinstance(instance, automaton::Automaton)

@given(instance=automaton::InternalModel_strategy)
@settings(max_examples=50)
def test_automaton::internalmodel_instantiation(instance):
    assert isinstance(instance, automaton::InternalModel)

@given(instance=automaton::InternalModel_strategy)
def test_automaton::internalmodel_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=automaton::InternalModel_strategy)
def test_automaton::internalmodel_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

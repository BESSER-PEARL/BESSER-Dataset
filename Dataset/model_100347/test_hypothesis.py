import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    automaton::ParameterBinding,
    TimedZone,
    automaton::HoldsFor,
    automaton::Within,
    automaton::EventPattern,
    TypedTransition,
    automaton::NegativeTransition,
    automaton::Parameter,
    automaton::Guard,
    Transition,
    automaton::EpsilonTransition,
    automaton::TypedTransition,
    automaton::Transition,
    State,
    automaton::ParameterTable,
    automaton::TrapState,
    automaton::FinalState,
    automaton::InitState,
    automaton::State,
    automaton::EventToken,
    automaton::Event,
    automaton::TimedZone,
    automaton::Automaton,
    automaton::InternalModel,
    EventContext,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_automaton::parameterbinding_is_not_abstract():
    assert not inspect.isabstract(automaton::ParameterBinding)


def test_automaton::parameterbinding_constructor_exists():
    assert callable(automaton::ParameterBinding.__init__)


def test_automaton::parameterbinding_constructor_args():
    sig = inspect.signature(automaton::ParameterBinding.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "symbolicName" in params, "Missing parameter 'symbolicName'"

def test_automaton::parameterbinding_has_value():
    assert hasattr(automaton::ParameterBinding, "value")
    descriptor = None
    for klass in automaton::ParameterBinding.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_automaton::parameterbinding_has_symbolicName():
    assert hasattr(automaton::ParameterBinding, "symbolicName")
    descriptor = None
    for klass in automaton::ParameterBinding.__mro__:
        if "symbolicName" in klass.__dict__:
            descriptor = klass.__dict__["symbolicName"]
            break
    assert isinstance(descriptor, property)



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



def test_automaton::eventpattern_is_not_abstract():
    assert not inspect.isabstract(automaton::EventPattern)


def test_automaton::eventpattern_constructor_exists():
    assert callable(automaton::EventPattern.__init__)


def test_automaton::eventpattern_constructor_args():
    sig = inspect.signature(automaton::EventPattern.__init__)
    params = list(sig.parameters.keys())



def test_typedtransition_is_not_abstract():
    assert not inspect.isabstract(TypedTransition)


def test_typedtransition_constructor_exists():
    assert callable(TypedTransition.__init__)


def test_typedtransition_constructor_args():
    sig = inspect.signature(TypedTransition.__init__)
    params = list(sig.parameters.keys())



def test_automaton::negativetransition_is_not_abstract():
    assert not inspect.isabstract(automaton::NegativeTransition)


def test_automaton::negativetransition_constructor_exists():
    assert callable(automaton::NegativeTransition.__init__)


def test_automaton::negativetransition_constructor_args():
    sig = inspect.signature(automaton::NegativeTransition.__init__)
    params = list(sig.parameters.keys())



def test_automaton::parameter_is_not_abstract():
    assert not inspect.isabstract(automaton::Parameter)


def test_automaton::parameter_constructor_exists():
    assert callable(automaton::Parameter.__init__)


def test_automaton::parameter_constructor_args():
    sig = inspect.signature(automaton::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "symbolicName" in params, "Missing parameter 'symbolicName'"
    assert "position" in params, "Missing parameter 'position'"

def test_automaton::parameter_has_symbolicName():
    assert hasattr(automaton::Parameter, "symbolicName")
    descriptor = None
    for klass in automaton::Parameter.__mro__:
        if "symbolicName" in klass.__dict__:
            descriptor = klass.__dict__["symbolicName"]
            break
    assert isinstance(descriptor, property)

def test_automaton::parameter_has_position():
    assert hasattr(automaton::Parameter, "position")
    descriptor = None
    for klass in automaton::Parameter.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



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



def test_automaton::transition_is_not_abstract():
    assert not inspect.isabstract(automaton::Transition)


def test_automaton::transition_constructor_exists():
    assert callable(automaton::Transition.__init__)


def test_automaton::transition_constructor_args():
    sig = inspect.signature(automaton::Transition.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_automaton::parametertable_is_not_abstract():
    assert not inspect.isabstract(automaton::ParameterTable)


def test_automaton::parametertable_constructor_exists():
    assert callable(automaton::ParameterTable.__init__)


def test_automaton::parametertable_constructor_args():
    sig = inspect.signature(automaton::ParameterTable.__init__)
    params = list(sig.parameters.keys())



def test_automaton::trapstate_is_not_abstract():
    assert not inspect.isabstract(automaton::TrapState)


def test_automaton::trapstate_constructor_exists():
    assert callable(automaton::TrapState.__init__)


def test_automaton::trapstate_constructor_args():
    sig = inspect.signature(automaton::TrapState.__init__)
    params = list(sig.parameters.keys())



def test_automaton::finalstate_is_not_abstract():
    assert not inspect.isabstract(automaton::FinalState)


def test_automaton::finalstate_constructor_exists():
    assert callable(automaton::FinalState.__init__)


def test_automaton::finalstate_constructor_args():
    sig = inspect.signature(automaton::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_automaton::initstate_is_not_abstract():
    assert not inspect.isabstract(automaton::InitState)


def test_automaton::initstate_constructor_exists():
    assert callable(automaton::InitState.__init__)


def test_automaton::initstate_constructor_args():
    sig = inspect.signature(automaton::InitState.__init__)
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



def test_automaton::eventtoken_is_not_abstract():
    assert not inspect.isabstract(automaton::EventToken)


def test_automaton::eventtoken_constructor_exists():
    assert callable(automaton::EventToken.__init__)


def test_automaton::eventtoken_constructor_args():
    sig = inspect.signature(automaton::EventToken.__init__)
    params = list(sig.parameters.keys())



def test_automaton::event_is_not_abstract():
    assert not inspect.isabstract(automaton::Event)


def test_automaton::event_constructor_exists():
    assert callable(automaton::Event.__init__)


def test_automaton::event_constructor_args():
    sig = inspect.signature(automaton::Event.__init__)
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



def test_automaton::automaton_is_not_abstract():
    assert not inspect.isabstract(automaton::Automaton)


def test_automaton::automaton_constructor_exists():
    assert callable(automaton::Automaton.__init__)


def test_automaton::automaton_constructor_args():
    sig = inspect.signature(automaton::Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "eventPatternId" in params, "Missing parameter 'eventPatternId'"

def test_automaton::automaton_has_eventPatternId():
    assert hasattr(automaton::Automaton, "eventPatternId")
    descriptor = None
    for klass in automaton::Automaton.__mro__:
        if "eventPatternId" in klass.__dict__:
            descriptor = klass.__dict__["eventPatternId"]
            break
    assert isinstance(descriptor, property)



def test_automaton::internalmodel_is_not_abstract():
    assert not inspect.isabstract(automaton::InternalModel)


def test_automaton::internalmodel_constructor_exists():
    assert callable(automaton::InternalModel.__init__)


def test_automaton::internalmodel_constructor_args():
    sig = inspect.signature(automaton::InternalModel.__init__)
    params = list(sig.parameters.keys())

def test_eventcontext_exists():
    # Check that the Enumeration exists
    assert EventContext is not None

def test_eventcontext_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventContext]
    expected_literals = [
        "IMMEDIATE",
        "RECENT",
        "UNRESTRICTED",
        "CHRONICLE",
        "STRICT_IMMEDIATE",
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
automaton::ParameterBinding_strategy = st.builds(
    automaton::ParameterBinding,
    value=
        safe_text,
    symbolicName=
        safe_text
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
automaton::EventPattern_strategy = st.builds(
    automaton::EventPattern,
)
TypedTransition_strategy = st.builds(
    TypedTransition,
)
automaton::NegativeTransition_strategy = st.builds(
    automaton::NegativeTransition,
)
automaton::Parameter_strategy = st.builds(
    automaton::Parameter,
    symbolicName=
        safe_text,
    position=
        st.integers()
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
automaton::Transition_strategy = st.builds(
    automaton::Transition,
)
State_strategy = st.builds(
    State,
)
automaton::ParameterTable_strategy = st.builds(
    automaton::ParameterTable,
)
automaton::TrapState_strategy = st.builds(
    automaton::TrapState,
)
automaton::FinalState_strategy = st.builds(
    automaton::FinalState,
)
automaton::InitState_strategy = st.builds(
    automaton::InitState,
)
automaton::State_strategy = st.builds(
    automaton::State,
    label=
        safe_text
)
automaton::EventToken_strategy = st.builds(
    automaton::EventToken,
)
automaton::Event_strategy = st.builds(
    automaton::Event,
)
automaton::TimedZone_strategy = st.builds(
    automaton::TimedZone,
    time=
        safe_text
)
automaton::Automaton_strategy = st.builds(
    automaton::Automaton,
    eventPatternId=
        safe_text
)
automaton::InternalModel_strategy = st.builds(
    automaton::InternalModel,
)

@given(instance=automaton::ParameterBinding_strategy)
@settings(max_examples=50)
def test_automaton::parameterbinding_instantiation(instance):
    assert isinstance(instance, automaton::ParameterBinding)

@given(instance=automaton::ParameterBinding_strategy)
def test_automaton::parameterbinding_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=automaton::ParameterBinding_strategy)
def test_automaton::parameterbinding_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=automaton::ParameterBinding_strategy)
def test_automaton::parameterbinding_symbolicName_type(instance):
    assert isinstance(instance.symbolicName, str)


@given(instance=automaton::ParameterBinding_strategy)
def test_automaton::parameterbinding_symbolicName_setter(instance):
    original = instance.symbolicName
    instance.symbolicName = original
    assert instance.symbolicName == original

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

@given(instance=automaton::EventPattern_strategy)
@settings(max_examples=50)
def test_automaton::eventpattern_instantiation(instance):
    assert isinstance(instance, automaton::EventPattern)

@given(instance=TypedTransition_strategy)
@settings(max_examples=50)
def test_typedtransition_instantiation(instance):
    assert isinstance(instance, TypedTransition)

@given(instance=automaton::NegativeTransition_strategy)
@settings(max_examples=50)
def test_automaton::negativetransition_instantiation(instance):
    assert isinstance(instance, automaton::NegativeTransition)

@given(instance=automaton::Parameter_strategy)
@settings(max_examples=50)
def test_automaton::parameter_instantiation(instance):
    assert isinstance(instance, automaton::Parameter)

@given(instance=automaton::Parameter_strategy)
def test_automaton::parameter_symbolicName_type(instance):
    assert isinstance(instance.symbolicName, str)


@given(instance=automaton::Parameter_strategy)
def test_automaton::parameter_symbolicName_setter(instance):
    original = instance.symbolicName
    instance.symbolicName = original
    assert instance.symbolicName == original

@given(instance=automaton::Parameter_strategy)
def test_automaton::parameter_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=automaton::Parameter_strategy)
def test_automaton::parameter_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

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

@given(instance=automaton::Transition_strategy)
@settings(max_examples=50)
def test_automaton::transition_instantiation(instance):
    assert isinstance(instance, automaton::Transition)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=automaton::ParameterTable_strategy)
@settings(max_examples=50)
def test_automaton::parametertable_instantiation(instance):
    assert isinstance(instance, automaton::ParameterTable)

@given(instance=automaton::TrapState_strategy)
@settings(max_examples=50)
def test_automaton::trapstate_instantiation(instance):
    assert isinstance(instance, automaton::TrapState)

@given(instance=automaton::FinalState_strategy)
@settings(max_examples=50)
def test_automaton::finalstate_instantiation(instance):
    assert isinstance(instance, automaton::FinalState)

@given(instance=automaton::InitState_strategy)
@settings(max_examples=50)
def test_automaton::initstate_instantiation(instance):
    assert isinstance(instance, automaton::InitState)

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

@given(instance=automaton::EventToken_strategy)
@settings(max_examples=50)
def test_automaton::eventtoken_instantiation(instance):
    assert isinstance(instance, automaton::EventToken)

@given(instance=automaton::Event_strategy)
@settings(max_examples=50)
def test_automaton::event_instantiation(instance):
    assert isinstance(instance, automaton::Event)

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

@given(instance=automaton::Automaton_strategy)
@settings(max_examples=50)
def test_automaton::automaton_instantiation(instance):
    assert isinstance(instance, automaton::Automaton)

@given(instance=automaton::Automaton_strategy)
def test_automaton::automaton_eventPatternId_type(instance):
    assert isinstance(instance.eventPatternId, str)


@given(instance=automaton::Automaton_strategy)
def test_automaton::automaton_eventPatternId_setter(instance):
    original = instance.eventPatternId
    instance.eventPatternId = original
    assert instance.eventPatternId == original

@given(instance=automaton::InternalModel_strategy)
@settings(max_examples=50)
def test_automaton::internalmodel_instantiation(instance):
    assert isinstance(instance, automaton::InternalModel)

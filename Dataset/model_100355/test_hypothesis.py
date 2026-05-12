import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EventAutomatonModel::NotEquivalentRelation,
    EventAutomatonModel::Action,
    EventAutomatonModel::EventGuard,
    EventAutomatonModel::Event,
    AbstractTransition,
    EventAutomatonModel::Transition,
    EventAutomatonModel::EpsilonTransition,
    Action,
    EventAutomatonModel::TimerAction,
    EventAutomatonModel::Binding,
    Parameter,
    EventAutomatonModel::FreeParameter,
    EventAutomatonModel::FixParameter,
    EventAutomatonModel::AbstractTransition,
    SymbolicParameter,
    EventAutomatonModel::SymbolicEventParameter,
    EventAutomatonModel::Parameter,
    EventAutomatonModel::SymbolicEvent,
    EventAutomatonModel::ComplexEventProcessor,
    EventAutomatonModel::SymbolicTimer,
    SymbolicEvent,
    EventAutomatonModel::SymbolicTimeoutEvent,
    EventAutomatonModel::SymbolicInputEvent,
    TimerAction,
    EventAutomatonModel::SetTimerAction,
    EventAutomatonModel::ResetTimerAction,
    EventAutomatonModel::SymbolicTokenParameter,
    Binding,
    EventAutomatonModel::ConstantBinding,
    EventAutomatonModel::TokenParameterBinding,
    EventAutomatonModel::SymbolicParameter,
    EventAutomatonModel::Token,
    EventAutomatonModel::State,
    EventAutomatonModel::Automaton,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eventautomatonmodel::notequivalentrelation_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::NotEquivalentRelation)


def test_eventautomatonmodel::notequivalentrelation_constructor_exists():
    assert callable(EventAutomatonModel::NotEquivalentRelation.__init__)


def test_eventautomatonmodel::notequivalentrelation_constructor_args():
    sig = inspect.signature(EventAutomatonModel::NotEquivalentRelation.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::action_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::Action)


def test_eventautomatonmodel::action_constructor_exists():
    assert callable(EventAutomatonModel::Action.__init__)


def test_eventautomatonmodel::action_constructor_args():
    sig = inspect.signature(EventAutomatonModel::Action.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::eventguard_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::EventGuard)


def test_eventautomatonmodel::eventguard_constructor_exists():
    assert callable(EventAutomatonModel::EventGuard.__init__)


def test_eventautomatonmodel::eventguard_constructor_args():
    sig = inspect.signature(EventAutomatonModel::EventGuard.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::event_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::Event)


def test_eventautomatonmodel::event_constructor_exists():
    assert callable(EventAutomatonModel::Event.__init__)


def test_eventautomatonmodel::event_constructor_args():
    sig = inspect.signature(EventAutomatonModel::Event.__init__)
    params = list(sig.parameters.keys())



def test_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(AbstractTransition)


def test_abstracttransition_constructor_exists():
    assert callable(AbstractTransition.__init__)


def test_abstracttransition_constructor_args():
    sig = inspect.signature(AbstractTransition.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::transition_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::Transition)


def test_eventautomatonmodel::transition_constructor_exists():
    assert callable(EventAutomatonModel::Transition.__init__)


def test_eventautomatonmodel::transition_constructor_args():
    sig = inspect.signature(EventAutomatonModel::Transition.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::epsilontransition_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::EpsilonTransition)


def test_eventautomatonmodel::epsilontransition_constructor_exists():
    assert callable(EventAutomatonModel::EpsilonTransition.__init__)


def test_eventautomatonmodel::epsilontransition_constructor_args():
    sig = inspect.signature(EventAutomatonModel::EpsilonTransition.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::timeraction_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::TimerAction)


def test_eventautomatonmodel::timeraction_constructor_exists():
    assert callable(EventAutomatonModel::TimerAction.__init__)


def test_eventautomatonmodel::timeraction_constructor_args():
    sig = inspect.signature(EventAutomatonModel::TimerAction.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::binding_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::Binding)


def test_eventautomatonmodel::binding_constructor_exists():
    assert callable(EventAutomatonModel::Binding.__init__)


def test_eventautomatonmodel::binding_constructor_args():
    sig = inspect.signature(EventAutomatonModel::Binding.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::freeparameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::FreeParameter)


def test_eventautomatonmodel::freeparameter_constructor_exists():
    assert callable(EventAutomatonModel::FreeParameter.__init__)


def test_eventautomatonmodel::freeparameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel::FreeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "excludedValues" in params, "Missing parameter 'excludedValues'"

def test_eventautomatonmodel::freeparameter_has_excludedValues():
    assert hasattr(EventAutomatonModel::FreeParameter, "excludedValues")
    descriptor = None
    for klass in EventAutomatonModel::FreeParameter.__mro__:
        if "excludedValues" in klass.__dict__:
            descriptor = klass.__dict__["excludedValues"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel::fixparameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::FixParameter)


def test_eventautomatonmodel::fixparameter_constructor_exists():
    assert callable(EventAutomatonModel::FixParameter.__init__)


def test_eventautomatonmodel::fixparameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel::FixParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eventautomatonmodel::fixparameter_has_value():
    assert hasattr(EventAutomatonModel::FixParameter, "value")
    descriptor = None
    for klass in EventAutomatonModel::FixParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel::abstracttransition_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::AbstractTransition)


def test_eventautomatonmodel::abstracttransition_constructor_exists():
    assert callable(EventAutomatonModel::AbstractTransition.__init__)


def test_eventautomatonmodel::abstracttransition_constructor_args():
    sig = inspect.signature(EventAutomatonModel::AbstractTransition.__init__)
    params = list(sig.parameters.keys())



def test_symbolicparameter_is_not_abstract():
    assert not inspect.isabstract(SymbolicParameter)


def test_symbolicparameter_constructor_exists():
    assert callable(SymbolicParameter.__init__)


def test_symbolicparameter_constructor_args():
    sig = inspect.signature(SymbolicParameter.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::symboliceventparameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::SymbolicEventParameter)


def test_eventautomatonmodel::symboliceventparameter_constructor_exists():
    assert callable(EventAutomatonModel::SymbolicEventParameter.__init__)


def test_eventautomatonmodel::symboliceventparameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel::SymbolicEventParameter.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::parameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::Parameter)


def test_eventautomatonmodel::parameter_constructor_exists():
    assert callable(EventAutomatonModel::Parameter.__init__)


def test_eventautomatonmodel::parameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::symbolicevent_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::SymbolicEvent)


def test_eventautomatonmodel::symbolicevent_constructor_exists():
    assert callable(EventAutomatonModel::SymbolicEvent.__init__)


def test_eventautomatonmodel::symbolicevent_constructor_args():
    sig = inspect.signature(EventAutomatonModel::SymbolicEvent.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::complexeventprocessor_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::ComplexEventProcessor)


def test_eventautomatonmodel::complexeventprocessor_constructor_exists():
    assert callable(EventAutomatonModel::ComplexEventProcessor.__init__)


def test_eventautomatonmodel::complexeventprocessor_constructor_args():
    sig = inspect.signature(EventAutomatonModel::ComplexEventProcessor.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::symbolictimer_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::SymbolicTimer)


def test_eventautomatonmodel::symbolictimer_constructor_exists():
    assert callable(EventAutomatonModel::SymbolicTimer.__init__)


def test_eventautomatonmodel::symbolictimer_constructor_args():
    sig = inspect.signature(EventAutomatonModel::SymbolicTimer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eventautomatonmodel::symbolictimer_has_name():
    assert hasattr(EventAutomatonModel::SymbolicTimer, "name")
    descriptor = None
    for klass in EventAutomatonModel::SymbolicTimer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_symbolicevent_is_not_abstract():
    assert not inspect.isabstract(SymbolicEvent)


def test_symbolicevent_constructor_exists():
    assert callable(SymbolicEvent.__init__)


def test_symbolicevent_constructor_args():
    sig = inspect.signature(SymbolicEvent.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::symbolictimeoutevent_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::SymbolicTimeoutEvent)


def test_eventautomatonmodel::symbolictimeoutevent_constructor_exists():
    assert callable(EventAutomatonModel::SymbolicTimeoutEvent.__init__)


def test_eventautomatonmodel::symbolictimeoutevent_constructor_args():
    sig = inspect.signature(EventAutomatonModel::SymbolicTimeoutEvent.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::symbolicinputevent_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::SymbolicInputEvent)


def test_eventautomatonmodel::symbolicinputevent_constructor_exists():
    assert callable(EventAutomatonModel::SymbolicInputEvent.__init__)


def test_eventautomatonmodel::symbolicinputevent_constructor_args():
    sig = inspect.signature(EventAutomatonModel::SymbolicInputEvent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eventautomatonmodel::symbolicinputevent_has_name():
    assert hasattr(EventAutomatonModel::SymbolicInputEvent, "name")
    descriptor = None
    for klass in EventAutomatonModel::SymbolicInputEvent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_timeraction_is_not_abstract():
    assert not inspect.isabstract(TimerAction)


def test_timeraction_constructor_exists():
    assert callable(TimerAction.__init__)


def test_timeraction_constructor_args():
    sig = inspect.signature(TimerAction.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::settimeraction_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::SetTimerAction)


def test_eventautomatonmodel::settimeraction_constructor_exists():
    assert callable(EventAutomatonModel::SetTimerAction.__init__)


def test_eventautomatonmodel::settimeraction_constructor_args():
    sig = inspect.signature(EventAutomatonModel::SetTimerAction.__init__)
    params = list(sig.parameters.keys())
    assert "toValue" in params, "Missing parameter 'toValue'"

def test_eventautomatonmodel::settimeraction_has_toValue():
    assert hasattr(EventAutomatonModel::SetTimerAction, "toValue")
    descriptor = None
    for klass in EventAutomatonModel::SetTimerAction.__mro__:
        if "toValue" in klass.__dict__:
            descriptor = klass.__dict__["toValue"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel::resettimeraction_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::ResetTimerAction)


def test_eventautomatonmodel::resettimeraction_constructor_exists():
    assert callable(EventAutomatonModel::ResetTimerAction.__init__)


def test_eventautomatonmodel::resettimeraction_constructor_args():
    sig = inspect.signature(EventAutomatonModel::ResetTimerAction.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::symbolictokenparameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::SymbolicTokenParameter)


def test_eventautomatonmodel::symbolictokenparameter_constructor_exists():
    assert callable(EventAutomatonModel::SymbolicTokenParameter.__init__)


def test_eventautomatonmodel::symbolictokenparameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel::SymbolicTokenParameter.__init__)
    params = list(sig.parameters.keys())



def test_binding_is_not_abstract():
    assert not inspect.isabstract(Binding)


def test_binding_constructor_exists():
    assert callable(Binding.__init__)


def test_binding_constructor_args():
    sig = inspect.signature(Binding.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::constantbinding_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::ConstantBinding)


def test_eventautomatonmodel::constantbinding_constructor_exists():
    assert callable(EventAutomatonModel::ConstantBinding.__init__)


def test_eventautomatonmodel::constantbinding_constructor_args():
    sig = inspect.signature(EventAutomatonModel::ConstantBinding.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::tokenparameterbinding_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::TokenParameterBinding)


def test_eventautomatonmodel::tokenparameterbinding_constructor_exists():
    assert callable(EventAutomatonModel::TokenParameterBinding.__init__)


def test_eventautomatonmodel::tokenparameterbinding_constructor_args():
    sig = inspect.signature(EventAutomatonModel::TokenParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::symbolicparameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::SymbolicParameter)


def test_eventautomatonmodel::symbolicparameter_constructor_exists():
    assert callable(EventAutomatonModel::SymbolicParameter.__init__)


def test_eventautomatonmodel::symbolicparameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel::SymbolicParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eventautomatonmodel::symbolicparameter_has_name():
    assert hasattr(EventAutomatonModel::SymbolicParameter, "name")
    descriptor = None
    for klass in EventAutomatonModel::SymbolicParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel::token_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::Token)


def test_eventautomatonmodel::token_constructor_exists():
    assert callable(EventAutomatonModel::Token.__init__)


def test_eventautomatonmodel::token_constructor_args():
    sig = inspect.signature(EventAutomatonModel::Token.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel::state_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::State)


def test_eventautomatonmodel::state_constructor_exists():
    assert callable(EventAutomatonModel::State.__init__)


def test_eventautomatonmodel::state_constructor_args():
    sig = inspect.signature(EventAutomatonModel::State.__init__)
    params = list(sig.parameters.keys())
    assert "acceptor" in params, "Missing parameter 'acceptor'"
    assert "id" in params, "Missing parameter 'id'"

def test_eventautomatonmodel::state_has_acceptor():
    assert hasattr(EventAutomatonModel::State, "acceptor")
    descriptor = None
    for klass in EventAutomatonModel::State.__mro__:
        if "acceptor" in klass.__dict__:
            descriptor = klass.__dict__["acceptor"]
            break
    assert isinstance(descriptor, property)

def test_eventautomatonmodel::state_has_id():
    assert hasattr(EventAutomatonModel::State, "id")
    descriptor = None
    for klass in EventAutomatonModel::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel::automaton_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel::Automaton)


def test_eventautomatonmodel::automaton_constructor_exists():
    assert callable(EventAutomatonModel::Automaton.__init__)


def test_eventautomatonmodel::automaton_constructor_args():
    sig = inspect.signature(EventAutomatonModel::Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eventautomatonmodel::automaton_has_name():
    assert hasattr(EventAutomatonModel::Automaton, "name")
    descriptor = None
    for klass in EventAutomatonModel::Automaton.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
EventAutomatonModel::NotEquivalentRelation_strategy = st.builds(
    EventAutomatonModel::NotEquivalentRelation,
)
EventAutomatonModel::Action_strategy = st.builds(
    EventAutomatonModel::Action,
)
EventAutomatonModel::EventGuard_strategy = st.builds(
    EventAutomatonModel::EventGuard,
)
EventAutomatonModel::Event_strategy = st.builds(
    EventAutomatonModel::Event,
)
AbstractTransition_strategy = st.builds(
    AbstractTransition,
)
EventAutomatonModel::Transition_strategy = st.builds(
    EventAutomatonModel::Transition,
)
EventAutomatonModel::EpsilonTransition_strategy = st.builds(
    EventAutomatonModel::EpsilonTransition,
)
Action_strategy = st.builds(
    Action,
)
EventAutomatonModel::TimerAction_strategy = st.builds(
    EventAutomatonModel::TimerAction,
)
EventAutomatonModel::Binding_strategy = st.builds(
    EventAutomatonModel::Binding,
)
Parameter_strategy = st.builds(
    Parameter,
)
EventAutomatonModel::FreeParameter_strategy = st.builds(
    EventAutomatonModel::FreeParameter,
    excludedValues=
        safe_text
)
EventAutomatonModel::FixParameter_strategy = st.builds(
    EventAutomatonModel::FixParameter,
    value=
        safe_text
)
EventAutomatonModel::AbstractTransition_strategy = st.builds(
    EventAutomatonModel::AbstractTransition,
)
SymbolicParameter_strategy = st.builds(
    SymbolicParameter,
)
EventAutomatonModel::SymbolicEventParameter_strategy = st.builds(
    EventAutomatonModel::SymbolicEventParameter,
)
EventAutomatonModel::Parameter_strategy = st.builds(
    EventAutomatonModel::Parameter,
)
EventAutomatonModel::SymbolicEvent_strategy = st.builds(
    EventAutomatonModel::SymbolicEvent,
)
EventAutomatonModel::ComplexEventProcessor_strategy = st.builds(
    EventAutomatonModel::ComplexEventProcessor,
)
EventAutomatonModel::SymbolicTimer_strategy = st.builds(
    EventAutomatonModel::SymbolicTimer,
    name=
        safe_text
)
SymbolicEvent_strategy = st.builds(
    SymbolicEvent,
)
EventAutomatonModel::SymbolicTimeoutEvent_strategy = st.builds(
    EventAutomatonModel::SymbolicTimeoutEvent,
)
EventAutomatonModel::SymbolicInputEvent_strategy = st.builds(
    EventAutomatonModel::SymbolicInputEvent,
    name=
        safe_text
)
TimerAction_strategy = st.builds(
    TimerAction,
)
EventAutomatonModel::SetTimerAction_strategy = st.builds(
    EventAutomatonModel::SetTimerAction,
    toValue=
        st.integers()
)
EventAutomatonModel::ResetTimerAction_strategy = st.builds(
    EventAutomatonModel::ResetTimerAction,
)
EventAutomatonModel::SymbolicTokenParameter_strategy = st.builds(
    EventAutomatonModel::SymbolicTokenParameter,
)
Binding_strategy = st.builds(
    Binding,
)
EventAutomatonModel::ConstantBinding_strategy = st.builds(
    EventAutomatonModel::ConstantBinding,
)
EventAutomatonModel::TokenParameterBinding_strategy = st.builds(
    EventAutomatonModel::TokenParameterBinding,
)
EventAutomatonModel::SymbolicParameter_strategy = st.builds(
    EventAutomatonModel::SymbolicParameter,
    name=
        safe_text
)
EventAutomatonModel::Token_strategy = st.builds(
    EventAutomatonModel::Token,
)
EventAutomatonModel::State_strategy = st.builds(
    EventAutomatonModel::State,
    acceptor=
        safe_text,
    id=
        st.integers()
)
EventAutomatonModel::Automaton_strategy = st.builds(
    EventAutomatonModel::Automaton,
    name=
        safe_text
)

@given(instance=EventAutomatonModel::NotEquivalentRelation_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::notequivalentrelation_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::NotEquivalentRelation)

@given(instance=EventAutomatonModel::Action_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::action_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::Action)

@given(instance=EventAutomatonModel::EventGuard_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::eventguard_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::EventGuard)

@given(instance=EventAutomatonModel::Event_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::event_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::Event)

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=EventAutomatonModel::Transition_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::transition_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::Transition)

@given(instance=EventAutomatonModel::EpsilonTransition_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::epsilontransition_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::EpsilonTransition)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=EventAutomatonModel::TimerAction_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::timeraction_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::TimerAction)

@given(instance=EventAutomatonModel::Binding_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::binding_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::Binding)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=EventAutomatonModel::FreeParameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::freeparameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::FreeParameter)

@given(instance=EventAutomatonModel::FreeParameter_strategy)
def test_eventautomatonmodel::freeparameter_excludedValues_type(instance):
    assert isinstance(instance.excludedValues, str)


@given(instance=EventAutomatonModel::FreeParameter_strategy)
def test_eventautomatonmodel::freeparameter_excludedValues_setter(instance):
    original = instance.excludedValues
    instance.excludedValues = original
    assert instance.excludedValues == original

@given(instance=EventAutomatonModel::FixParameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::fixparameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::FixParameter)

@given(instance=EventAutomatonModel::FixParameter_strategy)
def test_eventautomatonmodel::fixparameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=EventAutomatonModel::FixParameter_strategy)
def test_eventautomatonmodel::fixparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=EventAutomatonModel::AbstractTransition_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::abstracttransition_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::AbstractTransition)

@given(instance=SymbolicParameter_strategy)
@settings(max_examples=50)
def test_symbolicparameter_instantiation(instance):
    assert isinstance(instance, SymbolicParameter)

@given(instance=EventAutomatonModel::SymbolicEventParameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::symboliceventparameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::SymbolicEventParameter)

@given(instance=EventAutomatonModel::Parameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::parameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::Parameter)

@given(instance=EventAutomatonModel::SymbolicEvent_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::symbolicevent_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::SymbolicEvent)

@given(instance=EventAutomatonModel::ComplexEventProcessor_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::complexeventprocessor_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::ComplexEventProcessor)

@given(instance=EventAutomatonModel::SymbolicTimer_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::symbolictimer_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::SymbolicTimer)

@given(instance=EventAutomatonModel::SymbolicTimer_strategy)
def test_eventautomatonmodel::symbolictimer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EventAutomatonModel::SymbolicTimer_strategy)
def test_eventautomatonmodel::symbolictimer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SymbolicEvent_strategy)
@settings(max_examples=50)
def test_symbolicevent_instantiation(instance):
    assert isinstance(instance, SymbolicEvent)

@given(instance=EventAutomatonModel::SymbolicTimeoutEvent_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::symbolictimeoutevent_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::SymbolicTimeoutEvent)

@given(instance=EventAutomatonModel::SymbolicInputEvent_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::symbolicinputevent_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::SymbolicInputEvent)

@given(instance=EventAutomatonModel::SymbolicInputEvent_strategy)
def test_eventautomatonmodel::symbolicinputevent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EventAutomatonModel::SymbolicInputEvent_strategy)
def test_eventautomatonmodel::symbolicinputevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TimerAction_strategy)
@settings(max_examples=50)
def test_timeraction_instantiation(instance):
    assert isinstance(instance, TimerAction)

@given(instance=EventAutomatonModel::SetTimerAction_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::settimeraction_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::SetTimerAction)

@given(instance=EventAutomatonModel::SetTimerAction_strategy)
def test_eventautomatonmodel::settimeraction_toValue_type(instance):
    assert isinstance(instance.toValue, int)


@given(instance=EventAutomatonModel::SetTimerAction_strategy)
def test_eventautomatonmodel::settimeraction_toValue_setter(instance):
    original = instance.toValue
    instance.toValue = original
    assert instance.toValue == original

@given(instance=EventAutomatonModel::ResetTimerAction_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::resettimeraction_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::ResetTimerAction)

@given(instance=EventAutomatonModel::SymbolicTokenParameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::symbolictokenparameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::SymbolicTokenParameter)

@given(instance=Binding_strategy)
@settings(max_examples=50)
def test_binding_instantiation(instance):
    assert isinstance(instance, Binding)

@given(instance=EventAutomatonModel::ConstantBinding_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::constantbinding_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::ConstantBinding)

@given(instance=EventAutomatonModel::TokenParameterBinding_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::tokenparameterbinding_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::TokenParameterBinding)

@given(instance=EventAutomatonModel::SymbolicParameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::symbolicparameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::SymbolicParameter)

@given(instance=EventAutomatonModel::SymbolicParameter_strategy)
def test_eventautomatonmodel::symbolicparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EventAutomatonModel::SymbolicParameter_strategy)
def test_eventautomatonmodel::symbolicparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EventAutomatonModel::Token_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::token_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::Token)

@given(instance=EventAutomatonModel::State_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::state_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::State)

@given(instance=EventAutomatonModel::State_strategy)
def test_eventautomatonmodel::state_acceptor_type(instance):
    assert isinstance(instance.acceptor, str)


@given(instance=EventAutomatonModel::State_strategy)
def test_eventautomatonmodel::state_acceptor_setter(instance):
    original = instance.acceptor
    instance.acceptor = original
    assert instance.acceptor == original

@given(instance=EventAutomatonModel::State_strategy)
def test_eventautomatonmodel::state_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=EventAutomatonModel::State_strategy)
def test_eventautomatonmodel::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=EventAutomatonModel::Automaton_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel::automaton_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel::Automaton)

@given(instance=EventAutomatonModel::Automaton_strategy)
def test_eventautomatonmodel::automaton_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EventAutomatonModel::Automaton_strategy)
def test_eventautomatonmodel::automaton_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EventAutomatonModel_SymbolicEvent,
    Action,
    EventAutomatonModel_TimerAction,
    EventAutomatonModel_Binding,
    Parameter,
    EventAutomatonModel_FreeParameter,
    EventAutomatonModel_FixParameter,
    EventAutomatonModel_AbstractTransition,
    EventAutomatonModel_ComplexEventProcessor,
    SymbolicParameter,
    EventAutomatonModel_SymbolicEventParameter,
    SymbolicEvent,
    EventAutomatonModel_SymbolicTimeoutEvent,
    EventAutomatonModel_SymbolicInputEvent,
    TimerAction,
    EventAutomatonModel_SetTimerAction,
    EventAutomatonModel_ResetTimerAction,
    EventAutomatonModel_SymbolicTokenParameter,
    Binding,
    EventAutomatonModel_ConstantBinding,
    EventAutomatonModel_TokenParameterBinding,
    EventAutomatonModel_SymbolicTimer,
    EventAutomatonModel_SymbolicParameter,
    EventAutomatonModel_Token,
    EventAutomatonModel_State,
    EventAutomatonModel_Automaton,
    EventAutomatonModel_Event,
    EventAutomatonModel_Action,
    AbstractTransition,
    EventAutomatonModel_EpsilonTransition,
    EventAutomatonModel_EventGuard,
    EventAutomatonModel_Transition,
    EventAutomatonModel_Parameter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eventautomatonmodel_symbolicevent_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_SymbolicEvent)


def test_eventautomatonmodel_symbolicevent_constructor_exists():
    assert callable(EventAutomatonModel_SymbolicEvent.__init__)


def test_eventautomatonmodel_symbolicevent_constructor_args():
    sig = inspect.signature(EventAutomatonModel_SymbolicEvent.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_timeraction_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_TimerAction)


def test_eventautomatonmodel_timeraction_constructor_exists():
    assert callable(EventAutomatonModel_TimerAction.__init__)


def test_eventautomatonmodel_timeraction_constructor_args():
    sig = inspect.signature(EventAutomatonModel_TimerAction.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_binding_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_Binding)


def test_eventautomatonmodel_binding_constructor_exists():
    assert callable(EventAutomatonModel_Binding.__init__)


def test_eventautomatonmodel_binding_constructor_args():
    sig = inspect.signature(EventAutomatonModel_Binding.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_freeparameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_FreeParameter)


def test_eventautomatonmodel_freeparameter_constructor_exists():
    assert callable(EventAutomatonModel_FreeParameter.__init__)


def test_eventautomatonmodel_freeparameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel_FreeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "excludedValues" in params, "Missing parameter 'excludedValues'"

def test_eventautomatonmodel_freeparameter_has_excludedValues():
    assert hasattr(EventAutomatonModel_FreeParameter, "excludedValues")
    descriptor = None
    for klass in EventAutomatonModel_FreeParameter.__mro__:
        if "excludedValues" in klass.__dict__:
            descriptor = klass.__dict__["excludedValues"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel_fixparameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_FixParameter)


def test_eventautomatonmodel_fixparameter_constructor_exists():
    assert callable(EventAutomatonModel_FixParameter.__init__)


def test_eventautomatonmodel_fixparameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel_FixParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eventautomatonmodel_fixparameter_has_value():
    assert hasattr(EventAutomatonModel_FixParameter, "value")
    descriptor = None
    for klass in EventAutomatonModel_FixParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_AbstractTransition)


def test_eventautomatonmodel_abstracttransition_constructor_exists():
    assert callable(EventAutomatonModel_AbstractTransition.__init__)


def test_eventautomatonmodel_abstracttransition_constructor_args():
    sig = inspect.signature(EventAutomatonModel_AbstractTransition.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_complexeventprocessor_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_ComplexEventProcessor)


def test_eventautomatonmodel_complexeventprocessor_constructor_exists():
    assert callable(EventAutomatonModel_ComplexEventProcessor.__init__)


def test_eventautomatonmodel_complexeventprocessor_constructor_args():
    sig = inspect.signature(EventAutomatonModel_ComplexEventProcessor.__init__)
    params = list(sig.parameters.keys())



def test_symbolicparameter_is_not_abstract():
    assert not inspect.isabstract(SymbolicParameter)


def test_symbolicparameter_constructor_exists():
    assert callable(SymbolicParameter.__init__)


def test_symbolicparameter_constructor_args():
    sig = inspect.signature(SymbolicParameter.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_symboliceventparameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_SymbolicEventParameter)


def test_eventautomatonmodel_symboliceventparameter_constructor_exists():
    assert callable(EventAutomatonModel_SymbolicEventParameter.__init__)


def test_eventautomatonmodel_symboliceventparameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel_SymbolicEventParameter.__init__)
    params = list(sig.parameters.keys())



def test_symbolicevent_is_not_abstract():
    assert not inspect.isabstract(SymbolicEvent)


def test_symbolicevent_constructor_exists():
    assert callable(SymbolicEvent.__init__)


def test_symbolicevent_constructor_args():
    sig = inspect.signature(SymbolicEvent.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_symbolictimeoutevent_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_SymbolicTimeoutEvent)


def test_eventautomatonmodel_symbolictimeoutevent_constructor_exists():
    assert callable(EventAutomatonModel_SymbolicTimeoutEvent.__init__)


def test_eventautomatonmodel_symbolictimeoutevent_constructor_args():
    sig = inspect.signature(EventAutomatonModel_SymbolicTimeoutEvent.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_symbolicinputevent_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_SymbolicInputEvent)


def test_eventautomatonmodel_symbolicinputevent_constructor_exists():
    assert callable(EventAutomatonModel_SymbolicInputEvent.__init__)


def test_eventautomatonmodel_symbolicinputevent_constructor_args():
    sig = inspect.signature(EventAutomatonModel_SymbolicInputEvent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eventautomatonmodel_symbolicinputevent_has_name():
    assert hasattr(EventAutomatonModel_SymbolicInputEvent, "name")
    descriptor = None
    for klass in EventAutomatonModel_SymbolicInputEvent.__mro__:
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



def test_eventautomatonmodel_settimeraction_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_SetTimerAction)


def test_eventautomatonmodel_settimeraction_constructor_exists():
    assert callable(EventAutomatonModel_SetTimerAction.__init__)


def test_eventautomatonmodel_settimeraction_constructor_args():
    sig = inspect.signature(EventAutomatonModel_SetTimerAction.__init__)
    params = list(sig.parameters.keys())
    assert "toValue" in params, "Missing parameter 'toValue'"

def test_eventautomatonmodel_settimeraction_has_toValue():
    assert hasattr(EventAutomatonModel_SetTimerAction, "toValue")
    descriptor = None
    for klass in EventAutomatonModel_SetTimerAction.__mro__:
        if "toValue" in klass.__dict__:
            descriptor = klass.__dict__["toValue"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel_resettimeraction_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_ResetTimerAction)


def test_eventautomatonmodel_resettimeraction_constructor_exists():
    assert callable(EventAutomatonModel_ResetTimerAction.__init__)


def test_eventautomatonmodel_resettimeraction_constructor_args():
    sig = inspect.signature(EventAutomatonModel_ResetTimerAction.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_symbolictokenparameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_SymbolicTokenParameter)


def test_eventautomatonmodel_symbolictokenparameter_constructor_exists():
    assert callable(EventAutomatonModel_SymbolicTokenParameter.__init__)


def test_eventautomatonmodel_symbolictokenparameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel_SymbolicTokenParameter.__init__)
    params = list(sig.parameters.keys())



def test_binding_is_not_abstract():
    assert not inspect.isabstract(Binding)


def test_binding_constructor_exists():
    assert callable(Binding.__init__)


def test_binding_constructor_args():
    sig = inspect.signature(Binding.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_constantbinding_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_ConstantBinding)


def test_eventautomatonmodel_constantbinding_constructor_exists():
    assert callable(EventAutomatonModel_ConstantBinding.__init__)


def test_eventautomatonmodel_constantbinding_constructor_args():
    sig = inspect.signature(EventAutomatonModel_ConstantBinding.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_tokenparameterbinding_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_TokenParameterBinding)


def test_eventautomatonmodel_tokenparameterbinding_constructor_exists():
    assert callable(EventAutomatonModel_TokenParameterBinding.__init__)


def test_eventautomatonmodel_tokenparameterbinding_constructor_args():
    sig = inspect.signature(EventAutomatonModel_TokenParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_symbolictimer_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_SymbolicTimer)


def test_eventautomatonmodel_symbolictimer_constructor_exists():
    assert callable(EventAutomatonModel_SymbolicTimer.__init__)


def test_eventautomatonmodel_symbolictimer_constructor_args():
    sig = inspect.signature(EventAutomatonModel_SymbolicTimer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eventautomatonmodel_symbolictimer_has_name():
    assert hasattr(EventAutomatonModel_SymbolicTimer, "name")
    descriptor = None
    for klass in EventAutomatonModel_SymbolicTimer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel_symbolicparameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_SymbolicParameter)


def test_eventautomatonmodel_symbolicparameter_constructor_exists():
    assert callable(EventAutomatonModel_SymbolicParameter.__init__)


def test_eventautomatonmodel_symbolicparameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel_SymbolicParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eventautomatonmodel_symbolicparameter_has_name():
    assert hasattr(EventAutomatonModel_SymbolicParameter, "name")
    descriptor = None
    for klass in EventAutomatonModel_SymbolicParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel_token_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_Token)


def test_eventautomatonmodel_token_constructor_exists():
    assert callable(EventAutomatonModel_Token.__init__)


def test_eventautomatonmodel_token_constructor_args():
    sig = inspect.signature(EventAutomatonModel_Token.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_state_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_State)


def test_eventautomatonmodel_state_constructor_exists():
    assert callable(EventAutomatonModel_State.__init__)


def test_eventautomatonmodel_state_constructor_args():
    sig = inspect.signature(EventAutomatonModel_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "acceptor" in params, "Missing parameter 'acceptor'"

def test_eventautomatonmodel_state_has_id():
    assert hasattr(EventAutomatonModel_State, "id")
    descriptor = None
    for klass in EventAutomatonModel_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_eventautomatonmodel_state_has_acceptor():
    assert hasattr(EventAutomatonModel_State, "acceptor")
    descriptor = None
    for klass in EventAutomatonModel_State.__mro__:
        if "acceptor" in klass.__dict__:
            descriptor = klass.__dict__["acceptor"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel_automaton_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_Automaton)


def test_eventautomatonmodel_automaton_constructor_exists():
    assert callable(EventAutomatonModel_Automaton.__init__)


def test_eventautomatonmodel_automaton_constructor_args():
    sig = inspect.signature(EventAutomatonModel_Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eventautomatonmodel_automaton_has_name():
    assert hasattr(EventAutomatonModel_Automaton, "name")
    descriptor = None
    for klass in EventAutomatonModel_Automaton.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eventautomatonmodel_event_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_Event)


def test_eventautomatonmodel_event_constructor_exists():
    assert callable(EventAutomatonModel_Event.__init__)


def test_eventautomatonmodel_event_constructor_args():
    sig = inspect.signature(EventAutomatonModel_Event.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_action_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_Action)


def test_eventautomatonmodel_action_constructor_exists():
    assert callable(EventAutomatonModel_Action.__init__)


def test_eventautomatonmodel_action_constructor_args():
    sig = inspect.signature(EventAutomatonModel_Action.__init__)
    params = list(sig.parameters.keys())



def test_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(AbstractTransition)


def test_abstracttransition_constructor_exists():
    assert callable(AbstractTransition.__init__)


def test_abstracttransition_constructor_args():
    sig = inspect.signature(AbstractTransition.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_epsilontransition_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_EpsilonTransition)


def test_eventautomatonmodel_epsilontransition_constructor_exists():
    assert callable(EventAutomatonModel_EpsilonTransition.__init__)


def test_eventautomatonmodel_epsilontransition_constructor_args():
    sig = inspect.signature(EventAutomatonModel_EpsilonTransition.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_eventguard_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_EventGuard)


def test_eventautomatonmodel_eventguard_constructor_exists():
    assert callable(EventAutomatonModel_EventGuard.__init__)


def test_eventautomatonmodel_eventguard_constructor_args():
    sig = inspect.signature(EventAutomatonModel_EventGuard.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_transition_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_Transition)


def test_eventautomatonmodel_transition_constructor_exists():
    assert callable(EventAutomatonModel_Transition.__init__)


def test_eventautomatonmodel_transition_constructor_args():
    sig = inspect.signature(EventAutomatonModel_Transition.__init__)
    params = list(sig.parameters.keys())



def test_eventautomatonmodel_parameter_is_not_abstract():
    assert not inspect.isabstract(EventAutomatonModel_Parameter)


def test_eventautomatonmodel_parameter_constructor_exists():
    assert callable(EventAutomatonModel_Parameter.__init__)


def test_eventautomatonmodel_parameter_constructor_args():
    sig = inspect.signature(EventAutomatonModel_Parameter.__init__)
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
EventAutomatonModel_SymbolicEvent_strategy = st.builds(
    EventAutomatonModel_SymbolicEvent,
)
Action_strategy = st.builds(
    Action,
)
EventAutomatonModel_TimerAction_strategy = st.builds(
    EventAutomatonModel_TimerAction,
)
EventAutomatonModel_Binding_strategy = st.builds(
    EventAutomatonModel_Binding,
)
Parameter_strategy = st.builds(
    Parameter,
)
EventAutomatonModel_FreeParameter_strategy = st.builds(
    EventAutomatonModel_FreeParameter,
    excludedValues=
        safe_text
)
EventAutomatonModel_FixParameter_strategy = st.builds(
    EventAutomatonModel_FixParameter,
    value=
        safe_text
)
EventAutomatonModel_AbstractTransition_strategy = st.builds(
    EventAutomatonModel_AbstractTransition,
)
EventAutomatonModel_ComplexEventProcessor_strategy = st.builds(
    EventAutomatonModel_ComplexEventProcessor,
)
SymbolicParameter_strategy = st.builds(
    SymbolicParameter,
)
EventAutomatonModel_SymbolicEventParameter_strategy = st.builds(
    EventAutomatonModel_SymbolicEventParameter,
)
SymbolicEvent_strategy = st.builds(
    SymbolicEvent,
)
EventAutomatonModel_SymbolicTimeoutEvent_strategy = st.builds(
    EventAutomatonModel_SymbolicTimeoutEvent,
)
EventAutomatonModel_SymbolicInputEvent_strategy = st.builds(
    EventAutomatonModel_SymbolicInputEvent,
    name=
        safe_text
)
TimerAction_strategy = st.builds(
    TimerAction,
)
EventAutomatonModel_SetTimerAction_strategy = st.builds(
    EventAutomatonModel_SetTimerAction,
    toValue=
        st.integers()
)
EventAutomatonModel_ResetTimerAction_strategy = st.builds(
    EventAutomatonModel_ResetTimerAction,
)
EventAutomatonModel_SymbolicTokenParameter_strategy = st.builds(
    EventAutomatonModel_SymbolicTokenParameter,
)
Binding_strategy = st.builds(
    Binding,
)
EventAutomatonModel_ConstantBinding_strategy = st.builds(
    EventAutomatonModel_ConstantBinding,
)
EventAutomatonModel_TokenParameterBinding_strategy = st.builds(
    EventAutomatonModel_TokenParameterBinding,
)
EventAutomatonModel_SymbolicTimer_strategy = st.builds(
    EventAutomatonModel_SymbolicTimer,
    name=
        safe_text
)
EventAutomatonModel_SymbolicParameter_strategy = st.builds(
    EventAutomatonModel_SymbolicParameter,
    name=
        safe_text
)
EventAutomatonModel_Token_strategy = st.builds(
    EventAutomatonModel_Token,
)
EventAutomatonModel_State_strategy = st.builds(
    EventAutomatonModel_State,
    id=
        st.integers(),
    acceptor=
        safe_text
)
EventAutomatonModel_Automaton_strategy = st.builds(
    EventAutomatonModel_Automaton,
    name=
        safe_text
)
EventAutomatonModel_Event_strategy = st.builds(
    EventAutomatonModel_Event,
)
EventAutomatonModel_Action_strategy = st.builds(
    EventAutomatonModel_Action,
)
AbstractTransition_strategy = st.builds(
    AbstractTransition,
)
EventAutomatonModel_EpsilonTransition_strategy = st.builds(
    EventAutomatonModel_EpsilonTransition,
)
EventAutomatonModel_EventGuard_strategy = st.builds(
    EventAutomatonModel_EventGuard,
)
EventAutomatonModel_Transition_strategy = st.builds(
    EventAutomatonModel_Transition,
)
EventAutomatonModel_Parameter_strategy = st.builds(
    EventAutomatonModel_Parameter,
)

@given(instance=EventAutomatonModel_SymbolicEvent_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_symbolicevent_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_SymbolicEvent)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=EventAutomatonModel_TimerAction_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_timeraction_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_TimerAction)

@given(instance=EventAutomatonModel_Binding_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_binding_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_Binding)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=EventAutomatonModel_FreeParameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_freeparameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_FreeParameter)



@given(instance=EventAutomatonModel_FreeParameter_strategy)
def test_eventautomatonmodel_freeparameter_excludedValues_setter(instance):
    original = instance.excludedValues
    instance.excludedValues = original
    assert instance.excludedValues == original

@given(instance=EventAutomatonModel_FixParameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_fixparameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_FixParameter)



@given(instance=EventAutomatonModel_FixParameter_strategy)
def test_eventautomatonmodel_fixparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=EventAutomatonModel_AbstractTransition_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_abstracttransition_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_AbstractTransition)

@given(instance=EventAutomatonModel_ComplexEventProcessor_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_complexeventprocessor_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_ComplexEventProcessor)

@given(instance=SymbolicParameter_strategy)
@settings(max_examples=50)
def test_symbolicparameter_instantiation(instance):
    assert isinstance(instance, SymbolicParameter)

@given(instance=EventAutomatonModel_SymbolicEventParameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_symboliceventparameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_SymbolicEventParameter)

@given(instance=SymbolicEvent_strategy)
@settings(max_examples=50)
def test_symbolicevent_instantiation(instance):
    assert isinstance(instance, SymbolicEvent)

@given(instance=EventAutomatonModel_SymbolicTimeoutEvent_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_symbolictimeoutevent_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_SymbolicTimeoutEvent)

@given(instance=EventAutomatonModel_SymbolicInputEvent_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_symbolicinputevent_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_SymbolicInputEvent)



@given(instance=EventAutomatonModel_SymbolicInputEvent_strategy)
def test_eventautomatonmodel_symbolicinputevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TimerAction_strategy)
@settings(max_examples=50)
def test_timeraction_instantiation(instance):
    assert isinstance(instance, TimerAction)

@given(instance=EventAutomatonModel_SetTimerAction_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_settimeraction_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_SetTimerAction)



@given(instance=EventAutomatonModel_SetTimerAction_strategy)
def test_eventautomatonmodel_settimeraction_toValue_setter(instance):
    original = instance.toValue
    instance.toValue = original
    assert instance.toValue == original

@given(instance=EventAutomatonModel_ResetTimerAction_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_resettimeraction_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_ResetTimerAction)

@given(instance=EventAutomatonModel_SymbolicTokenParameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_symbolictokenparameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_SymbolicTokenParameter)

@given(instance=Binding_strategy)
@settings(max_examples=50)
def test_binding_instantiation(instance):
    assert isinstance(instance, Binding)

@given(instance=EventAutomatonModel_ConstantBinding_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_constantbinding_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_ConstantBinding)

@given(instance=EventAutomatonModel_TokenParameterBinding_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_tokenparameterbinding_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_TokenParameterBinding)

@given(instance=EventAutomatonModel_SymbolicTimer_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_symbolictimer_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_SymbolicTimer)



@given(instance=EventAutomatonModel_SymbolicTimer_strategy)
def test_eventautomatonmodel_symbolictimer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EventAutomatonModel_SymbolicParameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_symbolicparameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_SymbolicParameter)



@given(instance=EventAutomatonModel_SymbolicParameter_strategy)
def test_eventautomatonmodel_symbolicparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EventAutomatonModel_Token_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_token_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_Token)

@given(instance=EventAutomatonModel_State_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_state_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_State)



@given(instance=EventAutomatonModel_State_strategy)
def test_eventautomatonmodel_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=EventAutomatonModel_State_strategy)
def test_eventautomatonmodel_state_acceptor_setter(instance):
    original = instance.acceptor
    instance.acceptor = original
    assert instance.acceptor == original

@given(instance=EventAutomatonModel_Automaton_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_automaton_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_Automaton)



@given(instance=EventAutomatonModel_Automaton_strategy)
def test_eventautomatonmodel_automaton_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EventAutomatonModel_Event_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_event_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_Event)

@given(instance=EventAutomatonModel_Action_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_action_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_Action)

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=EventAutomatonModel_EpsilonTransition_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_epsilontransition_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_EpsilonTransition)

@given(instance=EventAutomatonModel_EventGuard_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_eventguard_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_EventGuard)

@given(instance=EventAutomatonModel_Transition_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_transition_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_Transition)

@given(instance=EventAutomatonModel_Parameter_strategy)
@settings(max_examples=50)
def test_eventautomatonmodel_parameter_instantiation(instance):
    assert isinstance(instance, EventAutomatonModel_Parameter)

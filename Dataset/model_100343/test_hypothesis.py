import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TimedZone,
    automaton_HoldsFor,
    automaton_Within,
    automaton_ParameterBinding,
    automaton_EventPattern,
    TypedTransition,
    automaton_NegativeTransition,
    automaton_Parameter,
    State,
    automaton_Guard,
    Transition,
    automaton_EpsilonTransition,
    automaton_TypedTransition,
    automaton_Transition,
    automaton_ParameterTable,
    automaton_TimedZone,
    automaton_State,
    automaton_TrapState,
    automaton_FinalState,
    automaton_InitState,
    automaton_Automaton,
    automaton_InternalModel,
    automaton_EventToken,
    automaton_Event,
    EventContext,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_timedzone_is_not_abstract():
    assert not inspect.isabstract(TimedZone)


def test_timedzone_constructor_exists():
    assert callable(TimedZone.__init__)


def test_timedzone_constructor_args():
    sig = inspect.signature(TimedZone.__init__)
    params = list(sig.parameters.keys())



def test_automaton_holdsfor_is_not_abstract():
    assert not inspect.isabstract(automaton_HoldsFor)


def test_automaton_holdsfor_constructor_exists():
    assert callable(automaton_HoldsFor.__init__)


def test_automaton_holdsfor_constructor_args():
    sig = inspect.signature(automaton_HoldsFor.__init__)
    params = list(sig.parameters.keys())



def test_automaton_within_is_not_abstract():
    assert not inspect.isabstract(automaton_Within)


def test_automaton_within_constructor_exists():
    assert callable(automaton_Within.__init__)


def test_automaton_within_constructor_args():
    sig = inspect.signature(automaton_Within.__init__)
    params = list(sig.parameters.keys())



def test_automaton_parameterbinding_is_not_abstract():
    assert not inspect.isabstract(automaton_ParameterBinding)


def test_automaton_parameterbinding_constructor_exists():
    assert callable(automaton_ParameterBinding.__init__)


def test_automaton_parameterbinding_constructor_args():
    sig = inspect.signature(automaton_ParameterBinding.__init__)
    params = list(sig.parameters.keys())
    assert "symbolicName" in params, "Missing parameter 'symbolicName'"
    assert "value" in params, "Missing parameter 'value'"

def test_automaton_parameterbinding_has_symbolicName():
    assert hasattr(automaton_ParameterBinding, "symbolicName")
    descriptor = None
    for klass in automaton_ParameterBinding.__mro__:
        if "symbolicName" in klass.__dict__:
            descriptor = klass.__dict__["symbolicName"]
            break
    assert isinstance(descriptor, property)

def test_automaton_parameterbinding_has_value():
    assert hasattr(automaton_ParameterBinding, "value")
    descriptor = None
    for klass in automaton_ParameterBinding.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_automaton_eventpattern_is_not_abstract():
    assert not inspect.isabstract(automaton_EventPattern)


def test_automaton_eventpattern_constructor_exists():
    assert callable(automaton_EventPattern.__init__)


def test_automaton_eventpattern_constructor_args():
    sig = inspect.signature(automaton_EventPattern.__init__)
    params = list(sig.parameters.keys())



def test_typedtransition_is_not_abstract():
    assert not inspect.isabstract(TypedTransition)


def test_typedtransition_constructor_exists():
    assert callable(TypedTransition.__init__)


def test_typedtransition_constructor_args():
    sig = inspect.signature(TypedTransition.__init__)
    params = list(sig.parameters.keys())



def test_automaton_negativetransition_is_not_abstract():
    assert not inspect.isabstract(automaton_NegativeTransition)


def test_automaton_negativetransition_constructor_exists():
    assert callable(automaton_NegativeTransition.__init__)


def test_automaton_negativetransition_constructor_args():
    sig = inspect.signature(automaton_NegativeTransition.__init__)
    params = list(sig.parameters.keys())



def test_automaton_parameter_is_not_abstract():
    assert not inspect.isabstract(automaton_Parameter)


def test_automaton_parameter_constructor_exists():
    assert callable(automaton_Parameter.__init__)


def test_automaton_parameter_constructor_args():
    sig = inspect.signature(automaton_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "symbolicName" in params, "Missing parameter 'symbolicName'"

def test_automaton_parameter_has_position():
    assert hasattr(automaton_Parameter, "position")
    descriptor = None
    for klass in automaton_Parameter.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_automaton_parameter_has_symbolicName():
    assert hasattr(automaton_Parameter, "symbolicName")
    descriptor = None
    for klass in automaton_Parameter.__mro__:
        if "symbolicName" in klass.__dict__:
            descriptor = klass.__dict__["symbolicName"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_automaton_guard_is_not_abstract():
    assert not inspect.isabstract(automaton_Guard)


def test_automaton_guard_constructor_exists():
    assert callable(automaton_Guard.__init__)


def test_automaton_guard_constructor_args():
    sig = inspect.signature(automaton_Guard.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_automaton_epsilontransition_is_not_abstract():
    assert not inspect.isabstract(automaton_EpsilonTransition)


def test_automaton_epsilontransition_constructor_exists():
    assert callable(automaton_EpsilonTransition.__init__)


def test_automaton_epsilontransition_constructor_args():
    sig = inspect.signature(automaton_EpsilonTransition.__init__)
    params = list(sig.parameters.keys())



def test_automaton_typedtransition_is_not_abstract():
    assert not inspect.isabstract(automaton_TypedTransition)


def test_automaton_typedtransition_constructor_exists():
    assert callable(automaton_TypedTransition.__init__)


def test_automaton_typedtransition_constructor_args():
    sig = inspect.signature(automaton_TypedTransition.__init__)
    params = list(sig.parameters.keys())



def test_automaton_transition_is_not_abstract():
    assert not inspect.isabstract(automaton_Transition)


def test_automaton_transition_constructor_exists():
    assert callable(automaton_Transition.__init__)


def test_automaton_transition_constructor_args():
    sig = inspect.signature(automaton_Transition.__init__)
    params = list(sig.parameters.keys())



def test_automaton_parametertable_is_not_abstract():
    assert not inspect.isabstract(automaton_ParameterTable)


def test_automaton_parametertable_constructor_exists():
    assert callable(automaton_ParameterTable.__init__)


def test_automaton_parametertable_constructor_args():
    sig = inspect.signature(automaton_ParameterTable.__init__)
    params = list(sig.parameters.keys())



def test_automaton_timedzone_is_not_abstract():
    assert not inspect.isabstract(automaton_TimedZone)


def test_automaton_timedzone_constructor_exists():
    assert callable(automaton_TimedZone.__init__)


def test_automaton_timedzone_constructor_args():
    sig = inspect.signature(automaton_TimedZone.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_automaton_timedzone_has_time():
    assert hasattr(automaton_TimedZone, "time")
    descriptor = None
    for klass in automaton_TimedZone.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_automaton_state_is_not_abstract():
    assert not inspect.isabstract(automaton_State)


def test_automaton_state_constructor_exists():
    assert callable(automaton_State.__init__)


def test_automaton_state_constructor_args():
    sig = inspect.signature(automaton_State.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_automaton_state_has_label():
    assert hasattr(automaton_State, "label")
    descriptor = None
    for klass in automaton_State.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_automaton_trapstate_is_not_abstract():
    assert not inspect.isabstract(automaton_TrapState)


def test_automaton_trapstate_constructor_exists():
    assert callable(automaton_TrapState.__init__)


def test_automaton_trapstate_constructor_args():
    sig = inspect.signature(automaton_TrapState.__init__)
    params = list(sig.parameters.keys())



def test_automaton_finalstate_is_not_abstract():
    assert not inspect.isabstract(automaton_FinalState)


def test_automaton_finalstate_constructor_exists():
    assert callable(automaton_FinalState.__init__)


def test_automaton_finalstate_constructor_args():
    sig = inspect.signature(automaton_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_automaton_initstate_is_not_abstract():
    assert not inspect.isabstract(automaton_InitState)


def test_automaton_initstate_constructor_exists():
    assert callable(automaton_InitState.__init__)


def test_automaton_initstate_constructor_args():
    sig = inspect.signature(automaton_InitState.__init__)
    params = list(sig.parameters.keys())



def test_automaton_automaton_is_not_abstract():
    assert not inspect.isabstract(automaton_Automaton)


def test_automaton_automaton_constructor_exists():
    assert callable(automaton_Automaton.__init__)


def test_automaton_automaton_constructor_args():
    sig = inspect.signature(automaton_Automaton.__init__)
    params = list(sig.parameters.keys())
    assert "eventPatternId" in params, "Missing parameter 'eventPatternId'"

def test_automaton_automaton_has_eventPatternId():
    assert hasattr(automaton_Automaton, "eventPatternId")
    descriptor = None
    for klass in automaton_Automaton.__mro__:
        if "eventPatternId" in klass.__dict__:
            descriptor = klass.__dict__["eventPatternId"]
            break
    assert isinstance(descriptor, property)



def test_automaton_internalmodel_is_not_abstract():
    assert not inspect.isabstract(automaton_InternalModel)


def test_automaton_internalmodel_constructor_exists():
    assert callable(automaton_InternalModel.__init__)


def test_automaton_internalmodel_constructor_args():
    sig = inspect.signature(automaton_InternalModel.__init__)
    params = list(sig.parameters.keys())



def test_automaton_eventtoken_is_not_abstract():
    assert not inspect.isabstract(automaton_EventToken)


def test_automaton_eventtoken_constructor_exists():
    assert callable(automaton_EventToken.__init__)


def test_automaton_eventtoken_constructor_args():
    sig = inspect.signature(automaton_EventToken.__init__)
    params = list(sig.parameters.keys())



def test_automaton_event_is_not_abstract():
    assert not inspect.isabstract(automaton_Event)


def test_automaton_event_constructor_exists():
    assert callable(automaton_Event.__init__)


def test_automaton_event_constructor_args():
    sig = inspect.signature(automaton_Event.__init__)
    params = list(sig.parameters.keys())

def test_eventcontext_exists():
    # Check that the Enumeration exists
    assert EventContext is not None

def test_eventcontext_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventContext]
    expected_literals = [
        "NOT_SET",
        "RECENT",
        "STRICT_IMMEDIATE",
        "IMMEDIATE",
        "UNRESTRICTED",
        "CHRONICLE",
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
TimedZone_strategy = st.builds(
    TimedZone,
)
automaton_HoldsFor_strategy = st.builds(
    automaton_HoldsFor,
)
automaton_Within_strategy = st.builds(
    automaton_Within,
)
automaton_ParameterBinding_strategy = st.builds(
    automaton_ParameterBinding,
    symbolicName=
        safe_text,
    value=
        safe_text
)
automaton_EventPattern_strategy = st.builds(
    automaton_EventPattern,
)
TypedTransition_strategy = st.builds(
    TypedTransition,
)
automaton_NegativeTransition_strategy = st.builds(
    automaton_NegativeTransition,
)
automaton_Parameter_strategy = st.builds(
    automaton_Parameter,
    position=
        st.integers(),
    symbolicName=
        safe_text
)
State_strategy = st.builds(
    State,
)
automaton_Guard_strategy = st.builds(
    automaton_Guard,
)
Transition_strategy = st.builds(
    Transition,
)
automaton_EpsilonTransition_strategy = st.builds(
    automaton_EpsilonTransition,
)
automaton_TypedTransition_strategy = st.builds(
    automaton_TypedTransition,
)
automaton_Transition_strategy = st.builds(
    automaton_Transition,
)
automaton_ParameterTable_strategy = st.builds(
    automaton_ParameterTable,
)
automaton_TimedZone_strategy = st.builds(
    automaton_TimedZone,
    time=
        safe_text
)
automaton_State_strategy = st.builds(
    automaton_State,
    label=
        safe_text
)
automaton_TrapState_strategy = st.builds(
    automaton_TrapState,
)
automaton_FinalState_strategy = st.builds(
    automaton_FinalState,
)
automaton_InitState_strategy = st.builds(
    automaton_InitState,
)
automaton_Automaton_strategy = st.builds(
    automaton_Automaton,
    eventPatternId=
        safe_text
)
automaton_InternalModel_strategy = st.builds(
    automaton_InternalModel,
)
automaton_EventToken_strategy = st.builds(
    automaton_EventToken,
)
automaton_Event_strategy = st.builds(
    automaton_Event,
)

@given(instance=TimedZone_strategy)
@settings(max_examples=50)
def test_timedzone_instantiation(instance):
    assert isinstance(instance, TimedZone)

@given(instance=automaton_HoldsFor_strategy)
@settings(max_examples=50)
def test_automaton_holdsfor_instantiation(instance):
    assert isinstance(instance, automaton_HoldsFor)

@given(instance=automaton_Within_strategy)
@settings(max_examples=50)
def test_automaton_within_instantiation(instance):
    assert isinstance(instance, automaton_Within)

@given(instance=automaton_ParameterBinding_strategy)
@settings(max_examples=50)
def test_automaton_parameterbinding_instantiation(instance):
    assert isinstance(instance, automaton_ParameterBinding)



@given(instance=automaton_ParameterBinding_strategy)
def test_automaton_parameterbinding_symbolicName_setter(instance):
    original = instance.symbolicName
    instance.symbolicName = original
    assert instance.symbolicName == original



@given(instance=automaton_ParameterBinding_strategy)
def test_automaton_parameterbinding_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=automaton_EventPattern_strategy)
@settings(max_examples=50)
def test_automaton_eventpattern_instantiation(instance):
    assert isinstance(instance, automaton_EventPattern)

@given(instance=TypedTransition_strategy)
@settings(max_examples=50)
def test_typedtransition_instantiation(instance):
    assert isinstance(instance, TypedTransition)

@given(instance=automaton_NegativeTransition_strategy)
@settings(max_examples=50)
def test_automaton_negativetransition_instantiation(instance):
    assert isinstance(instance, automaton_NegativeTransition)

@given(instance=automaton_Parameter_strategy)
@settings(max_examples=50)
def test_automaton_parameter_instantiation(instance):
    assert isinstance(instance, automaton_Parameter)



@given(instance=automaton_Parameter_strategy)
def test_automaton_parameter_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=automaton_Parameter_strategy)
def test_automaton_parameter_symbolicName_setter(instance):
    original = instance.symbolicName
    instance.symbolicName = original
    assert instance.symbolicName == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=automaton_Guard_strategy)
@settings(max_examples=50)
def test_automaton_guard_instantiation(instance):
    assert isinstance(instance, automaton_Guard)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=automaton_EpsilonTransition_strategy)
@settings(max_examples=50)
def test_automaton_epsilontransition_instantiation(instance):
    assert isinstance(instance, automaton_EpsilonTransition)

@given(instance=automaton_TypedTransition_strategy)
@settings(max_examples=50)
def test_automaton_typedtransition_instantiation(instance):
    assert isinstance(instance, automaton_TypedTransition)

@given(instance=automaton_Transition_strategy)
@settings(max_examples=50)
def test_automaton_transition_instantiation(instance):
    assert isinstance(instance, automaton_Transition)

@given(instance=automaton_ParameterTable_strategy)
@settings(max_examples=50)
def test_automaton_parametertable_instantiation(instance):
    assert isinstance(instance, automaton_ParameterTable)

@given(instance=automaton_TimedZone_strategy)
@settings(max_examples=50)
def test_automaton_timedzone_instantiation(instance):
    assert isinstance(instance, automaton_TimedZone)



@given(instance=automaton_TimedZone_strategy)
def test_automaton_timedzone_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=automaton_State_strategy)
@settings(max_examples=50)
def test_automaton_state_instantiation(instance):
    assert isinstance(instance, automaton_State)



@given(instance=automaton_State_strategy)
def test_automaton_state_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=automaton_TrapState_strategy)
@settings(max_examples=50)
def test_automaton_trapstate_instantiation(instance):
    assert isinstance(instance, automaton_TrapState)

@given(instance=automaton_FinalState_strategy)
@settings(max_examples=50)
def test_automaton_finalstate_instantiation(instance):
    assert isinstance(instance, automaton_FinalState)

@given(instance=automaton_InitState_strategy)
@settings(max_examples=50)
def test_automaton_initstate_instantiation(instance):
    assert isinstance(instance, automaton_InitState)

@given(instance=automaton_Automaton_strategy)
@settings(max_examples=50)
def test_automaton_automaton_instantiation(instance):
    assert isinstance(instance, automaton_Automaton)



@given(instance=automaton_Automaton_strategy)
def test_automaton_automaton_eventPatternId_setter(instance):
    original = instance.eventPatternId
    instance.eventPatternId = original
    assert instance.eventPatternId == original

@given(instance=automaton_InternalModel_strategy)
@settings(max_examples=50)
def test_automaton_internalmodel_instantiation(instance):
    assert isinstance(instance, automaton_InternalModel)

@given(instance=automaton_EventToken_strategy)
@settings(max_examples=50)
def test_automaton_eventtoken_instantiation(instance):
    assert isinstance(instance, automaton_EventToken)

@given(instance=automaton_Event_strategy)
@settings(max_examples=50)
def test_automaton_event_instantiation(instance):
    assert isinstance(instance, automaton_Event)

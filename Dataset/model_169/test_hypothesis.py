import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Events_trace_Net,
    Transition_fireExitEventOccurrence,
    Transition_fireEntryEventOccurrence,
    Transition_isEnabledExitEventOccurrence,
    Transition_isEnabledEntryEventOccurrence,
    Place_removeTokenExitEventOccurrence,
    Place_removeTokenEntryEventOccurrence,
    Place_addTokenExitEventOccurrence,
    Place_addTokenEntryEventOccurrence,
    Net_runExitEventOccurrence,
    Net_runEntryEventOccurrence,
    Net_mainExitEventOccurrence,
    Net_mainEntryEventOccurrence,
    trace_Events_Events,
    Events_trace_GlobalState,
    trace_Events_EventOccurrence,
    trace_Net,
    trace_Transition,
    Place_tokens_State,
    EventOccurrence,
    trace_Events_Net_mainEntryEventOccurrence,
    trace_StaticObjectsPools,
    TracedObjects,
    petrinet_trace_Place,
    trace_petrinet_TracedPlace,
    trace_Traced_TracedObjects,
    States_trace_GlobalState,
    trace_States_Place_tokens_State,
    trace_Events_Transition_fireExitEventOccurrence,
    trace_Events_Transition_fireEntryEventOccurrence,
    Events_trace_EObject,
    trace_Events_Transition_isEnabledExitEventOccurrence,
    Events_trace_Transition,
    trace_Events_Transition_isEnabledEntryEventOccurrence,
    trace_Events_Place_removeTokenExitEventOccurrence,
    trace_Events_Place_removeTokenEntryEventOccurrence,
    trace_Events_Place_addTokenExitEventOccurrence,
    petrinet_TracedPlace,
    trace_Events_Place_addTokenEntryEventOccurrence,
    trace_Events_Net_runExitEventOccurrence,
    trace_Events_Net_runEntryEventOccurrence,
    trace_Events_Net_mainExitEventOccurrence,
    Events,
    trace_GlobalState,
    trace_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_events_trace_net_is_not_abstract():
    assert not inspect.isabstract(Events_trace_Net)


def test_events_trace_net_constructor_exists():
    assert callable(Events_trace_Net.__init__)


def test_events_trace_net_constructor_args():
    sig = inspect.signature(Events_trace_Net.__init__)
    params = list(sig.parameters.keys())



def test_transition_fireexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Transition_fireExitEventOccurrence)


def test_transition_fireexiteventoccurrence_constructor_exists():
    assert callable(Transition_fireExitEventOccurrence.__init__)


def test_transition_fireexiteventoccurrence_constructor_args():
    sig = inspect.signature(Transition_fireExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_transition_fireentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Transition_fireEntryEventOccurrence)


def test_transition_fireentryeventoccurrence_constructor_exists():
    assert callable(Transition_fireEntryEventOccurrence.__init__)


def test_transition_fireentryeventoccurrence_constructor_args():
    sig = inspect.signature(Transition_fireEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_transition_isenabledexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Transition_isEnabledExitEventOccurrence)


def test_transition_isenabledexiteventoccurrence_constructor_exists():
    assert callable(Transition_isEnabledExitEventOccurrence.__init__)


def test_transition_isenabledexiteventoccurrence_constructor_args():
    sig = inspect.signature(Transition_isEnabledExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_transition_isenabledentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Transition_isEnabledEntryEventOccurrence)


def test_transition_isenabledentryeventoccurrence_constructor_exists():
    assert callable(Transition_isEnabledEntryEventOccurrence.__init__)


def test_transition_isenabledentryeventoccurrence_constructor_args():
    sig = inspect.signature(Transition_isEnabledEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_place_removetokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Place_removeTokenExitEventOccurrence)


def test_place_removetokenexiteventoccurrence_constructor_exists():
    assert callable(Place_removeTokenExitEventOccurrence.__init__)


def test_place_removetokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(Place_removeTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_place_removetokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Place_removeTokenEntryEventOccurrence)


def test_place_removetokenentryeventoccurrence_constructor_exists():
    assert callable(Place_removeTokenEntryEventOccurrence.__init__)


def test_place_removetokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(Place_removeTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_place_addtokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Place_addTokenExitEventOccurrence)


def test_place_addtokenexiteventoccurrence_constructor_exists():
    assert callable(Place_addTokenExitEventOccurrence.__init__)


def test_place_addtokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(Place_addTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_place_addtokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Place_addTokenEntryEventOccurrence)


def test_place_addtokenentryeventoccurrence_constructor_exists():
    assert callable(Place_addTokenEntryEventOccurrence.__init__)


def test_place_addtokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(Place_addTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_net_runexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Net_runExitEventOccurrence)


def test_net_runexiteventoccurrence_constructor_exists():
    assert callable(Net_runExitEventOccurrence.__init__)


def test_net_runexiteventoccurrence_constructor_args():
    sig = inspect.signature(Net_runExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_net_runentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Net_runEntryEventOccurrence)


def test_net_runentryeventoccurrence_constructor_exists():
    assert callable(Net_runEntryEventOccurrence.__init__)


def test_net_runentryeventoccurrence_constructor_args():
    sig = inspect.signature(Net_runEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_net_mainexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Net_mainExitEventOccurrence)


def test_net_mainexiteventoccurrence_constructor_exists():
    assert callable(Net_mainExitEventOccurrence.__init__)


def test_net_mainexiteventoccurrence_constructor_args():
    sig = inspect.signature(Net_mainExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_net_mainentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Net_mainEntryEventOccurrence)


def test_net_mainentryeventoccurrence_constructor_exists():
    assert callable(Net_mainEntryEventOccurrence.__init__)


def test_net_mainentryeventoccurrence_constructor_args():
    sig = inspect.signature(Net_mainEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_events_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Events)


def test_trace_events_events_constructor_exists():
    assert callable(trace_Events_Events.__init__)


def test_trace_events_events_constructor_args():
    sig = inspect.signature(trace_Events_Events.__init__)
    params = list(sig.parameters.keys())



def test_events_trace_globalstate_is_not_abstract():
    assert not inspect.isabstract(Events_trace_GlobalState)


def test_events_trace_globalstate_constructor_exists():
    assert callable(Events_trace_GlobalState.__init__)


def test_events_trace_globalstate_constructor_args():
    sig = inspect.signature(Events_trace_GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_EventOccurrence)


def test_trace_events_eventoccurrence_constructor_exists():
    assert callable(trace_Events_EventOccurrence.__init__)


def test_trace_events_eventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_net_is_not_abstract():
    assert not inspect.isabstract(trace_Net)


def test_trace_net_constructor_exists():
    assert callable(trace_Net.__init__)


def test_trace_net_constructor_args():
    sig = inspect.signature(trace_Net.__init__)
    params = list(sig.parameters.keys())



def test_trace_transition_is_not_abstract():
    assert not inspect.isabstract(trace_Transition)


def test_trace_transition_constructor_exists():
    assert callable(trace_Transition.__init__)


def test_trace_transition_constructor_args():
    sig = inspect.signature(trace_Transition.__init__)
    params = list(sig.parameters.keys())



def test_place_tokens_state_is_not_abstract():
    assert not inspect.isabstract(Place_tokens_State)


def test_place_tokens_state_constructor_exists():
    assert callable(Place_tokens_State.__init__)


def test_place_tokens_state_constructor_args():
    sig = inspect.signature(Place_tokens_State.__init__)
    params = list(sig.parameters.keys())



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_net_mainentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Net_mainEntryEventOccurrence)


def test_trace_events_net_mainentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Net_mainEntryEventOccurrence.__init__)


def test_trace_events_net_mainentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Net_mainEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_staticobjectspools_is_not_abstract():
    assert not inspect.isabstract(trace_StaticObjectsPools)


def test_trace_staticobjectspools_constructor_exists():
    assert callable(trace_StaticObjectsPools.__init__)


def test_trace_staticobjectspools_constructor_args():
    sig = inspect.signature(trace_StaticObjectsPools.__init__)
    params = list(sig.parameters.keys())



def test_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(TracedObjects)


def test_tracedobjects_constructor_exists():
    assert callable(TracedObjects.__init__)


def test_tracedobjects_constructor_args():
    sig = inspect.signature(TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_trace_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_trace_Place)


def test_petrinet_trace_place_constructor_exists():
    assert callable(petrinet_trace_Place.__init__)


def test_petrinet_trace_place_constructor_args():
    sig = inspect.signature(petrinet_trace_Place.__init__)
    params = list(sig.parameters.keys())



def test_trace_petrinet_tracedplace_is_not_abstract():
    assert not inspect.isabstract(trace_petrinet_TracedPlace)


def test_trace_petrinet_tracedplace_constructor_exists():
    assert callable(trace_petrinet_TracedPlace.__init__)


def test_trace_petrinet_tracedplace_constructor_args():
    sig = inspect.signature(trace_petrinet_TracedPlace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"

def test_trace_petrinet_tracedplace_has_name():
    assert hasattr(trace_petrinet_TracedPlace, "name")
    descriptor = None
    for klass in trace_petrinet_TracedPlace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_trace_petrinet_tracedplace_has_initialTokens():
    assert hasattr(trace_petrinet_TracedPlace, "initialTokens")
    descriptor = None
    for klass in trace_petrinet_TracedPlace.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)



def test_trace_traced_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(trace_Traced_TracedObjects)


def test_trace_traced_tracedobjects_constructor_exists():
    assert callable(trace_Traced_TracedObjects.__init__)


def test_trace_traced_tracedobjects_constructor_args():
    sig = inspect.signature(trace_Traced_TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_states_trace_globalstate_is_not_abstract():
    assert not inspect.isabstract(States_trace_GlobalState)


def test_states_trace_globalstate_constructor_exists():
    assert callable(States_trace_GlobalState.__init__)


def test_states_trace_globalstate_constructor_args():
    sig = inspect.signature(States_trace_GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_place_tokens_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_Place_tokens_State)


def test_trace_states_place_tokens_state_constructor_exists():
    assert callable(trace_States_Place_tokens_State.__init__)


def test_trace_states_place_tokens_state_constructor_args():
    sig = inspect.signature(trace_States_Place_tokens_State.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_trace_states_place_tokens_state_has_tokens():
    assert hasattr(trace_States_Place_tokens_State, "tokens")
    descriptor = None
    for klass in trace_States_Place_tokens_State.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_trace_events_transition_fireexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Transition_fireExitEventOccurrence)


def test_trace_events_transition_fireexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Transition_fireExitEventOccurrence.__init__)


def test_trace_events_transition_fireexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Transition_fireExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_transition_fireentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Transition_fireEntryEventOccurrence)


def test_trace_events_transition_fireentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Transition_fireEntryEventOccurrence.__init__)


def test_trace_events_transition_fireentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Transition_fireEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_events_trace_eobject_is_not_abstract():
    assert not inspect.isabstract(Events_trace_EObject)


def test_events_trace_eobject_constructor_exists():
    assert callable(Events_trace_EObject.__init__)


def test_events_trace_eobject_constructor_args():
    sig = inspect.signature(Events_trace_EObject.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_transition_isenabledexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Transition_isEnabledExitEventOccurrence)


def test_trace_events_transition_isenabledexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Transition_isEnabledExitEventOccurrence.__init__)


def test_trace_events_transition_isenabledexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Transition_isEnabledExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_events_trace_transition_is_not_abstract():
    assert not inspect.isabstract(Events_trace_Transition)


def test_events_trace_transition_constructor_exists():
    assert callable(Events_trace_Transition.__init__)


def test_events_trace_transition_constructor_args():
    sig = inspect.signature(Events_trace_Transition.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_transition_isenabledentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Transition_isEnabledEntryEventOccurrence)


def test_trace_events_transition_isenabledentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Transition_isEnabledEntryEventOccurrence.__init__)


def test_trace_events_transition_isenabledentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Transition_isEnabledEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_place_removetokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Place_removeTokenExitEventOccurrence)


def test_trace_events_place_removetokenexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Place_removeTokenExitEventOccurrence.__init__)


def test_trace_events_place_removetokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Place_removeTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_place_removetokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Place_removeTokenEntryEventOccurrence)


def test_trace_events_place_removetokenentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Place_removeTokenEntryEventOccurrence.__init__)


def test_trace_events_place_removetokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Place_removeTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_place_addtokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Place_addTokenExitEventOccurrence)


def test_trace_events_place_addtokenexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Place_addTokenExitEventOccurrence.__init__)


def test_trace_events_place_addtokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Place_addTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_tracedplace_is_not_abstract():
    assert not inspect.isabstract(petrinet_TracedPlace)


def test_petrinet_tracedplace_constructor_exists():
    assert callable(petrinet_TracedPlace.__init__)


def test_petrinet_tracedplace_constructor_args():
    sig = inspect.signature(petrinet_TracedPlace.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_place_addtokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Place_addTokenEntryEventOccurrence)


def test_trace_events_place_addtokenentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Place_addTokenEntryEventOccurrence.__init__)


def test_trace_events_place_addtokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Place_addTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_net_runexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Net_runExitEventOccurrence)


def test_trace_events_net_runexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Net_runExitEventOccurrence.__init__)


def test_trace_events_net_runexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Net_runExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_net_runentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Net_runEntryEventOccurrence)


def test_trace_events_net_runentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Net_runEntryEventOccurrence.__init__)


def test_trace_events_net_runentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Net_runEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_net_mainexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Net_mainExitEventOccurrence)


def test_trace_events_net_mainexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Net_mainExitEventOccurrence.__init__)


def test_trace_events_net_mainexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Net_mainExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_events_is_not_abstract():
    assert not inspect.isabstract(Events)


def test_events_constructor_exists():
    assert callable(Events.__init__)


def test_events_constructor_args():
    sig = inspect.signature(Events.__init__)
    params = list(sig.parameters.keys())



def test_trace_globalstate_is_not_abstract():
    assert not inspect.isabstract(trace_GlobalState)


def test_trace_globalstate_constructor_exists():
    assert callable(trace_GlobalState.__init__)


def test_trace_globalstate_constructor_args():
    sig = inspect.signature(trace_GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_trace_trace_is_not_abstract():
    assert not inspect.isabstract(trace_Trace)


def test_trace_trace_constructor_exists():
    assert callable(trace_Trace.__init__)


def test_trace_trace_constructor_args():
    sig = inspect.signature(trace_Trace.__init__)
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
Events_trace_Net_strategy = st.builds(
    Events_trace_Net,
)
Transition_fireExitEventOccurrence_strategy = st.builds(
    Transition_fireExitEventOccurrence,
)
Transition_fireEntryEventOccurrence_strategy = st.builds(
    Transition_fireEntryEventOccurrence,
)
Transition_isEnabledExitEventOccurrence_strategy = st.builds(
    Transition_isEnabledExitEventOccurrence,
)
Transition_isEnabledEntryEventOccurrence_strategy = st.builds(
    Transition_isEnabledEntryEventOccurrence,
)
Place_removeTokenExitEventOccurrence_strategy = st.builds(
    Place_removeTokenExitEventOccurrence,
)
Place_removeTokenEntryEventOccurrence_strategy = st.builds(
    Place_removeTokenEntryEventOccurrence,
)
Place_addTokenExitEventOccurrence_strategy = st.builds(
    Place_addTokenExitEventOccurrence,
)
Place_addTokenEntryEventOccurrence_strategy = st.builds(
    Place_addTokenEntryEventOccurrence,
)
Net_runExitEventOccurrence_strategy = st.builds(
    Net_runExitEventOccurrence,
)
Net_runEntryEventOccurrence_strategy = st.builds(
    Net_runEntryEventOccurrence,
)
Net_mainExitEventOccurrence_strategy = st.builds(
    Net_mainExitEventOccurrence,
)
Net_mainEntryEventOccurrence_strategy = st.builds(
    Net_mainEntryEventOccurrence,
)
trace_Events_Events_strategy = st.builds(
    trace_Events_Events,
)
Events_trace_GlobalState_strategy = st.builds(
    Events_trace_GlobalState,
)
trace_Events_EventOccurrence_strategy = st.builds(
    trace_Events_EventOccurrence,
)
trace_Net_strategy = st.builds(
    trace_Net,
)
trace_Transition_strategy = st.builds(
    trace_Transition,
)
Place_tokens_State_strategy = st.builds(
    Place_tokens_State,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
trace_Events_Net_mainEntryEventOccurrence_strategy = st.builds(
    trace_Events_Net_mainEntryEventOccurrence,
)
trace_StaticObjectsPools_strategy = st.builds(
    trace_StaticObjectsPools,
)
TracedObjects_strategy = st.builds(
    TracedObjects,
)
petrinet_trace_Place_strategy = st.builds(
    petrinet_trace_Place,
)
trace_petrinet_TracedPlace_strategy = st.builds(
    trace_petrinet_TracedPlace,
    name=
        safe_text,
    initialTokens=
        st.integers()
)
trace_Traced_TracedObjects_strategy = st.builds(
    trace_Traced_TracedObjects,
)
States_trace_GlobalState_strategy = st.builds(
    States_trace_GlobalState,
)
trace_States_Place_tokens_State_strategy = st.builds(
    trace_States_Place_tokens_State,
    tokens=
        st.integers()
)
trace_Events_Transition_fireExitEventOccurrence_strategy = st.builds(
    trace_Events_Transition_fireExitEventOccurrence,
)
trace_Events_Transition_fireEntryEventOccurrence_strategy = st.builds(
    trace_Events_Transition_fireEntryEventOccurrence,
)
Events_trace_EObject_strategy = st.builds(
    Events_trace_EObject,
)
trace_Events_Transition_isEnabledExitEventOccurrence_strategy = st.builds(
    trace_Events_Transition_isEnabledExitEventOccurrence,
)
Events_trace_Transition_strategy = st.builds(
    Events_trace_Transition,
)
trace_Events_Transition_isEnabledEntryEventOccurrence_strategy = st.builds(
    trace_Events_Transition_isEnabledEntryEventOccurrence,
)
trace_Events_Place_removeTokenExitEventOccurrence_strategy = st.builds(
    trace_Events_Place_removeTokenExitEventOccurrence,
)
trace_Events_Place_removeTokenEntryEventOccurrence_strategy = st.builds(
    trace_Events_Place_removeTokenEntryEventOccurrence,
)
trace_Events_Place_addTokenExitEventOccurrence_strategy = st.builds(
    trace_Events_Place_addTokenExitEventOccurrence,
)
petrinet_TracedPlace_strategy = st.builds(
    petrinet_TracedPlace,
)
trace_Events_Place_addTokenEntryEventOccurrence_strategy = st.builds(
    trace_Events_Place_addTokenEntryEventOccurrence,
)
trace_Events_Net_runExitEventOccurrence_strategy = st.builds(
    trace_Events_Net_runExitEventOccurrence,
)
trace_Events_Net_runEntryEventOccurrence_strategy = st.builds(
    trace_Events_Net_runEntryEventOccurrence,
)
trace_Events_Net_mainExitEventOccurrence_strategy = st.builds(
    trace_Events_Net_mainExitEventOccurrence,
)
Events_strategy = st.builds(
    Events,
)
trace_GlobalState_strategy = st.builds(
    trace_GlobalState,
)
trace_Trace_strategy = st.builds(
    trace_Trace,
)

@given(instance=Events_trace_Net_strategy)
@settings(max_examples=50)
def test_events_trace_net_instantiation(instance):
    assert isinstance(instance, Events_trace_Net)

@given(instance=Transition_fireExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_transition_fireexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Transition_fireExitEventOccurrence)

@given(instance=Transition_fireEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_transition_fireentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Transition_fireEntryEventOccurrence)

@given(instance=Transition_isEnabledExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_transition_isenabledexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Transition_isEnabledExitEventOccurrence)

@given(instance=Transition_isEnabledEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_transition_isenabledentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Transition_isEnabledEntryEventOccurrence)

@given(instance=Place_removeTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_place_removetokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Place_removeTokenExitEventOccurrence)

@given(instance=Place_removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_place_removetokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Place_removeTokenEntryEventOccurrence)

@given(instance=Place_addTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_place_addtokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Place_addTokenExitEventOccurrence)

@given(instance=Place_addTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_place_addtokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Place_addTokenEntryEventOccurrence)

@given(instance=Net_runExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_net_runexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Net_runExitEventOccurrence)

@given(instance=Net_runEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_net_runentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Net_runEntryEventOccurrence)

@given(instance=Net_mainExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_net_mainexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Net_mainExitEventOccurrence)

@given(instance=Net_mainEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_net_mainentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Net_mainEntryEventOccurrence)

@given(instance=trace_Events_Events_strategy)
@settings(max_examples=50)
def test_trace_events_events_instantiation(instance):
    assert isinstance(instance, trace_Events_Events)

@given(instance=Events_trace_GlobalState_strategy)
@settings(max_examples=50)
def test_events_trace_globalstate_instantiation(instance):
    assert isinstance(instance, Events_trace_GlobalState)

@given(instance=trace_Events_EventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_eventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_EventOccurrence)

@given(instance=trace_Net_strategy)
@settings(max_examples=50)
def test_trace_net_instantiation(instance):
    assert isinstance(instance, trace_Net)

@given(instance=trace_Transition_strategy)
@settings(max_examples=50)
def test_trace_transition_instantiation(instance):
    assert isinstance(instance, trace_Transition)

@given(instance=Place_tokens_State_strategy)
@settings(max_examples=50)
def test_place_tokens_state_instantiation(instance):
    assert isinstance(instance, Place_tokens_State)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=trace_Events_Net_mainEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_net_mainentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Net_mainEntryEventOccurrence)

@given(instance=trace_StaticObjectsPools_strategy)
@settings(max_examples=50)
def test_trace_staticobjectspools_instantiation(instance):
    assert isinstance(instance, trace_StaticObjectsPools)

@given(instance=TracedObjects_strategy)
@settings(max_examples=50)
def test_tracedobjects_instantiation(instance):
    assert isinstance(instance, TracedObjects)

@given(instance=petrinet_trace_Place_strategy)
@settings(max_examples=50)
def test_petrinet_trace_place_instantiation(instance):
    assert isinstance(instance, petrinet_trace_Place)

@given(instance=trace_petrinet_TracedPlace_strategy)
@settings(max_examples=50)
def test_trace_petrinet_tracedplace_instantiation(instance):
    assert isinstance(instance, trace_petrinet_TracedPlace)



@given(instance=trace_petrinet_TracedPlace_strategy)
def test_trace_petrinet_tracedplace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=trace_petrinet_TracedPlace_strategy)
def test_trace_petrinet_tracedplace_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original

@given(instance=trace_Traced_TracedObjects_strategy)
@settings(max_examples=50)
def test_trace_traced_tracedobjects_instantiation(instance):
    assert isinstance(instance, trace_Traced_TracedObjects)

@given(instance=States_trace_GlobalState_strategy)
@settings(max_examples=50)
def test_states_trace_globalstate_instantiation(instance):
    assert isinstance(instance, States_trace_GlobalState)

@given(instance=trace_States_Place_tokens_State_strategy)
@settings(max_examples=50)
def test_trace_states_place_tokens_state_instantiation(instance):
    assert isinstance(instance, trace_States_Place_tokens_State)



@given(instance=trace_States_Place_tokens_State_strategy)
def test_trace_states_place_tokens_state_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=trace_Events_Transition_fireExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_transition_fireexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Transition_fireExitEventOccurrence)

@given(instance=trace_Events_Transition_fireEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_transition_fireentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Transition_fireEntryEventOccurrence)

@given(instance=Events_trace_EObject_strategy)
@settings(max_examples=50)
def test_events_trace_eobject_instantiation(instance):
    assert isinstance(instance, Events_trace_EObject)

@given(instance=trace_Events_Transition_isEnabledExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_transition_isenabledexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Transition_isEnabledExitEventOccurrence)

@given(instance=Events_trace_Transition_strategy)
@settings(max_examples=50)
def test_events_trace_transition_instantiation(instance):
    assert isinstance(instance, Events_trace_Transition)

@given(instance=trace_Events_Transition_isEnabledEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_transition_isenabledentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Transition_isEnabledEntryEventOccurrence)

@given(instance=trace_Events_Place_removeTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_place_removetokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Place_removeTokenExitEventOccurrence)

@given(instance=trace_Events_Place_removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_place_removetokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Place_removeTokenEntryEventOccurrence)

@given(instance=trace_Events_Place_addTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_place_addtokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Place_addTokenExitEventOccurrence)

@given(instance=petrinet_TracedPlace_strategy)
@settings(max_examples=50)
def test_petrinet_tracedplace_instantiation(instance):
    assert isinstance(instance, petrinet_TracedPlace)

@given(instance=trace_Events_Place_addTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_place_addtokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Place_addTokenEntryEventOccurrence)

@given(instance=trace_Events_Net_runExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_net_runexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Net_runExitEventOccurrence)

@given(instance=trace_Events_Net_runEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_net_runentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Net_runEntryEventOccurrence)

@given(instance=trace_Events_Net_mainExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_net_mainexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Net_mainExitEventOccurrence)

@given(instance=Events_strategy)
@settings(max_examples=50)
def test_events_instantiation(instance):
    assert isinstance(instance, Events)

@given(instance=trace_GlobalState_strategy)
@settings(max_examples=50)
def test_trace_globalstate_instantiation(instance):
    assert isinstance(instance, trace_GlobalState)

@given(instance=trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, trace_Trace)

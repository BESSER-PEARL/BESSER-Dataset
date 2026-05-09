import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet::trace::Place,
    trace::petrinet::TracedPlace,
    trace::Traced::TracedObjects,
    States::trace::GlobalState,
    trace::States::Place::tokens::State,
    Events::trace::EObject,
    Events::trace::Transition,
    petrinet::TracedPlace,
    Events::trace::Net,
    Transition::fireExitEventOccurrence,
    Transition::fireEntryEventOccurrence,
    Transition::isEnabledExitEventOccurrence,
    Transition::isEnabledEntryEventOccurrence,
    Place::removeTokenExitEventOccurrence,
    Place::removeTokenEntryEventOccurrence,
    Place::addTokenExitEventOccurrence,
    Place::addTokenEntryEventOccurrence,
    Net::runExitEventOccurrence,
    Net::runEntryEventOccurrence,
    Net::mainExitEventOccurrence,
    Net::mainEntryEventOccurrence,
    trace::Events::Events,
    Events::trace::GlobalState,
    trace::Events::EventOccurrence,
    trace::Net,
    trace::Transition,
    Place::tokens::State,
    EventOccurrence,
    trace::Events::Net::runExitEventOccurrence,
    trace::Events::Place::addTokenEntryEventOccurrence,
    trace::Events::Place::removeTokenEntryEventOccurrence,
    trace::Events::Net::mainExitEventOccurrence,
    trace::Events::Net::mainEntryEventOccurrence,
    trace::Events::Transition::isEnabledExitEventOccurrence,
    trace::Events::Transition::fireEntryEventOccurrence,
    trace::Events::Transition::isEnabledEntryEventOccurrence,
    trace::Events::Place::addTokenExitEventOccurrence,
    trace::Events::Transition::fireExitEventOccurrence,
    trace::Events::Place::removeTokenExitEventOccurrence,
    trace::Events::Net::runEntryEventOccurrence,
    trace::StaticObjectsPools,
    TracedObjects,
    Events,
    trace::GlobalState,
    trace::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::trace::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::trace::Place)


def test_petrinet::trace::place_constructor_exists():
    assert callable(petrinet::trace::Place.__init__)


def test_petrinet::trace::place_constructor_args():
    sig = inspect.signature(petrinet::trace::Place.__init__)
    params = list(sig.parameters.keys())



def test_trace::petrinet::tracedplace_is_not_abstract():
    assert not inspect.isabstract(trace::petrinet::TracedPlace)


def test_trace::petrinet::tracedplace_constructor_exists():
    assert callable(trace::petrinet::TracedPlace.__init__)


def test_trace::petrinet::tracedplace_constructor_args():
    sig = inspect.signature(trace::petrinet::TracedPlace.__init__)
    params = list(sig.parameters.keys())
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"
    assert "name" in params, "Missing parameter 'name'"

def test_trace::petrinet::tracedplace_has_initialTokens():
    assert hasattr(trace::petrinet::TracedPlace, "initialTokens")
    descriptor = None
    for klass in trace::petrinet::TracedPlace.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)

def test_trace::petrinet::tracedplace_has_name():
    assert hasattr(trace::petrinet::TracedPlace, "name")
    descriptor = None
    for klass in trace::petrinet::TracedPlace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trace::traced::tracedobjects_is_not_abstract():
    assert not inspect.isabstract(trace::Traced::TracedObjects)


def test_trace::traced::tracedobjects_constructor_exists():
    assert callable(trace::Traced::TracedObjects.__init__)


def test_trace::traced::tracedobjects_constructor_args():
    sig = inspect.signature(trace::Traced::TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_states::trace::globalstate_is_not_abstract():
    assert not inspect.isabstract(States::trace::GlobalState)


def test_states::trace::globalstate_constructor_exists():
    assert callable(States::trace::GlobalState.__init__)


def test_states::trace::globalstate_constructor_args():
    sig = inspect.signature(States::trace::GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::place::tokens::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::Place::tokens::State)


def test_trace::states::place::tokens::state_constructor_exists():
    assert callable(trace::States::Place::tokens::State.__init__)


def test_trace::states::place::tokens::state_constructor_args():
    sig = inspect.signature(trace::States::Place::tokens::State.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_trace::states::place::tokens::state_has_tokens():
    assert hasattr(trace::States::Place::tokens::State, "tokens")
    descriptor = None
    for klass in trace::States::Place::tokens::State.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_events::trace::eobject_is_not_abstract():
    assert not inspect.isabstract(Events::trace::EObject)


def test_events::trace::eobject_constructor_exists():
    assert callable(Events::trace::EObject.__init__)


def test_events::trace::eobject_constructor_args():
    sig = inspect.signature(Events::trace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::transition_is_not_abstract():
    assert not inspect.isabstract(Events::trace::Transition)


def test_events::trace::transition_constructor_exists():
    assert callable(Events::trace::Transition.__init__)


def test_events::trace::transition_constructor_args():
    sig = inspect.signature(Events::trace::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::tracedplace_is_not_abstract():
    assert not inspect.isabstract(petrinet::TracedPlace)


def test_petrinet::tracedplace_constructor_exists():
    assert callable(petrinet::TracedPlace.__init__)


def test_petrinet::tracedplace_constructor_args():
    sig = inspect.signature(petrinet::TracedPlace.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::net_is_not_abstract():
    assert not inspect.isabstract(Events::trace::Net)


def test_events::trace::net_constructor_exists():
    assert callable(Events::trace::Net.__init__)


def test_events::trace::net_constructor_args():
    sig = inspect.signature(Events::trace::Net.__init__)
    params = list(sig.parameters.keys())



def test_transition::fireexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Transition::fireExitEventOccurrence)


def test_transition::fireexiteventoccurrence_constructor_exists():
    assert callable(Transition::fireExitEventOccurrence.__init__)


def test_transition::fireexiteventoccurrence_constructor_args():
    sig = inspect.signature(Transition::fireExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_transition::fireentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Transition::fireEntryEventOccurrence)


def test_transition::fireentryeventoccurrence_constructor_exists():
    assert callable(Transition::fireEntryEventOccurrence.__init__)


def test_transition::fireentryeventoccurrence_constructor_args():
    sig = inspect.signature(Transition::fireEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_transition::isenabledexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Transition::isEnabledExitEventOccurrence)


def test_transition::isenabledexiteventoccurrence_constructor_exists():
    assert callable(Transition::isEnabledExitEventOccurrence.__init__)


def test_transition::isenabledexiteventoccurrence_constructor_args():
    sig = inspect.signature(Transition::isEnabledExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_transition::isenabledentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Transition::isEnabledEntryEventOccurrence)


def test_transition::isenabledentryeventoccurrence_constructor_exists():
    assert callable(Transition::isEnabledEntryEventOccurrence.__init__)


def test_transition::isenabledentryeventoccurrence_constructor_args():
    sig = inspect.signature(Transition::isEnabledEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_place::removetokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Place::removeTokenExitEventOccurrence)


def test_place::removetokenexiteventoccurrence_constructor_exists():
    assert callable(Place::removeTokenExitEventOccurrence.__init__)


def test_place::removetokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(Place::removeTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_place::removetokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Place::removeTokenEntryEventOccurrence)


def test_place::removetokenentryeventoccurrence_constructor_exists():
    assert callable(Place::removeTokenEntryEventOccurrence.__init__)


def test_place::removetokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(Place::removeTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_place::addtokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Place::addTokenExitEventOccurrence)


def test_place::addtokenexiteventoccurrence_constructor_exists():
    assert callable(Place::addTokenExitEventOccurrence.__init__)


def test_place::addtokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(Place::addTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_place::addtokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Place::addTokenEntryEventOccurrence)


def test_place::addtokenentryeventoccurrence_constructor_exists():
    assert callable(Place::addTokenEntryEventOccurrence.__init__)


def test_place::addtokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(Place::addTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_net::runexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Net::runExitEventOccurrence)


def test_net::runexiteventoccurrence_constructor_exists():
    assert callable(Net::runExitEventOccurrence.__init__)


def test_net::runexiteventoccurrence_constructor_args():
    sig = inspect.signature(Net::runExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_net::runentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Net::runEntryEventOccurrence)


def test_net::runentryeventoccurrence_constructor_exists():
    assert callable(Net::runEntryEventOccurrence.__init__)


def test_net::runentryeventoccurrence_constructor_args():
    sig = inspect.signature(Net::runEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_net::mainexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Net::mainExitEventOccurrence)


def test_net::mainexiteventoccurrence_constructor_exists():
    assert callable(Net::mainExitEventOccurrence.__init__)


def test_net::mainexiteventoccurrence_constructor_args():
    sig = inspect.signature(Net::mainExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_net::mainentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Net::mainEntryEventOccurrence)


def test_net::mainentryeventoccurrence_constructor_exists():
    assert callable(Net::mainEntryEventOccurrence.__init__)


def test_net::mainentryeventoccurrence_constructor_args():
    sig = inspect.signature(Net::mainEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::events_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Events)


def test_trace::events::events_constructor_exists():
    assert callable(trace::Events::Events.__init__)


def test_trace::events::events_constructor_args():
    sig = inspect.signature(trace::Events::Events.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::globalstate_is_not_abstract():
    assert not inspect.isabstract(Events::trace::GlobalState)


def test_events::trace::globalstate_constructor_exists():
    assert callable(Events::trace::GlobalState.__init__)


def test_events::trace::globalstate_constructor_args():
    sig = inspect.signature(Events::trace::GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::EventOccurrence)


def test_trace::events::eventoccurrence_constructor_exists():
    assert callable(trace::Events::EventOccurrence.__init__)


def test_trace::events::eventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::net_is_not_abstract():
    assert not inspect.isabstract(trace::Net)


def test_trace::net_constructor_exists():
    assert callable(trace::Net.__init__)


def test_trace::net_constructor_args():
    sig = inspect.signature(trace::Net.__init__)
    params = list(sig.parameters.keys())



def test_trace::transition_is_not_abstract():
    assert not inspect.isabstract(trace::Transition)


def test_trace::transition_constructor_exists():
    assert callable(trace::Transition.__init__)


def test_trace::transition_constructor_args():
    sig = inspect.signature(trace::Transition.__init__)
    params = list(sig.parameters.keys())



def test_place::tokens::state_is_not_abstract():
    assert not inspect.isabstract(Place::tokens::State)


def test_place::tokens::state_constructor_exists():
    assert callable(Place::tokens::State.__init__)


def test_place::tokens::state_constructor_args():
    sig = inspect.signature(Place::tokens::State.__init__)
    params = list(sig.parameters.keys())



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::net::runexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Net::runExitEventOccurrence)


def test_trace::events::net::runexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Net::runExitEventOccurrence.__init__)


def test_trace::events::net::runexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Net::runExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::place::addtokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Place::addTokenEntryEventOccurrence)


def test_trace::events::place::addtokenentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Place::addTokenEntryEventOccurrence.__init__)


def test_trace::events::place::addtokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Place::addTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::place::removetokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Place::removeTokenEntryEventOccurrence)


def test_trace::events::place::removetokenentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Place::removeTokenEntryEventOccurrence.__init__)


def test_trace::events::place::removetokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Place::removeTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::net::mainexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Net::mainExitEventOccurrence)


def test_trace::events::net::mainexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Net::mainExitEventOccurrence.__init__)


def test_trace::events::net::mainexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Net::mainExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::net::mainentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Net::mainEntryEventOccurrence)


def test_trace::events::net::mainentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Net::mainEntryEventOccurrence.__init__)


def test_trace::events::net::mainentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Net::mainEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::transition::isenabledexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Transition::isEnabledExitEventOccurrence)


def test_trace::events::transition::isenabledexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Transition::isEnabledExitEventOccurrence.__init__)


def test_trace::events::transition::isenabledexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Transition::isEnabledExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::transition::fireentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Transition::fireEntryEventOccurrence)


def test_trace::events::transition::fireentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Transition::fireEntryEventOccurrence.__init__)


def test_trace::events::transition::fireentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Transition::fireEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::transition::isenabledentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Transition::isEnabledEntryEventOccurrence)


def test_trace::events::transition::isenabledentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Transition::isEnabledEntryEventOccurrence.__init__)


def test_trace::events::transition::isenabledentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Transition::isEnabledEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::place::addtokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Place::addTokenExitEventOccurrence)


def test_trace::events::place::addtokenexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Place::addTokenExitEventOccurrence.__init__)


def test_trace::events::place::addtokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Place::addTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::transition::fireexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Transition::fireExitEventOccurrence)


def test_trace::events::transition::fireexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Transition::fireExitEventOccurrence.__init__)


def test_trace::events::transition::fireexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Transition::fireExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::place::removetokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Place::removeTokenExitEventOccurrence)


def test_trace::events::place::removetokenexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Place::removeTokenExitEventOccurrence.__init__)


def test_trace::events::place::removetokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Place::removeTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::net::runentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Net::runEntryEventOccurrence)


def test_trace::events::net::runentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Net::runEntryEventOccurrence.__init__)


def test_trace::events::net::runentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Net::runEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::staticobjectspools_is_not_abstract():
    assert not inspect.isabstract(trace::StaticObjectsPools)


def test_trace::staticobjectspools_constructor_exists():
    assert callable(trace::StaticObjectsPools.__init__)


def test_trace::staticobjectspools_constructor_args():
    sig = inspect.signature(trace::StaticObjectsPools.__init__)
    params = list(sig.parameters.keys())



def test_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(TracedObjects)


def test_tracedobjects_constructor_exists():
    assert callable(TracedObjects.__init__)


def test_tracedobjects_constructor_args():
    sig = inspect.signature(TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_events_is_not_abstract():
    assert not inspect.isabstract(Events)


def test_events_constructor_exists():
    assert callable(Events.__init__)


def test_events_constructor_args():
    sig = inspect.signature(Events.__init__)
    params = list(sig.parameters.keys())



def test_trace::globalstate_is_not_abstract():
    assert not inspect.isabstract(trace::GlobalState)


def test_trace::globalstate_constructor_exists():
    assert callable(trace::GlobalState.__init__)


def test_trace::globalstate_constructor_args():
    sig = inspect.signature(trace::GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
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
petrinet::trace::Place_strategy = st.builds(
    petrinet::trace::Place,
)
trace::petrinet::TracedPlace_strategy = st.builds(
    trace::petrinet::TracedPlace,
    initialTokens=
        st.integers(),
    name=
        safe_text
)
trace::Traced::TracedObjects_strategy = st.builds(
    trace::Traced::TracedObjects,
)
States::trace::GlobalState_strategy = st.builds(
    States::trace::GlobalState,
)
trace::States::Place::tokens::State_strategy = st.builds(
    trace::States::Place::tokens::State,
    tokens=
        st.integers()
)
Events::trace::EObject_strategy = st.builds(
    Events::trace::EObject,
)
Events::trace::Transition_strategy = st.builds(
    Events::trace::Transition,
)
petrinet::TracedPlace_strategy = st.builds(
    petrinet::TracedPlace,
)
Events::trace::Net_strategy = st.builds(
    Events::trace::Net,
)
Transition::fireExitEventOccurrence_strategy = st.builds(
    Transition::fireExitEventOccurrence,
)
Transition::fireEntryEventOccurrence_strategy = st.builds(
    Transition::fireEntryEventOccurrence,
)
Transition::isEnabledExitEventOccurrence_strategy = st.builds(
    Transition::isEnabledExitEventOccurrence,
)
Transition::isEnabledEntryEventOccurrence_strategy = st.builds(
    Transition::isEnabledEntryEventOccurrence,
)
Place::removeTokenExitEventOccurrence_strategy = st.builds(
    Place::removeTokenExitEventOccurrence,
)
Place::removeTokenEntryEventOccurrence_strategy = st.builds(
    Place::removeTokenEntryEventOccurrence,
)
Place::addTokenExitEventOccurrence_strategy = st.builds(
    Place::addTokenExitEventOccurrence,
)
Place::addTokenEntryEventOccurrence_strategy = st.builds(
    Place::addTokenEntryEventOccurrence,
)
Net::runExitEventOccurrence_strategy = st.builds(
    Net::runExitEventOccurrence,
)
Net::runEntryEventOccurrence_strategy = st.builds(
    Net::runEntryEventOccurrence,
)
Net::mainExitEventOccurrence_strategy = st.builds(
    Net::mainExitEventOccurrence,
)
Net::mainEntryEventOccurrence_strategy = st.builds(
    Net::mainEntryEventOccurrence,
)
trace::Events::Events_strategy = st.builds(
    trace::Events::Events,
)
Events::trace::GlobalState_strategy = st.builds(
    Events::trace::GlobalState,
)
trace::Events::EventOccurrence_strategy = st.builds(
    trace::Events::EventOccurrence,
)
trace::Net_strategy = st.builds(
    trace::Net,
)
trace::Transition_strategy = st.builds(
    trace::Transition,
)
Place::tokens::State_strategy = st.builds(
    Place::tokens::State,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
trace::Events::Net::runExitEventOccurrence_strategy = st.builds(
    trace::Events::Net::runExitEventOccurrence,
)
trace::Events::Place::addTokenEntryEventOccurrence_strategy = st.builds(
    trace::Events::Place::addTokenEntryEventOccurrence,
)
trace::Events::Place::removeTokenEntryEventOccurrence_strategy = st.builds(
    trace::Events::Place::removeTokenEntryEventOccurrence,
)
trace::Events::Net::mainExitEventOccurrence_strategy = st.builds(
    trace::Events::Net::mainExitEventOccurrence,
)
trace::Events::Net::mainEntryEventOccurrence_strategy = st.builds(
    trace::Events::Net::mainEntryEventOccurrence,
)
trace::Events::Transition::isEnabledExitEventOccurrence_strategy = st.builds(
    trace::Events::Transition::isEnabledExitEventOccurrence,
)
trace::Events::Transition::fireEntryEventOccurrence_strategy = st.builds(
    trace::Events::Transition::fireEntryEventOccurrence,
)
trace::Events::Transition::isEnabledEntryEventOccurrence_strategy = st.builds(
    trace::Events::Transition::isEnabledEntryEventOccurrence,
)
trace::Events::Place::addTokenExitEventOccurrence_strategy = st.builds(
    trace::Events::Place::addTokenExitEventOccurrence,
)
trace::Events::Transition::fireExitEventOccurrence_strategy = st.builds(
    trace::Events::Transition::fireExitEventOccurrence,
)
trace::Events::Place::removeTokenExitEventOccurrence_strategy = st.builds(
    trace::Events::Place::removeTokenExitEventOccurrence,
)
trace::Events::Net::runEntryEventOccurrence_strategy = st.builds(
    trace::Events::Net::runEntryEventOccurrence,
)
trace::StaticObjectsPools_strategy = st.builds(
    trace::StaticObjectsPools,
)
TracedObjects_strategy = st.builds(
    TracedObjects,
)
Events_strategy = st.builds(
    Events,
)
trace::GlobalState_strategy = st.builds(
    trace::GlobalState,
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)

@given(instance=petrinet::trace::Place_strategy)
@settings(max_examples=50)
def test_petrinet::trace::place_instantiation(instance):
    assert isinstance(instance, petrinet::trace::Place)

@given(instance=trace::petrinet::TracedPlace_strategy)
@settings(max_examples=50)
def test_trace::petrinet::tracedplace_instantiation(instance):
    assert isinstance(instance, trace::petrinet::TracedPlace)

@given(instance=trace::petrinet::TracedPlace_strategy)
def test_trace::petrinet::tracedplace_initialTokens_type(instance):
    assert isinstance(instance.initialTokens, int)


@given(instance=trace::petrinet::TracedPlace_strategy)
def test_trace::petrinet::tracedplace_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original

@given(instance=trace::petrinet::TracedPlace_strategy)
def test_trace::petrinet::tracedplace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trace::petrinet::TracedPlace_strategy)
def test_trace::petrinet::tracedplace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trace::Traced::TracedObjects_strategy)
@settings(max_examples=50)
def test_trace::traced::tracedobjects_instantiation(instance):
    assert isinstance(instance, trace::Traced::TracedObjects)

@given(instance=States::trace::GlobalState_strategy)
@settings(max_examples=50)
def test_states::trace::globalstate_instantiation(instance):
    assert isinstance(instance, States::trace::GlobalState)

@given(instance=trace::States::Place::tokens::State_strategy)
@settings(max_examples=50)
def test_trace::states::place::tokens::state_instantiation(instance):
    assert isinstance(instance, trace::States::Place::tokens::State)

@given(instance=trace::States::Place::tokens::State_strategy)
def test_trace::states::place::tokens::state_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=trace::States::Place::tokens::State_strategy)
def test_trace::states::place::tokens::state_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=Events::trace::EObject_strategy)
@settings(max_examples=50)
def test_events::trace::eobject_instantiation(instance):
    assert isinstance(instance, Events::trace::EObject)

@given(instance=Events::trace::Transition_strategy)
@settings(max_examples=50)
def test_events::trace::transition_instantiation(instance):
    assert isinstance(instance, Events::trace::Transition)

@given(instance=petrinet::TracedPlace_strategy)
@settings(max_examples=50)
def test_petrinet::tracedplace_instantiation(instance):
    assert isinstance(instance, petrinet::TracedPlace)

@given(instance=Events::trace::Net_strategy)
@settings(max_examples=50)
def test_events::trace::net_instantiation(instance):
    assert isinstance(instance, Events::trace::Net)

@given(instance=Transition::fireExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_transition::fireexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Transition::fireExitEventOccurrence)

@given(instance=Transition::fireEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_transition::fireentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Transition::fireEntryEventOccurrence)

@given(instance=Transition::isEnabledExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_transition::isenabledexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Transition::isEnabledExitEventOccurrence)

@given(instance=Transition::isEnabledEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_transition::isenabledentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Transition::isEnabledEntryEventOccurrence)

@given(instance=Place::removeTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_place::removetokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Place::removeTokenExitEventOccurrence)

@given(instance=Place::removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_place::removetokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Place::removeTokenEntryEventOccurrence)

@given(instance=Place::addTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_place::addtokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Place::addTokenExitEventOccurrence)

@given(instance=Place::addTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_place::addtokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Place::addTokenEntryEventOccurrence)

@given(instance=Net::runExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_net::runexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Net::runExitEventOccurrence)

@given(instance=Net::runEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_net::runentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Net::runEntryEventOccurrence)

@given(instance=Net::mainExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_net::mainexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Net::mainExitEventOccurrence)

@given(instance=Net::mainEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_net::mainentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Net::mainEntryEventOccurrence)

@given(instance=trace::Events::Events_strategy)
@settings(max_examples=50)
def test_trace::events::events_instantiation(instance):
    assert isinstance(instance, trace::Events::Events)

@given(instance=Events::trace::GlobalState_strategy)
@settings(max_examples=50)
def test_events::trace::globalstate_instantiation(instance):
    assert isinstance(instance, Events::trace::GlobalState)

@given(instance=trace::Events::EventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::eventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::EventOccurrence)

@given(instance=trace::Net_strategy)
@settings(max_examples=50)
def test_trace::net_instantiation(instance):
    assert isinstance(instance, trace::Net)

@given(instance=trace::Transition_strategy)
@settings(max_examples=50)
def test_trace::transition_instantiation(instance):
    assert isinstance(instance, trace::Transition)

@given(instance=Place::tokens::State_strategy)
@settings(max_examples=50)
def test_place::tokens::state_instantiation(instance):
    assert isinstance(instance, Place::tokens::State)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=trace::Events::Net::runExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::net::runexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Net::runExitEventOccurrence)

@given(instance=trace::Events::Place::addTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::place::addtokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Place::addTokenEntryEventOccurrence)

@given(instance=trace::Events::Place::removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::place::removetokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Place::removeTokenEntryEventOccurrence)

@given(instance=trace::Events::Net::mainExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::net::mainexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Net::mainExitEventOccurrence)

@given(instance=trace::Events::Net::mainEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::net::mainentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Net::mainEntryEventOccurrence)

@given(instance=trace::Events::Transition::isEnabledExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::transition::isenabledexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Transition::isEnabledExitEventOccurrence)

@given(instance=trace::Events::Transition::fireEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::transition::fireentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Transition::fireEntryEventOccurrence)

@given(instance=trace::Events::Transition::isEnabledEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::transition::isenabledentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Transition::isEnabledEntryEventOccurrence)

@given(instance=trace::Events::Place::addTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::place::addtokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Place::addTokenExitEventOccurrence)

@given(instance=trace::Events::Transition::fireExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::transition::fireexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Transition::fireExitEventOccurrence)

@given(instance=trace::Events::Place::removeTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::place::removetokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Place::removeTokenExitEventOccurrence)

@given(instance=trace::Events::Net::runEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::net::runentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Net::runEntryEventOccurrence)

@given(instance=trace::StaticObjectsPools_strategy)
@settings(max_examples=50)
def test_trace::staticobjectspools_instantiation(instance):
    assert isinstance(instance, trace::StaticObjectsPools)

@given(instance=TracedObjects_strategy)
@settings(max_examples=50)
def test_tracedobjects_instantiation(instance):
    assert isinstance(instance, TracedObjects)

@given(instance=Events_strategy)
@settings(max_examples=50)
def test_events_instantiation(instance):
    assert isinstance(instance, Events)

@given(instance=trace::GlobalState_strategy)
@settings(max_examples=50)
def test_trace::globalstate_instantiation(instance):
    assert isinstance(instance, trace::GlobalState)

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

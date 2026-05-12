import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    trace_Traced_TracedObjects,
    trace_States_A_a_State,
    model2_trace_A,
    trace_model2_TracedA,
    trace_model2Configuration_TracedC,
    trace_model2Configuration_TracedB,
    A_doAEntryEventOccurrence,
    trace_Events_Events,
    Events_trace_GlobalState,
    trace_Events_EventOccurrence,
    trace_F,
    States_trace_F,
    trace_States_C_c_State,
    States_trace_GlobalState,
    trace_States_B_b_State,
    model2Configuration_TracedB,
    model2Configuration_TracedC,
    model2_TracedA,
    C_doCExitEventOccurrence,
    C_doCEntryEventOccurrence,
    A_doAExitEventOccurrence,
    A_a_State,
    C_c_State,
    B_b_State,
    EventOccurrence,
    trace_Events_A_doAEntryEventOccurrence,
    trace_Events_C_doCExitEventOccurrence,
    trace_Events_A_doAExitEventOccurrence,
    trace_Events_C_doCEntryEventOccurrence,
    trace_StaticObjectsPools,
    TracedObjects,
    Events,
    trace_GlobalState,
    trace_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace_traced_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(trace_Traced_TracedObjects)


def test_trace_traced_tracedobjects_constructor_exists():
    assert callable(trace_Traced_TracedObjects.__init__)


def test_trace_traced_tracedobjects_constructor_args():
    sig = inspect.signature(trace_Traced_TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_a_a_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_A_a_State)


def test_trace_states_a_a_state_constructor_exists():
    assert callable(trace_States_A_a_State.__init__)


def test_trace_states_a_a_state_constructor_args():
    sig = inspect.signature(trace_States_A_a_State.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_trace_states_a_a_state_has_a():
    assert hasattr(trace_States_A_a_State, "a")
    descriptor = None
    for klass in trace_States_A_a_State.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_model2_trace_a_is_not_abstract():
    assert not inspect.isabstract(model2_trace_A)


def test_model2_trace_a_constructor_exists():
    assert callable(model2_trace_A.__init__)


def test_model2_trace_a_constructor_args():
    sig = inspect.signature(model2_trace_A.__init__)
    params = list(sig.parameters.keys())



def test_trace_model2_traceda_is_not_abstract():
    assert not inspect.isabstract(trace_model2_TracedA)


def test_trace_model2_traceda_constructor_exists():
    assert callable(trace_model2_TracedA.__init__)


def test_trace_model2_traceda_constructor_args():
    sig = inspect.signature(trace_model2_TracedA.__init__)
    params = list(sig.parameters.keys())



def test_trace_model2configuration_tracedc_is_not_abstract():
    assert not inspect.isabstract(trace_model2Configuration_TracedC)


def test_trace_model2configuration_tracedc_constructor_exists():
    assert callable(trace_model2Configuration_TracedC.__init__)


def test_trace_model2configuration_tracedc_constructor_args():
    sig = inspect.signature(trace_model2Configuration_TracedC.__init__)
    params = list(sig.parameters.keys())



def test_trace_model2configuration_tracedb_is_not_abstract():
    assert not inspect.isabstract(trace_model2Configuration_TracedB)


def test_trace_model2configuration_tracedb_constructor_exists():
    assert callable(trace_model2Configuration_TracedB.__init__)


def test_trace_model2configuration_tracedb_constructor_args():
    sig = inspect.signature(trace_model2Configuration_TracedB.__init__)
    params = list(sig.parameters.keys())



def test_a_doaentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(A_doAEntryEventOccurrence)


def test_a_doaentryeventoccurrence_constructor_exists():
    assert callable(A_doAEntryEventOccurrence.__init__)


def test_a_doaentryeventoccurrence_constructor_args():
    sig = inspect.signature(A_doAEntryEventOccurrence.__init__)
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



def test_trace_f_is_not_abstract():
    assert not inspect.isabstract(trace_F)


def test_trace_f_constructor_exists():
    assert callable(trace_F.__init__)


def test_trace_f_constructor_args():
    sig = inspect.signature(trace_F.__init__)
    params = list(sig.parameters.keys())



def test_states_trace_f_is_not_abstract():
    assert not inspect.isabstract(States_trace_F)


def test_states_trace_f_constructor_exists():
    assert callable(States_trace_F.__init__)


def test_states_trace_f_constructor_args():
    sig = inspect.signature(States_trace_F.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_c_c_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_C_c_State)


def test_trace_states_c_c_state_constructor_exists():
    assert callable(trace_States_C_c_State.__init__)


def test_trace_states_c_c_state_constructor_args():
    sig = inspect.signature(trace_States_C_c_State.__init__)
    params = list(sig.parameters.keys())



def test_states_trace_globalstate_is_not_abstract():
    assert not inspect.isabstract(States_trace_GlobalState)


def test_states_trace_globalstate_constructor_exists():
    assert callable(States_trace_GlobalState.__init__)


def test_states_trace_globalstate_constructor_args():
    sig = inspect.signature(States_trace_GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_b_b_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_B_b_State)


def test_trace_states_b_b_state_constructor_exists():
    assert callable(trace_States_B_b_State.__init__)


def test_trace_states_b_b_state_constructor_args():
    sig = inspect.signature(trace_States_B_b_State.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_trace_states_b_b_state_has_b():
    assert hasattr(trace_States_B_b_State, "b")
    descriptor = None
    for klass in trace_States_B_b_State.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_model2configuration_tracedb_is_not_abstract():
    assert not inspect.isabstract(model2Configuration_TracedB)


def test_model2configuration_tracedb_constructor_exists():
    assert callable(model2Configuration_TracedB.__init__)


def test_model2configuration_tracedb_constructor_args():
    sig = inspect.signature(model2Configuration_TracedB.__init__)
    params = list(sig.parameters.keys())



def test_model2configuration_tracedc_is_not_abstract():
    assert not inspect.isabstract(model2Configuration_TracedC)


def test_model2configuration_tracedc_constructor_exists():
    assert callable(model2Configuration_TracedC.__init__)


def test_model2configuration_tracedc_constructor_args():
    sig = inspect.signature(model2Configuration_TracedC.__init__)
    params = list(sig.parameters.keys())



def test_model2_traceda_is_not_abstract():
    assert not inspect.isabstract(model2_TracedA)


def test_model2_traceda_constructor_exists():
    assert callable(model2_TracedA.__init__)


def test_model2_traceda_constructor_args():
    sig = inspect.signature(model2_TracedA.__init__)
    params = list(sig.parameters.keys())



def test_c_docexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(C_doCExitEventOccurrence)


def test_c_docexiteventoccurrence_constructor_exists():
    assert callable(C_doCExitEventOccurrence.__init__)


def test_c_docexiteventoccurrence_constructor_args():
    sig = inspect.signature(C_doCExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_c_docentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(C_doCEntryEventOccurrence)


def test_c_docentryeventoccurrence_constructor_exists():
    assert callable(C_doCEntryEventOccurrence.__init__)


def test_c_docentryeventoccurrence_constructor_args():
    sig = inspect.signature(C_doCEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_a_doaexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(A_doAExitEventOccurrence)


def test_a_doaexiteventoccurrence_constructor_exists():
    assert callable(A_doAExitEventOccurrence.__init__)


def test_a_doaexiteventoccurrence_constructor_args():
    sig = inspect.signature(A_doAExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_a_a_state_is_not_abstract():
    assert not inspect.isabstract(A_a_State)


def test_a_a_state_constructor_exists():
    assert callable(A_a_State.__init__)


def test_a_a_state_constructor_args():
    sig = inspect.signature(A_a_State.__init__)
    params = list(sig.parameters.keys())



def test_c_c_state_is_not_abstract():
    assert not inspect.isabstract(C_c_State)


def test_c_c_state_constructor_exists():
    assert callable(C_c_State.__init__)


def test_c_c_state_constructor_args():
    sig = inspect.signature(C_c_State.__init__)
    params = list(sig.parameters.keys())



def test_b_b_state_is_not_abstract():
    assert not inspect.isabstract(B_b_State)


def test_b_b_state_constructor_exists():
    assert callable(B_b_State.__init__)


def test_b_b_state_constructor_args():
    sig = inspect.signature(B_b_State.__init__)
    params = list(sig.parameters.keys())



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_a_doaentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_A_doAEntryEventOccurrence)


def test_trace_events_a_doaentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_A_doAEntryEventOccurrence.__init__)


def test_trace_events_a_doaentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_A_doAEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_c_docexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_C_doCExitEventOccurrence)


def test_trace_events_c_docexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_C_doCExitEventOccurrence.__init__)


def test_trace_events_c_docexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_C_doCExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_a_doaexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_A_doAExitEventOccurrence)


def test_trace_events_a_doaexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_A_doAExitEventOccurrence.__init__)


def test_trace_events_a_doaexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_A_doAExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_c_docentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_C_doCEntryEventOccurrence)


def test_trace_events_c_docentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_C_doCEntryEventOccurrence.__init__)


def test_trace_events_c_docentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_C_doCEntryEventOccurrence.__init__)
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
trace_Traced_TracedObjects_strategy = st.builds(
    trace_Traced_TracedObjects,
)
trace_States_A_a_State_strategy = st.builds(
    trace_States_A_a_State,
    a=
        st.integers()
)
model2_trace_A_strategy = st.builds(
    model2_trace_A,
)
trace_model2_TracedA_strategy = st.builds(
    trace_model2_TracedA,
)
trace_model2Configuration_TracedC_strategy = st.builds(
    trace_model2Configuration_TracedC,
)
trace_model2Configuration_TracedB_strategy = st.builds(
    trace_model2Configuration_TracedB,
)
A_doAEntryEventOccurrence_strategy = st.builds(
    A_doAEntryEventOccurrence,
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
trace_F_strategy = st.builds(
    trace_F,
)
States_trace_F_strategy = st.builds(
    States_trace_F,
)
trace_States_C_c_State_strategy = st.builds(
    trace_States_C_c_State,
)
States_trace_GlobalState_strategy = st.builds(
    States_trace_GlobalState,
)
trace_States_B_b_State_strategy = st.builds(
    trace_States_B_b_State,
    b=
        st.integers()
)
model2Configuration_TracedB_strategy = st.builds(
    model2Configuration_TracedB,
)
model2Configuration_TracedC_strategy = st.builds(
    model2Configuration_TracedC,
)
model2_TracedA_strategy = st.builds(
    model2_TracedA,
)
C_doCExitEventOccurrence_strategy = st.builds(
    C_doCExitEventOccurrence,
)
C_doCEntryEventOccurrence_strategy = st.builds(
    C_doCEntryEventOccurrence,
)
A_doAExitEventOccurrence_strategy = st.builds(
    A_doAExitEventOccurrence,
)
A_a_State_strategy = st.builds(
    A_a_State,
)
C_c_State_strategy = st.builds(
    C_c_State,
)
B_b_State_strategy = st.builds(
    B_b_State,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
trace_Events_A_doAEntryEventOccurrence_strategy = st.builds(
    trace_Events_A_doAEntryEventOccurrence,
)
trace_Events_C_doCExitEventOccurrence_strategy = st.builds(
    trace_Events_C_doCExitEventOccurrence,
)
trace_Events_A_doAExitEventOccurrence_strategy = st.builds(
    trace_Events_A_doAExitEventOccurrence,
)
trace_Events_C_doCEntryEventOccurrence_strategy = st.builds(
    trace_Events_C_doCEntryEventOccurrence,
)
trace_StaticObjectsPools_strategy = st.builds(
    trace_StaticObjectsPools,
)
TracedObjects_strategy = st.builds(
    TracedObjects,
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

@given(instance=trace_Traced_TracedObjects_strategy)
@settings(max_examples=50)
def test_trace_traced_tracedobjects_instantiation(instance):
    assert isinstance(instance, trace_Traced_TracedObjects)

@given(instance=trace_States_A_a_State_strategy)
@settings(max_examples=50)
def test_trace_states_a_a_state_instantiation(instance):
    assert isinstance(instance, trace_States_A_a_State)



@given(instance=trace_States_A_a_State_strategy)
def test_trace_states_a_a_state_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=model2_trace_A_strategy)
@settings(max_examples=50)
def test_model2_trace_a_instantiation(instance):
    assert isinstance(instance, model2_trace_A)

@given(instance=trace_model2_TracedA_strategy)
@settings(max_examples=50)
def test_trace_model2_traceda_instantiation(instance):
    assert isinstance(instance, trace_model2_TracedA)

@given(instance=trace_model2Configuration_TracedC_strategy)
@settings(max_examples=50)
def test_trace_model2configuration_tracedc_instantiation(instance):
    assert isinstance(instance, trace_model2Configuration_TracedC)

@given(instance=trace_model2Configuration_TracedB_strategy)
@settings(max_examples=50)
def test_trace_model2configuration_tracedb_instantiation(instance):
    assert isinstance(instance, trace_model2Configuration_TracedB)

@given(instance=A_doAEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_a_doaentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, A_doAEntryEventOccurrence)

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

@given(instance=trace_F_strategy)
@settings(max_examples=50)
def test_trace_f_instantiation(instance):
    assert isinstance(instance, trace_F)

@given(instance=States_trace_F_strategy)
@settings(max_examples=50)
def test_states_trace_f_instantiation(instance):
    assert isinstance(instance, States_trace_F)

@given(instance=trace_States_C_c_State_strategy)
@settings(max_examples=50)
def test_trace_states_c_c_state_instantiation(instance):
    assert isinstance(instance, trace_States_C_c_State)

@given(instance=States_trace_GlobalState_strategy)
@settings(max_examples=50)
def test_states_trace_globalstate_instantiation(instance):
    assert isinstance(instance, States_trace_GlobalState)

@given(instance=trace_States_B_b_State_strategy)
@settings(max_examples=50)
def test_trace_states_b_b_state_instantiation(instance):
    assert isinstance(instance, trace_States_B_b_State)



@given(instance=trace_States_B_b_State_strategy)
def test_trace_states_b_b_state_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=model2Configuration_TracedB_strategy)
@settings(max_examples=50)
def test_model2configuration_tracedb_instantiation(instance):
    assert isinstance(instance, model2Configuration_TracedB)

@given(instance=model2Configuration_TracedC_strategy)
@settings(max_examples=50)
def test_model2configuration_tracedc_instantiation(instance):
    assert isinstance(instance, model2Configuration_TracedC)

@given(instance=model2_TracedA_strategy)
@settings(max_examples=50)
def test_model2_traceda_instantiation(instance):
    assert isinstance(instance, model2_TracedA)

@given(instance=C_doCExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_c_docexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, C_doCExitEventOccurrence)

@given(instance=C_doCEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_c_docentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, C_doCEntryEventOccurrence)

@given(instance=A_doAExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_a_doaexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, A_doAExitEventOccurrence)

@given(instance=A_a_State_strategy)
@settings(max_examples=50)
def test_a_a_state_instantiation(instance):
    assert isinstance(instance, A_a_State)

@given(instance=C_c_State_strategy)
@settings(max_examples=50)
def test_c_c_state_instantiation(instance):
    assert isinstance(instance, C_c_State)

@given(instance=B_b_State_strategy)
@settings(max_examples=50)
def test_b_b_state_instantiation(instance):
    assert isinstance(instance, B_b_State)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=trace_Events_A_doAEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_a_doaentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_A_doAEntryEventOccurrence)

@given(instance=trace_Events_C_doCExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_c_docexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_C_doCExitEventOccurrence)

@given(instance=trace_Events_A_doAExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_a_doaexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_A_doAExitEventOccurrence)

@given(instance=trace_Events_C_doCEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_c_docentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_C_doCEntryEventOccurrence)

@given(instance=trace_StaticObjectsPools_strategy)
@settings(max_examples=50)
def test_trace_staticobjectspools_instantiation(instance):
    assert isinstance(instance, trace_StaticObjectsPools)

@given(instance=TracedObjects_strategy)
@settings(max_examples=50)
def test_tracedobjects_instantiation(instance):
    assert isinstance(instance, TracedObjects)

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

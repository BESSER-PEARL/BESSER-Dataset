import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    trace_Transition,
    trace_TimedZone,
    trace_Automaton,
    trace_EventPattern,
    trace_TimedZoneTrace,
    trace_Trace,
    trace_TraceModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace_transition_is_not_abstract():
    assert not inspect.isabstract(trace_Transition)


def test_trace_transition_constructor_exists():
    assert callable(trace_Transition.__init__)


def test_trace_transition_constructor_args():
    sig = inspect.signature(trace_Transition.__init__)
    params = list(sig.parameters.keys())



def test_trace_timedzone_is_not_abstract():
    assert not inspect.isabstract(trace_TimedZone)


def test_trace_timedzone_constructor_exists():
    assert callable(trace_TimedZone.__init__)


def test_trace_timedzone_constructor_args():
    sig = inspect.signature(trace_TimedZone.__init__)
    params = list(sig.parameters.keys())



def test_trace_automaton_is_not_abstract():
    assert not inspect.isabstract(trace_Automaton)


def test_trace_automaton_constructor_exists():
    assert callable(trace_Automaton.__init__)


def test_trace_automaton_constructor_args():
    sig = inspect.signature(trace_Automaton.__init__)
    params = list(sig.parameters.keys())



def test_trace_eventpattern_is_not_abstract():
    assert not inspect.isabstract(trace_EventPattern)


def test_trace_eventpattern_constructor_exists():
    assert callable(trace_EventPattern.__init__)


def test_trace_eventpattern_constructor_args():
    sig = inspect.signature(trace_EventPattern.__init__)
    params = list(sig.parameters.keys())



def test_trace_timedzonetrace_is_not_abstract():
    assert not inspect.isabstract(trace_TimedZoneTrace)


def test_trace_timedzonetrace_constructor_exists():
    assert callable(trace_TimedZoneTrace.__init__)


def test_trace_timedzonetrace_constructor_args():
    sig = inspect.signature(trace_TimedZoneTrace.__init__)
    params = list(sig.parameters.keys())



def test_trace_trace_is_not_abstract():
    assert not inspect.isabstract(trace_Trace)


def test_trace_trace_constructor_exists():
    assert callable(trace_Trace.__init__)


def test_trace_trace_constructor_args():
    sig = inspect.signature(trace_Trace.__init__)
    params = list(sig.parameters.keys())



def test_trace_tracemodel_is_not_abstract():
    assert not inspect.isabstract(trace_TraceModel)


def test_trace_tracemodel_constructor_exists():
    assert callable(trace_TraceModel.__init__)


def test_trace_tracemodel_constructor_args():
    sig = inspect.signature(trace_TraceModel.__init__)
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
trace_Transition_strategy = st.builds(
    trace_Transition,
)
trace_TimedZone_strategy = st.builds(
    trace_TimedZone,
)
trace_Automaton_strategy = st.builds(
    trace_Automaton,
)
trace_EventPattern_strategy = st.builds(
    trace_EventPattern,
)
trace_TimedZoneTrace_strategy = st.builds(
    trace_TimedZoneTrace,
)
trace_Trace_strategy = st.builds(
    trace_Trace,
)
trace_TraceModel_strategy = st.builds(
    trace_TraceModel,
)

@given(instance=trace_Transition_strategy)
@settings(max_examples=50)
def test_trace_transition_instantiation(instance):
    assert isinstance(instance, trace_Transition)

@given(instance=trace_TimedZone_strategy)
@settings(max_examples=50)
def test_trace_timedzone_instantiation(instance):
    assert isinstance(instance, trace_TimedZone)

@given(instance=trace_Automaton_strategy)
@settings(max_examples=50)
def test_trace_automaton_instantiation(instance):
    assert isinstance(instance, trace_Automaton)

@given(instance=trace_EventPattern_strategy)
@settings(max_examples=50)
def test_trace_eventpattern_instantiation(instance):
    assert isinstance(instance, trace_EventPattern)

@given(instance=trace_TimedZoneTrace_strategy)
@settings(max_examples=50)
def test_trace_timedzonetrace_instantiation(instance):
    assert isinstance(instance, trace_TimedZoneTrace)

@given(instance=trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, trace_Trace)

@given(instance=trace_TraceModel_strategy)
@settings(max_examples=50)
def test_trace_tracemodel_instantiation(instance):
    assert isinstance(instance, trace_TraceModel)

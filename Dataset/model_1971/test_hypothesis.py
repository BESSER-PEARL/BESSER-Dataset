import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trace::Transition,
    trace::TimedZone,
    trace::Automaton,
    trace::EventPattern,
    trace::TimedZoneTrace,
    trace::Trace,
    trace::TraceModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace::transition_is_not_abstract():
    assert not inspect.isabstract(trace::Transition)


def test_trace::transition_constructor_exists():
    assert callable(trace::Transition.__init__)


def test_trace::transition_constructor_args():
    sig = inspect.signature(trace::Transition.__init__)
    params = list(sig.parameters.keys())



def test_trace::timedzone_is_not_abstract():
    assert not inspect.isabstract(trace::TimedZone)


def test_trace::timedzone_constructor_exists():
    assert callable(trace::TimedZone.__init__)


def test_trace::timedzone_constructor_args():
    sig = inspect.signature(trace::TimedZone.__init__)
    params = list(sig.parameters.keys())



def test_trace::automaton_is_not_abstract():
    assert not inspect.isabstract(trace::Automaton)


def test_trace::automaton_constructor_exists():
    assert callable(trace::Automaton.__init__)


def test_trace::automaton_constructor_args():
    sig = inspect.signature(trace::Automaton.__init__)
    params = list(sig.parameters.keys())



def test_trace::eventpattern_is_not_abstract():
    assert not inspect.isabstract(trace::EventPattern)


def test_trace::eventpattern_constructor_exists():
    assert callable(trace::EventPattern.__init__)


def test_trace::eventpattern_constructor_args():
    sig = inspect.signature(trace::EventPattern.__init__)
    params = list(sig.parameters.keys())



def test_trace::timedzonetrace_is_not_abstract():
    assert not inspect.isabstract(trace::TimedZoneTrace)


def test_trace::timedzonetrace_constructor_exists():
    assert callable(trace::TimedZoneTrace.__init__)


def test_trace::timedzonetrace_constructor_args():
    sig = inspect.signature(trace::TimedZoneTrace.__init__)
    params = list(sig.parameters.keys())



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
    params = list(sig.parameters.keys())



def test_trace::tracemodel_is_not_abstract():
    assert not inspect.isabstract(trace::TraceModel)


def test_trace::tracemodel_constructor_exists():
    assert callable(trace::TraceModel.__init__)


def test_trace::tracemodel_constructor_args():
    sig = inspect.signature(trace::TraceModel.__init__)
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
trace::Transition_strategy = st.builds(
    trace::Transition,
)
trace::TimedZone_strategy = st.builds(
    trace::TimedZone,
)
trace::Automaton_strategy = st.builds(
    trace::Automaton,
)
trace::EventPattern_strategy = st.builds(
    trace::EventPattern,
)
trace::TimedZoneTrace_strategy = st.builds(
    trace::TimedZoneTrace,
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)
trace::TraceModel_strategy = st.builds(
    trace::TraceModel,
)

@given(instance=trace::Transition_strategy)
@settings(max_examples=50)
def test_trace::transition_instantiation(instance):
    assert isinstance(instance, trace::Transition)

@given(instance=trace::TimedZone_strategy)
@settings(max_examples=50)
def test_trace::timedzone_instantiation(instance):
    assert isinstance(instance, trace::TimedZone)

@given(instance=trace::Automaton_strategy)
@settings(max_examples=50)
def test_trace::automaton_instantiation(instance):
    assert isinstance(instance, trace::Automaton)

@given(instance=trace::EventPattern_strategy)
@settings(max_examples=50)
def test_trace::eventpattern_instantiation(instance):
    assert isinstance(instance, trace::EventPattern)

@given(instance=trace::TimedZoneTrace_strategy)
@settings(max_examples=50)
def test_trace::timedzonetrace_instantiation(instance):
    assert isinstance(instance, trace::TimedZoneTrace)

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

@given(instance=trace::TraceModel_strategy)
@settings(max_examples=50)
def test_trace::tracemodel_instantiation(instance):
    assert isinstance(instance, trace::TraceModel)

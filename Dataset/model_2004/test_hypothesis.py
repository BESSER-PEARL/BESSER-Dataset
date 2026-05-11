import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trace::TraceElement,
    trace::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace::traceelement_is_not_abstract():
    assert not inspect.isabstract(trace::TraceElement)


def test_trace::traceelement_constructor_exists():
    assert callable(trace::TraceElement.__init__)


def test_trace::traceelement_constructor_args():
    sig = inspect.signature(trace::TraceElement.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "event" in params, "Missing parameter 'event'"

def test_trace::traceelement_has_timestamp():
    assert hasattr(trace::TraceElement, "timestamp")
    descriptor = None
    for klass in trace::TraceElement.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_trace::traceelement_has_event():
    assert hasattr(trace::TraceElement, "event")
    descriptor = None
    for klass in trace::TraceElement.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



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
trace::TraceElement_strategy = st.builds(
    trace::TraceElement,
    timestamp=
        st.integers(),
    event=
        safe_text
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)

@given(instance=trace::TraceElement_strategy)
@settings(max_examples=50)
def test_trace::traceelement_instantiation(instance):
    assert isinstance(instance, trace::TraceElement)

@given(instance=trace::TraceElement_strategy)
def test_trace::traceelement_timestamp_type(instance):
    assert isinstance(instance.timestamp, int)


@given(instance=trace::TraceElement_strategy)
def test_trace::traceelement_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=trace::TraceElement_strategy)
def test_trace::traceelement_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=trace::TraceElement_strategy)
def test_trace::traceelement_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

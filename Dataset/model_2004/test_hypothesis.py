import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    trace_TraceElement,
    trace_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace_traceelement_is_not_abstract():
    assert not inspect.isabstract(trace_TraceElement)


def test_trace_traceelement_constructor_exists():
    assert callable(trace_TraceElement.__init__)


def test_trace_traceelement_constructor_args():
    sig = inspect.signature(trace_TraceElement.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"

def test_trace_traceelement_has_event():
    assert hasattr(trace_TraceElement, "event")
    descriptor = None
    for klass in trace_TraceElement.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_trace_traceelement_has_timestamp():
    assert hasattr(trace_TraceElement, "timestamp")
    descriptor = None
    for klass in trace_TraceElement.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)



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
trace_TraceElement_strategy = st.builds(
    trace_TraceElement,
    event=
        safe_text,
    timestamp=
        st.integers()
)
trace_Trace_strategy = st.builds(
    trace_Trace,
)

@given(instance=trace_TraceElement_strategy)
@settings(max_examples=50)
def test_trace_traceelement_instantiation(instance):
    assert isinstance(instance, trace_TraceElement)



@given(instance=trace_TraceElement_strategy)
def test_trace_traceelement_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=trace_TraceElement_strategy)
def test_trace_traceelement_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, trace_Trace)

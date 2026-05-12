import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    trace_Exception,
    trace_Log,
    trace_Trace,
    LogLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace_exception_is_not_abstract():
    assert not inspect.isabstract(trace_Exception)


def test_trace_exception_constructor_exists():
    assert callable(trace_Exception.__init__)


def test_trace_exception_constructor_args():
    sig = inspect.signature(trace_Exception.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_trace_exception_has_message():
    assert hasattr(trace_Exception, "message")
    descriptor = None
    for klass in trace_Exception.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_trace_log_is_not_abstract():
    assert not inspect.isabstract(trace_Log)


def test_trace_log_constructor_exists():
    assert callable(trace_Log.__init__)


def test_trace_log_constructor_args():
    sig = inspect.signature(trace_Log.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "message" in params, "Missing parameter 'message'"
    assert "source" in params, "Missing parameter 'source'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"

def test_trace_log_has_level():
    assert hasattr(trace_Log, "level")
    descriptor = None
    for klass in trace_Log.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_trace_log_has_message():
    assert hasattr(trace_Log, "message")
    descriptor = None
    for klass in trace_Log.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_trace_log_has_source():
    assert hasattr(trace_Log, "source")
    descriptor = None
    for klass in trace_Log.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_trace_log_has_timestamp():
    assert hasattr(trace_Log, "timestamp")
    descriptor = None
    for klass in trace_Log.__mro__:
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

def test_loglevel_exists():
    # Check that the Enumeration exists
    assert LogLevel is not None

def test_loglevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogLevel]
    expected_literals = [
        "WARNING",
        "SEVERE",
        "FINEST",
        "INFO",
        "FINE",
        "CONFIG",
        "FINER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogLevel"


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
trace_Exception_strategy = st.builds(
    trace_Exception,
    message=
        safe_text
)
trace_Log_strategy = st.builds(
    trace_Log,
    level=
        safe_text,
    message=
        safe_text,
    source=
        safe_text,
    timestamp=
        st.dates()
)
trace_Trace_strategy = st.builds(
    trace_Trace,
)

@given(instance=trace_Exception_strategy)
@settings(max_examples=50)
def test_trace_exception_instantiation(instance):
    assert isinstance(instance, trace_Exception)



@given(instance=trace_Exception_strategy)
def test_trace_exception_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=trace_Log_strategy)
@settings(max_examples=50)
def test_trace_log_instantiation(instance):
    assert isinstance(instance, trace_Log)



@given(instance=trace_Log_strategy)
def test_trace_log_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=trace_Log_strategy)
def test_trace_log_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=trace_Log_strategy)
def test_trace_log_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=trace_Log_strategy)
def test_trace_log_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, trace_Trace)

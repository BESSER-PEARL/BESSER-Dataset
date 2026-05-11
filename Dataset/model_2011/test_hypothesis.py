import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trace::Exception,
    trace::Log,
    trace::Trace,
    LogLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace::exception_is_not_abstract():
    assert not inspect.isabstract(trace::Exception)


def test_trace::exception_constructor_exists():
    assert callable(trace::Exception.__init__)


def test_trace::exception_constructor_args():
    sig = inspect.signature(trace::Exception.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_trace::exception_has_message():
    assert hasattr(trace::Exception, "message")
    descriptor = None
    for klass in trace::Exception.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_trace::log_is_not_abstract():
    assert not inspect.isabstract(trace::Log)


def test_trace::log_constructor_exists():
    assert callable(trace::Log.__init__)


def test_trace::log_constructor_args():
    sig = inspect.signature(trace::Log.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "level" in params, "Missing parameter 'level'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "message" in params, "Missing parameter 'message'"

def test_trace::log_has_source():
    assert hasattr(trace::Log, "source")
    descriptor = None
    for klass in trace::Log.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_trace::log_has_level():
    assert hasattr(trace::Log, "level")
    descriptor = None
    for klass in trace::Log.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_trace::log_has_timestamp():
    assert hasattr(trace::Log, "timestamp")
    descriptor = None
    for klass in trace::Log.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_trace::log_has_message():
    assert hasattr(trace::Log, "message")
    descriptor = None
    for klass in trace::Log.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
    params = list(sig.parameters.keys())

def test_loglevel_exists():
    # Check that the Enumeration exists
    assert LogLevel is not None

def test_loglevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogLevel]
    expected_literals = [
        "SEVERE",
        "CONFIG",
        "FINER",
        "INFO",
        "WARNING",
        "FINE",
        "FINEST",
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
trace::Exception_strategy = st.builds(
    trace::Exception,
    message=
        safe_text
)
trace::Log_strategy = st.builds(
    trace::Log,
    source=
        safe_text,
    level=
        safe_text,
    timestamp=
        st.dates(),
    message=
        safe_text
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)

@given(instance=trace::Exception_strategy)
@settings(max_examples=50)
def test_trace::exception_instantiation(instance):
    assert isinstance(instance, trace::Exception)

@given(instance=trace::Exception_strategy)
def test_trace::exception_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=trace::Exception_strategy)
def test_trace::exception_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=trace::Log_strategy)
@settings(max_examples=50)
def test_trace::log_instantiation(instance):
    assert isinstance(instance, trace::Log)

@given(instance=trace::Log_strategy)
def test_trace::log_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=trace::Log_strategy)
def test_trace::log_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=trace::Log_strategy)
def test_trace::log_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=trace::Log_strategy)
def test_trace::log_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=trace::Log_strategy)
def test_trace::log_timestamp_type(instance):
    assert isinstance(instance.timestamp, date)


@given(instance=trace::Log_strategy)
def test_trace::log_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=trace::Log_strategy)
def test_trace::log_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=trace::Log_strategy)
def test_trace::log_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

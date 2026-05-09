import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trace::EObject,
    trace::TraceLink,
    trace::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace::eobject_is_not_abstract():
    assert not inspect.isabstract(trace::EObject)


def test_trace::eobject_constructor_exists():
    assert callable(trace::EObject.__init__)


def test_trace::eobject_constructor_args():
    sig = inspect.signature(trace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_trace::tracelink_is_not_abstract():
    assert not inspect.isabstract(trace::TraceLink)


def test_trace::tracelink_constructor_exists():
    assert callable(trace::TraceLink.__init__)


def test_trace::tracelink_constructor_args():
    sig = inspect.signature(trace::TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "ruleName" in params, "Missing parameter 'ruleName'"

def test_trace::tracelink_has_ruleName():
    assert hasattr(trace::TraceLink, "ruleName")
    descriptor = None
    for klass in trace::TraceLink.__mro__:
        if "ruleName" in klass.__dict__:
            descriptor = klass.__dict__["ruleName"]
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
trace::EObject_strategy = st.builds(
    trace::EObject,
)
trace::TraceLink_strategy = st.builds(
    trace::TraceLink,
    ruleName=
        safe_text
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)

@given(instance=trace::EObject_strategy)
@settings(max_examples=50)
def test_trace::eobject_instantiation(instance):
    assert isinstance(instance, trace::EObject)

@given(instance=trace::TraceLink_strategy)
@settings(max_examples=50)
def test_trace::tracelink_instantiation(instance):
    assert isinstance(instance, trace::TraceLink)

@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_ruleName_type(instance):
    assert isinstance(instance.ruleName, str)


@given(instance=trace::TraceLink_strategy)
def test_trace::tracelink_ruleName_setter(instance):
    original = instance.ruleName
    instance.ruleName = original
    assert instance.ruleName == original

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

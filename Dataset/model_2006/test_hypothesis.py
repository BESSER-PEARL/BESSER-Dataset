import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Lqn2umlTrace_Trace,
    Lqn2umlTrace_TraceLink,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lqn2umltrace_trace_is_not_abstract():
    assert not inspect.isabstract(Lqn2umlTrace_Trace)


def test_lqn2umltrace_trace_constructor_exists():
    assert callable(Lqn2umlTrace_Trace.__init__)


def test_lqn2umltrace_trace_constructor_args():
    sig = inspect.signature(Lqn2umlTrace_Trace.__init__)
    params = list(sig.parameters.keys())



def test_lqn2umltrace_tracelink_is_not_abstract():
    assert not inspect.isabstract(Lqn2umlTrace_TraceLink)


def test_lqn2umltrace_tracelink_constructor_exists():
    assert callable(Lqn2umlTrace_TraceLink.__init__)


def test_lqn2umltrace_tracelink_constructor_args():
    sig = inspect.signature(Lqn2umlTrace_TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "sources" in params, "Missing parameter 'sources'"
    assert "targets" in params, "Missing parameter 'targets'"
    assert "description" in params, "Missing parameter 'description'"

def test_lqn2umltrace_tracelink_has_sources():
    assert hasattr(Lqn2umlTrace_TraceLink, "sources")
    descriptor = None
    for klass in Lqn2umlTrace_TraceLink.__mro__:
        if "sources" in klass.__dict__:
            descriptor = klass.__dict__["sources"]
            break
    assert isinstance(descriptor, property)

def test_lqn2umltrace_tracelink_has_targets():
    assert hasattr(Lqn2umlTrace_TraceLink, "targets")
    descriptor = None
    for klass in Lqn2umlTrace_TraceLink.__mro__:
        if "targets" in klass.__dict__:
            descriptor = klass.__dict__["targets"]
            break
    assert isinstance(descriptor, property)

def test_lqn2umltrace_tracelink_has_description():
    assert hasattr(Lqn2umlTrace_TraceLink, "description")
    descriptor = None
    for klass in Lqn2umlTrace_TraceLink.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)


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
Lqn2umlTrace_Trace_strategy = st.builds(
    Lqn2umlTrace_Trace,
)
Lqn2umlTrace_TraceLink_strategy = st.builds(
    Lqn2umlTrace_TraceLink,
    sources=
        safe_text,
    targets=
        safe_text,
    description=
        safe_text
)

@given(instance=Lqn2umlTrace_Trace_strategy)
@settings(max_examples=50)
def test_lqn2umltrace_trace_instantiation(instance):
    assert isinstance(instance, Lqn2umlTrace_Trace)

@given(instance=Lqn2umlTrace_TraceLink_strategy)
@settings(max_examples=50)
def test_lqn2umltrace_tracelink_instantiation(instance):
    assert isinstance(instance, Lqn2umlTrace_TraceLink)



@given(instance=Lqn2umlTrace_TraceLink_strategy)
def test_lqn2umltrace_tracelink_sources_setter(instance):
    original = instance.sources
    instance.sources = original
    assert instance.sources == original



@given(instance=Lqn2umlTrace_TraceLink_strategy)
def test_lqn2umltrace_tracelink_targets_setter(instance):
    original = instance.targets
    instance.targets = original
    assert instance.targets == original



@given(instance=Lqn2umlTrace_TraceLink_strategy)
def test_lqn2umltrace_tracelink_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

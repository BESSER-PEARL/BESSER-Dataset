import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Lqn2umlTrace::TraceLink,
    Lqn2umlTrace::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lqn2umltrace::tracelink_is_not_abstract():
    assert not inspect.isabstract(Lqn2umlTrace::TraceLink)


def test_lqn2umltrace::tracelink_constructor_exists():
    assert callable(Lqn2umlTrace::TraceLink.__init__)


def test_lqn2umltrace::tracelink_constructor_args():
    sig = inspect.signature(Lqn2umlTrace::TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "targets" in params, "Missing parameter 'targets'"
    assert "sources" in params, "Missing parameter 'sources'"

def test_lqn2umltrace::tracelink_has_description():
    assert hasattr(Lqn2umlTrace::TraceLink, "description")
    descriptor = None
    for klass in Lqn2umlTrace::TraceLink.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_lqn2umltrace::tracelink_has_targets():
    assert hasattr(Lqn2umlTrace::TraceLink, "targets")
    descriptor = None
    for klass in Lqn2umlTrace::TraceLink.__mro__:
        if "targets" in klass.__dict__:
            descriptor = klass.__dict__["targets"]
            break
    assert isinstance(descriptor, property)

def test_lqn2umltrace::tracelink_has_sources():
    assert hasattr(Lqn2umlTrace::TraceLink, "sources")
    descriptor = None
    for klass in Lqn2umlTrace::TraceLink.__mro__:
        if "sources" in klass.__dict__:
            descriptor = klass.__dict__["sources"]
            break
    assert isinstance(descriptor, property)



def test_lqn2umltrace::trace_is_not_abstract():
    assert not inspect.isabstract(Lqn2umlTrace::Trace)


def test_lqn2umltrace::trace_constructor_exists():
    assert callable(Lqn2umlTrace::Trace.__init__)


def test_lqn2umltrace::trace_constructor_args():
    sig = inspect.signature(Lqn2umlTrace::Trace.__init__)
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
Lqn2umlTrace::TraceLink_strategy = st.builds(
    Lqn2umlTrace::TraceLink,
    description=
        safe_text,
    targets=
        safe_text,
    sources=
        safe_text
)
Lqn2umlTrace::Trace_strategy = st.builds(
    Lqn2umlTrace::Trace,
)

@given(instance=Lqn2umlTrace::TraceLink_strategy)
@settings(max_examples=50)
def test_lqn2umltrace::tracelink_instantiation(instance):
    assert isinstance(instance, Lqn2umlTrace::TraceLink)

@given(instance=Lqn2umlTrace::TraceLink_strategy)
def test_lqn2umltrace::tracelink_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=Lqn2umlTrace::TraceLink_strategy)
def test_lqn2umltrace::tracelink_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Lqn2umlTrace::TraceLink_strategy)
def test_lqn2umltrace::tracelink_targets_type(instance):
    assert isinstance(instance.targets, str)


@given(instance=Lqn2umlTrace::TraceLink_strategy)
def test_lqn2umltrace::tracelink_targets_setter(instance):
    original = instance.targets
    instance.targets = original
    assert instance.targets == original

@given(instance=Lqn2umlTrace::TraceLink_strategy)
def test_lqn2umltrace::tracelink_sources_type(instance):
    assert isinstance(instance.sources, str)


@given(instance=Lqn2umlTrace::TraceLink_strategy)
def test_lqn2umltrace::tracelink_sources_setter(instance):
    original = instance.sources
    instance.sources = original
    assert instance.sources == original

@given(instance=Lqn2umlTrace::Trace_strategy)
@settings(max_examples=50)
def test_lqn2umltrace::trace_instantiation(instance):
    assert isinstance(instance, Lqn2umlTrace::Trace)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    traces::EObject,
    traces::Trace,
    traces::TraceSet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traces::eobject_is_not_abstract():
    assert not inspect.isabstract(traces::EObject)


def test_traces::eobject_constructor_exists():
    assert callable(traces::EObject.__init__)


def test_traces::eobject_constructor_args():
    sig = inspect.signature(traces::EObject.__init__)
    params = list(sig.parameters.keys())



def test_traces::trace_is_not_abstract():
    assert not inspect.isabstract(traces::Trace)


def test_traces::trace_constructor_exists():
    assert callable(traces::Trace.__init__)


def test_traces::trace_constructor_args():
    sig = inspect.signature(traces::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "rule" in params, "Missing parameter 'rule'"

def test_traces::trace_has_rule():
    assert hasattr(traces::Trace, "rule")
    descriptor = None
    for klass in traces::Trace.__mro__:
        if "rule" in klass.__dict__:
            descriptor = klass.__dict__["rule"]
            break
    assert isinstance(descriptor, property)



def test_traces::traceset_is_not_abstract():
    assert not inspect.isabstract(traces::TraceSet)


def test_traces::traceset_constructor_exists():
    assert callable(traces::TraceSet.__init__)


def test_traces::traceset_constructor_args():
    sig = inspect.signature(traces::TraceSet.__init__)
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
traces::EObject_strategy = st.builds(
    traces::EObject,
)
traces::Trace_strategy = st.builds(
    traces::Trace,
    rule=
        safe_text
)
traces::TraceSet_strategy = st.builds(
    traces::TraceSet,
)

@given(instance=traces::EObject_strategy)
@settings(max_examples=50)
def test_traces::eobject_instantiation(instance):
    assert isinstance(instance, traces::EObject)

@given(instance=traces::Trace_strategy)
@settings(max_examples=50)
def test_traces::trace_instantiation(instance):
    assert isinstance(instance, traces::Trace)

@given(instance=traces::Trace_strategy)
def test_traces::trace_rule_type(instance):
    assert isinstance(instance.rule, str)


@given(instance=traces::Trace_strategy)
def test_traces::trace_rule_setter(instance):
    original = instance.rule
    instance.rule = original
    assert instance.rule == original

@given(instance=traces::TraceSet_strategy)
@settings(max_examples=50)
def test_traces::traceset_instantiation(instance):
    assert isinstance(instance, traces::TraceSet)

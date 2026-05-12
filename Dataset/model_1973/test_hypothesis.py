import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    traces_EObject,
    traces_Trace,
    traces_TraceSet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traces_eobject_is_not_abstract():
    assert not inspect.isabstract(traces_EObject)


def test_traces_eobject_constructor_exists():
    assert callable(traces_EObject.__init__)


def test_traces_eobject_constructor_args():
    sig = inspect.signature(traces_EObject.__init__)
    params = list(sig.parameters.keys())



def test_traces_trace_is_not_abstract():
    assert not inspect.isabstract(traces_Trace)


def test_traces_trace_constructor_exists():
    assert callable(traces_Trace.__init__)


def test_traces_trace_constructor_args():
    sig = inspect.signature(traces_Trace.__init__)
    params = list(sig.parameters.keys())
    assert "rule" in params, "Missing parameter 'rule'"

def test_traces_trace_has_rule():
    assert hasattr(traces_Trace, "rule")
    descriptor = None
    for klass in traces_Trace.__mro__:
        if "rule" in klass.__dict__:
            descriptor = klass.__dict__["rule"]
            break
    assert isinstance(descriptor, property)



def test_traces_traceset_is_not_abstract():
    assert not inspect.isabstract(traces_TraceSet)


def test_traces_traceset_constructor_exists():
    assert callable(traces_TraceSet.__init__)


def test_traces_traceset_constructor_args():
    sig = inspect.signature(traces_TraceSet.__init__)
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
traces_EObject_strategy = st.builds(
    traces_EObject,
)
traces_Trace_strategy = st.builds(
    traces_Trace,
    rule=
        safe_text
)
traces_TraceSet_strategy = st.builds(
    traces_TraceSet,
)

@given(instance=traces_EObject_strategy)
@settings(max_examples=50)
def test_traces_eobject_instantiation(instance):
    assert isinstance(instance, traces_EObject)

@given(instance=traces_Trace_strategy)
@settings(max_examples=50)
def test_traces_trace_instantiation(instance):
    assert isinstance(instance, traces_Trace)



@given(instance=traces_Trace_strategy)
def test_traces_trace_rule_setter(instance):
    original = instance.rule
    instance.rule = original
    assert instance.rule == original

@given(instance=traces_TraceSet_strategy)
@settings(max_examples=50)
def test_traces_traceset_instantiation(instance):
    assert isinstance(instance, traces_TraceSet)

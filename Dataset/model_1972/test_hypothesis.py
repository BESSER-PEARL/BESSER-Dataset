import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    traces_TraceRepository,
    traces_EObject,
    traces_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traces_tracerepository_is_not_abstract():
    assert not inspect.isabstract(traces_TraceRepository)


def test_traces_tracerepository_constructor_exists():
    assert callable(traces_TraceRepository.__init__)


def test_traces_tracerepository_constructor_args():
    sig = inspect.signature(traces_TraceRepository.__init__)
    params = list(sig.parameters.keys())



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
    assert "Role" in params, "Missing parameter 'Role'"

def test_traces_trace_has_Role():
    assert hasattr(traces_Trace, "Role")
    descriptor = None
    for klass in traces_Trace.__mro__:
        if "Role" in klass.__dict__:
            descriptor = klass.__dict__["Role"]
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
traces_TraceRepository_strategy = st.builds(
    traces_TraceRepository,
)
traces_EObject_strategy = st.builds(
    traces_EObject,
)
traces_Trace_strategy = st.builds(
    traces_Trace,
    Role=
        safe_text
)

@given(instance=traces_TraceRepository_strategy)
@settings(max_examples=50)
def test_traces_tracerepository_instantiation(instance):
    assert isinstance(instance, traces_TraceRepository)

@given(instance=traces_EObject_strategy)
@settings(max_examples=50)
def test_traces_eobject_instantiation(instance):
    assert isinstance(instance, traces_EObject)

@given(instance=traces_Trace_strategy)
@settings(max_examples=50)
def test_traces_trace_instantiation(instance):
    assert isinstance(instance, traces_Trace)



@given(instance=traces_Trace_strategy)
def test_traces_trace_Role_setter(instance):
    original = instance.Role
    instance.Role = original
    assert instance.Role == original

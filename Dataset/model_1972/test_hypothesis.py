import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    traces::TraceRepository,
    traces::EObject,
    traces::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traces::tracerepository_is_not_abstract():
    assert not inspect.isabstract(traces::TraceRepository)


def test_traces::tracerepository_constructor_exists():
    assert callable(traces::TraceRepository.__init__)


def test_traces::tracerepository_constructor_args():
    sig = inspect.signature(traces::TraceRepository.__init__)
    params = list(sig.parameters.keys())



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
    assert "Role" in params, "Missing parameter 'Role'"

def test_traces::trace_has_Role():
    assert hasattr(traces::Trace, "Role")
    descriptor = None
    for klass in traces::Trace.__mro__:
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
traces::TraceRepository_strategy = st.builds(
    traces::TraceRepository,
)
traces::EObject_strategy = st.builds(
    traces::EObject,
)
traces::Trace_strategy = st.builds(
    traces::Trace,
    Role=
        safe_text
)

@given(instance=traces::TraceRepository_strategy)
@settings(max_examples=50)
def test_traces::tracerepository_instantiation(instance):
    assert isinstance(instance, traces::TraceRepository)

@given(instance=traces::EObject_strategy)
@settings(max_examples=50)
def test_traces::eobject_instantiation(instance):
    assert isinstance(instance, traces::EObject)

@given(instance=traces::Trace_strategy)
@settings(max_examples=50)
def test_traces::trace_instantiation(instance):
    assert isinstance(instance, traces::Trace)

@given(instance=traces::Trace_strategy)
def test_traces::trace_Role_type(instance):
    assert isinstance(instance.Role, str)


@given(instance=traces::Trace_strategy)
def test_traces::trace_Role_setter(instance):
    original = instance.Role
    instance.Role = original
    assert instance.Role == original

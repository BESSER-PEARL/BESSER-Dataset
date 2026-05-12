import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    trace_EObject,
    trace_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace_eobject_is_not_abstract():
    assert not inspect.isabstract(trace_EObject)


def test_trace_eobject_constructor_exists():
    assert callable(trace_EObject.__init__)


def test_trace_eobject_constructor_args():
    sig = inspect.signature(trace_EObject.__init__)
    params = list(sig.parameters.keys())



def test_trace_trace_is_not_abstract():
    assert not inspect.isabstract(trace_Trace)


def test_trace_trace_constructor_exists():
    assert callable(trace_Trace.__init__)


def test_trace_trace_constructor_args():
    sig = inspect.signature(trace_Trace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trace_trace_has_name():
    assert hasattr(trace_Trace, "name")
    descriptor = None
    for klass in trace_Trace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
trace_EObject_strategy = st.builds(
    trace_EObject,
)
trace_Trace_strategy = st.builds(
    trace_Trace,
    name=
        safe_text
)

@given(instance=trace_EObject_strategy)
@settings(max_examples=50)
def test_trace_eobject_instantiation(instance):
    assert isinstance(instance, trace_EObject)

@given(instance=trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, trace_Trace)



@given(instance=trace_Trace_strategy)
def test_trace_trace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

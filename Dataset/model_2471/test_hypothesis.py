import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleTrace_EObject,
    SimpleTrace_TraceLink,
    SimpleTrace_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletrace_eobject_is_not_abstract():
    assert not inspect.isabstract(SimpleTrace_EObject)


def test_simpletrace_eobject_constructor_exists():
    assert callable(SimpleTrace_EObject.__init__)


def test_simpletrace_eobject_constructor_args():
    sig = inspect.signature(SimpleTrace_EObject.__init__)
    params = list(sig.parameters.keys())



def test_simpletrace_tracelink_is_not_abstract():
    assert not inspect.isabstract(SimpleTrace_TraceLink)


def test_simpletrace_tracelink_constructor_exists():
    assert callable(SimpleTrace_TraceLink.__init__)


def test_simpletrace_tracelink_constructor_args():
    sig = inspect.signature(SimpleTrace_TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_simpletrace_tracelink_has_description():
    assert hasattr(SimpleTrace_TraceLink, "description")
    descriptor = None
    for klass in SimpleTrace_TraceLink.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_simpletrace_trace_is_not_abstract():
    assert not inspect.isabstract(SimpleTrace_Trace)


def test_simpletrace_trace_constructor_exists():
    assert callable(SimpleTrace_Trace.__init__)


def test_simpletrace_trace_constructor_args():
    sig = inspect.signature(SimpleTrace_Trace.__init__)
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
SimpleTrace_EObject_strategy = st.builds(
    SimpleTrace_EObject,
)
SimpleTrace_TraceLink_strategy = st.builds(
    SimpleTrace_TraceLink,
    description=
        safe_text
)
SimpleTrace_Trace_strategy = st.builds(
    SimpleTrace_Trace,
)

@given(instance=SimpleTrace_EObject_strategy)
@settings(max_examples=50)
def test_simpletrace_eobject_instantiation(instance):
    assert isinstance(instance, SimpleTrace_EObject)

@given(instance=SimpleTrace_TraceLink_strategy)
@settings(max_examples=50)
def test_simpletrace_tracelink_instantiation(instance):
    assert isinstance(instance, SimpleTrace_TraceLink)



@given(instance=SimpleTrace_TraceLink_strategy)
def test_simpletrace_tracelink_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=SimpleTrace_Trace_strategy)
@settings(max_examples=50)
def test_simpletrace_trace_instantiation(instance):
    assert isinstance(instance, SimpleTrace_Trace)

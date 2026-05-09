import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleTrace::EObject,
    SimpleTrace::TraceLink,
    SimpleTrace::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletrace::eobject_is_not_abstract():
    assert not inspect.isabstract(SimpleTrace::EObject)


def test_simpletrace::eobject_constructor_exists():
    assert callable(SimpleTrace::EObject.__init__)


def test_simpletrace::eobject_constructor_args():
    sig = inspect.signature(SimpleTrace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_simpletrace::tracelink_is_not_abstract():
    assert not inspect.isabstract(SimpleTrace::TraceLink)


def test_simpletrace::tracelink_constructor_exists():
    assert callable(SimpleTrace::TraceLink.__init__)


def test_simpletrace::tracelink_constructor_args():
    sig = inspect.signature(SimpleTrace::TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_simpletrace::tracelink_has_description():
    assert hasattr(SimpleTrace::TraceLink, "description")
    descriptor = None
    for klass in SimpleTrace::TraceLink.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_simpletrace::trace_is_not_abstract():
    assert not inspect.isabstract(SimpleTrace::Trace)


def test_simpletrace::trace_constructor_exists():
    assert callable(SimpleTrace::Trace.__init__)


def test_simpletrace::trace_constructor_args():
    sig = inspect.signature(SimpleTrace::Trace.__init__)
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
SimpleTrace::EObject_strategy = st.builds(
    SimpleTrace::EObject,
)
SimpleTrace::TraceLink_strategy = st.builds(
    SimpleTrace::TraceLink,
    description=
        safe_text
)
SimpleTrace::Trace_strategy = st.builds(
    SimpleTrace::Trace,
)

@given(instance=SimpleTrace::EObject_strategy)
@settings(max_examples=50)
def test_simpletrace::eobject_instantiation(instance):
    assert isinstance(instance, SimpleTrace::EObject)

@given(instance=SimpleTrace::TraceLink_strategy)
@settings(max_examples=50)
def test_simpletrace::tracelink_instantiation(instance):
    assert isinstance(instance, SimpleTrace::TraceLink)

@given(instance=SimpleTrace::TraceLink_strategy)
def test_simpletrace::tracelink_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=SimpleTrace::TraceLink_strategy)
def test_simpletrace::tracelink_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=SimpleTrace::Trace_strategy)
@settings(max_examples=50)
def test_simpletrace::trace_instantiation(instance):
    assert isinstance(instance, SimpleTrace::Trace)

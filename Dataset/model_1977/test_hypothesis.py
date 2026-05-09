import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EtlSimpleTrace::EObject,
    EtlSimpleTrace::TraceLink,
    EtlSimpleTrace::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_etlsimpletrace::eobject_is_not_abstract():
    assert not inspect.isabstract(EtlSimpleTrace::EObject)


def test_etlsimpletrace::eobject_constructor_exists():
    assert callable(EtlSimpleTrace::EObject.__init__)


def test_etlsimpletrace::eobject_constructor_args():
    sig = inspect.signature(EtlSimpleTrace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_etlsimpletrace::tracelink_is_not_abstract():
    assert not inspect.isabstract(EtlSimpleTrace::TraceLink)


def test_etlsimpletrace::tracelink_constructor_exists():
    assert callable(EtlSimpleTrace::TraceLink.__init__)


def test_etlsimpletrace::tracelink_constructor_args():
    sig = inspect.signature(EtlSimpleTrace::TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_etlsimpletrace::tracelink_has_description():
    assert hasattr(EtlSimpleTrace::TraceLink, "description")
    descriptor = None
    for klass in EtlSimpleTrace::TraceLink.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_etlsimpletrace::trace_is_not_abstract():
    assert not inspect.isabstract(EtlSimpleTrace::Trace)


def test_etlsimpletrace::trace_constructor_exists():
    assert callable(EtlSimpleTrace::Trace.__init__)


def test_etlsimpletrace::trace_constructor_args():
    sig = inspect.signature(EtlSimpleTrace::Trace.__init__)
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
EtlSimpleTrace::EObject_strategy = st.builds(
    EtlSimpleTrace::EObject,
)
EtlSimpleTrace::TraceLink_strategy = st.builds(
    EtlSimpleTrace::TraceLink,
    description=
        safe_text
)
EtlSimpleTrace::Trace_strategy = st.builds(
    EtlSimpleTrace::Trace,
)

@given(instance=EtlSimpleTrace::EObject_strategy)
@settings(max_examples=50)
def test_etlsimpletrace::eobject_instantiation(instance):
    assert isinstance(instance, EtlSimpleTrace::EObject)

@given(instance=EtlSimpleTrace::TraceLink_strategy)
@settings(max_examples=50)
def test_etlsimpletrace::tracelink_instantiation(instance):
    assert isinstance(instance, EtlSimpleTrace::TraceLink)

@given(instance=EtlSimpleTrace::TraceLink_strategy)
def test_etlsimpletrace::tracelink_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=EtlSimpleTrace::TraceLink_strategy)
def test_etlsimpletrace::tracelink_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=EtlSimpleTrace::Trace_strategy)
@settings(max_examples=50)
def test_etlsimpletrace::trace_instantiation(instance):
    assert isinstance(instance, EtlSimpleTrace::Trace)

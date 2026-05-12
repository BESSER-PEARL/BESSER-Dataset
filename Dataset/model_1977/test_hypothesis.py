import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EtlSimpleTrace_EObject,
    EtlSimpleTrace_TraceLink,
    EtlSimpleTrace_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_etlsimpletrace_eobject_is_not_abstract():
    assert not inspect.isabstract(EtlSimpleTrace_EObject)


def test_etlsimpletrace_eobject_constructor_exists():
    assert callable(EtlSimpleTrace_EObject.__init__)


def test_etlsimpletrace_eobject_constructor_args():
    sig = inspect.signature(EtlSimpleTrace_EObject.__init__)
    params = list(sig.parameters.keys())



def test_etlsimpletrace_tracelink_is_not_abstract():
    assert not inspect.isabstract(EtlSimpleTrace_TraceLink)


def test_etlsimpletrace_tracelink_constructor_exists():
    assert callable(EtlSimpleTrace_TraceLink.__init__)


def test_etlsimpletrace_tracelink_constructor_args():
    sig = inspect.signature(EtlSimpleTrace_TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_etlsimpletrace_tracelink_has_description():
    assert hasattr(EtlSimpleTrace_TraceLink, "description")
    descriptor = None
    for klass in EtlSimpleTrace_TraceLink.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_etlsimpletrace_trace_is_not_abstract():
    assert not inspect.isabstract(EtlSimpleTrace_Trace)


def test_etlsimpletrace_trace_constructor_exists():
    assert callable(EtlSimpleTrace_Trace.__init__)


def test_etlsimpletrace_trace_constructor_args():
    sig = inspect.signature(EtlSimpleTrace_Trace.__init__)
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
EtlSimpleTrace_EObject_strategy = st.builds(
    EtlSimpleTrace_EObject,
)
EtlSimpleTrace_TraceLink_strategy = st.builds(
    EtlSimpleTrace_TraceLink,
    description=
        safe_text
)
EtlSimpleTrace_Trace_strategy = st.builds(
    EtlSimpleTrace_Trace,
)

@given(instance=EtlSimpleTrace_EObject_strategy)
@settings(max_examples=50)
def test_etlsimpletrace_eobject_instantiation(instance):
    assert isinstance(instance, EtlSimpleTrace_EObject)

@given(instance=EtlSimpleTrace_TraceLink_strategy)
@settings(max_examples=50)
def test_etlsimpletrace_tracelink_instantiation(instance):
    assert isinstance(instance, EtlSimpleTrace_TraceLink)



@given(instance=EtlSimpleTrace_TraceLink_strategy)
def test_etlsimpletrace_tracelink_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=EtlSimpleTrace_Trace_strategy)
@settings(max_examples=50)
def test_etlsimpletrace_trace_instantiation(instance):
    assert isinstance(instance, EtlSimpleTrace_Trace)

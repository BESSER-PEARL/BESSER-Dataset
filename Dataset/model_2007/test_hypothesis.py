import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Trace_Trace,
    Trace_TraceLink,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace_trace_is_not_abstract():
    assert not inspect.isabstract(Trace_Trace)


def test_trace_trace_constructor_exists():
    assert callable(Trace_Trace.__init__)


def test_trace_trace_constructor_args():
    sig = inspect.signature(Trace_Trace.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_trace_trace_has_description():
    assert hasattr(Trace_Trace, "description")
    descriptor = None
    for klass in Trace_Trace.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_trace_tracelink_is_not_abstract():
    assert not inspect.isabstract(Trace_TraceLink)


def test_trace_tracelink_constructor_exists():
    assert callable(Trace_TraceLink.__init__)


def test_trace_tracelink_constructor_args():
    sig = inspect.signature(Trace_TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "sourceName" in params, "Missing parameter 'sourceName'"
    assert "targetName" in params, "Missing parameter 'targetName'"
    assert "sourceType" in params, "Missing parameter 'sourceType'"
    assert "targetType" in params, "Missing parameter 'targetType'"

def test_trace_tracelink_has_description():
    assert hasattr(Trace_TraceLink, "description")
    descriptor = None
    for klass in Trace_TraceLink.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_trace_tracelink_has_sourceName():
    assert hasattr(Trace_TraceLink, "sourceName")
    descriptor = None
    for klass in Trace_TraceLink.__mro__:
        if "sourceName" in klass.__dict__:
            descriptor = klass.__dict__["sourceName"]
            break
    assert isinstance(descriptor, property)

def test_trace_tracelink_has_targetName():
    assert hasattr(Trace_TraceLink, "targetName")
    descriptor = None
    for klass in Trace_TraceLink.__mro__:
        if "targetName" in klass.__dict__:
            descriptor = klass.__dict__["targetName"]
            break
    assert isinstance(descriptor, property)

def test_trace_tracelink_has_sourceType():
    assert hasattr(Trace_TraceLink, "sourceType")
    descriptor = None
    for klass in Trace_TraceLink.__mro__:
        if "sourceType" in klass.__dict__:
            descriptor = klass.__dict__["sourceType"]
            break
    assert isinstance(descriptor, property)

def test_trace_tracelink_has_targetType():
    assert hasattr(Trace_TraceLink, "targetType")
    descriptor = None
    for klass in Trace_TraceLink.__mro__:
        if "targetType" in klass.__dict__:
            descriptor = klass.__dict__["targetType"]
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
Trace_Trace_strategy = st.builds(
    Trace_Trace,
    description=
        safe_text
)
Trace_TraceLink_strategy = st.builds(
    Trace_TraceLink,
    description=
        safe_text,
    sourceName=
        safe_text,
    targetName=
        safe_text,
    sourceType=
        safe_text,
    targetType=
        safe_text
)

@given(instance=Trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, Trace_Trace)



@given(instance=Trace_Trace_strategy)
def test_trace_trace_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Trace_TraceLink_strategy)
@settings(max_examples=50)
def test_trace_tracelink_instantiation(instance):
    assert isinstance(instance, Trace_TraceLink)



@given(instance=Trace_TraceLink_strategy)
def test_trace_tracelink_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Trace_TraceLink_strategy)
def test_trace_tracelink_sourceName_setter(instance):
    original = instance.sourceName
    instance.sourceName = original
    assert instance.sourceName == original



@given(instance=Trace_TraceLink_strategy)
def test_trace_tracelink_targetName_setter(instance):
    original = instance.targetName
    instance.targetName = original
    assert instance.targetName == original



@given(instance=Trace_TraceLink_strategy)
def test_trace_tracelink_sourceType_setter(instance):
    original = instance.sourceType
    instance.sourceType = original
    assert instance.sourceType == original



@given(instance=Trace_TraceLink_strategy)
def test_trace_tracelink_targetType_setter(instance):
    original = instance.targetType
    instance.targetType = original
    assert instance.targetType == original

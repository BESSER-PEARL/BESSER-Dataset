import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Trace::Trace,
    Trace::TraceLink,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(Trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(Trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(Trace::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_trace::trace_has_description():
    assert hasattr(Trace::Trace, "description")
    descriptor = None
    for klass in Trace::Trace.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_trace::tracelink_is_not_abstract():
    assert not inspect.isabstract(Trace::TraceLink)


def test_trace::tracelink_constructor_exists():
    assert callable(Trace::TraceLink.__init__)


def test_trace::tracelink_constructor_args():
    sig = inspect.signature(Trace::TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "targetType" in params, "Missing parameter 'targetType'"
    assert "sourceName" in params, "Missing parameter 'sourceName'"
    assert "targetName" in params, "Missing parameter 'targetName'"
    assert "description" in params, "Missing parameter 'description'"
    assert "sourceType" in params, "Missing parameter 'sourceType'"

def test_trace::tracelink_has_targetType():
    assert hasattr(Trace::TraceLink, "targetType")
    descriptor = None
    for klass in Trace::TraceLink.__mro__:
        if "targetType" in klass.__dict__:
            descriptor = klass.__dict__["targetType"]
            break
    assert isinstance(descriptor, property)

def test_trace::tracelink_has_sourceName():
    assert hasattr(Trace::TraceLink, "sourceName")
    descriptor = None
    for klass in Trace::TraceLink.__mro__:
        if "sourceName" in klass.__dict__:
            descriptor = klass.__dict__["sourceName"]
            break
    assert isinstance(descriptor, property)

def test_trace::tracelink_has_targetName():
    assert hasattr(Trace::TraceLink, "targetName")
    descriptor = None
    for klass in Trace::TraceLink.__mro__:
        if "targetName" in klass.__dict__:
            descriptor = klass.__dict__["targetName"]
            break
    assert isinstance(descriptor, property)

def test_trace::tracelink_has_description():
    assert hasattr(Trace::TraceLink, "description")
    descriptor = None
    for klass in Trace::TraceLink.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_trace::tracelink_has_sourceType():
    assert hasattr(Trace::TraceLink, "sourceType")
    descriptor = None
    for klass in Trace::TraceLink.__mro__:
        if "sourceType" in klass.__dict__:
            descriptor = klass.__dict__["sourceType"]
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
Trace::Trace_strategy = st.builds(
    Trace::Trace,
    description=
        safe_text
)
Trace::TraceLink_strategy = st.builds(
    Trace::TraceLink,
    targetType=
        safe_text,
    sourceName=
        safe_text,
    targetName=
        safe_text,
    description=
        safe_text,
    sourceType=
        safe_text
)

@given(instance=Trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, Trace::Trace)

@given(instance=Trace::Trace_strategy)
def test_trace::trace_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=Trace::Trace_strategy)
def test_trace::trace_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Trace::TraceLink_strategy)
@settings(max_examples=50)
def test_trace::tracelink_instantiation(instance):
    assert isinstance(instance, Trace::TraceLink)

@given(instance=Trace::TraceLink_strategy)
def test_trace::tracelink_targetType_type(instance):
    assert isinstance(instance.targetType, str)


@given(instance=Trace::TraceLink_strategy)
def test_trace::tracelink_targetType_setter(instance):
    original = instance.targetType
    instance.targetType = original
    assert instance.targetType == original

@given(instance=Trace::TraceLink_strategy)
def test_trace::tracelink_sourceName_type(instance):
    assert isinstance(instance.sourceName, str)


@given(instance=Trace::TraceLink_strategy)
def test_trace::tracelink_sourceName_setter(instance):
    original = instance.sourceName
    instance.sourceName = original
    assert instance.sourceName == original

@given(instance=Trace::TraceLink_strategy)
def test_trace::tracelink_targetName_type(instance):
    assert isinstance(instance.targetName, str)


@given(instance=Trace::TraceLink_strategy)
def test_trace::tracelink_targetName_setter(instance):
    original = instance.targetName
    instance.targetName = original
    assert instance.targetName == original

@given(instance=Trace::TraceLink_strategy)
def test_trace::tracelink_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=Trace::TraceLink_strategy)
def test_trace::tracelink_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Trace::TraceLink_strategy)
def test_trace::tracelink_sourceType_type(instance):
    assert isinstance(instance.sourceType, str)


@given(instance=Trace::TraceLink_strategy)
def test_trace::tracelink_sourceType_setter(instance):
    original = instance.sourceType
    instance.sourceType = original
    assert instance.sourceType == original

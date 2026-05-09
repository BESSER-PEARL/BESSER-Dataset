import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    traces::EObject,
    traces::TraceElement,
    traces::Model,
    traces::Trace,
    traces::TraceRecord,
    ParameterType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traces::eobject_is_not_abstract():
    assert not inspect.isabstract(traces::EObject)


def test_traces::eobject_constructor_exists():
    assert callable(traces::EObject.__init__)


def test_traces::eobject_constructor_args():
    sig = inspect.signature(traces::EObject.__init__)
    params = list(sig.parameters.keys())



def test_traces::traceelement_is_not_abstract():
    assert not inspect.isabstract(traces::TraceElement)


def test_traces::traceelement_constructor_exists():
    assert callable(traces::TraceElement.__init__)


def test_traces::traceelement_constructor_args():
    sig = inspect.signature(traces::TraceElement.__init__)
    params = list(sig.parameters.keys())
    assert "traceType" in params, "Missing parameter 'traceType'"
    assert "value" in params, "Missing parameter 'value'"
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_traces::traceelement_has_traceType():
    assert hasattr(traces::TraceElement, "traceType")
    descriptor = None
    for klass in traces::TraceElement.__mro__:
        if "traceType" in klass.__dict__:
            descriptor = klass.__dict__["traceType"]
            break
    assert isinstance(descriptor, property)

def test_traces::traceelement_has_value():
    assert hasattr(traces::TraceElement, "value")
    descriptor = None
    for klass in traces::TraceElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_traces::traceelement_has_typeName():
    assert hasattr(traces::TraceElement, "typeName")
    descriptor = None
    for klass in traces::TraceElement.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_traces::model_is_not_abstract():
    assert not inspect.isabstract(traces::Model)


def test_traces::model_constructor_exists():
    assert callable(traces::Model.__init__)


def test_traces::model_constructor_args():
    sig = inspect.signature(traces::Model.__init__)
    params = list(sig.parameters.keys())
    assert "uriModel" in params, "Missing parameter 'uriModel'"

def test_traces::model_has_uriModel():
    assert hasattr(traces::Model, "uriModel")
    descriptor = None
    for klass in traces::Model.__mro__:
        if "uriModel" in klass.__dict__:
            descriptor = klass.__dict__["uriModel"]
            break
    assert isinstance(descriptor, property)



def test_traces::trace_is_not_abstract():
    assert not inspect.isabstract(traces::Trace)


def test_traces::trace_constructor_exists():
    assert callable(traces::Trace.__init__)


def test_traces::trace_constructor_args():
    sig = inspect.signature(traces::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "ruleName" in params, "Missing parameter 'ruleName'"
    assert "ruleInfo" in params, "Missing parameter 'ruleInfo'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"

def test_traces::trace_has_ruleName():
    assert hasattr(traces::Trace, "ruleName")
    descriptor = None
    for klass in traces::Trace.__mro__:
        if "ruleName" in klass.__dict__:
            descriptor = klass.__dict__["ruleName"]
            break
    assert isinstance(descriptor, property)

def test_traces::trace_has_ruleInfo():
    assert hasattr(traces::Trace, "ruleInfo")
    descriptor = None
    for klass in traces::Trace.__mro__:
        if "ruleInfo" in klass.__dict__:
            descriptor = klass.__dict__["ruleInfo"]
            break
    assert isinstance(descriptor, property)

def test_traces::trace_has_timestamp():
    assert hasattr(traces::Trace, "timestamp")
    descriptor = None
    for klass in traces::Trace.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)



def test_traces::tracerecord_is_not_abstract():
    assert not inspect.isabstract(traces::TraceRecord)


def test_traces::tracerecord_constructor_exists():
    assert callable(traces::TraceRecord.__init__)


def test_traces::tracerecord_constructor_args():
    sig = inspect.signature(traces::TraceRecord.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_traces::tracerecord_has_name():
    assert hasattr(traces::TraceRecord, "name")
    descriptor = None
    for klass in traces::TraceRecord.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_parametertype_exists():
    # Check that the Enumeration exists
    assert ParameterType is not None

def test_parametertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterType]
    expected_literals = [
        "target",
        "source",
        "used",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterType"


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
traces::EObject_strategy = st.builds(
    traces::EObject,
)
traces::TraceElement_strategy = st.builds(
    traces::TraceElement,
    traceType=
        safe_text,
    value=
        safe_text,
    typeName=
        safe_text
)
traces::Model_strategy = st.builds(
    traces::Model,
    uriModel=
        safe_text
)
traces::Trace_strategy = st.builds(
    traces::Trace,
    ruleName=
        safe_text,
    ruleInfo=
        safe_text,
    timestamp=
        safe_text
)
traces::TraceRecord_strategy = st.builds(
    traces::TraceRecord,
    name=
        safe_text
)

@given(instance=traces::EObject_strategy)
@settings(max_examples=50)
def test_traces::eobject_instantiation(instance):
    assert isinstance(instance, traces::EObject)

@given(instance=traces::TraceElement_strategy)
@settings(max_examples=50)
def test_traces::traceelement_instantiation(instance):
    assert isinstance(instance, traces::TraceElement)

@given(instance=traces::TraceElement_strategy)
def test_traces::traceelement_traceType_type(instance):
    assert isinstance(instance.traceType, str)


@given(instance=traces::TraceElement_strategy)
def test_traces::traceelement_traceType_setter(instance):
    original = instance.traceType
    instance.traceType = original
    assert instance.traceType == original

@given(instance=traces::TraceElement_strategy)
def test_traces::traceelement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=traces::TraceElement_strategy)
def test_traces::traceelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=traces::TraceElement_strategy)
def test_traces::traceelement_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=traces::TraceElement_strategy)
def test_traces::traceelement_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=traces::Model_strategy)
@settings(max_examples=50)
def test_traces::model_instantiation(instance):
    assert isinstance(instance, traces::Model)

@given(instance=traces::Model_strategy)
def test_traces::model_uriModel_type(instance):
    assert isinstance(instance.uriModel, str)


@given(instance=traces::Model_strategy)
def test_traces::model_uriModel_setter(instance):
    original = instance.uriModel
    instance.uriModel = original
    assert instance.uriModel == original

@given(instance=traces::Trace_strategy)
@settings(max_examples=50)
def test_traces::trace_instantiation(instance):
    assert isinstance(instance, traces::Trace)

@given(instance=traces::Trace_strategy)
def test_traces::trace_ruleName_type(instance):
    assert isinstance(instance.ruleName, str)


@given(instance=traces::Trace_strategy)
def test_traces::trace_ruleName_setter(instance):
    original = instance.ruleName
    instance.ruleName = original
    assert instance.ruleName == original

@given(instance=traces::Trace_strategy)
def test_traces::trace_ruleInfo_type(instance):
    assert isinstance(instance.ruleInfo, str)


@given(instance=traces::Trace_strategy)
def test_traces::trace_ruleInfo_setter(instance):
    original = instance.ruleInfo
    instance.ruleInfo = original
    assert instance.ruleInfo == original

@given(instance=traces::Trace_strategy)
def test_traces::trace_timestamp_type(instance):
    assert isinstance(instance.timestamp, str)


@given(instance=traces::Trace_strategy)
def test_traces::trace_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=traces::TraceRecord_strategy)
@settings(max_examples=50)
def test_traces::tracerecord_instantiation(instance):
    assert isinstance(instance, traces::TraceRecord)

@given(instance=traces::TraceRecord_strategy)
def test_traces::tracerecord_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=traces::TraceRecord_strategy)
def test_traces::tracerecord_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

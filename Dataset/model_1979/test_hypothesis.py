import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    traces_EObject,
    traces_TraceElement,
    traces_Model,
    traces_Trace,
    traces_TraceRecord,
    ParameterType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traces_eobject_is_not_abstract():
    assert not inspect.isabstract(traces_EObject)


def test_traces_eobject_constructor_exists():
    assert callable(traces_EObject.__init__)


def test_traces_eobject_constructor_args():
    sig = inspect.signature(traces_EObject.__init__)
    params = list(sig.parameters.keys())



def test_traces_traceelement_is_not_abstract():
    assert not inspect.isabstract(traces_TraceElement)


def test_traces_traceelement_constructor_exists():
    assert callable(traces_TraceElement.__init__)


def test_traces_traceelement_constructor_args():
    sig = inspect.signature(traces_TraceElement.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "value" in params, "Missing parameter 'value'"
    assert "traceType" in params, "Missing parameter 'traceType'"

def test_traces_traceelement_has_typeName():
    assert hasattr(traces_TraceElement, "typeName")
    descriptor = None
    for klass in traces_TraceElement.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_traces_traceelement_has_value():
    assert hasattr(traces_TraceElement, "value")
    descriptor = None
    for klass in traces_TraceElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_traces_traceelement_has_traceType():
    assert hasattr(traces_TraceElement, "traceType")
    descriptor = None
    for klass in traces_TraceElement.__mro__:
        if "traceType" in klass.__dict__:
            descriptor = klass.__dict__["traceType"]
            break
    assert isinstance(descriptor, property)



def test_traces_model_is_not_abstract():
    assert not inspect.isabstract(traces_Model)


def test_traces_model_constructor_exists():
    assert callable(traces_Model.__init__)


def test_traces_model_constructor_args():
    sig = inspect.signature(traces_Model.__init__)
    params = list(sig.parameters.keys())
    assert "uriModel" in params, "Missing parameter 'uriModel'"

def test_traces_model_has_uriModel():
    assert hasattr(traces_Model, "uriModel")
    descriptor = None
    for klass in traces_Model.__mro__:
        if "uriModel" in klass.__dict__:
            descriptor = klass.__dict__["uriModel"]
            break
    assert isinstance(descriptor, property)



def test_traces_trace_is_not_abstract():
    assert not inspect.isabstract(traces_Trace)


def test_traces_trace_constructor_exists():
    assert callable(traces_Trace.__init__)


def test_traces_trace_constructor_args():
    sig = inspect.signature(traces_Trace.__init__)
    params = list(sig.parameters.keys())
    assert "ruleInfo" in params, "Missing parameter 'ruleInfo'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "ruleName" in params, "Missing parameter 'ruleName'"

def test_traces_trace_has_ruleInfo():
    assert hasattr(traces_Trace, "ruleInfo")
    descriptor = None
    for klass in traces_Trace.__mro__:
        if "ruleInfo" in klass.__dict__:
            descriptor = klass.__dict__["ruleInfo"]
            break
    assert isinstance(descriptor, property)

def test_traces_trace_has_timestamp():
    assert hasattr(traces_Trace, "timestamp")
    descriptor = None
    for klass in traces_Trace.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_traces_trace_has_ruleName():
    assert hasattr(traces_Trace, "ruleName")
    descriptor = None
    for klass in traces_Trace.__mro__:
        if "ruleName" in klass.__dict__:
            descriptor = klass.__dict__["ruleName"]
            break
    assert isinstance(descriptor, property)



def test_traces_tracerecord_is_not_abstract():
    assert not inspect.isabstract(traces_TraceRecord)


def test_traces_tracerecord_constructor_exists():
    assert callable(traces_TraceRecord.__init__)


def test_traces_tracerecord_constructor_args():
    sig = inspect.signature(traces_TraceRecord.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_traces_tracerecord_has_name():
    assert hasattr(traces_TraceRecord, "name")
    descriptor = None
    for klass in traces_TraceRecord.__mro__:
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
        "used",
        "source",
        "target",
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
traces_EObject_strategy = st.builds(
    traces_EObject,
)
traces_TraceElement_strategy = st.builds(
    traces_TraceElement,
    typeName=
        safe_text,
    value=
        safe_text,
    traceType=
        safe_text
)
traces_Model_strategy = st.builds(
    traces_Model,
    uriModel=
        safe_text
)
traces_Trace_strategy = st.builds(
    traces_Trace,
    ruleInfo=
        safe_text,
    timestamp=
        safe_text,
    ruleName=
        safe_text
)
traces_TraceRecord_strategy = st.builds(
    traces_TraceRecord,
    name=
        safe_text
)

@given(instance=traces_EObject_strategy)
@settings(max_examples=50)
def test_traces_eobject_instantiation(instance):
    assert isinstance(instance, traces_EObject)

@given(instance=traces_TraceElement_strategy)
@settings(max_examples=50)
def test_traces_traceelement_instantiation(instance):
    assert isinstance(instance, traces_TraceElement)



@given(instance=traces_TraceElement_strategy)
def test_traces_traceelement_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original



@given(instance=traces_TraceElement_strategy)
def test_traces_traceelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=traces_TraceElement_strategy)
def test_traces_traceelement_traceType_setter(instance):
    original = instance.traceType
    instance.traceType = original
    assert instance.traceType == original

@given(instance=traces_Model_strategy)
@settings(max_examples=50)
def test_traces_model_instantiation(instance):
    assert isinstance(instance, traces_Model)



@given(instance=traces_Model_strategy)
def test_traces_model_uriModel_setter(instance):
    original = instance.uriModel
    instance.uriModel = original
    assert instance.uriModel == original

@given(instance=traces_Trace_strategy)
@settings(max_examples=50)
def test_traces_trace_instantiation(instance):
    assert isinstance(instance, traces_Trace)



@given(instance=traces_Trace_strategy)
def test_traces_trace_ruleInfo_setter(instance):
    original = instance.ruleInfo
    instance.ruleInfo = original
    assert instance.ruleInfo == original



@given(instance=traces_Trace_strategy)
def test_traces_trace_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original



@given(instance=traces_Trace_strategy)
def test_traces_trace_ruleName_setter(instance):
    original = instance.ruleName
    instance.ruleName = original
    assert instance.ruleName == original

@given(instance=traces_TraceRecord_strategy)
@settings(max_examples=50)
def test_traces_tracerecord_instantiation(instance):
    assert isinstance(instance, traces_TraceRecord)



@given(instance=traces_TraceRecord_strategy)
def test_traces_tracerecord_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

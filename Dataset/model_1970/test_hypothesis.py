import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TraceItem,
    trace::M2CTraceItem,
    trace::M2MTraceItem,
    trace::EObject,
    trace::TraceItem,
    trace::TraceBySource,
    trace::TraceList,
    trace::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traceitem_is_not_abstract():
    assert not inspect.isabstract(TraceItem)


def test_traceitem_constructor_exists():
    assert callable(TraceItem.__init__)


def test_traceitem_constructor_args():
    sig = inspect.signature(TraceItem.__init__)
    params = list(sig.parameters.keys())



def test_trace::m2ctraceitem_is_not_abstract():
    assert not inspect.isabstract(trace::M2CTraceItem)


def test_trace::m2ctraceitem_constructor_exists():
    assert callable(trace::M2CTraceItem.__init__)


def test_trace::m2ctraceitem_constructor_args():
    sig = inspect.signature(trace::M2CTraceItem.__init__)
    params = list(sig.parameters.keys())
    assert "targetFile" in params, "Missing parameter 'targetFile'"
    assert "token" in params, "Missing parameter 'token'"

def test_trace::m2ctraceitem_has_targetFile():
    assert hasattr(trace::M2CTraceItem, "targetFile")
    descriptor = None
    for klass in trace::M2CTraceItem.__mro__:
        if "targetFile" in klass.__dict__:
            descriptor = klass.__dict__["targetFile"]
            break
    assert isinstance(descriptor, property)

def test_trace::m2ctraceitem_has_token():
    assert hasattr(trace::M2CTraceItem, "token")
    descriptor = None
    for klass in trace::M2CTraceItem.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_trace::m2mtraceitem_is_not_abstract():
    assert not inspect.isabstract(trace::M2MTraceItem)


def test_trace::m2mtraceitem_constructor_exists():
    assert callable(trace::M2MTraceItem.__init__)


def test_trace::m2mtraceitem_constructor_args():
    sig = inspect.signature(trace::M2MTraceItem.__init__)
    params = list(sig.parameters.keys())



def test_trace::eobject_is_not_abstract():
    assert not inspect.isabstract(trace::EObject)


def test_trace::eobject_constructor_exists():
    assert callable(trace::EObject.__init__)


def test_trace::eobject_constructor_args():
    sig = inspect.signature(trace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_trace::traceitem_is_not_abstract():
    assert not inspect.isabstract(trace::TraceItem)


def test_trace::traceitem_constructor_exists():
    assert callable(trace::TraceItem.__init__)


def test_trace::traceitem_constructor_args():
    sig = inspect.signature(trace::TraceItem.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_trace::traceitem_has_kind():
    assert hasattr(trace::TraceItem, "kind")
    descriptor = None
    for klass in trace::TraceItem.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_trace::tracebysource_is_not_abstract():
    assert not inspect.isabstract(trace::TraceBySource)


def test_trace::tracebysource_constructor_exists():
    assert callable(trace::TraceBySource.__init__)


def test_trace::tracebysource_constructor_args():
    sig = inspect.signature(trace::TraceBySource.__init__)
    params = list(sig.parameters.keys())



def test_trace::tracelist_is_not_abstract():
    assert not inspect.isabstract(trace::TraceList)


def test_trace::tracelist_constructor_exists():
    assert callable(trace::TraceList.__init__)


def test_trace::tracelist_constructor_args():
    sig = inspect.signature(trace::TraceList.__init__)
    params = list(sig.parameters.keys())



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
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
TraceItem_strategy = st.builds(
    TraceItem,
)
trace::M2CTraceItem_strategy = st.builds(
    trace::M2CTraceItem,
    targetFile=
        safe_text,
    token=
        safe_text
)
trace::M2MTraceItem_strategy = st.builds(
    trace::M2MTraceItem,
)
trace::EObject_strategy = st.builds(
    trace::EObject,
)
trace::TraceItem_strategy = st.builds(
    trace::TraceItem,
    kind=
        safe_text
)
trace::TraceBySource_strategy = st.builds(
    trace::TraceBySource,
)
trace::TraceList_strategy = st.builds(
    trace::TraceList,
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)

@given(instance=TraceItem_strategy)
@settings(max_examples=50)
def test_traceitem_instantiation(instance):
    assert isinstance(instance, TraceItem)

@given(instance=trace::M2CTraceItem_strategy)
@settings(max_examples=50)
def test_trace::m2ctraceitem_instantiation(instance):
    assert isinstance(instance, trace::M2CTraceItem)

@given(instance=trace::M2CTraceItem_strategy)
def test_trace::m2ctraceitem_targetFile_type(instance):
    assert isinstance(instance.targetFile, str)


@given(instance=trace::M2CTraceItem_strategy)
def test_trace::m2ctraceitem_targetFile_setter(instance):
    original = instance.targetFile
    instance.targetFile = original
    assert instance.targetFile == original

@given(instance=trace::M2CTraceItem_strategy)
def test_trace::m2ctraceitem_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=trace::M2CTraceItem_strategy)
def test_trace::m2ctraceitem_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=trace::M2MTraceItem_strategy)
@settings(max_examples=50)
def test_trace::m2mtraceitem_instantiation(instance):
    assert isinstance(instance, trace::M2MTraceItem)

@given(instance=trace::EObject_strategy)
@settings(max_examples=50)
def test_trace::eobject_instantiation(instance):
    assert isinstance(instance, trace::EObject)

@given(instance=trace::TraceItem_strategy)
@settings(max_examples=50)
def test_trace::traceitem_instantiation(instance):
    assert isinstance(instance, trace::TraceItem)

@given(instance=trace::TraceItem_strategy)
def test_trace::traceitem_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=trace::TraceItem_strategy)
def test_trace::traceitem_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=trace::TraceBySource_strategy)
@settings(max_examples=50)
def test_trace::tracebysource_instantiation(instance):
    assert isinstance(instance, trace::TraceBySource)

@given(instance=trace::TraceList_strategy)
@settings(max_examples=50)
def test_trace::tracelist_instantiation(instance):
    assert isinstance(instance, trace::TraceList)

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

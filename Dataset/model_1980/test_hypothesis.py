import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MRPTrace_RDMElement,
    MRPTrace_NamedElement,
    MRPTrace_TraceEntry,
    NamedElement,
    MRPTrace_Event,
    MRPTrace_Trace,
    MRPTrace_TraceModel,
    TimeUnit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mrptrace_rdmelement_is_not_abstract():
    assert not inspect.isabstract(MRPTrace_RDMElement)


def test_mrptrace_rdmelement_constructor_exists():
    assert callable(MRPTrace_RDMElement.__init__)


def test_mrptrace_rdmelement_constructor_args():
    sig = inspect.signature(MRPTrace_RDMElement.__init__)
    params = list(sig.parameters.keys())



def test_mrptrace_namedelement_is_not_abstract():
    assert not inspect.isabstract(MRPTrace_NamedElement)


def test_mrptrace_namedelement_constructor_exists():
    assert callable(MRPTrace_NamedElement.__init__)


def test_mrptrace_namedelement_constructor_args():
    sig = inspect.signature(MRPTrace_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mrptrace_namedelement_has_name():
    assert hasattr(MRPTrace_NamedElement, "name")
    descriptor = None
    for klass in MRPTrace_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mrptrace_traceentry_is_not_abstract():
    assert not inspect.isabstract(MRPTrace_TraceEntry)


def test_mrptrace_traceentry_constructor_exists():
    assert callable(MRPTrace_TraceEntry.__init__)


def test_mrptrace_traceentry_constructor_args():
    sig = inspect.signature(MRPTrace_TraceEntry.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_mrptrace_traceentry_has_description():
    assert hasattr(MRPTrace_TraceEntry, "description")
    descriptor = None
    for klass in MRPTrace_TraceEntry.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mrptrace_event_is_not_abstract():
    assert not inspect.isabstract(MRPTrace_Event)


def test_mrptrace_event_constructor_exists():
    assert callable(MRPTrace_Event.__init__)


def test_mrptrace_event_constructor_args():
    sig = inspect.signature(MRPTrace_Event.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_mrptrace_event_has_time():
    assert hasattr(MRPTrace_Event, "time")
    descriptor = None
    for klass in MRPTrace_Event.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_mrptrace_trace_is_not_abstract():
    assert not inspect.isabstract(MRPTrace_Trace)


def test_mrptrace_trace_constructor_exists():
    assert callable(MRPTrace_Trace.__init__)


def test_mrptrace_trace_constructor_args():
    sig = inspect.signature(MRPTrace_Trace.__init__)
    params = list(sig.parameters.keys())
    assert "granularity" in params, "Missing parameter 'granularity'"

def test_mrptrace_trace_has_granularity():
    assert hasattr(MRPTrace_Trace, "granularity")
    descriptor = None
    for klass in MRPTrace_Trace.__mro__:
        if "granularity" in klass.__dict__:
            descriptor = klass.__dict__["granularity"]
            break
    assert isinstance(descriptor, property)



def test_mrptrace_tracemodel_is_not_abstract():
    assert not inspect.isabstract(MRPTrace_TraceModel)


def test_mrptrace_tracemodel_constructor_exists():
    assert callable(MRPTrace_TraceModel.__init__)


def test_mrptrace_tracemodel_constructor_args():
    sig = inspect.signature(MRPTrace_TraceModel.__init__)
    params = list(sig.parameters.keys())

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "HOURS",
        "NANOSECONDS",
        "DAYS",
        "MILLISECONDS",
        "MICROSECONDS",
        "SECONDS",
        "MINUTES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"


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
MRPTrace_RDMElement_strategy = st.builds(
    MRPTrace_RDMElement,
)
MRPTrace_NamedElement_strategy = st.builds(
    MRPTrace_NamedElement,
    name=
        safe_text
)
MRPTrace_TraceEntry_strategy = st.builds(
    MRPTrace_TraceEntry,
    description=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
MRPTrace_Event_strategy = st.builds(
    MRPTrace_Event,
    time=
        safe_text
)
MRPTrace_Trace_strategy = st.builds(
    MRPTrace_Trace,
    granularity=
        safe_text
)
MRPTrace_TraceModel_strategy = st.builds(
    MRPTrace_TraceModel,
)

@given(instance=MRPTrace_RDMElement_strategy)
@settings(max_examples=50)
def test_mrptrace_rdmelement_instantiation(instance):
    assert isinstance(instance, MRPTrace_RDMElement)

@given(instance=MRPTrace_NamedElement_strategy)
@settings(max_examples=50)
def test_mrptrace_namedelement_instantiation(instance):
    assert isinstance(instance, MRPTrace_NamedElement)



@given(instance=MRPTrace_NamedElement_strategy)
def test_mrptrace_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MRPTrace_TraceEntry_strategy)
@settings(max_examples=50)
def test_mrptrace_traceentry_instantiation(instance):
    assert isinstance(instance, MRPTrace_TraceEntry)



@given(instance=MRPTrace_TraceEntry_strategy)
def test_mrptrace_traceentry_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=MRPTrace_Event_strategy)
@settings(max_examples=50)
def test_mrptrace_event_instantiation(instance):
    assert isinstance(instance, MRPTrace_Event)



@given(instance=MRPTrace_Event_strategy)
def test_mrptrace_event_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=MRPTrace_Trace_strategy)
@settings(max_examples=50)
def test_mrptrace_trace_instantiation(instance):
    assert isinstance(instance, MRPTrace_Trace)



@given(instance=MRPTrace_Trace_strategy)
def test_mrptrace_trace_granularity_setter(instance):
    original = instance.granularity
    instance.granularity = original
    assert instance.granularity == original

@given(instance=MRPTrace_TraceModel_strategy)
@settings(max_examples=50)
def test_mrptrace_tracemodel_instantiation(instance):
    assert isinstance(instance, MRPTrace_TraceModel)

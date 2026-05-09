import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MRPTrace::RDMElement,
    MRPTrace::NamedElement,
    MRPTrace::TraceEntry,
    NamedElement,
    MRPTrace::Event,
    MRPTrace::Trace,
    MRPTrace::TraceModel,
    TimeUnit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mrptrace::rdmelement_is_not_abstract():
    assert not inspect.isabstract(MRPTrace::RDMElement)


def test_mrptrace::rdmelement_constructor_exists():
    assert callable(MRPTrace::RDMElement.__init__)


def test_mrptrace::rdmelement_constructor_args():
    sig = inspect.signature(MRPTrace::RDMElement.__init__)
    params = list(sig.parameters.keys())



def test_mrptrace::namedelement_is_not_abstract():
    assert not inspect.isabstract(MRPTrace::NamedElement)


def test_mrptrace::namedelement_constructor_exists():
    assert callable(MRPTrace::NamedElement.__init__)


def test_mrptrace::namedelement_constructor_args():
    sig = inspect.signature(MRPTrace::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mrptrace::namedelement_has_name():
    assert hasattr(MRPTrace::NamedElement, "name")
    descriptor = None
    for klass in MRPTrace::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mrptrace::traceentry_is_not_abstract():
    assert not inspect.isabstract(MRPTrace::TraceEntry)


def test_mrptrace::traceentry_constructor_exists():
    assert callable(MRPTrace::TraceEntry.__init__)


def test_mrptrace::traceentry_constructor_args():
    sig = inspect.signature(MRPTrace::TraceEntry.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_mrptrace::traceentry_has_description():
    assert hasattr(MRPTrace::TraceEntry, "description")
    descriptor = None
    for klass in MRPTrace::TraceEntry.__mro__:
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



def test_mrptrace::event_is_not_abstract():
    assert not inspect.isabstract(MRPTrace::Event)


def test_mrptrace::event_constructor_exists():
    assert callable(MRPTrace::Event.__init__)


def test_mrptrace::event_constructor_args():
    sig = inspect.signature(MRPTrace::Event.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_mrptrace::event_has_time():
    assert hasattr(MRPTrace::Event, "time")
    descriptor = None
    for klass in MRPTrace::Event.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_mrptrace::trace_is_not_abstract():
    assert not inspect.isabstract(MRPTrace::Trace)


def test_mrptrace::trace_constructor_exists():
    assert callable(MRPTrace::Trace.__init__)


def test_mrptrace::trace_constructor_args():
    sig = inspect.signature(MRPTrace::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "granularity" in params, "Missing parameter 'granularity'"

def test_mrptrace::trace_has_granularity():
    assert hasattr(MRPTrace::Trace, "granularity")
    descriptor = None
    for klass in MRPTrace::Trace.__mro__:
        if "granularity" in klass.__dict__:
            descriptor = klass.__dict__["granularity"]
            break
    assert isinstance(descriptor, property)



def test_mrptrace::tracemodel_is_not_abstract():
    assert not inspect.isabstract(MRPTrace::TraceModel)


def test_mrptrace::tracemodel_constructor_exists():
    assert callable(MRPTrace::TraceModel.__init__)


def test_mrptrace::tracemodel_constructor_args():
    sig = inspect.signature(MRPTrace::TraceModel.__init__)
    params = list(sig.parameters.keys())

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "MICROSECONDS",
        "MINUTES",
        "MILLISECONDS",
        "NANOSECONDS",
        "SECONDS",
        "HOURS",
        "DAYS",
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
MRPTrace::RDMElement_strategy = st.builds(
    MRPTrace::RDMElement,
)
MRPTrace::NamedElement_strategy = st.builds(
    MRPTrace::NamedElement,
    name=
        safe_text
)
MRPTrace::TraceEntry_strategy = st.builds(
    MRPTrace::TraceEntry,
    description=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
MRPTrace::Event_strategy = st.builds(
    MRPTrace::Event,
    time=
        safe_text
)
MRPTrace::Trace_strategy = st.builds(
    MRPTrace::Trace,
    granularity=
        safe_text
)
MRPTrace::TraceModel_strategy = st.builds(
    MRPTrace::TraceModel,
)

@given(instance=MRPTrace::RDMElement_strategy)
@settings(max_examples=50)
def test_mrptrace::rdmelement_instantiation(instance):
    assert isinstance(instance, MRPTrace::RDMElement)

@given(instance=MRPTrace::NamedElement_strategy)
@settings(max_examples=50)
def test_mrptrace::namedelement_instantiation(instance):
    assert isinstance(instance, MRPTrace::NamedElement)

@given(instance=MRPTrace::NamedElement_strategy)
def test_mrptrace::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MRPTrace::NamedElement_strategy)
def test_mrptrace::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MRPTrace::TraceEntry_strategy)
@settings(max_examples=50)
def test_mrptrace::traceentry_instantiation(instance):
    assert isinstance(instance, MRPTrace::TraceEntry)

@given(instance=MRPTrace::TraceEntry_strategy)
def test_mrptrace::traceentry_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=MRPTrace::TraceEntry_strategy)
def test_mrptrace::traceentry_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=MRPTrace::Event_strategy)
@settings(max_examples=50)
def test_mrptrace::event_instantiation(instance):
    assert isinstance(instance, MRPTrace::Event)

@given(instance=MRPTrace::Event_strategy)
def test_mrptrace::event_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=MRPTrace::Event_strategy)
def test_mrptrace::event_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=MRPTrace::Trace_strategy)
@settings(max_examples=50)
def test_mrptrace::trace_instantiation(instance):
    assert isinstance(instance, MRPTrace::Trace)

@given(instance=MRPTrace::Trace_strategy)
def test_mrptrace::trace_granularity_type(instance):
    assert isinstance(instance.granularity, str)


@given(instance=MRPTrace::Trace_strategy)
def test_mrptrace::trace_granularity_setter(instance):
    original = instance.granularity
    instance.granularity = original
    assert instance.granularity == original

@given(instance=MRPTrace::TraceModel_strategy)
@settings(max_examples=50)
def test_mrptrace::tracemodel_instantiation(instance):
    assert isinstance(instance, MRPTrace::TraceModel)

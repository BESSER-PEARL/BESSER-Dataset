import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metrics::MetricLibrary,
    metrics::Metric,
    metrics::MetricSource,
    MetricKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metrics::metriclibrary_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricLibrary)


def test_metrics::metriclibrary_constructor_exists():
    assert callable(metrics::MetricLibrary.__init__)


def test_metrics::metriclibrary_constructor_args():
    sig = inspect.signature(metrics::MetricLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metrics::metriclibrary_has_name():
    assert hasattr(metrics::MetricLibrary, "name")
    descriptor = None
    for klass in metrics::MetricLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metrics::metric_is_not_abstract():
    assert not inspect.isabstract(metrics::Metric)


def test_metrics::metric_constructor_exists():
    assert callable(metrics::Metric.__init__)


def test_metrics::metric_constructor_args():
    sig = inspect.signature(metrics::Metric.__init__)
    params = list(sig.parameters.keys())



def test_metrics::metricsource_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricSource)


def test_metrics::metricsource_constructor_exists():
    assert callable(metrics::MetricSource.__init__)


def test_metrics::metricsource_constructor_args():
    sig = inspect.signature(metrics::MetricSource.__init__)
    params = list(sig.parameters.keys())
    assert "metricLocation" in params, "Missing parameter 'metricLocation'"
    assert "name" in params, "Missing parameter 'name'"
    assert "metrickind" in params, "Missing parameter 'metrickind'"
    assert "lastPurge" in params, "Missing parameter 'lastPurge'"
    assert "lastContact" in params, "Missing parameter 'lastContact'"
    assert "mappingFile" in params, "Missing parameter 'mappingFile'"

def test_metrics::metricsource_has_metricLocation():
    assert hasattr(metrics::MetricSource, "metricLocation")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "metricLocation" in klass.__dict__:
            descriptor = klass.__dict__["metricLocation"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricsource_has_name():
    assert hasattr(metrics::MetricSource, "name")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricsource_has_metrickind():
    assert hasattr(metrics::MetricSource, "metrickind")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "metrickind" in klass.__dict__:
            descriptor = klass.__dict__["metrickind"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricsource_has_lastPurge():
    assert hasattr(metrics::MetricSource, "lastPurge")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "lastPurge" in klass.__dict__:
            descriptor = klass.__dict__["lastPurge"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricsource_has_lastContact():
    assert hasattr(metrics::MetricSource, "lastContact")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "lastContact" in klass.__dict__:
            descriptor = klass.__dict__["lastContact"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricsource_has_mappingFile():
    assert hasattr(metrics::MetricSource, "mappingFile")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "mappingFile" in klass.__dict__:
            descriptor = klass.__dict__["mappingFile"]
            break
    assert isinstance(descriptor, property)

def test_metrickind_exists():
    # Check that the Enumeration exists
    assert MetricKind is not None

def test_metrickind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MetricKind]
    expected_literals = [
        "RDMS",
        "FILE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MetricKind"


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
metrics::MetricLibrary_strategy = st.builds(
    metrics::MetricLibrary,
    name=
        safe_text
)
metrics::Metric_strategy = st.builds(
    metrics::Metric,
)
metrics::MetricSource_strategy = st.builds(
    metrics::MetricSource,
    metricLocation=
        safe_text,
    name=
        safe_text,
    metrickind=
        safe_text,
    lastPurge=
        safe_text,
    lastContact=
        safe_text,
    mappingFile=
        safe_text
)

@given(instance=metrics::MetricLibrary_strategy)
@settings(max_examples=50)
def test_metrics::metriclibrary_instantiation(instance):
    assert isinstance(instance, metrics::MetricLibrary)

@given(instance=metrics::MetricLibrary_strategy)
def test_metrics::metriclibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metrics::MetricLibrary_strategy)
def test_metrics::metriclibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metrics::Metric_strategy)
@settings(max_examples=50)
def test_metrics::metric_instantiation(instance):
    assert isinstance(instance, metrics::Metric)

@given(instance=metrics::MetricSource_strategy)
@settings(max_examples=50)
def test_metrics::metricsource_instantiation(instance):
    assert isinstance(instance, metrics::MetricSource)

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_metricLocation_type(instance):
    assert isinstance(instance.metricLocation, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_metricLocation_setter(instance):
    original = instance.metricLocation
    instance.metricLocation = original
    assert instance.metricLocation == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_metrickind_type(instance):
    assert isinstance(instance.metrickind, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_metrickind_setter(instance):
    original = instance.metrickind
    instance.metrickind = original
    assert instance.metrickind == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_lastPurge_type(instance):
    assert isinstance(instance.lastPurge, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_lastPurge_setter(instance):
    original = instance.lastPurge
    instance.lastPurge = original
    assert instance.lastPurge == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_lastContact_type(instance):
    assert isinstance(instance.lastContact, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_lastContact_setter(instance):
    original = instance.lastContact
    instance.lastContact = original
    assert instance.lastContact == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_mappingFile_type(instance):
    assert isinstance(instance.mappingFile, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_mappingFile_setter(instance):
    original = instance.mappingFile
    instance.mappingFile = original
    assert instance.mappingFile == original

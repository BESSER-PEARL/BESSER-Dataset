import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metrics::Value,
    metrics::MetricSource,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metrics::value_is_not_abstract():
    assert not inspect.isabstract(metrics::Value)


def test_metrics::value_constructor_exists():
    assert callable(metrics::Value.__init__)


def test_metrics::value_constructor_args():
    sig = inspect.signature(metrics::Value.__init__)
    params = list(sig.parameters.keys())



def test_metrics::metricsource_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricSource)


def test_metrics::metricsource_constructor_exists():
    assert callable(metrics::MetricSource.__init__)


def test_metrics::metricsource_constructor_args():
    sig = inspect.signature(metrics::MetricSource.__init__)
    params = list(sig.parameters.keys())
    assert "lastPurge" in params, "Missing parameter 'lastPurge'"
    assert "location" in params, "Missing parameter 'location'"
    assert "lastContact" in params, "Missing parameter 'lastContact'"
    assert "metrickind" in params, "Missing parameter 'metrickind'"
    assert "name" in params, "Missing parameter 'name'"

def test_metrics::metricsource_has_lastPurge():
    assert hasattr(metrics::MetricSource, "lastPurge")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "lastPurge" in klass.__dict__:
            descriptor = klass.__dict__["lastPurge"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricsource_has_location():
    assert hasattr(metrics::MetricSource, "location")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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

def test_metrics::metricsource_has_metrickind():
    assert hasattr(metrics::MetricSource, "metrickind")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "metrickind" in klass.__dict__:
            descriptor = klass.__dict__["metrickind"]
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
metrics::Value_strategy = st.builds(
    metrics::Value,
)
metrics::MetricSource_strategy = st.builds(
    metrics::MetricSource,
    lastPurge=
        safe_text,
    location=
        safe_text,
    lastContact=
        safe_text,
    metrickind=
        safe_text,
    name=
        safe_text
)

@given(instance=metrics::Value_strategy)
@settings(max_examples=50)
def test_metrics::value_instantiation(instance):
    assert isinstance(instance, metrics::Value)

@given(instance=metrics::MetricSource_strategy)
@settings(max_examples=50)
def test_metrics::metricsource_instantiation(instance):
    assert isinstance(instance, metrics::MetricSource)

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_lastPurge_type(instance):
    assert isinstance(instance.lastPurge, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_lastPurge_setter(instance):
    original = instance.lastPurge
    instance.lastPurge = original
    assert instance.lastPurge == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_lastContact_type(instance):
    assert isinstance(instance.lastContact, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_lastContact_setter(instance):
    original = instance.lastContact
    instance.lastContact = original
    assert instance.lastContact == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_metrickind_type(instance):
    assert isinstance(instance.metrickind, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_metrickind_setter(instance):
    original = instance.metrickind
    instance.metrickind = original
    assert instance.metrickind == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

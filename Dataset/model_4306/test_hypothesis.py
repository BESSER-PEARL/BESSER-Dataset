import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    metrics_Value,
    metrics_MetricSource,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metrics_value_is_not_abstract():
    assert not inspect.isabstract(metrics_Value)


def test_metrics_value_constructor_exists():
    assert callable(metrics_Value.__init__)


def test_metrics_value_constructor_args():
    sig = inspect.signature(metrics_Value.__init__)
    params = list(sig.parameters.keys())



def test_metrics_metricsource_is_not_abstract():
    assert not inspect.isabstract(metrics_MetricSource)


def test_metrics_metricsource_constructor_exists():
    assert callable(metrics_MetricSource.__init__)


def test_metrics_metricsource_constructor_args():
    sig = inspect.signature(metrics_MetricSource.__init__)
    params = list(sig.parameters.keys())
    assert "metrickind" in params, "Missing parameter 'metrickind'"
    assert "location" in params, "Missing parameter 'location'"
    assert "lastPurge" in params, "Missing parameter 'lastPurge'"
    assert "lastContact" in params, "Missing parameter 'lastContact'"
    assert "name" in params, "Missing parameter 'name'"

def test_metrics_metricsource_has_metrickind():
    assert hasattr(metrics_MetricSource, "metrickind")
    descriptor = None
    for klass in metrics_MetricSource.__mro__:
        if "metrickind" in klass.__dict__:
            descriptor = klass.__dict__["metrickind"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metricsource_has_location():
    assert hasattr(metrics_MetricSource, "location")
    descriptor = None
    for klass in metrics_MetricSource.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metricsource_has_lastPurge():
    assert hasattr(metrics_MetricSource, "lastPurge")
    descriptor = None
    for klass in metrics_MetricSource.__mro__:
        if "lastPurge" in klass.__dict__:
            descriptor = klass.__dict__["lastPurge"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metricsource_has_lastContact():
    assert hasattr(metrics_MetricSource, "lastContact")
    descriptor = None
    for klass in metrics_MetricSource.__mro__:
        if "lastContact" in klass.__dict__:
            descriptor = klass.__dict__["lastContact"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metricsource_has_name():
    assert hasattr(metrics_MetricSource, "name")
    descriptor = None
    for klass in metrics_MetricSource.__mro__:
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
metrics_Value_strategy = st.builds(
    metrics_Value,
)
metrics_MetricSource_strategy = st.builds(
    metrics_MetricSource,
    metrickind=
        safe_text,
    location=
        safe_text,
    lastPurge=
        safe_text,
    lastContact=
        safe_text,
    name=
        safe_text
)

@given(instance=metrics_Value_strategy)
@settings(max_examples=50)
def test_metrics_value_instantiation(instance):
    assert isinstance(instance, metrics_Value)

@given(instance=metrics_MetricSource_strategy)
@settings(max_examples=50)
def test_metrics_metricsource_instantiation(instance):
    assert isinstance(instance, metrics_MetricSource)



@given(instance=metrics_MetricSource_strategy)
def test_metrics_metricsource_metrickind_setter(instance):
    original = instance.metrickind
    instance.metrickind = original
    assert instance.metrickind == original



@given(instance=metrics_MetricSource_strategy)
def test_metrics_metricsource_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=metrics_MetricSource_strategy)
def test_metrics_metricsource_lastPurge_setter(instance):
    original = instance.lastPurge
    instance.lastPurge = original
    assert instance.lastPurge == original



@given(instance=metrics_MetricSource_strategy)
def test_metrics_metricsource_lastContact_setter(instance):
    original = instance.lastContact
    instance.lastContact = original
    assert instance.lastContact == original



@given(instance=metrics_MetricSource_strategy)
def test_metrics_metricsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

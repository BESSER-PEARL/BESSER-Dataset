import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metrics::Metric,
    metrics::MetricsSet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metrics::metric_is_not_abstract():
    assert not inspect.isabstract(metrics::Metric)


def test_metrics::metric_constructor_exists():
    assert callable(metrics::Metric.__init__)


def test_metrics::metric_constructor_args():
    sig = inspect.signature(metrics::Metric.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_metrics::metric_has_name():
    assert hasattr(metrics::Metric, "name")
    descriptor = None
    for klass in metrics::Metric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metric_has_value():
    assert hasattr(metrics::Metric, "value")
    descriptor = None
    for klass in metrics::Metric.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metrics::metricsset_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricsSet)


def test_metrics::metricsset_constructor_exists():
    assert callable(metrics::MetricsSet.__init__)


def test_metrics::metricsset_constructor_args():
    sig = inspect.signature(metrics::MetricsSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metrics::metricsset_has_name():
    assert hasattr(metrics::MetricsSet, "name")
    descriptor = None
    for klass in metrics::MetricsSet.__mro__:
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
metrics::Metric_strategy = st.builds(
    metrics::Metric,
    name=
        safe_text,
    value=
        safe_text
)
metrics::MetricsSet_strategy = st.builds(
    metrics::MetricsSet,
    name=
        safe_text
)

@given(instance=metrics::Metric_strategy)
@settings(max_examples=50)
def test_metrics::metric_instantiation(instance):
    assert isinstance(instance, metrics::Metric)

@given(instance=metrics::Metric_strategy)
def test_metrics::metric_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metrics::Metric_strategy)
def test_metrics::metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metrics::Metric_strategy)
def test_metrics::metric_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=metrics::Metric_strategy)
def test_metrics::metric_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metrics::MetricsSet_strategy)
@settings(max_examples=50)
def test_metrics::metricsset_instantiation(instance):
    assert isinstance(instance, metrics::MetricsSet)

@given(instance=metrics::MetricsSet_strategy)
def test_metrics::metricsset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metrics::MetricsSet_strategy)
def test_metrics::metricsset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

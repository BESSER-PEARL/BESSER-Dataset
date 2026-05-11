import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simple::metrics::Metric,
    simple::metrics::MetricsSet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simple::metrics::metric_is_not_abstract():
    assert not inspect.isabstract(simple::metrics::Metric)


def test_simple::metrics::metric_constructor_exists():
    assert callable(simple::metrics::Metric.__init__)


def test_simple::metrics::metric_constructor_args():
    sig = inspect.signature(simple::metrics::Metric.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_simple::metrics::metric_has_value():
    assert hasattr(simple::metrics::Metric, "value")
    descriptor = None
    for klass in simple::metrics::Metric.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_simple::metrics::metric_has_name():
    assert hasattr(simple::metrics::Metric, "name")
    descriptor = None
    for klass in simple::metrics::Metric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simple::metrics::metricsset_is_not_abstract():
    assert not inspect.isabstract(simple::metrics::MetricsSet)


def test_simple::metrics::metricsset_constructor_exists():
    assert callable(simple::metrics::MetricsSet.__init__)


def test_simple::metrics::metricsset_constructor_args():
    sig = inspect.signature(simple::metrics::MetricsSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simple::metrics::metricsset_has_name():
    assert hasattr(simple::metrics::MetricsSet, "name")
    descriptor = None
    for klass in simple::metrics::MetricsSet.__mro__:
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
simple::metrics::Metric_strategy = st.builds(
    simple::metrics::Metric,
    value=
        safe_text,
    name=
        safe_text
)
simple::metrics::MetricsSet_strategy = st.builds(
    simple::metrics::MetricsSet,
    name=
        safe_text
)

@given(instance=simple::metrics::Metric_strategy)
@settings(max_examples=50)
def test_simple::metrics::metric_instantiation(instance):
    assert isinstance(instance, simple::metrics::Metric)

@given(instance=simple::metrics::Metric_strategy)
def test_simple::metrics::metric_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=simple::metrics::Metric_strategy)
def test_simple::metrics::metric_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simple::metrics::Metric_strategy)
def test_simple::metrics::metric_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simple::metrics::Metric_strategy)
def test_simple::metrics::metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simple::metrics::MetricsSet_strategy)
@settings(max_examples=50)
def test_simple::metrics::metricsset_instantiation(instance):
    assert isinstance(instance, simple::metrics::MetricsSet)

@given(instance=simple::metrics::MetricsSet_strategy)
def test_simple::metrics::metricsset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simple::metrics::MetricsSet_strategy)
def test_simple::metrics::metricsset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

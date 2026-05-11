import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metrics::MetricRetentionPeriods,
    metrics::EObject,
    Rule,
    metrics::MetricRetentionRule,
    metrics::MetricAggregationRule,
    Base,
    metrics::MetricAggregationRules,
    metrics::MetricRetentionRules,
    metrics::MetricSource,
    metrics::Metric,
    metrics::Addon,
    FixedMetricRetentionPeriod,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metrics::metricretentionperiods_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricRetentionPeriods)


def test_metrics::metricretentionperiods_constructor_exists():
    assert callable(metrics::MetricRetentionPeriods.__init__)


def test_metrics::metricretentionperiods_constructor_args():
    sig = inspect.signature(metrics::MetricRetentionPeriods.__init__)
    params = list(sig.parameters.keys())
    assert "metricRetentionPeriods" in params, "Missing parameter 'metricRetentionPeriods'"

def test_metrics::metricretentionperiods_has_metricRetentionPeriods():
    assert hasattr(metrics::MetricRetentionPeriods, "metricRetentionPeriods")
    descriptor = None
    for klass in metrics::MetricRetentionPeriods.__mro__:
        if "metricRetentionPeriods" in klass.__dict__:
            descriptor = klass.__dict__["metricRetentionPeriods"]
            break
    assert isinstance(descriptor, property)



def test_metrics::eobject_is_not_abstract():
    assert not inspect.isabstract(metrics::EObject)


def test_metrics::eobject_constructor_exists():
    assert callable(metrics::EObject.__init__)


def test_metrics::eobject_constructor_args():
    sig = inspect.signature(metrics::EObject.__init__)
    params = list(sig.parameters.keys())



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_metrics::metricretentionrule_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricRetentionRule)


def test_metrics::metricretentionrule_constructor_exists():
    assert callable(metrics::MetricRetentionRule.__init__)


def test_metrics::metricretentionrule_constructor_args():
    sig = inspect.signature(metrics::MetricRetentionRule.__init__)
    params = list(sig.parameters.keys())
    assert "period" in params, "Missing parameter 'period'"
    assert "intervalHint" in params, "Missing parameter 'intervalHint'"

def test_metrics::metricretentionrule_has_period():
    assert hasattr(metrics::MetricRetentionRule, "period")
    descriptor = None
    for klass in metrics::MetricRetentionRule.__mro__:
        if "period" in klass.__dict__:
            descriptor = klass.__dict__["period"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricretentionrule_has_intervalHint():
    assert hasattr(metrics::MetricRetentionRule, "intervalHint")
    descriptor = None
    for klass in metrics::MetricRetentionRule.__mro__:
        if "intervalHint" in klass.__dict__:
            descriptor = klass.__dict__["intervalHint"]
            break
    assert isinstance(descriptor, property)



def test_metrics::metricaggregationrule_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricAggregationRule)


def test_metrics::metricaggregationrule_constructor_exists():
    assert callable(metrics::MetricAggregationRule.__init__)


def test_metrics::metricaggregationrule_constructor_args():
    sig = inspect.signature(metrics::MetricAggregationRule.__init__)
    params = list(sig.parameters.keys())
    assert "period" in params, "Missing parameter 'period'"
    assert "intervalHint" in params, "Missing parameter 'intervalHint'"

def test_metrics::metricaggregationrule_has_period():
    assert hasattr(metrics::MetricAggregationRule, "period")
    descriptor = None
    for klass in metrics::MetricAggregationRule.__mro__:
        if "period" in klass.__dict__:
            descriptor = klass.__dict__["period"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricaggregationrule_has_intervalHint():
    assert hasattr(metrics::MetricAggregationRule, "intervalHint")
    descriptor = None
    for klass in metrics::MetricAggregationRule.__mro__:
        if "intervalHint" in klass.__dict__:
            descriptor = klass.__dict__["intervalHint"]
            break
    assert isinstance(descriptor, property)



def test_base_is_not_abstract():
    assert not inspect.isabstract(Base)


def test_base_constructor_exists():
    assert callable(Base.__init__)


def test_base_constructor_args():
    sig = inspect.signature(Base.__init__)
    params = list(sig.parameters.keys())



def test_metrics::metricaggregationrules_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricAggregationRules)


def test_metrics::metricaggregationrules_constructor_exists():
    assert callable(metrics::MetricAggregationRules.__init__)


def test_metrics::metricaggregationrules_constructor_args():
    sig = inspect.signature(metrics::MetricAggregationRules.__init__)
    params = list(sig.parameters.keys())



def test_metrics::metricretentionrules_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricRetentionRules)


def test_metrics::metricretentionrules_constructor_exists():
    assert callable(metrics::MetricRetentionRules.__init__)


def test_metrics::metricretentionrules_constructor_args():
    sig = inspect.signature(metrics::MetricRetentionRules.__init__)
    params = list(sig.parameters.keys())



def test_metrics::metricsource_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricSource)


def test_metrics::metricsource_constructor_exists():
    assert callable(metrics::MetricSource.__init__)


def test_metrics::metricsource_constructor_args():
    sig = inspect.signature(metrics::MetricSource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metrics::metricsource_has_name():
    assert hasattr(metrics::MetricSource, "name")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
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
    assert "name" in params, "Missing parameter 'name'"

def test_metrics::metric_has_name():
    assert hasattr(metrics::Metric, "name")
    descriptor = None
    for klass in metrics::Metric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metrics::addon_is_not_abstract():
    assert not inspect.isabstract(metrics::Addon)


def test_metrics::addon_constructor_exists():
    assert callable(metrics::Addon.__init__)


def test_metrics::addon_constructor_args():
    sig = inspect.signature(metrics::Addon.__init__)
    params = list(sig.parameters.keys())

def test_fixedmetricretentionperiod_exists():
    # Check that the Enumeration exists
    assert FixedMetricRetentionPeriod is not None

def test_fixedmetricretentionperiod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FixedMetricRetentionPeriod]
    expected_literals = [
        "Always",
        "OneWeek",
        "OneYear",
        "OneMonth",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FixedMetricRetentionPeriod"


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
metrics::MetricRetentionPeriods_strategy = st.builds(
    metrics::MetricRetentionPeriods,
    metricRetentionPeriods=
        safe_text
)
metrics::EObject_strategy = st.builds(
    metrics::EObject,
)
Rule_strategy = st.builds(
    Rule,
)
metrics::MetricRetentionRule_strategy = st.builds(
    metrics::MetricRetentionRule,
    period=
        safe_text,
    intervalHint=
        safe_text
)
metrics::MetricAggregationRule_strategy = st.builds(
    metrics::MetricAggregationRule,
    period=
        safe_text,
    intervalHint=
        safe_text
)
Base_strategy = st.builds(
    Base,
)
metrics::MetricAggregationRules_strategy = st.builds(
    metrics::MetricAggregationRules,
)
metrics::MetricRetentionRules_strategy = st.builds(
    metrics::MetricRetentionRules,
)
metrics::MetricSource_strategy = st.builds(
    metrics::MetricSource,
    name=
        safe_text
)
metrics::Metric_strategy = st.builds(
    metrics::Metric,
    name=
        safe_text
)
metrics::Addon_strategy = st.builds(
    metrics::Addon,
)

@given(instance=metrics::MetricRetentionPeriods_strategy)
@settings(max_examples=50)
def test_metrics::metricretentionperiods_instantiation(instance):
    assert isinstance(instance, metrics::MetricRetentionPeriods)

@given(instance=metrics::MetricRetentionPeriods_strategy)
def test_metrics::metricretentionperiods_metricRetentionPeriods_type(instance):
    assert isinstance(instance.metricRetentionPeriods, str)


@given(instance=metrics::MetricRetentionPeriods_strategy)
def test_metrics::metricretentionperiods_metricRetentionPeriods_setter(instance):
    original = instance.metricRetentionPeriods
    instance.metricRetentionPeriods = original
    assert instance.metricRetentionPeriods == original

@given(instance=metrics::EObject_strategy)
@settings(max_examples=50)
def test_metrics::eobject_instantiation(instance):
    assert isinstance(instance, metrics::EObject)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=metrics::MetricRetentionRule_strategy)
@settings(max_examples=50)
def test_metrics::metricretentionrule_instantiation(instance):
    assert isinstance(instance, metrics::MetricRetentionRule)

@given(instance=metrics::MetricRetentionRule_strategy)
def test_metrics::metricretentionrule_period_type(instance):
    assert isinstance(instance.period, str)


@given(instance=metrics::MetricRetentionRule_strategy)
def test_metrics::metricretentionrule_period_setter(instance):
    original = instance.period
    instance.period = original
    assert instance.period == original

@given(instance=metrics::MetricRetentionRule_strategy)
def test_metrics::metricretentionrule_intervalHint_type(instance):
    assert isinstance(instance.intervalHint, str)


@given(instance=metrics::MetricRetentionRule_strategy)
def test_metrics::metricretentionrule_intervalHint_setter(instance):
    original = instance.intervalHint
    instance.intervalHint = original
    assert instance.intervalHint == original

@given(instance=metrics::MetricAggregationRule_strategy)
@settings(max_examples=50)
def test_metrics::metricaggregationrule_instantiation(instance):
    assert isinstance(instance, metrics::MetricAggregationRule)

@given(instance=metrics::MetricAggregationRule_strategy)
def test_metrics::metricaggregationrule_period_type(instance):
    assert isinstance(instance.period, str)


@given(instance=metrics::MetricAggregationRule_strategy)
def test_metrics::metricaggregationrule_period_setter(instance):
    original = instance.period
    instance.period = original
    assert instance.period == original

@given(instance=metrics::MetricAggregationRule_strategy)
def test_metrics::metricaggregationrule_intervalHint_type(instance):
    assert isinstance(instance.intervalHint, str)


@given(instance=metrics::MetricAggregationRule_strategy)
def test_metrics::metricaggregationrule_intervalHint_setter(instance):
    original = instance.intervalHint
    instance.intervalHint = original
    assert instance.intervalHint == original

@given(instance=Base_strategy)
@settings(max_examples=50)
def test_base_instantiation(instance):
    assert isinstance(instance, Base)

@given(instance=metrics::MetricAggregationRules_strategy)
@settings(max_examples=50)
def test_metrics::metricaggregationrules_instantiation(instance):
    assert isinstance(instance, metrics::MetricAggregationRules)

@given(instance=metrics::MetricRetentionRules_strategy)
@settings(max_examples=50)
def test_metrics::metricretentionrules_instantiation(instance):
    assert isinstance(instance, metrics::MetricRetentionRules)

@given(instance=metrics::MetricSource_strategy)
@settings(max_examples=50)
def test_metrics::metricsource_instantiation(instance):
    assert isinstance(instance, metrics::MetricSource)

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=metrics::Addon_strategy)
@settings(max_examples=50)
def test_metrics::addon_instantiation(instance):
    assert isinstance(instance, metrics::Addon)

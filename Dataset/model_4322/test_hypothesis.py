import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metric::Constraint,
    Metric,
    metric::ConstraintMetric,
    ConstraintMetric,
    metric::ConstraintMetrics,
    metric::Metric,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metric::constraint_is_not_abstract():
    assert not inspect.isabstract(metric::Constraint)


def test_metric::constraint_constructor_exists():
    assert callable(metric::Constraint.__init__)


def test_metric::constraint_constructor_args():
    sig = inspect.signature(metric::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_metric_is_not_abstract():
    assert not inspect.isabstract(Metric)


def test_metric_constructor_exists():
    assert callable(Metric.__init__)


def test_metric_constructor_args():
    sig = inspect.signature(Metric.__init__)
    params = list(sig.parameters.keys())



def test_metric::constraintmetric_is_not_abstract():
    assert not inspect.isabstract(metric::ConstraintMetric)


def test_metric::constraintmetric_constructor_exists():
    assert callable(metric::ConstraintMetric.__init__)


def test_metric::constraintmetric_constructor_args():
    sig = inspect.signature(metric::ConstraintMetric.__init__)
    params = list(sig.parameters.keys())
    assert "calledOperations" in params, "Missing parameter 'calledOperations'"
    assert "usedIterators" in params, "Missing parameter 'usedIterators'"
    assert "calledProperties" in params, "Missing parameter 'calledProperties'"
    assert "expressionDepth" in params, "Missing parameter 'expressionDepth'"
    assert "expressionCount" in params, "Missing parameter 'expressionCount'"
    assert "numberOfLetExpressions" in params, "Missing parameter 'numberOfLetExpressions'"
    assert "usedLiterals" in params, "Missing parameter 'usedLiterals'"
    assert "numberOfIfExpressions" in params, "Missing parameter 'numberOfIfExpressions'"

def test_metric::constraintmetric_has_calledOperations():
    assert hasattr(metric::ConstraintMetric, "calledOperations")
    descriptor = None
    for klass in metric::ConstraintMetric.__mro__:
        if "calledOperations" in klass.__dict__:
            descriptor = klass.__dict__["calledOperations"]
            break
    assert isinstance(descriptor, property)

def test_metric::constraintmetric_has_usedIterators():
    assert hasattr(metric::ConstraintMetric, "usedIterators")
    descriptor = None
    for klass in metric::ConstraintMetric.__mro__:
        if "usedIterators" in klass.__dict__:
            descriptor = klass.__dict__["usedIterators"]
            break
    assert isinstance(descriptor, property)

def test_metric::constraintmetric_has_calledProperties():
    assert hasattr(metric::ConstraintMetric, "calledProperties")
    descriptor = None
    for klass in metric::ConstraintMetric.__mro__:
        if "calledProperties" in klass.__dict__:
            descriptor = klass.__dict__["calledProperties"]
            break
    assert isinstance(descriptor, property)

def test_metric::constraintmetric_has_expressionDepth():
    assert hasattr(metric::ConstraintMetric, "expressionDepth")
    descriptor = None
    for klass in metric::ConstraintMetric.__mro__:
        if "expressionDepth" in klass.__dict__:
            descriptor = klass.__dict__["expressionDepth"]
            break
    assert isinstance(descriptor, property)

def test_metric::constraintmetric_has_expressionCount():
    assert hasattr(metric::ConstraintMetric, "expressionCount")
    descriptor = None
    for klass in metric::ConstraintMetric.__mro__:
        if "expressionCount" in klass.__dict__:
            descriptor = klass.__dict__["expressionCount"]
            break
    assert isinstance(descriptor, property)

def test_metric::constraintmetric_has_numberOfLetExpressions():
    assert hasattr(metric::ConstraintMetric, "numberOfLetExpressions")
    descriptor = None
    for klass in metric::ConstraintMetric.__mro__:
        if "numberOfLetExpressions" in klass.__dict__:
            descriptor = klass.__dict__["numberOfLetExpressions"]
            break
    assert isinstance(descriptor, property)

def test_metric::constraintmetric_has_usedLiterals():
    assert hasattr(metric::ConstraintMetric, "usedLiterals")
    descriptor = None
    for klass in metric::ConstraintMetric.__mro__:
        if "usedLiterals" in klass.__dict__:
            descriptor = klass.__dict__["usedLiterals"]
            break
    assert isinstance(descriptor, property)

def test_metric::constraintmetric_has_numberOfIfExpressions():
    assert hasattr(metric::ConstraintMetric, "numberOfIfExpressions")
    descriptor = None
    for klass in metric::ConstraintMetric.__mro__:
        if "numberOfIfExpressions" in klass.__dict__:
            descriptor = klass.__dict__["numberOfIfExpressions"]
            break
    assert isinstance(descriptor, property)



def test_constraintmetric_is_not_abstract():
    assert not inspect.isabstract(ConstraintMetric)


def test_constraintmetric_constructor_exists():
    assert callable(ConstraintMetric.__init__)


def test_constraintmetric_constructor_args():
    sig = inspect.signature(ConstraintMetric.__init__)
    params = list(sig.parameters.keys())



def test_metric::constraintmetrics_is_not_abstract():
    assert not inspect.isabstract(metric::ConstraintMetrics)


def test_metric::constraintmetrics_constructor_exists():
    assert callable(metric::ConstraintMetrics.__init__)


def test_metric::constraintmetrics_constructor_args():
    sig = inspect.signature(metric::ConstraintMetrics.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfConstraintsByKind" in params, "Missing parameter 'numberOfConstraintsByKind'"

def test_metric::constraintmetrics_has_numberOfConstraintsByKind():
    assert hasattr(metric::ConstraintMetrics, "numberOfConstraintsByKind")
    descriptor = None
    for klass in metric::ConstraintMetrics.__mro__:
        if "numberOfConstraintsByKind" in klass.__dict__:
            descriptor = klass.__dict__["numberOfConstraintsByKind"]
            break
    assert isinstance(descriptor, property)



def test_metric::metric_is_not_abstract():
    assert not inspect.isabstract(metric::Metric)


def test_metric::metric_constructor_exists():
    assert callable(metric::Metric.__init__)


def test_metric::metric_constructor_args():
    sig = inspect.signature(metric::Metric.__init__)
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
metric::Constraint_strategy = st.builds(
    metric::Constraint,
)
Metric_strategy = st.builds(
    Metric,
)
metric::ConstraintMetric_strategy = st.builds(
    metric::ConstraintMetric,
    calledOperations=
        safe_text,
    usedIterators=
        safe_text,
    calledProperties=
        safe_text,
    expressionDepth=
        st.integers(),
    expressionCount=
        st.integers(),
    numberOfLetExpressions=
        st.integers(),
    usedLiterals=
        safe_text,
    numberOfIfExpressions=
        st.integers()
)
ConstraintMetric_strategy = st.builds(
    ConstraintMetric,
)
metric::ConstraintMetrics_strategy = st.builds(
    metric::ConstraintMetrics,
    numberOfConstraintsByKind=
        safe_text
)
metric::Metric_strategy = st.builds(
    metric::Metric,
)

@given(instance=metric::Constraint_strategy)
@settings(max_examples=50)
def test_metric::constraint_instantiation(instance):
    assert isinstance(instance, metric::Constraint)

@given(instance=Metric_strategy)
@settings(max_examples=50)
def test_metric_instantiation(instance):
    assert isinstance(instance, Metric)

@given(instance=metric::ConstraintMetric_strategy)
@settings(max_examples=50)
def test_metric::constraintmetric_instantiation(instance):
    assert isinstance(instance, metric::ConstraintMetric)

@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_calledOperations_type(instance):
    assert isinstance(instance.calledOperations, str)


@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_calledOperations_setter(instance):
    original = instance.calledOperations
    instance.calledOperations = original
    assert instance.calledOperations == original

@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_usedIterators_type(instance):
    assert isinstance(instance.usedIterators, str)


@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_usedIterators_setter(instance):
    original = instance.usedIterators
    instance.usedIterators = original
    assert instance.usedIterators == original

@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_calledProperties_type(instance):
    assert isinstance(instance.calledProperties, str)


@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_calledProperties_setter(instance):
    original = instance.calledProperties
    instance.calledProperties = original
    assert instance.calledProperties == original

@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_expressionDepth_type(instance):
    assert isinstance(instance.expressionDepth, int)


@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_expressionDepth_setter(instance):
    original = instance.expressionDepth
    instance.expressionDepth = original
    assert instance.expressionDepth == original

@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_expressionCount_type(instance):
    assert isinstance(instance.expressionCount, int)


@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_expressionCount_setter(instance):
    original = instance.expressionCount
    instance.expressionCount = original
    assert instance.expressionCount == original

@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_numberOfLetExpressions_type(instance):
    assert isinstance(instance.numberOfLetExpressions, int)


@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_numberOfLetExpressions_setter(instance):
    original = instance.numberOfLetExpressions
    instance.numberOfLetExpressions = original
    assert instance.numberOfLetExpressions == original

@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_usedLiterals_type(instance):
    assert isinstance(instance.usedLiterals, str)


@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_usedLiterals_setter(instance):
    original = instance.usedLiterals
    instance.usedLiterals = original
    assert instance.usedLiterals == original

@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_numberOfIfExpressions_type(instance):
    assert isinstance(instance.numberOfIfExpressions, int)


@given(instance=metric::ConstraintMetric_strategy)
def test_metric::constraintmetric_numberOfIfExpressions_setter(instance):
    original = instance.numberOfIfExpressions
    instance.numberOfIfExpressions = original
    assert instance.numberOfIfExpressions == original

@given(instance=ConstraintMetric_strategy)
@settings(max_examples=50)
def test_constraintmetric_instantiation(instance):
    assert isinstance(instance, ConstraintMetric)

@given(instance=metric::ConstraintMetrics_strategy)
@settings(max_examples=50)
def test_metric::constraintmetrics_instantiation(instance):
    assert isinstance(instance, metric::ConstraintMetrics)

@given(instance=metric::ConstraintMetrics_strategy)
def test_metric::constraintmetrics_numberOfConstraintsByKind_type(instance):
    assert isinstance(instance.numberOfConstraintsByKind, str)


@given(instance=metric::ConstraintMetrics_strategy)
def test_metric::constraintmetrics_numberOfConstraintsByKind_setter(instance):
    original = instance.numberOfConstraintsByKind
    instance.numberOfConstraintsByKind = original
    assert instance.numberOfConstraintsByKind == original

@given(instance=metric::Metric_strategy)
@settings(max_examples=50)
def test_metric::metric_instantiation(instance):
    assert isinstance(instance, metric::Metric)

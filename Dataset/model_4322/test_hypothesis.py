import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    metric_Constraint,
    Metric,
    metric_ConstraintMetric,
    ConstraintMetric,
    metric_ConstraintMetrics,
    metric_Metric,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metric_constraint_is_not_abstract():
    assert not inspect.isabstract(metric_Constraint)


def test_metric_constraint_constructor_exists():
    assert callable(metric_Constraint.__init__)


def test_metric_constraint_constructor_args():
    sig = inspect.signature(metric_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_metric_is_not_abstract():
    assert not inspect.isabstract(Metric)


def test_metric_constructor_exists():
    assert callable(Metric.__init__)


def test_metric_constructor_args():
    sig = inspect.signature(Metric.__init__)
    params = list(sig.parameters.keys())



def test_metric_constraintmetric_is_not_abstract():
    assert not inspect.isabstract(metric_ConstraintMetric)


def test_metric_constraintmetric_constructor_exists():
    assert callable(metric_ConstraintMetric.__init__)


def test_metric_constraintmetric_constructor_args():
    sig = inspect.signature(metric_ConstraintMetric.__init__)
    params = list(sig.parameters.keys())
    assert "usedIterators" in params, "Missing parameter 'usedIterators'"
    assert "calledProperties" in params, "Missing parameter 'calledProperties'"
    assert "numberOfLetExpressions" in params, "Missing parameter 'numberOfLetExpressions'"
    assert "numberOfIfExpressions" in params, "Missing parameter 'numberOfIfExpressions'"
    assert "expressionDepth" in params, "Missing parameter 'expressionDepth'"
    assert "expressionCount" in params, "Missing parameter 'expressionCount'"
    assert "usedLiterals" in params, "Missing parameter 'usedLiterals'"
    assert "calledOperations" in params, "Missing parameter 'calledOperations'"

def test_metric_constraintmetric_has_usedIterators():
    assert hasattr(metric_ConstraintMetric, "usedIterators")
    descriptor = None
    for klass in metric_ConstraintMetric.__mro__:
        if "usedIterators" in klass.__dict__:
            descriptor = klass.__dict__["usedIterators"]
            break
    assert isinstance(descriptor, property)

def test_metric_constraintmetric_has_calledProperties():
    assert hasattr(metric_ConstraintMetric, "calledProperties")
    descriptor = None
    for klass in metric_ConstraintMetric.__mro__:
        if "calledProperties" in klass.__dict__:
            descriptor = klass.__dict__["calledProperties"]
            break
    assert isinstance(descriptor, property)

def test_metric_constraintmetric_has_numberOfLetExpressions():
    assert hasattr(metric_ConstraintMetric, "numberOfLetExpressions")
    descriptor = None
    for klass in metric_ConstraintMetric.__mro__:
        if "numberOfLetExpressions" in klass.__dict__:
            descriptor = klass.__dict__["numberOfLetExpressions"]
            break
    assert isinstance(descriptor, property)

def test_metric_constraintmetric_has_numberOfIfExpressions():
    assert hasattr(metric_ConstraintMetric, "numberOfIfExpressions")
    descriptor = None
    for klass in metric_ConstraintMetric.__mro__:
        if "numberOfIfExpressions" in klass.__dict__:
            descriptor = klass.__dict__["numberOfIfExpressions"]
            break
    assert isinstance(descriptor, property)

def test_metric_constraintmetric_has_expressionDepth():
    assert hasattr(metric_ConstraintMetric, "expressionDepth")
    descriptor = None
    for klass in metric_ConstraintMetric.__mro__:
        if "expressionDepth" in klass.__dict__:
            descriptor = klass.__dict__["expressionDepth"]
            break
    assert isinstance(descriptor, property)

def test_metric_constraintmetric_has_expressionCount():
    assert hasattr(metric_ConstraintMetric, "expressionCount")
    descriptor = None
    for klass in metric_ConstraintMetric.__mro__:
        if "expressionCount" in klass.__dict__:
            descriptor = klass.__dict__["expressionCount"]
            break
    assert isinstance(descriptor, property)

def test_metric_constraintmetric_has_usedLiterals():
    assert hasattr(metric_ConstraintMetric, "usedLiterals")
    descriptor = None
    for klass in metric_ConstraintMetric.__mro__:
        if "usedLiterals" in klass.__dict__:
            descriptor = klass.__dict__["usedLiterals"]
            break
    assert isinstance(descriptor, property)

def test_metric_constraintmetric_has_calledOperations():
    assert hasattr(metric_ConstraintMetric, "calledOperations")
    descriptor = None
    for klass in metric_ConstraintMetric.__mro__:
        if "calledOperations" in klass.__dict__:
            descriptor = klass.__dict__["calledOperations"]
            break
    assert isinstance(descriptor, property)



def test_constraintmetric_is_not_abstract():
    assert not inspect.isabstract(ConstraintMetric)


def test_constraintmetric_constructor_exists():
    assert callable(ConstraintMetric.__init__)


def test_constraintmetric_constructor_args():
    sig = inspect.signature(ConstraintMetric.__init__)
    params = list(sig.parameters.keys())



def test_metric_constraintmetrics_is_not_abstract():
    assert not inspect.isabstract(metric_ConstraintMetrics)


def test_metric_constraintmetrics_constructor_exists():
    assert callable(metric_ConstraintMetrics.__init__)


def test_metric_constraintmetrics_constructor_args():
    sig = inspect.signature(metric_ConstraintMetrics.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfConstraintsByKind" in params, "Missing parameter 'numberOfConstraintsByKind'"

def test_metric_constraintmetrics_has_numberOfConstraintsByKind():
    assert hasattr(metric_ConstraintMetrics, "numberOfConstraintsByKind")
    descriptor = None
    for klass in metric_ConstraintMetrics.__mro__:
        if "numberOfConstraintsByKind" in klass.__dict__:
            descriptor = klass.__dict__["numberOfConstraintsByKind"]
            break
    assert isinstance(descriptor, property)



def test_metric_metric_is_not_abstract():
    assert not inspect.isabstract(metric_Metric)


def test_metric_metric_constructor_exists():
    assert callable(metric_Metric.__init__)


def test_metric_metric_constructor_args():
    sig = inspect.signature(metric_Metric.__init__)
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
metric_Constraint_strategy = st.builds(
    metric_Constraint,
)
Metric_strategy = st.builds(
    Metric,
)
metric_ConstraintMetric_strategy = st.builds(
    metric_ConstraintMetric,
    usedIterators=
        safe_text,
    calledProperties=
        safe_text,
    numberOfLetExpressions=
        st.integers(),
    numberOfIfExpressions=
        st.integers(),
    expressionDepth=
        st.integers(),
    expressionCount=
        st.integers(),
    usedLiterals=
        safe_text,
    calledOperations=
        safe_text
)
ConstraintMetric_strategy = st.builds(
    ConstraintMetric,
)
metric_ConstraintMetrics_strategy = st.builds(
    metric_ConstraintMetrics,
    numberOfConstraintsByKind=
        safe_text
)
metric_Metric_strategy = st.builds(
    metric_Metric,
)

@given(instance=metric_Constraint_strategy)
@settings(max_examples=50)
def test_metric_constraint_instantiation(instance):
    assert isinstance(instance, metric_Constraint)

@given(instance=Metric_strategy)
@settings(max_examples=50)
def test_metric_instantiation(instance):
    assert isinstance(instance, Metric)

@given(instance=metric_ConstraintMetric_strategy)
@settings(max_examples=50)
def test_metric_constraintmetric_instantiation(instance):
    assert isinstance(instance, metric_ConstraintMetric)



@given(instance=metric_ConstraintMetric_strategy)
def test_metric_constraintmetric_usedIterators_setter(instance):
    original = instance.usedIterators
    instance.usedIterators = original
    assert instance.usedIterators == original



@given(instance=metric_ConstraintMetric_strategy)
def test_metric_constraintmetric_calledProperties_setter(instance):
    original = instance.calledProperties
    instance.calledProperties = original
    assert instance.calledProperties == original



@given(instance=metric_ConstraintMetric_strategy)
def test_metric_constraintmetric_numberOfLetExpressions_setter(instance):
    original = instance.numberOfLetExpressions
    instance.numberOfLetExpressions = original
    assert instance.numberOfLetExpressions == original



@given(instance=metric_ConstraintMetric_strategy)
def test_metric_constraintmetric_numberOfIfExpressions_setter(instance):
    original = instance.numberOfIfExpressions
    instance.numberOfIfExpressions = original
    assert instance.numberOfIfExpressions == original



@given(instance=metric_ConstraintMetric_strategy)
def test_metric_constraintmetric_expressionDepth_setter(instance):
    original = instance.expressionDepth
    instance.expressionDepth = original
    assert instance.expressionDepth == original



@given(instance=metric_ConstraintMetric_strategy)
def test_metric_constraintmetric_expressionCount_setter(instance):
    original = instance.expressionCount
    instance.expressionCount = original
    assert instance.expressionCount == original



@given(instance=metric_ConstraintMetric_strategy)
def test_metric_constraintmetric_usedLiterals_setter(instance):
    original = instance.usedLiterals
    instance.usedLiterals = original
    assert instance.usedLiterals == original



@given(instance=metric_ConstraintMetric_strategy)
def test_metric_constraintmetric_calledOperations_setter(instance):
    original = instance.calledOperations
    instance.calledOperations = original
    assert instance.calledOperations == original

@given(instance=ConstraintMetric_strategy)
@settings(max_examples=50)
def test_constraintmetric_instantiation(instance):
    assert isinstance(instance, ConstraintMetric)

@given(instance=metric_ConstraintMetrics_strategy)
@settings(max_examples=50)
def test_metric_constraintmetrics_instantiation(instance):
    assert isinstance(instance, metric_ConstraintMetrics)



@given(instance=metric_ConstraintMetrics_strategy)
def test_metric_constraintmetrics_numberOfConstraintsByKind_setter(instance):
    original = instance.numberOfConstraintsByKind
    instance.numberOfConstraintsByKind = original
    assert instance.numberOfConstraintsByKind == original

@given(instance=metric_Metric_strategy)
@settings(max_examples=50)
def test_metric_metric_instantiation(instance):
    assert isinstance(instance, metric_Metric)

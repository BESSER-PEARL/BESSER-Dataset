import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MetricModel_MetricPlanModel,
    Metric,
    MetricModel_TaskMetric,
    MetricModel_ActivityMetric,
    MetricModel_Metric,
    ColectType,
    BaseElement,
    MetricUnit,
    MetricType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metricmodel_metricplanmodel_is_not_abstract():
    assert not inspect.isabstract(MetricModel_MetricPlanModel)


def test_metricmodel_metricplanmodel_constructor_exists():
    assert callable(MetricModel_MetricPlanModel.__init__)


def test_metricmodel_metricplanmodel_constructor_args():
    sig = inspect.signature(MetricModel_MetricPlanModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metricmodel_metricplanmodel_has_name():
    assert hasattr(MetricModel_MetricPlanModel, "name")
    descriptor = None
    for klass in MetricModel_MetricPlanModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metric_is_not_abstract():
    assert not inspect.isabstract(Metric)


def test_metric_constructor_exists():
    assert callable(Metric.__init__)


def test_metric_constructor_args():
    sig = inspect.signature(Metric.__init__)
    params = list(sig.parameters.keys())



def test_metricmodel_taskmetric_is_not_abstract():
    assert not inspect.isabstract(MetricModel_TaskMetric)


def test_metricmodel_taskmetric_constructor_exists():
    assert callable(MetricModel_TaskMetric.__init__)


def test_metricmodel_taskmetric_constructor_args():
    sig = inspect.signature(MetricModel_TaskMetric.__init__)
    params = list(sig.parameters.keys())
    assert "tasksBase" in params, "Missing parameter 'tasksBase'"

def test_metricmodel_taskmetric_has_tasksBase():
    assert hasattr(MetricModel_TaskMetric, "tasksBase")
    descriptor = None
    for klass in MetricModel_TaskMetric.__mro__:
        if "tasksBase" in klass.__dict__:
            descriptor = klass.__dict__["tasksBase"]
            break
    assert isinstance(descriptor, property)



def test_metricmodel_activitymetric_is_not_abstract():
    assert not inspect.isabstract(MetricModel_ActivityMetric)


def test_metricmodel_activitymetric_constructor_exists():
    assert callable(MetricModel_ActivityMetric.__init__)


def test_metricmodel_activitymetric_constructor_args():
    sig = inspect.signature(MetricModel_ActivityMetric.__init__)
    params = list(sig.parameters.keys())
    assert "activityEnd" in params, "Missing parameter 'activityEnd'"
    assert "activityBegin" in params, "Missing parameter 'activityBegin'"

def test_metricmodel_activitymetric_has_activityEnd():
    assert hasattr(MetricModel_ActivityMetric, "activityEnd")
    descriptor = None
    for klass in MetricModel_ActivityMetric.__mro__:
        if "activityEnd" in klass.__dict__:
            descriptor = klass.__dict__["activityEnd"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel_activitymetric_has_activityBegin():
    assert hasattr(MetricModel_ActivityMetric, "activityBegin")
    descriptor = None
    for klass in MetricModel_ActivityMetric.__mro__:
        if "activityBegin" in klass.__dict__:
            descriptor = klass.__dict__["activityBegin"]
            break
    assert isinstance(descriptor, property)



def test_metricmodel_metric_is_not_abstract():
    assert not inspect.isabstract(MetricModel_Metric)


def test_metricmodel_metric_constructor_exists():
    assert callable(MetricModel_Metric.__init__)


def test_metricmodel_metric_constructor_args():
    sig = inspect.signature(MetricModel_Metric.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "description" in params, "Missing parameter 'description'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "form" in params, "Missing parameter 'form'"

def test_metricmodel_metric_has_name():
    assert hasattr(MetricModel_Metric, "name")
    descriptor = None
    for klass in MetricModel_Metric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel_metric_has_unit():
    assert hasattr(MetricModel_Metric, "unit")
    descriptor = None
    for klass in MetricModel_Metric.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel_metric_has_description():
    assert hasattr(MetricModel_Metric, "description")
    descriptor = None
    for klass in MetricModel_Metric.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel_metric_has_type():
    assert hasattr(MetricModel_Metric, "type")
    descriptor = None
    for klass in MetricModel_Metric.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel_metric_has_id():
    assert hasattr(MetricModel_Metric, "id")
    descriptor = None
    for klass in MetricModel_Metric.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel_metric_has_form():
    assert hasattr(MetricModel_Metric, "form")
    descriptor = None
    for klass in MetricModel_Metric.__mro__:
        if "form" in klass.__dict__:
            descriptor = klass.__dict__["form"]
            break
    assert isinstance(descriptor, property)

def test_colecttype_exists():
    # Check that the Enumeration exists
    assert ColectType is not None

def test_colecttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColectType]
    expected_literals = [
        "intercalated",
        "continuous",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColectType"

def test_baseelement_exists():
    # Check that the Enumeration exists
    assert BaseElement is not None

def test_baseelement_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BaseElement]
    expected_literals = [
        "Activity",
        "Task",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BaseElement"

def test_metricunit_exists():
    # Check that the Enumeration exists
    assert MetricUnit is not None

def test_metricunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MetricUnit]
    expected_literals = [
        "minutes",
        "uc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MetricUnit"

def test_metrictype_exists():
    # Check that the Enumeration exists
    assert MetricType is not None

def test_metrictype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MetricType]
    expected_literals = [
        "softData",
        "normalizedData",
        "hardData",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MetricType"


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
MetricModel_MetricPlanModel_strategy = st.builds(
    MetricModel_MetricPlanModel,
    name=
        safe_text
)
Metric_strategy = st.builds(
    Metric,
)
MetricModel_TaskMetric_strategy = st.builds(
    MetricModel_TaskMetric,
    tasksBase=
        safe_text
)
MetricModel_ActivityMetric_strategy = st.builds(
    MetricModel_ActivityMetric,
    activityEnd=
        safe_text,
    activityBegin=
        safe_text
)
MetricModel_Metric_strategy = st.builds(
    MetricModel_Metric,
    name=
        safe_text,
    unit=
        safe_text,
    description=
        safe_text,
    type=
        safe_text,
    id=
        safe_text,
    form=
        safe_text
)

@given(instance=MetricModel_MetricPlanModel_strategy)
@settings(max_examples=50)
def test_metricmodel_metricplanmodel_instantiation(instance):
    assert isinstance(instance, MetricModel_MetricPlanModel)



@given(instance=MetricModel_MetricPlanModel_strategy)
def test_metricmodel_metricplanmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Metric_strategy)
@settings(max_examples=50)
def test_metric_instantiation(instance):
    assert isinstance(instance, Metric)

@given(instance=MetricModel_TaskMetric_strategy)
@settings(max_examples=50)
def test_metricmodel_taskmetric_instantiation(instance):
    assert isinstance(instance, MetricModel_TaskMetric)



@given(instance=MetricModel_TaskMetric_strategy)
def test_metricmodel_taskmetric_tasksBase_setter(instance):
    original = instance.tasksBase
    instance.tasksBase = original
    assert instance.tasksBase == original

@given(instance=MetricModel_ActivityMetric_strategy)
@settings(max_examples=50)
def test_metricmodel_activitymetric_instantiation(instance):
    assert isinstance(instance, MetricModel_ActivityMetric)



@given(instance=MetricModel_ActivityMetric_strategy)
def test_metricmodel_activitymetric_activityEnd_setter(instance):
    original = instance.activityEnd
    instance.activityEnd = original
    assert instance.activityEnd == original



@given(instance=MetricModel_ActivityMetric_strategy)
def test_metricmodel_activitymetric_activityBegin_setter(instance):
    original = instance.activityBegin
    instance.activityBegin = original
    assert instance.activityBegin == original

@given(instance=MetricModel_Metric_strategy)
@settings(max_examples=50)
def test_metricmodel_metric_instantiation(instance):
    assert isinstance(instance, MetricModel_Metric)



@given(instance=MetricModel_Metric_strategy)
def test_metricmodel_metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MetricModel_Metric_strategy)
def test_metricmodel_metric_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=MetricModel_Metric_strategy)
def test_metricmodel_metric_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=MetricModel_Metric_strategy)
def test_metricmodel_metric_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MetricModel_Metric_strategy)
def test_metricmodel_metric_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=MetricModel_Metric_strategy)
def test_metricmodel_metric_form_setter(instance):
    original = instance.form
    instance.form = original
    assert instance.form == original

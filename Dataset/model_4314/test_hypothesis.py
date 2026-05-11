import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MetricModel::MetricPlanModel,
    Metric,
    MetricModel::TaskMetric,
    MetricModel::ActivityMetric,
    MetricModel::Metric,
    MetricUnit,
    MetricType,
    BaseElement,
    ColectType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metricmodel::metricplanmodel_is_not_abstract():
    assert not inspect.isabstract(MetricModel::MetricPlanModel)


def test_metricmodel::metricplanmodel_constructor_exists():
    assert callable(MetricModel::MetricPlanModel.__init__)


def test_metricmodel::metricplanmodel_constructor_args():
    sig = inspect.signature(MetricModel::MetricPlanModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metricmodel::metricplanmodel_has_name():
    assert hasattr(MetricModel::MetricPlanModel, "name")
    descriptor = None
    for klass in MetricModel::MetricPlanModel.__mro__:
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



def test_metricmodel::taskmetric_is_not_abstract():
    assert not inspect.isabstract(MetricModel::TaskMetric)


def test_metricmodel::taskmetric_constructor_exists():
    assert callable(MetricModel::TaskMetric.__init__)


def test_metricmodel::taskmetric_constructor_args():
    sig = inspect.signature(MetricModel::TaskMetric.__init__)
    params = list(sig.parameters.keys())
    assert "tasksBase" in params, "Missing parameter 'tasksBase'"

def test_metricmodel::taskmetric_has_tasksBase():
    assert hasattr(MetricModel::TaskMetric, "tasksBase")
    descriptor = None
    for klass in MetricModel::TaskMetric.__mro__:
        if "tasksBase" in klass.__dict__:
            descriptor = klass.__dict__["tasksBase"]
            break
    assert isinstance(descriptor, property)



def test_metricmodel::activitymetric_is_not_abstract():
    assert not inspect.isabstract(MetricModel::ActivityMetric)


def test_metricmodel::activitymetric_constructor_exists():
    assert callable(MetricModel::ActivityMetric.__init__)


def test_metricmodel::activitymetric_constructor_args():
    sig = inspect.signature(MetricModel::ActivityMetric.__init__)
    params = list(sig.parameters.keys())
    assert "activityEnd" in params, "Missing parameter 'activityEnd'"
    assert "activityBegin" in params, "Missing parameter 'activityBegin'"

def test_metricmodel::activitymetric_has_activityEnd():
    assert hasattr(MetricModel::ActivityMetric, "activityEnd")
    descriptor = None
    for klass in MetricModel::ActivityMetric.__mro__:
        if "activityEnd" in klass.__dict__:
            descriptor = klass.__dict__["activityEnd"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel::activitymetric_has_activityBegin():
    assert hasattr(MetricModel::ActivityMetric, "activityBegin")
    descriptor = None
    for klass in MetricModel::ActivityMetric.__mro__:
        if "activityBegin" in klass.__dict__:
            descriptor = klass.__dict__["activityBegin"]
            break
    assert isinstance(descriptor, property)



def test_metricmodel::metric_is_not_abstract():
    assert not inspect.isabstract(MetricModel::Metric)


def test_metricmodel::metric_constructor_exists():
    assert callable(MetricModel::Metric.__init__)


def test_metricmodel::metric_constructor_args():
    sig = inspect.signature(MetricModel::Metric.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "form" in params, "Missing parameter 'form'"
    assert "type" in params, "Missing parameter 'type'"

def test_metricmodel::metric_has_id():
    assert hasattr(MetricModel::Metric, "id")
    descriptor = None
    for klass in MetricModel::Metric.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel::metric_has_unit():
    assert hasattr(MetricModel::Metric, "unit")
    descriptor = None
    for klass in MetricModel::Metric.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel::metric_has_name():
    assert hasattr(MetricModel::Metric, "name")
    descriptor = None
    for klass in MetricModel::Metric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel::metric_has_description():
    assert hasattr(MetricModel::Metric, "description")
    descriptor = None
    for klass in MetricModel::Metric.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel::metric_has_form():
    assert hasattr(MetricModel::Metric, "form")
    descriptor = None
    for klass in MetricModel::Metric.__mro__:
        if "form" in klass.__dict__:
            descriptor = klass.__dict__["form"]
            break
    assert isinstance(descriptor, property)

def test_metricmodel::metric_has_type():
    assert hasattr(MetricModel::Metric, "type")
    descriptor = None
    for klass in MetricModel::Metric.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_metricunit_exists():
    # Check that the Enumeration exists
    assert MetricUnit is not None

def test_metricunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MetricUnit]
    expected_literals = [
        "uc",
        "minutes",
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
        "normalizedData",
        "softData",
        "hardData",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MetricType"

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

def test_colecttype_exists():
    # Check that the Enumeration exists
    assert ColectType is not None

def test_colecttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColectType]
    expected_literals = [
        "continuous",
        "intercalated",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColectType"


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
MetricModel::MetricPlanModel_strategy = st.builds(
    MetricModel::MetricPlanModel,
    name=
        safe_text
)
Metric_strategy = st.builds(
    Metric,
)
MetricModel::TaskMetric_strategy = st.builds(
    MetricModel::TaskMetric,
    tasksBase=
        safe_text
)
MetricModel::ActivityMetric_strategy = st.builds(
    MetricModel::ActivityMetric,
    activityEnd=
        safe_text,
    activityBegin=
        safe_text
)
MetricModel::Metric_strategy = st.builds(
    MetricModel::Metric,
    id=
        safe_text,
    unit=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    form=
        safe_text,
    type=
        safe_text
)

@given(instance=MetricModel::MetricPlanModel_strategy)
@settings(max_examples=50)
def test_metricmodel::metricplanmodel_instantiation(instance):
    assert isinstance(instance, MetricModel::MetricPlanModel)

@given(instance=MetricModel::MetricPlanModel_strategy)
def test_metricmodel::metricplanmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MetricModel::MetricPlanModel_strategy)
def test_metricmodel::metricplanmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Metric_strategy)
@settings(max_examples=50)
def test_metric_instantiation(instance):
    assert isinstance(instance, Metric)

@given(instance=MetricModel::TaskMetric_strategy)
@settings(max_examples=50)
def test_metricmodel::taskmetric_instantiation(instance):
    assert isinstance(instance, MetricModel::TaskMetric)

@given(instance=MetricModel::TaskMetric_strategy)
def test_metricmodel::taskmetric_tasksBase_type(instance):
    assert isinstance(instance.tasksBase, str)


@given(instance=MetricModel::TaskMetric_strategy)
def test_metricmodel::taskmetric_tasksBase_setter(instance):
    original = instance.tasksBase
    instance.tasksBase = original
    assert instance.tasksBase == original

@given(instance=MetricModel::ActivityMetric_strategy)
@settings(max_examples=50)
def test_metricmodel::activitymetric_instantiation(instance):
    assert isinstance(instance, MetricModel::ActivityMetric)

@given(instance=MetricModel::ActivityMetric_strategy)
def test_metricmodel::activitymetric_activityEnd_type(instance):
    assert isinstance(instance.activityEnd, str)


@given(instance=MetricModel::ActivityMetric_strategy)
def test_metricmodel::activitymetric_activityEnd_setter(instance):
    original = instance.activityEnd
    instance.activityEnd = original
    assert instance.activityEnd == original

@given(instance=MetricModel::ActivityMetric_strategy)
def test_metricmodel::activitymetric_activityBegin_type(instance):
    assert isinstance(instance.activityBegin, str)


@given(instance=MetricModel::ActivityMetric_strategy)
def test_metricmodel::activitymetric_activityBegin_setter(instance):
    original = instance.activityBegin
    instance.activityBegin = original
    assert instance.activityBegin == original

@given(instance=MetricModel::Metric_strategy)
@settings(max_examples=50)
def test_metricmodel::metric_instantiation(instance):
    assert isinstance(instance, MetricModel::Metric)

@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_form_type(instance):
    assert isinstance(instance.form, str)


@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_form_setter(instance):
    original = instance.form
    instance.form = original
    assert instance.form == original

@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MetricModel::Metric_strategy)
def test_metricmodel::metric_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

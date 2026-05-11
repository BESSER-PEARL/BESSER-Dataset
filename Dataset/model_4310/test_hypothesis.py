import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metricDSL::MetricAndWeight,
    MetricDefinition,
    metricDSL::StepwiseMetric,
    metricDSL::WeightedMetric,
    Number,
    metricDSL::Constant,
    metricDSL::Parameter,
    metricDSL::MetricDefinition,
    metricDSL::Number,
    Metric,
    metricDSL::InternalMetric,
    metricDSL::ExternalMetric,
    metricDSL::RatioMetric,
    metricDSL::BoundAndWeight,
    metricDSL::Metric,
    metricDSL::MetricModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metricdsl::metricandweight_is_not_abstract():
    assert not inspect.isabstract(metricDSL::MetricAndWeight)


def test_metricdsl::metricandweight_constructor_exists():
    assert callable(metricDSL::MetricAndWeight.__init__)


def test_metricdsl::metricandweight_constructor_args():
    sig = inspect.signature(metricDSL::MetricAndWeight.__init__)
    params = list(sig.parameters.keys())



def test_metricdefinition_is_not_abstract():
    assert not inspect.isabstract(MetricDefinition)


def test_metricdefinition_constructor_exists():
    assert callable(MetricDefinition.__init__)


def test_metricdefinition_constructor_args():
    sig = inspect.signature(MetricDefinition.__init__)
    params = list(sig.parameters.keys())



def test_metricdsl::stepwisemetric_is_not_abstract():
    assert not inspect.isabstract(metricDSL::StepwiseMetric)


def test_metricdsl::stepwisemetric_constructor_exists():
    assert callable(metricDSL::StepwiseMetric.__init__)


def test_metricdsl::stepwisemetric_constructor_args():
    sig = inspect.signature(metricDSL::StepwiseMetric.__init__)
    params = list(sig.parameters.keys())



def test_metricdsl::weightedmetric_is_not_abstract():
    assert not inspect.isabstract(metricDSL::WeightedMetric)


def test_metricdsl::weightedmetric_constructor_exists():
    assert callable(metricDSL::WeightedMetric.__init__)


def test_metricdsl::weightedmetric_constructor_args():
    sig = inspect.signature(metricDSL::WeightedMetric.__init__)
    params = list(sig.parameters.keys())



def test_number_is_not_abstract():
    assert not inspect.isabstract(Number)


def test_number_constructor_exists():
    assert callable(Number.__init__)


def test_number_constructor_args():
    sig = inspect.signature(Number.__init__)
    params = list(sig.parameters.keys())



def test_metricdsl::constant_is_not_abstract():
    assert not inspect.isabstract(metricDSL::Constant)


def test_metricdsl::constant_constructor_exists():
    assert callable(metricDSL::Constant.__init__)


def test_metricdsl::constant_constructor_args():
    sig = inspect.signature(metricDSL::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metricdsl::constant_has_value():
    assert hasattr(metricDSL::Constant, "value")
    descriptor = None
    for klass in metricDSL::Constant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metricdsl::parameter_is_not_abstract():
    assert not inspect.isabstract(metricDSL::Parameter)


def test_metricdsl::parameter_constructor_exists():
    assert callable(metricDSL::Parameter.__init__)


def test_metricdsl::parameter_constructor_args():
    sig = inspect.signature(metricDSL::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "shortname" in params, "Missing parameter 'shortname'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_metricdsl::parameter_has_description():
    assert hasattr(metricDSL::Parameter, "description")
    descriptor = None
    for klass in metricDSL::Parameter.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_metricdsl::parameter_has_shortname():
    assert hasattr(metricDSL::Parameter, "shortname")
    descriptor = None
    for klass in metricDSL::Parameter.__mro__:
        if "shortname" in klass.__dict__:
            descriptor = klass.__dict__["shortname"]
            break
    assert isinstance(descriptor, property)

def test_metricdsl::parameter_has_defaultValue():
    assert hasattr(metricDSL::Parameter, "defaultValue")
    descriptor = None
    for klass in metricDSL::Parameter.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_metricdsl::metricdefinition_is_not_abstract():
    assert not inspect.isabstract(metricDSL::MetricDefinition)


def test_metricdsl::metricdefinition_constructor_exists():
    assert callable(metricDSL::MetricDefinition.__init__)


def test_metricdsl::metricdefinition_constructor_args():
    sig = inspect.signature(metricDSL::MetricDefinition.__init__)
    params = list(sig.parameters.keys())



def test_metricdsl::number_is_not_abstract():
    assert not inspect.isabstract(metricDSL::Number)


def test_metricdsl::number_constructor_exists():
    assert callable(metricDSL::Number.__init__)


def test_metricdsl::number_constructor_args():
    sig = inspect.signature(metricDSL::Number.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metricdsl::number_has_name():
    assert hasattr(metricDSL::Number, "name")
    descriptor = None
    for klass in metricDSL::Number.__mro__:
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



def test_metricdsl::internalmetric_is_not_abstract():
    assert not inspect.isabstract(metricDSL::InternalMetric)


def test_metricdsl::internalmetric_constructor_exists():
    assert callable(metricDSL::InternalMetric.__init__)


def test_metricdsl::internalmetric_constructor_args():
    sig = inspect.signature(metricDSL::InternalMetric.__init__)
    params = list(sig.parameters.keys())
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "description" in params, "Missing parameter 'description'"

def test_metricdsl::internalmetric_has_shortName():
    assert hasattr(metricDSL::InternalMetric, "shortName")
    descriptor = None
    for klass in metricDSL::InternalMetric.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_metricdsl::internalmetric_has_description():
    assert hasattr(metricDSL::InternalMetric, "description")
    descriptor = None
    for klass in metricDSL::InternalMetric.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_metricdsl::externalmetric_is_not_abstract():
    assert not inspect.isabstract(metricDSL::ExternalMetric)


def test_metricdsl::externalmetric_constructor_exists():
    assert callable(metricDSL::ExternalMetric.__init__)


def test_metricdsl::externalmetric_constructor_args():
    sig = inspect.signature(metricDSL::ExternalMetric.__init__)
    params = list(sig.parameters.keys())



def test_metricdsl::ratiometric_is_not_abstract():
    assert not inspect.isabstract(metricDSL::RatioMetric)


def test_metricdsl::ratiometric_constructor_exists():
    assert callable(metricDSL::RatioMetric.__init__)


def test_metricdsl::ratiometric_constructor_args():
    sig = inspect.signature(metricDSL::RatioMetric.__init__)
    params = list(sig.parameters.keys())



def test_metricdsl::boundandweight_is_not_abstract():
    assert not inspect.isabstract(metricDSL::BoundAndWeight)


def test_metricdsl::boundandweight_constructor_exists():
    assert callable(metricDSL::BoundAndWeight.__init__)


def test_metricdsl::boundandweight_constructor_args():
    sig = inspect.signature(metricDSL::BoundAndWeight.__init__)
    params = list(sig.parameters.keys())



def test_metricdsl::metric_is_not_abstract():
    assert not inspect.isabstract(metricDSL::Metric)


def test_metricdsl::metric_constructor_exists():
    assert callable(metricDSL::Metric.__init__)


def test_metricdsl::metric_constructor_args():
    sig = inspect.signature(metricDSL::Metric.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metricdsl::metric_has_name():
    assert hasattr(metricDSL::Metric, "name")
    descriptor = None
    for klass in metricDSL::Metric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metricdsl::metricmodel_is_not_abstract():
    assert not inspect.isabstract(metricDSL::MetricModel)


def test_metricdsl::metricmodel_constructor_exists():
    assert callable(metricDSL::MetricModel.__init__)


def test_metricdsl::metricmodel_constructor_args():
    sig = inspect.signature(metricDSL::MetricModel.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_metricdsl::metricmodel_has_importURI():
    assert hasattr(metricDSL::MetricModel, "importURI")
    descriptor = None
    for klass in metricDSL::MetricModel.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
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
metricDSL::MetricAndWeight_strategy = st.builds(
    metricDSL::MetricAndWeight,
)
MetricDefinition_strategy = st.builds(
    MetricDefinition,
)
metricDSL::StepwiseMetric_strategy = st.builds(
    metricDSL::StepwiseMetric,
)
metricDSL::WeightedMetric_strategy = st.builds(
    metricDSL::WeightedMetric,
)
Number_strategy = st.builds(
    Number,
)
metricDSL::Constant_strategy = st.builds(
    metricDSL::Constant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
metricDSL::Parameter_strategy = st.builds(
    metricDSL::Parameter,
    description=
        safe_text,
    shortname=
        safe_text,
    defaultValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
metricDSL::MetricDefinition_strategy = st.builds(
    metricDSL::MetricDefinition,
)
metricDSL::Number_strategy = st.builds(
    metricDSL::Number,
    name=
        safe_text
)
Metric_strategy = st.builds(
    Metric,
)
metricDSL::InternalMetric_strategy = st.builds(
    metricDSL::InternalMetric,
    shortName=
        safe_text,
    description=
        safe_text
)
metricDSL::ExternalMetric_strategy = st.builds(
    metricDSL::ExternalMetric,
)
metricDSL::RatioMetric_strategy = st.builds(
    metricDSL::RatioMetric,
)
metricDSL::BoundAndWeight_strategy = st.builds(
    metricDSL::BoundAndWeight,
)
metricDSL::Metric_strategy = st.builds(
    metricDSL::Metric,
    name=
        safe_text
)
metricDSL::MetricModel_strategy = st.builds(
    metricDSL::MetricModel,
    importURI=
        safe_text
)

@given(instance=metricDSL::MetricAndWeight_strategy)
@settings(max_examples=50)
def test_metricdsl::metricandweight_instantiation(instance):
    assert isinstance(instance, metricDSL::MetricAndWeight)

@given(instance=MetricDefinition_strategy)
@settings(max_examples=50)
def test_metricdefinition_instantiation(instance):
    assert isinstance(instance, MetricDefinition)

@given(instance=metricDSL::StepwiseMetric_strategy)
@settings(max_examples=50)
def test_metricdsl::stepwisemetric_instantiation(instance):
    assert isinstance(instance, metricDSL::StepwiseMetric)

@given(instance=metricDSL::WeightedMetric_strategy)
@settings(max_examples=50)
def test_metricdsl::weightedmetric_instantiation(instance):
    assert isinstance(instance, metricDSL::WeightedMetric)

@given(instance=Number_strategy)
@settings(max_examples=50)
def test_number_instantiation(instance):
    assert isinstance(instance, Number)

@given(instance=metricDSL::Constant_strategy)
@settings(max_examples=50)
def test_metricdsl::constant_instantiation(instance):
    assert isinstance(instance, metricDSL::Constant)

@given(instance=metricDSL::Constant_strategy)
def test_metricdsl::constant_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=metricDSL::Constant_strategy)
def test_metricdsl::constant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metricDSL::Parameter_strategy)
@settings(max_examples=50)
def test_metricdsl::parameter_instantiation(instance):
    assert isinstance(instance, metricDSL::Parameter)

@given(instance=metricDSL::Parameter_strategy)
def test_metricdsl::parameter_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=metricDSL::Parameter_strategy)
def test_metricdsl::parameter_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=metricDSL::Parameter_strategy)
def test_metricdsl::parameter_shortname_type(instance):
    assert isinstance(instance.shortname, str)


@given(instance=metricDSL::Parameter_strategy)
def test_metricdsl::parameter_shortname_setter(instance):
    original = instance.shortname
    instance.shortname = original
    assert instance.shortname == original

@given(instance=metricDSL::Parameter_strategy)
def test_metricdsl::parameter_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, float)


@given(instance=metricDSL::Parameter_strategy)
def test_metricdsl::parameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=metricDSL::MetricDefinition_strategy)
@settings(max_examples=50)
def test_metricdsl::metricdefinition_instantiation(instance):
    assert isinstance(instance, metricDSL::MetricDefinition)

@given(instance=metricDSL::Number_strategy)
@settings(max_examples=50)
def test_metricdsl::number_instantiation(instance):
    assert isinstance(instance, metricDSL::Number)

@given(instance=metricDSL::Number_strategy)
def test_metricdsl::number_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metricDSL::Number_strategy)
def test_metricdsl::number_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Metric_strategy)
@settings(max_examples=50)
def test_metric_instantiation(instance):
    assert isinstance(instance, Metric)

@given(instance=metricDSL::InternalMetric_strategy)
@settings(max_examples=50)
def test_metricdsl::internalmetric_instantiation(instance):
    assert isinstance(instance, metricDSL::InternalMetric)

@given(instance=metricDSL::InternalMetric_strategy)
def test_metricdsl::internalmetric_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=metricDSL::InternalMetric_strategy)
def test_metricdsl::internalmetric_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=metricDSL::InternalMetric_strategy)
def test_metricdsl::internalmetric_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=metricDSL::InternalMetric_strategy)
def test_metricdsl::internalmetric_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=metricDSL::ExternalMetric_strategy)
@settings(max_examples=50)
def test_metricdsl::externalmetric_instantiation(instance):
    assert isinstance(instance, metricDSL::ExternalMetric)

@given(instance=metricDSL::RatioMetric_strategy)
@settings(max_examples=50)
def test_metricdsl::ratiometric_instantiation(instance):
    assert isinstance(instance, metricDSL::RatioMetric)

@given(instance=metricDSL::BoundAndWeight_strategy)
@settings(max_examples=50)
def test_metricdsl::boundandweight_instantiation(instance):
    assert isinstance(instance, metricDSL::BoundAndWeight)

@given(instance=metricDSL::Metric_strategy)
@settings(max_examples=50)
def test_metricdsl::metric_instantiation(instance):
    assert isinstance(instance, metricDSL::Metric)

@given(instance=metricDSL::Metric_strategy)
def test_metricdsl::metric_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metricDSL::Metric_strategy)
def test_metricdsl::metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metricDSL::MetricModel_strategy)
@settings(max_examples=50)
def test_metricdsl::metricmodel_instantiation(instance):
    assert isinstance(instance, metricDSL::MetricModel)

@given(instance=metricDSL::MetricModel_strategy)
def test_metricdsl::metricmodel_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=metricDSL::MetricModel_strategy)
def test_metricdsl::metricmodel_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

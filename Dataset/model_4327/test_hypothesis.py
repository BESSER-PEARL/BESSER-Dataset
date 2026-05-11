import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    QualityMetamodel::EnumerationItem,
    ValueType,
    QualityMetamodel::EnumerationMetric,
    QualityMetamodel::IntegerValueType,
    QualityMetamodel::RealValueType,
    QualityMetamodel::BooleanValueType,
    QualityMetamodel::RangeValueType,
    QualityMetamodel::AggregatedValueMetric,
    QualityMetamodel::TextValueType,
    QualityMetamodel::Value,
    QualityMetamodel::QualityAttribute,
    QualityMetamodel::ValueType,
    QualityMetamodel::MetricProvider,
    QualityMetamodel::QualityModel,
    QualityMetamodel::Operation,
    Value,
    QualityMetamodel::AggregatedValue,
    QualityMetamodel::SingleValue,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qualitymetamodel::enumerationitem_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::EnumerationItem)


def test_qualitymetamodel::enumerationitem_constructor_exists():
    assert callable(QualityMetamodel::EnumerationItem.__init__)


def test_qualitymetamodel::enumerationitem_constructor_args():
    sig = inspect.signature(QualityMetamodel::EnumerationItem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::enumerationitem_has_name():
    assert hasattr(QualityMetamodel::EnumerationItem, "name")
    descriptor = None
    for klass in QualityMetamodel::EnumerationItem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::enumerationmetric_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::EnumerationMetric)


def test_qualitymetamodel::enumerationmetric_constructor_exists():
    assert callable(QualityMetamodel::EnumerationMetric.__init__)


def test_qualitymetamodel::enumerationmetric_constructor_args():
    sig = inspect.signature(QualityMetamodel::EnumerationMetric.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::integervaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::IntegerValueType)


def test_qualitymetamodel::integervaluetype_constructor_exists():
    assert callable(QualityMetamodel::IntegerValueType.__init__)


def test_qualitymetamodel::integervaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::IntegerValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel::integervaluetype_has_value():
    assert hasattr(QualityMetamodel::IntegerValueType, "value")
    descriptor = None
    for klass in QualityMetamodel::IntegerValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::realvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::RealValueType)


def test_qualitymetamodel::realvaluetype_constructor_exists():
    assert callable(QualityMetamodel::RealValueType.__init__)


def test_qualitymetamodel::realvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::RealValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel::realvaluetype_has_value():
    assert hasattr(QualityMetamodel::RealValueType, "value")
    descriptor = None
    for klass in QualityMetamodel::RealValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::booleanvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::BooleanValueType)


def test_qualitymetamodel::booleanvaluetype_constructor_exists():
    assert callable(QualityMetamodel::BooleanValueType.__init__)


def test_qualitymetamodel::booleanvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::BooleanValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel::booleanvaluetype_has_value():
    assert hasattr(QualityMetamodel::BooleanValueType, "value")
    descriptor = None
    for klass in QualityMetamodel::BooleanValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::rangevaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::RangeValueType)


def test_qualitymetamodel::rangevaluetype_constructor_exists():
    assert callable(QualityMetamodel::RangeValueType.__init__)


def test_qualitymetamodel::rangevaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::RangeValueType.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_qualitymetamodel::rangevaluetype_has_min():
    assert hasattr(QualityMetamodel::RangeValueType, "min")
    descriptor = None
    for klass in QualityMetamodel::RangeValueType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::rangevaluetype_has_max():
    assert hasattr(QualityMetamodel::RangeValueType, "max")
    descriptor = None
    for klass in QualityMetamodel::RangeValueType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::aggregatedvaluemetric_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::AggregatedValueMetric)


def test_qualitymetamodel::aggregatedvaluemetric_constructor_exists():
    assert callable(QualityMetamodel::AggregatedValueMetric.__init__)


def test_qualitymetamodel::aggregatedvaluemetric_constructor_args():
    sig = inspect.signature(QualityMetamodel::AggregatedValueMetric.__init__)
    params = list(sig.parameters.keys())
    assert "average" in params, "Missing parameter 'average'"
    assert "standardDeviation" in params, "Missing parameter 'standardDeviation'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "median" in params, "Missing parameter 'median'"

def test_qualitymetamodel::aggregatedvaluemetric_has_average():
    assert hasattr(QualityMetamodel::AggregatedValueMetric, "average")
    descriptor = None
    for klass in QualityMetamodel::AggregatedValueMetric.__mro__:
        if "average" in klass.__dict__:
            descriptor = klass.__dict__["average"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::aggregatedvaluemetric_has_standardDeviation():
    assert hasattr(QualityMetamodel::AggregatedValueMetric, "standardDeviation")
    descriptor = None
    for klass in QualityMetamodel::AggregatedValueMetric.__mro__:
        if "standardDeviation" in klass.__dict__:
            descriptor = klass.__dict__["standardDeviation"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::aggregatedvaluemetric_has_maximum():
    assert hasattr(QualityMetamodel::AggregatedValueMetric, "maximum")
    descriptor = None
    for klass in QualityMetamodel::AggregatedValueMetric.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::aggregatedvaluemetric_has_minimum():
    assert hasattr(QualityMetamodel::AggregatedValueMetric, "minimum")
    descriptor = None
    for klass in QualityMetamodel::AggregatedValueMetric.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::aggregatedvaluemetric_has_median():
    assert hasattr(QualityMetamodel::AggregatedValueMetric, "median")
    descriptor = None
    for klass in QualityMetamodel::AggregatedValueMetric.__mro__:
        if "median" in klass.__dict__:
            descriptor = klass.__dict__["median"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::textvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::TextValueType)


def test_qualitymetamodel::textvaluetype_constructor_exists():
    assert callable(QualityMetamodel::TextValueType.__init__)


def test_qualitymetamodel::textvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::TextValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel::textvaluetype_has_value():
    assert hasattr(QualityMetamodel::TextValueType, "value")
    descriptor = None
    for klass in QualityMetamodel::TextValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::value_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::Value)


def test_qualitymetamodel::value_constructor_exists():
    assert callable(QualityMetamodel::Value.__init__)


def test_qualitymetamodel::value_constructor_args():
    sig = inspect.signature(QualityMetamodel::Value.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_qualitymetamodel::value_has_name():
    assert hasattr(QualityMetamodel::Value, "name")
    descriptor = None
    for klass in QualityMetamodel::Value.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::value_has_description():
    assert hasattr(QualityMetamodel::Value, "description")
    descriptor = None
    for klass in QualityMetamodel::Value.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qualityattribute_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QualityAttribute)


def test_qualitymetamodel::qualityattribute_constructor_exists():
    assert callable(QualityMetamodel::QualityAttribute.__init__)


def test_qualitymetamodel::qualityattribute_constructor_args():
    sig = inspect.signature(QualityMetamodel::QualityAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::qualityattribute_has_name():
    assert hasattr(QualityMetamodel::QualityAttribute, "name")
    descriptor = None
    for klass in QualityMetamodel::QualityAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::valuetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::ValueType)


def test_qualitymetamodel::valuetype_constructor_exists():
    assert callable(QualityMetamodel::ValueType.__init__)


def test_qualitymetamodel::valuetype_constructor_args():
    sig = inspect.signature(QualityMetamodel::ValueType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::valuetype_has_name():
    assert hasattr(QualityMetamodel::ValueType, "name")
    descriptor = None
    for klass in QualityMetamodel::ValueType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::metricprovider_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::MetricProvider)


def test_qualitymetamodel::metricprovider_constructor_exists():
    assert callable(QualityMetamodel::MetricProvider.__init__)


def test_qualitymetamodel::metricprovider_constructor_args():
    sig = inspect.signature(QualityMetamodel::MetricProvider.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"

def test_qualitymetamodel::metricprovider_has_name():
    assert hasattr(QualityMetamodel::MetricProvider, "name")
    descriptor = None
    for klass in QualityMetamodel::MetricProvider.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::metricprovider_has_description():
    assert hasattr(QualityMetamodel::MetricProvider, "description")
    descriptor = None
    for klass in QualityMetamodel::MetricProvider.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::metricprovider_has_id():
    assert hasattr(QualityMetamodel::MetricProvider, "id")
    descriptor = None
    for klass in QualityMetamodel::MetricProvider.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::qualitymodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::QualityModel)


def test_qualitymetamodel::qualitymodel_constructor_exists():
    assert callable(QualityMetamodel::QualityModel.__init__)


def test_qualitymetamodel::qualitymodel_constructor_args():
    sig = inspect.signature(QualityMetamodel::QualityModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel::qualitymodel_has_name():
    assert hasattr(QualityMetamodel::QualityModel, "name")
    descriptor = None
    for klass in QualityMetamodel::QualityModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel::operation_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::Operation)


def test_qualitymetamodel::operation_constructor_exists():
    assert callable(QualityMetamodel::Operation.__init__)


def test_qualitymetamodel::operation_constructor_args():
    sig = inspect.signature(QualityMetamodel::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_qualitymetamodel::operation_has_name():
    assert hasattr(QualityMetamodel::Operation, "name")
    descriptor = None
    for klass in QualityMetamodel::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel::operation_has_body():
    assert hasattr(QualityMetamodel::Operation, "body")
    descriptor = None
    for klass in QualityMetamodel::Operation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::aggregatedvalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::AggregatedValue)


def test_qualitymetamodel::aggregatedvalue_constructor_exists():
    assert callable(QualityMetamodel::AggregatedValue.__init__)


def test_qualitymetamodel::aggregatedvalue_constructor_args():
    sig = inspect.signature(QualityMetamodel::AggregatedValue.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel::singlevalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel::SingleValue)


def test_qualitymetamodel::singlevalue_constructor_exists():
    assert callable(QualityMetamodel::SingleValue.__init__)


def test_qualitymetamodel::singlevalue_constructor_args():
    sig = inspect.signature(QualityMetamodel::SingleValue.__init__)
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
QualityMetamodel::EnumerationItem_strategy = st.builds(
    QualityMetamodel::EnumerationItem,
    name=
        safe_text
)
ValueType_strategy = st.builds(
    ValueType,
)
QualityMetamodel::EnumerationMetric_strategy = st.builds(
    QualityMetamodel::EnumerationMetric,
)
QualityMetamodel::IntegerValueType_strategy = st.builds(
    QualityMetamodel::IntegerValueType,
    value=
        safe_text
)
QualityMetamodel::RealValueType_strategy = st.builds(
    QualityMetamodel::RealValueType,
    value=
        safe_text
)
QualityMetamodel::BooleanValueType_strategy = st.builds(
    QualityMetamodel::BooleanValueType,
    value=
        safe_text
)
QualityMetamodel::RangeValueType_strategy = st.builds(
    QualityMetamodel::RangeValueType,
    min=
        safe_text,
    max=
        safe_text
)
QualityMetamodel::AggregatedValueMetric_strategy = st.builds(
    QualityMetamodel::AggregatedValueMetric,
    average=
        safe_text,
    standardDeviation=
        safe_text,
    maximum=
        safe_text,
    minimum=
        safe_text,
    median=
        safe_text
)
QualityMetamodel::TextValueType_strategy = st.builds(
    QualityMetamodel::TextValueType,
    value=
        safe_text
)
QualityMetamodel::Value_strategy = st.builds(
    QualityMetamodel::Value,
    name=
        safe_text,
    description=
        safe_text
)
QualityMetamodel::QualityAttribute_strategy = st.builds(
    QualityMetamodel::QualityAttribute,
    name=
        safe_text
)
QualityMetamodel::ValueType_strategy = st.builds(
    QualityMetamodel::ValueType,
    name=
        safe_text
)
QualityMetamodel::MetricProvider_strategy = st.builds(
    QualityMetamodel::MetricProvider,
    name=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)
QualityMetamodel::QualityModel_strategy = st.builds(
    QualityMetamodel::QualityModel,
    name=
        safe_text
)
QualityMetamodel::Operation_strategy = st.builds(
    QualityMetamodel::Operation,
    name=
        safe_text,
    body=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
QualityMetamodel::AggregatedValue_strategy = st.builds(
    QualityMetamodel::AggregatedValue,
)
QualityMetamodel::SingleValue_strategy = st.builds(
    QualityMetamodel::SingleValue,
)

@given(instance=QualityMetamodel::EnumerationItem_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::enumerationitem_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::EnumerationItem)

@given(instance=QualityMetamodel::EnumerationItem_strategy)
def test_qualitymetamodel::enumerationitem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::EnumerationItem_strategy)
def test_qualitymetamodel::enumerationitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=QualityMetamodel::EnumerationMetric_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::enumerationmetric_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::EnumerationMetric)

@given(instance=QualityMetamodel::IntegerValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::integervaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::IntegerValueType)

@given(instance=QualityMetamodel::IntegerValueType_strategy)
def test_qualitymetamodel::integervaluetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=QualityMetamodel::IntegerValueType_strategy)
def test_qualitymetamodel::integervaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel::RealValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::realvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::RealValueType)

@given(instance=QualityMetamodel::RealValueType_strategy)
def test_qualitymetamodel::realvaluetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=QualityMetamodel::RealValueType_strategy)
def test_qualitymetamodel::realvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel::BooleanValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::booleanvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::BooleanValueType)

@given(instance=QualityMetamodel::BooleanValueType_strategy)
def test_qualitymetamodel::booleanvaluetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=QualityMetamodel::BooleanValueType_strategy)
def test_qualitymetamodel::booleanvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel::RangeValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::rangevaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::RangeValueType)

@given(instance=QualityMetamodel::RangeValueType_strategy)
def test_qualitymetamodel::rangevaluetype_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=QualityMetamodel::RangeValueType_strategy)
def test_qualitymetamodel::rangevaluetype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=QualityMetamodel::RangeValueType_strategy)
def test_qualitymetamodel::rangevaluetype_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=QualityMetamodel::RangeValueType_strategy)
def test_qualitymetamodel::rangevaluetype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::aggregatedvaluemetric_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::AggregatedValueMetric)

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_average_type(instance):
    assert isinstance(instance.average, str)


@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_average_setter(instance):
    original = instance.average
    instance.average = original
    assert instance.average == original

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_standardDeviation_type(instance):
    assert isinstance(instance.standardDeviation, str)


@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_standardDeviation_setter(instance):
    original = instance.standardDeviation
    instance.standardDeviation = original
    assert instance.standardDeviation == original

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_maximum_type(instance):
    assert isinstance(instance.maximum, str)


@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_minimum_type(instance):
    assert isinstance(instance.minimum, str)


@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original

@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_median_type(instance):
    assert isinstance(instance.median, str)


@given(instance=QualityMetamodel::AggregatedValueMetric_strategy)
def test_qualitymetamodel::aggregatedvaluemetric_median_setter(instance):
    original = instance.median
    instance.median = original
    assert instance.median == original

@given(instance=QualityMetamodel::TextValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::textvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::TextValueType)

@given(instance=QualityMetamodel::TextValueType_strategy)
def test_qualitymetamodel::textvaluetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=QualityMetamodel::TextValueType_strategy)
def test_qualitymetamodel::textvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel::Value_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::value_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::Value)

@given(instance=QualityMetamodel::Value_strategy)
def test_qualitymetamodel::value_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::Value_strategy)
def test_qualitymetamodel::value_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::Value_strategy)
def test_qualitymetamodel::value_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=QualityMetamodel::Value_strategy)
def test_qualitymetamodel::value_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=QualityMetamodel::QualityAttribute_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qualityattribute_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QualityAttribute)

@given(instance=QualityMetamodel::QualityAttribute_strategy)
def test_qualitymetamodel::qualityattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::QualityAttribute_strategy)
def test_qualitymetamodel::qualityattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::ValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::valuetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::ValueType)

@given(instance=QualityMetamodel::ValueType_strategy)
def test_qualitymetamodel::valuetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::ValueType_strategy)
def test_qualitymetamodel::valuetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::MetricProvider_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::metricprovider_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::MetricProvider)

@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=QualityMetamodel::MetricProvider_strategy)
def test_qualitymetamodel::metricprovider_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=QualityMetamodel::QualityModel_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::qualitymodel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::QualityModel)

@given(instance=QualityMetamodel::QualityModel_strategy)
def test_qualitymetamodel::qualitymodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::QualityModel_strategy)
def test_qualitymetamodel::qualitymodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::Operation_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::operation_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::Operation)

@given(instance=QualityMetamodel::Operation_strategy)
def test_qualitymetamodel::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=QualityMetamodel::Operation_strategy)
def test_qualitymetamodel::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel::Operation_strategy)
def test_qualitymetamodel::operation_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=QualityMetamodel::Operation_strategy)
def test_qualitymetamodel::operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=QualityMetamodel::AggregatedValue_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::aggregatedvalue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::AggregatedValue)

@given(instance=QualityMetamodel::SingleValue_strategy)
@settings(max_examples=50)
def test_qualitymetamodel::singlevalue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel::SingleValue)

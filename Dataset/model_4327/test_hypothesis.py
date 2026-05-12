import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    QualityMetamodel_EnumerationItem,
    ValueType,
    QualityMetamodel_IntegerValueType,
    QualityMetamodel_AggregatedValueMetric,
    QualityMetamodel_BooleanValueType,
    QualityMetamodel_RangeValueType,
    QualityMetamodel_EnumerationMetric,
    QualityMetamodel_RealValueType,
    QualityMetamodel_TextValueType,
    QualityMetamodel_Value,
    QualityMetamodel_QualityAttribute,
    QualityMetamodel_ValueType,
    QualityMetamodel_MetricProvider,
    QualityMetamodel_QualityModel,
    QualityMetamodel_Operation,
    Value,
    QualityMetamodel_AggregatedValue,
    QualityMetamodel_SingleValue,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qualitymetamodel_enumerationitem_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_EnumerationItem)


def test_qualitymetamodel_enumerationitem_constructor_exists():
    assert callable(QualityMetamodel_EnumerationItem.__init__)


def test_qualitymetamodel_enumerationitem_constructor_args():
    sig = inspect.signature(QualityMetamodel_EnumerationItem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_enumerationitem_has_name():
    assert hasattr(QualityMetamodel_EnumerationItem, "name")
    descriptor = None
    for klass in QualityMetamodel_EnumerationItem.__mro__:
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



def test_qualitymetamodel_integervaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_IntegerValueType)


def test_qualitymetamodel_integervaluetype_constructor_exists():
    assert callable(QualityMetamodel_IntegerValueType.__init__)


def test_qualitymetamodel_integervaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_IntegerValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel_integervaluetype_has_value():
    assert hasattr(QualityMetamodel_IntegerValueType, "value")
    descriptor = None
    for klass in QualityMetamodel_IntegerValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_aggregatedvaluemetric_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_AggregatedValueMetric)


def test_qualitymetamodel_aggregatedvaluemetric_constructor_exists():
    assert callable(QualityMetamodel_AggregatedValueMetric.__init__)


def test_qualitymetamodel_aggregatedvaluemetric_constructor_args():
    sig = inspect.signature(QualityMetamodel_AggregatedValueMetric.__init__)
    params = list(sig.parameters.keys())
    assert "standardDeviation" in params, "Missing parameter 'standardDeviation'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "average" in params, "Missing parameter 'average'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "median" in params, "Missing parameter 'median'"

def test_qualitymetamodel_aggregatedvaluemetric_has_standardDeviation():
    assert hasattr(QualityMetamodel_AggregatedValueMetric, "standardDeviation")
    descriptor = None
    for klass in QualityMetamodel_AggregatedValueMetric.__mro__:
        if "standardDeviation" in klass.__dict__:
            descriptor = klass.__dict__["standardDeviation"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_aggregatedvaluemetric_has_minimum():
    assert hasattr(QualityMetamodel_AggregatedValueMetric, "minimum")
    descriptor = None
    for klass in QualityMetamodel_AggregatedValueMetric.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_aggregatedvaluemetric_has_average():
    assert hasattr(QualityMetamodel_AggregatedValueMetric, "average")
    descriptor = None
    for klass in QualityMetamodel_AggregatedValueMetric.__mro__:
        if "average" in klass.__dict__:
            descriptor = klass.__dict__["average"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_aggregatedvaluemetric_has_maximum():
    assert hasattr(QualityMetamodel_AggregatedValueMetric, "maximum")
    descriptor = None
    for klass in QualityMetamodel_AggregatedValueMetric.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_aggregatedvaluemetric_has_median():
    assert hasattr(QualityMetamodel_AggregatedValueMetric, "median")
    descriptor = None
    for klass in QualityMetamodel_AggregatedValueMetric.__mro__:
        if "median" in klass.__dict__:
            descriptor = klass.__dict__["median"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_booleanvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_BooleanValueType)


def test_qualitymetamodel_booleanvaluetype_constructor_exists():
    assert callable(QualityMetamodel_BooleanValueType.__init__)


def test_qualitymetamodel_booleanvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_BooleanValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel_booleanvaluetype_has_value():
    assert hasattr(QualityMetamodel_BooleanValueType, "value")
    descriptor = None
    for klass in QualityMetamodel_BooleanValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_rangevaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_RangeValueType)


def test_qualitymetamodel_rangevaluetype_constructor_exists():
    assert callable(QualityMetamodel_RangeValueType.__init__)


def test_qualitymetamodel_rangevaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_RangeValueType.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_qualitymetamodel_rangevaluetype_has_max():
    assert hasattr(QualityMetamodel_RangeValueType, "max")
    descriptor = None
    for klass in QualityMetamodel_RangeValueType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_rangevaluetype_has_min():
    assert hasattr(QualityMetamodel_RangeValueType, "min")
    descriptor = None
    for klass in QualityMetamodel_RangeValueType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_enumerationmetric_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_EnumerationMetric)


def test_qualitymetamodel_enumerationmetric_constructor_exists():
    assert callable(QualityMetamodel_EnumerationMetric.__init__)


def test_qualitymetamodel_enumerationmetric_constructor_args():
    sig = inspect.signature(QualityMetamodel_EnumerationMetric.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_realvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_RealValueType)


def test_qualitymetamodel_realvaluetype_constructor_exists():
    assert callable(QualityMetamodel_RealValueType.__init__)


def test_qualitymetamodel_realvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_RealValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel_realvaluetype_has_value():
    assert hasattr(QualityMetamodel_RealValueType, "value")
    descriptor = None
    for klass in QualityMetamodel_RealValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_textvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_TextValueType)


def test_qualitymetamodel_textvaluetype_constructor_exists():
    assert callable(QualityMetamodel_TextValueType.__init__)


def test_qualitymetamodel_textvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_TextValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_qualitymetamodel_textvaluetype_has_value():
    assert hasattr(QualityMetamodel_TextValueType, "value")
    descriptor = None
    for klass in QualityMetamodel_TextValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_value_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_Value)


def test_qualitymetamodel_value_constructor_exists():
    assert callable(QualityMetamodel_Value.__init__)


def test_qualitymetamodel_value_constructor_args():
    sig = inspect.signature(QualityMetamodel_Value.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_qualitymetamodel_value_has_name():
    assert hasattr(QualityMetamodel_Value, "name")
    descriptor = None
    for klass in QualityMetamodel_Value.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_value_has_description():
    assert hasattr(QualityMetamodel_Value, "description")
    descriptor = None
    for klass in QualityMetamodel_Value.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qualityattribute_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QualityAttribute)


def test_qualitymetamodel_qualityattribute_constructor_exists():
    assert callable(QualityMetamodel_QualityAttribute.__init__)


def test_qualitymetamodel_qualityattribute_constructor_args():
    sig = inspect.signature(QualityMetamodel_QualityAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_qualityattribute_has_name():
    assert hasattr(QualityMetamodel_QualityAttribute, "name")
    descriptor = None
    for klass in QualityMetamodel_QualityAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_valuetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_ValueType)


def test_qualitymetamodel_valuetype_constructor_exists():
    assert callable(QualityMetamodel_ValueType.__init__)


def test_qualitymetamodel_valuetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_ValueType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_valuetype_has_name():
    assert hasattr(QualityMetamodel_ValueType, "name")
    descriptor = None
    for klass in QualityMetamodel_ValueType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_metricprovider_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_MetricProvider)


def test_qualitymetamodel_metricprovider_constructor_exists():
    assert callable(QualityMetamodel_MetricProvider.__init__)


def test_qualitymetamodel_metricprovider_constructor_args():
    sig = inspect.signature(QualityMetamodel_MetricProvider.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_metricprovider_has_description():
    assert hasattr(QualityMetamodel_MetricProvider, "description")
    descriptor = None
    for klass in QualityMetamodel_MetricProvider.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_metricprovider_has_id():
    assert hasattr(QualityMetamodel_MetricProvider, "id")
    descriptor = None
    for klass in QualityMetamodel_MetricProvider.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_metricprovider_has_name():
    assert hasattr(QualityMetamodel_MetricProvider, "name")
    descriptor = None
    for klass in QualityMetamodel_MetricProvider.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_qualitymodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QualityModel)


def test_qualitymetamodel_qualitymodel_constructor_exists():
    assert callable(QualityMetamodel_QualityModel.__init__)


def test_qualitymetamodel_qualitymodel_constructor_args():
    sig = inspect.signature(QualityMetamodel_QualityModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qualitymetamodel_qualitymodel_has_name():
    assert hasattr(QualityMetamodel_QualityModel, "name")
    descriptor = None
    for klass in QualityMetamodel_QualityModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qualitymetamodel_operation_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_Operation)


def test_qualitymetamodel_operation_constructor_exists():
    assert callable(QualityMetamodel_Operation.__init__)


def test_qualitymetamodel_operation_constructor_args():
    sig = inspect.signature(QualityMetamodel_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"

def test_qualitymetamodel_operation_has_name():
    assert hasattr(QualityMetamodel_Operation, "name")
    descriptor = None
    for klass in QualityMetamodel_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_qualitymetamodel_operation_has_body():
    assert hasattr(QualityMetamodel_Operation, "body")
    descriptor = None
    for klass in QualityMetamodel_Operation.__mro__:
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



def test_qualitymetamodel_aggregatedvalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_AggregatedValue)


def test_qualitymetamodel_aggregatedvalue_constructor_exists():
    assert callable(QualityMetamodel_AggregatedValue.__init__)


def test_qualitymetamodel_aggregatedvalue_constructor_args():
    sig = inspect.signature(QualityMetamodel_AggregatedValue.__init__)
    params = list(sig.parameters.keys())



def test_qualitymetamodel_singlevalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_SingleValue)


def test_qualitymetamodel_singlevalue_constructor_exists():
    assert callable(QualityMetamodel_SingleValue.__init__)


def test_qualitymetamodel_singlevalue_constructor_args():
    sig = inspect.signature(QualityMetamodel_SingleValue.__init__)
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
QualityMetamodel_EnumerationItem_strategy = st.builds(
    QualityMetamodel_EnumerationItem,
    name=
        safe_text
)
ValueType_strategy = st.builds(
    ValueType,
)
QualityMetamodel_IntegerValueType_strategy = st.builds(
    QualityMetamodel_IntegerValueType,
    value=
        safe_text
)
QualityMetamodel_AggregatedValueMetric_strategy = st.builds(
    QualityMetamodel_AggregatedValueMetric,
    standardDeviation=
        safe_text,
    minimum=
        safe_text,
    average=
        safe_text,
    maximum=
        safe_text,
    median=
        safe_text
)
QualityMetamodel_BooleanValueType_strategy = st.builds(
    QualityMetamodel_BooleanValueType,
    value=
        safe_text
)
QualityMetamodel_RangeValueType_strategy = st.builds(
    QualityMetamodel_RangeValueType,
    max=
        safe_text,
    min=
        safe_text
)
QualityMetamodel_EnumerationMetric_strategy = st.builds(
    QualityMetamodel_EnumerationMetric,
)
QualityMetamodel_RealValueType_strategy = st.builds(
    QualityMetamodel_RealValueType,
    value=
        safe_text
)
QualityMetamodel_TextValueType_strategy = st.builds(
    QualityMetamodel_TextValueType,
    value=
        safe_text
)
QualityMetamodel_Value_strategy = st.builds(
    QualityMetamodel_Value,
    name=
        safe_text,
    description=
        safe_text
)
QualityMetamodel_QualityAttribute_strategy = st.builds(
    QualityMetamodel_QualityAttribute,
    name=
        safe_text
)
QualityMetamodel_ValueType_strategy = st.builds(
    QualityMetamodel_ValueType,
    name=
        safe_text
)
QualityMetamodel_MetricProvider_strategy = st.builds(
    QualityMetamodel_MetricProvider,
    description=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
QualityMetamodel_QualityModel_strategy = st.builds(
    QualityMetamodel_QualityModel,
    name=
        safe_text
)
QualityMetamodel_Operation_strategy = st.builds(
    QualityMetamodel_Operation,
    name=
        safe_text,
    body=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
QualityMetamodel_AggregatedValue_strategy = st.builds(
    QualityMetamodel_AggregatedValue,
)
QualityMetamodel_SingleValue_strategy = st.builds(
    QualityMetamodel_SingleValue,
)

@given(instance=QualityMetamodel_EnumerationItem_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_enumerationitem_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_EnumerationItem)



@given(instance=QualityMetamodel_EnumerationItem_strategy)
def test_qualitymetamodel_enumerationitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=QualityMetamodel_IntegerValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_integervaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_IntegerValueType)



@given(instance=QualityMetamodel_IntegerValueType_strategy)
def test_qualitymetamodel_integervaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_aggregatedvaluemetric_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_AggregatedValueMetric)



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_qualitymetamodel_aggregatedvaluemetric_standardDeviation_setter(instance):
    original = instance.standardDeviation
    instance.standardDeviation = original
    assert instance.standardDeviation == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_qualitymetamodel_aggregatedvaluemetric_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_qualitymetamodel_aggregatedvaluemetric_average_setter(instance):
    original = instance.average
    instance.average = original
    assert instance.average == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_qualitymetamodel_aggregatedvaluemetric_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_qualitymetamodel_aggregatedvaluemetric_median_setter(instance):
    original = instance.median
    instance.median = original
    assert instance.median == original

@given(instance=QualityMetamodel_BooleanValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_booleanvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_BooleanValueType)



@given(instance=QualityMetamodel_BooleanValueType_strategy)
def test_qualitymetamodel_booleanvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel_RangeValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_rangevaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_RangeValueType)



@given(instance=QualityMetamodel_RangeValueType_strategy)
def test_qualitymetamodel_rangevaluetype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=QualityMetamodel_RangeValueType_strategy)
def test_qualitymetamodel_rangevaluetype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=QualityMetamodel_EnumerationMetric_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_enumerationmetric_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_EnumerationMetric)

@given(instance=QualityMetamodel_RealValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_realvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_RealValueType)



@given(instance=QualityMetamodel_RealValueType_strategy)
def test_qualitymetamodel_realvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel_TextValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_textvaluetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_TextValueType)



@given(instance=QualityMetamodel_TextValueType_strategy)
def test_qualitymetamodel_textvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QualityMetamodel_Value_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_value_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_Value)



@given(instance=QualityMetamodel_Value_strategy)
def test_qualitymetamodel_value_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=QualityMetamodel_Value_strategy)
def test_qualitymetamodel_value_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=QualityMetamodel_QualityAttribute_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qualityattribute_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QualityAttribute)



@given(instance=QualityMetamodel_QualityAttribute_strategy)
def test_qualitymetamodel_qualityattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_ValueType_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_valuetype_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_ValueType)



@given(instance=QualityMetamodel_ValueType_strategy)
def test_qualitymetamodel_valuetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_MetricProvider_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_metricprovider_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_MetricProvider)



@given(instance=QualityMetamodel_MetricProvider_strategy)
def test_qualitymetamodel_metricprovider_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=QualityMetamodel_MetricProvider_strategy)
def test_qualitymetamodel_metricprovider_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=QualityMetamodel_MetricProvider_strategy)
def test_qualitymetamodel_metricprovider_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_QualityModel_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_qualitymodel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QualityModel)



@given(instance=QualityMetamodel_QualityModel_strategy)
def test_qualitymetamodel_qualitymodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QualityMetamodel_Operation_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_operation_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_Operation)



@given(instance=QualityMetamodel_Operation_strategy)
def test_qualitymetamodel_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=QualityMetamodel_Operation_strategy)
def test_qualitymetamodel_operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=QualityMetamodel_AggregatedValue_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_aggregatedvalue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_AggregatedValue)

@given(instance=QualityMetamodel_SingleValue_strategy)
@settings(max_examples=50)
def test_qualitymetamodel_singlevalue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_SingleValue)

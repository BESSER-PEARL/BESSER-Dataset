import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Measure,
    Measure::PercentageMeasure,
    Measure::DoubleMeasure,
    Measure::IntegerMeasure,
    Measure::Measure,
    Measure::Metric,
    Measure::MeasureSet,
    Measure::Category,
    Measure::RootMeasureSet,
    ElementKind,
    ModelKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_measure_is_not_abstract():
    assert not inspect.isabstract(Measure)


def test_measure_constructor_exists():
    assert callable(Measure.__init__)


def test_measure_constructor_args():
    sig = inspect.signature(Measure.__init__)
    params = list(sig.parameters.keys())



def test_measure::percentagemeasure_is_not_abstract():
    assert not inspect.isabstract(Measure::PercentageMeasure)


def test_measure::percentagemeasure_constructor_exists():
    assert callable(Measure::PercentageMeasure.__init__)


def test_measure::percentagemeasure_constructor_args():
    sig = inspect.signature(Measure::PercentageMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_measure::percentagemeasure_has_value():
    assert hasattr(Measure::PercentageMeasure, "value")
    descriptor = None
    for klass in Measure::PercentageMeasure.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_measure::doublemeasure_is_not_abstract():
    assert not inspect.isabstract(Measure::DoubleMeasure)


def test_measure::doublemeasure_constructor_exists():
    assert callable(Measure::DoubleMeasure.__init__)


def test_measure::doublemeasure_constructor_args():
    sig = inspect.signature(Measure::DoubleMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_measure::doublemeasure_has_value():
    assert hasattr(Measure::DoubleMeasure, "value")
    descriptor = None
    for klass in Measure::DoubleMeasure.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_measure::integermeasure_is_not_abstract():
    assert not inspect.isabstract(Measure::IntegerMeasure)


def test_measure::integermeasure_constructor_exists():
    assert callable(Measure::IntegerMeasure.__init__)


def test_measure::integermeasure_constructor_args():
    sig = inspect.signature(Measure::IntegerMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_measure::integermeasure_has_value():
    assert hasattr(Measure::IntegerMeasure, "value")
    descriptor = None
    for klass in Measure::IntegerMeasure.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_measure::measure_is_not_abstract():
    assert not inspect.isabstract(Measure::Measure)


def test_measure::measure_constructor_exists():
    assert callable(Measure::Measure.__init__)


def test_measure::measure_constructor_args():
    sig = inspect.signature(Measure::Measure.__init__)
    params = list(sig.parameters.keys())



def test_measure::metric_is_not_abstract():
    assert not inspect.isabstract(Measure::Metric)


def test_measure::metric_constructor_exists():
    assert callable(Measure::Metric.__init__)


def test_measure::metric_constructor_args():
    sig = inspect.signature(Measure::Metric.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"
    assert "name" in params, "Missing parameter 'name'"
    assert "preferredValue" in params, "Missing parameter 'preferredValue'"

def test_measure::metric_has_desc():
    assert hasattr(Measure::Metric, "desc")
    descriptor = None
    for klass in Measure::Metric.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_measure::metric_has_name():
    assert hasattr(Measure::Metric, "name")
    descriptor = None
    for klass in Measure::Metric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_measure::metric_has_preferredValue():
    assert hasattr(Measure::Metric, "preferredValue")
    descriptor = None
    for klass in Measure::Metric.__mro__:
        if "preferredValue" in klass.__dict__:
            descriptor = klass.__dict__["preferredValue"]
            break
    assert isinstance(descriptor, property)



def test_measure::measureset_is_not_abstract():
    assert not inspect.isabstract(Measure::MeasureSet)


def test_measure::measureset_constructor_exists():
    assert callable(Measure::MeasureSet.__init__)


def test_measure::measureset_constructor_args():
    sig = inspect.signature(Measure::MeasureSet.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"
    assert "elementType" in params, "Missing parameter 'elementType'"

def test_measure::measureset_has_elementName():
    assert hasattr(Measure::MeasureSet, "elementName")
    descriptor = None
    for klass in Measure::MeasureSet.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)

def test_measure::measureset_has_elementType():
    assert hasattr(Measure::MeasureSet, "elementType")
    descriptor = None
    for klass in Measure::MeasureSet.__mro__:
        if "elementType" in klass.__dict__:
            descriptor = klass.__dict__["elementType"]
            break
    assert isinstance(descriptor, property)



def test_measure::category_is_not_abstract():
    assert not inspect.isabstract(Measure::Category)


def test_measure::category_constructor_exists():
    assert callable(Measure::Category.__init__)


def test_measure::category_constructor_args():
    sig = inspect.signature(Measure::Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_measure::category_has_name():
    assert hasattr(Measure::Category, "name")
    descriptor = None
    for klass in Measure::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_measure::category_has_desc():
    assert hasattr(Measure::Category, "desc")
    descriptor = None
    for klass in Measure::Category.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_measure::rootmeasureset_is_not_abstract():
    assert not inspect.isabstract(Measure::RootMeasureSet)


def test_measure::rootmeasureset_constructor_exists():
    assert callable(Measure::RootMeasureSet.__init__)


def test_measure::rootmeasureset_constructor_args():
    sig = inspect.signature(Measure::RootMeasureSet.__init__)
    params = list(sig.parameters.keys())
    assert "modelType" in params, "Missing parameter 'modelType'"

def test_measure::rootmeasureset_has_modelType():
    assert hasattr(Measure::RootMeasureSet, "modelType")
    descriptor = None
    for klass in Measure::RootMeasureSet.__mro__:
        if "modelType" in klass.__dict__:
            descriptor = klass.__dict__["modelType"]
            break
    assert isinstance(descriptor, property)

def test_elementkind_exists():
    # Check that the Enumeration exists
    assert ElementKind is not None

def test_elementkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ElementKind]
    expected_literals = [
        "model",
        "interface",
        "metamodel",
        "class_",
        "package",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ElementKind"

def test_modelkind_exists():
    # Check that the Enumeration exists
    assert ModelKind is not None

def test_modelkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModelKind]
    expected_literals = [
        "KM3",
        "UML2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModelKind"


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
Measure_strategy = st.builds(
    Measure,
)
Measure::PercentageMeasure_strategy = st.builds(
    Measure::PercentageMeasure,
    value=
        safe_text
)
Measure::DoubleMeasure_strategy = st.builds(
    Measure::DoubleMeasure,
    value=
        safe_text
)
Measure::IntegerMeasure_strategy = st.builds(
    Measure::IntegerMeasure,
    value=
        safe_text
)
Measure::Measure_strategy = st.builds(
    Measure::Measure,
)
Measure::Metric_strategy = st.builds(
    Measure::Metric,
    desc=
        safe_text,
    name=
        safe_text,
    preferredValue=
        safe_text
)
Measure::MeasureSet_strategy = st.builds(
    Measure::MeasureSet,
    elementName=
        safe_text,
    elementType=
        safe_text
)
Measure::Category_strategy = st.builds(
    Measure::Category,
    name=
        safe_text,
    desc=
        safe_text
)
Measure::RootMeasureSet_strategy = st.builds(
    Measure::RootMeasureSet,
    modelType=
        safe_text
)

@given(instance=Measure_strategy)
@settings(max_examples=50)
def test_measure_instantiation(instance):
    assert isinstance(instance, Measure)

@given(instance=Measure::PercentageMeasure_strategy)
@settings(max_examples=50)
def test_measure::percentagemeasure_instantiation(instance):
    assert isinstance(instance, Measure::PercentageMeasure)

@given(instance=Measure::PercentageMeasure_strategy)
def test_measure::percentagemeasure_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Measure::PercentageMeasure_strategy)
def test_measure::percentagemeasure_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Measure::DoubleMeasure_strategy)
@settings(max_examples=50)
def test_measure::doublemeasure_instantiation(instance):
    assert isinstance(instance, Measure::DoubleMeasure)

@given(instance=Measure::DoubleMeasure_strategy)
def test_measure::doublemeasure_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Measure::DoubleMeasure_strategy)
def test_measure::doublemeasure_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Measure::IntegerMeasure_strategy)
@settings(max_examples=50)
def test_measure::integermeasure_instantiation(instance):
    assert isinstance(instance, Measure::IntegerMeasure)

@given(instance=Measure::IntegerMeasure_strategy)
def test_measure::integermeasure_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Measure::IntegerMeasure_strategy)
def test_measure::integermeasure_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Measure::Measure_strategy)
@settings(max_examples=50)
def test_measure::measure_instantiation(instance):
    assert isinstance(instance, Measure::Measure)

@given(instance=Measure::Metric_strategy)
@settings(max_examples=50)
def test_measure::metric_instantiation(instance):
    assert isinstance(instance, Measure::Metric)

@given(instance=Measure::Metric_strategy)
def test_measure::metric_desc_type(instance):
    assert isinstance(instance.desc, str)


@given(instance=Measure::Metric_strategy)
def test_measure::metric_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=Measure::Metric_strategy)
def test_measure::metric_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Measure::Metric_strategy)
def test_measure::metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Measure::Metric_strategy)
def test_measure::metric_preferredValue_type(instance):
    assert isinstance(instance.preferredValue, str)


@given(instance=Measure::Metric_strategy)
def test_measure::metric_preferredValue_setter(instance):
    original = instance.preferredValue
    instance.preferredValue = original
    assert instance.preferredValue == original

@given(instance=Measure::MeasureSet_strategy)
@settings(max_examples=50)
def test_measure::measureset_instantiation(instance):
    assert isinstance(instance, Measure::MeasureSet)

@given(instance=Measure::MeasureSet_strategy)
def test_measure::measureset_elementName_type(instance):
    assert isinstance(instance.elementName, str)


@given(instance=Measure::MeasureSet_strategy)
def test_measure::measureset_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=Measure::MeasureSet_strategy)
def test_measure::measureset_elementType_type(instance):
    assert isinstance(instance.elementType, str)


@given(instance=Measure::MeasureSet_strategy)
def test_measure::measureset_elementType_setter(instance):
    original = instance.elementType
    instance.elementType = original
    assert instance.elementType == original

@given(instance=Measure::Category_strategy)
@settings(max_examples=50)
def test_measure::category_instantiation(instance):
    assert isinstance(instance, Measure::Category)

@given(instance=Measure::Category_strategy)
def test_measure::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Measure::Category_strategy)
def test_measure::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Measure::Category_strategy)
def test_measure::category_desc_type(instance):
    assert isinstance(instance.desc, str)


@given(instance=Measure::Category_strategy)
def test_measure::category_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=Measure::RootMeasureSet_strategy)
@settings(max_examples=50)
def test_measure::rootmeasureset_instantiation(instance):
    assert isinstance(instance, Measure::RootMeasureSet)

@given(instance=Measure::RootMeasureSet_strategy)
def test_measure::rootmeasureset_modelType_type(instance):
    assert isinstance(instance.modelType, str)


@given(instance=Measure::RootMeasureSet_strategy)
def test_measure::rootmeasureset_modelType_setter(instance):
    original = instance.modelType
    instance.modelType = original
    assert instance.modelType == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Measure,
    Measure_PercentageMeasure,
    Measure_DoubleMeasure,
    Measure_IntegerMeasure,
    Measure_Measure,
    Measure_Metric,
    Measure_MeasureSet,
    Measure_Category,
    Measure_RootMeasureSet,
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



def test_measure_percentagemeasure_is_not_abstract():
    assert not inspect.isabstract(Measure_PercentageMeasure)


def test_measure_percentagemeasure_constructor_exists():
    assert callable(Measure_PercentageMeasure.__init__)


def test_measure_percentagemeasure_constructor_args():
    sig = inspect.signature(Measure_PercentageMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_measure_percentagemeasure_has_value():
    assert hasattr(Measure_PercentageMeasure, "value")
    descriptor = None
    for klass in Measure_PercentageMeasure.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_measure_doublemeasure_is_not_abstract():
    assert not inspect.isabstract(Measure_DoubleMeasure)


def test_measure_doublemeasure_constructor_exists():
    assert callable(Measure_DoubleMeasure.__init__)


def test_measure_doublemeasure_constructor_args():
    sig = inspect.signature(Measure_DoubleMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_measure_doublemeasure_has_value():
    assert hasattr(Measure_DoubleMeasure, "value")
    descriptor = None
    for klass in Measure_DoubleMeasure.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_measure_integermeasure_is_not_abstract():
    assert not inspect.isabstract(Measure_IntegerMeasure)


def test_measure_integermeasure_constructor_exists():
    assert callable(Measure_IntegerMeasure.__init__)


def test_measure_integermeasure_constructor_args():
    sig = inspect.signature(Measure_IntegerMeasure.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_measure_integermeasure_has_value():
    assert hasattr(Measure_IntegerMeasure, "value")
    descriptor = None
    for klass in Measure_IntegerMeasure.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_measure_measure_is_not_abstract():
    assert not inspect.isabstract(Measure_Measure)


def test_measure_measure_constructor_exists():
    assert callable(Measure_Measure.__init__)


def test_measure_measure_constructor_args():
    sig = inspect.signature(Measure_Measure.__init__)
    params = list(sig.parameters.keys())



def test_measure_metric_is_not_abstract():
    assert not inspect.isabstract(Measure_Metric)


def test_measure_metric_constructor_exists():
    assert callable(Measure_Metric.__init__)


def test_measure_metric_constructor_args():
    sig = inspect.signature(Measure_Metric.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"
    assert "preferredValue" in params, "Missing parameter 'preferredValue'"
    assert "name" in params, "Missing parameter 'name'"

def test_measure_metric_has_desc():
    assert hasattr(Measure_Metric, "desc")
    descriptor = None
    for klass in Measure_Metric.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_measure_metric_has_preferredValue():
    assert hasattr(Measure_Metric, "preferredValue")
    descriptor = None
    for klass in Measure_Metric.__mro__:
        if "preferredValue" in klass.__dict__:
            descriptor = klass.__dict__["preferredValue"]
            break
    assert isinstance(descriptor, property)

def test_measure_metric_has_name():
    assert hasattr(Measure_Metric, "name")
    descriptor = None
    for klass in Measure_Metric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_measure_measureset_is_not_abstract():
    assert not inspect.isabstract(Measure_MeasureSet)


def test_measure_measureset_constructor_exists():
    assert callable(Measure_MeasureSet.__init__)


def test_measure_measureset_constructor_args():
    sig = inspect.signature(Measure_MeasureSet.__init__)
    params = list(sig.parameters.keys())
    assert "elementType" in params, "Missing parameter 'elementType'"
    assert "elementName" in params, "Missing parameter 'elementName'"

def test_measure_measureset_has_elementType():
    assert hasattr(Measure_MeasureSet, "elementType")
    descriptor = None
    for klass in Measure_MeasureSet.__mro__:
        if "elementType" in klass.__dict__:
            descriptor = klass.__dict__["elementType"]
            break
    assert isinstance(descriptor, property)

def test_measure_measureset_has_elementName():
    assert hasattr(Measure_MeasureSet, "elementName")
    descriptor = None
    for klass in Measure_MeasureSet.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)



def test_measure_category_is_not_abstract():
    assert not inspect.isabstract(Measure_Category)


def test_measure_category_constructor_exists():
    assert callable(Measure_Category.__init__)


def test_measure_category_constructor_args():
    sig = inspect.signature(Measure_Category.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"
    assert "name" in params, "Missing parameter 'name'"

def test_measure_category_has_desc():
    assert hasattr(Measure_Category, "desc")
    descriptor = None
    for klass in Measure_Category.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_measure_category_has_name():
    assert hasattr(Measure_Category, "name")
    descriptor = None
    for klass in Measure_Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_measure_rootmeasureset_is_not_abstract():
    assert not inspect.isabstract(Measure_RootMeasureSet)


def test_measure_rootmeasureset_constructor_exists():
    assert callable(Measure_RootMeasureSet.__init__)


def test_measure_rootmeasureset_constructor_args():
    sig = inspect.signature(Measure_RootMeasureSet.__init__)
    params = list(sig.parameters.keys())
    assert "modelType" in params, "Missing parameter 'modelType'"

def test_measure_rootmeasureset_has_modelType():
    assert hasattr(Measure_RootMeasureSet, "modelType")
    descriptor = None
    for klass in Measure_RootMeasureSet.__mro__:
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
        "metamodel",
        "package",
        "class_",
        "interface",
        "model",
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
Measure_PercentageMeasure_strategy = st.builds(
    Measure_PercentageMeasure,
    value=
        safe_text
)
Measure_DoubleMeasure_strategy = st.builds(
    Measure_DoubleMeasure,
    value=
        safe_text
)
Measure_IntegerMeasure_strategy = st.builds(
    Measure_IntegerMeasure,
    value=
        safe_text
)
Measure_Measure_strategy = st.builds(
    Measure_Measure,
)
Measure_Metric_strategy = st.builds(
    Measure_Metric,
    desc=
        safe_text,
    preferredValue=
        safe_text,
    name=
        safe_text
)
Measure_MeasureSet_strategy = st.builds(
    Measure_MeasureSet,
    elementType=
        safe_text,
    elementName=
        safe_text
)
Measure_Category_strategy = st.builds(
    Measure_Category,
    desc=
        safe_text,
    name=
        safe_text
)
Measure_RootMeasureSet_strategy = st.builds(
    Measure_RootMeasureSet,
    modelType=
        safe_text
)

@given(instance=Measure_strategy)
@settings(max_examples=50)
def test_measure_instantiation(instance):
    assert isinstance(instance, Measure)

@given(instance=Measure_PercentageMeasure_strategy)
@settings(max_examples=50)
def test_measure_percentagemeasure_instantiation(instance):
    assert isinstance(instance, Measure_PercentageMeasure)



@given(instance=Measure_PercentageMeasure_strategy)
def test_measure_percentagemeasure_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Measure_DoubleMeasure_strategy)
@settings(max_examples=50)
def test_measure_doublemeasure_instantiation(instance):
    assert isinstance(instance, Measure_DoubleMeasure)



@given(instance=Measure_DoubleMeasure_strategy)
def test_measure_doublemeasure_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Measure_IntegerMeasure_strategy)
@settings(max_examples=50)
def test_measure_integermeasure_instantiation(instance):
    assert isinstance(instance, Measure_IntegerMeasure)



@given(instance=Measure_IntegerMeasure_strategy)
def test_measure_integermeasure_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Measure_Measure_strategy)
@settings(max_examples=50)
def test_measure_measure_instantiation(instance):
    assert isinstance(instance, Measure_Measure)

@given(instance=Measure_Metric_strategy)
@settings(max_examples=50)
def test_measure_metric_instantiation(instance):
    assert isinstance(instance, Measure_Metric)



@given(instance=Measure_Metric_strategy)
def test_measure_metric_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original



@given(instance=Measure_Metric_strategy)
def test_measure_metric_preferredValue_setter(instance):
    original = instance.preferredValue
    instance.preferredValue = original
    assert instance.preferredValue == original



@given(instance=Measure_Metric_strategy)
def test_measure_metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Measure_MeasureSet_strategy)
@settings(max_examples=50)
def test_measure_measureset_instantiation(instance):
    assert isinstance(instance, Measure_MeasureSet)



@given(instance=Measure_MeasureSet_strategy)
def test_measure_measureset_elementType_setter(instance):
    original = instance.elementType
    instance.elementType = original
    assert instance.elementType == original



@given(instance=Measure_MeasureSet_strategy)
def test_measure_measureset_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=Measure_Category_strategy)
@settings(max_examples=50)
def test_measure_category_instantiation(instance):
    assert isinstance(instance, Measure_Category)



@given(instance=Measure_Category_strategy)
def test_measure_category_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original



@given(instance=Measure_Category_strategy)
def test_measure_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Measure_RootMeasureSet_strategy)
@settings(max_examples=50)
def test_measure_rootmeasureset_instantiation(instance):
    assert isinstance(instance, Measure_RootMeasureSet)



@given(instance=Measure_RootMeasureSet_strategy)
def test_measure_rootmeasureset_modelType_setter(instance):
    original = instance.modelType
    instance.modelType = original
    assert instance.modelType == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UmlMM_Parameter,
    UmlMM_Property,
    UmlMM_Operation,
    UmlMM_Classifier,
    UmlMM_UmlPackage,
    Classifier,
    UmlMM_Class,
    UmlMM_DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlmm_parameter_is_not_abstract():
    assert not inspect.isabstract(UmlMM_Parameter)


def test_umlmm_parameter_constructor_exists():
    assert callable(UmlMM_Parameter.__init__)


def test_umlmm_parameter_constructor_args():
    sig = inspect.signature(UmlMM_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm_parameter_has_name():
    assert hasattr(UmlMM_Parameter, "name")
    descriptor = None
    for klass in UmlMM_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm_property_is_not_abstract():
    assert not inspect.isabstract(UmlMM_Property)


def test_umlmm_property_constructor_exists():
    assert callable(UmlMM_Property.__init__)


def test_umlmm_property_constructor_args():
    sig = inspect.signature(UmlMM_Property.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm_property_has_lower():
    assert hasattr(UmlMM_Property, "lower")
    descriptor = None
    for klass in UmlMM_Property.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_umlmm_property_has_upper():
    assert hasattr(UmlMM_Property, "upper")
    descriptor = None
    for klass in UmlMM_Property.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_umlmm_property_has_name():
    assert hasattr(UmlMM_Property, "name")
    descriptor = None
    for klass in UmlMM_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm_operation_is_not_abstract():
    assert not inspect.isabstract(UmlMM_Operation)


def test_umlmm_operation_constructor_exists():
    assert callable(UmlMM_Operation.__init__)


def test_umlmm_operation_constructor_args():
    sig = inspect.signature(UmlMM_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm_operation_has_name():
    assert hasattr(UmlMM_Operation, "name")
    descriptor = None
    for klass in UmlMM_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm_classifier_is_not_abstract():
    assert not inspect.isabstract(UmlMM_Classifier)


def test_umlmm_classifier_constructor_exists():
    assert callable(UmlMM_Classifier.__init__)


def test_umlmm_classifier_constructor_args():
    sig = inspect.signature(UmlMM_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmm_umlpackage_is_not_abstract():
    assert not inspect.isabstract(UmlMM_UmlPackage)


def test_umlmm_umlpackage_constructor_exists():
    assert callable(UmlMM_UmlPackage.__init__)


def test_umlmm_umlpackage_constructor_args():
    sig = inspect.signature(UmlMM_UmlPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm_umlpackage_has_name():
    assert hasattr(UmlMM_UmlPackage, "name")
    descriptor = None
    for klass in UmlMM_UmlPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmm_class_is_not_abstract():
    assert not inspect.isabstract(UmlMM_Class)


def test_umlmm_class_constructor_exists():
    assert callable(UmlMM_Class.__init__)


def test_umlmm_class_constructor_args():
    sig = inspect.signature(UmlMM_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm_class_has_name():
    assert hasattr(UmlMM_Class, "name")
    descriptor = None
    for klass in UmlMM_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm_datatype_is_not_abstract():
    assert not inspect.isabstract(UmlMM_DataType)


def test_umlmm_datatype_constructor_exists():
    assert callable(UmlMM_DataType.__init__)


def test_umlmm_datatype_constructor_args():
    sig = inspect.signature(UmlMM_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm_datatype_has_name():
    assert hasattr(UmlMM_DataType, "name")
    descriptor = None
    for klass in UmlMM_DataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
UmlMM_Parameter_strategy = st.builds(
    UmlMM_Parameter,
    name=
        safe_text
)
UmlMM_Property_strategy = st.builds(
    UmlMM_Property,
    lower=
        st.integers(),
    upper=
        st.integers(),
    name=
        safe_text
)
UmlMM_Operation_strategy = st.builds(
    UmlMM_Operation,
    name=
        safe_text
)
UmlMM_Classifier_strategy = st.builds(
    UmlMM_Classifier,
)
UmlMM_UmlPackage_strategy = st.builds(
    UmlMM_UmlPackage,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
UmlMM_Class_strategy = st.builds(
    UmlMM_Class,
    name=
        safe_text
)
UmlMM_DataType_strategy = st.builds(
    UmlMM_DataType,
    name=
        safe_text
)

@given(instance=UmlMM_Parameter_strategy)
@settings(max_examples=50)
def test_umlmm_parameter_instantiation(instance):
    assert isinstance(instance, UmlMM_Parameter)



@given(instance=UmlMM_Parameter_strategy)
def test_umlmm_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UmlMM_Property_strategy)
@settings(max_examples=50)
def test_umlmm_property_instantiation(instance):
    assert isinstance(instance, UmlMM_Property)



@given(instance=UmlMM_Property_strategy)
def test_umlmm_property_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=UmlMM_Property_strategy)
def test_umlmm_property_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=UmlMM_Property_strategy)
def test_umlmm_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UmlMM_Operation_strategy)
@settings(max_examples=50)
def test_umlmm_operation_instantiation(instance):
    assert isinstance(instance, UmlMM_Operation)



@given(instance=UmlMM_Operation_strategy)
def test_umlmm_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UmlMM_Classifier_strategy)
@settings(max_examples=50)
def test_umlmm_classifier_instantiation(instance):
    assert isinstance(instance, UmlMM_Classifier)

@given(instance=UmlMM_UmlPackage_strategy)
@settings(max_examples=50)
def test_umlmm_umlpackage_instantiation(instance):
    assert isinstance(instance, UmlMM_UmlPackage)



@given(instance=UmlMM_UmlPackage_strategy)
def test_umlmm_umlpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UmlMM_Class_strategy)
@settings(max_examples=50)
def test_umlmm_class_instantiation(instance):
    assert isinstance(instance, UmlMM_Class)



@given(instance=UmlMM_Class_strategy)
def test_umlmm_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UmlMM_DataType_strategy)
@settings(max_examples=50)
def test_umlmm_datatype_instantiation(instance):
    assert isinstance(instance, UmlMM_DataType)



@given(instance=UmlMM_DataType_strategy)
def test_umlmm_datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

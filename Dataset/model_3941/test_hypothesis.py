import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UmlMM::Parameter,
    UmlMM::Property,
    UmlMM::Operation,
    UmlMM::Classifier,
    UmlMM::UmlPackage,
    Classifier,
    UmlMM::Class,
    UmlMM::DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlmm::parameter_is_not_abstract():
    assert not inspect.isabstract(UmlMM::Parameter)


def test_umlmm::parameter_constructor_exists():
    assert callable(UmlMM::Parameter.__init__)


def test_umlmm::parameter_constructor_args():
    sig = inspect.signature(UmlMM::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::parameter_has_name():
    assert hasattr(UmlMM::Parameter, "name")
    descriptor = None
    for klass in UmlMM::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::property_is_not_abstract():
    assert not inspect.isabstract(UmlMM::Property)


def test_umlmm::property_constructor_exists():
    assert callable(UmlMM::Property.__init__)


def test_umlmm::property_constructor_args():
    sig = inspect.signature(UmlMM::Property.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "name" in params, "Missing parameter 'name'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_umlmm::property_has_lower():
    assert hasattr(UmlMM::Property, "lower")
    descriptor = None
    for klass in UmlMM::Property.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_umlmm::property_has_name():
    assert hasattr(UmlMM::Property, "name")
    descriptor = None
    for klass in UmlMM::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umlmm::property_has_upper():
    assert hasattr(UmlMM::Property, "upper")
    descriptor = None
    for klass in UmlMM::Property.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::operation_is_not_abstract():
    assert not inspect.isabstract(UmlMM::Operation)


def test_umlmm::operation_constructor_exists():
    assert callable(UmlMM::Operation.__init__)


def test_umlmm::operation_constructor_args():
    sig = inspect.signature(UmlMM::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::operation_has_name():
    assert hasattr(UmlMM::Operation, "name")
    descriptor = None
    for klass in UmlMM::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::classifier_is_not_abstract():
    assert not inspect.isabstract(UmlMM::Classifier)


def test_umlmm::classifier_constructor_exists():
    assert callable(UmlMM::Classifier.__init__)


def test_umlmm::classifier_constructor_args():
    sig = inspect.signature(UmlMM::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::umlpackage_is_not_abstract():
    assert not inspect.isabstract(UmlMM::UmlPackage)


def test_umlmm::umlpackage_constructor_exists():
    assert callable(UmlMM::UmlPackage.__init__)


def test_umlmm::umlpackage_constructor_args():
    sig = inspect.signature(UmlMM::UmlPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::umlpackage_has_name():
    assert hasattr(UmlMM::UmlPackage, "name")
    descriptor = None
    for klass in UmlMM::UmlPackage.__mro__:
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



def test_umlmm::class_is_not_abstract():
    assert not inspect.isabstract(UmlMM::Class)


def test_umlmm::class_constructor_exists():
    assert callable(UmlMM::Class.__init__)


def test_umlmm::class_constructor_args():
    sig = inspect.signature(UmlMM::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::class_has_name():
    assert hasattr(UmlMM::Class, "name")
    descriptor = None
    for klass in UmlMM::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::datatype_is_not_abstract():
    assert not inspect.isabstract(UmlMM::DataType)


def test_umlmm::datatype_constructor_exists():
    assert callable(UmlMM::DataType.__init__)


def test_umlmm::datatype_constructor_args():
    sig = inspect.signature(UmlMM::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::datatype_has_name():
    assert hasattr(UmlMM::DataType, "name")
    descriptor = None
    for klass in UmlMM::DataType.__mro__:
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
UmlMM::Parameter_strategy = st.builds(
    UmlMM::Parameter,
    name=
        safe_text
)
UmlMM::Property_strategy = st.builds(
    UmlMM::Property,
    lower=
        st.integers(),
    name=
        safe_text,
    upper=
        st.integers()
)
UmlMM::Operation_strategy = st.builds(
    UmlMM::Operation,
    name=
        safe_text
)
UmlMM::Classifier_strategy = st.builds(
    UmlMM::Classifier,
)
UmlMM::UmlPackage_strategy = st.builds(
    UmlMM::UmlPackage,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
UmlMM::Class_strategy = st.builds(
    UmlMM::Class,
    name=
        safe_text
)
UmlMM::DataType_strategy = st.builds(
    UmlMM::DataType,
    name=
        safe_text
)

@given(instance=UmlMM::Parameter_strategy)
@settings(max_examples=50)
def test_umlmm::parameter_instantiation(instance):
    assert isinstance(instance, UmlMM::Parameter)

@given(instance=UmlMM::Parameter_strategy)
def test_umlmm::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UmlMM::Parameter_strategy)
def test_umlmm::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UmlMM::Property_strategy)
@settings(max_examples=50)
def test_umlmm::property_instantiation(instance):
    assert isinstance(instance, UmlMM::Property)

@given(instance=UmlMM::Property_strategy)
def test_umlmm::property_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=UmlMM::Property_strategy)
def test_umlmm::property_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=UmlMM::Property_strategy)
def test_umlmm::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UmlMM::Property_strategy)
def test_umlmm::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UmlMM::Property_strategy)
def test_umlmm::property_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=UmlMM::Property_strategy)
def test_umlmm::property_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=UmlMM::Operation_strategy)
@settings(max_examples=50)
def test_umlmm::operation_instantiation(instance):
    assert isinstance(instance, UmlMM::Operation)

@given(instance=UmlMM::Operation_strategy)
def test_umlmm::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UmlMM::Operation_strategy)
def test_umlmm::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UmlMM::Classifier_strategy)
@settings(max_examples=50)
def test_umlmm::classifier_instantiation(instance):
    assert isinstance(instance, UmlMM::Classifier)

@given(instance=UmlMM::UmlPackage_strategy)
@settings(max_examples=50)
def test_umlmm::umlpackage_instantiation(instance):
    assert isinstance(instance, UmlMM::UmlPackage)

@given(instance=UmlMM::UmlPackage_strategy)
def test_umlmm::umlpackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UmlMM::UmlPackage_strategy)
def test_umlmm::umlpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UmlMM::Class_strategy)
@settings(max_examples=50)
def test_umlmm::class_instantiation(instance):
    assert isinstance(instance, UmlMM::Class)

@given(instance=UmlMM::Class_strategy)
def test_umlmm::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UmlMM::Class_strategy)
def test_umlmm::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UmlMM::DataType_strategy)
@settings(max_examples=50)
def test_umlmm::datatype_instantiation(instance):
    assert isinstance(instance, UmlMM::DataType)

@given(instance=UmlMM::DataType_strategy)
def test_umlmm::datatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UmlMM::DataType_strategy)
def test_umlmm::datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

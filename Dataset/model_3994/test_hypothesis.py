import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    classes::Attribute,
    Type,
    classes::DataType,
    classes::Type,
    classes::Class,
    classes::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classes::attribute_is_not_abstract():
    assert not inspect.isabstract(classes::Attribute)


def test_classes::attribute_constructor_exists():
    assert callable(classes::Attribute.__init__)


def test_classes::attribute_constructor_args():
    sig = inspect.signature(classes::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_classes::attribute_has_name():
    assert hasattr(classes::Attribute, "name")
    descriptor = None
    for klass in classes::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classes::attribute_has_value():
    assert hasattr(classes::Attribute, "value")
    descriptor = None
    for klass in classes::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_classes::datatype_is_not_abstract():
    assert not inspect.isabstract(classes::DataType)


def test_classes::datatype_constructor_exists():
    assert callable(classes::DataType.__init__)


def test_classes::datatype_constructor_args():
    sig = inspect.signature(classes::DataType.__init__)
    params = list(sig.parameters.keys())



def test_classes::type_is_not_abstract():
    assert not inspect.isabstract(classes::Type)


def test_classes::type_constructor_exists():
    assert callable(classes::Type.__init__)


def test_classes::type_constructor_args():
    sig = inspect.signature(classes::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes::type_has_name():
    assert hasattr(classes::Type, "name")
    descriptor = None
    for klass in classes::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes::class_is_not_abstract():
    assert not inspect.isabstract(classes::Class)


def test_classes::class_constructor_exists():
    assert callable(classes::Class.__init__)


def test_classes::class_constructor_args():
    sig = inspect.signature(classes::Class.__init__)
    params = list(sig.parameters.keys())



def test_classes::model_is_not_abstract():
    assert not inspect.isabstract(classes::Model)


def test_classes::model_constructor_exists():
    assert callable(classes::Model.__init__)


def test_classes::model_constructor_args():
    sig = inspect.signature(classes::Model.__init__)
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
classes::Attribute_strategy = st.builds(
    classes::Attribute,
    name=
        safe_text,
    value=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
classes::DataType_strategy = st.builds(
    classes::DataType,
)
classes::Type_strategy = st.builds(
    classes::Type,
    name=
        safe_text
)
classes::Class_strategy = st.builds(
    classes::Class,
)
classes::Model_strategy = st.builds(
    classes::Model,
)

@given(instance=classes::Attribute_strategy)
@settings(max_examples=50)
def test_classes::attribute_instantiation(instance):
    assert isinstance(instance, classes::Attribute)

@given(instance=classes::Attribute_strategy)
def test_classes::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::Attribute_strategy)
def test_classes::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes::Attribute_strategy)
def test_classes::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=classes::Attribute_strategy)
def test_classes::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=classes::DataType_strategy)
@settings(max_examples=50)
def test_classes::datatype_instantiation(instance):
    assert isinstance(instance, classes::DataType)

@given(instance=classes::Type_strategy)
@settings(max_examples=50)
def test_classes::type_instantiation(instance):
    assert isinstance(instance, classes::Type)

@given(instance=classes::Type_strategy)
def test_classes::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::Type_strategy)
def test_classes::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes::Class_strategy)
@settings(max_examples=50)
def test_classes::class_instantiation(instance):
    assert isinstance(instance, classes::Class)

@given(instance=classes::Model_strategy)
@settings(max_examples=50)
def test_classes::model_instantiation(instance):
    assert isinstance(instance, classes::Model)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data::Type,
    Data::Attribute,
    Data::Class,
    Data::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data::type_is_not_abstract():
    assert not inspect.isabstract(Data::Type)


def test_data::type_constructor_exists():
    assert callable(Data::Type.__init__)


def test_data::type_constructor_args():
    sig = inspect.signature(Data::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isReference" in params, "Missing parameter 'isReference'"

def test_data::type_has_name():
    assert hasattr(Data::Type, "name")
    descriptor = None
    for klass in Data::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_data::type_has_isReference():
    assert hasattr(Data::Type, "isReference")
    descriptor = None
    for klass in Data::Type.__mro__:
        if "isReference" in klass.__dict__:
            descriptor = klass.__dict__["isReference"]
            break
    assert isinstance(descriptor, property)



def test_data::attribute_is_not_abstract():
    assert not inspect.isabstract(Data::Attribute)


def test_data::attribute_constructor_exists():
    assert callable(Data::Attribute.__init__)


def test_data::attribute_constructor_args():
    sig = inspect.signature(Data::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_data::attribute_has_visibility():
    assert hasattr(Data::Attribute, "visibility")
    descriptor = None
    for klass in Data::Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_data::attribute_has_name():
    assert hasattr(Data::Attribute, "name")
    descriptor = None
    for klass in Data::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data::class_is_not_abstract():
    assert not inspect.isabstract(Data::Class)


def test_data::class_constructor_exists():
    assert callable(Data::Class.__init__)


def test_data::class_constructor_args():
    sig = inspect.signature(Data::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_data::class_has_name():
    assert hasattr(Data::Class, "name")
    descriptor = None
    for klass in Data::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data::model_is_not_abstract():
    assert not inspect.isabstract(Data::Model)


def test_data::model_constructor_exists():
    assert callable(Data::Model.__init__)


def test_data::model_constructor_args():
    sig = inspect.signature(Data::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_data::model_has_name():
    assert hasattr(Data::Model, "name")
    descriptor = None
    for klass in Data::Model.__mro__:
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
Data::Type_strategy = st.builds(
    Data::Type,
    name=
        safe_text,
    isReference=
        st.booleans()
)
Data::Attribute_strategy = st.builds(
    Data::Attribute,
    visibility=
        safe_text,
    name=
        safe_text
)
Data::Class_strategy = st.builds(
    Data::Class,
    name=
        safe_text
)
Data::Model_strategy = st.builds(
    Data::Model,
    name=
        safe_text
)

@given(instance=Data::Type_strategy)
@settings(max_examples=50)
def test_data::type_instantiation(instance):
    assert isinstance(instance, Data::Type)

@given(instance=Data::Type_strategy)
def test_data::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Type_strategy)
def test_data::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Type_strategy)
def test_data::type_isReference_type(instance):
    assert isinstance(instance.isReference, bool)


@given(instance=Data::Type_strategy)
def test_data::type_isReference_setter(instance):
    original = instance.isReference
    instance.isReference = original
    assert instance.isReference == original

@given(instance=Data::Attribute_strategy)
@settings(max_examples=50)
def test_data::attribute_instantiation(instance):
    assert isinstance(instance, Data::Attribute)

@given(instance=Data::Attribute_strategy)
def test_data::attribute_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=Data::Attribute_strategy)
def test_data::attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Data::Attribute_strategy)
def test_data::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Attribute_strategy)
def test_data::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Class_strategy)
@settings(max_examples=50)
def test_data::class_instantiation(instance):
    assert isinstance(instance, Data::Class)

@given(instance=Data::Class_strategy)
def test_data::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Class_strategy)
def test_data::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Model_strategy)
@settings(max_examples=50)
def test_data::model_instantiation(instance):
    assert isinstance(instance, Data::Model)

@given(instance=Data::Model_strategy)
def test_data::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Model_strategy)
def test_data::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

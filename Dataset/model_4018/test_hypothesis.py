import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data::Attribute,
    Data::Class,
    Data::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data::attribute_is_not_abstract():
    assert not inspect.isabstract(Data::Attribute)


def test_data::attribute_constructor_exists():
    assert callable(Data::Attribute.__init__)


def test_data::attribute_constructor_args():
    sig = inspect.signature(Data::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_data::attribute_has_Type():
    assert hasattr(Data::Attribute, "Type")
    descriptor = None
    for klass in Data::Attribute.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_data::attribute_has_Name():
    assert hasattr(Data::Attribute, "Name")
    descriptor = None
    for klass in Data::Attribute.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_data::class_is_not_abstract():
    assert not inspect.isabstract(Data::Class)


def test_data::class_constructor_exists():
    assert callable(Data::Class.__init__)


def test_data::class_constructor_args():
    sig = inspect.signature(Data::Class.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_data::class_has_Name():
    assert hasattr(Data::Class, "Name")
    descriptor = None
    for klass in Data::Class.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_data::model_is_not_abstract():
    assert not inspect.isabstract(Data::Model)


def test_data::model_constructor_exists():
    assert callable(Data::Model.__init__)


def test_data::model_constructor_args():
    sig = inspect.signature(Data::Model.__init__)
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
Data::Attribute_strategy = st.builds(
    Data::Attribute,
    Type=
        safe_text,
    Name=
        safe_text
)
Data::Class_strategy = st.builds(
    Data::Class,
    Name=
        safe_text
)
Data::Model_strategy = st.builds(
    Data::Model,
)

@given(instance=Data::Attribute_strategy)
@settings(max_examples=50)
def test_data::attribute_instantiation(instance):
    assert isinstance(instance, Data::Attribute)

@given(instance=Data::Attribute_strategy)
def test_data::attribute_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=Data::Attribute_strategy)
def test_data::attribute_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=Data::Attribute_strategy)
def test_data::attribute_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Data::Attribute_strategy)
def test_data::attribute_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Data::Class_strategy)
@settings(max_examples=50)
def test_data::class_instantiation(instance):
    assert isinstance(instance, Data::Class)

@given(instance=Data::Class_strategy)
def test_data::class_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Data::Class_strategy)
def test_data::class_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Data::Model_strategy)
@settings(max_examples=50)
def test_data::model_instantiation(instance):
    assert isinstance(instance, Data::Model)

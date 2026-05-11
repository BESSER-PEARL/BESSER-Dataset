import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data::Field,
    Data::Class,
    Data::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data::field_is_not_abstract():
    assert not inspect.isabstract(Data::Field)


def test_data::field_constructor_exists():
    assert callable(Data::Field.__init__)


def test_data::field_constructor_args():
    sig = inspect.signature(Data::Field.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_data::field_has_type():
    assert hasattr(Data::Field, "type")
    descriptor = None
    for klass in Data::Field.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_data::field_has_name():
    assert hasattr(Data::Field, "name")
    descriptor = None
    for klass in Data::Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_data::field_has_modifier():
    assert hasattr(Data::Field, "modifier")
    descriptor = None
    for klass in Data::Field.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
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
Data::Field_strategy = st.builds(
    Data::Field,
    type=
        safe_text,
    name=
        safe_text,
    modifier=
        safe_text
)
Data::Class_strategy = st.builds(
    Data::Class,
    name=
        safe_text
)
Data::Model_strategy = st.builds(
    Data::Model,
)

@given(instance=Data::Field_strategy)
@settings(max_examples=50)
def test_data::field_instantiation(instance):
    assert isinstance(instance, Data::Field)

@given(instance=Data::Field_strategy)
def test_data::field_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Data::Field_strategy)
def test_data::field_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Data::Field_strategy)
def test_data::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Field_strategy)
def test_data::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Field_strategy)
def test_data::field_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=Data::Field_strategy)
def test_data::field_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

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

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Data_Field,
    Data_Class,
    Data_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_field_is_not_abstract():
    assert not inspect.isabstract(Data_Field)


def test_data_field_constructor_exists():
    assert callable(Data_Field.__init__)


def test_data_field_constructor_args():
    sig = inspect.signature(Data_Field.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_data_field_has_modifier():
    assert hasattr(Data_Field, "modifier")
    descriptor = None
    for klass in Data_Field.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_data_field_has_type():
    assert hasattr(Data_Field, "type")
    descriptor = None
    for klass in Data_Field.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_data_field_has_name():
    assert hasattr(Data_Field, "name")
    descriptor = None
    for klass in Data_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data_class_is_not_abstract():
    assert not inspect.isabstract(Data_Class)


def test_data_class_constructor_exists():
    assert callable(Data_Class.__init__)


def test_data_class_constructor_args():
    sig = inspect.signature(Data_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_data_class_has_name():
    assert hasattr(Data_Class, "name")
    descriptor = None
    for klass in Data_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data_model_is_not_abstract():
    assert not inspect.isabstract(Data_Model)


def test_data_model_constructor_exists():
    assert callable(Data_Model.__init__)


def test_data_model_constructor_args():
    sig = inspect.signature(Data_Model.__init__)
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
Data_Field_strategy = st.builds(
    Data_Field,
    modifier=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
Data_Class_strategy = st.builds(
    Data_Class,
    name=
        safe_text
)
Data_Model_strategy = st.builds(
    Data_Model,
)

@given(instance=Data_Field_strategy)
@settings(max_examples=50)
def test_data_field_instantiation(instance):
    assert isinstance(instance, Data_Field)



@given(instance=Data_Field_strategy)
def test_data_field_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original



@given(instance=Data_Field_strategy)
def test_data_field_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Data_Field_strategy)
def test_data_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data_Class_strategy)
@settings(max_examples=50)
def test_data_class_instantiation(instance):
    assert isinstance(instance, Data_Class)



@given(instance=Data_Class_strategy)
def test_data_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data_Model_strategy)
@settings(max_examples=50)
def test_data_model_instantiation(instance):
    assert isinstance(instance, Data_Model)

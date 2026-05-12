import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Data_Model,
    Data_Attribut,
    Data_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_model_is_not_abstract():
    assert not inspect.isabstract(Data_Model)


def test_data_model_constructor_exists():
    assert callable(Data_Model.__init__)


def test_data_model_constructor_args():
    sig = inspect.signature(Data_Model.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_data_model_has_Name():
    assert hasattr(Data_Model, "Name")
    descriptor = None
    for klass in Data_Model.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_data_attribut_is_not_abstract():
    assert not inspect.isabstract(Data_Attribut)


def test_data_attribut_constructor_exists():
    assert callable(Data_Attribut.__init__)


def test_data_attribut_constructor_args():
    sig = inspect.signature(Data_Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "Static" in params, "Missing parameter 'Static'"
    assert "Visibility" in params, "Missing parameter 'Visibility'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_data_attribut_has_Static():
    assert hasattr(Data_Attribut, "Static")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "Static" in klass.__dict__:
            descriptor = klass.__dict__["Static"]
            break
    assert isinstance(descriptor, property)

def test_data_attribut_has_Visibility():
    assert hasattr(Data_Attribut, "Visibility")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "Visibility" in klass.__dict__:
            descriptor = klass.__dict__["Visibility"]
            break
    assert isinstance(descriptor, property)

def test_data_attribut_has_Name():
    assert hasattr(Data_Attribut, "Name")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_data_attribut_has_Type():
    assert hasattr(Data_Attribut, "Type")
    descriptor = None
    for klass in Data_Attribut.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_data_class_is_not_abstract():
    assert not inspect.isabstract(Data_Class)


def test_data_class_constructor_exists():
    assert callable(Data_Class.__init__)


def test_data_class_constructor_args():
    sig = inspect.signature(Data_Class.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_data_class_has_Name():
    assert hasattr(Data_Class, "Name")
    descriptor = None
    for klass in Data_Class.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
Data_Model_strategy = st.builds(
    Data_Model,
    Name=
        safe_text
)
Data_Attribut_strategy = st.builds(
    Data_Attribut,
    Static=
        st.booleans(),
    Visibility=
        safe_text,
    Name=
        safe_text,
    Type=
        safe_text
)
Data_Class_strategy = st.builds(
    Data_Class,
    Name=
        safe_text
)

@given(instance=Data_Model_strategy)
@settings(max_examples=50)
def test_data_model_instantiation(instance):
    assert isinstance(instance, Data_Model)



@given(instance=Data_Model_strategy)
def test_data_model_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Data_Attribut_strategy)
@settings(max_examples=50)
def test_data_attribut_instantiation(instance):
    assert isinstance(instance, Data_Attribut)



@given(instance=Data_Attribut_strategy)
def test_data_attribut_Static_setter(instance):
    original = instance.Static
    instance.Static = original
    assert instance.Static == original



@given(instance=Data_Attribut_strategy)
def test_data_attribut_Visibility_setter(instance):
    original = instance.Visibility
    instance.Visibility = original
    assert instance.Visibility == original



@given(instance=Data_Attribut_strategy)
def test_data_attribut_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Data_Attribut_strategy)
def test_data_attribut_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=Data_Class_strategy)
@settings(max_examples=50)
def test_data_class_instantiation(instance):
    assert isinstance(instance, Data_Class)



@given(instance=Data_Class_strategy)
def test_data_class_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

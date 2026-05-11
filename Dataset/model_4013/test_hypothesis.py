import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data::Model,
    Data::Attribut,
    Data::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data::model_is_not_abstract():
    assert not inspect.isabstract(Data::Model)


def test_data::model_constructor_exists():
    assert callable(Data::Model.__init__)


def test_data::model_constructor_args():
    sig = inspect.signature(Data::Model.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_data::model_has_Name():
    assert hasattr(Data::Model, "Name")
    descriptor = None
    for klass in Data::Model.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_data::attribut_is_not_abstract():
    assert not inspect.isabstract(Data::Attribut)


def test_data::attribut_constructor_exists():
    assert callable(Data::Attribut.__init__)


def test_data::attribut_constructor_args():
    sig = inspect.signature(Data::Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Visibility" in params, "Missing parameter 'Visibility'"
    assert "Static" in params, "Missing parameter 'Static'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_data::attribut_has_Type():
    assert hasattr(Data::Attribut, "Type")
    descriptor = None
    for klass in Data::Attribut.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_data::attribut_has_Visibility():
    assert hasattr(Data::Attribut, "Visibility")
    descriptor = None
    for klass in Data::Attribut.__mro__:
        if "Visibility" in klass.__dict__:
            descriptor = klass.__dict__["Visibility"]
            break
    assert isinstance(descriptor, property)

def test_data::attribut_has_Static():
    assert hasattr(Data::Attribut, "Static")
    descriptor = None
    for klass in Data::Attribut.__mro__:
        if "Static" in klass.__dict__:
            descriptor = klass.__dict__["Static"]
            break
    assert isinstance(descriptor, property)

def test_data::attribut_has_Name():
    assert hasattr(Data::Attribut, "Name")
    descriptor = None
    for klass in Data::Attribut.__mro__:
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
Data::Model_strategy = st.builds(
    Data::Model,
    Name=
        safe_text
)
Data::Attribut_strategy = st.builds(
    Data::Attribut,
    Type=
        safe_text,
    Visibility=
        safe_text,
    Static=
        st.booleans(),
    Name=
        safe_text
)
Data::Class_strategy = st.builds(
    Data::Class,
    Name=
        safe_text
)

@given(instance=Data::Model_strategy)
@settings(max_examples=50)
def test_data::model_instantiation(instance):
    assert isinstance(instance, Data::Model)

@given(instance=Data::Model_strategy)
def test_data::model_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Data::Model_strategy)
def test_data::model_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Data::Attribut_strategy)
@settings(max_examples=50)
def test_data::attribut_instantiation(instance):
    assert isinstance(instance, Data::Attribut)

@given(instance=Data::Attribut_strategy)
def test_data::attribut_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=Data::Attribut_strategy)
def test_data::attribut_Visibility_type(instance):
    assert isinstance(instance.Visibility, str)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_Visibility_setter(instance):
    original = instance.Visibility
    instance.Visibility = original
    assert instance.Visibility == original

@given(instance=Data::Attribut_strategy)
def test_data::attribut_Static_type(instance):
    assert isinstance(instance.Static, bool)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_Static_setter(instance):
    original = instance.Static
    instance.Static = original
    assert instance.Static == original

@given(instance=Data::Attribut_strategy)
def test_data::attribut_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Data::Attribut_strategy)
def test_data::attribut_Name_setter(instance):
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

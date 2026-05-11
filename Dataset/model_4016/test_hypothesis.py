import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data::Parameter,
    Data::Attribute,
    Data::Method,
    Data::Class,
    Data::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data::parameter_is_not_abstract():
    assert not inspect.isabstract(Data::Parameter)


def test_data::parameter_constructor_exists():
    assert callable(Data::Parameter.__init__)


def test_data::parameter_constructor_args():
    sig = inspect.signature(Data::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_data::parameter_has_name():
    assert hasattr(Data::Parameter, "name")
    descriptor = None
    for klass in Data::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_data::parameter_has_type():
    assert hasattr(Data::Parameter, "type")
    descriptor = None
    for klass in Data::Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_data::attribute_is_not_abstract():
    assert not inspect.isabstract(Data::Attribute)


def test_data::attribute_constructor_exists():
    assert callable(Data::Attribute.__init__)


def test_data::attribute_constructor_args():
    sig = inspect.signature(Data::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_data::attribute_has_type():
    assert hasattr(Data::Attribute, "type")
    descriptor = None
    for klass in Data::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_data::attribute_has_modifier():
    assert hasattr(Data::Attribute, "modifier")
    descriptor = None
    for klass in Data::Attribute.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
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



def test_data::method_is_not_abstract():
    assert not inspect.isabstract(Data::Method)


def test_data::method_constructor_exists():
    assert callable(Data::Method.__init__)


def test_data::method_constructor_args():
    sig = inspect.signature(Data::Method.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_data::method_has_modifier():
    assert hasattr(Data::Method, "modifier")
    descriptor = None
    for klass in Data::Method.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_data::method_has_name():
    assert hasattr(Data::Method, "name")
    descriptor = None
    for klass in Data::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_data::method_has_type():
    assert hasattr(Data::Method, "type")
    descriptor = None
    for klass in Data::Method.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
Data::Parameter_strategy = st.builds(
    Data::Parameter,
    name=
        safe_text,
    type=
        safe_text
)
Data::Attribute_strategy = st.builds(
    Data::Attribute,
    type=
        safe_text,
    modifier=
        safe_text,
    name=
        safe_text
)
Data::Method_strategy = st.builds(
    Data::Method,
    modifier=
        safe_text,
    name=
        safe_text,
    type=
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

@given(instance=Data::Parameter_strategy)
@settings(max_examples=50)
def test_data::parameter_instantiation(instance):
    assert isinstance(instance, Data::Parameter)

@given(instance=Data::Parameter_strategy)
def test_data::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Parameter_strategy)
def test_data::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Parameter_strategy)
def test_data::parameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Data::Parameter_strategy)
def test_data::parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Data::Attribute_strategy)
@settings(max_examples=50)
def test_data::attribute_instantiation(instance):
    assert isinstance(instance, Data::Attribute)

@given(instance=Data::Attribute_strategy)
def test_data::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Data::Attribute_strategy)
def test_data::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Data::Attribute_strategy)
def test_data::attribute_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=Data::Attribute_strategy)
def test_data::attribute_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=Data::Attribute_strategy)
def test_data::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Attribute_strategy)
def test_data::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Method_strategy)
@settings(max_examples=50)
def test_data::method_instantiation(instance):
    assert isinstance(instance, Data::Method)

@given(instance=Data::Method_strategy)
def test_data::method_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=Data::Method_strategy)
def test_data::method_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=Data::Method_strategy)
def test_data::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Method_strategy)
def test_data::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Method_strategy)
def test_data::method_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Data::Method_strategy)
def test_data::method_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

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

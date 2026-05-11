import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data::Parameter,
    Data::Method,
    Data::Attribute,
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
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_data::parameter_has_type():
    assert hasattr(Data::Parameter, "type")
    descriptor = None
    for klass in Data::Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_data::parameter_has_name():
    assert hasattr(Data::Parameter, "name")
    descriptor = None
    for klass in Data::Parameter.__mro__:
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
    assert "return_" in params, "Missing parameter 'return_'"
    assert "name" in params, "Missing parameter 'name'"
    assert "encapsulation" in params, "Missing parameter 'encapsulation'"

def test_data::method_has_return_():
    assert hasattr(Data::Method, "return_")
    descriptor = None
    for klass in Data::Method.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
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

def test_data::method_has_encapsulation():
    assert hasattr(Data::Method, "encapsulation")
    descriptor = None
    for klass in Data::Method.__mro__:
        if "encapsulation" in klass.__dict__:
            descriptor = klass.__dict__["encapsulation"]
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
    assert "name" in params, "Missing parameter 'name'"
    assert "encapsulation" in params, "Missing parameter 'encapsulation'"

def test_data::attribute_has_type():
    assert hasattr(Data::Attribute, "type")
    descriptor = None
    for klass in Data::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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

def test_data::attribute_has_encapsulation():
    assert hasattr(Data::Attribute, "encapsulation")
    descriptor = None
    for klass in Data::Attribute.__mro__:
        if "encapsulation" in klass.__dict__:
            descriptor = klass.__dict__["encapsulation"]
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
Data::Parameter_strategy = st.builds(
    Data::Parameter,
    type=
        safe_text,
    name=
        safe_text
)
Data::Method_strategy = st.builds(
    Data::Method,
    return_=
        safe_text,
    name=
        safe_text,
    encapsulation=
        safe_text
)
Data::Attribute_strategy = st.builds(
    Data::Attribute,
    type=
        safe_text,
    name=
        safe_text,
    encapsulation=
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

@given(instance=Data::Parameter_strategy)
@settings(max_examples=50)
def test_data::parameter_instantiation(instance):
    assert isinstance(instance, Data::Parameter)

@given(instance=Data::Parameter_strategy)
def test_data::parameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Data::Parameter_strategy)
def test_data::parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Data::Parameter_strategy)
def test_data::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Parameter_strategy)
def test_data::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Method_strategy)
@settings(max_examples=50)
def test_data::method_instantiation(instance):
    assert isinstance(instance, Data::Method)

@given(instance=Data::Method_strategy)
def test_data::method_return__type(instance):
    assert isinstance(instance.return_, str)


@given(instance=Data::Method_strategy)
def test_data::method_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=Data::Method_strategy)
def test_data::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Method_strategy)
def test_data::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Method_strategy)
def test_data::method_encapsulation_type(instance):
    assert isinstance(instance.encapsulation, str)


@given(instance=Data::Method_strategy)
def test_data::method_encapsulation_setter(instance):
    original = instance.encapsulation
    instance.encapsulation = original
    assert instance.encapsulation == original

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
def test_data::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Data::Attribute_strategy)
def test_data::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data::Attribute_strategy)
def test_data::attribute_encapsulation_type(instance):
    assert isinstance(instance.encapsulation, str)


@given(instance=Data::Attribute_strategy)
def test_data::attribute_encapsulation_setter(instance):
    original = instance.encapsulation
    instance.encapsulation = original
    assert instance.encapsulation == original

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

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Data_Parameter,
    Data_Method,
    Data_Attribute,
    Data_Class,
    Data_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_parameter_is_not_abstract():
    assert not inspect.isabstract(Data_Parameter)


def test_data_parameter_constructor_exists():
    assert callable(Data_Parameter.__init__)


def test_data_parameter_constructor_args():
    sig = inspect.signature(Data_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_data_parameter_has_type():
    assert hasattr(Data_Parameter, "type")
    descriptor = None
    for klass in Data_Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_data_parameter_has_name():
    assert hasattr(Data_Parameter, "name")
    descriptor = None
    for klass in Data_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_data_method_is_not_abstract():
    assert not inspect.isabstract(Data_Method)


def test_data_method_constructor_exists():
    assert callable(Data_Method.__init__)


def test_data_method_constructor_args():
    sig = inspect.signature(Data_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "encapsulation" in params, "Missing parameter 'encapsulation'"
    assert "return_" in params, "Missing parameter 'return_'"

def test_data_method_has_name():
    assert hasattr(Data_Method, "name")
    descriptor = None
    for klass in Data_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_data_method_has_encapsulation():
    assert hasattr(Data_Method, "encapsulation")
    descriptor = None
    for klass in Data_Method.__mro__:
        if "encapsulation" in klass.__dict__:
            descriptor = klass.__dict__["encapsulation"]
            break
    assert isinstance(descriptor, property)

def test_data_method_has_return_():
    assert hasattr(Data_Method, "return_")
    descriptor = None
    for klass in Data_Method.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)



def test_data_attribute_is_not_abstract():
    assert not inspect.isabstract(Data_Attribute)


def test_data_attribute_constructor_exists():
    assert callable(Data_Attribute.__init__)


def test_data_attribute_constructor_args():
    sig = inspect.signature(Data_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "encapsulation" in params, "Missing parameter 'encapsulation'"
    assert "name" in params, "Missing parameter 'name'"

def test_data_attribute_has_type():
    assert hasattr(Data_Attribute, "type")
    descriptor = None
    for klass in Data_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_data_attribute_has_encapsulation():
    assert hasattr(Data_Attribute, "encapsulation")
    descriptor = None
    for klass in Data_Attribute.__mro__:
        if "encapsulation" in klass.__dict__:
            descriptor = klass.__dict__["encapsulation"]
            break
    assert isinstance(descriptor, property)

def test_data_attribute_has_name():
    assert hasattr(Data_Attribute, "name")
    descriptor = None
    for klass in Data_Attribute.__mro__:
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
Data_Parameter_strategy = st.builds(
    Data_Parameter,
    type=
        safe_text,
    name=
        safe_text
)
Data_Method_strategy = st.builds(
    Data_Method,
    name=
        safe_text,
    encapsulation=
        safe_text,
    return_=
        safe_text
)
Data_Attribute_strategy = st.builds(
    Data_Attribute,
    type=
        safe_text,
    encapsulation=
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

@given(instance=Data_Parameter_strategy)
@settings(max_examples=50)
def test_data_parameter_instantiation(instance):
    assert isinstance(instance, Data_Parameter)



@given(instance=Data_Parameter_strategy)
def test_data_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Data_Parameter_strategy)
def test_data_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Data_Method_strategy)
@settings(max_examples=50)
def test_data_method_instantiation(instance):
    assert isinstance(instance, Data_Method)



@given(instance=Data_Method_strategy)
def test_data_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Data_Method_strategy)
def test_data_method_encapsulation_setter(instance):
    original = instance.encapsulation
    instance.encapsulation = original
    assert instance.encapsulation == original



@given(instance=Data_Method_strategy)
def test_data_method_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=Data_Attribute_strategy)
@settings(max_examples=50)
def test_data_attribute_instantiation(instance):
    assert isinstance(instance, Data_Attribute)



@given(instance=Data_Attribute_strategy)
def test_data_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Data_Attribute_strategy)
def test_data_attribute_encapsulation_setter(instance):
    original = instance.encapsulation
    instance.encapsulation = original
    assert instance.encapsulation == original



@given(instance=Data_Attribute_strategy)
def test_data_attribute_name_setter(instance):
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

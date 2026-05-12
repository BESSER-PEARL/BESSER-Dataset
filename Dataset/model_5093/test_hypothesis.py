import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Interface,
    adl201_Interface,
    adl201_Binding,
    adl201_Provided,
    adl201_Required,
    adl201_Content,
    adl201_BindingAttributes,
    adl201_Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_adl201_interface_is_not_abstract():
    assert not inspect.isabstract(adl201_Interface)


def test_adl201_interface_constructor_exists():
    assert callable(adl201_Interface.__init__)


def test_adl201_interface_constructor_args():
    sig = inspect.signature(adl201_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl201_interface_has_name():
    assert hasattr(adl201_Interface, "name")
    descriptor = None
    for klass in adl201_Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adl201_interface_has_signature():
    assert hasattr(adl201_Interface, "signature")
    descriptor = None
    for klass in adl201_Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl201_binding_is_not_abstract():
    assert not inspect.isabstract(adl201_Binding)


def test_adl201_binding_constructor_exists():
    assert callable(adl201_Binding.__init__)


def test_adl201_binding_constructor_args():
    sig = inspect.signature(adl201_Binding.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl201_binding_has_name():
    assert hasattr(adl201_Binding, "name")
    descriptor = None
    for klass in adl201_Binding.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl201_provided_is_not_abstract():
    assert not inspect.isabstract(adl201_Provided)


def test_adl201_provided_constructor_exists():
    assert callable(adl201_Provided.__init__)


def test_adl201_provided_constructor_args():
    sig = inspect.signature(adl201_Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl201_required_is_not_abstract():
    assert not inspect.isabstract(adl201_Required)


def test_adl201_required_constructor_exists():
    assert callable(adl201_Required.__init__)


def test_adl201_required_constructor_args():
    sig = inspect.signature(adl201_Required.__init__)
    params = list(sig.parameters.keys())



def test_adl201_content_is_not_abstract():
    assert not inspect.isabstract(adl201_Content)


def test_adl201_content_constructor_exists():
    assert callable(adl201_Content.__init__)


def test_adl201_content_constructor_args():
    sig = inspect.signature(adl201_Content.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "language" in params, "Missing parameter 'language'"

def test_adl201_content_has_expression():
    assert hasattr(adl201_Content, "expression")
    descriptor = None
    for klass in adl201_Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_adl201_content_has_language():
    assert hasattr(adl201_Content, "language")
    descriptor = None
    for klass in adl201_Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_adl201_bindingattributes_is_not_abstract():
    assert not inspect.isabstract(adl201_BindingAttributes)


def test_adl201_bindingattributes_constructor_exists():
    assert callable(adl201_BindingAttributes.__init__)


def test_adl201_bindingattributes_constructor_args():
    sig = inspect.signature(adl201_BindingAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl201_bindingattributes_has_value():
    assert hasattr(adl201_BindingAttributes, "value")
    descriptor = None
    for klass in adl201_BindingAttributes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_adl201_bindingattributes_has_name():
    assert hasattr(adl201_BindingAttributes, "name")
    descriptor = None
    for klass in adl201_BindingAttributes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl201_component_is_not_abstract():
    assert not inspect.isabstract(adl201_Component)


def test_adl201_component_constructor_exists():
    assert callable(adl201_Component.__init__)


def test_adl201_component_constructor_args():
    sig = inspect.signature(adl201_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl201_component_has_name():
    assert hasattr(adl201_Component, "name")
    descriptor = None
    for klass in adl201_Component.__mro__:
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
Interface_strategy = st.builds(
    Interface,
)
adl201_Interface_strategy = st.builds(
    adl201_Interface,
    name=
        safe_text,
    signature=
        safe_text
)
adl201_Binding_strategy = st.builds(
    adl201_Binding,
    name=
        safe_text
)
adl201_Provided_strategy = st.builds(
    adl201_Provided,
)
adl201_Required_strategy = st.builds(
    adl201_Required,
)
adl201_Content_strategy = st.builds(
    adl201_Content,
    expression=
        safe_text,
    language=
        safe_text
)
adl201_BindingAttributes_strategy = st.builds(
    adl201_BindingAttributes,
    value=
        safe_text,
    name=
        safe_text
)
adl201_Component_strategy = st.builds(
    adl201_Component,
    name=
        safe_text
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl201_Interface_strategy)
@settings(max_examples=50)
def test_adl201_interface_instantiation(instance):
    assert isinstance(instance, adl201_Interface)



@given(instance=adl201_Interface_strategy)
def test_adl201_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=adl201_Interface_strategy)
def test_adl201_interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl201_Binding_strategy)
@settings(max_examples=50)
def test_adl201_binding_instantiation(instance):
    assert isinstance(instance, adl201_Binding)



@given(instance=adl201_Binding_strategy)
def test_adl201_binding_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl201_Provided_strategy)
@settings(max_examples=50)
def test_adl201_provided_instantiation(instance):
    assert isinstance(instance, adl201_Provided)

@given(instance=adl201_Required_strategy)
@settings(max_examples=50)
def test_adl201_required_instantiation(instance):
    assert isinstance(instance, adl201_Required)

@given(instance=adl201_Content_strategy)
@settings(max_examples=50)
def test_adl201_content_instantiation(instance):
    assert isinstance(instance, adl201_Content)



@given(instance=adl201_Content_strategy)
def test_adl201_content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=adl201_Content_strategy)
def test_adl201_content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=adl201_BindingAttributes_strategy)
@settings(max_examples=50)
def test_adl201_bindingattributes_instantiation(instance):
    assert isinstance(instance, adl201_BindingAttributes)



@given(instance=adl201_BindingAttributes_strategy)
def test_adl201_bindingattributes_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=adl201_BindingAttributes_strategy)
def test_adl201_bindingattributes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl201_Component_strategy)
@settings(max_examples=50)
def test_adl201_component_instantiation(instance):
    assert isinstance(instance, adl201_Component)



@given(instance=adl201_Component_strategy)
def test_adl201_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

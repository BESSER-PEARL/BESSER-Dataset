import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    adl202_Interface,
    adl202_Binding,
    Interface,
    adl202_BindingAttributes,
    adl202_Provided,
    adl202_Required,
    adl202_Content,
    adl202_Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adl202_interface_is_not_abstract():
    assert not inspect.isabstract(adl202_Interface)


def test_adl202_interface_constructor_exists():
    assert callable(adl202_Interface.__init__)


def test_adl202_interface_constructor_args():
    sig = inspect.signature(adl202_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl202_interface_has_name():
    assert hasattr(adl202_Interface, "name")
    descriptor = None
    for klass in adl202_Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adl202_interface_has_signature():
    assert hasattr(adl202_Interface, "signature")
    descriptor = None
    for klass in adl202_Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl202_binding_is_not_abstract():
    assert not inspect.isabstract(adl202_Binding)


def test_adl202_binding_constructor_exists():
    assert callable(adl202_Binding.__init__)


def test_adl202_binding_constructor_args():
    sig = inspect.signature(adl202_Binding.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl202_binding_has_name():
    assert hasattr(adl202_Binding, "name")
    descriptor = None
    for klass in adl202_Binding.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_adl202_bindingattributes_is_not_abstract():
    assert not inspect.isabstract(adl202_BindingAttributes)


def test_adl202_bindingattributes_constructor_exists():
    assert callable(adl202_BindingAttributes.__init__)


def test_adl202_bindingattributes_constructor_args():
    sig = inspect.signature(adl202_BindingAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl202_bindingattributes_has_value():
    assert hasattr(adl202_BindingAttributes, "value")
    descriptor = None
    for klass in adl202_BindingAttributes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_adl202_bindingattributes_has_name():
    assert hasattr(adl202_BindingAttributes, "name")
    descriptor = None
    for klass in adl202_BindingAttributes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl202_provided_is_not_abstract():
    assert not inspect.isabstract(adl202_Provided)


def test_adl202_provided_constructor_exists():
    assert callable(adl202_Provided.__init__)


def test_adl202_provided_constructor_args():
    sig = inspect.signature(adl202_Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl202_required_is_not_abstract():
    assert not inspect.isabstract(adl202_Required)


def test_adl202_required_constructor_exists():
    assert callable(adl202_Required.__init__)


def test_adl202_required_constructor_args():
    sig = inspect.signature(adl202_Required.__init__)
    params = list(sig.parameters.keys())



def test_adl202_content_is_not_abstract():
    assert not inspect.isabstract(adl202_Content)


def test_adl202_content_constructor_exists():
    assert callable(adl202_Content.__init__)


def test_adl202_content_constructor_args():
    sig = inspect.signature(adl202_Content.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "language" in params, "Missing parameter 'language'"

def test_adl202_content_has_expression():
    assert hasattr(adl202_Content, "expression")
    descriptor = None
    for klass in adl202_Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_adl202_content_has_language():
    assert hasattr(adl202_Content, "language")
    descriptor = None
    for klass in adl202_Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_adl202_component_is_not_abstract():
    assert not inspect.isabstract(adl202_Component)


def test_adl202_component_constructor_exists():
    assert callable(adl202_Component.__init__)


def test_adl202_component_constructor_args():
    sig = inspect.signature(adl202_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl202_component_has_name():
    assert hasattr(adl202_Component, "name")
    descriptor = None
    for klass in adl202_Component.__mro__:
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
adl202_Interface_strategy = st.builds(
    adl202_Interface,
    name=
        safe_text,
    signature=
        safe_text
)
adl202_Binding_strategy = st.builds(
    adl202_Binding,
    name=
        safe_text
)
Interface_strategy = st.builds(
    Interface,
)
adl202_BindingAttributes_strategy = st.builds(
    adl202_BindingAttributes,
    value=
        safe_text,
    name=
        safe_text
)
adl202_Provided_strategy = st.builds(
    adl202_Provided,
)
adl202_Required_strategy = st.builds(
    adl202_Required,
)
adl202_Content_strategy = st.builds(
    adl202_Content,
    expression=
        safe_text,
    language=
        safe_text
)
adl202_Component_strategy = st.builds(
    adl202_Component,
    name=
        safe_text
)

@given(instance=adl202_Interface_strategy)
@settings(max_examples=50)
def test_adl202_interface_instantiation(instance):
    assert isinstance(instance, adl202_Interface)



@given(instance=adl202_Interface_strategy)
def test_adl202_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=adl202_Interface_strategy)
def test_adl202_interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl202_Binding_strategy)
@settings(max_examples=50)
def test_adl202_binding_instantiation(instance):
    assert isinstance(instance, adl202_Binding)



@given(instance=adl202_Binding_strategy)
def test_adl202_binding_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl202_BindingAttributes_strategy)
@settings(max_examples=50)
def test_adl202_bindingattributes_instantiation(instance):
    assert isinstance(instance, adl202_BindingAttributes)



@given(instance=adl202_BindingAttributes_strategy)
def test_adl202_bindingattributes_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=adl202_BindingAttributes_strategy)
def test_adl202_bindingattributes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl202_Provided_strategy)
@settings(max_examples=50)
def test_adl202_provided_instantiation(instance):
    assert isinstance(instance, adl202_Provided)

@given(instance=adl202_Required_strategy)
@settings(max_examples=50)
def test_adl202_required_instantiation(instance):
    assert isinstance(instance, adl202_Required)

@given(instance=adl202_Content_strategy)
@settings(max_examples=50)
def test_adl202_content_instantiation(instance):
    assert isinstance(instance, adl202_Content)



@given(instance=adl202_Content_strategy)
def test_adl202_content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=adl202_Content_strategy)
def test_adl202_content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=adl202_Component_strategy)
@settings(max_examples=50)
def test_adl202_component_instantiation(instance):
    assert isinstance(instance, adl202_Component)



@given(instance=adl202_Component_strategy)
def test_adl202_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

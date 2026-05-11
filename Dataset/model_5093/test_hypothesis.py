import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Interface,
    adl201::Interface,
    adl201::Binding,
    adl201::Provided,
    adl201::Required,
    adl201::Content,
    adl201::BindingAttributes,
    adl201::Component,
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



def test_adl201::interface_is_not_abstract():
    assert not inspect.isabstract(adl201::Interface)


def test_adl201::interface_constructor_exists():
    assert callable(adl201::Interface.__init__)


def test_adl201::interface_constructor_args():
    sig = inspect.signature(adl201::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl201::interface_has_signature():
    assert hasattr(adl201::Interface, "signature")
    descriptor = None
    for klass in adl201::Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adl201::interface_has_name():
    assert hasattr(adl201::Interface, "name")
    descriptor = None
    for klass in adl201::Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl201::binding_is_not_abstract():
    assert not inspect.isabstract(adl201::Binding)


def test_adl201::binding_constructor_exists():
    assert callable(adl201::Binding.__init__)


def test_adl201::binding_constructor_args():
    sig = inspect.signature(adl201::Binding.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl201::binding_has_name():
    assert hasattr(adl201::Binding, "name")
    descriptor = None
    for klass in adl201::Binding.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl201::provided_is_not_abstract():
    assert not inspect.isabstract(adl201::Provided)


def test_adl201::provided_constructor_exists():
    assert callable(adl201::Provided.__init__)


def test_adl201::provided_constructor_args():
    sig = inspect.signature(adl201::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl201::required_is_not_abstract():
    assert not inspect.isabstract(adl201::Required)


def test_adl201::required_constructor_exists():
    assert callable(adl201::Required.__init__)


def test_adl201::required_constructor_args():
    sig = inspect.signature(adl201::Required.__init__)
    params = list(sig.parameters.keys())



def test_adl201::content_is_not_abstract():
    assert not inspect.isabstract(adl201::Content)


def test_adl201::content_constructor_exists():
    assert callable(adl201::Content.__init__)


def test_adl201::content_constructor_args():
    sig = inspect.signature(adl201::Content.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_adl201::content_has_language():
    assert hasattr(adl201::Content, "language")
    descriptor = None
    for klass in adl201::Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_adl201::content_has_expression():
    assert hasattr(adl201::Content, "expression")
    descriptor = None
    for klass in adl201::Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_adl201::bindingattributes_is_not_abstract():
    assert not inspect.isabstract(adl201::BindingAttributes)


def test_adl201::bindingattributes_constructor_exists():
    assert callable(adl201::BindingAttributes.__init__)


def test_adl201::bindingattributes_constructor_args():
    sig = inspect.signature(adl201::BindingAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_adl201::bindingattributes_has_name():
    assert hasattr(adl201::BindingAttributes, "name")
    descriptor = None
    for klass in adl201::BindingAttributes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adl201::bindingattributes_has_value():
    assert hasattr(adl201::BindingAttributes, "value")
    descriptor = None
    for klass in adl201::BindingAttributes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adl201::component_is_not_abstract():
    assert not inspect.isabstract(adl201::Component)


def test_adl201::component_constructor_exists():
    assert callable(adl201::Component.__init__)


def test_adl201::component_constructor_args():
    sig = inspect.signature(adl201::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl201::component_has_name():
    assert hasattr(adl201::Component, "name")
    descriptor = None
    for klass in adl201::Component.__mro__:
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
adl201::Interface_strategy = st.builds(
    adl201::Interface,
    signature=
        safe_text,
    name=
        safe_text
)
adl201::Binding_strategy = st.builds(
    adl201::Binding,
    name=
        safe_text
)
adl201::Provided_strategy = st.builds(
    adl201::Provided,
)
adl201::Required_strategy = st.builds(
    adl201::Required,
)
adl201::Content_strategy = st.builds(
    adl201::Content,
    language=
        safe_text,
    expression=
        safe_text
)
adl201::BindingAttributes_strategy = st.builds(
    adl201::BindingAttributes,
    name=
        safe_text,
    value=
        safe_text
)
adl201::Component_strategy = st.builds(
    adl201::Component,
    name=
        safe_text
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl201::Interface_strategy)
@settings(max_examples=50)
def test_adl201::interface_instantiation(instance):
    assert isinstance(instance, adl201::Interface)

@given(instance=adl201::Interface_strategy)
def test_adl201::interface_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adl201::Interface_strategy)
def test_adl201::interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl201::Interface_strategy)
def test_adl201::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl201::Interface_strategy)
def test_adl201::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl201::Binding_strategy)
@settings(max_examples=50)
def test_adl201::binding_instantiation(instance):
    assert isinstance(instance, adl201::Binding)

@given(instance=adl201::Binding_strategy)
def test_adl201::binding_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl201::Binding_strategy)
def test_adl201::binding_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl201::Provided_strategy)
@settings(max_examples=50)
def test_adl201::provided_instantiation(instance):
    assert isinstance(instance, adl201::Provided)

@given(instance=adl201::Required_strategy)
@settings(max_examples=50)
def test_adl201::required_instantiation(instance):
    assert isinstance(instance, adl201::Required)

@given(instance=adl201::Content_strategy)
@settings(max_examples=50)
def test_adl201::content_instantiation(instance):
    assert isinstance(instance, adl201::Content)

@given(instance=adl201::Content_strategy)
def test_adl201::content_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=adl201::Content_strategy)
def test_adl201::content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=adl201::Content_strategy)
def test_adl201::content_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=adl201::Content_strategy)
def test_adl201::content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=adl201::BindingAttributes_strategy)
@settings(max_examples=50)
def test_adl201::bindingattributes_instantiation(instance):
    assert isinstance(instance, adl201::BindingAttributes)

@given(instance=adl201::BindingAttributes_strategy)
def test_adl201::bindingattributes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl201::BindingAttributes_strategy)
def test_adl201::bindingattributes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl201::BindingAttributes_strategy)
def test_adl201::bindingattributes_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=adl201::BindingAttributes_strategy)
def test_adl201::bindingattributes_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=adl201::Component_strategy)
@settings(max_examples=50)
def test_adl201::component_instantiation(instance):
    assert isinstance(instance, adl201::Component)

@given(instance=adl201::Component_strategy)
def test_adl201::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl201::Component_strategy)
def test_adl201::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    adl202::Interface,
    adl202::Binding,
    Interface,
    adl202::BindingAttributes,
    adl202::Provided,
    adl202::Required,
    adl202::Content,
    adl202::Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adl202::interface_is_not_abstract():
    assert not inspect.isabstract(adl202::Interface)


def test_adl202::interface_constructor_exists():
    assert callable(adl202::Interface.__init__)


def test_adl202::interface_constructor_args():
    sig = inspect.signature(adl202::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl202::interface_has_signature():
    assert hasattr(adl202::Interface, "signature")
    descriptor = None
    for klass in adl202::Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adl202::interface_has_name():
    assert hasattr(adl202::Interface, "name")
    descriptor = None
    for klass in adl202::Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl202::binding_is_not_abstract():
    assert not inspect.isabstract(adl202::Binding)


def test_adl202::binding_constructor_exists():
    assert callable(adl202::Binding.__init__)


def test_adl202::binding_constructor_args():
    sig = inspect.signature(adl202::Binding.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl202::binding_has_name():
    assert hasattr(adl202::Binding, "name")
    descriptor = None
    for klass in adl202::Binding.__mro__:
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



def test_adl202::bindingattributes_is_not_abstract():
    assert not inspect.isabstract(adl202::BindingAttributes)


def test_adl202::bindingattributes_constructor_exists():
    assert callable(adl202::BindingAttributes.__init__)


def test_adl202::bindingattributes_constructor_args():
    sig = inspect.signature(adl202::BindingAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl202::bindingattributes_has_value():
    assert hasattr(adl202::BindingAttributes, "value")
    descriptor = None
    for klass in adl202::BindingAttributes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_adl202::bindingattributes_has_name():
    assert hasattr(adl202::BindingAttributes, "name")
    descriptor = None
    for klass in adl202::BindingAttributes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl202::provided_is_not_abstract():
    assert not inspect.isabstract(adl202::Provided)


def test_adl202::provided_constructor_exists():
    assert callable(adl202::Provided.__init__)


def test_adl202::provided_constructor_args():
    sig = inspect.signature(adl202::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl202::required_is_not_abstract():
    assert not inspect.isabstract(adl202::Required)


def test_adl202::required_constructor_exists():
    assert callable(adl202::Required.__init__)


def test_adl202::required_constructor_args():
    sig = inspect.signature(adl202::Required.__init__)
    params = list(sig.parameters.keys())



def test_adl202::content_is_not_abstract():
    assert not inspect.isabstract(adl202::Content)


def test_adl202::content_constructor_exists():
    assert callable(adl202::Content.__init__)


def test_adl202::content_constructor_args():
    sig = inspect.signature(adl202::Content.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "language" in params, "Missing parameter 'language'"

def test_adl202::content_has_expression():
    assert hasattr(adl202::Content, "expression")
    descriptor = None
    for klass in adl202::Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_adl202::content_has_language():
    assert hasattr(adl202::Content, "language")
    descriptor = None
    for klass in adl202::Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_adl202::component_is_not_abstract():
    assert not inspect.isabstract(adl202::Component)


def test_adl202::component_constructor_exists():
    assert callable(adl202::Component.__init__)


def test_adl202::component_constructor_args():
    sig = inspect.signature(adl202::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl202::component_has_name():
    assert hasattr(adl202::Component, "name")
    descriptor = None
    for klass in adl202::Component.__mro__:
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
adl202::Interface_strategy = st.builds(
    adl202::Interface,
    signature=
        safe_text,
    name=
        safe_text
)
adl202::Binding_strategy = st.builds(
    adl202::Binding,
    name=
        safe_text
)
Interface_strategy = st.builds(
    Interface,
)
adl202::BindingAttributes_strategy = st.builds(
    adl202::BindingAttributes,
    value=
        safe_text,
    name=
        safe_text
)
adl202::Provided_strategy = st.builds(
    adl202::Provided,
)
adl202::Required_strategy = st.builds(
    adl202::Required,
)
adl202::Content_strategy = st.builds(
    adl202::Content,
    expression=
        safe_text,
    language=
        safe_text
)
adl202::Component_strategy = st.builds(
    adl202::Component,
    name=
        safe_text
)

@given(instance=adl202::Interface_strategy)
@settings(max_examples=50)
def test_adl202::interface_instantiation(instance):
    assert isinstance(instance, adl202::Interface)

@given(instance=adl202::Interface_strategy)
def test_adl202::interface_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adl202::Interface_strategy)
def test_adl202::interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl202::Interface_strategy)
def test_adl202::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl202::Interface_strategy)
def test_adl202::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl202::Binding_strategy)
@settings(max_examples=50)
def test_adl202::binding_instantiation(instance):
    assert isinstance(instance, adl202::Binding)

@given(instance=adl202::Binding_strategy)
def test_adl202::binding_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl202::Binding_strategy)
def test_adl202::binding_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl202::BindingAttributes_strategy)
@settings(max_examples=50)
def test_adl202::bindingattributes_instantiation(instance):
    assert isinstance(instance, adl202::BindingAttributes)

@given(instance=adl202::BindingAttributes_strategy)
def test_adl202::bindingattributes_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=adl202::BindingAttributes_strategy)
def test_adl202::bindingattributes_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=adl202::BindingAttributes_strategy)
def test_adl202::bindingattributes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl202::BindingAttributes_strategy)
def test_adl202::bindingattributes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl202::Provided_strategy)
@settings(max_examples=50)
def test_adl202::provided_instantiation(instance):
    assert isinstance(instance, adl202::Provided)

@given(instance=adl202::Required_strategy)
@settings(max_examples=50)
def test_adl202::required_instantiation(instance):
    assert isinstance(instance, adl202::Required)

@given(instance=adl202::Content_strategy)
@settings(max_examples=50)
def test_adl202::content_instantiation(instance):
    assert isinstance(instance, adl202::Content)

@given(instance=adl202::Content_strategy)
def test_adl202::content_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=adl202::Content_strategy)
def test_adl202::content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=adl202::Content_strategy)
def test_adl202::content_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=adl202::Content_strategy)
def test_adl202::content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=adl202::Component_strategy)
@settings(max_examples=50)
def test_adl202::component_instantiation(instance):
    assert isinstance(instance, adl202::Component)

@given(instance=adl202::Component_strategy)
def test_adl202::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl202::Component_strategy)
def test_adl202::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

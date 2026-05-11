import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Interface,
    adl101::Required,
    adl101::Component,
    adl101::Content,
    adl101::Binding,
    adl101::Interface,
    adl101::Provided,
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



def test_adl101::required_is_not_abstract():
    assert not inspect.isabstract(adl101::Required)


def test_adl101::required_constructor_exists():
    assert callable(adl101::Required.__init__)


def test_adl101::required_constructor_args():
    sig = inspect.signature(adl101::Required.__init__)
    params = list(sig.parameters.keys())



def test_adl101::component_is_not_abstract():
    assert not inspect.isabstract(adl101::Component)


def test_adl101::component_constructor_exists():
    assert callable(adl101::Component.__init__)


def test_adl101::component_constructor_args():
    sig = inspect.signature(adl101::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl101::component_has_name():
    assert hasattr(adl101::Component, "name")
    descriptor = None
    for klass in adl101::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl101::content_is_not_abstract():
    assert not inspect.isabstract(adl101::Content)


def test_adl101::content_constructor_exists():
    assert callable(adl101::Content.__init__)


def test_adl101::content_constructor_args():
    sig = inspect.signature(adl101::Content.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_adl101::content_has_language():
    assert hasattr(adl101::Content, "language")
    descriptor = None
    for klass in adl101::Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_adl101::content_has_expression():
    assert hasattr(adl101::Content, "expression")
    descriptor = None
    for klass in adl101::Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_adl101::binding_is_not_abstract():
    assert not inspect.isabstract(adl101::Binding)


def test_adl101::binding_constructor_exists():
    assert callable(adl101::Binding.__init__)


def test_adl101::binding_constructor_args():
    sig = inspect.signature(adl101::Binding.__init__)
    params = list(sig.parameters.keys())



def test_adl101::interface_is_not_abstract():
    assert not inspect.isabstract(adl101::Interface)


def test_adl101::interface_constructor_exists():
    assert callable(adl101::Interface.__init__)


def test_adl101::interface_constructor_args():
    sig = inspect.signature(adl101::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl101::interface_has_signature():
    assert hasattr(adl101::Interface, "signature")
    descriptor = None
    for klass in adl101::Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adl101::interface_has_name():
    assert hasattr(adl101::Interface, "name")
    descriptor = None
    for klass in adl101::Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl101::provided_is_not_abstract():
    assert not inspect.isabstract(adl101::Provided)


def test_adl101::provided_constructor_exists():
    assert callable(adl101::Provided.__init__)


def test_adl101::provided_constructor_args():
    sig = inspect.signature(adl101::Provided.__init__)
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
Interface_strategy = st.builds(
    Interface,
)
adl101::Required_strategy = st.builds(
    adl101::Required,
)
adl101::Component_strategy = st.builds(
    adl101::Component,
    name=
        safe_text
)
adl101::Content_strategy = st.builds(
    adl101::Content,
    language=
        safe_text,
    expression=
        safe_text
)
adl101::Binding_strategy = st.builds(
    adl101::Binding,
)
adl101::Interface_strategy = st.builds(
    adl101::Interface,
    signature=
        safe_text,
    name=
        safe_text
)
adl101::Provided_strategy = st.builds(
    adl101::Provided,
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl101::Required_strategy)
@settings(max_examples=50)
def test_adl101::required_instantiation(instance):
    assert isinstance(instance, adl101::Required)

@given(instance=adl101::Component_strategy)
@settings(max_examples=50)
def test_adl101::component_instantiation(instance):
    assert isinstance(instance, adl101::Component)

@given(instance=adl101::Component_strategy)
def test_adl101::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl101::Component_strategy)
def test_adl101::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl101::Content_strategy)
@settings(max_examples=50)
def test_adl101::content_instantiation(instance):
    assert isinstance(instance, adl101::Content)

@given(instance=adl101::Content_strategy)
def test_adl101::content_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=adl101::Content_strategy)
def test_adl101::content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=adl101::Content_strategy)
def test_adl101::content_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=adl101::Content_strategy)
def test_adl101::content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=adl101::Binding_strategy)
@settings(max_examples=50)
def test_adl101::binding_instantiation(instance):
    assert isinstance(instance, adl101::Binding)

@given(instance=adl101::Interface_strategy)
@settings(max_examples=50)
def test_adl101::interface_instantiation(instance):
    assert isinstance(instance, adl101::Interface)

@given(instance=adl101::Interface_strategy)
def test_adl101::interface_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adl101::Interface_strategy)
def test_adl101::interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl101::Interface_strategy)
def test_adl101::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl101::Interface_strategy)
def test_adl101::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl101::Provided_strategy)
@settings(max_examples=50)
def test_adl101::provided_instantiation(instance):
    assert isinstance(instance, adl101::Provided)

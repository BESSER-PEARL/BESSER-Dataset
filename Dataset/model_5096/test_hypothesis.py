import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Interface,
    adl200::Interface,
    adl200::Provided,
    adl200::Required,
    adl200::Component,
    adl200::Content,
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



def test_adl200::interface_is_not_abstract():
    assert not inspect.isabstract(adl200::Interface)


def test_adl200::interface_constructor_exists():
    assert callable(adl200::Interface.__init__)


def test_adl200::interface_constructor_args():
    sig = inspect.signature(adl200::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl200::interface_has_name():
    assert hasattr(adl200::Interface, "name")
    descriptor = None
    for klass in adl200::Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adl200::interface_has_signature():
    assert hasattr(adl200::Interface, "signature")
    descriptor = None
    for klass in adl200::Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl200::provided_is_not_abstract():
    assert not inspect.isabstract(adl200::Provided)


def test_adl200::provided_constructor_exists():
    assert callable(adl200::Provided.__init__)


def test_adl200::provided_constructor_args():
    sig = inspect.signature(adl200::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl200::required_is_not_abstract():
    assert not inspect.isabstract(adl200::Required)


def test_adl200::required_constructor_exists():
    assert callable(adl200::Required.__init__)


def test_adl200::required_constructor_args():
    sig = inspect.signature(adl200::Required.__init__)
    params = list(sig.parameters.keys())



def test_adl200::component_is_not_abstract():
    assert not inspect.isabstract(adl200::Component)


def test_adl200::component_constructor_exists():
    assert callable(adl200::Component.__init__)


def test_adl200::component_constructor_args():
    sig = inspect.signature(adl200::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl200::component_has_name():
    assert hasattr(adl200::Component, "name")
    descriptor = None
    for klass in adl200::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl200::content_is_not_abstract():
    assert not inspect.isabstract(adl200::Content)


def test_adl200::content_constructor_exists():
    assert callable(adl200::Content.__init__)


def test_adl200::content_constructor_args():
    sig = inspect.signature(adl200::Content.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "language" in params, "Missing parameter 'language'"

def test_adl200::content_has_expression():
    assert hasattr(adl200::Content, "expression")
    descriptor = None
    for klass in adl200::Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_adl200::content_has_language():
    assert hasattr(adl200::Content, "language")
    descriptor = None
    for klass in adl200::Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
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
adl200::Interface_strategy = st.builds(
    adl200::Interface,
    name=
        safe_text,
    signature=
        safe_text
)
adl200::Provided_strategy = st.builds(
    adl200::Provided,
)
adl200::Required_strategy = st.builds(
    adl200::Required,
)
adl200::Component_strategy = st.builds(
    adl200::Component,
    name=
        safe_text
)
adl200::Content_strategy = st.builds(
    adl200::Content,
    expression=
        safe_text,
    language=
        safe_text
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl200::Interface_strategy)
@settings(max_examples=50)
def test_adl200::interface_instantiation(instance):
    assert isinstance(instance, adl200::Interface)

@given(instance=adl200::Interface_strategy)
def test_adl200::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl200::Interface_strategy)
def test_adl200::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl200::Interface_strategy)
def test_adl200::interface_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adl200::Interface_strategy)
def test_adl200::interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl200::Provided_strategy)
@settings(max_examples=50)
def test_adl200::provided_instantiation(instance):
    assert isinstance(instance, adl200::Provided)

@given(instance=adl200::Required_strategy)
@settings(max_examples=50)
def test_adl200::required_instantiation(instance):
    assert isinstance(instance, adl200::Required)

@given(instance=adl200::Component_strategy)
@settings(max_examples=50)
def test_adl200::component_instantiation(instance):
    assert isinstance(instance, adl200::Component)

@given(instance=adl200::Component_strategy)
def test_adl200::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl200::Component_strategy)
def test_adl200::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl200::Content_strategy)
@settings(max_examples=50)
def test_adl200::content_instantiation(instance):
    assert isinstance(instance, adl200::Content)

@given(instance=adl200::Content_strategy)
def test_adl200::content_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=adl200::Content_strategy)
def test_adl200::content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=adl200::Content_strategy)
def test_adl200::content_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=adl200::Content_strategy)
def test_adl200::content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

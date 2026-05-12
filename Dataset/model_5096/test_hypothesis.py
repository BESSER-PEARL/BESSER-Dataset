import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Interface,
    adl200_Interface,
    adl200_Provided,
    adl200_Required,
    adl200_Component,
    adl200_Content,
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



def test_adl200_interface_is_not_abstract():
    assert not inspect.isabstract(adl200_Interface)


def test_adl200_interface_constructor_exists():
    assert callable(adl200_Interface.__init__)


def test_adl200_interface_constructor_args():
    sig = inspect.signature(adl200_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl200_interface_has_signature():
    assert hasattr(adl200_Interface, "signature")
    descriptor = None
    for klass in adl200_Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adl200_interface_has_name():
    assert hasattr(adl200_Interface, "name")
    descriptor = None
    for klass in adl200_Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl200_provided_is_not_abstract():
    assert not inspect.isabstract(adl200_Provided)


def test_adl200_provided_constructor_exists():
    assert callable(adl200_Provided.__init__)


def test_adl200_provided_constructor_args():
    sig = inspect.signature(adl200_Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl200_required_is_not_abstract():
    assert not inspect.isabstract(adl200_Required)


def test_adl200_required_constructor_exists():
    assert callable(adl200_Required.__init__)


def test_adl200_required_constructor_args():
    sig = inspect.signature(adl200_Required.__init__)
    params = list(sig.parameters.keys())



def test_adl200_component_is_not_abstract():
    assert not inspect.isabstract(adl200_Component)


def test_adl200_component_constructor_exists():
    assert callable(adl200_Component.__init__)


def test_adl200_component_constructor_args():
    sig = inspect.signature(adl200_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl200_component_has_name():
    assert hasattr(adl200_Component, "name")
    descriptor = None
    for klass in adl200_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl200_content_is_not_abstract():
    assert not inspect.isabstract(adl200_Content)


def test_adl200_content_constructor_exists():
    assert callable(adl200_Content.__init__)


def test_adl200_content_constructor_args():
    sig = inspect.signature(adl200_Content.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "language" in params, "Missing parameter 'language'"

def test_adl200_content_has_expression():
    assert hasattr(adl200_Content, "expression")
    descriptor = None
    for klass in adl200_Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_adl200_content_has_language():
    assert hasattr(adl200_Content, "language")
    descriptor = None
    for klass in adl200_Content.__mro__:
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
adl200_Interface_strategy = st.builds(
    adl200_Interface,
    signature=
        safe_text,
    name=
        safe_text
)
adl200_Provided_strategy = st.builds(
    adl200_Provided,
)
adl200_Required_strategy = st.builds(
    adl200_Required,
)
adl200_Component_strategy = st.builds(
    adl200_Component,
    name=
        safe_text
)
adl200_Content_strategy = st.builds(
    adl200_Content,
    expression=
        safe_text,
    language=
        safe_text
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl200_Interface_strategy)
@settings(max_examples=50)
def test_adl200_interface_instantiation(instance):
    assert isinstance(instance, adl200_Interface)



@given(instance=adl200_Interface_strategy)
def test_adl200_interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=adl200_Interface_strategy)
def test_adl200_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl200_Provided_strategy)
@settings(max_examples=50)
def test_adl200_provided_instantiation(instance):
    assert isinstance(instance, adl200_Provided)

@given(instance=adl200_Required_strategy)
@settings(max_examples=50)
def test_adl200_required_instantiation(instance):
    assert isinstance(instance, adl200_Required)

@given(instance=adl200_Component_strategy)
@settings(max_examples=50)
def test_adl200_component_instantiation(instance):
    assert isinstance(instance, adl200_Component)



@given(instance=adl200_Component_strategy)
def test_adl200_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl200_Content_strategy)
@settings(max_examples=50)
def test_adl200_content_instantiation(instance):
    assert isinstance(instance, adl200_Content)



@given(instance=adl200_Content_strategy)
def test_adl200_content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=adl200_Content_strategy)
def test_adl200_content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

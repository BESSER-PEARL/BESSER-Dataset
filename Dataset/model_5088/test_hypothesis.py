import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Interface,
    adl101_Required,
    adl101_Component,
    adl101_Content,
    adl101_Binding,
    adl101_Interface,
    adl101_Provided,
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



def test_adl101_required_is_not_abstract():
    assert not inspect.isabstract(adl101_Required)


def test_adl101_required_constructor_exists():
    assert callable(adl101_Required.__init__)


def test_adl101_required_constructor_args():
    sig = inspect.signature(adl101_Required.__init__)
    params = list(sig.parameters.keys())



def test_adl101_component_is_not_abstract():
    assert not inspect.isabstract(adl101_Component)


def test_adl101_component_constructor_exists():
    assert callable(adl101_Component.__init__)


def test_adl101_component_constructor_args():
    sig = inspect.signature(adl101_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl101_component_has_name():
    assert hasattr(adl101_Component, "name")
    descriptor = None
    for klass in adl101_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl101_content_is_not_abstract():
    assert not inspect.isabstract(adl101_Content)


def test_adl101_content_constructor_exists():
    assert callable(adl101_Content.__init__)


def test_adl101_content_constructor_args():
    sig = inspect.signature(adl101_Content.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_adl101_content_has_language():
    assert hasattr(adl101_Content, "language")
    descriptor = None
    for klass in adl101_Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_adl101_content_has_expression():
    assert hasattr(adl101_Content, "expression")
    descriptor = None
    for klass in adl101_Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_adl101_binding_is_not_abstract():
    assert not inspect.isabstract(adl101_Binding)


def test_adl101_binding_constructor_exists():
    assert callable(adl101_Binding.__init__)


def test_adl101_binding_constructor_args():
    sig = inspect.signature(adl101_Binding.__init__)
    params = list(sig.parameters.keys())



def test_adl101_interface_is_not_abstract():
    assert not inspect.isabstract(adl101_Interface)


def test_adl101_interface_constructor_exists():
    assert callable(adl101_Interface.__init__)


def test_adl101_interface_constructor_args():
    sig = inspect.signature(adl101_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl101_interface_has_name():
    assert hasattr(adl101_Interface, "name")
    descriptor = None
    for klass in adl101_Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adl101_interface_has_signature():
    assert hasattr(adl101_Interface, "signature")
    descriptor = None
    for klass in adl101_Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl101_provided_is_not_abstract():
    assert not inspect.isabstract(adl101_Provided)


def test_adl101_provided_constructor_exists():
    assert callable(adl101_Provided.__init__)


def test_adl101_provided_constructor_args():
    sig = inspect.signature(adl101_Provided.__init__)
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
adl101_Required_strategy = st.builds(
    adl101_Required,
)
adl101_Component_strategy = st.builds(
    adl101_Component,
    name=
        safe_text
)
adl101_Content_strategy = st.builds(
    adl101_Content,
    language=
        safe_text,
    expression=
        safe_text
)
adl101_Binding_strategy = st.builds(
    adl101_Binding,
)
adl101_Interface_strategy = st.builds(
    adl101_Interface,
    name=
        safe_text,
    signature=
        safe_text
)
adl101_Provided_strategy = st.builds(
    adl101_Provided,
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl101_Required_strategy)
@settings(max_examples=50)
def test_adl101_required_instantiation(instance):
    assert isinstance(instance, adl101_Required)

@given(instance=adl101_Component_strategy)
@settings(max_examples=50)
def test_adl101_component_instantiation(instance):
    assert isinstance(instance, adl101_Component)



@given(instance=adl101_Component_strategy)
def test_adl101_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl101_Content_strategy)
@settings(max_examples=50)
def test_adl101_content_instantiation(instance):
    assert isinstance(instance, adl101_Content)



@given(instance=adl101_Content_strategy)
def test_adl101_content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=adl101_Content_strategy)
def test_adl101_content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=adl101_Binding_strategy)
@settings(max_examples=50)
def test_adl101_binding_instantiation(instance):
    assert isinstance(instance, adl101_Binding)

@given(instance=adl101_Interface_strategy)
@settings(max_examples=50)
def test_adl101_interface_instantiation(instance):
    assert isinstance(instance, adl101_Interface)



@given(instance=adl101_Interface_strategy)
def test_adl101_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=adl101_Interface_strategy)
def test_adl101_interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl101_Provided_strategy)
@settings(max_examples=50)
def test_adl101_provided_instantiation(instance):
    assert isinstance(instance, adl101_Provided)

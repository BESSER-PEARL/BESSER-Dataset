import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    adl401_Binding,
    Interface,
    adl401_Provided,
    adl401_Required,
    adl401_EClass0,
    adl401_Component,
    adl401_Content,
    adl401_Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adl401_binding_is_not_abstract():
    assert not inspect.isabstract(adl401_Binding)


def test_adl401_binding_constructor_exists():
    assert callable(adl401_Binding.__init__)


def test_adl401_binding_constructor_args():
    sig = inspect.signature(adl401_Binding.__init__)
    params = list(sig.parameters.keys())



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_adl401_provided_is_not_abstract():
    assert not inspect.isabstract(adl401_Provided)


def test_adl401_provided_constructor_exists():
    assert callable(adl401_Provided.__init__)


def test_adl401_provided_constructor_args():
    sig = inspect.signature(adl401_Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl401_required_is_not_abstract():
    assert not inspect.isabstract(adl401_Required)


def test_adl401_required_constructor_exists():
    assert callable(adl401_Required.__init__)


def test_adl401_required_constructor_args():
    sig = inspect.signature(adl401_Required.__init__)
    params = list(sig.parameters.keys())



def test_adl401_eclass0_is_not_abstract():
    assert not inspect.isabstract(adl401_EClass0)


def test_adl401_eclass0_constructor_exists():
    assert callable(adl401_EClass0.__init__)


def test_adl401_eclass0_constructor_args():
    sig = inspect.signature(adl401_EClass0.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"

def test_adl401_eclass0_has_EAttribute0():
    assert hasattr(adl401_EClass0, "EAttribute0")
    descriptor = None
    for klass in adl401_EClass0.__mro__:
        if "EAttribute0" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute0"]
            break
    assert isinstance(descriptor, property)



def test_adl401_component_is_not_abstract():
    assert not inspect.isabstract(adl401_Component)


def test_adl401_component_constructor_exists():
    assert callable(adl401_Component.__init__)


def test_adl401_component_constructor_args():
    sig = inspect.signature(adl401_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl401_component_has_name():
    assert hasattr(adl401_Component, "name")
    descriptor = None
    for klass in adl401_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl401_content_is_not_abstract():
    assert not inspect.isabstract(adl401_Content)


def test_adl401_content_constructor_exists():
    assert callable(adl401_Content.__init__)


def test_adl401_content_constructor_args():
    sig = inspect.signature(adl401_Content.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_adl401_content_has_language():
    assert hasattr(adl401_Content, "language")
    descriptor = None
    for klass in adl401_Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_adl401_content_has_expression():
    assert hasattr(adl401_Content, "expression")
    descriptor = None
    for klass in adl401_Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_adl401_interface_is_not_abstract():
    assert not inspect.isabstract(adl401_Interface)


def test_adl401_interface_constructor_exists():
    assert callable(adl401_Interface.__init__)


def test_adl401_interface_constructor_args():
    sig = inspect.signature(adl401_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl401_interface_has_signature():
    assert hasattr(adl401_Interface, "signature")
    descriptor = None
    for klass in adl401_Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adl401_interface_has_name():
    assert hasattr(adl401_Interface, "name")
    descriptor = None
    for klass in adl401_Interface.__mro__:
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
adl401_Binding_strategy = st.builds(
    adl401_Binding,
)
Interface_strategy = st.builds(
    Interface,
)
adl401_Provided_strategy = st.builds(
    adl401_Provided,
)
adl401_Required_strategy = st.builds(
    adl401_Required,
)
adl401_EClass0_strategy = st.builds(
    adl401_EClass0,
    EAttribute0=
        safe_text
)
adl401_Component_strategy = st.builds(
    adl401_Component,
    name=
        safe_text
)
adl401_Content_strategy = st.builds(
    adl401_Content,
    language=
        safe_text,
    expression=
        safe_text
)
adl401_Interface_strategy = st.builds(
    adl401_Interface,
    signature=
        safe_text,
    name=
        safe_text
)

@given(instance=adl401_Binding_strategy)
@settings(max_examples=50)
def test_adl401_binding_instantiation(instance):
    assert isinstance(instance, adl401_Binding)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl401_Provided_strategy)
@settings(max_examples=50)
def test_adl401_provided_instantiation(instance):
    assert isinstance(instance, adl401_Provided)

@given(instance=adl401_Required_strategy)
@settings(max_examples=50)
def test_adl401_required_instantiation(instance):
    assert isinstance(instance, adl401_Required)

@given(instance=adl401_EClass0_strategy)
@settings(max_examples=50)
def test_adl401_eclass0_instantiation(instance):
    assert isinstance(instance, adl401_EClass0)



@given(instance=adl401_EClass0_strategy)
def test_adl401_eclass0_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original

@given(instance=adl401_Component_strategy)
@settings(max_examples=50)
def test_adl401_component_instantiation(instance):
    assert isinstance(instance, adl401_Component)



@given(instance=adl401_Component_strategy)
def test_adl401_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl401_Content_strategy)
@settings(max_examples=50)
def test_adl401_content_instantiation(instance):
    assert isinstance(instance, adl401_Content)



@given(instance=adl401_Content_strategy)
def test_adl401_content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=adl401_Content_strategy)
def test_adl401_content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=adl401_Interface_strategy)
@settings(max_examples=50)
def test_adl401_interface_instantiation(instance):
    assert isinstance(instance, adl401_Interface)



@given(instance=adl401_Interface_strategy)
def test_adl401_interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=adl401_Interface_strategy)
def test_adl401_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

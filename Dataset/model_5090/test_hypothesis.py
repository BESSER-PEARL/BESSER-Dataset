import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Binding,
    adl402_EClass2,
    adl402_EClass1,
    adl402_Content,
    Interface,
    adl402_Provided,
    adl402_Required,
    adl402_EClass0,
    adl402_Component,
    adl402_Binding,
    adl402_Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binding_is_not_abstract():
    assert not inspect.isabstract(Binding)


def test_binding_constructor_exists():
    assert callable(Binding.__init__)


def test_binding_constructor_args():
    sig = inspect.signature(Binding.__init__)
    params = list(sig.parameters.keys())



def test_adl402_eclass2_is_not_abstract():
    assert not inspect.isabstract(adl402_EClass2)


def test_adl402_eclass2_constructor_exists():
    assert callable(adl402_EClass2.__init__)


def test_adl402_eclass2_constructor_args():
    sig = inspect.signature(adl402_EClass2.__init__)
    params = list(sig.parameters.keys())



def test_adl402_eclass1_is_not_abstract():
    assert not inspect.isabstract(adl402_EClass1)


def test_adl402_eclass1_constructor_exists():
    assert callable(adl402_EClass1.__init__)


def test_adl402_eclass1_constructor_args():
    sig = inspect.signature(adl402_EClass1.__init__)
    params = list(sig.parameters.keys())



def test_adl402_content_is_not_abstract():
    assert not inspect.isabstract(adl402_Content)


def test_adl402_content_constructor_exists():
    assert callable(adl402_Content.__init__)


def test_adl402_content_constructor_args():
    sig = inspect.signature(adl402_Content.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "language" in params, "Missing parameter 'language'"

def test_adl402_content_has_expression():
    assert hasattr(adl402_Content, "expression")
    descriptor = None
    for klass in adl402_Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_adl402_content_has_language():
    assert hasattr(adl402_Content, "language")
    descriptor = None
    for klass in adl402_Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_adl402_provided_is_not_abstract():
    assert not inspect.isabstract(adl402_Provided)


def test_adl402_provided_constructor_exists():
    assert callable(adl402_Provided.__init__)


def test_adl402_provided_constructor_args():
    sig = inspect.signature(adl402_Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl402_required_is_not_abstract():
    assert not inspect.isabstract(adl402_Required)


def test_adl402_required_constructor_exists():
    assert callable(adl402_Required.__init__)


def test_adl402_required_constructor_args():
    sig = inspect.signature(adl402_Required.__init__)
    params = list(sig.parameters.keys())



def test_adl402_eclass0_is_not_abstract():
    assert not inspect.isabstract(adl402_EClass0)


def test_adl402_eclass0_constructor_exists():
    assert callable(adl402_EClass0.__init__)


def test_adl402_eclass0_constructor_args():
    sig = inspect.signature(adl402_EClass0.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"

def test_adl402_eclass0_has_EAttribute0():
    assert hasattr(adl402_EClass0, "EAttribute0")
    descriptor = None
    for klass in adl402_EClass0.__mro__:
        if "EAttribute0" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute0"]
            break
    assert isinstance(descriptor, property)



def test_adl402_component_is_not_abstract():
    assert not inspect.isabstract(adl402_Component)


def test_adl402_component_constructor_exists():
    assert callable(adl402_Component.__init__)


def test_adl402_component_constructor_args():
    sig = inspect.signature(adl402_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl402_component_has_name():
    assert hasattr(adl402_Component, "name")
    descriptor = None
    for klass in adl402_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl402_binding_is_not_abstract():
    assert not inspect.isabstract(adl402_Binding)


def test_adl402_binding_constructor_exists():
    assert callable(adl402_Binding.__init__)


def test_adl402_binding_constructor_args():
    sig = inspect.signature(adl402_Binding.__init__)
    params = list(sig.parameters.keys())



def test_adl402_interface_is_not_abstract():
    assert not inspect.isabstract(adl402_Interface)


def test_adl402_interface_constructor_exists():
    assert callable(adl402_Interface.__init__)


def test_adl402_interface_constructor_args():
    sig = inspect.signature(adl402_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl402_interface_has_signature():
    assert hasattr(adl402_Interface, "signature")
    descriptor = None
    for klass in adl402_Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adl402_interface_has_name():
    assert hasattr(adl402_Interface, "name")
    descriptor = None
    for klass in adl402_Interface.__mro__:
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
Binding_strategy = st.builds(
    Binding,
)
adl402_EClass2_strategy = st.builds(
    adl402_EClass2,
)
adl402_EClass1_strategy = st.builds(
    adl402_EClass1,
)
adl402_Content_strategy = st.builds(
    adl402_Content,
    expression=
        safe_text,
    language=
        safe_text
)
Interface_strategy = st.builds(
    Interface,
)
adl402_Provided_strategy = st.builds(
    adl402_Provided,
)
adl402_Required_strategy = st.builds(
    adl402_Required,
)
adl402_EClass0_strategy = st.builds(
    adl402_EClass0,
    EAttribute0=
        safe_text
)
adl402_Component_strategy = st.builds(
    adl402_Component,
    name=
        safe_text
)
adl402_Binding_strategy = st.builds(
    adl402_Binding,
)
adl402_Interface_strategy = st.builds(
    adl402_Interface,
    signature=
        safe_text,
    name=
        safe_text
)

@given(instance=Binding_strategy)
@settings(max_examples=50)
def test_binding_instantiation(instance):
    assert isinstance(instance, Binding)

@given(instance=adl402_EClass2_strategy)
@settings(max_examples=50)
def test_adl402_eclass2_instantiation(instance):
    assert isinstance(instance, adl402_EClass2)

@given(instance=adl402_EClass1_strategy)
@settings(max_examples=50)
def test_adl402_eclass1_instantiation(instance):
    assert isinstance(instance, adl402_EClass1)

@given(instance=adl402_Content_strategy)
@settings(max_examples=50)
def test_adl402_content_instantiation(instance):
    assert isinstance(instance, adl402_Content)



@given(instance=adl402_Content_strategy)
def test_adl402_content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=adl402_Content_strategy)
def test_adl402_content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl402_Provided_strategy)
@settings(max_examples=50)
def test_adl402_provided_instantiation(instance):
    assert isinstance(instance, adl402_Provided)

@given(instance=adl402_Required_strategy)
@settings(max_examples=50)
def test_adl402_required_instantiation(instance):
    assert isinstance(instance, adl402_Required)

@given(instance=adl402_EClass0_strategy)
@settings(max_examples=50)
def test_adl402_eclass0_instantiation(instance):
    assert isinstance(instance, adl402_EClass0)



@given(instance=adl402_EClass0_strategy)
def test_adl402_eclass0_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original

@given(instance=adl402_Component_strategy)
@settings(max_examples=50)
def test_adl402_component_instantiation(instance):
    assert isinstance(instance, adl402_Component)



@given(instance=adl402_Component_strategy)
def test_adl402_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl402_Binding_strategy)
@settings(max_examples=50)
def test_adl402_binding_instantiation(instance):
    assert isinstance(instance, adl402_Binding)

@given(instance=adl402_Interface_strategy)
@settings(max_examples=50)
def test_adl402_interface_instantiation(instance):
    assert isinstance(instance, adl402_Interface)



@given(instance=adl402_Interface_strategy)
def test_adl402_interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=adl402_Interface_strategy)
def test_adl402_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

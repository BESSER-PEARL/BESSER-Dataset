import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Binding,
    adl402::EClass2,
    adl402::EClass1,
    adl402::Content,
    Interface,
    adl402::Provided,
    adl402::Required,
    adl402::EClass0,
    adl402::Component,
    adl402::Binding,
    adl402::Interface,
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



def test_adl402::eclass2_is_not_abstract():
    assert not inspect.isabstract(adl402::EClass2)


def test_adl402::eclass2_constructor_exists():
    assert callable(adl402::EClass2.__init__)


def test_adl402::eclass2_constructor_args():
    sig = inspect.signature(adl402::EClass2.__init__)
    params = list(sig.parameters.keys())



def test_adl402::eclass1_is_not_abstract():
    assert not inspect.isabstract(adl402::EClass1)


def test_adl402::eclass1_constructor_exists():
    assert callable(adl402::EClass1.__init__)


def test_adl402::eclass1_constructor_args():
    sig = inspect.signature(adl402::EClass1.__init__)
    params = list(sig.parameters.keys())



def test_adl402::content_is_not_abstract():
    assert not inspect.isabstract(adl402::Content)


def test_adl402::content_constructor_exists():
    assert callable(adl402::Content.__init__)


def test_adl402::content_constructor_args():
    sig = inspect.signature(adl402::Content.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_adl402::content_has_language():
    assert hasattr(adl402::Content, "language")
    descriptor = None
    for klass in adl402::Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_adl402::content_has_expression():
    assert hasattr(adl402::Content, "expression")
    descriptor = None
    for klass in adl402::Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_adl402::provided_is_not_abstract():
    assert not inspect.isabstract(adl402::Provided)


def test_adl402::provided_constructor_exists():
    assert callable(adl402::Provided.__init__)


def test_adl402::provided_constructor_args():
    sig = inspect.signature(adl402::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl402::required_is_not_abstract():
    assert not inspect.isabstract(adl402::Required)


def test_adl402::required_constructor_exists():
    assert callable(adl402::Required.__init__)


def test_adl402::required_constructor_args():
    sig = inspect.signature(adl402::Required.__init__)
    params = list(sig.parameters.keys())



def test_adl402::eclass0_is_not_abstract():
    assert not inspect.isabstract(adl402::EClass0)


def test_adl402::eclass0_constructor_exists():
    assert callable(adl402::EClass0.__init__)


def test_adl402::eclass0_constructor_args():
    sig = inspect.signature(adl402::EClass0.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"

def test_adl402::eclass0_has_EAttribute0():
    assert hasattr(adl402::EClass0, "EAttribute0")
    descriptor = None
    for klass in adl402::EClass0.__mro__:
        if "EAttribute0" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute0"]
            break
    assert isinstance(descriptor, property)



def test_adl402::component_is_not_abstract():
    assert not inspect.isabstract(adl402::Component)


def test_adl402::component_constructor_exists():
    assert callable(adl402::Component.__init__)


def test_adl402::component_constructor_args():
    sig = inspect.signature(adl402::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl402::component_has_name():
    assert hasattr(adl402::Component, "name")
    descriptor = None
    for klass in adl402::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl402::binding_is_not_abstract():
    assert not inspect.isabstract(adl402::Binding)


def test_adl402::binding_constructor_exists():
    assert callable(adl402::Binding.__init__)


def test_adl402::binding_constructor_args():
    sig = inspect.signature(adl402::Binding.__init__)
    params = list(sig.parameters.keys())



def test_adl402::interface_is_not_abstract():
    assert not inspect.isabstract(adl402::Interface)


def test_adl402::interface_constructor_exists():
    assert callable(adl402::Interface.__init__)


def test_adl402::interface_constructor_args():
    sig = inspect.signature(adl402::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl402::interface_has_signature():
    assert hasattr(adl402::Interface, "signature")
    descriptor = None
    for klass in adl402::Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adl402::interface_has_name():
    assert hasattr(adl402::Interface, "name")
    descriptor = None
    for klass in adl402::Interface.__mro__:
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
adl402::EClass2_strategy = st.builds(
    adl402::EClass2,
)
adl402::EClass1_strategy = st.builds(
    adl402::EClass1,
)
adl402::Content_strategy = st.builds(
    adl402::Content,
    language=
        safe_text,
    expression=
        safe_text
)
Interface_strategy = st.builds(
    Interface,
)
adl402::Provided_strategy = st.builds(
    adl402::Provided,
)
adl402::Required_strategy = st.builds(
    adl402::Required,
)
adl402::EClass0_strategy = st.builds(
    adl402::EClass0,
    EAttribute0=
        safe_text
)
adl402::Component_strategy = st.builds(
    adl402::Component,
    name=
        safe_text
)
adl402::Binding_strategy = st.builds(
    adl402::Binding,
)
adl402::Interface_strategy = st.builds(
    adl402::Interface,
    signature=
        safe_text,
    name=
        safe_text
)

@given(instance=Binding_strategy)
@settings(max_examples=50)
def test_binding_instantiation(instance):
    assert isinstance(instance, Binding)

@given(instance=adl402::EClass2_strategy)
@settings(max_examples=50)
def test_adl402::eclass2_instantiation(instance):
    assert isinstance(instance, adl402::EClass2)

@given(instance=adl402::EClass1_strategy)
@settings(max_examples=50)
def test_adl402::eclass1_instantiation(instance):
    assert isinstance(instance, adl402::EClass1)

@given(instance=adl402::Content_strategy)
@settings(max_examples=50)
def test_adl402::content_instantiation(instance):
    assert isinstance(instance, adl402::Content)

@given(instance=adl402::Content_strategy)
def test_adl402::content_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=adl402::Content_strategy)
def test_adl402::content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=adl402::Content_strategy)
def test_adl402::content_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=adl402::Content_strategy)
def test_adl402::content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl402::Provided_strategy)
@settings(max_examples=50)
def test_adl402::provided_instantiation(instance):
    assert isinstance(instance, adl402::Provided)

@given(instance=adl402::Required_strategy)
@settings(max_examples=50)
def test_adl402::required_instantiation(instance):
    assert isinstance(instance, adl402::Required)

@given(instance=adl402::EClass0_strategy)
@settings(max_examples=50)
def test_adl402::eclass0_instantiation(instance):
    assert isinstance(instance, adl402::EClass0)

@given(instance=adl402::EClass0_strategy)
def test_adl402::eclass0_EAttribute0_type(instance):
    assert isinstance(instance.EAttribute0, str)


@given(instance=adl402::EClass0_strategy)
def test_adl402::eclass0_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original

@given(instance=adl402::Component_strategy)
@settings(max_examples=50)
def test_adl402::component_instantiation(instance):
    assert isinstance(instance, adl402::Component)

@given(instance=adl402::Component_strategy)
def test_adl402::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl402::Component_strategy)
def test_adl402::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl402::Binding_strategy)
@settings(max_examples=50)
def test_adl402::binding_instantiation(instance):
    assert isinstance(instance, adl402::Binding)

@given(instance=adl402::Interface_strategy)
@settings(max_examples=50)
def test_adl402::interface_instantiation(instance):
    assert isinstance(instance, adl402::Interface)

@given(instance=adl402::Interface_strategy)
def test_adl402::interface_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adl402::Interface_strategy)
def test_adl402::interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl402::Interface_strategy)
def test_adl402::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl402::Interface_strategy)
def test_adl402::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

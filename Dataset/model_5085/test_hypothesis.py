import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractComponent,
    adl199::AtomicComponent,
    adl199::Component,
    Interface,
    adl199::Binding,
    adl199::Interface,
    adl199::Delegation,
    adl199::Provided,
    adl199::Required,
    adl199::Content,
    adl199::AbstractComponent,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(AbstractComponent)


def test_abstractcomponent_constructor_exists():
    assert callable(AbstractComponent.__init__)


def test_abstractcomponent_constructor_args():
    sig = inspect.signature(AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_adl199::atomiccomponent_is_not_abstract():
    assert not inspect.isabstract(adl199::AtomicComponent)


def test_adl199::atomiccomponent_constructor_exists():
    assert callable(adl199::AtomicComponent.__init__)


def test_adl199::atomiccomponent_constructor_args():
    sig = inspect.signature(adl199::AtomicComponent.__init__)
    params = list(sig.parameters.keys())



def test_adl199::component_is_not_abstract():
    assert not inspect.isabstract(adl199::Component)


def test_adl199::component_constructor_exists():
    assert callable(adl199::Component.__init__)


def test_adl199::component_constructor_args():
    sig = inspect.signature(adl199::Component.__init__)
    params = list(sig.parameters.keys())



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_adl199::binding_is_not_abstract():
    assert not inspect.isabstract(adl199::Binding)


def test_adl199::binding_constructor_exists():
    assert callable(adl199::Binding.__init__)


def test_adl199::binding_constructor_args():
    sig = inspect.signature(adl199::Binding.__init__)
    params = list(sig.parameters.keys())



def test_adl199::interface_is_not_abstract():
    assert not inspect.isabstract(adl199::Interface)


def test_adl199::interface_constructor_exists():
    assert callable(adl199::Interface.__init__)


def test_adl199::interface_constructor_args():
    sig = inspect.signature(adl199::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl199::interface_has_name():
    assert hasattr(adl199::Interface, "name")
    descriptor = None
    for klass in adl199::Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adl199::interface_has_signature():
    assert hasattr(adl199::Interface, "signature")
    descriptor = None
    for klass in adl199::Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl199::delegation_is_not_abstract():
    assert not inspect.isabstract(adl199::Delegation)


def test_adl199::delegation_constructor_exists():
    assert callable(adl199::Delegation.__init__)


def test_adl199::delegation_constructor_args():
    sig = inspect.signature(adl199::Delegation.__init__)
    params = list(sig.parameters.keys())



def test_adl199::provided_is_not_abstract():
    assert not inspect.isabstract(adl199::Provided)


def test_adl199::provided_constructor_exists():
    assert callable(adl199::Provided.__init__)


def test_adl199::provided_constructor_args():
    sig = inspect.signature(adl199::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl199::required_is_not_abstract():
    assert not inspect.isabstract(adl199::Required)


def test_adl199::required_constructor_exists():
    assert callable(adl199::Required.__init__)


def test_adl199::required_constructor_args():
    sig = inspect.signature(adl199::Required.__init__)
    params = list(sig.parameters.keys())



def test_adl199::content_is_not_abstract():
    assert not inspect.isabstract(adl199::Content)


def test_adl199::content_constructor_exists():
    assert callable(adl199::Content.__init__)


def test_adl199::content_constructor_args():
    sig = inspect.signature(adl199::Content.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "language" in params, "Missing parameter 'language'"

def test_adl199::content_has_expression():
    assert hasattr(adl199::Content, "expression")
    descriptor = None
    for klass in adl199::Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_adl199::content_has_language():
    assert hasattr(adl199::Content, "language")
    descriptor = None
    for klass in adl199::Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_adl199::abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(adl199::AbstractComponent)


def test_adl199::abstractcomponent_constructor_exists():
    assert callable(adl199::AbstractComponent.__init__)


def test_adl199::abstractcomponent_constructor_args():
    sig = inspect.signature(adl199::AbstractComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl199::abstractcomponent_has_name():
    assert hasattr(adl199::AbstractComponent, "name")
    descriptor = None
    for klass in adl199::AbstractComponent.__mro__:
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
AbstractComponent_strategy = st.builds(
    AbstractComponent,
)
adl199::AtomicComponent_strategy = st.builds(
    adl199::AtomicComponent,
)
adl199::Component_strategy = st.builds(
    adl199::Component,
)
Interface_strategy = st.builds(
    Interface,
)
adl199::Binding_strategy = st.builds(
    adl199::Binding,
)
adl199::Interface_strategy = st.builds(
    adl199::Interface,
    name=
        safe_text,
    signature=
        safe_text
)
adl199::Delegation_strategy = st.builds(
    adl199::Delegation,
)
adl199::Provided_strategy = st.builds(
    adl199::Provided,
)
adl199::Required_strategy = st.builds(
    adl199::Required,
)
adl199::Content_strategy = st.builds(
    adl199::Content,
    expression=
        safe_text,
    language=
        safe_text
)
adl199::AbstractComponent_strategy = st.builds(
    adl199::AbstractComponent,
    name=
        safe_text
)

@given(instance=AbstractComponent_strategy)
@settings(max_examples=50)
def test_abstractcomponent_instantiation(instance):
    assert isinstance(instance, AbstractComponent)

@given(instance=adl199::AtomicComponent_strategy)
@settings(max_examples=50)
def test_adl199::atomiccomponent_instantiation(instance):
    assert isinstance(instance, adl199::AtomicComponent)

@given(instance=adl199::Component_strategy)
@settings(max_examples=50)
def test_adl199::component_instantiation(instance):
    assert isinstance(instance, adl199::Component)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl199::Binding_strategy)
@settings(max_examples=50)
def test_adl199::binding_instantiation(instance):
    assert isinstance(instance, adl199::Binding)

@given(instance=adl199::Interface_strategy)
@settings(max_examples=50)
def test_adl199::interface_instantiation(instance):
    assert isinstance(instance, adl199::Interface)

@given(instance=adl199::Interface_strategy)
def test_adl199::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl199::Interface_strategy)
def test_adl199::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl199::Interface_strategy)
def test_adl199::interface_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adl199::Interface_strategy)
def test_adl199::interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl199::Delegation_strategy)
@settings(max_examples=50)
def test_adl199::delegation_instantiation(instance):
    assert isinstance(instance, adl199::Delegation)

@given(instance=adl199::Provided_strategy)
@settings(max_examples=50)
def test_adl199::provided_instantiation(instance):
    assert isinstance(instance, adl199::Provided)

@given(instance=adl199::Required_strategy)
@settings(max_examples=50)
def test_adl199::required_instantiation(instance):
    assert isinstance(instance, adl199::Required)

@given(instance=adl199::Content_strategy)
@settings(max_examples=50)
def test_adl199::content_instantiation(instance):
    assert isinstance(instance, adl199::Content)

@given(instance=adl199::Content_strategy)
def test_adl199::content_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=adl199::Content_strategy)
def test_adl199::content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=adl199::Content_strategy)
def test_adl199::content_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=adl199::Content_strategy)
def test_adl199::content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=adl199::AbstractComponent_strategy)
@settings(max_examples=50)
def test_adl199::abstractcomponent_instantiation(instance):
    assert isinstance(instance, adl199::AbstractComponent)

@given(instance=adl199::AbstractComponent_strategy)
def test_adl199::abstractcomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl199::AbstractComponent_strategy)
def test_adl199::abstractcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

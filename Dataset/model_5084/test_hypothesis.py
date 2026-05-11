import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Interface,
    AbstractComponent,
    adlold::Component,
    adlold::Binding,
    adlold::Interface,
    adlold::Provided,
    adlold::Required,
    adlold::Content,
    adlold::AbstractComponent,
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



def test_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(AbstractComponent)


def test_abstractcomponent_constructor_exists():
    assert callable(AbstractComponent.__init__)


def test_abstractcomponent_constructor_args():
    sig = inspect.signature(AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_adlold::component_is_not_abstract():
    assert not inspect.isabstract(adlold::Component)


def test_adlold::component_constructor_exists():
    assert callable(adlold::Component.__init__)


def test_adlold::component_constructor_args():
    sig = inspect.signature(adlold::Component.__init__)
    params = list(sig.parameters.keys())



def test_adlold::binding_is_not_abstract():
    assert not inspect.isabstract(adlold::Binding)


def test_adlold::binding_constructor_exists():
    assert callable(adlold::Binding.__init__)


def test_adlold::binding_constructor_args():
    sig = inspect.signature(adlold::Binding.__init__)
    params = list(sig.parameters.keys())



def test_adlold::interface_is_not_abstract():
    assert not inspect.isabstract(adlold::Interface)


def test_adlold::interface_constructor_exists():
    assert callable(adlold::Interface.__init__)


def test_adlold::interface_constructor_args():
    sig = inspect.signature(adlold::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_adlold::interface_has_name():
    assert hasattr(adlold::Interface, "name")
    descriptor = None
    for klass in adlold::Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adlold::interface_has_signature():
    assert hasattr(adlold::Interface, "signature")
    descriptor = None
    for klass in adlold::Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adlold::provided_is_not_abstract():
    assert not inspect.isabstract(adlold::Provided)


def test_adlold::provided_constructor_exists():
    assert callable(adlold::Provided.__init__)


def test_adlold::provided_constructor_args():
    sig = inspect.signature(adlold::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adlold::required_is_not_abstract():
    assert not inspect.isabstract(adlold::Required)


def test_adlold::required_constructor_exists():
    assert callable(adlold::Required.__init__)


def test_adlold::required_constructor_args():
    sig = inspect.signature(adlold::Required.__init__)
    params = list(sig.parameters.keys())



def test_adlold::content_is_not_abstract():
    assert not inspect.isabstract(adlold::Content)


def test_adlold::content_constructor_exists():
    assert callable(adlold::Content.__init__)


def test_adlold::content_constructor_args():
    sig = inspect.signature(adlold::Content.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_adlold::content_has_language():
    assert hasattr(adlold::Content, "language")
    descriptor = None
    for klass in adlold::Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_adlold::content_has_expression():
    assert hasattr(adlold::Content, "expression")
    descriptor = None
    for klass in adlold::Content.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_adlold::abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(adlold::AbstractComponent)


def test_adlold::abstractcomponent_constructor_exists():
    assert callable(adlold::AbstractComponent.__init__)


def test_adlold::abstractcomponent_constructor_args():
    sig = inspect.signature(adlold::AbstractComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adlold::abstractcomponent_has_name():
    assert hasattr(adlold::AbstractComponent, "name")
    descriptor = None
    for klass in adlold::AbstractComponent.__mro__:
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
AbstractComponent_strategy = st.builds(
    AbstractComponent,
)
adlold::Component_strategy = st.builds(
    adlold::Component,
)
adlold::Binding_strategy = st.builds(
    adlold::Binding,
)
adlold::Interface_strategy = st.builds(
    adlold::Interface,
    name=
        safe_text,
    signature=
        safe_text
)
adlold::Provided_strategy = st.builds(
    adlold::Provided,
)
adlold::Required_strategy = st.builds(
    adlold::Required,
)
adlold::Content_strategy = st.builds(
    adlold::Content,
    language=
        safe_text,
    expression=
        safe_text
)
adlold::AbstractComponent_strategy = st.builds(
    adlold::AbstractComponent,
    name=
        safe_text
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=AbstractComponent_strategy)
@settings(max_examples=50)
def test_abstractcomponent_instantiation(instance):
    assert isinstance(instance, AbstractComponent)

@given(instance=adlold::Component_strategy)
@settings(max_examples=50)
def test_adlold::component_instantiation(instance):
    assert isinstance(instance, adlold::Component)

@given(instance=adlold::Binding_strategy)
@settings(max_examples=50)
def test_adlold::binding_instantiation(instance):
    assert isinstance(instance, adlold::Binding)

@given(instance=adlold::Interface_strategy)
@settings(max_examples=50)
def test_adlold::interface_instantiation(instance):
    assert isinstance(instance, adlold::Interface)

@given(instance=adlold::Interface_strategy)
def test_adlold::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adlold::Interface_strategy)
def test_adlold::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adlold::Interface_strategy)
def test_adlold::interface_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adlold::Interface_strategy)
def test_adlold::interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adlold::Provided_strategy)
@settings(max_examples=50)
def test_adlold::provided_instantiation(instance):
    assert isinstance(instance, adlold::Provided)

@given(instance=adlold::Required_strategy)
@settings(max_examples=50)
def test_adlold::required_instantiation(instance):
    assert isinstance(instance, adlold::Required)

@given(instance=adlold::Content_strategy)
@settings(max_examples=50)
def test_adlold::content_instantiation(instance):
    assert isinstance(instance, adlold::Content)

@given(instance=adlold::Content_strategy)
def test_adlold::content_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=adlold::Content_strategy)
def test_adlold::content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=adlold::Content_strategy)
def test_adlold::content_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=adlold::Content_strategy)
def test_adlold::content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=adlold::AbstractComponent_strategy)
@settings(max_examples=50)
def test_adlold::abstractcomponent_instantiation(instance):
    assert isinstance(instance, adlold::AbstractComponent)

@given(instance=adlold::AbstractComponent_strategy)
def test_adlold::abstractcomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adlold::AbstractComponent_strategy)
def test_adlold::abstractcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

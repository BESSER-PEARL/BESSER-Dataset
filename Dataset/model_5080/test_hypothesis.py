import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    adlrecur::Binding,
    Component,
    adlrecur::Base,
    Interface,
    adlrecur::Component,
    adlrecur::Interface,
    adlrecur::Provided,
    adlrecur::Required,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adlrecur::binding_is_not_abstract():
    assert not inspect.isabstract(adlrecur::Binding)


def test_adlrecur::binding_constructor_exists():
    assert callable(adlrecur::Binding.__init__)


def test_adlrecur::binding_constructor_args():
    sig = inspect.signature(adlrecur::Binding.__init__)
    params = list(sig.parameters.keys())



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_adlrecur::base_is_not_abstract():
    assert not inspect.isabstract(adlrecur::Base)


def test_adlrecur::base_constructor_exists():
    assert callable(adlrecur::Base.__init__)


def test_adlrecur::base_constructor_args():
    sig = inspect.signature(adlrecur::Base.__init__)
    params = list(sig.parameters.keys())



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_adlrecur::component_is_not_abstract():
    assert not inspect.isabstract(adlrecur::Component)


def test_adlrecur::component_constructor_exists():
    assert callable(adlrecur::Component.__init__)


def test_adlrecur::component_constructor_args():
    sig = inspect.signature(adlrecur::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adlrecur::component_has_name():
    assert hasattr(adlrecur::Component, "name")
    descriptor = None
    for klass in adlrecur::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adlrecur::interface_is_not_abstract():
    assert not inspect.isabstract(adlrecur::Interface)


def test_adlrecur::interface_constructor_exists():
    assert callable(adlrecur::Interface.__init__)


def test_adlrecur::interface_constructor_args():
    sig = inspect.signature(adlrecur::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adlrecur::interface_has_signature():
    assert hasattr(adlrecur::Interface, "signature")
    descriptor = None
    for klass in adlrecur::Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adlrecur::interface_has_name():
    assert hasattr(adlrecur::Interface, "name")
    descriptor = None
    for klass in adlrecur::Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adlrecur::provided_is_not_abstract():
    assert not inspect.isabstract(adlrecur::Provided)


def test_adlrecur::provided_constructor_exists():
    assert callable(adlrecur::Provided.__init__)


def test_adlrecur::provided_constructor_args():
    sig = inspect.signature(adlrecur::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adlrecur::required_is_not_abstract():
    assert not inspect.isabstract(adlrecur::Required)


def test_adlrecur::required_constructor_exists():
    assert callable(adlrecur::Required.__init__)


def test_adlrecur::required_constructor_args():
    sig = inspect.signature(adlrecur::Required.__init__)
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
adlrecur::Binding_strategy = st.builds(
    adlrecur::Binding,
)
Component_strategy = st.builds(
    Component,
)
adlrecur::Base_strategy = st.builds(
    adlrecur::Base,
)
Interface_strategy = st.builds(
    Interface,
)
adlrecur::Component_strategy = st.builds(
    adlrecur::Component,
    name=
        safe_text
)
adlrecur::Interface_strategy = st.builds(
    adlrecur::Interface,
    signature=
        safe_text,
    name=
        safe_text
)
adlrecur::Provided_strategy = st.builds(
    adlrecur::Provided,
)
adlrecur::Required_strategy = st.builds(
    adlrecur::Required,
)

@given(instance=adlrecur::Binding_strategy)
@settings(max_examples=50)
def test_adlrecur::binding_instantiation(instance):
    assert isinstance(instance, adlrecur::Binding)

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=adlrecur::Base_strategy)
@settings(max_examples=50)
def test_adlrecur::base_instantiation(instance):
    assert isinstance(instance, adlrecur::Base)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adlrecur::Component_strategy)
@settings(max_examples=50)
def test_adlrecur::component_instantiation(instance):
    assert isinstance(instance, adlrecur::Component)

@given(instance=adlrecur::Component_strategy)
def test_adlrecur::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adlrecur::Component_strategy)
def test_adlrecur::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adlrecur::Interface_strategy)
@settings(max_examples=50)
def test_adlrecur::interface_instantiation(instance):
    assert isinstance(instance, adlrecur::Interface)

@given(instance=adlrecur::Interface_strategy)
def test_adlrecur::interface_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adlrecur::Interface_strategy)
def test_adlrecur::interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adlrecur::Interface_strategy)
def test_adlrecur::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adlrecur::Interface_strategy)
def test_adlrecur::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adlrecur::Provided_strategy)
@settings(max_examples=50)
def test_adlrecur::provided_instantiation(instance):
    assert isinstance(instance, adlrecur::Provided)

@given(instance=adlrecur::Required_strategy)
@settings(max_examples=50)
def test_adlrecur::required_instantiation(instance):
    assert isinstance(instance, adlrecur::Required)

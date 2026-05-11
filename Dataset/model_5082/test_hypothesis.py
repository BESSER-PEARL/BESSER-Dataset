import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    adlsimple::Base,
    adlsimple::Binding,
    adlsimple::Interface,
    adlsimple::Component,
    Interface,
    adlsimple::Provided,
    adlsimple::Required,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adlsimple::base_is_not_abstract():
    assert not inspect.isabstract(adlsimple::Base)


def test_adlsimple::base_constructor_exists():
    assert callable(adlsimple::Base.__init__)


def test_adlsimple::base_constructor_args():
    sig = inspect.signature(adlsimple::Base.__init__)
    params = list(sig.parameters.keys())



def test_adlsimple::binding_is_not_abstract():
    assert not inspect.isabstract(adlsimple::Binding)


def test_adlsimple::binding_constructor_exists():
    assert callable(adlsimple::Binding.__init__)


def test_adlsimple::binding_constructor_args():
    sig = inspect.signature(adlsimple::Binding.__init__)
    params = list(sig.parameters.keys())



def test_adlsimple::interface_is_not_abstract():
    assert not inspect.isabstract(adlsimple::Interface)


def test_adlsimple::interface_constructor_exists():
    assert callable(adlsimple::Interface.__init__)


def test_adlsimple::interface_constructor_args():
    sig = inspect.signature(adlsimple::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adlsimple::interface_has_signature():
    assert hasattr(adlsimple::Interface, "signature")
    descriptor = None
    for klass in adlsimple::Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adlsimple::interface_has_name():
    assert hasattr(adlsimple::Interface, "name")
    descriptor = None
    for klass in adlsimple::Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adlsimple::component_is_not_abstract():
    assert not inspect.isabstract(adlsimple::Component)


def test_adlsimple::component_constructor_exists():
    assert callable(adlsimple::Component.__init__)


def test_adlsimple::component_constructor_args():
    sig = inspect.signature(adlsimple::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adlsimple::component_has_name():
    assert hasattr(adlsimple::Component, "name")
    descriptor = None
    for klass in adlsimple::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_adlsimple::provided_is_not_abstract():
    assert not inspect.isabstract(adlsimple::Provided)


def test_adlsimple::provided_constructor_exists():
    assert callable(adlsimple::Provided.__init__)


def test_adlsimple::provided_constructor_args():
    sig = inspect.signature(adlsimple::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adlsimple::required_is_not_abstract():
    assert not inspect.isabstract(adlsimple::Required)


def test_adlsimple::required_constructor_exists():
    assert callable(adlsimple::Required.__init__)


def test_adlsimple::required_constructor_args():
    sig = inspect.signature(adlsimple::Required.__init__)
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
adlsimple::Base_strategy = st.builds(
    adlsimple::Base,
)
adlsimple::Binding_strategy = st.builds(
    adlsimple::Binding,
)
adlsimple::Interface_strategy = st.builds(
    adlsimple::Interface,
    signature=
        safe_text,
    name=
        safe_text
)
adlsimple::Component_strategy = st.builds(
    adlsimple::Component,
    name=
        safe_text
)
Interface_strategy = st.builds(
    Interface,
)
adlsimple::Provided_strategy = st.builds(
    adlsimple::Provided,
)
adlsimple::Required_strategy = st.builds(
    adlsimple::Required,
)

@given(instance=adlsimple::Base_strategy)
@settings(max_examples=50)
def test_adlsimple::base_instantiation(instance):
    assert isinstance(instance, adlsimple::Base)

@given(instance=adlsimple::Binding_strategy)
@settings(max_examples=50)
def test_adlsimple::binding_instantiation(instance):
    assert isinstance(instance, adlsimple::Binding)

@given(instance=adlsimple::Interface_strategy)
@settings(max_examples=50)
def test_adlsimple::interface_instantiation(instance):
    assert isinstance(instance, adlsimple::Interface)

@given(instance=adlsimple::Interface_strategy)
def test_adlsimple::interface_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adlsimple::Interface_strategy)
def test_adlsimple::interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adlsimple::Interface_strategy)
def test_adlsimple::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adlsimple::Interface_strategy)
def test_adlsimple::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adlsimple::Component_strategy)
@settings(max_examples=50)
def test_adlsimple::component_instantiation(instance):
    assert isinstance(instance, adlsimple::Component)

@given(instance=adlsimple::Component_strategy)
def test_adlsimple::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adlsimple::Component_strategy)
def test_adlsimple::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adlsimple::Provided_strategy)
@settings(max_examples=50)
def test_adlsimple::provided_instantiation(instance):
    assert isinstance(instance, adlsimple::Provided)

@given(instance=adlsimple::Required_strategy)
@settings(max_examples=50)
def test_adlsimple::required_instantiation(instance):
    assert isinstance(instance, adlsimple::Required)

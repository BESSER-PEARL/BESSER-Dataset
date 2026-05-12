import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    adlsimple_Base,
    adlsimple_Binding,
    adlsimple_Interface,
    adlsimple_Component,
    Interface,
    adlsimple_Provided,
    adlsimple_Required,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adlsimple_base_is_not_abstract():
    assert not inspect.isabstract(adlsimple_Base)


def test_adlsimple_base_constructor_exists():
    assert callable(adlsimple_Base.__init__)


def test_adlsimple_base_constructor_args():
    sig = inspect.signature(adlsimple_Base.__init__)
    params = list(sig.parameters.keys())



def test_adlsimple_binding_is_not_abstract():
    assert not inspect.isabstract(adlsimple_Binding)


def test_adlsimple_binding_constructor_exists():
    assert callable(adlsimple_Binding.__init__)


def test_adlsimple_binding_constructor_args():
    sig = inspect.signature(adlsimple_Binding.__init__)
    params = list(sig.parameters.keys())



def test_adlsimple_interface_is_not_abstract():
    assert not inspect.isabstract(adlsimple_Interface)


def test_adlsimple_interface_constructor_exists():
    assert callable(adlsimple_Interface.__init__)


def test_adlsimple_interface_constructor_args():
    sig = inspect.signature(adlsimple_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "name" in params, "Missing parameter 'name'"

def test_adlsimple_interface_has_signature():
    assert hasattr(adlsimple_Interface, "signature")
    descriptor = None
    for klass in adlsimple_Interface.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_adlsimple_interface_has_name():
    assert hasattr(adlsimple_Interface, "name")
    descriptor = None
    for klass in adlsimple_Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adlsimple_component_is_not_abstract():
    assert not inspect.isabstract(adlsimple_Component)


def test_adlsimple_component_constructor_exists():
    assert callable(adlsimple_Component.__init__)


def test_adlsimple_component_constructor_args():
    sig = inspect.signature(adlsimple_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adlsimple_component_has_name():
    assert hasattr(adlsimple_Component, "name")
    descriptor = None
    for klass in adlsimple_Component.__mro__:
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



def test_adlsimple_provided_is_not_abstract():
    assert not inspect.isabstract(adlsimple_Provided)


def test_adlsimple_provided_constructor_exists():
    assert callable(adlsimple_Provided.__init__)


def test_adlsimple_provided_constructor_args():
    sig = inspect.signature(adlsimple_Provided.__init__)
    params = list(sig.parameters.keys())



def test_adlsimple_required_is_not_abstract():
    assert not inspect.isabstract(adlsimple_Required)


def test_adlsimple_required_constructor_exists():
    assert callable(adlsimple_Required.__init__)


def test_adlsimple_required_constructor_args():
    sig = inspect.signature(adlsimple_Required.__init__)
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
adlsimple_Base_strategy = st.builds(
    adlsimple_Base,
)
adlsimple_Binding_strategy = st.builds(
    adlsimple_Binding,
)
adlsimple_Interface_strategy = st.builds(
    adlsimple_Interface,
    signature=
        safe_text,
    name=
        safe_text
)
adlsimple_Component_strategy = st.builds(
    adlsimple_Component,
    name=
        safe_text
)
Interface_strategy = st.builds(
    Interface,
)
adlsimple_Provided_strategy = st.builds(
    adlsimple_Provided,
)
adlsimple_Required_strategy = st.builds(
    adlsimple_Required,
)

@given(instance=adlsimple_Base_strategy)
@settings(max_examples=50)
def test_adlsimple_base_instantiation(instance):
    assert isinstance(instance, adlsimple_Base)

@given(instance=adlsimple_Binding_strategy)
@settings(max_examples=50)
def test_adlsimple_binding_instantiation(instance):
    assert isinstance(instance, adlsimple_Binding)

@given(instance=adlsimple_Interface_strategy)
@settings(max_examples=50)
def test_adlsimple_interface_instantiation(instance):
    assert isinstance(instance, adlsimple_Interface)



@given(instance=adlsimple_Interface_strategy)
def test_adlsimple_interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=adlsimple_Interface_strategy)
def test_adlsimple_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adlsimple_Component_strategy)
@settings(max_examples=50)
def test_adlsimple_component_instantiation(instance):
    assert isinstance(instance, adlsimple_Component)



@given(instance=adlsimple_Component_strategy)
def test_adlsimple_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adlsimple_Provided_strategy)
@settings(max_examples=50)
def test_adlsimple_provided_instantiation(instance):
    assert isinstance(instance, adlsimple_Provided)

@given(instance=adlsimple_Required_strategy)
@settings(max_examples=50)
def test_adlsimple_required_instantiation(instance):
    assert isinstance(instance, adlsimple_Required)

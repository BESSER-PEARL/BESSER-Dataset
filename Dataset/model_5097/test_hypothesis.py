import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Interface,
    adl_Type,
    adl_NamedElement,
    NamedElement,
    adl_Interface,
    AbstractComponent,
    adl_Component,
    adl_AbstractComponent,
    Type,
    adl_Required,
    adl_Provided,
    adl_Binding,
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



def test_adl_type_is_not_abstract():
    assert not inspect.isabstract(adl_Type)


def test_adl_type_constructor_exists():
    assert callable(adl_Type.__init__)


def test_adl_type_constructor_args():
    sig = inspect.signature(adl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl_type_has_signature():
    assert hasattr(adl_Type, "signature")
    descriptor = None
    for klass in adl_Type.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl_namedelement_is_not_abstract():
    assert not inspect.isabstract(adl_NamedElement)


def test_adl_namedelement_constructor_exists():
    assert callable(adl_NamedElement.__init__)


def test_adl_namedelement_constructor_args():
    sig = inspect.signature(adl_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl_namedelement_has_name():
    assert hasattr(adl_NamedElement, "name")
    descriptor = None
    for klass in adl_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_adl_interface_is_not_abstract():
    assert not inspect.isabstract(adl_Interface)


def test_adl_interface_constructor_exists():
    assert callable(adl_Interface.__init__)


def test_adl_interface_constructor_args():
    sig = inspect.signature(adl_Interface.__init__)
    params = list(sig.parameters.keys())



def test_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(AbstractComponent)


def test_abstractcomponent_constructor_exists():
    assert callable(AbstractComponent.__init__)


def test_abstractcomponent_constructor_args():
    sig = inspect.signature(AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_adl_component_is_not_abstract():
    assert not inspect.isabstract(adl_Component)


def test_adl_component_constructor_exists():
    assert callable(adl_Component.__init__)


def test_adl_component_constructor_args():
    sig = inspect.signature(adl_Component.__init__)
    params = list(sig.parameters.keys())



def test_adl_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(adl_AbstractComponent)


def test_adl_abstractcomponent_constructor_exists():
    assert callable(adl_AbstractComponent.__init__)


def test_adl_abstractcomponent_constructor_args():
    sig = inspect.signature(adl_AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_adl_required_is_not_abstract():
    assert not inspect.isabstract(adl_Required)


def test_adl_required_constructor_exists():
    assert callable(adl_Required.__init__)


def test_adl_required_constructor_args():
    sig = inspect.signature(adl_Required.__init__)
    params = list(sig.parameters.keys())



def test_adl_provided_is_not_abstract():
    assert not inspect.isabstract(adl_Provided)


def test_adl_provided_constructor_exists():
    assert callable(adl_Provided.__init__)


def test_adl_provided_constructor_args():
    sig = inspect.signature(adl_Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl_binding_is_not_abstract():
    assert not inspect.isabstract(adl_Binding)


def test_adl_binding_constructor_exists():
    assert callable(adl_Binding.__init__)


def test_adl_binding_constructor_args():
    sig = inspect.signature(adl_Binding.__init__)
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
adl_Type_strategy = st.builds(
    adl_Type,
    signature=
        safe_text
)
adl_NamedElement_strategy = st.builds(
    adl_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
adl_Interface_strategy = st.builds(
    adl_Interface,
)
AbstractComponent_strategy = st.builds(
    AbstractComponent,
)
adl_Component_strategy = st.builds(
    adl_Component,
)
adl_AbstractComponent_strategy = st.builds(
    adl_AbstractComponent,
)
Type_strategy = st.builds(
    Type,
)
adl_Required_strategy = st.builds(
    adl_Required,
)
adl_Provided_strategy = st.builds(
    adl_Provided,
)
adl_Binding_strategy = st.builds(
    adl_Binding,
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl_Type_strategy)
@settings(max_examples=50)
def test_adl_type_instantiation(instance):
    assert isinstance(instance, adl_Type)



@given(instance=adl_Type_strategy)
def test_adl_type_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl_NamedElement_strategy)
@settings(max_examples=50)
def test_adl_namedelement_instantiation(instance):
    assert isinstance(instance, adl_NamedElement)



@given(instance=adl_NamedElement_strategy)
def test_adl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=adl_Interface_strategy)
@settings(max_examples=50)
def test_adl_interface_instantiation(instance):
    assert isinstance(instance, adl_Interface)

@given(instance=AbstractComponent_strategy)
@settings(max_examples=50)
def test_abstractcomponent_instantiation(instance):
    assert isinstance(instance, AbstractComponent)

@given(instance=adl_Component_strategy)
@settings(max_examples=50)
def test_adl_component_instantiation(instance):
    assert isinstance(instance, adl_Component)

@given(instance=adl_AbstractComponent_strategy)
@settings(max_examples=50)
def test_adl_abstractcomponent_instantiation(instance):
    assert isinstance(instance, adl_AbstractComponent)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=adl_Required_strategy)
@settings(max_examples=50)
def test_adl_required_instantiation(instance):
    assert isinstance(instance, adl_Required)

@given(instance=adl_Provided_strategy)
@settings(max_examples=50)
def test_adl_provided_instantiation(instance):
    assert isinstance(instance, adl_Provided)

@given(instance=adl_Binding_strategy)
@settings(max_examples=50)
def test_adl_binding_instantiation(instance):
    assert isinstance(instance, adl_Binding)

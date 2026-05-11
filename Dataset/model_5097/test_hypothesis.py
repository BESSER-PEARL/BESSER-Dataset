import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Interface,
    adl::Type,
    adl::NamedElement,
    NamedElement,
    adl::Interface,
    AbstractComponent,
    adl::Component,
    adl::AbstractComponent,
    Type,
    adl::Provided,
    adl::Required,
    adl::Binding,
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



def test_adl::type_is_not_abstract():
    assert not inspect.isabstract(adl::Type)


def test_adl::type_constructor_exists():
    assert callable(adl::Type.__init__)


def test_adl::type_constructor_args():
    sig = inspect.signature(adl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl::type_has_signature():
    assert hasattr(adl::Type, "signature")
    descriptor = None
    for klass in adl::Type.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl::namedelement_is_not_abstract():
    assert not inspect.isabstract(adl::NamedElement)


def test_adl::namedelement_constructor_exists():
    assert callable(adl::NamedElement.__init__)


def test_adl::namedelement_constructor_args():
    sig = inspect.signature(adl::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl::namedelement_has_name():
    assert hasattr(adl::NamedElement, "name")
    descriptor = None
    for klass in adl::NamedElement.__mro__:
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



def test_adl::interface_is_not_abstract():
    assert not inspect.isabstract(adl::Interface)


def test_adl::interface_constructor_exists():
    assert callable(adl::Interface.__init__)


def test_adl::interface_constructor_args():
    sig = inspect.signature(adl::Interface.__init__)
    params = list(sig.parameters.keys())



def test_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(AbstractComponent)


def test_abstractcomponent_constructor_exists():
    assert callable(AbstractComponent.__init__)


def test_abstractcomponent_constructor_args():
    sig = inspect.signature(AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_adl::component_is_not_abstract():
    assert not inspect.isabstract(adl::Component)


def test_adl::component_constructor_exists():
    assert callable(adl::Component.__init__)


def test_adl::component_constructor_args():
    sig = inspect.signature(adl::Component.__init__)
    params = list(sig.parameters.keys())



def test_adl::abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(adl::AbstractComponent)


def test_adl::abstractcomponent_constructor_exists():
    assert callable(adl::AbstractComponent.__init__)


def test_adl::abstractcomponent_constructor_args():
    sig = inspect.signature(adl::AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_adl::provided_is_not_abstract():
    assert not inspect.isabstract(adl::Provided)


def test_adl::provided_constructor_exists():
    assert callable(adl::Provided.__init__)


def test_adl::provided_constructor_args():
    sig = inspect.signature(adl::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl::required_is_not_abstract():
    assert not inspect.isabstract(adl::Required)


def test_adl::required_constructor_exists():
    assert callable(adl::Required.__init__)


def test_adl::required_constructor_args():
    sig = inspect.signature(adl::Required.__init__)
    params = list(sig.parameters.keys())



def test_adl::binding_is_not_abstract():
    assert not inspect.isabstract(adl::Binding)


def test_adl::binding_constructor_exists():
    assert callable(adl::Binding.__init__)


def test_adl::binding_constructor_args():
    sig = inspect.signature(adl::Binding.__init__)
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
adl::Type_strategy = st.builds(
    adl::Type,
    signature=
        safe_text
)
adl::NamedElement_strategy = st.builds(
    adl::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
adl::Interface_strategy = st.builds(
    adl::Interface,
)
AbstractComponent_strategy = st.builds(
    AbstractComponent,
)
adl::Component_strategy = st.builds(
    adl::Component,
)
adl::AbstractComponent_strategy = st.builds(
    adl::AbstractComponent,
)
Type_strategy = st.builds(
    Type,
)
adl::Provided_strategy = st.builds(
    adl::Provided,
)
adl::Required_strategy = st.builds(
    adl::Required,
)
adl::Binding_strategy = st.builds(
    adl::Binding,
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl::Type_strategy)
@settings(max_examples=50)
def test_adl::type_instantiation(instance):
    assert isinstance(instance, adl::Type)

@given(instance=adl::Type_strategy)
def test_adl::type_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adl::Type_strategy)
def test_adl::type_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl::NamedElement_strategy)
@settings(max_examples=50)
def test_adl::namedelement_instantiation(instance):
    assert isinstance(instance, adl::NamedElement)

@given(instance=adl::NamedElement_strategy)
def test_adl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl::NamedElement_strategy)
def test_adl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=adl::Interface_strategy)
@settings(max_examples=50)
def test_adl::interface_instantiation(instance):
    assert isinstance(instance, adl::Interface)

@given(instance=AbstractComponent_strategy)
@settings(max_examples=50)
def test_abstractcomponent_instantiation(instance):
    assert isinstance(instance, AbstractComponent)

@given(instance=adl::Component_strategy)
@settings(max_examples=50)
def test_adl::component_instantiation(instance):
    assert isinstance(instance, adl::Component)

@given(instance=adl::AbstractComponent_strategy)
@settings(max_examples=50)
def test_adl::abstractcomponent_instantiation(instance):
    assert isinstance(instance, adl::AbstractComponent)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=adl::Provided_strategy)
@settings(max_examples=50)
def test_adl::provided_instantiation(instance):
    assert isinstance(instance, adl::Provided)

@given(instance=adl::Required_strategy)
@settings(max_examples=50)
def test_adl::required_instantiation(instance):
    assert isinstance(instance, adl::Required)

@given(instance=adl::Binding_strategy)
@settings(max_examples=50)
def test_adl::binding_instantiation(instance):
    assert isinstance(instance, adl::Binding)

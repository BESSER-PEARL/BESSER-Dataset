import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Interface,
    adl301::Type,
    adl301::NamedElement,
    AbstractComponent,
    Type,
    NamedElement,
    adl301::Component,
    adl301::Item,
    adl301::Binding,
    adl301::Interface,
    adl301::Provided,
    adl301::Required,
    adl301::Attribute,
    adl301::Attributes,
    adl301::Content,
    adl301::AbstractComponent,
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



def test_adl301::type_is_not_abstract():
    assert not inspect.isabstract(adl301::Type)


def test_adl301::type_constructor_exists():
    assert callable(adl301::Type.__init__)


def test_adl301::type_constructor_args():
    sig = inspect.signature(adl301::Type.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl301::type_has_signature():
    assert hasattr(adl301::Type, "signature")
    descriptor = None
    for klass in adl301::Type.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl301::namedelement_is_not_abstract():
    assert not inspect.isabstract(adl301::NamedElement)


def test_adl301::namedelement_constructor_exists():
    assert callable(adl301::NamedElement.__init__)


def test_adl301::namedelement_constructor_args():
    sig = inspect.signature(adl301::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl301::namedelement_has_name():
    assert hasattr(adl301::NamedElement, "name")
    descriptor = None
    for klass in adl301::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(AbstractComponent)


def test_abstractcomponent_constructor_exists():
    assert callable(AbstractComponent.__init__)


def test_abstractcomponent_constructor_args():
    sig = inspect.signature(AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_adl301::component_is_not_abstract():
    assert not inspect.isabstract(adl301::Component)


def test_adl301::component_constructor_exists():
    assert callable(adl301::Component.__init__)


def test_adl301::component_constructor_args():
    sig = inspect.signature(adl301::Component.__init__)
    params = list(sig.parameters.keys())



def test_adl301::item_is_not_abstract():
    assert not inspect.isabstract(adl301::Item)


def test_adl301::item_constructor_exists():
    assert callable(adl301::Item.__init__)


def test_adl301::item_constructor_args():
    sig = inspect.signature(adl301::Item.__init__)
    params = list(sig.parameters.keys())



def test_adl301::binding_is_not_abstract():
    assert not inspect.isabstract(adl301::Binding)


def test_adl301::binding_constructor_exists():
    assert callable(adl301::Binding.__init__)


def test_adl301::binding_constructor_args():
    sig = inspect.signature(adl301::Binding.__init__)
    params = list(sig.parameters.keys())



def test_adl301::interface_is_not_abstract():
    assert not inspect.isabstract(adl301::Interface)


def test_adl301::interface_constructor_exists():
    assert callable(adl301::Interface.__init__)


def test_adl301::interface_constructor_args():
    sig = inspect.signature(adl301::Interface.__init__)
    params = list(sig.parameters.keys())



def test_adl301::provided_is_not_abstract():
    assert not inspect.isabstract(adl301::Provided)


def test_adl301::provided_constructor_exists():
    assert callable(adl301::Provided.__init__)


def test_adl301::provided_constructor_args():
    sig = inspect.signature(adl301::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl301::required_is_not_abstract():
    assert not inspect.isabstract(adl301::Required)


def test_adl301::required_constructor_exists():
    assert callable(adl301::Required.__init__)


def test_adl301::required_constructor_args():
    sig = inspect.signature(adl301::Required.__init__)
    params = list(sig.parameters.keys())



def test_adl301::attribute_is_not_abstract():
    assert not inspect.isabstract(adl301::Attribute)


def test_adl301::attribute_constructor_exists():
    assert callable(adl301::Attribute.__init__)


def test_adl301::attribute_constructor_args():
    sig = inspect.signature(adl301::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl301::attribute_has_value():
    assert hasattr(adl301::Attribute, "value")
    descriptor = None
    for klass in adl301::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_adl301::attribute_has_name():
    assert hasattr(adl301::Attribute, "name")
    descriptor = None
    for klass in adl301::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl301::attributes_is_not_abstract():
    assert not inspect.isabstract(adl301::Attributes)


def test_adl301::attributes_constructor_exists():
    assert callable(adl301::Attributes.__init__)


def test_adl301::attributes_constructor_args():
    sig = inspect.signature(adl301::Attributes.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl301::attributes_has_signature():
    assert hasattr(adl301::Attributes, "signature")
    descriptor = None
    for klass in adl301::Attributes.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl301::content_is_not_abstract():
    assert not inspect.isabstract(adl301::Content)


def test_adl301::content_constructor_exists():
    assert callable(adl301::Content.__init__)


def test_adl301::content_constructor_args():
    sig = inspect.signature(adl301::Content.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "language" in params, "Missing parameter 'language'"

def test_adl301::content_has_class_():
    assert hasattr(adl301::Content, "class_")
    descriptor = None
    for klass in adl301::Content.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_adl301::content_has_language():
    assert hasattr(adl301::Content, "language")
    descriptor = None
    for klass in adl301::Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_adl301::abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(adl301::AbstractComponent)


def test_adl301::abstractcomponent_constructor_exists():
    assert callable(adl301::AbstractComponent.__init__)


def test_adl301::abstractcomponent_constructor_args():
    sig = inspect.signature(adl301::AbstractComponent.__init__)
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
adl301::Type_strategy = st.builds(
    adl301::Type,
    signature=
        safe_text
)
adl301::NamedElement_strategy = st.builds(
    adl301::NamedElement,
    name=
        safe_text
)
AbstractComponent_strategy = st.builds(
    AbstractComponent,
)
Type_strategy = st.builds(
    Type,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
adl301::Component_strategy = st.builds(
    adl301::Component,
)
adl301::Item_strategy = st.builds(
    adl301::Item,
)
adl301::Binding_strategy = st.builds(
    adl301::Binding,
)
adl301::Interface_strategy = st.builds(
    adl301::Interface,
)
adl301::Provided_strategy = st.builds(
    adl301::Provided,
)
adl301::Required_strategy = st.builds(
    adl301::Required,
)
adl301::Attribute_strategy = st.builds(
    adl301::Attribute,
    value=
        safe_text,
    name=
        safe_text
)
adl301::Attributes_strategy = st.builds(
    adl301::Attributes,
    signature=
        safe_text
)
adl301::Content_strategy = st.builds(
    adl301::Content,
    class_=
        safe_text,
    language=
        safe_text
)
adl301::AbstractComponent_strategy = st.builds(
    adl301::AbstractComponent,
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl301::Type_strategy)
@settings(max_examples=50)
def test_adl301::type_instantiation(instance):
    assert isinstance(instance, adl301::Type)

@given(instance=adl301::Type_strategy)
def test_adl301::type_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adl301::Type_strategy)
def test_adl301::type_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl301::NamedElement_strategy)
@settings(max_examples=50)
def test_adl301::namedelement_instantiation(instance):
    assert isinstance(instance, adl301::NamedElement)

@given(instance=adl301::NamedElement_strategy)
def test_adl301::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl301::NamedElement_strategy)
def test_adl301::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractComponent_strategy)
@settings(max_examples=50)
def test_abstractcomponent_instantiation(instance):
    assert isinstance(instance, AbstractComponent)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=adl301::Component_strategy)
@settings(max_examples=50)
def test_adl301::component_instantiation(instance):
    assert isinstance(instance, adl301::Component)

@given(instance=adl301::Item_strategy)
@settings(max_examples=50)
def test_adl301::item_instantiation(instance):
    assert isinstance(instance, adl301::Item)

@given(instance=adl301::Binding_strategy)
@settings(max_examples=50)
def test_adl301::binding_instantiation(instance):
    assert isinstance(instance, adl301::Binding)

@given(instance=adl301::Interface_strategy)
@settings(max_examples=50)
def test_adl301::interface_instantiation(instance):
    assert isinstance(instance, adl301::Interface)

@given(instance=adl301::Provided_strategy)
@settings(max_examples=50)
def test_adl301::provided_instantiation(instance):
    assert isinstance(instance, adl301::Provided)

@given(instance=adl301::Required_strategy)
@settings(max_examples=50)
def test_adl301::required_instantiation(instance):
    assert isinstance(instance, adl301::Required)

@given(instance=adl301::Attribute_strategy)
@settings(max_examples=50)
def test_adl301::attribute_instantiation(instance):
    assert isinstance(instance, adl301::Attribute)

@given(instance=adl301::Attribute_strategy)
def test_adl301::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=adl301::Attribute_strategy)
def test_adl301::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=adl301::Attribute_strategy)
def test_adl301::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adl301::Attribute_strategy)
def test_adl301::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl301::Attributes_strategy)
@settings(max_examples=50)
def test_adl301::attributes_instantiation(instance):
    assert isinstance(instance, adl301::Attributes)

@given(instance=adl301::Attributes_strategy)
def test_adl301::attributes_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adl301::Attributes_strategy)
def test_adl301::attributes_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl301::Content_strategy)
@settings(max_examples=50)
def test_adl301::content_instantiation(instance):
    assert isinstance(instance, adl301::Content)

@given(instance=adl301::Content_strategy)
def test_adl301::content_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=adl301::Content_strategy)
def test_adl301::content_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=adl301::Content_strategy)
def test_adl301::content_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=adl301::Content_strategy)
def test_adl301::content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=adl301::AbstractComponent_strategy)
@settings(max_examples=50)
def test_adl301::abstractcomponent_instantiation(instance):
    assert isinstance(instance, adl301::AbstractComponent)

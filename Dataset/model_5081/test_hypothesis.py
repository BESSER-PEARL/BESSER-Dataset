import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Type,
    Interface,
    adlrecurs::Type,
    adlrecurs::NamedElement,
    AbstractComponent,
    adlrecurs::Required,
    adlrecurs::Attributes,
    adlrecurs::Attribute,
    NamedElement,
    adlrecurs::Component,
    adlrecurs::Item,
    adlrecurs::Binding,
    adlrecurs::Interface,
    adlrecurs::Provided,
    adlrecurs::Content,
    adlrecurs::AbstractComponent,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_adlrecurs::type_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::Type)


def test_adlrecurs::type_constructor_exists():
    assert callable(adlrecurs::Type.__init__)


def test_adlrecurs::type_constructor_args():
    sig = inspect.signature(adlrecurs::Type.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"

def test_adlrecurs::type_has_signature():
    assert hasattr(adlrecurs::Type, "signature")
    descriptor = None
    for klass in adlrecurs::Type.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adlrecurs::namedelement_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::NamedElement)


def test_adlrecurs::namedelement_constructor_exists():
    assert callable(adlrecurs::NamedElement.__init__)


def test_adlrecurs::namedelement_constructor_args():
    sig = inspect.signature(adlrecurs::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adlrecurs::namedelement_has_name():
    assert hasattr(adlrecurs::NamedElement, "name")
    descriptor = None
    for klass in adlrecurs::NamedElement.__mro__:
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



def test_adlrecurs::required_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::Required)


def test_adlrecurs::required_constructor_exists():
    assert callable(adlrecurs::Required.__init__)


def test_adlrecurs::required_constructor_args():
    sig = inspect.signature(adlrecurs::Required.__init__)
    params = list(sig.parameters.keys())



def test_adlrecurs::attributes_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::Attributes)


def test_adlrecurs::attributes_constructor_exists():
    assert callable(adlrecurs::Attributes.__init__)


def test_adlrecurs::attributes_constructor_args():
    sig = inspect.signature(adlrecurs::Attributes.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"

def test_adlrecurs::attributes_has_signature():
    assert hasattr(adlrecurs::Attributes, "signature")
    descriptor = None
    for klass in adlrecurs::Attributes.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adlrecurs::attribute_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::Attribute)


def test_adlrecurs::attribute_constructor_exists():
    assert callable(adlrecurs::Attribute.__init__)


def test_adlrecurs::attribute_constructor_args():
    sig = inspect.signature(adlrecurs::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_adlrecurs::attribute_has_name():
    assert hasattr(adlrecurs::Attribute, "name")
    descriptor = None
    for klass in adlrecurs::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adlrecurs::attribute_has_value():
    assert hasattr(adlrecurs::Attribute, "value")
    descriptor = None
    for klass in adlrecurs::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_adlrecurs::component_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::Component)


def test_adlrecurs::component_constructor_exists():
    assert callable(adlrecurs::Component.__init__)


def test_adlrecurs::component_constructor_args():
    sig = inspect.signature(adlrecurs::Component.__init__)
    params = list(sig.parameters.keys())



def test_adlrecurs::item_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::Item)


def test_adlrecurs::item_constructor_exists():
    assert callable(adlrecurs::Item.__init__)


def test_adlrecurs::item_constructor_args():
    sig = inspect.signature(adlrecurs::Item.__init__)
    params = list(sig.parameters.keys())



def test_adlrecurs::binding_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::Binding)


def test_adlrecurs::binding_constructor_exists():
    assert callable(adlrecurs::Binding.__init__)


def test_adlrecurs::binding_constructor_args():
    sig = inspect.signature(adlrecurs::Binding.__init__)
    params = list(sig.parameters.keys())



def test_adlrecurs::interface_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::Interface)


def test_adlrecurs::interface_constructor_exists():
    assert callable(adlrecurs::Interface.__init__)


def test_adlrecurs::interface_constructor_args():
    sig = inspect.signature(adlrecurs::Interface.__init__)
    params = list(sig.parameters.keys())



def test_adlrecurs::provided_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::Provided)


def test_adlrecurs::provided_constructor_exists():
    assert callable(adlrecurs::Provided.__init__)


def test_adlrecurs::provided_constructor_args():
    sig = inspect.signature(adlrecurs::Provided.__init__)
    params = list(sig.parameters.keys())



def test_adlrecurs::content_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::Content)


def test_adlrecurs::content_constructor_exists():
    assert callable(adlrecurs::Content.__init__)


def test_adlrecurs::content_constructor_args():
    sig = inspect.signature(adlrecurs::Content.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_adlrecurs::content_has_language():
    assert hasattr(adlrecurs::Content, "language")
    descriptor = None
    for klass in adlrecurs::Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_adlrecurs::content_has_class_():
    assert hasattr(adlrecurs::Content, "class_")
    descriptor = None
    for klass in adlrecurs::Content.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_adlrecurs::abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(adlrecurs::AbstractComponent)


def test_adlrecurs::abstractcomponent_constructor_exists():
    assert callable(adlrecurs::AbstractComponent.__init__)


def test_adlrecurs::abstractcomponent_constructor_args():
    sig = inspect.signature(adlrecurs::AbstractComponent.__init__)
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
Type_strategy = st.builds(
    Type,
)
Interface_strategy = st.builds(
    Interface,
)
adlrecurs::Type_strategy = st.builds(
    adlrecurs::Type,
    signature=
        safe_text
)
adlrecurs::NamedElement_strategy = st.builds(
    adlrecurs::NamedElement,
    name=
        safe_text
)
AbstractComponent_strategy = st.builds(
    AbstractComponent,
)
adlrecurs::Required_strategy = st.builds(
    adlrecurs::Required,
)
adlrecurs::Attributes_strategy = st.builds(
    adlrecurs::Attributes,
    signature=
        safe_text
)
adlrecurs::Attribute_strategy = st.builds(
    adlrecurs::Attribute,
    name=
        safe_text,
    value=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
adlrecurs::Component_strategy = st.builds(
    adlrecurs::Component,
)
adlrecurs::Item_strategy = st.builds(
    adlrecurs::Item,
)
adlrecurs::Binding_strategy = st.builds(
    adlrecurs::Binding,
)
adlrecurs::Interface_strategy = st.builds(
    adlrecurs::Interface,
)
adlrecurs::Provided_strategy = st.builds(
    adlrecurs::Provided,
)
adlrecurs::Content_strategy = st.builds(
    adlrecurs::Content,
    language=
        safe_text,
    class_=
        safe_text
)
adlrecurs::AbstractComponent_strategy = st.builds(
    adlrecurs::AbstractComponent,
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adlrecurs::Type_strategy)
@settings(max_examples=50)
def test_adlrecurs::type_instantiation(instance):
    assert isinstance(instance, adlrecurs::Type)

@given(instance=adlrecurs::Type_strategy)
def test_adlrecurs::type_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adlrecurs::Type_strategy)
def test_adlrecurs::type_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adlrecurs::NamedElement_strategy)
@settings(max_examples=50)
def test_adlrecurs::namedelement_instantiation(instance):
    assert isinstance(instance, adlrecurs::NamedElement)

@given(instance=adlrecurs::NamedElement_strategy)
def test_adlrecurs::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adlrecurs::NamedElement_strategy)
def test_adlrecurs::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractComponent_strategy)
@settings(max_examples=50)
def test_abstractcomponent_instantiation(instance):
    assert isinstance(instance, AbstractComponent)

@given(instance=adlrecurs::Required_strategy)
@settings(max_examples=50)
def test_adlrecurs::required_instantiation(instance):
    assert isinstance(instance, adlrecurs::Required)

@given(instance=adlrecurs::Attributes_strategy)
@settings(max_examples=50)
def test_adlrecurs::attributes_instantiation(instance):
    assert isinstance(instance, adlrecurs::Attributes)

@given(instance=adlrecurs::Attributes_strategy)
def test_adlrecurs::attributes_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=adlrecurs::Attributes_strategy)
def test_adlrecurs::attributes_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adlrecurs::Attribute_strategy)
@settings(max_examples=50)
def test_adlrecurs::attribute_instantiation(instance):
    assert isinstance(instance, adlrecurs::Attribute)

@given(instance=adlrecurs::Attribute_strategy)
def test_adlrecurs::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adlrecurs::Attribute_strategy)
def test_adlrecurs::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adlrecurs::Attribute_strategy)
def test_adlrecurs::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=adlrecurs::Attribute_strategy)
def test_adlrecurs::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=adlrecurs::Component_strategy)
@settings(max_examples=50)
def test_adlrecurs::component_instantiation(instance):
    assert isinstance(instance, adlrecurs::Component)

@given(instance=adlrecurs::Item_strategy)
@settings(max_examples=50)
def test_adlrecurs::item_instantiation(instance):
    assert isinstance(instance, adlrecurs::Item)

@given(instance=adlrecurs::Binding_strategy)
@settings(max_examples=50)
def test_adlrecurs::binding_instantiation(instance):
    assert isinstance(instance, adlrecurs::Binding)

@given(instance=adlrecurs::Interface_strategy)
@settings(max_examples=50)
def test_adlrecurs::interface_instantiation(instance):
    assert isinstance(instance, adlrecurs::Interface)

@given(instance=adlrecurs::Provided_strategy)
@settings(max_examples=50)
def test_adlrecurs::provided_instantiation(instance):
    assert isinstance(instance, adlrecurs::Provided)

@given(instance=adlrecurs::Content_strategy)
@settings(max_examples=50)
def test_adlrecurs::content_instantiation(instance):
    assert isinstance(instance, adlrecurs::Content)

@given(instance=adlrecurs::Content_strategy)
def test_adlrecurs::content_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=adlrecurs::Content_strategy)
def test_adlrecurs::content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=adlrecurs::Content_strategy)
def test_adlrecurs::content_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=adlrecurs::Content_strategy)
def test_adlrecurs::content_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=adlrecurs::AbstractComponent_strategy)
@settings(max_examples=50)
def test_adlrecurs::abstractcomponent_instantiation(instance):
    assert isinstance(instance, adlrecurs::AbstractComponent)

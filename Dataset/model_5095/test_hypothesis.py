import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Interface,
    adl301_Type,
    adl301_NamedElement,
    AbstractComponent,
    Type,
    NamedElement,
    adl301_Binding,
    adl301_Item,
    adl301_Component,
    adl301_Interface,
    adl301_Provided,
    adl301_Required,
    adl301_Attribute,
    adl301_Attributes,
    adl301_Content,
    adl301_AbstractComponent,
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



def test_adl301_type_is_not_abstract():
    assert not inspect.isabstract(adl301_Type)


def test_adl301_type_constructor_exists():
    assert callable(adl301_Type.__init__)


def test_adl301_type_constructor_args():
    sig = inspect.signature(adl301_Type.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl301_type_has_signature():
    assert hasattr(adl301_Type, "signature")
    descriptor = None
    for klass in adl301_Type.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl301_namedelement_is_not_abstract():
    assert not inspect.isabstract(adl301_NamedElement)


def test_adl301_namedelement_constructor_exists():
    assert callable(adl301_NamedElement.__init__)


def test_adl301_namedelement_constructor_args():
    sig = inspect.signature(adl301_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adl301_namedelement_has_name():
    assert hasattr(adl301_NamedElement, "name")
    descriptor = None
    for klass in adl301_NamedElement.__mro__:
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



def test_adl301_binding_is_not_abstract():
    assert not inspect.isabstract(adl301_Binding)


def test_adl301_binding_constructor_exists():
    assert callable(adl301_Binding.__init__)


def test_adl301_binding_constructor_args():
    sig = inspect.signature(adl301_Binding.__init__)
    params = list(sig.parameters.keys())



def test_adl301_item_is_not_abstract():
    assert not inspect.isabstract(adl301_Item)


def test_adl301_item_constructor_exists():
    assert callable(adl301_Item.__init__)


def test_adl301_item_constructor_args():
    sig = inspect.signature(adl301_Item.__init__)
    params = list(sig.parameters.keys())



def test_adl301_component_is_not_abstract():
    assert not inspect.isabstract(adl301_Component)


def test_adl301_component_constructor_exists():
    assert callable(adl301_Component.__init__)


def test_adl301_component_constructor_args():
    sig = inspect.signature(adl301_Component.__init__)
    params = list(sig.parameters.keys())



def test_adl301_interface_is_not_abstract():
    assert not inspect.isabstract(adl301_Interface)


def test_adl301_interface_constructor_exists():
    assert callable(adl301_Interface.__init__)


def test_adl301_interface_constructor_args():
    sig = inspect.signature(adl301_Interface.__init__)
    params = list(sig.parameters.keys())



def test_adl301_provided_is_not_abstract():
    assert not inspect.isabstract(adl301_Provided)


def test_adl301_provided_constructor_exists():
    assert callable(adl301_Provided.__init__)


def test_adl301_provided_constructor_args():
    sig = inspect.signature(adl301_Provided.__init__)
    params = list(sig.parameters.keys())



def test_adl301_required_is_not_abstract():
    assert not inspect.isabstract(adl301_Required)


def test_adl301_required_constructor_exists():
    assert callable(adl301_Required.__init__)


def test_adl301_required_constructor_args():
    sig = inspect.signature(adl301_Required.__init__)
    params = list(sig.parameters.keys())



def test_adl301_attribute_is_not_abstract():
    assert not inspect.isabstract(adl301_Attribute)


def test_adl301_attribute_constructor_exists():
    assert callable(adl301_Attribute.__init__)


def test_adl301_attribute_constructor_args():
    sig = inspect.signature(adl301_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_adl301_attribute_has_value():
    assert hasattr(adl301_Attribute, "value")
    descriptor = None
    for klass in adl301_Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_adl301_attribute_has_name():
    assert hasattr(adl301_Attribute, "name")
    descriptor = None
    for klass in adl301_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adl301_attributes_is_not_abstract():
    assert not inspect.isabstract(adl301_Attributes)


def test_adl301_attributes_constructor_exists():
    assert callable(adl301_Attributes.__init__)


def test_adl301_attributes_constructor_args():
    sig = inspect.signature(adl301_Attributes.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"

def test_adl301_attributes_has_signature():
    assert hasattr(adl301_Attributes, "signature")
    descriptor = None
    for klass in adl301_Attributes.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_adl301_content_is_not_abstract():
    assert not inspect.isabstract(adl301_Content)


def test_adl301_content_constructor_exists():
    assert callable(adl301_Content.__init__)


def test_adl301_content_constructor_args():
    sig = inspect.signature(adl301_Content.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_adl301_content_has_language():
    assert hasattr(adl301_Content, "language")
    descriptor = None
    for klass in adl301_Content.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_adl301_content_has_class_():
    assert hasattr(adl301_Content, "class_")
    descriptor = None
    for klass in adl301_Content.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_adl301_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(adl301_AbstractComponent)


def test_adl301_abstractcomponent_constructor_exists():
    assert callable(adl301_AbstractComponent.__init__)


def test_adl301_abstractcomponent_constructor_args():
    sig = inspect.signature(adl301_AbstractComponent.__init__)
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
adl301_Type_strategy = st.builds(
    adl301_Type,
    signature=
        safe_text
)
adl301_NamedElement_strategy = st.builds(
    adl301_NamedElement,
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
adl301_Binding_strategy = st.builds(
    adl301_Binding,
)
adl301_Item_strategy = st.builds(
    adl301_Item,
)
adl301_Component_strategy = st.builds(
    adl301_Component,
)
adl301_Interface_strategy = st.builds(
    adl301_Interface,
)
adl301_Provided_strategy = st.builds(
    adl301_Provided,
)
adl301_Required_strategy = st.builds(
    adl301_Required,
)
adl301_Attribute_strategy = st.builds(
    adl301_Attribute,
    value=
        safe_text,
    name=
        safe_text
)
adl301_Attributes_strategy = st.builds(
    adl301_Attributes,
    signature=
        safe_text
)
adl301_Content_strategy = st.builds(
    adl301_Content,
    language=
        safe_text,
    class_=
        safe_text
)
adl301_AbstractComponent_strategy = st.builds(
    adl301_AbstractComponent,
)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=adl301_Type_strategy)
@settings(max_examples=50)
def test_adl301_type_instantiation(instance):
    assert isinstance(instance, adl301_Type)



@given(instance=adl301_Type_strategy)
def test_adl301_type_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl301_NamedElement_strategy)
@settings(max_examples=50)
def test_adl301_namedelement_instantiation(instance):
    assert isinstance(instance, adl301_NamedElement)



@given(instance=adl301_NamedElement_strategy)
def test_adl301_namedelement_name_setter(instance):
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

@given(instance=adl301_Binding_strategy)
@settings(max_examples=50)
def test_adl301_binding_instantiation(instance):
    assert isinstance(instance, adl301_Binding)

@given(instance=adl301_Item_strategy)
@settings(max_examples=50)
def test_adl301_item_instantiation(instance):
    assert isinstance(instance, adl301_Item)

@given(instance=adl301_Component_strategy)
@settings(max_examples=50)
def test_adl301_component_instantiation(instance):
    assert isinstance(instance, adl301_Component)

@given(instance=adl301_Interface_strategy)
@settings(max_examples=50)
def test_adl301_interface_instantiation(instance):
    assert isinstance(instance, adl301_Interface)

@given(instance=adl301_Provided_strategy)
@settings(max_examples=50)
def test_adl301_provided_instantiation(instance):
    assert isinstance(instance, adl301_Provided)

@given(instance=adl301_Required_strategy)
@settings(max_examples=50)
def test_adl301_required_instantiation(instance):
    assert isinstance(instance, adl301_Required)

@given(instance=adl301_Attribute_strategy)
@settings(max_examples=50)
def test_adl301_attribute_instantiation(instance):
    assert isinstance(instance, adl301_Attribute)



@given(instance=adl301_Attribute_strategy)
def test_adl301_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=adl301_Attribute_strategy)
def test_adl301_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adl301_Attributes_strategy)
@settings(max_examples=50)
def test_adl301_attributes_instantiation(instance):
    assert isinstance(instance, adl301_Attributes)



@given(instance=adl301_Attributes_strategy)
def test_adl301_attributes_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=adl301_Content_strategy)
@settings(max_examples=50)
def test_adl301_content_instantiation(instance):
    assert isinstance(instance, adl301_Content)



@given(instance=adl301_Content_strategy)
def test_adl301_content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=adl301_Content_strategy)
def test_adl301_content_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=adl301_AbstractComponent_strategy)
@settings(max_examples=50)
def test_adl301_abstractcomponent_instantiation(instance):
    assert isinstance(instance, adl301_AbstractComponent)

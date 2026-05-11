import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ER::NamedElement,
    NamedElement,
    ER::EntityType,
    ER::ERModel,
    Reference,
    ER::StrongReference,
    ER::WeakReference,
    Feature,
    ER::Reference,
    ER::Attribute,
    ER::Feature,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_er::namedelement_is_not_abstract():
    assert not inspect.isabstract(ER::NamedElement)


def test_er::namedelement_constructor_exists():
    assert callable(ER::NamedElement.__init__)


def test_er::namedelement_constructor_args():
    sig = inspect.signature(ER::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er::namedelement_has_name():
    assert hasattr(ER::NamedElement, "name")
    descriptor = None
    for klass in ER::NamedElement.__mro__:
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



def test_er::entitytype_is_not_abstract():
    assert not inspect.isabstract(ER::EntityType)


def test_er::entitytype_constructor_exists():
    assert callable(ER::EntityType.__init__)


def test_er::entitytype_constructor_args():
    sig = inspect.signature(ER::EntityType.__init__)
    params = list(sig.parameters.keys())



def test_er::ermodel_is_not_abstract():
    assert not inspect.isabstract(ER::ERModel)


def test_er::ermodel_constructor_exists():
    assert callable(ER::ERModel.__init__)


def test_er::ermodel_constructor_args():
    sig = inspect.signature(ER::ERModel.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_er::strongreference_is_not_abstract():
    assert not inspect.isabstract(ER::StrongReference)


def test_er::strongreference_constructor_exists():
    assert callable(ER::StrongReference.__init__)


def test_er::strongreference_constructor_args():
    sig = inspect.signature(ER::StrongReference.__init__)
    params = list(sig.parameters.keys())



def test_er::weakreference_is_not_abstract():
    assert not inspect.isabstract(ER::WeakReference)


def test_er::weakreference_constructor_exists():
    assert callable(ER::WeakReference.__init__)


def test_er::weakreference_constructor_args():
    sig = inspect.signature(ER::WeakReference.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_er::reference_is_not_abstract():
    assert not inspect.isabstract(ER::Reference)


def test_er::reference_constructor_exists():
    assert callable(ER::Reference.__init__)


def test_er::reference_constructor_args():
    sig = inspect.signature(ER::Reference.__init__)
    params = list(sig.parameters.keys())



def test_er::attribute_is_not_abstract():
    assert not inspect.isabstract(ER::Attribute)


def test_er::attribute_constructor_exists():
    assert callable(ER::Attribute.__init__)


def test_er::attribute_constructor_args():
    sig = inspect.signature(ER::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_er::attribute_has_type():
    assert hasattr(ER::Attribute, "type")
    descriptor = None
    for klass in ER::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_er::feature_is_not_abstract():
    assert not inspect.isabstract(ER::Feature)


def test_er::feature_constructor_exists():
    assert callable(ER::Feature.__init__)


def test_er::feature_constructor_args():
    sig = inspect.signature(ER::Feature.__init__)
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
ER::NamedElement_strategy = st.builds(
    ER::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ER::EntityType_strategy = st.builds(
    ER::EntityType,
)
ER::ERModel_strategy = st.builds(
    ER::ERModel,
)
Reference_strategy = st.builds(
    Reference,
)
ER::StrongReference_strategy = st.builds(
    ER::StrongReference,
)
ER::WeakReference_strategy = st.builds(
    ER::WeakReference,
)
Feature_strategy = st.builds(
    Feature,
)
ER::Reference_strategy = st.builds(
    ER::Reference,
)
ER::Attribute_strategy = st.builds(
    ER::Attribute,
    type=
        safe_text
)
ER::Feature_strategy = st.builds(
    ER::Feature,
)

@given(instance=ER::NamedElement_strategy)
@settings(max_examples=50)
def test_er::namedelement_instantiation(instance):
    assert isinstance(instance, ER::NamedElement)

@given(instance=ER::NamedElement_strategy)
def test_er::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ER::NamedElement_strategy)
def test_er::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ER::EntityType_strategy)
@settings(max_examples=50)
def test_er::entitytype_instantiation(instance):
    assert isinstance(instance, ER::EntityType)

@given(instance=ER::ERModel_strategy)
@settings(max_examples=50)
def test_er::ermodel_instantiation(instance):
    assert isinstance(instance, ER::ERModel)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=ER::StrongReference_strategy)
@settings(max_examples=50)
def test_er::strongreference_instantiation(instance):
    assert isinstance(instance, ER::StrongReference)

@given(instance=ER::WeakReference_strategy)
@settings(max_examples=50)
def test_er::weakreference_instantiation(instance):
    assert isinstance(instance, ER::WeakReference)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=ER::Reference_strategy)
@settings(max_examples=50)
def test_er::reference_instantiation(instance):
    assert isinstance(instance, ER::Reference)

@given(instance=ER::Attribute_strategy)
@settings(max_examples=50)
def test_er::attribute_instantiation(instance):
    assert isinstance(instance, ER::Attribute)

@given(instance=ER::Attribute_strategy)
def test_er::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ER::Attribute_strategy)
def test_er::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ER::Feature_strategy)
@settings(max_examples=50)
def test_er::feature_instantiation(instance):
    assert isinstance(instance, ER::Feature)

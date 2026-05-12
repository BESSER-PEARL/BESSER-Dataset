import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ER_NamedElement,
    Feature,
    ER_Reference,
    ER_Attribute,
    NamedElement,
    ER_EntityType,
    ER_Feature,
    ER_ERModel,
    Reference,
    ER_WeakReference,
    ER_StrongReference,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_er_namedelement_is_not_abstract():
    assert not inspect.isabstract(ER_NamedElement)


def test_er_namedelement_constructor_exists():
    assert callable(ER_NamedElement.__init__)


def test_er_namedelement_constructor_args():
    sig = inspect.signature(ER_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_er_namedelement_has_name():
    assert hasattr(ER_NamedElement, "name")
    descriptor = None
    for klass in ER_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_er_reference_is_not_abstract():
    assert not inspect.isabstract(ER_Reference)


def test_er_reference_constructor_exists():
    assert callable(ER_Reference.__init__)


def test_er_reference_constructor_args():
    sig = inspect.signature(ER_Reference.__init__)
    params = list(sig.parameters.keys())



def test_er_attribute_is_not_abstract():
    assert not inspect.isabstract(ER_Attribute)


def test_er_attribute_constructor_exists():
    assert callable(ER_Attribute.__init__)


def test_er_attribute_constructor_args():
    sig = inspect.signature(ER_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_er_attribute_has_type():
    assert hasattr(ER_Attribute, "type")
    descriptor = None
    for klass in ER_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_er_entitytype_is_not_abstract():
    assert not inspect.isabstract(ER_EntityType)


def test_er_entitytype_constructor_exists():
    assert callable(ER_EntityType.__init__)


def test_er_entitytype_constructor_args():
    sig = inspect.signature(ER_EntityType.__init__)
    params = list(sig.parameters.keys())



def test_er_feature_is_not_abstract():
    assert not inspect.isabstract(ER_Feature)


def test_er_feature_constructor_exists():
    assert callable(ER_Feature.__init__)


def test_er_feature_constructor_args():
    sig = inspect.signature(ER_Feature.__init__)
    params = list(sig.parameters.keys())



def test_er_ermodel_is_not_abstract():
    assert not inspect.isabstract(ER_ERModel)


def test_er_ermodel_constructor_exists():
    assert callable(ER_ERModel.__init__)


def test_er_ermodel_constructor_args():
    sig = inspect.signature(ER_ERModel.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_er_weakreference_is_not_abstract():
    assert not inspect.isabstract(ER_WeakReference)


def test_er_weakreference_constructor_exists():
    assert callable(ER_WeakReference.__init__)


def test_er_weakreference_constructor_args():
    sig = inspect.signature(ER_WeakReference.__init__)
    params = list(sig.parameters.keys())



def test_er_strongreference_is_not_abstract():
    assert not inspect.isabstract(ER_StrongReference)


def test_er_strongreference_constructor_exists():
    assert callable(ER_StrongReference.__init__)


def test_er_strongreference_constructor_args():
    sig = inspect.signature(ER_StrongReference.__init__)
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
ER_NamedElement_strategy = st.builds(
    ER_NamedElement,
    name=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
ER_Reference_strategy = st.builds(
    ER_Reference,
)
ER_Attribute_strategy = st.builds(
    ER_Attribute,
    type=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ER_EntityType_strategy = st.builds(
    ER_EntityType,
)
ER_Feature_strategy = st.builds(
    ER_Feature,
)
ER_ERModel_strategy = st.builds(
    ER_ERModel,
)
Reference_strategy = st.builds(
    Reference,
)
ER_WeakReference_strategy = st.builds(
    ER_WeakReference,
)
ER_StrongReference_strategy = st.builds(
    ER_StrongReference,
)

@given(instance=ER_NamedElement_strategy)
@settings(max_examples=50)
def test_er_namedelement_instantiation(instance):
    assert isinstance(instance, ER_NamedElement)



@given(instance=ER_NamedElement_strategy)
def test_er_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=ER_Reference_strategy)
@settings(max_examples=50)
def test_er_reference_instantiation(instance):
    assert isinstance(instance, ER_Reference)

@given(instance=ER_Attribute_strategy)
@settings(max_examples=50)
def test_er_attribute_instantiation(instance):
    assert isinstance(instance, ER_Attribute)



@given(instance=ER_Attribute_strategy)
def test_er_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ER_EntityType_strategy)
@settings(max_examples=50)
def test_er_entitytype_instantiation(instance):
    assert isinstance(instance, ER_EntityType)

@given(instance=ER_Feature_strategy)
@settings(max_examples=50)
def test_er_feature_instantiation(instance):
    assert isinstance(instance, ER_Feature)

@given(instance=ER_ERModel_strategy)
@settings(max_examples=50)
def test_er_ermodel_instantiation(instance):
    assert isinstance(instance, ER_ERModel)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=ER_WeakReference_strategy)
@settings(max_examples=50)
def test_er_weakreference_instantiation(instance):
    assert isinstance(instance, ER_WeakReference)

@given(instance=ER_StrongReference_strategy)
@settings(max_examples=50)
def test_er_strongreference_instantiation(instance):
    assert isinstance(instance, ER_StrongReference)

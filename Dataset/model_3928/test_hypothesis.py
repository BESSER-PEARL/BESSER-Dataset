import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    entity_Type,
    entity_Namespace,
    entity_NamedElement,
    entity_Attribute,
    entity_Reference,
    Type,
    entity_Datatype,
    entity_Entity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_entity_type_is_not_abstract():
    assert not inspect.isabstract(entity_Type)


def test_entity_type_constructor_exists():
    assert callable(entity_Type.__init__)


def test_entity_type_constructor_args():
    sig = inspect.signature(entity_Type.__init__)
    params = list(sig.parameters.keys())



def test_entity_namespace_is_not_abstract():
    assert not inspect.isabstract(entity_Namespace)


def test_entity_namespace_constructor_exists():
    assert callable(entity_Namespace.__init__)


def test_entity_namespace_constructor_args():
    sig = inspect.signature(entity_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_entity_namedelement_is_not_abstract():
    assert not inspect.isabstract(entity_NamedElement)


def test_entity_namedelement_constructor_exists():
    assert callable(entity_NamedElement.__init__)


def test_entity_namedelement_constructor_args():
    sig = inspect.signature(entity_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity_namedelement_has_name():
    assert hasattr(entity_NamedElement, "name")
    descriptor = None
    for klass in entity_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity_attribute_is_not_abstract():
    assert not inspect.isabstract(entity_Attribute)


def test_entity_attribute_constructor_exists():
    assert callable(entity_Attribute.__init__)


def test_entity_attribute_constructor_args():
    sig = inspect.signature(entity_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_entity_reference_is_not_abstract():
    assert not inspect.isabstract(entity_Reference)


def test_entity_reference_constructor_exists():
    assert callable(entity_Reference.__init__)


def test_entity_reference_constructor_args():
    sig = inspect.signature(entity_Reference.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_entity_datatype_is_not_abstract():
    assert not inspect.isabstract(entity_Datatype)


def test_entity_datatype_constructor_exists():
    assert callable(entity_Datatype.__init__)


def test_entity_datatype_constructor_args():
    sig = inspect.signature(entity_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_entity_entity_is_not_abstract():
    assert not inspect.isabstract(entity_Entity)


def test_entity_entity_constructor_exists():
    assert callable(entity_Entity.__init__)


def test_entity_entity_constructor_args():
    sig = inspect.signature(entity_Entity.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
entity_Type_strategy = st.builds(
    entity_Type,
)
entity_Namespace_strategy = st.builds(
    entity_Namespace,
)
entity_NamedElement_strategy = st.builds(
    entity_NamedElement,
    name=
        safe_text
)
entity_Attribute_strategy = st.builds(
    entity_Attribute,
)
entity_Reference_strategy = st.builds(
    entity_Reference,
)
Type_strategy = st.builds(
    Type,
)
entity_Datatype_strategy = st.builds(
    entity_Datatype,
)
entity_Entity_strategy = st.builds(
    entity_Entity,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=entity_Type_strategy)
@settings(max_examples=50)
def test_entity_type_instantiation(instance):
    assert isinstance(instance, entity_Type)

@given(instance=entity_Namespace_strategy)
@settings(max_examples=50)
def test_entity_namespace_instantiation(instance):
    assert isinstance(instance, entity_Namespace)

@given(instance=entity_NamedElement_strategy)
@settings(max_examples=50)
def test_entity_namedelement_instantiation(instance):
    assert isinstance(instance, entity_NamedElement)



@given(instance=entity_NamedElement_strategy)
def test_entity_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entity_Attribute_strategy)
@settings(max_examples=50)
def test_entity_attribute_instantiation(instance):
    assert isinstance(instance, entity_Attribute)

@given(instance=entity_Reference_strategy)
@settings(max_examples=50)
def test_entity_reference_instantiation(instance):
    assert isinstance(instance, entity_Reference)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entity_Datatype_strategy)
@settings(max_examples=50)
def test_entity_datatype_instantiation(instance):
    assert isinstance(instance, entity_Datatype)

@given(instance=entity_Entity_strategy)
@settings(max_examples=50)
def test_entity_entity_instantiation(instance):
    assert isinstance(instance, entity_Entity)

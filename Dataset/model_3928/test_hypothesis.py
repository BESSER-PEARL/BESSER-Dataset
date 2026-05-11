import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    entity::Type,
    entity::Namespace,
    entity::NamedElement,
    entity::Attribute,
    entity::Reference,
    Type,
    entity::Datatype,
    entity::Entity,
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



def test_entity::type_is_not_abstract():
    assert not inspect.isabstract(entity::Type)


def test_entity::type_constructor_exists():
    assert callable(entity::Type.__init__)


def test_entity::type_constructor_args():
    sig = inspect.signature(entity::Type.__init__)
    params = list(sig.parameters.keys())



def test_entity::namespace_is_not_abstract():
    assert not inspect.isabstract(entity::Namespace)


def test_entity::namespace_constructor_exists():
    assert callable(entity::Namespace.__init__)


def test_entity::namespace_constructor_args():
    sig = inspect.signature(entity::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_entity::namedelement_is_not_abstract():
    assert not inspect.isabstract(entity::NamedElement)


def test_entity::namedelement_constructor_exists():
    assert callable(entity::NamedElement.__init__)


def test_entity::namedelement_constructor_args():
    sig = inspect.signature(entity::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity::namedelement_has_name():
    assert hasattr(entity::NamedElement, "name")
    descriptor = None
    for klass in entity::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity::attribute_is_not_abstract():
    assert not inspect.isabstract(entity::Attribute)


def test_entity::attribute_constructor_exists():
    assert callable(entity::Attribute.__init__)


def test_entity::attribute_constructor_args():
    sig = inspect.signature(entity::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_entity::reference_is_not_abstract():
    assert not inspect.isabstract(entity::Reference)


def test_entity::reference_constructor_exists():
    assert callable(entity::Reference.__init__)


def test_entity::reference_constructor_args():
    sig = inspect.signature(entity::Reference.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_entity::datatype_is_not_abstract():
    assert not inspect.isabstract(entity::Datatype)


def test_entity::datatype_constructor_exists():
    assert callable(entity::Datatype.__init__)


def test_entity::datatype_constructor_args():
    sig = inspect.signature(entity::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_entity::entity_is_not_abstract():
    assert not inspect.isabstract(entity::Entity)


def test_entity::entity_constructor_exists():
    assert callable(entity::Entity.__init__)


def test_entity::entity_constructor_args():
    sig = inspect.signature(entity::Entity.__init__)
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
entity::Type_strategy = st.builds(
    entity::Type,
)
entity::Namespace_strategy = st.builds(
    entity::Namespace,
)
entity::NamedElement_strategy = st.builds(
    entity::NamedElement,
    name=
        safe_text
)
entity::Attribute_strategy = st.builds(
    entity::Attribute,
)
entity::Reference_strategy = st.builds(
    entity::Reference,
)
Type_strategy = st.builds(
    Type,
)
entity::Datatype_strategy = st.builds(
    entity::Datatype,
)
entity::Entity_strategy = st.builds(
    entity::Entity,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=entity::Type_strategy)
@settings(max_examples=50)
def test_entity::type_instantiation(instance):
    assert isinstance(instance, entity::Type)

@given(instance=entity::Namespace_strategy)
@settings(max_examples=50)
def test_entity::namespace_instantiation(instance):
    assert isinstance(instance, entity::Namespace)

@given(instance=entity::NamedElement_strategy)
@settings(max_examples=50)
def test_entity::namedelement_instantiation(instance):
    assert isinstance(instance, entity::NamedElement)

@given(instance=entity::NamedElement_strategy)
def test_entity::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entity::NamedElement_strategy)
def test_entity::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entity::Attribute_strategy)
@settings(max_examples=50)
def test_entity::attribute_instantiation(instance):
    assert isinstance(instance, entity::Attribute)

@given(instance=entity::Reference_strategy)
@settings(max_examples=50)
def test_entity::reference_instantiation(instance):
    assert isinstance(instance, entity::Reference)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entity::Datatype_strategy)
@settings(max_examples=50)
def test_entity::datatype_instantiation(instance):
    assert isinstance(instance, entity::Datatype)

@given(instance=entity::Entity_strategy)
@settings(max_examples=50)
def test_entity::entity_instantiation(instance):
    assert isinstance(instance, entity::Entity)

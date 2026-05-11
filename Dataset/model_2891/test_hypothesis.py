import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    entity::Feature,
    Type,
    entity::Entity,
    entity::Datatype,
    entity::Type,
    entity::Domain,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity::feature_is_not_abstract():
    assert not inspect.isabstract(entity::Feature)


def test_entity::feature_constructor_exists():
    assert callable(entity::Feature.__init__)


def test_entity::feature_constructor_args():
    sig = inspect.signature(entity::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity::feature_has_name():
    assert hasattr(entity::Feature, "name")
    descriptor = None
    for klass in entity::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_entity::entity_is_not_abstract():
    assert not inspect.isabstract(entity::Entity)


def test_entity::entity_constructor_exists():
    assert callable(entity::Entity.__init__)


def test_entity::entity_constructor_args():
    sig = inspect.signature(entity::Entity.__init__)
    params = list(sig.parameters.keys())



def test_entity::datatype_is_not_abstract():
    assert not inspect.isabstract(entity::Datatype)


def test_entity::datatype_constructor_exists():
    assert callable(entity::Datatype.__init__)


def test_entity::datatype_constructor_args():
    sig = inspect.signature(entity::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_entity::type_is_not_abstract():
    assert not inspect.isabstract(entity::Type)


def test_entity::type_constructor_exists():
    assert callable(entity::Type.__init__)


def test_entity::type_constructor_args():
    sig = inspect.signature(entity::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity::type_has_name():
    assert hasattr(entity::Type, "name")
    descriptor = None
    for klass in entity::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity::domain_is_not_abstract():
    assert not inspect.isabstract(entity::Domain)


def test_entity::domain_constructor_exists():
    assert callable(entity::Domain.__init__)


def test_entity::domain_constructor_args():
    sig = inspect.signature(entity::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity::domain_has_name():
    assert hasattr(entity::Domain, "name")
    descriptor = None
    for klass in entity::Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
entity::Feature_strategy = st.builds(
    entity::Feature,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
entity::Entity_strategy = st.builds(
    entity::Entity,
)
entity::Datatype_strategy = st.builds(
    entity::Datatype,
)
entity::Type_strategy = st.builds(
    entity::Type,
    name=
        safe_text
)
entity::Domain_strategy = st.builds(
    entity::Domain,
    name=
        safe_text
)

@given(instance=entity::Feature_strategy)
@settings(max_examples=50)
def test_entity::feature_instantiation(instance):
    assert isinstance(instance, entity::Feature)

@given(instance=entity::Feature_strategy)
def test_entity::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entity::Feature_strategy)
def test_entity::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entity::Entity_strategy)
@settings(max_examples=50)
def test_entity::entity_instantiation(instance):
    assert isinstance(instance, entity::Entity)

@given(instance=entity::Datatype_strategy)
@settings(max_examples=50)
def test_entity::datatype_instantiation(instance):
    assert isinstance(instance, entity::Datatype)

@given(instance=entity::Type_strategy)
@settings(max_examples=50)
def test_entity::type_instantiation(instance):
    assert isinstance(instance, entity::Type)

@given(instance=entity::Type_strategy)
def test_entity::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entity::Type_strategy)
def test_entity::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entity::Domain_strategy)
@settings(max_examples=50)
def test_entity::domain_instantiation(instance):
    assert isinstance(instance, entity::Domain)

@given(instance=entity::Domain_strategy)
def test_entity::domain_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entity::Domain_strategy)
def test_entity::domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

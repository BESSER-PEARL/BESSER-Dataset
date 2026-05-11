import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    entities::DomainModel,
    entities::Feature,
    entities::Entity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entities::domainmodel_is_not_abstract():
    assert not inspect.isabstract(entities::DomainModel)


def test_entities::domainmodel_constructor_exists():
    assert callable(entities::DomainModel.__init__)


def test_entities::domainmodel_constructor_args():
    sig = inspect.signature(entities::DomainModel.__init__)
    params = list(sig.parameters.keys())



def test_entities::feature_is_not_abstract():
    assert not inspect.isabstract(entities::Feature)


def test_entities::feature_constructor_exists():
    assert callable(entities::Feature.__init__)


def test_entities::feature_constructor_args():
    sig = inspect.signature(entities::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_entities::feature_has_many():
    assert hasattr(entities::Feature, "many")
    descriptor = None
    for klass in entities::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_entities::feature_has_name():
    assert hasattr(entities::Feature, "name")
    descriptor = None
    for klass in entities::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entities::entity_is_not_abstract():
    assert not inspect.isabstract(entities::Entity)


def test_entities::entity_constructor_exists():
    assert callable(entities::Entity.__init__)


def test_entities::entity_constructor_args():
    sig = inspect.signature(entities::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entities::entity_has_name():
    assert hasattr(entities::Entity, "name")
    descriptor = None
    for klass in entities::Entity.__mro__:
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
entities::DomainModel_strategy = st.builds(
    entities::DomainModel,
)
entities::Feature_strategy = st.builds(
    entities::Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
entities::Entity_strategy = st.builds(
    entities::Entity,
    name=
        safe_text
)

@given(instance=entities::DomainModel_strategy)
@settings(max_examples=50)
def test_entities::domainmodel_instantiation(instance):
    assert isinstance(instance, entities::DomainModel)

@given(instance=entities::Feature_strategy)
@settings(max_examples=50)
def test_entities::feature_instantiation(instance):
    assert isinstance(instance, entities::Feature)

@given(instance=entities::Feature_strategy)
def test_entities::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=entities::Feature_strategy)
def test_entities::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=entities::Feature_strategy)
def test_entities::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entities::Feature_strategy)
def test_entities::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entities::Entity_strategy)
@settings(max_examples=50)
def test_entities::entity_instantiation(instance):
    assert isinstance(instance, entities::Entity)

@given(instance=entities::Entity_strategy)
def test_entities::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entities::Entity_strategy)
def test_entities::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Entity::Entity,
    Entity::System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity::entity_is_not_abstract():
    assert not inspect.isabstract(Entity::Entity)


def test_entity::entity_constructor_exists():
    assert callable(Entity::Entity.__init__)


def test_entity::entity_constructor_args():
    sig = inspect.signature(Entity::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "inDomain" in params, "Missing parameter 'inDomain'"
    assert "name" in params, "Missing parameter 'name'"

def test_entity::entity_has_inDomain():
    assert hasattr(Entity::Entity, "inDomain")
    descriptor = None
    for klass in Entity::Entity.__mro__:
        if "inDomain" in klass.__dict__:
            descriptor = klass.__dict__["inDomain"]
            break
    assert isinstance(descriptor, property)

def test_entity::entity_has_name():
    assert hasattr(Entity::Entity, "name")
    descriptor = None
    for klass in Entity::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity::system_is_not_abstract():
    assert not inspect.isabstract(Entity::System)


def test_entity::system_constructor_exists():
    assert callable(Entity::System.__init__)


def test_entity::system_constructor_args():
    sig = inspect.signature(Entity::System.__init__)
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
Entity::Entity_strategy = st.builds(
    Entity::Entity,
    inDomain=
        safe_text,
    name=
        safe_text
)
Entity::System_strategy = st.builds(
    Entity::System,
)

@given(instance=Entity::Entity_strategy)
@settings(max_examples=50)
def test_entity::entity_instantiation(instance):
    assert isinstance(instance, Entity::Entity)

@given(instance=Entity::Entity_strategy)
def test_entity::entity_inDomain_type(instance):
    assert isinstance(instance.inDomain, str)


@given(instance=Entity::Entity_strategy)
def test_entity::entity_inDomain_setter(instance):
    original = instance.inDomain
    instance.inDomain = original
    assert instance.inDomain == original

@given(instance=Entity::Entity_strategy)
def test_entity::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Entity::Entity_strategy)
def test_entity::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Entity::System_strategy)
@settings(max_examples=50)
def test_entity::system_instantiation(instance):
    assert isinstance(instance, Entity::System)

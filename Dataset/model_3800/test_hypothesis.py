import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    era::Attribute,
    era::Relationship,
    era::Entity,
    era::System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_era::attribute_is_not_abstract():
    assert not inspect.isabstract(era::Attribute)


def test_era::attribute_constructor_exists():
    assert callable(era::Attribute.__init__)


def test_era::attribute_constructor_args():
    sig = inspect.signature(era::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_era::attribute_has_name():
    assert hasattr(era::Attribute, "name")
    descriptor = None
    for klass in era::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_era::relationship_is_not_abstract():
    assert not inspect.isabstract(era::Relationship)


def test_era::relationship_constructor_exists():
    assert callable(era::Relationship.__init__)


def test_era::relationship_constructor_args():
    sig = inspect.signature(era::Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_era::relationship_has_name():
    assert hasattr(era::Relationship, "name")
    descriptor = None
    for klass in era::Relationship.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_era::entity_is_not_abstract():
    assert not inspect.isabstract(era::Entity)


def test_era::entity_constructor_exists():
    assert callable(era::Entity.__init__)


def test_era::entity_constructor_args():
    sig = inspect.signature(era::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "inDomain" in params, "Missing parameter 'inDomain'"

def test_era::entity_has_name():
    assert hasattr(era::Entity, "name")
    descriptor = None
    for klass in era::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_era::entity_has_inDomain():
    assert hasattr(era::Entity, "inDomain")
    descriptor = None
    for klass in era::Entity.__mro__:
        if "inDomain" in klass.__dict__:
            descriptor = klass.__dict__["inDomain"]
            break
    assert isinstance(descriptor, property)



def test_era::system_is_not_abstract():
    assert not inspect.isabstract(era::System)


def test_era::system_constructor_exists():
    assert callable(era::System.__init__)


def test_era::system_constructor_args():
    sig = inspect.signature(era::System.__init__)
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
era::Attribute_strategy = st.builds(
    era::Attribute,
    name=
        safe_text
)
era::Relationship_strategy = st.builds(
    era::Relationship,
    name=
        safe_text
)
era::Entity_strategy = st.builds(
    era::Entity,
    name=
        safe_text,
    inDomain=
        safe_text
)
era::System_strategy = st.builds(
    era::System,
)

@given(instance=era::Attribute_strategy)
@settings(max_examples=50)
def test_era::attribute_instantiation(instance):
    assert isinstance(instance, era::Attribute)

@given(instance=era::Attribute_strategy)
def test_era::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=era::Attribute_strategy)
def test_era::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=era::Relationship_strategy)
@settings(max_examples=50)
def test_era::relationship_instantiation(instance):
    assert isinstance(instance, era::Relationship)

@given(instance=era::Relationship_strategy)
def test_era::relationship_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=era::Relationship_strategy)
def test_era::relationship_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=era::Entity_strategy)
@settings(max_examples=50)
def test_era::entity_instantiation(instance):
    assert isinstance(instance, era::Entity)

@given(instance=era::Entity_strategy)
def test_era::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=era::Entity_strategy)
def test_era::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=era::Entity_strategy)
def test_era::entity_inDomain_type(instance):
    assert isinstance(instance.inDomain, str)


@given(instance=era::Entity_strategy)
def test_era::entity_inDomain_setter(instance):
    original = instance.inDomain
    instance.inDomain = original
    assert instance.inDomain == original

@given(instance=era::System_strategy)
@settings(max_examples=50)
def test_era::system_instantiation(instance):
    assert isinstance(instance, era::System)

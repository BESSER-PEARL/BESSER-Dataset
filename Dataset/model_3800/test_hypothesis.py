import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    era_Attribute,
    era_Relationship,
    era_Entity,
    era_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_era_attribute_is_not_abstract():
    assert not inspect.isabstract(era_Attribute)


def test_era_attribute_constructor_exists():
    assert callable(era_Attribute.__init__)


def test_era_attribute_constructor_args():
    sig = inspect.signature(era_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_era_attribute_has_name():
    assert hasattr(era_Attribute, "name")
    descriptor = None
    for klass in era_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_era_relationship_is_not_abstract():
    assert not inspect.isabstract(era_Relationship)


def test_era_relationship_constructor_exists():
    assert callable(era_Relationship.__init__)


def test_era_relationship_constructor_args():
    sig = inspect.signature(era_Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_era_relationship_has_name():
    assert hasattr(era_Relationship, "name")
    descriptor = None
    for klass in era_Relationship.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_era_entity_is_not_abstract():
    assert not inspect.isabstract(era_Entity)


def test_era_entity_constructor_exists():
    assert callable(era_Entity.__init__)


def test_era_entity_constructor_args():
    sig = inspect.signature(era_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "inDomain" in params, "Missing parameter 'inDomain'"
    assert "name" in params, "Missing parameter 'name'"

def test_era_entity_has_inDomain():
    assert hasattr(era_Entity, "inDomain")
    descriptor = None
    for klass in era_Entity.__mro__:
        if "inDomain" in klass.__dict__:
            descriptor = klass.__dict__["inDomain"]
            break
    assert isinstance(descriptor, property)

def test_era_entity_has_name():
    assert hasattr(era_Entity, "name")
    descriptor = None
    for klass in era_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_era_system_is_not_abstract():
    assert not inspect.isabstract(era_System)


def test_era_system_constructor_exists():
    assert callable(era_System.__init__)


def test_era_system_constructor_args():
    sig = inspect.signature(era_System.__init__)
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
era_Attribute_strategy = st.builds(
    era_Attribute,
    name=
        safe_text
)
era_Relationship_strategy = st.builds(
    era_Relationship,
    name=
        safe_text
)
era_Entity_strategy = st.builds(
    era_Entity,
    inDomain=
        safe_text,
    name=
        safe_text
)
era_System_strategy = st.builds(
    era_System,
)

@given(instance=era_Attribute_strategy)
@settings(max_examples=50)
def test_era_attribute_instantiation(instance):
    assert isinstance(instance, era_Attribute)



@given(instance=era_Attribute_strategy)
def test_era_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=era_Relationship_strategy)
@settings(max_examples=50)
def test_era_relationship_instantiation(instance):
    assert isinstance(instance, era_Relationship)



@given(instance=era_Relationship_strategy)
def test_era_relationship_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=era_Entity_strategy)
@settings(max_examples=50)
def test_era_entity_instantiation(instance):
    assert isinstance(instance, era_Entity)



@given(instance=era_Entity_strategy)
def test_era_entity_inDomain_setter(instance):
    original = instance.inDomain
    instance.inDomain = original
    assert instance.inDomain == original



@given(instance=era_Entity_strategy)
def test_era_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=era_System_strategy)
@settings(max_examples=50)
def test_era_system_instantiation(instance):
    assert isinstance(instance, era_System)

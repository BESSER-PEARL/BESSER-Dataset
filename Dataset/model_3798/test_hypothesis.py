import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Entity_Entity,
    Entity_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity_entity_is_not_abstract():
    assert not inspect.isabstract(Entity_Entity)


def test_entity_entity_constructor_exists():
    assert callable(Entity_Entity.__init__)


def test_entity_entity_constructor_args():
    sig = inspect.signature(Entity_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "inDomain" in params, "Missing parameter 'inDomain'"

def test_entity_entity_has_name():
    assert hasattr(Entity_Entity, "name")
    descriptor = None
    for klass in Entity_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_entity_entity_has_inDomain():
    assert hasattr(Entity_Entity, "inDomain")
    descriptor = None
    for klass in Entity_Entity.__mro__:
        if "inDomain" in klass.__dict__:
            descriptor = klass.__dict__["inDomain"]
            break
    assert isinstance(descriptor, property)



def test_entity_system_is_not_abstract():
    assert not inspect.isabstract(Entity_System)


def test_entity_system_constructor_exists():
    assert callable(Entity_System.__init__)


def test_entity_system_constructor_args():
    sig = inspect.signature(Entity_System.__init__)
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
Entity_Entity_strategy = st.builds(
    Entity_Entity,
    name=
        safe_text,
    inDomain=
        safe_text
)
Entity_System_strategy = st.builds(
    Entity_System,
)

@given(instance=Entity_Entity_strategy)
@settings(max_examples=50)
def test_entity_entity_instantiation(instance):
    assert isinstance(instance, Entity_Entity)



@given(instance=Entity_Entity_strategy)
def test_entity_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Entity_Entity_strategy)
def test_entity_entity_inDomain_setter(instance):
    original = instance.inDomain
    instance.inDomain = original
    assert instance.inDomain == original

@given(instance=Entity_System_strategy)
@settings(max_examples=50)
def test_entity_system_instantiation(instance):
    assert isinstance(instance, Entity_System)

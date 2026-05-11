import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    panamaNeo4j::Entity,
    panamaNeo4j::Officer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_panamaneo4j::entity_is_not_abstract():
    assert not inspect.isabstract(panamaNeo4j::Entity)


def test_panamaneo4j::entity_constructor_exists():
    assert callable(panamaNeo4j::Entity.__init__)


def test_panamaneo4j::entity_constructor_args():
    sig = inspect.signature(panamaNeo4j::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_panamaneo4j::entity_has_name():
    assert hasattr(panamaNeo4j::Entity, "name")
    descriptor = None
    for klass in panamaNeo4j::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_panamaneo4j::officer_is_not_abstract():
    assert not inspect.isabstract(panamaNeo4j::Officer)


def test_panamaneo4j::officer_constructor_exists():
    assert callable(panamaNeo4j::Officer.__init__)


def test_panamaneo4j::officer_constructor_args():
    sig = inspect.signature(panamaNeo4j::Officer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_panamaneo4j::officer_has_name():
    assert hasattr(panamaNeo4j::Officer, "name")
    descriptor = None
    for klass in panamaNeo4j::Officer.__mro__:
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
panamaNeo4j::Entity_strategy = st.builds(
    panamaNeo4j::Entity,
    name=
        safe_text
)
panamaNeo4j::Officer_strategy = st.builds(
    panamaNeo4j::Officer,
    name=
        safe_text
)

@given(instance=panamaNeo4j::Entity_strategy)
@settings(max_examples=50)
def test_panamaneo4j::entity_instantiation(instance):
    assert isinstance(instance, panamaNeo4j::Entity)

@given(instance=panamaNeo4j::Entity_strategy)
def test_panamaneo4j::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=panamaNeo4j::Entity_strategy)
def test_panamaneo4j::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=panamaNeo4j::Officer_strategy)
@settings(max_examples=50)
def test_panamaneo4j::officer_instantiation(instance):
    assert isinstance(instance, panamaNeo4j::Officer)

@given(instance=panamaNeo4j::Officer_strategy)
def test_panamaneo4j::officer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=panamaNeo4j::Officer_strategy)
def test_panamaneo4j::officer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

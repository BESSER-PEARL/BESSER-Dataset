import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleworld::NamedElement,
    NamedElement,
    simpleworld::RelatedTo,
    simpleworld::Thing,
    simpleworld::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleworld::namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleworld::NamedElement)


def test_simpleworld::namedelement_constructor_exists():
    assert callable(simpleworld::NamedElement.__init__)


def test_simpleworld::namedelement_constructor_args():
    sig = inspect.signature(simpleworld::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleworld::namedelement_has_name():
    assert hasattr(simpleworld::NamedElement, "name")
    descriptor = None
    for klass in simpleworld::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleworld::relatedto_is_not_abstract():
    assert not inspect.isabstract(simpleworld::RelatedTo)


def test_simpleworld::relatedto_constructor_exists():
    assert callable(simpleworld::RelatedTo.__init__)


def test_simpleworld::relatedto_constructor_args():
    sig = inspect.signature(simpleworld::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_simpleworld::relatedto_has_since():
    assert hasattr(simpleworld::RelatedTo, "since")
    descriptor = None
    for klass in simpleworld::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_simpleworld::thing_is_not_abstract():
    assert not inspect.isabstract(simpleworld::Thing)


def test_simpleworld::thing_constructor_exists():
    assert callable(simpleworld::Thing.__init__)


def test_simpleworld::thing_constructor_args():
    sig = inspect.signature(simpleworld::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_simpleworld::thing_has_id():
    assert hasattr(simpleworld::Thing, "id")
    descriptor = None
    for klass in simpleworld::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_simpleworld::world_is_not_abstract():
    assert not inspect.isabstract(simpleworld::World)


def test_simpleworld::world_constructor_exists():
    assert callable(simpleworld::World.__init__)


def test_simpleworld::world_constructor_args():
    sig = inspect.signature(simpleworld::World.__init__)
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
simpleworld::NamedElement_strategy = st.builds(
    simpleworld::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleworld::RelatedTo_strategy = st.builds(
    simpleworld::RelatedTo,
    since=
        safe_text
)
simpleworld::Thing_strategy = st.builds(
    simpleworld::Thing,
    id=
        st.integers()
)
simpleworld::World_strategy = st.builds(
    simpleworld::World,
)

@given(instance=simpleworld::NamedElement_strategy)
@settings(max_examples=50)
def test_simpleworld::namedelement_instantiation(instance):
    assert isinstance(instance, simpleworld::NamedElement)

@given(instance=simpleworld::NamedElement_strategy)
def test_simpleworld::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleworld::NamedElement_strategy)
def test_simpleworld::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleworld::RelatedTo_strategy)
@settings(max_examples=50)
def test_simpleworld::relatedto_instantiation(instance):
    assert isinstance(instance, simpleworld::RelatedTo)

@given(instance=simpleworld::RelatedTo_strategy)
def test_simpleworld::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=simpleworld::RelatedTo_strategy)
def test_simpleworld::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=simpleworld::Thing_strategy)
@settings(max_examples=50)
def test_simpleworld::thing_instantiation(instance):
    assert isinstance(instance, simpleworld::Thing)

@given(instance=simpleworld::Thing_strategy)
def test_simpleworld::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=simpleworld::Thing_strategy)
def test_simpleworld::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=simpleworld::World_strategy)
@settings(max_examples=50)
def test_simpleworld::world_instantiation(instance):
    assert isinstance(instance, simpleworld::World)

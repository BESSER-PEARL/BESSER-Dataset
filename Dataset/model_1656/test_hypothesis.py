import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    error4::NamedElement,
    error4::World,
    NamedElement,
    error4::Component,
    error4::RelatedTo,
    error4::Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_error4::namedelement_is_not_abstract():
    assert not inspect.isabstract(error4::NamedElement)


def test_error4::namedelement_constructor_exists():
    assert callable(error4::NamedElement.__init__)


def test_error4::namedelement_constructor_args():
    sig = inspect.signature(error4::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_error4::namedelement_has_name():
    assert hasattr(error4::NamedElement, "name")
    descriptor = None
    for klass in error4::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_error4::world_is_not_abstract():
    assert not inspect.isabstract(error4::World)


def test_error4::world_constructor_exists():
    assert callable(error4::World.__init__)


def test_error4::world_constructor_args():
    sig = inspect.signature(error4::World.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_error4::component_is_not_abstract():
    assert not inspect.isabstract(error4::Component)


def test_error4::component_constructor_exists():
    assert callable(error4::Component.__init__)


def test_error4::component_constructor_args():
    sig = inspect.signature(error4::Component.__init__)
    params = list(sig.parameters.keys())



def test_error4::relatedto_is_not_abstract():
    assert not inspect.isabstract(error4::RelatedTo)


def test_error4::relatedto_constructor_exists():
    assert callable(error4::RelatedTo.__init__)


def test_error4::relatedto_constructor_args():
    sig = inspect.signature(error4::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_error4::relatedto_has_since():
    assert hasattr(error4::RelatedTo, "since")
    descriptor = None
    for klass in error4::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_error4::thing_is_not_abstract():
    assert not inspect.isabstract(error4::Thing)


def test_error4::thing_constructor_exists():
    assert callable(error4::Thing.__init__)


def test_error4::thing_constructor_args():
    sig = inspect.signature(error4::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_error4::thing_has_id():
    assert hasattr(error4::Thing, "id")
    descriptor = None
    for klass in error4::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
error4::NamedElement_strategy = st.builds(
    error4::NamedElement,
    name=
        safe_text
)
error4::World_strategy = st.builds(
    error4::World,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
error4::Component_strategy = st.builds(
    error4::Component,
)
error4::RelatedTo_strategy = st.builds(
    error4::RelatedTo,
    since=
        safe_text
)
error4::Thing_strategy = st.builds(
    error4::Thing,
    id=
        st.integers()
)

@given(instance=error4::NamedElement_strategy)
@settings(max_examples=50)
def test_error4::namedelement_instantiation(instance):
    assert isinstance(instance, error4::NamedElement)

@given(instance=error4::NamedElement_strategy)
def test_error4::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=error4::NamedElement_strategy)
def test_error4::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=error4::World_strategy)
@settings(max_examples=50)
def test_error4::world_instantiation(instance):
    assert isinstance(instance, error4::World)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=error4::Component_strategy)
@settings(max_examples=50)
def test_error4::component_instantiation(instance):
    assert isinstance(instance, error4::Component)

@given(instance=error4::RelatedTo_strategy)
@settings(max_examples=50)
def test_error4::relatedto_instantiation(instance):
    assert isinstance(instance, error4::RelatedTo)

@given(instance=error4::RelatedTo_strategy)
def test_error4::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=error4::RelatedTo_strategy)
def test_error4::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=error4::Thing_strategy)
@settings(max_examples=50)
def test_error4::thing_instantiation(instance):
    assert isinstance(instance, error4::Thing)

@given(instance=error4::Thing_strategy)
def test_error4::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=error4::Thing_strategy)
def test_error4::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

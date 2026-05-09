import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    helloworld123::Alias,
    helloworld123::World,
    helloworld123::NamedElement,
    NamedElement,
    helloworld123::Thing,
    helloworld123::RelatedTo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld123::alias_is_not_abstract():
    assert not inspect.isabstract(helloworld123::Alias)


def test_helloworld123::alias_constructor_exists():
    assert callable(helloworld123::Alias.__init__)


def test_helloworld123::alias_constructor_args():
    sig = inspect.signature(helloworld123::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_helloworld123::alias_has_id():
    assert hasattr(helloworld123::Alias, "id")
    descriptor = None
    for klass in helloworld123::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_helloworld123::world_is_not_abstract():
    assert not inspect.isabstract(helloworld123::World)


def test_helloworld123::world_constructor_exists():
    assert callable(helloworld123::World.__init__)


def test_helloworld123::world_constructor_args():
    sig = inspect.signature(helloworld123::World.__init__)
    params = list(sig.parameters.keys())



def test_helloworld123::namedelement_is_not_abstract():
    assert not inspect.isabstract(helloworld123::NamedElement)


def test_helloworld123::namedelement_constructor_exists():
    assert callable(helloworld123::NamedElement.__init__)


def test_helloworld123::namedelement_constructor_args():
    sig = inspect.signature(helloworld123::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld123::namedelement_has_name():
    assert hasattr(helloworld123::NamedElement, "name")
    descriptor = None
    for klass in helloworld123::NamedElement.__mro__:
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



def test_helloworld123::thing_is_not_abstract():
    assert not inspect.isabstract(helloworld123::Thing)


def test_helloworld123::thing_constructor_exists():
    assert callable(helloworld123::Thing.__init__)


def test_helloworld123::thing_constructor_args():
    sig = inspect.signature(helloworld123::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_helloworld123::thing_has_id():
    assert hasattr(helloworld123::Thing, "id")
    descriptor = None
    for klass in helloworld123::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_helloworld123::relatedto_is_not_abstract():
    assert not inspect.isabstract(helloworld123::RelatedTo)


def test_helloworld123::relatedto_constructor_exists():
    assert callable(helloworld123::RelatedTo.__init__)


def test_helloworld123::relatedto_constructor_args():
    sig = inspect.signature(helloworld123::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_helloworld123::relatedto_has_since():
    assert hasattr(helloworld123::RelatedTo, "since")
    descriptor = None
    for klass in helloworld123::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
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
helloworld123::Alias_strategy = st.builds(
    helloworld123::Alias,
    id=
        safe_text
)
helloworld123::World_strategy = st.builds(
    helloworld123::World,
)
helloworld123::NamedElement_strategy = st.builds(
    helloworld123::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
helloworld123::Thing_strategy = st.builds(
    helloworld123::Thing,
    id=
        st.integers()
)
helloworld123::RelatedTo_strategy = st.builds(
    helloworld123::RelatedTo,
    since=
        safe_text
)

@given(instance=helloworld123::Alias_strategy)
@settings(max_examples=50)
def test_helloworld123::alias_instantiation(instance):
    assert isinstance(instance, helloworld123::Alias)

@given(instance=helloworld123::Alias_strategy)
def test_helloworld123::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=helloworld123::Alias_strategy)
def test_helloworld123::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=helloworld123::World_strategy)
@settings(max_examples=50)
def test_helloworld123::world_instantiation(instance):
    assert isinstance(instance, helloworld123::World)

@given(instance=helloworld123::NamedElement_strategy)
@settings(max_examples=50)
def test_helloworld123::namedelement_instantiation(instance):
    assert isinstance(instance, helloworld123::NamedElement)

@given(instance=helloworld123::NamedElement_strategy)
def test_helloworld123::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloworld123::NamedElement_strategy)
def test_helloworld123::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=helloworld123::Thing_strategy)
@settings(max_examples=50)
def test_helloworld123::thing_instantiation(instance):
    assert isinstance(instance, helloworld123::Thing)

@given(instance=helloworld123::Thing_strategy)
def test_helloworld123::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=helloworld123::Thing_strategy)
def test_helloworld123::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=helloworld123::RelatedTo_strategy)
@settings(max_examples=50)
def test_helloworld123::relatedto_instantiation(instance):
    assert isinstance(instance, helloworld123::RelatedTo)

@given(instance=helloworld123::RelatedTo_strategy)
def test_helloworld123::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=helloworld123::RelatedTo_strategy)
def test_helloworld123::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

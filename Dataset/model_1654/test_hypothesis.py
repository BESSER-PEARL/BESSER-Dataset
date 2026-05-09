import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    yyaa::Alias,
    yyaa::NamedElement,
    NamedElement,
    yyaa::RelatedTo,
    yyaa::Thing,
    yyaa::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yyaa::alias_is_not_abstract():
    assert not inspect.isabstract(yyaa::Alias)


def test_yyaa::alias_constructor_exists():
    assert callable(yyaa::Alias.__init__)


def test_yyaa::alias_constructor_args():
    sig = inspect.signature(yyaa::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyaa::alias_has_id():
    assert hasattr(yyaa::Alias, "id")
    descriptor = None
    for klass in yyaa::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyaa::namedelement_is_not_abstract():
    assert not inspect.isabstract(yyaa::NamedElement)


def test_yyaa::namedelement_constructor_exists():
    assert callable(yyaa::NamedElement.__init__)


def test_yyaa::namedelement_constructor_args():
    sig = inspect.signature(yyaa::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yyaa::namedelement_has_name():
    assert hasattr(yyaa::NamedElement, "name")
    descriptor = None
    for klass in yyaa::NamedElement.__mro__:
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



def test_yyaa::relatedto_is_not_abstract():
    assert not inspect.isabstract(yyaa::RelatedTo)


def test_yyaa::relatedto_constructor_exists():
    assert callable(yyaa::RelatedTo.__init__)


def test_yyaa::relatedto_constructor_args():
    sig = inspect.signature(yyaa::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyaa::relatedto_has_since():
    assert hasattr(yyaa::RelatedTo, "since")
    descriptor = None
    for klass in yyaa::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyaa::thing_is_not_abstract():
    assert not inspect.isabstract(yyaa::Thing)


def test_yyaa::thing_constructor_exists():
    assert callable(yyaa::Thing.__init__)


def test_yyaa::thing_constructor_args():
    sig = inspect.signature(yyaa::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyaa::thing_has_id():
    assert hasattr(yyaa::Thing, "id")
    descriptor = None
    for klass in yyaa::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyaa::world_is_not_abstract():
    assert not inspect.isabstract(yyaa::World)


def test_yyaa::world_constructor_exists():
    assert callable(yyaa::World.__init__)


def test_yyaa::world_constructor_args():
    sig = inspect.signature(yyaa::World.__init__)
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
yyaa::Alias_strategy = st.builds(
    yyaa::Alias,
    id=
        safe_text
)
yyaa::NamedElement_strategy = st.builds(
    yyaa::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yyaa::RelatedTo_strategy = st.builds(
    yyaa::RelatedTo,
    since=
        safe_text
)
yyaa::Thing_strategy = st.builds(
    yyaa::Thing,
    id=
        st.integers()
)
yyaa::World_strategy = st.builds(
    yyaa::World,
)

@given(instance=yyaa::Alias_strategy)
@settings(max_examples=50)
def test_yyaa::alias_instantiation(instance):
    assert isinstance(instance, yyaa::Alias)

@given(instance=yyaa::Alias_strategy)
def test_yyaa::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyaa::Alias_strategy)
def test_yyaa::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyaa::NamedElement_strategy)
@settings(max_examples=50)
def test_yyaa::namedelement_instantiation(instance):
    assert isinstance(instance, yyaa::NamedElement)

@given(instance=yyaa::NamedElement_strategy)
def test_yyaa::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=yyaa::NamedElement_strategy)
def test_yyaa::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yyaa::RelatedTo_strategy)
@settings(max_examples=50)
def test_yyaa::relatedto_instantiation(instance):
    assert isinstance(instance, yyaa::RelatedTo)

@given(instance=yyaa::RelatedTo_strategy)
def test_yyaa::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=yyaa::RelatedTo_strategy)
def test_yyaa::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyaa::Thing_strategy)
@settings(max_examples=50)
def test_yyaa::thing_instantiation(instance):
    assert isinstance(instance, yyaa::Thing)

@given(instance=yyaa::Thing_strategy)
def test_yyaa::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=yyaa::Thing_strategy)
def test_yyaa::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyaa::World_strategy)
@settings(max_examples=50)
def test_yyaa::world_instantiation(instance):
    assert isinstance(instance, yyaa::World)

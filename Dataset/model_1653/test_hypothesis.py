import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    errya::Alias,
    errya::NamedElement,
    NamedElement,
    errya::RelatedTo,
    errya::Thing,
    errya::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_errya::alias_is_not_abstract():
    assert not inspect.isabstract(errya::Alias)


def test_errya::alias_constructor_exists():
    assert callable(errya::Alias.__init__)


def test_errya::alias_constructor_args():
    sig = inspect.signature(errya::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_errya::alias_has_id():
    assert hasattr(errya::Alias, "id")
    descriptor = None
    for klass in errya::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_errya::namedelement_is_not_abstract():
    assert not inspect.isabstract(errya::NamedElement)


def test_errya::namedelement_constructor_exists():
    assert callable(errya::NamedElement.__init__)


def test_errya::namedelement_constructor_args():
    sig = inspect.signature(errya::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_errya::namedelement_has_name():
    assert hasattr(errya::NamedElement, "name")
    descriptor = None
    for klass in errya::NamedElement.__mro__:
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



def test_errya::relatedto_is_not_abstract():
    assert not inspect.isabstract(errya::RelatedTo)


def test_errya::relatedto_constructor_exists():
    assert callable(errya::RelatedTo.__init__)


def test_errya::relatedto_constructor_args():
    sig = inspect.signature(errya::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_errya::relatedto_has_since():
    assert hasattr(errya::RelatedTo, "since")
    descriptor = None
    for klass in errya::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_errya::thing_is_not_abstract():
    assert not inspect.isabstract(errya::Thing)


def test_errya::thing_constructor_exists():
    assert callable(errya::Thing.__init__)


def test_errya::thing_constructor_args():
    sig = inspect.signature(errya::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_errya::thing_has_id():
    assert hasattr(errya::Thing, "id")
    descriptor = None
    for klass in errya::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_errya::world_is_not_abstract():
    assert not inspect.isabstract(errya::World)


def test_errya::world_constructor_exists():
    assert callable(errya::World.__init__)


def test_errya::world_constructor_args():
    sig = inspect.signature(errya::World.__init__)
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
errya::Alias_strategy = st.builds(
    errya::Alias,
    id=
        safe_text
)
errya::NamedElement_strategy = st.builds(
    errya::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
errya::RelatedTo_strategy = st.builds(
    errya::RelatedTo,
    since=
        safe_text
)
errya::Thing_strategy = st.builds(
    errya::Thing,
    id=
        st.integers()
)
errya::World_strategy = st.builds(
    errya::World,
)

@given(instance=errya::Alias_strategy)
@settings(max_examples=50)
def test_errya::alias_instantiation(instance):
    assert isinstance(instance, errya::Alias)

@given(instance=errya::Alias_strategy)
def test_errya::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=errya::Alias_strategy)
def test_errya::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=errya::NamedElement_strategy)
@settings(max_examples=50)
def test_errya::namedelement_instantiation(instance):
    assert isinstance(instance, errya::NamedElement)

@given(instance=errya::NamedElement_strategy)
def test_errya::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=errya::NamedElement_strategy)
def test_errya::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=errya::RelatedTo_strategy)
@settings(max_examples=50)
def test_errya::relatedto_instantiation(instance):
    assert isinstance(instance, errya::RelatedTo)

@given(instance=errya::RelatedTo_strategy)
def test_errya::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=errya::RelatedTo_strategy)
def test_errya::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=errya::Thing_strategy)
@settings(max_examples=50)
def test_errya::thing_instantiation(instance):
    assert isinstance(instance, errya::Thing)

@given(instance=errya::Thing_strategy)
def test_errya::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=errya::Thing_strategy)
def test_errya::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=errya::World_strategy)
@settings(max_examples=50)
def test_errya::world_instantiation(instance):
    assert isinstance(instance, errya::World)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    yya::Alias,
    yya::NamedElement,
    NamedElement,
    yya::RelatedTo,
    yya::Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yya::alias_is_not_abstract():
    assert not inspect.isabstract(yya::Alias)


def test_yya::alias_constructor_exists():
    assert callable(yya::Alias.__init__)


def test_yya::alias_constructor_args():
    sig = inspect.signature(yya::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yya::alias_has_id():
    assert hasattr(yya::Alias, "id")
    descriptor = None
    for klass in yya::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yya::namedelement_is_not_abstract():
    assert not inspect.isabstract(yya::NamedElement)


def test_yya::namedelement_constructor_exists():
    assert callable(yya::NamedElement.__init__)


def test_yya::namedelement_constructor_args():
    sig = inspect.signature(yya::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yya::namedelement_has_name():
    assert hasattr(yya::NamedElement, "name")
    descriptor = None
    for klass in yya::NamedElement.__mro__:
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



def test_yya::relatedto_is_not_abstract():
    assert not inspect.isabstract(yya::RelatedTo)


def test_yya::relatedto_constructor_exists():
    assert callable(yya::RelatedTo.__init__)


def test_yya::relatedto_constructor_args():
    sig = inspect.signature(yya::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yya::relatedto_has_since():
    assert hasattr(yya::RelatedTo, "since")
    descriptor = None
    for klass in yya::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yya::thing_is_not_abstract():
    assert not inspect.isabstract(yya::Thing)


def test_yya::thing_constructor_exists():
    assert callable(yya::Thing.__init__)


def test_yya::thing_constructor_args():
    sig = inspect.signature(yya::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yya::thing_has_id():
    assert hasattr(yya::Thing, "id")
    descriptor = None
    for klass in yya::Thing.__mro__:
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
yya::Alias_strategy = st.builds(
    yya::Alias,
    id=
        safe_text
)
yya::NamedElement_strategy = st.builds(
    yya::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yya::RelatedTo_strategy = st.builds(
    yya::RelatedTo,
    since=
        safe_text
)
yya::Thing_strategy = st.builds(
    yya::Thing,
    id=
        st.integers()
)

@given(instance=yya::Alias_strategy)
@settings(max_examples=50)
def test_yya::alias_instantiation(instance):
    assert isinstance(instance, yya::Alias)

@given(instance=yya::Alias_strategy)
def test_yya::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yya::Alias_strategy)
def test_yya::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yya::NamedElement_strategy)
@settings(max_examples=50)
def test_yya::namedelement_instantiation(instance):
    assert isinstance(instance, yya::NamedElement)

@given(instance=yya::NamedElement_strategy)
def test_yya::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=yya::NamedElement_strategy)
def test_yya::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yya::RelatedTo_strategy)
@settings(max_examples=50)
def test_yya::relatedto_instantiation(instance):
    assert isinstance(instance, yya::RelatedTo)

@given(instance=yya::RelatedTo_strategy)
def test_yya::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=yya::RelatedTo_strategy)
def test_yya::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yya::Thing_strategy)
@settings(max_examples=50)
def test_yya::thing_instantiation(instance):
    assert isinstance(instance, yya::Thing)

@given(instance=yya::Thing_strategy)
def test_yya::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=yya::Thing_strategy)
def test_yya::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

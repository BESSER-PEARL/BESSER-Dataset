import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mpupkb::Comment,
    mpupkb::NamedElement,
    NamedElement,
    mpupkb::Own,
    mpupkb::Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mpupkb::comment_is_not_abstract():
    assert not inspect.isabstract(mpupkb::Comment)


def test_mpupkb::comment_constructor_exists():
    assert callable(mpupkb::Comment.__init__)


def test_mpupkb::comment_constructor_args():
    sig = inspect.signature(mpupkb::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_mpupkb::comment_has_content():
    assert hasattr(mpupkb::Comment, "content")
    descriptor = None
    for klass in mpupkb::Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_mpupkb::namedelement_is_not_abstract():
    assert not inspect.isabstract(mpupkb::NamedElement)


def test_mpupkb::namedelement_constructor_exists():
    assert callable(mpupkb::NamedElement.__init__)


def test_mpupkb::namedelement_constructor_args():
    sig = inspect.signature(mpupkb::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mpupkb::namedelement_has_name():
    assert hasattr(mpupkb::NamedElement, "name")
    descriptor = None
    for klass in mpupkb::NamedElement.__mro__:
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



def test_mpupkb::own_is_not_abstract():
    assert not inspect.isabstract(mpupkb::Own)


def test_mpupkb::own_constructor_exists():
    assert callable(mpupkb::Own.__init__)


def test_mpupkb::own_constructor_args():
    sig = inspect.signature(mpupkb::Own.__init__)
    params = list(sig.parameters.keys())
    assert "ownerName" in params, "Missing parameter 'ownerName'"
    assert "since" in params, "Missing parameter 'since'"

def test_mpupkb::own_has_ownerName():
    assert hasattr(mpupkb::Own, "ownerName")
    descriptor = None
    for klass in mpupkb::Own.__mro__:
        if "ownerName" in klass.__dict__:
            descriptor = klass.__dict__["ownerName"]
            break
    assert isinstance(descriptor, property)

def test_mpupkb::own_has_since():
    assert hasattr(mpupkb::Own, "since")
    descriptor = None
    for klass in mpupkb::Own.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_mpupkb::thing_is_not_abstract():
    assert not inspect.isabstract(mpupkb::Thing)


def test_mpupkb::thing_constructor_exists():
    assert callable(mpupkb::Thing.__init__)


def test_mpupkb::thing_constructor_args():
    sig = inspect.signature(mpupkb::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mpupkb::thing_has_id():
    assert hasattr(mpupkb::Thing, "id")
    descriptor = None
    for klass in mpupkb::Thing.__mro__:
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
mpupkb::Comment_strategy = st.builds(
    mpupkb::Comment,
    content=
        safe_text
)
mpupkb::NamedElement_strategy = st.builds(
    mpupkb::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
mpupkb::Own_strategy = st.builds(
    mpupkb::Own,
    ownerName=
        safe_text,
    since=
        safe_text
)
mpupkb::Thing_strategy = st.builds(
    mpupkb::Thing,
    id=
        st.integers()
)

@given(instance=mpupkb::Comment_strategy)
@settings(max_examples=50)
def test_mpupkb::comment_instantiation(instance):
    assert isinstance(instance, mpupkb::Comment)

@given(instance=mpupkb::Comment_strategy)
def test_mpupkb::comment_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=mpupkb::Comment_strategy)
def test_mpupkb::comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=mpupkb::NamedElement_strategy)
@settings(max_examples=50)
def test_mpupkb::namedelement_instantiation(instance):
    assert isinstance(instance, mpupkb::NamedElement)

@given(instance=mpupkb::NamedElement_strategy)
def test_mpupkb::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mpupkb::NamedElement_strategy)
def test_mpupkb::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=mpupkb::Own_strategy)
@settings(max_examples=50)
def test_mpupkb::own_instantiation(instance):
    assert isinstance(instance, mpupkb::Own)

@given(instance=mpupkb::Own_strategy)
def test_mpupkb::own_ownerName_type(instance):
    assert isinstance(instance.ownerName, str)


@given(instance=mpupkb::Own_strategy)
def test_mpupkb::own_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original

@given(instance=mpupkb::Own_strategy)
def test_mpupkb::own_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=mpupkb::Own_strategy)
def test_mpupkb::own_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=mpupkb::Thing_strategy)
@settings(max_examples=50)
def test_mpupkb::thing_instantiation(instance):
    assert isinstance(instance, mpupkb::Thing)

@given(instance=mpupkb::Thing_strategy)
def test_mpupkb::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=mpupkb::Thing_strategy)
def test_mpupkb::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

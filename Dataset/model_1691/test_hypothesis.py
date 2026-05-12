import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mpupkb_Comment,
    mpupkb_NamedElement,
    NamedElement,
    mpupkb_Own,
    mpupkb_Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mpupkb_comment_is_not_abstract():
    assert not inspect.isabstract(mpupkb_Comment)


def test_mpupkb_comment_constructor_exists():
    assert callable(mpupkb_Comment.__init__)


def test_mpupkb_comment_constructor_args():
    sig = inspect.signature(mpupkb_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_mpupkb_comment_has_content():
    assert hasattr(mpupkb_Comment, "content")
    descriptor = None
    for klass in mpupkb_Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_mpupkb_namedelement_is_not_abstract():
    assert not inspect.isabstract(mpupkb_NamedElement)


def test_mpupkb_namedelement_constructor_exists():
    assert callable(mpupkb_NamedElement.__init__)


def test_mpupkb_namedelement_constructor_args():
    sig = inspect.signature(mpupkb_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mpupkb_namedelement_has_name():
    assert hasattr(mpupkb_NamedElement, "name")
    descriptor = None
    for klass in mpupkb_NamedElement.__mro__:
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



def test_mpupkb_own_is_not_abstract():
    assert not inspect.isabstract(mpupkb_Own)


def test_mpupkb_own_constructor_exists():
    assert callable(mpupkb_Own.__init__)


def test_mpupkb_own_constructor_args():
    sig = inspect.signature(mpupkb_Own.__init__)
    params = list(sig.parameters.keys())
    assert "ownerName" in params, "Missing parameter 'ownerName'"
    assert "since" in params, "Missing parameter 'since'"

def test_mpupkb_own_has_ownerName():
    assert hasattr(mpupkb_Own, "ownerName")
    descriptor = None
    for klass in mpupkb_Own.__mro__:
        if "ownerName" in klass.__dict__:
            descriptor = klass.__dict__["ownerName"]
            break
    assert isinstance(descriptor, property)

def test_mpupkb_own_has_since():
    assert hasattr(mpupkb_Own, "since")
    descriptor = None
    for klass in mpupkb_Own.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_mpupkb_thing_is_not_abstract():
    assert not inspect.isabstract(mpupkb_Thing)


def test_mpupkb_thing_constructor_exists():
    assert callable(mpupkb_Thing.__init__)


def test_mpupkb_thing_constructor_args():
    sig = inspect.signature(mpupkb_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mpupkb_thing_has_id():
    assert hasattr(mpupkb_Thing, "id")
    descriptor = None
    for klass in mpupkb_Thing.__mro__:
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
mpupkb_Comment_strategy = st.builds(
    mpupkb_Comment,
    content=
        safe_text
)
mpupkb_NamedElement_strategy = st.builds(
    mpupkb_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
mpupkb_Own_strategy = st.builds(
    mpupkb_Own,
    ownerName=
        safe_text,
    since=
        safe_text
)
mpupkb_Thing_strategy = st.builds(
    mpupkb_Thing,
    id=
        st.integers()
)

@given(instance=mpupkb_Comment_strategy)
@settings(max_examples=50)
def test_mpupkb_comment_instantiation(instance):
    assert isinstance(instance, mpupkb_Comment)



@given(instance=mpupkb_Comment_strategy)
def test_mpupkb_comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=mpupkb_NamedElement_strategy)
@settings(max_examples=50)
def test_mpupkb_namedelement_instantiation(instance):
    assert isinstance(instance, mpupkb_NamedElement)



@given(instance=mpupkb_NamedElement_strategy)
def test_mpupkb_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=mpupkb_Own_strategy)
@settings(max_examples=50)
def test_mpupkb_own_instantiation(instance):
    assert isinstance(instance, mpupkb_Own)



@given(instance=mpupkb_Own_strategy)
def test_mpupkb_own_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original



@given(instance=mpupkb_Own_strategy)
def test_mpupkb_own_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=mpupkb_Thing_strategy)
@settings(max_examples=50)
def test_mpupkb_thing_instantiation(instance):
    assert isinstance(instance, mpupkb_Thing)



@given(instance=mpupkb_Thing_strategy)
def test_mpupkb_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

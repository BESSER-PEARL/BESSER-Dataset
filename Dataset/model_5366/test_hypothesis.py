import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    attributes::EStringToStringMapEntry,
    attributes::DocumentRoot,
    attributes::R,
    attributes::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attributes::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(attributes::EStringToStringMapEntry)


def test_attributes::estringtostringmapentry_constructor_exists():
    assert callable(attributes::EStringToStringMapEntry.__init__)


def test_attributes::estringtostringmapentry_constructor_args():
    sig = inspect.signature(attributes::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_attributes::documentroot_is_not_abstract():
    assert not inspect.isabstract(attributes::DocumentRoot)


def test_attributes::documentroot_constructor_exists():
    assert callable(attributes::DocumentRoot.__init__)


def test_attributes::documentroot_constructor_args():
    sig = inspect.signature(attributes::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_attributes::documentroot_has_mixed():
    assert hasattr(attributes::DocumentRoot, "mixed")
    descriptor = None
    for klass in attributes::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_attributes::documentroot_has_comment():
    assert hasattr(attributes::DocumentRoot, "comment")
    descriptor = None
    for klass in attributes::DocumentRoot.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_attributes::r_is_not_abstract():
    assert not inspect.isabstract(attributes::R)


def test_attributes::r_constructor_exists():
    assert callable(attributes::R.__init__)


def test_attributes::r_constructor_args():
    sig = inspect.signature(attributes::R.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_attributes::r_has_name():
    assert hasattr(attributes::R, "name")
    descriptor = None
    for klass in attributes::R.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_attributes::a_is_not_abstract():
    assert not inspect.isabstract(attributes::A)


def test_attributes::a_constructor_exists():
    assert callable(attributes::A.__init__)


def test_attributes::a_constructor_args():
    sig = inspect.signature(attributes::A.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "b" in params, "Missing parameter 'b'"
    assert "name" in params, "Missing parameter 'name'"
    assert "c" in params, "Missing parameter 'c'"
    assert "id" in params, "Missing parameter 'id'"
    assert "d" in params, "Missing parameter 'd'"

def test_attributes::a_has_comment():
    assert hasattr(attributes::A, "comment")
    descriptor = None
    for klass in attributes::A.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_attributes::a_has_b():
    assert hasattr(attributes::A, "b")
    descriptor = None
    for klass in attributes::A.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_attributes::a_has_name():
    assert hasattr(attributes::A, "name")
    descriptor = None
    for klass in attributes::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attributes::a_has_c():
    assert hasattr(attributes::A, "c")
    descriptor = None
    for klass in attributes::A.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_attributes::a_has_id():
    assert hasattr(attributes::A, "id")
    descriptor = None
    for klass in attributes::A.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_attributes::a_has_d():
    assert hasattr(attributes::A, "d")
    descriptor = None
    for klass in attributes::A.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
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
attributes::EStringToStringMapEntry_strategy = st.builds(
    attributes::EStringToStringMapEntry,
)
attributes::DocumentRoot_strategy = st.builds(
    attributes::DocumentRoot,
    mixed=
        safe_text,
    comment=
        safe_text
)
attributes::R_strategy = st.builds(
    attributes::R,
    name=
        safe_text
)
attributes::A_strategy = st.builds(
    attributes::A,
    comment=
        safe_text,
    b=
        safe_text,
    name=
        safe_text,
    c=
        safe_text,
    id=
        safe_text,
    d=
        safe_text
)

@given(instance=attributes::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_attributes::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, attributes::EStringToStringMapEntry)

@given(instance=attributes::DocumentRoot_strategy)
@settings(max_examples=50)
def test_attributes::documentroot_instantiation(instance):
    assert isinstance(instance, attributes::DocumentRoot)

@given(instance=attributes::DocumentRoot_strategy)
def test_attributes::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=attributes::DocumentRoot_strategy)
def test_attributes::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=attributes::DocumentRoot_strategy)
def test_attributes::documentroot_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=attributes::DocumentRoot_strategy)
def test_attributes::documentroot_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=attributes::R_strategy)
@settings(max_examples=50)
def test_attributes::r_instantiation(instance):
    assert isinstance(instance, attributes::R)

@given(instance=attributes::R_strategy)
def test_attributes::r_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=attributes::R_strategy)
def test_attributes::r_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attributes::A_strategy)
@settings(max_examples=50)
def test_attributes::a_instantiation(instance):
    assert isinstance(instance, attributes::A)

@given(instance=attributes::A_strategy)
def test_attributes::a_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=attributes::A_strategy)
def test_attributes::a_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=attributes::A_strategy)
def test_attributes::a_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=attributes::A_strategy)
def test_attributes::a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=attributes::A_strategy)
def test_attributes::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=attributes::A_strategy)
def test_attributes::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attributes::A_strategy)
def test_attributes::a_c_type(instance):
    assert isinstance(instance.c, str)


@given(instance=attributes::A_strategy)
def test_attributes::a_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=attributes::A_strategy)
def test_attributes::a_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=attributes::A_strategy)
def test_attributes::a_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=attributes::A_strategy)
def test_attributes::a_d_type(instance):
    assert isinstance(instance.d, str)


@given(instance=attributes::A_strategy)
def test_attributes::a_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

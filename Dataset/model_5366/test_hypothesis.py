import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    attributes_EStringToStringMapEntry,
    attributes_DocumentRoot,
    attributes_R,
    attributes_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attributes_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(attributes_EStringToStringMapEntry)


def test_attributes_estringtostringmapentry_constructor_exists():
    assert callable(attributes_EStringToStringMapEntry.__init__)


def test_attributes_estringtostringmapentry_constructor_args():
    sig = inspect.signature(attributes_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_attributes_documentroot_is_not_abstract():
    assert not inspect.isabstract(attributes_DocumentRoot)


def test_attributes_documentroot_constructor_exists():
    assert callable(attributes_DocumentRoot.__init__)


def test_attributes_documentroot_constructor_args():
    sig = inspect.signature(attributes_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_attributes_documentroot_has_mixed():
    assert hasattr(attributes_DocumentRoot, "mixed")
    descriptor = None
    for klass in attributes_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_attributes_documentroot_has_comment():
    assert hasattr(attributes_DocumentRoot, "comment")
    descriptor = None
    for klass in attributes_DocumentRoot.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_attributes_r_is_not_abstract():
    assert not inspect.isabstract(attributes_R)


def test_attributes_r_constructor_exists():
    assert callable(attributes_R.__init__)


def test_attributes_r_constructor_args():
    sig = inspect.signature(attributes_R.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_attributes_r_has_name():
    assert hasattr(attributes_R, "name")
    descriptor = None
    for klass in attributes_R.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_attributes_a_is_not_abstract():
    assert not inspect.isabstract(attributes_A)


def test_attributes_a_constructor_exists():
    assert callable(attributes_A.__init__)


def test_attributes_a_constructor_args():
    sig = inspect.signature(attributes_A.__init__)
    params = list(sig.parameters.keys())
    assert "d" in params, "Missing parameter 'd'"
    assert "b" in params, "Missing parameter 'b'"
    assert "id" in params, "Missing parameter 'id'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "c" in params, "Missing parameter 'c'"

def test_attributes_a_has_d():
    assert hasattr(attributes_A, "d")
    descriptor = None
    for klass in attributes_A.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_attributes_a_has_b():
    assert hasattr(attributes_A, "b")
    descriptor = None
    for klass in attributes_A.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_attributes_a_has_id():
    assert hasattr(attributes_A, "id")
    descriptor = None
    for klass in attributes_A.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_attributes_a_has_comment():
    assert hasattr(attributes_A, "comment")
    descriptor = None
    for klass in attributes_A.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_attributes_a_has_name():
    assert hasattr(attributes_A, "name")
    descriptor = None
    for klass in attributes_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attributes_a_has_c():
    assert hasattr(attributes_A, "c")
    descriptor = None
    for klass in attributes_A.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
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
attributes_EStringToStringMapEntry_strategy = st.builds(
    attributes_EStringToStringMapEntry,
)
attributes_DocumentRoot_strategy = st.builds(
    attributes_DocumentRoot,
    mixed=
        safe_text,
    comment=
        safe_text
)
attributes_R_strategy = st.builds(
    attributes_R,
    name=
        safe_text
)
attributes_A_strategy = st.builds(
    attributes_A,
    d=
        safe_text,
    b=
        safe_text,
    id=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text,
    c=
        safe_text
)

@given(instance=attributes_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_attributes_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, attributes_EStringToStringMapEntry)

@given(instance=attributes_DocumentRoot_strategy)
@settings(max_examples=50)
def test_attributes_documentroot_instantiation(instance):
    assert isinstance(instance, attributes_DocumentRoot)



@given(instance=attributes_DocumentRoot_strategy)
def test_attributes_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=attributes_DocumentRoot_strategy)
def test_attributes_documentroot_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=attributes_R_strategy)
@settings(max_examples=50)
def test_attributes_r_instantiation(instance):
    assert isinstance(instance, attributes_R)



@given(instance=attributes_R_strategy)
def test_attributes_r_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=attributes_A_strategy)
@settings(max_examples=50)
def test_attributes_a_instantiation(instance):
    assert isinstance(instance, attributes_A)



@given(instance=attributes_A_strategy)
def test_attributes_a_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original



@given(instance=attributes_A_strategy)
def test_attributes_a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=attributes_A_strategy)
def test_attributes_a_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=attributes_A_strategy)
def test_attributes_a_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=attributes_A_strategy)
def test_attributes_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=attributes_A_strategy)
def test_attributes_a_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

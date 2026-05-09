import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    style::StylePointer,
    style::StyleSet,
    style::StyleLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_style::stylepointer_is_not_abstract():
    assert not inspect.isabstract(style::StylePointer)


def test_style::stylepointer_constructor_exists():
    assert callable(style::StylePointer.__init__)


def test_style::stylepointer_constructor_args():
    sig = inspect.signature(style::StylePointer.__init__)
    params = list(sig.parameters.keys())



def test_style::styleset_is_not_abstract():
    assert not inspect.isabstract(style::StyleSet)


def test_style::styleset_constructor_exists():
    assert callable(style::StyleSet.__init__)


def test_style::styleset_constructor_args():
    sig = inspect.signature(style::StyleSet.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_style::styleset_has_uid():
    assert hasattr(style::StyleSet, "uid")
    descriptor = None
    for klass in style::StyleSet.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_style::styleset_has_name():
    assert hasattr(style::StyleSet, "name")
    descriptor = None
    for klass in style::StyleSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_style::stylelibrary_is_not_abstract():
    assert not inspect.isabstract(style::StyleLibrary)


def test_style::stylelibrary_constructor_exists():
    assert callable(style::StyleLibrary.__init__)


def test_style::stylelibrary_constructor_args():
    sig = inspect.signature(style::StyleLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_style::stylelibrary_has_uid():
    assert hasattr(style::StyleLibrary, "uid")
    descriptor = None
    for klass in style::StyleLibrary.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_style::stylelibrary_has_name():
    assert hasattr(style::StyleLibrary, "name")
    descriptor = None
    for klass in style::StyleLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
style::StylePointer_strategy = st.builds(
    style::StylePointer,
)
style::StyleSet_strategy = st.builds(
    style::StyleSet,
    uid=
        safe_text,
    name=
        safe_text
)
style::StyleLibrary_strategy = st.builds(
    style::StyleLibrary,
    uid=
        safe_text,
    name=
        safe_text
)

@given(instance=style::StylePointer_strategy)
@settings(max_examples=50)
def test_style::stylepointer_instantiation(instance):
    assert isinstance(instance, style::StylePointer)

@given(instance=style::StyleSet_strategy)
@settings(max_examples=50)
def test_style::styleset_instantiation(instance):
    assert isinstance(instance, style::StyleSet)

@given(instance=style::StyleSet_strategy)
def test_style::styleset_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=style::StyleSet_strategy)
def test_style::styleset_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=style::StyleSet_strategy)
def test_style::styleset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=style::StyleSet_strategy)
def test_style::styleset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=style::StyleLibrary_strategy)
@settings(max_examples=50)
def test_style::stylelibrary_instantiation(instance):
    assert isinstance(instance, style::StyleLibrary)

@given(instance=style::StyleLibrary_strategy)
def test_style::stylelibrary_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=style::StyleLibrary_strategy)
def test_style::stylelibrary_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=style::StyleLibrary_strategy)
def test_style::stylelibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=style::StyleLibrary_strategy)
def test_style::stylelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

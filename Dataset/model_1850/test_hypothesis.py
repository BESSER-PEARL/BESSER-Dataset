import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    style_StylePointer,
    style_StyleSet,
    style_StyleLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_style_stylepointer_is_not_abstract():
    assert not inspect.isabstract(style_StylePointer)


def test_style_stylepointer_constructor_exists():
    assert callable(style_StylePointer.__init__)


def test_style_stylepointer_constructor_args():
    sig = inspect.signature(style_StylePointer.__init__)
    params = list(sig.parameters.keys())



def test_style_styleset_is_not_abstract():
    assert not inspect.isabstract(style_StyleSet)


def test_style_styleset_constructor_exists():
    assert callable(style_StyleSet.__init__)


def test_style_styleset_constructor_args():
    sig = inspect.signature(style_StyleSet.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_style_styleset_has_uid():
    assert hasattr(style_StyleSet, "uid")
    descriptor = None
    for klass in style_StyleSet.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_style_styleset_has_name():
    assert hasattr(style_StyleSet, "name")
    descriptor = None
    for klass in style_StyleSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_style_stylelibrary_is_not_abstract():
    assert not inspect.isabstract(style_StyleLibrary)


def test_style_stylelibrary_constructor_exists():
    assert callable(style_StyleLibrary.__init__)


def test_style_stylelibrary_constructor_args():
    sig = inspect.signature(style_StyleLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_style_stylelibrary_has_uid():
    assert hasattr(style_StyleLibrary, "uid")
    descriptor = None
    for klass in style_StyleLibrary.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_style_stylelibrary_has_name():
    assert hasattr(style_StyleLibrary, "name")
    descriptor = None
    for klass in style_StyleLibrary.__mro__:
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
style_StylePointer_strategy = st.builds(
    style_StylePointer,
)
style_StyleSet_strategy = st.builds(
    style_StyleSet,
    uid=
        safe_text,
    name=
        safe_text
)
style_StyleLibrary_strategy = st.builds(
    style_StyleLibrary,
    uid=
        safe_text,
    name=
        safe_text
)

@given(instance=style_StylePointer_strategy)
@settings(max_examples=50)
def test_style_stylepointer_instantiation(instance):
    assert isinstance(instance, style_StylePointer)

@given(instance=style_StyleSet_strategy)
@settings(max_examples=50)
def test_style_styleset_instantiation(instance):
    assert isinstance(instance, style_StyleSet)



@given(instance=style_StyleSet_strategy)
def test_style_styleset_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=style_StyleSet_strategy)
def test_style_styleset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=style_StyleLibrary_strategy)
@settings(max_examples=50)
def test_style_stylelibrary_instantiation(instance):
    assert isinstance(instance, style_StyleLibrary)



@given(instance=style_StyleLibrary_strategy)
def test_style_stylelibrary_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=style_StyleLibrary_strategy)
def test_style_stylelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

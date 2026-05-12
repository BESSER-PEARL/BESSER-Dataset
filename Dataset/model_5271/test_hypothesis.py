import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    clazz_BRef,
    clazz_Annotation,
    clazz_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_clazz_bref_is_not_abstract():
    assert not inspect.isabstract(clazz_BRef)


def test_clazz_bref_constructor_exists():
    assert callable(clazz_BRef.__init__)


def test_clazz_bref_constructor_args():
    sig = inspect.signature(clazz_BRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_clazz_bref_has_name():
    assert hasattr(clazz_BRef, "name")
    descriptor = None
    for klass in clazz_BRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_clazz_annotation_is_not_abstract():
    assert not inspect.isabstract(clazz_Annotation)


def test_clazz_annotation_constructor_exists():
    assert callable(clazz_Annotation.__init__)


def test_clazz_annotation_constructor_args():
    sig = inspect.signature(clazz_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"

def test_clazz_annotation_has_tag():
    assert hasattr(clazz_Annotation, "tag")
    descriptor = None
    for klass in clazz_Annotation.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_clazz_b_is_not_abstract():
    assert not inspect.isabstract(clazz_B)


def test_clazz_b_constructor_exists():
    assert callable(clazz_B.__init__)


def test_clazz_b_constructor_args():
    sig = inspect.signature(clazz_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_clazz_b_has_name():
    assert hasattr(clazz_B, "name")
    descriptor = None
    for klass in clazz_B.__mro__:
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
clazz_BRef_strategy = st.builds(
    clazz_BRef,
    name=
        safe_text
)
clazz_Annotation_strategy = st.builds(
    clazz_Annotation,
    tag=
        safe_text
)
clazz_B_strategy = st.builds(
    clazz_B,
    name=
        safe_text
)

@given(instance=clazz_BRef_strategy)
@settings(max_examples=50)
def test_clazz_bref_instantiation(instance):
    assert isinstance(instance, clazz_BRef)



@given(instance=clazz_BRef_strategy)
def test_clazz_bref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=clazz_Annotation_strategy)
@settings(max_examples=50)
def test_clazz_annotation_instantiation(instance):
    assert isinstance(instance, clazz_Annotation)



@given(instance=clazz_Annotation_strategy)
def test_clazz_annotation_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=clazz_B_strategy)
@settings(max_examples=50)
def test_clazz_b_instantiation(instance):
    assert isinstance(instance, clazz_B)



@given(instance=clazz_B_strategy)
def test_clazz_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

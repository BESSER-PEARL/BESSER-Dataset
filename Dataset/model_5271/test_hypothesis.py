import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    clazz::BRef,
    clazz::Annotation,
    clazz::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_clazz::bref_is_not_abstract():
    assert not inspect.isabstract(clazz::BRef)


def test_clazz::bref_constructor_exists():
    assert callable(clazz::BRef.__init__)


def test_clazz::bref_constructor_args():
    sig = inspect.signature(clazz::BRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_clazz::bref_has_name():
    assert hasattr(clazz::BRef, "name")
    descriptor = None
    for klass in clazz::BRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_clazz::annotation_is_not_abstract():
    assert not inspect.isabstract(clazz::Annotation)


def test_clazz::annotation_constructor_exists():
    assert callable(clazz::Annotation.__init__)


def test_clazz::annotation_constructor_args():
    sig = inspect.signature(clazz::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"

def test_clazz::annotation_has_tag():
    assert hasattr(clazz::Annotation, "tag")
    descriptor = None
    for klass in clazz::Annotation.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_clazz::b_is_not_abstract():
    assert not inspect.isabstract(clazz::B)


def test_clazz::b_constructor_exists():
    assert callable(clazz::B.__init__)


def test_clazz::b_constructor_args():
    sig = inspect.signature(clazz::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_clazz::b_has_name():
    assert hasattr(clazz::B, "name")
    descriptor = None
    for klass in clazz::B.__mro__:
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
clazz::BRef_strategy = st.builds(
    clazz::BRef,
    name=
        safe_text
)
clazz::Annotation_strategy = st.builds(
    clazz::Annotation,
    tag=
        safe_text
)
clazz::B_strategy = st.builds(
    clazz::B,
    name=
        safe_text
)

@given(instance=clazz::BRef_strategy)
@settings(max_examples=50)
def test_clazz::bref_instantiation(instance):
    assert isinstance(instance, clazz::BRef)

@given(instance=clazz::BRef_strategy)
def test_clazz::bref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=clazz::BRef_strategy)
def test_clazz::bref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=clazz::Annotation_strategy)
@settings(max_examples=50)
def test_clazz::annotation_instantiation(instance):
    assert isinstance(instance, clazz::Annotation)

@given(instance=clazz::Annotation_strategy)
def test_clazz::annotation_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=clazz::Annotation_strategy)
def test_clazz::annotation_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=clazz::B_strategy)
@settings(max_examples=50)
def test_clazz::b_instantiation(instance):
    assert isinstance(instance, clazz::B)

@given(instance=clazz::B_strategy)
def test_clazz::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=clazz::B_strategy)
def test_clazz::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    classdiagram::Attribute,
    classdiagram::Class,
    classdiagram::ClassDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Attribute)


def test_classdiagram::attribute_constructor_exists():
    assert callable(classdiagram::Attribute.__init__)


def test_classdiagram::attribute_constructor_args():
    sig = inspect.signature(classdiagram::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::attribute_has_name():
    assert hasattr(classdiagram::Attribute, "name")
    descriptor = None
    for klass in classdiagram::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::class_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Class)


def test_classdiagram::class_constructor_exists():
    assert callable(classdiagram::Class.__init__)


def test_classdiagram::class_constructor_args():
    sig = inspect.signature(classdiagram::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::class_has_name():
    assert hasattr(classdiagram::Class, "name")
    descriptor = None
    for klass in classdiagram::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::classdiagram_is_not_abstract():
    assert not inspect.isabstract(classdiagram::ClassDiagram)


def test_classdiagram::classdiagram_constructor_exists():
    assert callable(classdiagram::ClassDiagram.__init__)


def test_classdiagram::classdiagram_constructor_args():
    sig = inspect.signature(classdiagram::ClassDiagram.__init__)
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
classdiagram::Attribute_strategy = st.builds(
    classdiagram::Attribute,
    name=
        safe_text
)
classdiagram::Class_strategy = st.builds(
    classdiagram::Class,
    name=
        safe_text
)
classdiagram::ClassDiagram_strategy = st.builds(
    classdiagram::ClassDiagram,
)

@given(instance=classdiagram::Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram::attribute_instantiation(instance):
    assert isinstance(instance, classdiagram::Attribute)

@given(instance=classdiagram::Attribute_strategy)
def test_classdiagram::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classdiagram::Attribute_strategy)
def test_classdiagram::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classdiagram::Class_strategy)
@settings(max_examples=50)
def test_classdiagram::class_instantiation(instance):
    assert isinstance(instance, classdiagram::Class)

@given(instance=classdiagram::Class_strategy)
def test_classdiagram::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classdiagram::Class_strategy)
def test_classdiagram::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classdiagram::ClassDiagram_strategy)
@settings(max_examples=50)
def test_classdiagram::classdiagram_instantiation(instance):
    assert isinstance(instance, classdiagram::ClassDiagram)

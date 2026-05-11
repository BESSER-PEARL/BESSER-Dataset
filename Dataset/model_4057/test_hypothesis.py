import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    classdiagram::Method,
    classdiagram::Attribute,
    classdiagram::Class,
    classdiagram::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::method_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Method)


def test_classdiagram::method_constructor_exists():
    assert callable(classdiagram::Method.__init__)


def test_classdiagram::method_constructor_args():
    sig = inspect.signature(classdiagram::Method.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Attribute)


def test_classdiagram::attribute_constructor_exists():
    assert callable(classdiagram::Attribute.__init__)


def test_classdiagram::attribute_constructor_args():
    sig = inspect.signature(classdiagram::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::class_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Class)


def test_classdiagram::class_constructor_exists():
    assert callable(classdiagram::Class.__init__)


def test_classdiagram::class_constructor_args():
    sig = inspect.signature(classdiagram::Class.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::namedelement_is_not_abstract():
    assert not inspect.isabstract(classdiagram::NamedElement)


def test_classdiagram::namedelement_constructor_exists():
    assert callable(classdiagram::NamedElement.__init__)


def test_classdiagram::namedelement_constructor_args():
    sig = inspect.signature(classdiagram::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::namedelement_has_name():
    assert hasattr(classdiagram::NamedElement, "name")
    descriptor = None
    for klass in classdiagram::NamedElement.__mro__:
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
NamedElement_strategy = st.builds(
    NamedElement,
)
classdiagram::Method_strategy = st.builds(
    classdiagram::Method,
)
classdiagram::Attribute_strategy = st.builds(
    classdiagram::Attribute,
)
classdiagram::Class_strategy = st.builds(
    classdiagram::Class,
)
classdiagram::NamedElement_strategy = st.builds(
    classdiagram::NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=classdiagram::Method_strategy)
@settings(max_examples=50)
def test_classdiagram::method_instantiation(instance):
    assert isinstance(instance, classdiagram::Method)

@given(instance=classdiagram::Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram::attribute_instantiation(instance):
    assert isinstance(instance, classdiagram::Attribute)

@given(instance=classdiagram::Class_strategy)
@settings(max_examples=50)
def test_classdiagram::class_instantiation(instance):
    assert isinstance(instance, classdiagram::Class)

@given(instance=classdiagram::NamedElement_strategy)
@settings(max_examples=50)
def test_classdiagram::namedelement_instantiation(instance):
    assert isinstance(instance, classdiagram::NamedElement)

@given(instance=classdiagram::NamedElement_strategy)
def test_classdiagram::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classdiagram::NamedElement_strategy)
def test_classdiagram::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

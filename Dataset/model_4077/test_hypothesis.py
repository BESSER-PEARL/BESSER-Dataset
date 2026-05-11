import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleUML::NamedElement,
    NamedElement,
    SimpleUML::Feature,
    SimpleUML::Class,
    SimpleUML::Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml::namedelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::NamedElement)


def test_simpleuml::namedelement_constructor_exists():
    assert callable(SimpleUML::NamedElement.__init__)


def test_simpleuml::namedelement_constructor_args():
    sig = inspect.signature(SimpleUML::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::namedelement_has_name():
    assert hasattr(SimpleUML::NamedElement, "name")
    descriptor = None
    for klass in SimpleUML::NamedElement.__mro__:
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



def test_simpleuml::feature_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Feature)


def test_simpleuml::feature_constructor_exists():
    assert callable(SimpleUML::Feature.__init__)


def test_simpleuml::feature_constructor_args():
    sig = inspect.signature(SimpleUML::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isMultivalued" in params, "Missing parameter 'isMultivalued'"

def test_simpleuml::feature_has_isMultivalued():
    assert hasattr(SimpleUML::Feature, "isMultivalued")
    descriptor = None
    for klass in SimpleUML::Feature.__mro__:
        if "isMultivalued" in klass.__dict__:
            descriptor = klass.__dict__["isMultivalued"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::class_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Class)


def test_simpleuml::class_constructor_exists():
    assert callable(SimpleUML::Class.__init__)


def test_simpleuml::class_constructor_args():
    sig = inspect.signature(SimpleUML::Class.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::package_is_not_abstract():
    assert not inspect.isabstract(SimpleUML::Package)


def test_simpleuml::package_constructor_exists():
    assert callable(SimpleUML::Package.__init__)


def test_simpleuml::package_constructor_args():
    sig = inspect.signature(SimpleUML::Package.__init__)
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
SimpleUML::NamedElement_strategy = st.builds(
    SimpleUML::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SimpleUML::Feature_strategy = st.builds(
    SimpleUML::Feature,
    isMultivalued=
        st.booleans()
)
SimpleUML::Class_strategy = st.builds(
    SimpleUML::Class,
)
SimpleUML::Package_strategy = st.builds(
    SimpleUML::Package,
)

@given(instance=SimpleUML::NamedElement_strategy)
@settings(max_examples=50)
def test_simpleuml::namedelement_instantiation(instance):
    assert isinstance(instance, SimpleUML::NamedElement)

@given(instance=SimpleUML::NamedElement_strategy)
def test_simpleuml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleUML::NamedElement_strategy)
def test_simpleuml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SimpleUML::Feature_strategy)
@settings(max_examples=50)
def test_simpleuml::feature_instantiation(instance):
    assert isinstance(instance, SimpleUML::Feature)

@given(instance=SimpleUML::Feature_strategy)
def test_simpleuml::feature_isMultivalued_type(instance):
    assert isinstance(instance.isMultivalued, bool)


@given(instance=SimpleUML::Feature_strategy)
def test_simpleuml::feature_isMultivalued_setter(instance):
    original = instance.isMultivalued
    instance.isMultivalued = original
    assert instance.isMultivalued == original

@given(instance=SimpleUML::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::class_instantiation(instance):
    assert isinstance(instance, SimpleUML::Class)

@given(instance=SimpleUML::Package_strategy)
@settings(max_examples=50)
def test_simpleuml::package_instantiation(instance):
    assert isinstance(instance, SimpleUML::Package)

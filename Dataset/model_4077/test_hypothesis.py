import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleUML_NamedElement,
    NamedElement,
    SimpleUML_Feature,
    SimpleUML_Class,
    SimpleUML_Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml_namedelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_NamedElement)


def test_simpleuml_namedelement_constructor_exists():
    assert callable(SimpleUML_NamedElement.__init__)


def test_simpleuml_namedelement_constructor_args():
    sig = inspect.signature(SimpleUML_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml_namedelement_has_name():
    assert hasattr(SimpleUML_NamedElement, "name")
    descriptor = None
    for klass in SimpleUML_NamedElement.__mro__:
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



def test_simpleuml_feature_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Feature)


def test_simpleuml_feature_constructor_exists():
    assert callable(SimpleUML_Feature.__init__)


def test_simpleuml_feature_constructor_args():
    sig = inspect.signature(SimpleUML_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isMultivalued" in params, "Missing parameter 'isMultivalued'"

def test_simpleuml_feature_has_isMultivalued():
    assert hasattr(SimpleUML_Feature, "isMultivalued")
    descriptor = None
    for klass in SimpleUML_Feature.__mro__:
        if "isMultivalued" in klass.__dict__:
            descriptor = klass.__dict__["isMultivalued"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_class_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Class)


def test_simpleuml_class_constructor_exists():
    assert callable(SimpleUML_Class.__init__)


def test_simpleuml_class_constructor_args():
    sig = inspect.signature(SimpleUML_Class.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_package_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Package)


def test_simpleuml_package_constructor_exists():
    assert callable(SimpleUML_Package.__init__)


def test_simpleuml_package_constructor_args():
    sig = inspect.signature(SimpleUML_Package.__init__)
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
SimpleUML_NamedElement_strategy = st.builds(
    SimpleUML_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
SimpleUML_Feature_strategy = st.builds(
    SimpleUML_Feature,
    isMultivalued=
        st.booleans()
)
SimpleUML_Class_strategy = st.builds(
    SimpleUML_Class,
)
SimpleUML_Package_strategy = st.builds(
    SimpleUML_Package,
)

@given(instance=SimpleUML_NamedElement_strategy)
@settings(max_examples=50)
def test_simpleuml_namedelement_instantiation(instance):
    assert isinstance(instance, SimpleUML_NamedElement)



@given(instance=SimpleUML_NamedElement_strategy)
def test_simpleuml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=SimpleUML_Feature_strategy)
@settings(max_examples=50)
def test_simpleuml_feature_instantiation(instance):
    assert isinstance(instance, SimpleUML_Feature)



@given(instance=SimpleUML_Feature_strategy)
def test_simpleuml_feature_isMultivalued_setter(instance):
    original = instance.isMultivalued
    instance.isMultivalued = original
    assert instance.isMultivalued == original

@given(instance=SimpleUML_Class_strategy)
@settings(max_examples=50)
def test_simpleuml_class_instantiation(instance):
    assert isinstance(instance, SimpleUML_Class)

@given(instance=SimpleUML_Package_strategy)
@settings(max_examples=50)
def test_simpleuml_package_instantiation(instance):
    assert isinstance(instance, SimpleUML_Package)

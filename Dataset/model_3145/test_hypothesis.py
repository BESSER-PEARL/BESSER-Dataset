import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CNamedElement,
    classm1::Attribute,
    classm1::Class,
    classm1::CNamedElement,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cnamedelement_is_not_abstract():
    assert not inspect.isabstract(CNamedElement)


def test_cnamedelement_constructor_exists():
    assert callable(CNamedElement.__init__)


def test_cnamedelement_constructor_args():
    sig = inspect.signature(CNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_classm1::attribute_is_not_abstract():
    assert not inspect.isabstract(classm1::Attribute)


def test_classm1::attribute_constructor_exists():
    assert callable(classm1::Attribute.__init__)


def test_classm1::attribute_constructor_args():
    sig = inspect.signature(classm1::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "isKey" in params, "Missing parameter 'isKey'"

def test_classm1::attribute_has_visibility():
    assert hasattr(classm1::Attribute, "visibility")
    descriptor = None
    for klass in classm1::Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_classm1::attribute_has_isKey():
    assert hasattr(classm1::Attribute, "isKey")
    descriptor = None
    for klass in classm1::Attribute.__mro__:
        if "isKey" in klass.__dict__:
            descriptor = klass.__dict__["isKey"]
            break
    assert isinstance(descriptor, property)



def test_classm1::class_is_not_abstract():
    assert not inspect.isabstract(classm1::Class)


def test_classm1::class_constructor_exists():
    assert callable(classm1::Class.__init__)


def test_classm1::class_constructor_args():
    sig = inspect.signature(classm1::Class.__init__)
    params = list(sig.parameters.keys())



def test_classm1::cnamedelement_is_not_abstract():
    assert not inspect.isabstract(classm1::CNamedElement)


def test_classm1::cnamedelement_constructor_exists():
    assert callable(classm1::CNamedElement.__init__)


def test_classm1::cnamedelement_constructor_args():
    sig = inspect.signature(classm1::CNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classm1::cnamedelement_has_name():
    assert hasattr(classm1::CNamedElement, "name")
    descriptor = None
    for klass in classm1::CNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "private",
        "public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"


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
CNamedElement_strategy = st.builds(
    CNamedElement,
)
classm1::Attribute_strategy = st.builds(
    classm1::Attribute,
    visibility=
        safe_text,
    isKey=
        st.booleans()
)
classm1::Class_strategy = st.builds(
    classm1::Class,
)
classm1::CNamedElement_strategy = st.builds(
    classm1::CNamedElement,
    name=
        safe_text
)

@given(instance=CNamedElement_strategy)
@settings(max_examples=50)
def test_cnamedelement_instantiation(instance):
    assert isinstance(instance, CNamedElement)

@given(instance=classm1::Attribute_strategy)
@settings(max_examples=50)
def test_classm1::attribute_instantiation(instance):
    assert isinstance(instance, classm1::Attribute)

@given(instance=classm1::Attribute_strategy)
def test_classm1::attribute_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=classm1::Attribute_strategy)
def test_classm1::attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=classm1::Attribute_strategy)
def test_classm1::attribute_isKey_type(instance):
    assert isinstance(instance.isKey, bool)


@given(instance=classm1::Attribute_strategy)
def test_classm1::attribute_isKey_setter(instance):
    original = instance.isKey
    instance.isKey = original
    assert instance.isKey == original

@given(instance=classm1::Class_strategy)
@settings(max_examples=50)
def test_classm1::class_instantiation(instance):
    assert isinstance(instance, classm1::Class)

@given(instance=classm1::CNamedElement_strategy)
@settings(max_examples=50)
def test_classm1::cnamedelement_instantiation(instance):
    assert isinstance(instance, classm1::CNamedElement)

@given(instance=classm1::CNamedElement_strategy)
def test_classm1::cnamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classm1::CNamedElement_strategy)
def test_classm1::cnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

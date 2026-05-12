import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CNamedElement,
    classm1_Attribute,
    classm1_Class,
    classm1_CNamedElement,
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



def test_classm1_attribute_is_not_abstract():
    assert not inspect.isabstract(classm1_Attribute)


def test_classm1_attribute_constructor_exists():
    assert callable(classm1_Attribute.__init__)


def test_classm1_attribute_constructor_args():
    sig = inspect.signature(classm1_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "isKey" in params, "Missing parameter 'isKey'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_classm1_attribute_has_isKey():
    assert hasattr(classm1_Attribute, "isKey")
    descriptor = None
    for klass in classm1_Attribute.__mro__:
        if "isKey" in klass.__dict__:
            descriptor = klass.__dict__["isKey"]
            break
    assert isinstance(descriptor, property)

def test_classm1_attribute_has_visibility():
    assert hasattr(classm1_Attribute, "visibility")
    descriptor = None
    for klass in classm1_Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_classm1_class_is_not_abstract():
    assert not inspect.isabstract(classm1_Class)


def test_classm1_class_constructor_exists():
    assert callable(classm1_Class.__init__)


def test_classm1_class_constructor_args():
    sig = inspect.signature(classm1_Class.__init__)
    params = list(sig.parameters.keys())



def test_classm1_cnamedelement_is_not_abstract():
    assert not inspect.isabstract(classm1_CNamedElement)


def test_classm1_cnamedelement_constructor_exists():
    assert callable(classm1_CNamedElement.__init__)


def test_classm1_cnamedelement_constructor_args():
    sig = inspect.signature(classm1_CNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classm1_cnamedelement_has_name():
    assert hasattr(classm1_CNamedElement, "name")
    descriptor = None
    for klass in classm1_CNamedElement.__mro__:
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
        "public",
        "private",
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
classm1_Attribute_strategy = st.builds(
    classm1_Attribute,
    isKey=
        st.booleans(),
    visibility=
        safe_text
)
classm1_Class_strategy = st.builds(
    classm1_Class,
)
classm1_CNamedElement_strategy = st.builds(
    classm1_CNamedElement,
    name=
        safe_text
)

@given(instance=CNamedElement_strategy)
@settings(max_examples=50)
def test_cnamedelement_instantiation(instance):
    assert isinstance(instance, CNamedElement)

@given(instance=classm1_Attribute_strategy)
@settings(max_examples=50)
def test_classm1_attribute_instantiation(instance):
    assert isinstance(instance, classm1_Attribute)



@given(instance=classm1_Attribute_strategy)
def test_classm1_attribute_isKey_setter(instance):
    original = instance.isKey
    instance.isKey = original
    assert instance.isKey == original



@given(instance=classm1_Attribute_strategy)
def test_classm1_attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=classm1_Class_strategy)
@settings(max_examples=50)
def test_classm1_class_instantiation(instance):
    assert isinstance(instance, classm1_Class)

@given(instance=classm1_CNamedElement_strategy)
@settings(max_examples=50)
def test_classm1_cnamedelement_instantiation(instance):
    assert isinstance(instance, classm1_CNamedElement)



@given(instance=classm1_CNamedElement_strategy)
def test_classm1_cnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::subpackage::SubpackageMetaClass,
    SubpackageMetaClass,
    test::MyMetaClass,
    MyEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::subpackage::subpackagemetaclass_is_not_abstract():
    assert not inspect.isabstract(test::subpackage::SubpackageMetaClass)


def test_test::subpackage::subpackagemetaclass_constructor_exists():
    assert callable(test::subpackage::SubpackageMetaClass.__init__)


def test_test::subpackage::subpackagemetaclass_constructor_args():
    sig = inspect.signature(test::subpackage::SubpackageMetaClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test::subpackage::subpackagemetaclass_has_name():
    assert hasattr(test::subpackage::SubpackageMetaClass, "name")
    descriptor = None
    for klass in test::subpackage::SubpackageMetaClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_subpackagemetaclass_is_not_abstract():
    assert not inspect.isabstract(SubpackageMetaClass)


def test_subpackagemetaclass_constructor_exists():
    assert callable(SubpackageMetaClass.__init__)


def test_subpackagemetaclass_constructor_args():
    sig = inspect.signature(SubpackageMetaClass.__init__)
    params = list(sig.parameters.keys())



def test_test::mymetaclass_is_not_abstract():
    assert not inspect.isabstract(test::MyMetaClass)


def test_test::mymetaclass_constructor_exists():
    assert callable(test::MyMetaClass.__init__)


def test_test::mymetaclass_constructor_args():
    sig = inspect.signature(test::MyMetaClass.__init__)
    params = list(sig.parameters.keys())
    assert "enumAttr" in params, "Missing parameter 'enumAttr'"
    assert "name" in params, "Missing parameter 'name'"

def test_test::mymetaclass_has_enumAttr():
    assert hasattr(test::MyMetaClass, "enumAttr")
    descriptor = None
    for klass in test::MyMetaClass.__mro__:
        if "enumAttr" in klass.__dict__:
            descriptor = klass.__dict__["enumAttr"]
            break
    assert isinstance(descriptor, property)

def test_test::mymetaclass_has_name():
    assert hasattr(test::MyMetaClass, "name")
    descriptor = None
    for klass in test::MyMetaClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_myenum_exists():
    # Check that the Enumeration exists
    assert MyEnum is not None

def test_myenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MyEnum]
    expected_literals = [
        "X",
        "Y",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MyEnum"


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
test::subpackage::SubpackageMetaClass_strategy = st.builds(
    test::subpackage::SubpackageMetaClass,
    name=
        safe_text
)
SubpackageMetaClass_strategy = st.builds(
    SubpackageMetaClass,
)
test::MyMetaClass_strategy = st.builds(
    test::MyMetaClass,
    enumAttr=
        safe_text,
    name=
        safe_text
)

@given(instance=test::subpackage::SubpackageMetaClass_strategy)
@settings(max_examples=50)
def test_test::subpackage::subpackagemetaclass_instantiation(instance):
    assert isinstance(instance, test::subpackage::SubpackageMetaClass)

@given(instance=test::subpackage::SubpackageMetaClass_strategy)
def test_test::subpackage::subpackagemetaclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=test::subpackage::SubpackageMetaClass_strategy)
def test_test::subpackage::subpackagemetaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SubpackageMetaClass_strategy)
@settings(max_examples=50)
def test_subpackagemetaclass_instantiation(instance):
    assert isinstance(instance, SubpackageMetaClass)

@given(instance=test::MyMetaClass_strategy)
@settings(max_examples=50)
def test_test::mymetaclass_instantiation(instance):
    assert isinstance(instance, test::MyMetaClass)

@given(instance=test::MyMetaClass_strategy)
def test_test::mymetaclass_enumAttr_type(instance):
    assert isinstance(instance.enumAttr, str)


@given(instance=test::MyMetaClass_strategy)
def test_test::mymetaclass_enumAttr_setter(instance):
    original = instance.enumAttr
    instance.enumAttr = original
    assert instance.enumAttr == original

@given(instance=test::MyMetaClass_strategy)
def test_test::mymetaclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=test::MyMetaClass_strategy)
def test_test::mymetaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_subpackage_SubpackageMetaClass,
    SubpackageMetaClass,
    test_MyMetaClass,
    MyEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_subpackage_subpackagemetaclass_is_not_abstract():
    assert not inspect.isabstract(test_subpackage_SubpackageMetaClass)


def test_test_subpackage_subpackagemetaclass_constructor_exists():
    assert callable(test_subpackage_SubpackageMetaClass.__init__)


def test_test_subpackage_subpackagemetaclass_constructor_args():
    sig = inspect.signature(test_subpackage_SubpackageMetaClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test_subpackage_subpackagemetaclass_has_name():
    assert hasattr(test_subpackage_SubpackageMetaClass, "name")
    descriptor = None
    for klass in test_subpackage_SubpackageMetaClass.__mro__:
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



def test_test_mymetaclass_is_not_abstract():
    assert not inspect.isabstract(test_MyMetaClass)


def test_test_mymetaclass_constructor_exists():
    assert callable(test_MyMetaClass.__init__)


def test_test_mymetaclass_constructor_args():
    sig = inspect.signature(test_MyMetaClass.__init__)
    params = list(sig.parameters.keys())
    assert "enumAttr" in params, "Missing parameter 'enumAttr'"
    assert "name" in params, "Missing parameter 'name'"

def test_test_mymetaclass_has_enumAttr():
    assert hasattr(test_MyMetaClass, "enumAttr")
    descriptor = None
    for klass in test_MyMetaClass.__mro__:
        if "enumAttr" in klass.__dict__:
            descriptor = klass.__dict__["enumAttr"]
            break
    assert isinstance(descriptor, property)

def test_test_mymetaclass_has_name():
    assert hasattr(test_MyMetaClass, "name")
    descriptor = None
    for klass in test_MyMetaClass.__mro__:
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
test_subpackage_SubpackageMetaClass_strategy = st.builds(
    test_subpackage_SubpackageMetaClass,
    name=
        safe_text
)
SubpackageMetaClass_strategy = st.builds(
    SubpackageMetaClass,
)
test_MyMetaClass_strategy = st.builds(
    test_MyMetaClass,
    enumAttr=
        safe_text,
    name=
        safe_text
)

@given(instance=test_subpackage_SubpackageMetaClass_strategy)
@settings(max_examples=50)
def test_test_subpackage_subpackagemetaclass_instantiation(instance):
    assert isinstance(instance, test_subpackage_SubpackageMetaClass)



@given(instance=test_subpackage_SubpackageMetaClass_strategy)
def test_test_subpackage_subpackagemetaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SubpackageMetaClass_strategy)
@settings(max_examples=50)
def test_subpackagemetaclass_instantiation(instance):
    assert isinstance(instance, SubpackageMetaClass)

@given(instance=test_MyMetaClass_strategy)
@settings(max_examples=50)
def test_test_mymetaclass_instantiation(instance):
    assert isinstance(instance, test_MyMetaClass)



@given(instance=test_MyMetaClass_strategy)
def test_test_mymetaclass_enumAttr_setter(instance):
    original = instance.enumAttr
    instance.enumAttr = original
    assert instance.enumAttr == original



@given(instance=test_MyMetaClass_strategy)
def test_test_mymetaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

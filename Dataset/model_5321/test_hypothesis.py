import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    root_noLiterals_NoLitClass,
    root_nestedPackage1_NestedClass1,
    NestedClass1,
    root_RootClass,
    NoLitEnum,
    RootEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_noliterals_nolitclass_is_not_abstract():
    assert not inspect.isabstract(root_noLiterals_NoLitClass)


def test_root_noliterals_nolitclass_constructor_exists():
    assert callable(root_noLiterals_NoLitClass.__init__)


def test_root_noliterals_nolitclass_constructor_args():
    sig = inspect.signature(root_noLiterals_NoLitClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_root_noliterals_nolitclass_has_attribute2():
    assert hasattr(root_noLiterals_NoLitClass, "attribute2")
    descriptor = None
    for klass in root_noLiterals_NoLitClass.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_root_nestedpackage1_nestedclass1_is_not_abstract():
    assert not inspect.isabstract(root_nestedPackage1_NestedClass1)


def test_root_nestedpackage1_nestedclass1_constructor_exists():
    assert callable(root_nestedPackage1_NestedClass1.__init__)


def test_root_nestedpackage1_nestedclass1_constructor_args():
    sig = inspect.signature(root_nestedPackage1_NestedClass1.__init__)
    params = list(sig.parameters.keys())



def test_nestedclass1_is_not_abstract():
    assert not inspect.isabstract(NestedClass1)


def test_nestedclass1_constructor_exists():
    assert callable(NestedClass1.__init__)


def test_nestedclass1_constructor_args():
    sig = inspect.signature(NestedClass1.__init__)
    params = list(sig.parameters.keys())



def test_root_rootclass_is_not_abstract():
    assert not inspect.isabstract(root_RootClass)


def test_root_rootclass_constructor_exists():
    assert callable(root_RootClass.__init__)


def test_root_rootclass_constructor_args():
    sig = inspect.signature(root_RootClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute1" in params, "Missing parameter 'attribute1'"

def test_root_rootclass_has_attribute1():
    assert hasattr(root_RootClass, "attribute1")
    descriptor = None
    for klass in root_RootClass.__mro__:
        if "attribute1" in klass.__dict__:
            descriptor = klass.__dict__["attribute1"]
            break
    assert isinstance(descriptor, property)

def test_nolitenum_exists():
    # Check that the Enumeration exists
    assert NoLitEnum is not None

def test_nolitenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NoLitEnum]
    expected_literals = [
        "literal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NoLitEnum"

def test_rootenum_exists():
    # Check that the Enumeration exists
    assert RootEnum is not None

def test_rootenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RootEnum]
    expected_literals = [
        "literal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RootEnum"


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
root_noLiterals_NoLitClass_strategy = st.builds(
    root_noLiterals_NoLitClass,
    attribute2=
        safe_text
)
root_nestedPackage1_NestedClass1_strategy = st.builds(
    root_nestedPackage1_NestedClass1,
)
NestedClass1_strategy = st.builds(
    NestedClass1,
)
root_RootClass_strategy = st.builds(
    root_RootClass,
    attribute1=
        safe_text
)

@given(instance=root_noLiterals_NoLitClass_strategy)
@settings(max_examples=50)
def test_root_noliterals_nolitclass_instantiation(instance):
    assert isinstance(instance, root_noLiterals_NoLitClass)



@given(instance=root_noLiterals_NoLitClass_strategy)
def test_root_noliterals_nolitclass_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=root_nestedPackage1_NestedClass1_strategy)
@settings(max_examples=50)
def test_root_nestedpackage1_nestedclass1_instantiation(instance):
    assert isinstance(instance, root_nestedPackage1_NestedClass1)

@given(instance=NestedClass1_strategy)
@settings(max_examples=50)
def test_nestedclass1_instantiation(instance):
    assert isinstance(instance, NestedClass1)

@given(instance=root_RootClass_strategy)
@settings(max_examples=50)
def test_root_rootclass_instantiation(instance):
    assert isinstance(instance, root_RootClass)



@given(instance=root_RootClass_strategy)
def test_root_rootclass_attribute1_setter(instance):
    original = instance.attribute1
    instance.attribute1 = original
    assert instance.attribute1 == original

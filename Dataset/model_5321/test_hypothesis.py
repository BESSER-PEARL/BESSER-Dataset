import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    root::noLiterals::NoLitClass,
    root::nestedPackage1::NestedClass1,
    NestedClass1,
    root::RootClass,
    RootEnum,
    NoLitEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root::noliterals::nolitclass_is_not_abstract():
    assert not inspect.isabstract(root::noLiterals::NoLitClass)


def test_root::noliterals::nolitclass_constructor_exists():
    assert callable(root::noLiterals::NoLitClass.__init__)


def test_root::noliterals::nolitclass_constructor_args():
    sig = inspect.signature(root::noLiterals::NoLitClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_root::noliterals::nolitclass_has_attribute2():
    assert hasattr(root::noLiterals::NoLitClass, "attribute2")
    descriptor = None
    for klass in root::noLiterals::NoLitClass.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_root::nestedpackage1::nestedclass1_is_not_abstract():
    assert not inspect.isabstract(root::nestedPackage1::NestedClass1)


def test_root::nestedpackage1::nestedclass1_constructor_exists():
    assert callable(root::nestedPackage1::NestedClass1.__init__)


def test_root::nestedpackage1::nestedclass1_constructor_args():
    sig = inspect.signature(root::nestedPackage1::NestedClass1.__init__)
    params = list(sig.parameters.keys())



def test_nestedclass1_is_not_abstract():
    assert not inspect.isabstract(NestedClass1)


def test_nestedclass1_constructor_exists():
    assert callable(NestedClass1.__init__)


def test_nestedclass1_constructor_args():
    sig = inspect.signature(NestedClass1.__init__)
    params = list(sig.parameters.keys())



def test_root::rootclass_is_not_abstract():
    assert not inspect.isabstract(root::RootClass)


def test_root::rootclass_constructor_exists():
    assert callable(root::RootClass.__init__)


def test_root::rootclass_constructor_args():
    sig = inspect.signature(root::RootClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute1" in params, "Missing parameter 'attribute1'"

def test_root::rootclass_has_attribute1():
    assert hasattr(root::RootClass, "attribute1")
    descriptor = None
    for klass in root::RootClass.__mro__:
        if "attribute1" in klass.__dict__:
            descriptor = klass.__dict__["attribute1"]
            break
    assert isinstance(descriptor, property)

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
root::noLiterals::NoLitClass_strategy = st.builds(
    root::noLiterals::NoLitClass,
    attribute2=
        safe_text
)
root::nestedPackage1::NestedClass1_strategy = st.builds(
    root::nestedPackage1::NestedClass1,
)
NestedClass1_strategy = st.builds(
    NestedClass1,
)
root::RootClass_strategy = st.builds(
    root::RootClass,
    attribute1=
        safe_text
)

@given(instance=root::noLiterals::NoLitClass_strategy)
@settings(max_examples=50)
def test_root::noliterals::nolitclass_instantiation(instance):
    assert isinstance(instance, root::noLiterals::NoLitClass)

@given(instance=root::noLiterals::NoLitClass_strategy)
def test_root::noliterals::nolitclass_attribute2_type(instance):
    assert isinstance(instance.attribute2, str)


@given(instance=root::noLiterals::NoLitClass_strategy)
def test_root::noliterals::nolitclass_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=root::nestedPackage1::NestedClass1_strategy)
@settings(max_examples=50)
def test_root::nestedpackage1::nestedclass1_instantiation(instance):
    assert isinstance(instance, root::nestedPackage1::NestedClass1)

@given(instance=NestedClass1_strategy)
@settings(max_examples=50)
def test_nestedclass1_instantiation(instance):
    assert isinstance(instance, NestedClass1)

@given(instance=root::RootClass_strategy)
@settings(max_examples=50)
def test_root::rootclass_instantiation(instance):
    assert isinstance(instance, root::RootClass)

@given(instance=root::RootClass_strategy)
def test_root::rootclass_attribute1_type(instance):
    assert isinstance(instance.attribute1, str)


@given(instance=root::RootClass_strategy)
def test_root::rootclass_attribute1_setter(instance):
    original = instance.attribute1
    instance.attribute1 = original
    assert instance.attribute1 == original

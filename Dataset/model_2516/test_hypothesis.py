import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_EClass2,
    test_EClass1,
    test_EClass0,
    EEnum0,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_eclass2_is_not_abstract():
    assert not inspect.isabstract(test_EClass2)


def test_test_eclass2_constructor_exists():
    assert callable(test_EClass2.__init__)


def test_test_eclass2_constructor_args():
    sig = inspect.signature(test_EClass2.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"
    assert "EAttribute1" in params, "Missing parameter 'EAttribute1'"

def test_test_eclass2_has_EAttribute0():
    assert hasattr(test_EClass2, "EAttribute0")
    descriptor = None
    for klass in test_EClass2.__mro__:
        if "EAttribute0" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute0"]
            break
    assert isinstance(descriptor, property)

def test_test_eclass2_has_EAttribute1():
    assert hasattr(test_EClass2, "EAttribute1")
    descriptor = None
    for klass in test_EClass2.__mro__:
        if "EAttribute1" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute1"]
            break
    assert isinstance(descriptor, property)



def test_test_eclass1_is_not_abstract():
    assert not inspect.isabstract(test_EClass1)


def test_test_eclass1_constructor_exists():
    assert callable(test_EClass1.__init__)


def test_test_eclass1_constructor_args():
    sig = inspect.signature(test_EClass1.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"

def test_test_eclass1_has_EAttribute0():
    assert hasattr(test_EClass1, "EAttribute0")
    descriptor = None
    for klass in test_EClass1.__mro__:
        if "EAttribute0" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute0"]
            break
    assert isinstance(descriptor, property)



def test_test_eclass0_is_not_abstract():
    assert not inspect.isabstract(test_EClass0)


def test_test_eclass0_constructor_exists():
    assert callable(test_EClass0.__init__)


def test_test_eclass0_constructor_args():
    sig = inspect.signature(test_EClass0.__init__)
    params = list(sig.parameters.keys())
    assert "attr1" in params, "Missing parameter 'attr1'"
    assert "attr0" in params, "Missing parameter 'attr0'"

def test_test_eclass0_has_attr1():
    assert hasattr(test_EClass0, "attr1")
    descriptor = None
    for klass in test_EClass0.__mro__:
        if "attr1" in klass.__dict__:
            descriptor = klass.__dict__["attr1"]
            break
    assert isinstance(descriptor, property)

def test_test_eclass0_has_attr0():
    assert hasattr(test_EClass0, "attr0")
    descriptor = None
    for klass in test_EClass0.__mro__:
        if "attr0" in klass.__dict__:
            descriptor = klass.__dict__["attr0"]
            break
    assert isinstance(descriptor, property)

def test_eenum0_exists():
    # Check that the Enumeration exists
    assert EEnum0 is not None

def test_eenum0_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EEnum0]
    expected_literals = [
        "a",
        "b",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EEnum0"


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
test_EClass2_strategy = st.builds(
    test_EClass2,
    EAttribute0=
        st.booleans(),
    EAttribute1=
        st.integers()
)
test_EClass1_strategy = st.builds(
    test_EClass1,
    EAttribute0=
        safe_text
)
test_EClass0_strategy = st.builds(
    test_EClass0,
    attr1=
        st.booleans(),
    attr0=
        safe_text
)

@given(instance=test_EClass2_strategy)
@settings(max_examples=50)
def test_test_eclass2_instantiation(instance):
    assert isinstance(instance, test_EClass2)



@given(instance=test_EClass2_strategy)
def test_test_eclass2_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original



@given(instance=test_EClass2_strategy)
def test_test_eclass2_EAttribute1_setter(instance):
    original = instance.EAttribute1
    instance.EAttribute1 = original
    assert instance.EAttribute1 == original

@given(instance=test_EClass1_strategy)
@settings(max_examples=50)
def test_test_eclass1_instantiation(instance):
    assert isinstance(instance, test_EClass1)



@given(instance=test_EClass1_strategy)
def test_test_eclass1_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original

@given(instance=test_EClass0_strategy)
@settings(max_examples=50)
def test_test_eclass0_instantiation(instance):
    assert isinstance(instance, test_EClass0)



@given(instance=test_EClass0_strategy)
def test_test_eclass0_attr1_setter(instance):
    original = instance.attr1
    instance.attr1 = original
    assert instance.attr1 == original



@given(instance=test_EClass0_strategy)
def test_test_eclass0_attr0_setter(instance):
    original = instance.attr0
    instance.attr0 = original
    assert instance.attr0 == original

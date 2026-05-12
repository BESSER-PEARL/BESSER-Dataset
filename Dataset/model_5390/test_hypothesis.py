import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    nonemf_Serializable,
    nonemf_A,
    nonemf_B,
    Serializable,
    nonemf_MySerializableClass,
    TestB,
    TestA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nonemf_serializable_is_not_abstract():
    assert not inspect.isabstract(nonemf_Serializable)


def test_nonemf_serializable_constructor_exists():
    assert callable(nonemf_Serializable.__init__)


def test_nonemf_serializable_constructor_args():
    sig = inspect.signature(nonemf_Serializable.__init__)
    params = list(sig.parameters.keys())



def test_nonemf_a_is_not_abstract():
    assert not inspect.isabstract(nonemf_A)


def test_nonemf_a_constructor_exists():
    assert callable(nonemf_A.__init__)


def test_nonemf_a_constructor_args():
    sig = inspect.signature(nonemf_A.__init__)
    params = list(sig.parameters.keys())



def test_nonemf_b_is_not_abstract():
    assert not inspect.isabstract(nonemf_B)


def test_nonemf_b_constructor_exists():
    assert callable(nonemf_B.__init__)


def test_nonemf_b_constructor_args():
    sig = inspect.signature(nonemf_B.__init__)
    params = list(sig.parameters.keys())



def test_serializable_is_not_abstract():
    assert not inspect.isabstract(Serializable)


def test_serializable_constructor_exists():
    assert callable(Serializable.__init__)


def test_serializable_constructor_args():
    sig = inspect.signature(Serializable.__init__)
    params = list(sig.parameters.keys())



def test_nonemf_myserializableclass_is_not_abstract():
    assert not inspect.isabstract(nonemf_MySerializableClass)


def test_nonemf_myserializableclass_constructor_exists():
    assert callable(nonemf_MySerializableClass.__init__)


def test_nonemf_myserializableclass_constructor_args():
    sig = inspect.signature(nonemf_MySerializableClass.__init__)
    params = list(sig.parameters.keys())
    assert "somethingInteresting" in params, "Missing parameter 'somethingInteresting'"

def test_nonemf_myserializableclass_has_somethingInteresting():
    assert hasattr(nonemf_MySerializableClass, "somethingInteresting")
    descriptor = None
    for klass in nonemf_MySerializableClass.__mro__:
        if "somethingInteresting" in klass.__dict__:
            descriptor = klass.__dict__["somethingInteresting"]
            break
    assert isinstance(descriptor, property)

def test_testb_exists():
    # Check that the Enumeration exists
    assert TestB is not None

def test_testb_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestB]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestB"

def test_testa_exists():
    # Check that the Enumeration exists
    assert TestA is not None

def test_testa_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestA]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestA"


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
nonemf_Serializable_strategy = st.builds(
    nonemf_Serializable,
)
nonemf_A_strategy = st.builds(
    nonemf_A,
)
nonemf_B_strategy = st.builds(
    nonemf_B,
)
Serializable_strategy = st.builds(
    Serializable,
)
nonemf_MySerializableClass_strategy = st.builds(
    nonemf_MySerializableClass,
    somethingInteresting=
        safe_text
)

@given(instance=nonemf_Serializable_strategy)
@settings(max_examples=50)
def test_nonemf_serializable_instantiation(instance):
    assert isinstance(instance, nonemf_Serializable)

@given(instance=nonemf_A_strategy)
@settings(max_examples=50)
def test_nonemf_a_instantiation(instance):
    assert isinstance(instance, nonemf_A)

@given(instance=nonemf_B_strategy)
@settings(max_examples=50)
def test_nonemf_b_instantiation(instance):
    assert isinstance(instance, nonemf_B)

@given(instance=Serializable_strategy)
@settings(max_examples=50)
def test_serializable_instantiation(instance):
    assert isinstance(instance, Serializable)

@given(instance=nonemf_MySerializableClass_strategy)
@settings(max_examples=50)
def test_nonemf_myserializableclass_instantiation(instance):
    assert isinstance(instance, nonemf_MySerializableClass)



@given(instance=nonemf_MySerializableClass_strategy)
def test_nonemf_myserializableclass_somethingInteresting_setter(instance):
    original = instance.somethingInteresting
    instance.somethingInteresting = original
    assert instance.somethingInteresting == original

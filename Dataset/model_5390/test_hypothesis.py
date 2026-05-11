import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    nonemf::Serializable,
    nonemf::A,
    nonemf::B,
    Serializable,
    nonemf::MySerializableClass,
    TestA,
    TestB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nonemf::serializable_is_not_abstract():
    assert not inspect.isabstract(nonemf::Serializable)


def test_nonemf::serializable_constructor_exists():
    assert callable(nonemf::Serializable.__init__)


def test_nonemf::serializable_constructor_args():
    sig = inspect.signature(nonemf::Serializable.__init__)
    params = list(sig.parameters.keys())



def test_nonemf::a_is_not_abstract():
    assert not inspect.isabstract(nonemf::A)


def test_nonemf::a_constructor_exists():
    assert callable(nonemf::A.__init__)


def test_nonemf::a_constructor_args():
    sig = inspect.signature(nonemf::A.__init__)
    params = list(sig.parameters.keys())



def test_nonemf::b_is_not_abstract():
    assert not inspect.isabstract(nonemf::B)


def test_nonemf::b_constructor_exists():
    assert callable(nonemf::B.__init__)


def test_nonemf::b_constructor_args():
    sig = inspect.signature(nonemf::B.__init__)
    params = list(sig.parameters.keys())



def test_serializable_is_not_abstract():
    assert not inspect.isabstract(Serializable)


def test_serializable_constructor_exists():
    assert callable(Serializable.__init__)


def test_serializable_constructor_args():
    sig = inspect.signature(Serializable.__init__)
    params = list(sig.parameters.keys())



def test_nonemf::myserializableclass_is_not_abstract():
    assert not inspect.isabstract(nonemf::MySerializableClass)


def test_nonemf::myserializableclass_constructor_exists():
    assert callable(nonemf::MySerializableClass.__init__)


def test_nonemf::myserializableclass_constructor_args():
    sig = inspect.signature(nonemf::MySerializableClass.__init__)
    params = list(sig.parameters.keys())
    assert "somethingInteresting" in params, "Missing parameter 'somethingInteresting'"

def test_nonemf::myserializableclass_has_somethingInteresting():
    assert hasattr(nonemf::MySerializableClass, "somethingInteresting")
    descriptor = None
    for klass in nonemf::MySerializableClass.__mro__:
        if "somethingInteresting" in klass.__dict__:
            descriptor = klass.__dict__["somethingInteresting"]
            break
    assert isinstance(descriptor, property)

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
nonemf::Serializable_strategy = st.builds(
    nonemf::Serializable,
)
nonemf::A_strategy = st.builds(
    nonemf::A,
)
nonemf::B_strategy = st.builds(
    nonemf::B,
)
Serializable_strategy = st.builds(
    Serializable,
)
nonemf::MySerializableClass_strategy = st.builds(
    nonemf::MySerializableClass,
    somethingInteresting=
        safe_text
)

@given(instance=nonemf::Serializable_strategy)
@settings(max_examples=50)
def test_nonemf::serializable_instantiation(instance):
    assert isinstance(instance, nonemf::Serializable)

@given(instance=nonemf::A_strategy)
@settings(max_examples=50)
def test_nonemf::a_instantiation(instance):
    assert isinstance(instance, nonemf::A)

@given(instance=nonemf::B_strategy)
@settings(max_examples=50)
def test_nonemf::b_instantiation(instance):
    assert isinstance(instance, nonemf::B)

@given(instance=Serializable_strategy)
@settings(max_examples=50)
def test_serializable_instantiation(instance):
    assert isinstance(instance, Serializable)

@given(instance=nonemf::MySerializableClass_strategy)
@settings(max_examples=50)
def test_nonemf::myserializableclass_instantiation(instance):
    assert isinstance(instance, nonemf::MySerializableClass)

@given(instance=nonemf::MySerializableClass_strategy)
def test_nonemf::myserializableclass_somethingInteresting_type(instance):
    assert isinstance(instance.somethingInteresting, str)


@given(instance=nonemf::MySerializableClass_strategy)
def test_nonemf::myserializableclass_somethingInteresting_setter(instance):
    original = instance.somethingInteresting
    instance.somethingInteresting = original
    assert instance.somethingInteresting == original

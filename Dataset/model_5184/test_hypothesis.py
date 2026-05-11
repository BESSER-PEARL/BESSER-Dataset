import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B,
    A,
    MultipleInheritance::C,
    Object,
    MultipleInheritance::D,
    MultipleInheritance::B,
    MultipleInheritance::A,
    MultipleInheritance::Object,
    MultipleInheritance::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance::c_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance::C)


def test_multipleinheritance::c_constructor_exists():
    assert callable(MultipleInheritance::C.__init__)


def test_multipleinheritance::c_constructor_args():
    sig = inspect.signature(MultipleInheritance::C.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance::d_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance::D)


def test_multipleinheritance::d_constructor_exists():
    assert callable(MultipleInheritance::D.__init__)


def test_multipleinheritance::d_constructor_args():
    sig = inspect.signature(MultipleInheritance::D.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance::b_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance::B)


def test_multipleinheritance::b_constructor_exists():
    assert callable(MultipleInheritance::B.__init__)


def test_multipleinheritance::b_constructor_args():
    sig = inspect.signature(MultipleInheritance::B.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance::a_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance::A)


def test_multipleinheritance::a_constructor_exists():
    assert callable(MultipleInheritance::A.__init__)


def test_multipleinheritance::a_constructor_args():
    sig = inspect.signature(MultipleInheritance::A.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance::object_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance::Object)


def test_multipleinheritance::object_constructor_exists():
    assert callable(MultipleInheritance::Object.__init__)


def test_multipleinheritance::object_constructor_args():
    sig = inspect.signature(MultipleInheritance::Object.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance::model_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance::Model)


def test_multipleinheritance::model_constructor_exists():
    assert callable(MultipleInheritance::Model.__init__)


def test_multipleinheritance::model_constructor_args():
    sig = inspect.signature(MultipleInheritance::Model.__init__)
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
B_strategy = st.builds(
    B,
)
A_strategy = st.builds(
    A,
)
MultipleInheritance::C_strategy = st.builds(
    MultipleInheritance::C,
)
Object_strategy = st.builds(
    Object,
)
MultipleInheritance::D_strategy = st.builds(
    MultipleInheritance::D,
)
MultipleInheritance::B_strategy = st.builds(
    MultipleInheritance::B,
)
MultipleInheritance::A_strategy = st.builds(
    MultipleInheritance::A,
)
MultipleInheritance::Object_strategy = st.builds(
    MultipleInheritance::Object,
)
MultipleInheritance::Model_strategy = st.builds(
    MultipleInheritance::Model,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=MultipleInheritance::C_strategy)
@settings(max_examples=50)
def test_multipleinheritance::c_instantiation(instance):
    assert isinstance(instance, MultipleInheritance::C)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=MultipleInheritance::D_strategy)
@settings(max_examples=50)
def test_multipleinheritance::d_instantiation(instance):
    assert isinstance(instance, MultipleInheritance::D)

@given(instance=MultipleInheritance::B_strategy)
@settings(max_examples=50)
def test_multipleinheritance::b_instantiation(instance):
    assert isinstance(instance, MultipleInheritance::B)

@given(instance=MultipleInheritance::A_strategy)
@settings(max_examples=50)
def test_multipleinheritance::a_instantiation(instance):
    assert isinstance(instance, MultipleInheritance::A)

@given(instance=MultipleInheritance::Object_strategy)
@settings(max_examples=50)
def test_multipleinheritance::object_instantiation(instance):
    assert isinstance(instance, MultipleInheritance::Object)

@given(instance=MultipleInheritance::Model_strategy)
@settings(max_examples=50)
def test_multipleinheritance::model_instantiation(instance):
    assert isinstance(instance, MultipleInheritance::Model)

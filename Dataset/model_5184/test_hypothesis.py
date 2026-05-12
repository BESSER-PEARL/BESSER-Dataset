import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B,
    A,
    MultipleInheritance_C,
    Object,
    MultipleInheritance_D,
    MultipleInheritance_B,
    MultipleInheritance_A,
    MultipleInheritance_Object,
    MultipleInheritance_Model,
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



def test_multipleinheritance_c_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance_C)


def test_multipleinheritance_c_constructor_exists():
    assert callable(MultipleInheritance_C.__init__)


def test_multipleinheritance_c_constructor_args():
    sig = inspect.signature(MultipleInheritance_C.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance_d_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance_D)


def test_multipleinheritance_d_constructor_exists():
    assert callable(MultipleInheritance_D.__init__)


def test_multipleinheritance_d_constructor_args():
    sig = inspect.signature(MultipleInheritance_D.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance_b_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance_B)


def test_multipleinheritance_b_constructor_exists():
    assert callable(MultipleInheritance_B.__init__)


def test_multipleinheritance_b_constructor_args():
    sig = inspect.signature(MultipleInheritance_B.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance_a_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance_A)


def test_multipleinheritance_a_constructor_exists():
    assert callable(MultipleInheritance_A.__init__)


def test_multipleinheritance_a_constructor_args():
    sig = inspect.signature(MultipleInheritance_A.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance_object_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance_Object)


def test_multipleinheritance_object_constructor_exists():
    assert callable(MultipleInheritance_Object.__init__)


def test_multipleinheritance_object_constructor_args():
    sig = inspect.signature(MultipleInheritance_Object.__init__)
    params = list(sig.parameters.keys())



def test_multipleinheritance_model_is_not_abstract():
    assert not inspect.isabstract(MultipleInheritance_Model)


def test_multipleinheritance_model_constructor_exists():
    assert callable(MultipleInheritance_Model.__init__)


def test_multipleinheritance_model_constructor_args():
    sig = inspect.signature(MultipleInheritance_Model.__init__)
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
MultipleInheritance_C_strategy = st.builds(
    MultipleInheritance_C,
)
Object_strategy = st.builds(
    Object,
)
MultipleInheritance_D_strategy = st.builds(
    MultipleInheritance_D,
)
MultipleInheritance_B_strategy = st.builds(
    MultipleInheritance_B,
)
MultipleInheritance_A_strategy = st.builds(
    MultipleInheritance_A,
)
MultipleInheritance_Object_strategy = st.builds(
    MultipleInheritance_Object,
)
MultipleInheritance_Model_strategy = st.builds(
    MultipleInheritance_Model,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=MultipleInheritance_C_strategy)
@settings(max_examples=50)
def test_multipleinheritance_c_instantiation(instance):
    assert isinstance(instance, MultipleInheritance_C)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=MultipleInheritance_D_strategy)
@settings(max_examples=50)
def test_multipleinheritance_d_instantiation(instance):
    assert isinstance(instance, MultipleInheritance_D)

@given(instance=MultipleInheritance_B_strategy)
@settings(max_examples=50)
def test_multipleinheritance_b_instantiation(instance):
    assert isinstance(instance, MultipleInheritance_B)

@given(instance=MultipleInheritance_A_strategy)
@settings(max_examples=50)
def test_multipleinheritance_a_instantiation(instance):
    assert isinstance(instance, MultipleInheritance_A)

@given(instance=MultipleInheritance_Object_strategy)
@settings(max_examples=50)
def test_multipleinheritance_object_instantiation(instance):
    assert isinstance(instance, MultipleInheritance_Object)

@given(instance=MultipleInheritance_Model_strategy)
@settings(max_examples=50)
def test_multipleinheritance_model_instantiation(instance):
    assert isinstance(instance, MultipleInheritance_Model)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    link_Named,
    Named,
    link_D,
    link_W,
    link_K,
    link_N99,
    link_C,
    link_M,
    link_B,
    link_X,
    link_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_link_named_is_not_abstract():
    assert not inspect.isabstract(link_Named)


def test_link_named_constructor_exists():
    assert callable(link_Named.__init__)


def test_link_named_constructor_args():
    sig = inspect.signature(link_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_link_named_has_name():
    assert hasattr(link_Named, "name")
    descriptor = None
    for klass in link_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_link_d_is_not_abstract():
    assert not inspect.isabstract(link_D)


def test_link_d_constructor_exists():
    assert callable(link_D.__init__)


def test_link_d_constructor_args():
    sig = inspect.signature(link_D.__init__)
    params = list(sig.parameters.keys())



def test_link_w_is_not_abstract():
    assert not inspect.isabstract(link_W)


def test_link_w_constructor_exists():
    assert callable(link_W.__init__)


def test_link_w_constructor_args():
    sig = inspect.signature(link_W.__init__)
    params = list(sig.parameters.keys())



def test_link_k_is_not_abstract():
    assert not inspect.isabstract(link_K)


def test_link_k_constructor_exists():
    assert callable(link_K.__init__)


def test_link_k_constructor_args():
    sig = inspect.signature(link_K.__init__)
    params = list(sig.parameters.keys())



def test_link_n99_is_not_abstract():
    assert not inspect.isabstract(link_N99)


def test_link_n99_constructor_exists():
    assert callable(link_N99.__init__)


def test_link_n99_constructor_args():
    sig = inspect.signature(link_N99.__init__)
    params = list(sig.parameters.keys())



def test_link_c_is_not_abstract():
    assert not inspect.isabstract(link_C)


def test_link_c_constructor_exists():
    assert callable(link_C.__init__)


def test_link_c_constructor_args():
    sig = inspect.signature(link_C.__init__)
    params = list(sig.parameters.keys())



def test_link_m_is_not_abstract():
    assert not inspect.isabstract(link_M)


def test_link_m_constructor_exists():
    assert callable(link_M.__init__)


def test_link_m_constructor_args():
    sig = inspect.signature(link_M.__init__)
    params = list(sig.parameters.keys())



def test_link_b_is_not_abstract():
    assert not inspect.isabstract(link_B)


def test_link_b_constructor_exists():
    assert callable(link_B.__init__)


def test_link_b_constructor_args():
    sig = inspect.signature(link_B.__init__)
    params = list(sig.parameters.keys())



def test_link_x_is_not_abstract():
    assert not inspect.isabstract(link_X)


def test_link_x_constructor_exists():
    assert callable(link_X.__init__)


def test_link_x_constructor_args():
    sig = inspect.signature(link_X.__init__)
    params = list(sig.parameters.keys())



def test_link_a_is_not_abstract():
    assert not inspect.isabstract(link_A)


def test_link_a_constructor_exists():
    assert callable(link_A.__init__)


def test_link_a_constructor_args():
    sig = inspect.signature(link_A.__init__)
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
link_Named_strategy = st.builds(
    link_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
link_D_strategy = st.builds(
    link_D,
)
link_W_strategy = st.builds(
    link_W,
)
link_K_strategy = st.builds(
    link_K,
)
link_N99_strategy = st.builds(
    link_N99,
)
link_C_strategy = st.builds(
    link_C,
)
link_M_strategy = st.builds(
    link_M,
)
link_B_strategy = st.builds(
    link_B,
)
link_X_strategy = st.builds(
    link_X,
)
link_A_strategy = st.builds(
    link_A,
)

@given(instance=link_Named_strategy)
@settings(max_examples=50)
def test_link_named_instantiation(instance):
    assert isinstance(instance, link_Named)



@given(instance=link_Named_strategy)
def test_link_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=link_D_strategy)
@settings(max_examples=50)
def test_link_d_instantiation(instance):
    assert isinstance(instance, link_D)

@given(instance=link_W_strategy)
@settings(max_examples=50)
def test_link_w_instantiation(instance):
    assert isinstance(instance, link_W)

@given(instance=link_K_strategy)
@settings(max_examples=50)
def test_link_k_instantiation(instance):
    assert isinstance(instance, link_K)

@given(instance=link_N99_strategy)
@settings(max_examples=50)
def test_link_n99_instantiation(instance):
    assert isinstance(instance, link_N99)

@given(instance=link_C_strategy)
@settings(max_examples=50)
def test_link_c_instantiation(instance):
    assert isinstance(instance, link_C)

@given(instance=link_M_strategy)
@settings(max_examples=50)
def test_link_m_instantiation(instance):
    assert isinstance(instance, link_M)

@given(instance=link_B_strategy)
@settings(max_examples=50)
def test_link_b_instantiation(instance):
    assert isinstance(instance, link_B)

@given(instance=link_X_strategy)
@settings(max_examples=50)
def test_link_x_instantiation(instance):
    assert isinstance(instance, link_X)

@given(instance=link_A_strategy)
@settings(max_examples=50)
def test_link_a_instantiation(instance):
    assert isinstance(instance, link_A)

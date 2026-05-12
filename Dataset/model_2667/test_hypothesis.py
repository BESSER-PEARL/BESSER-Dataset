import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mydsl_W,
    W,
    mydsl_L,
    mydsl_D,
    mydsl_B,
    mydsl_C,
    mydsl_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_w_is_not_abstract():
    assert not inspect.isabstract(mydsl_W)


def test_mydsl_w_constructor_exists():
    assert callable(mydsl_W.__init__)


def test_mydsl_w_constructor_args():
    sig = inspect.signature(mydsl_W.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_w_has_name():
    assert hasattr(mydsl_W, "name")
    descriptor = None
    for klass in mydsl_W.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_w_is_not_abstract():
    assert not inspect.isabstract(W)


def test_w_constructor_exists():
    assert callable(W.__init__)


def test_w_constructor_args():
    sig = inspect.signature(W.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_l_is_not_abstract():
    assert not inspect.isabstract(mydsl_L)


def test_mydsl_l_constructor_exists():
    assert callable(mydsl_L.__init__)


def test_mydsl_l_constructor_args():
    sig = inspect.signature(mydsl_L.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_d_is_not_abstract():
    assert not inspect.isabstract(mydsl_D)


def test_mydsl_d_constructor_exists():
    assert callable(mydsl_D.__init__)


def test_mydsl_d_constructor_args():
    sig = inspect.signature(mydsl_D.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_b_is_not_abstract():
    assert not inspect.isabstract(mydsl_B)


def test_mydsl_b_constructor_exists():
    assert callable(mydsl_B.__init__)


def test_mydsl_b_constructor_args():
    sig = inspect.signature(mydsl_B.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_c_is_not_abstract():
    assert not inspect.isabstract(mydsl_C)


def test_mydsl_c_constructor_exists():
    assert callable(mydsl_C.__init__)


def test_mydsl_c_constructor_args():
    sig = inspect.signature(mydsl_C.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_a_is_not_abstract():
    assert not inspect.isabstract(mydsl_A)


def test_mydsl_a_constructor_exists():
    assert callable(mydsl_A.__init__)


def test_mydsl_a_constructor_args():
    sig = inspect.signature(mydsl_A.__init__)
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
mydsl_W_strategy = st.builds(
    mydsl_W,
    name=
        safe_text
)
W_strategy = st.builds(
    W,
)
mydsl_L_strategy = st.builds(
    mydsl_L,
)
mydsl_D_strategy = st.builds(
    mydsl_D,
)
mydsl_B_strategy = st.builds(
    mydsl_B,
)
mydsl_C_strategy = st.builds(
    mydsl_C,
)
mydsl_A_strategy = st.builds(
    mydsl_A,
)

@given(instance=mydsl_W_strategy)
@settings(max_examples=50)
def test_mydsl_w_instantiation(instance):
    assert isinstance(instance, mydsl_W)



@given(instance=mydsl_W_strategy)
def test_mydsl_w_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=W_strategy)
@settings(max_examples=50)
def test_w_instantiation(instance):
    assert isinstance(instance, W)

@given(instance=mydsl_L_strategy)
@settings(max_examples=50)
def test_mydsl_l_instantiation(instance):
    assert isinstance(instance, mydsl_L)

@given(instance=mydsl_D_strategy)
@settings(max_examples=50)
def test_mydsl_d_instantiation(instance):
    assert isinstance(instance, mydsl_D)

@given(instance=mydsl_B_strategy)
@settings(max_examples=50)
def test_mydsl_b_instantiation(instance):
    assert isinstance(instance, mydsl_B)

@given(instance=mydsl_C_strategy)
@settings(max_examples=50)
def test_mydsl_c_instantiation(instance):
    assert isinstance(instance, mydsl_C)

@given(instance=mydsl_A_strategy)
@settings(max_examples=50)
def test_mydsl_a_instantiation(instance):
    assert isinstance(instance, mydsl_A)

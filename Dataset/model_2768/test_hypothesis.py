import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    D,
    ref3_Named,
    Named,
    ref3_A,
    ref3_E,
    ref3_T,
    ref3_B,
    ref3_N,
    T,
    ref3_D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_d_constructor_exists():
    assert callable(D.__init__)


def test_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_ref3_named_is_not_abstract():
    assert not inspect.isabstract(ref3_Named)


def test_ref3_named_constructor_exists():
    assert callable(ref3_Named.__init__)


def test_ref3_named_constructor_args():
    sig = inspect.signature(ref3_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ref3_named_has_name():
    assert hasattr(ref3_Named, "name")
    descriptor = None
    for klass in ref3_Named.__mro__:
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



def test_ref3_a_is_not_abstract():
    assert not inspect.isabstract(ref3_A)


def test_ref3_a_constructor_exists():
    assert callable(ref3_A.__init__)


def test_ref3_a_constructor_args():
    sig = inspect.signature(ref3_A.__init__)
    params = list(sig.parameters.keys())



def test_ref3_e_is_not_abstract():
    assert not inspect.isabstract(ref3_E)


def test_ref3_e_constructor_exists():
    assert callable(ref3_E.__init__)


def test_ref3_e_constructor_args():
    sig = inspect.signature(ref3_E.__init__)
    params = list(sig.parameters.keys())



def test_ref3_t_is_not_abstract():
    assert not inspect.isabstract(ref3_T)


def test_ref3_t_constructor_exists():
    assert callable(ref3_T.__init__)


def test_ref3_t_constructor_args():
    sig = inspect.signature(ref3_T.__init__)
    params = list(sig.parameters.keys())



def test_ref3_b_is_not_abstract():
    assert not inspect.isabstract(ref3_B)


def test_ref3_b_constructor_exists():
    assert callable(ref3_B.__init__)


def test_ref3_b_constructor_args():
    sig = inspect.signature(ref3_B.__init__)
    params = list(sig.parameters.keys())



def test_ref3_n_is_not_abstract():
    assert not inspect.isabstract(ref3_N)


def test_ref3_n_constructor_exists():
    assert callable(ref3_N.__init__)


def test_ref3_n_constructor_args():
    sig = inspect.signature(ref3_N.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_ref3_d_is_not_abstract():
    assert not inspect.isabstract(ref3_D)


def test_ref3_d_constructor_exists():
    assert callable(ref3_D.__init__)


def test_ref3_d_constructor_args():
    sig = inspect.signature(ref3_D.__init__)
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
D_strategy = st.builds(
    D,
)
ref3_Named_strategy = st.builds(
    ref3_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
ref3_A_strategy = st.builds(
    ref3_A,
)
ref3_E_strategy = st.builds(
    ref3_E,
)
ref3_T_strategy = st.builds(
    ref3_T,
)
ref3_B_strategy = st.builds(
    ref3_B,
)
ref3_N_strategy = st.builds(
    ref3_N,
)
T_strategy = st.builds(
    T,
)
ref3_D_strategy = st.builds(
    ref3_D,
)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=ref3_Named_strategy)
@settings(max_examples=50)
def test_ref3_named_instantiation(instance):
    assert isinstance(instance, ref3_Named)



@given(instance=ref3_Named_strategy)
def test_ref3_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=ref3_A_strategy)
@settings(max_examples=50)
def test_ref3_a_instantiation(instance):
    assert isinstance(instance, ref3_A)

@given(instance=ref3_E_strategy)
@settings(max_examples=50)
def test_ref3_e_instantiation(instance):
    assert isinstance(instance, ref3_E)

@given(instance=ref3_T_strategy)
@settings(max_examples=50)
def test_ref3_t_instantiation(instance):
    assert isinstance(instance, ref3_T)

@given(instance=ref3_B_strategy)
@settings(max_examples=50)
def test_ref3_b_instantiation(instance):
    assert isinstance(instance, ref3_B)

@given(instance=ref3_N_strategy)
@settings(max_examples=50)
def test_ref3_n_instantiation(instance):
    assert isinstance(instance, ref3_N)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=ref3_D_strategy)
@settings(max_examples=50)
def test_ref3_d_instantiation(instance):
    assert isinstance(instance, ref3_D)

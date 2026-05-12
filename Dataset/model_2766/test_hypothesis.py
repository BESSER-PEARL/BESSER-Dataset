import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    D,
    case4_Named,
    Named,
    case4_T,
    case4_B,
    case4_A,
    case4_E,
    case4_N,
    T,
    case4_D,
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



def test_case4_named_is_not_abstract():
    assert not inspect.isabstract(case4_Named)


def test_case4_named_constructor_exists():
    assert callable(case4_Named.__init__)


def test_case4_named_constructor_args():
    sig = inspect.signature(case4_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_case4_named_has_name():
    assert hasattr(case4_Named, "name")
    descriptor = None
    for klass in case4_Named.__mro__:
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



def test_case4_t_is_not_abstract():
    assert not inspect.isabstract(case4_T)


def test_case4_t_constructor_exists():
    assert callable(case4_T.__init__)


def test_case4_t_constructor_args():
    sig = inspect.signature(case4_T.__init__)
    params = list(sig.parameters.keys())



def test_case4_b_is_not_abstract():
    assert not inspect.isabstract(case4_B)


def test_case4_b_constructor_exists():
    assert callable(case4_B.__init__)


def test_case4_b_constructor_args():
    sig = inspect.signature(case4_B.__init__)
    params = list(sig.parameters.keys())



def test_case4_a_is_not_abstract():
    assert not inspect.isabstract(case4_A)


def test_case4_a_constructor_exists():
    assert callable(case4_A.__init__)


def test_case4_a_constructor_args():
    sig = inspect.signature(case4_A.__init__)
    params = list(sig.parameters.keys())



def test_case4_e_is_not_abstract():
    assert not inspect.isabstract(case4_E)


def test_case4_e_constructor_exists():
    assert callable(case4_E.__init__)


def test_case4_e_constructor_args():
    sig = inspect.signature(case4_E.__init__)
    params = list(sig.parameters.keys())



def test_case4_n_is_not_abstract():
    assert not inspect.isabstract(case4_N)


def test_case4_n_constructor_exists():
    assert callable(case4_N.__init__)


def test_case4_n_constructor_args():
    sig = inspect.signature(case4_N.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_case4_d_is_not_abstract():
    assert not inspect.isabstract(case4_D)


def test_case4_d_constructor_exists():
    assert callable(case4_D.__init__)


def test_case4_d_constructor_args():
    sig = inspect.signature(case4_D.__init__)
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
case4_Named_strategy = st.builds(
    case4_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
case4_T_strategy = st.builds(
    case4_T,
)
case4_B_strategy = st.builds(
    case4_B,
)
case4_A_strategy = st.builds(
    case4_A,
)
case4_E_strategy = st.builds(
    case4_E,
)
case4_N_strategy = st.builds(
    case4_N,
)
T_strategy = st.builds(
    T,
)
case4_D_strategy = st.builds(
    case4_D,
)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=case4_Named_strategy)
@settings(max_examples=50)
def test_case4_named_instantiation(instance):
    assert isinstance(instance, case4_Named)



@given(instance=case4_Named_strategy)
def test_case4_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=case4_T_strategy)
@settings(max_examples=50)
def test_case4_t_instantiation(instance):
    assert isinstance(instance, case4_T)

@given(instance=case4_B_strategy)
@settings(max_examples=50)
def test_case4_b_instantiation(instance):
    assert isinstance(instance, case4_B)

@given(instance=case4_A_strategy)
@settings(max_examples=50)
def test_case4_a_instantiation(instance):
    assert isinstance(instance, case4_A)

@given(instance=case4_E_strategy)
@settings(max_examples=50)
def test_case4_e_instantiation(instance):
    assert isinstance(instance, case4_E)

@given(instance=case4_N_strategy)
@settings(max_examples=50)
def test_case4_n_instantiation(instance):
    assert isinstance(instance, case4_N)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=case4_D_strategy)
@settings(max_examples=50)
def test_case4_d_instantiation(instance):
    assert isinstance(instance, case4_D)

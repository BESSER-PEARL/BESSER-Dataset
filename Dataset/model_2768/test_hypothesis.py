import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    D,
    ref3::Named,
    Named,
    ref3::A,
    ref3::E,
    ref3::B,
    ref3::T,
    ref3::N,
    T,
    ref3::D,
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



def test_ref3::named_is_not_abstract():
    assert not inspect.isabstract(ref3::Named)


def test_ref3::named_constructor_exists():
    assert callable(ref3::Named.__init__)


def test_ref3::named_constructor_args():
    sig = inspect.signature(ref3::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ref3::named_has_name():
    assert hasattr(ref3::Named, "name")
    descriptor = None
    for klass in ref3::Named.__mro__:
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



def test_ref3::a_is_not_abstract():
    assert not inspect.isabstract(ref3::A)


def test_ref3::a_constructor_exists():
    assert callable(ref3::A.__init__)


def test_ref3::a_constructor_args():
    sig = inspect.signature(ref3::A.__init__)
    params = list(sig.parameters.keys())



def test_ref3::e_is_not_abstract():
    assert not inspect.isabstract(ref3::E)


def test_ref3::e_constructor_exists():
    assert callable(ref3::E.__init__)


def test_ref3::e_constructor_args():
    sig = inspect.signature(ref3::E.__init__)
    params = list(sig.parameters.keys())



def test_ref3::b_is_not_abstract():
    assert not inspect.isabstract(ref3::B)


def test_ref3::b_constructor_exists():
    assert callable(ref3::B.__init__)


def test_ref3::b_constructor_args():
    sig = inspect.signature(ref3::B.__init__)
    params = list(sig.parameters.keys())



def test_ref3::t_is_not_abstract():
    assert not inspect.isabstract(ref3::T)


def test_ref3::t_constructor_exists():
    assert callable(ref3::T.__init__)


def test_ref3::t_constructor_args():
    sig = inspect.signature(ref3::T.__init__)
    params = list(sig.parameters.keys())



def test_ref3::n_is_not_abstract():
    assert not inspect.isabstract(ref3::N)


def test_ref3::n_constructor_exists():
    assert callable(ref3::N.__init__)


def test_ref3::n_constructor_args():
    sig = inspect.signature(ref3::N.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_ref3::d_is_not_abstract():
    assert not inspect.isabstract(ref3::D)


def test_ref3::d_constructor_exists():
    assert callable(ref3::D.__init__)


def test_ref3::d_constructor_args():
    sig = inspect.signature(ref3::D.__init__)
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
ref3::Named_strategy = st.builds(
    ref3::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
ref3::A_strategy = st.builds(
    ref3::A,
)
ref3::E_strategy = st.builds(
    ref3::E,
)
ref3::B_strategy = st.builds(
    ref3::B,
)
ref3::T_strategy = st.builds(
    ref3::T,
)
ref3::N_strategy = st.builds(
    ref3::N,
)
T_strategy = st.builds(
    T,
)
ref3::D_strategy = st.builds(
    ref3::D,
)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=ref3::Named_strategy)
@settings(max_examples=50)
def test_ref3::named_instantiation(instance):
    assert isinstance(instance, ref3::Named)

@given(instance=ref3::Named_strategy)
def test_ref3::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ref3::Named_strategy)
def test_ref3::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=ref3::A_strategy)
@settings(max_examples=50)
def test_ref3::a_instantiation(instance):
    assert isinstance(instance, ref3::A)

@given(instance=ref3::E_strategy)
@settings(max_examples=50)
def test_ref3::e_instantiation(instance):
    assert isinstance(instance, ref3::E)

@given(instance=ref3::B_strategy)
@settings(max_examples=50)
def test_ref3::b_instantiation(instance):
    assert isinstance(instance, ref3::B)

@given(instance=ref3::T_strategy)
@settings(max_examples=50)
def test_ref3::t_instantiation(instance):
    assert isinstance(instance, ref3::T)

@given(instance=ref3::N_strategy)
@settings(max_examples=50)
def test_ref3::n_instantiation(instance):
    assert isinstance(instance, ref3::N)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=ref3::D_strategy)
@settings(max_examples=50)
def test_ref3::d_instantiation(instance):
    assert isinstance(instance, ref3::D)

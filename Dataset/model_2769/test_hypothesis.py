import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    D,
    v125case5::Named,
    Named,
    v125case5::E,
    v125case5::B,
    v125case5::T,
    v125case5::A,
    v125case5::N,
    T,
    v125case5::D,
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



def test_v125case5::named_is_not_abstract():
    assert not inspect.isabstract(v125case5::Named)


def test_v125case5::named_constructor_exists():
    assert callable(v125case5::Named.__init__)


def test_v125case5::named_constructor_args():
    sig = inspect.signature(v125case5::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_v125case5::named_has_name():
    assert hasattr(v125case5::Named, "name")
    descriptor = None
    for klass in v125case5::Named.__mro__:
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



def test_v125case5::e_is_not_abstract():
    assert not inspect.isabstract(v125case5::E)


def test_v125case5::e_constructor_exists():
    assert callable(v125case5::E.__init__)


def test_v125case5::e_constructor_args():
    sig = inspect.signature(v125case5::E.__init__)
    params = list(sig.parameters.keys())



def test_v125case5::b_is_not_abstract():
    assert not inspect.isabstract(v125case5::B)


def test_v125case5::b_constructor_exists():
    assert callable(v125case5::B.__init__)


def test_v125case5::b_constructor_args():
    sig = inspect.signature(v125case5::B.__init__)
    params = list(sig.parameters.keys())



def test_v125case5::t_is_not_abstract():
    assert not inspect.isabstract(v125case5::T)


def test_v125case5::t_constructor_exists():
    assert callable(v125case5::T.__init__)


def test_v125case5::t_constructor_args():
    sig = inspect.signature(v125case5::T.__init__)
    params = list(sig.parameters.keys())



def test_v125case5::a_is_not_abstract():
    assert not inspect.isabstract(v125case5::A)


def test_v125case5::a_constructor_exists():
    assert callable(v125case5::A.__init__)


def test_v125case5::a_constructor_args():
    sig = inspect.signature(v125case5::A.__init__)
    params = list(sig.parameters.keys())



def test_v125case5::n_is_not_abstract():
    assert not inspect.isabstract(v125case5::N)


def test_v125case5::n_constructor_exists():
    assert callable(v125case5::N.__init__)


def test_v125case5::n_constructor_args():
    sig = inspect.signature(v125case5::N.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_v125case5::d_is_not_abstract():
    assert not inspect.isabstract(v125case5::D)


def test_v125case5::d_constructor_exists():
    assert callable(v125case5::D.__init__)


def test_v125case5::d_constructor_args():
    sig = inspect.signature(v125case5::D.__init__)
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
v125case5::Named_strategy = st.builds(
    v125case5::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
v125case5::E_strategy = st.builds(
    v125case5::E,
)
v125case5::B_strategy = st.builds(
    v125case5::B,
)
v125case5::T_strategy = st.builds(
    v125case5::T,
)
v125case5::A_strategy = st.builds(
    v125case5::A,
)
v125case5::N_strategy = st.builds(
    v125case5::N,
)
T_strategy = st.builds(
    T,
)
v125case5::D_strategy = st.builds(
    v125case5::D,
)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=v125case5::Named_strategy)
@settings(max_examples=50)
def test_v125case5::named_instantiation(instance):
    assert isinstance(instance, v125case5::Named)

@given(instance=v125case5::Named_strategy)
def test_v125case5::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=v125case5::Named_strategy)
def test_v125case5::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=v125case5::E_strategy)
@settings(max_examples=50)
def test_v125case5::e_instantiation(instance):
    assert isinstance(instance, v125case5::E)

@given(instance=v125case5::B_strategy)
@settings(max_examples=50)
def test_v125case5::b_instantiation(instance):
    assert isinstance(instance, v125case5::B)

@given(instance=v125case5::T_strategy)
@settings(max_examples=50)
def test_v125case5::t_instantiation(instance):
    assert isinstance(instance, v125case5::T)

@given(instance=v125case5::A_strategy)
@settings(max_examples=50)
def test_v125case5::a_instantiation(instance):
    assert isinstance(instance, v125case5::A)

@given(instance=v125case5::N_strategy)
@settings(max_examples=50)
def test_v125case5::n_instantiation(instance):
    assert isinstance(instance, v125case5::N)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=v125case5::D_strategy)
@settings(max_examples=50)
def test_v125case5::d_instantiation(instance):
    assert isinstance(instance, v125case5::D)

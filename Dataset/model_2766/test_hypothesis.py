import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    D,
    case4::Named,
    Named,
    case4::E,
    case4::T,
    case4::B,
    case4::A,
    case4::N,
    T,
    case4::D,
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



def test_case4::named_is_not_abstract():
    assert not inspect.isabstract(case4::Named)


def test_case4::named_constructor_exists():
    assert callable(case4::Named.__init__)


def test_case4::named_constructor_args():
    sig = inspect.signature(case4::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_case4::named_has_name():
    assert hasattr(case4::Named, "name")
    descriptor = None
    for klass in case4::Named.__mro__:
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



def test_case4::e_is_not_abstract():
    assert not inspect.isabstract(case4::E)


def test_case4::e_constructor_exists():
    assert callable(case4::E.__init__)


def test_case4::e_constructor_args():
    sig = inspect.signature(case4::E.__init__)
    params = list(sig.parameters.keys())



def test_case4::t_is_not_abstract():
    assert not inspect.isabstract(case4::T)


def test_case4::t_constructor_exists():
    assert callable(case4::T.__init__)


def test_case4::t_constructor_args():
    sig = inspect.signature(case4::T.__init__)
    params = list(sig.parameters.keys())



def test_case4::b_is_not_abstract():
    assert not inspect.isabstract(case4::B)


def test_case4::b_constructor_exists():
    assert callable(case4::B.__init__)


def test_case4::b_constructor_args():
    sig = inspect.signature(case4::B.__init__)
    params = list(sig.parameters.keys())



def test_case4::a_is_not_abstract():
    assert not inspect.isabstract(case4::A)


def test_case4::a_constructor_exists():
    assert callable(case4::A.__init__)


def test_case4::a_constructor_args():
    sig = inspect.signature(case4::A.__init__)
    params = list(sig.parameters.keys())



def test_case4::n_is_not_abstract():
    assert not inspect.isabstract(case4::N)


def test_case4::n_constructor_exists():
    assert callable(case4::N.__init__)


def test_case4::n_constructor_args():
    sig = inspect.signature(case4::N.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_case4::d_is_not_abstract():
    assert not inspect.isabstract(case4::D)


def test_case4::d_constructor_exists():
    assert callable(case4::D.__init__)


def test_case4::d_constructor_args():
    sig = inspect.signature(case4::D.__init__)
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
case4::Named_strategy = st.builds(
    case4::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
case4::E_strategy = st.builds(
    case4::E,
)
case4::T_strategy = st.builds(
    case4::T,
)
case4::B_strategy = st.builds(
    case4::B,
)
case4::A_strategy = st.builds(
    case4::A,
)
case4::N_strategy = st.builds(
    case4::N,
)
T_strategy = st.builds(
    T,
)
case4::D_strategy = st.builds(
    case4::D,
)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=case4::Named_strategy)
@settings(max_examples=50)
def test_case4::named_instantiation(instance):
    assert isinstance(instance, case4::Named)

@given(instance=case4::Named_strategy)
def test_case4::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=case4::Named_strategy)
def test_case4::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=case4::E_strategy)
@settings(max_examples=50)
def test_case4::e_instantiation(instance):
    assert isinstance(instance, case4::E)

@given(instance=case4::T_strategy)
@settings(max_examples=50)
def test_case4::t_instantiation(instance):
    assert isinstance(instance, case4::T)

@given(instance=case4::B_strategy)
@settings(max_examples=50)
def test_case4::b_instantiation(instance):
    assert isinstance(instance, case4::B)

@given(instance=case4::A_strategy)
@settings(max_examples=50)
def test_case4::a_instantiation(instance):
    assert isinstance(instance, case4::A)

@given(instance=case4::N_strategy)
@settings(max_examples=50)
def test_case4::n_instantiation(instance):
    assert isinstance(instance, case4::N)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=case4::D_strategy)
@settings(max_examples=50)
def test_case4::d_instantiation(instance):
    assert isinstance(instance, case4::D)

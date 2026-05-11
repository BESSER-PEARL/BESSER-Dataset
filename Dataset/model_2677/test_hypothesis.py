import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B,
    kref::Named,
    Named,
    kref::C,
    kref::E,
    kref::F,
    kref::H,
    kref::K,
    kref::J,
    kref::G,
    kref::B,
    kref::A,
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



def test_kref::named_is_not_abstract():
    assert not inspect.isabstract(kref::Named)


def test_kref::named_constructor_exists():
    assert callable(kref::Named.__init__)


def test_kref::named_constructor_args():
    sig = inspect.signature(kref::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kref::named_has_name():
    assert hasattr(kref::Named, "name")
    descriptor = None
    for klass in kref::Named.__mro__:
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



def test_kref::c_is_not_abstract():
    assert not inspect.isabstract(kref::C)


def test_kref::c_constructor_exists():
    assert callable(kref::C.__init__)


def test_kref::c_constructor_args():
    sig = inspect.signature(kref::C.__init__)
    params = list(sig.parameters.keys())



def test_kref::e_is_not_abstract():
    assert not inspect.isabstract(kref::E)


def test_kref::e_constructor_exists():
    assert callable(kref::E.__init__)


def test_kref::e_constructor_args():
    sig = inspect.signature(kref::E.__init__)
    params = list(sig.parameters.keys())



def test_kref::f_is_not_abstract():
    assert not inspect.isabstract(kref::F)


def test_kref::f_constructor_exists():
    assert callable(kref::F.__init__)


def test_kref::f_constructor_args():
    sig = inspect.signature(kref::F.__init__)
    params = list(sig.parameters.keys())



def test_kref::h_is_not_abstract():
    assert not inspect.isabstract(kref::H)


def test_kref::h_constructor_exists():
    assert callable(kref::H.__init__)


def test_kref::h_constructor_args():
    sig = inspect.signature(kref::H.__init__)
    params = list(sig.parameters.keys())



def test_kref::k_is_not_abstract():
    assert not inspect.isabstract(kref::K)


def test_kref::k_constructor_exists():
    assert callable(kref::K.__init__)


def test_kref::k_constructor_args():
    sig = inspect.signature(kref::K.__init__)
    params = list(sig.parameters.keys())



def test_kref::j_is_not_abstract():
    assert not inspect.isabstract(kref::J)


def test_kref::j_constructor_exists():
    assert callable(kref::J.__init__)


def test_kref::j_constructor_args():
    sig = inspect.signature(kref::J.__init__)
    params = list(sig.parameters.keys())



def test_kref::g_is_not_abstract():
    assert not inspect.isabstract(kref::G)


def test_kref::g_constructor_exists():
    assert callable(kref::G.__init__)


def test_kref::g_constructor_args():
    sig = inspect.signature(kref::G.__init__)
    params = list(sig.parameters.keys())



def test_kref::b_is_not_abstract():
    assert not inspect.isabstract(kref::B)


def test_kref::b_constructor_exists():
    assert callable(kref::B.__init__)


def test_kref::b_constructor_args():
    sig = inspect.signature(kref::B.__init__)
    params = list(sig.parameters.keys())



def test_kref::a_is_not_abstract():
    assert not inspect.isabstract(kref::A)


def test_kref::a_constructor_exists():
    assert callable(kref::A.__init__)


def test_kref::a_constructor_args():
    sig = inspect.signature(kref::A.__init__)
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
kref::Named_strategy = st.builds(
    kref::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
kref::C_strategy = st.builds(
    kref::C,
)
kref::E_strategy = st.builds(
    kref::E,
)
kref::F_strategy = st.builds(
    kref::F,
)
kref::H_strategy = st.builds(
    kref::H,
)
kref::K_strategy = st.builds(
    kref::K,
)
kref::J_strategy = st.builds(
    kref::J,
)
kref::G_strategy = st.builds(
    kref::G,
)
kref::B_strategy = st.builds(
    kref::B,
)
kref::A_strategy = st.builds(
    kref::A,
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=kref::Named_strategy)
@settings(max_examples=50)
def test_kref::named_instantiation(instance):
    assert isinstance(instance, kref::Named)

@given(instance=kref::Named_strategy)
def test_kref::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kref::Named_strategy)
def test_kref::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=kref::C_strategy)
@settings(max_examples=50)
def test_kref::c_instantiation(instance):
    assert isinstance(instance, kref::C)

@given(instance=kref::E_strategy)
@settings(max_examples=50)
def test_kref::e_instantiation(instance):
    assert isinstance(instance, kref::E)

@given(instance=kref::F_strategy)
@settings(max_examples=50)
def test_kref::f_instantiation(instance):
    assert isinstance(instance, kref::F)

@given(instance=kref::H_strategy)
@settings(max_examples=50)
def test_kref::h_instantiation(instance):
    assert isinstance(instance, kref::H)

@given(instance=kref::K_strategy)
@settings(max_examples=50)
def test_kref::k_instantiation(instance):
    assert isinstance(instance, kref::K)

@given(instance=kref::J_strategy)
@settings(max_examples=50)
def test_kref::j_instantiation(instance):
    assert isinstance(instance, kref::J)

@given(instance=kref::G_strategy)
@settings(max_examples=50)
def test_kref::g_instantiation(instance):
    assert isinstance(instance, kref::G)

@given(instance=kref::B_strategy)
@settings(max_examples=50)
def test_kref::b_instantiation(instance):
    assert isinstance(instance, kref::B)

@given(instance=kref::A_strategy)
@settings(max_examples=50)
def test_kref::a_instantiation(instance):
    assert isinstance(instance, kref::A)

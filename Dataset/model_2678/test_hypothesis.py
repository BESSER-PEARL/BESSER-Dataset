import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    D,
    refinher::F,
    K,
    F,
    refinher::I,
    B,
    refinher::D,
    Named,
    refinher::G,
    refinher::L,
    refinher::C,
    refinher::E,
    refinher::H,
    refinher::Named,
    refinher::K,
    refinher::B,
    refinher::A,
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



def test_refinher::f_is_not_abstract():
    assert not inspect.isabstract(refinher::F)


def test_refinher::f_constructor_exists():
    assert callable(refinher::F.__init__)


def test_refinher::f_constructor_args():
    sig = inspect.signature(refinher::F.__init__)
    params = list(sig.parameters.keys())



def test_k_is_not_abstract():
    assert not inspect.isabstract(K)


def test_k_constructor_exists():
    assert callable(K.__init__)


def test_k_constructor_args():
    sig = inspect.signature(K.__init__)
    params = list(sig.parameters.keys())



def test_f_is_not_abstract():
    assert not inspect.isabstract(F)


def test_f_constructor_exists():
    assert callable(F.__init__)


def test_f_constructor_args():
    sig = inspect.signature(F.__init__)
    params = list(sig.parameters.keys())



def test_refinher::i_is_not_abstract():
    assert not inspect.isabstract(refinher::I)


def test_refinher::i_constructor_exists():
    assert callable(refinher::I.__init__)


def test_refinher::i_constructor_args():
    sig = inspect.signature(refinher::I.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_refinher::d_is_not_abstract():
    assert not inspect.isabstract(refinher::D)


def test_refinher::d_constructor_exists():
    assert callable(refinher::D.__init__)


def test_refinher::d_constructor_args():
    sig = inspect.signature(refinher::D.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_refinher::g_is_not_abstract():
    assert not inspect.isabstract(refinher::G)


def test_refinher::g_constructor_exists():
    assert callable(refinher::G.__init__)


def test_refinher::g_constructor_args():
    sig = inspect.signature(refinher::G.__init__)
    params = list(sig.parameters.keys())



def test_refinher::l_is_not_abstract():
    assert not inspect.isabstract(refinher::L)


def test_refinher::l_constructor_exists():
    assert callable(refinher::L.__init__)


def test_refinher::l_constructor_args():
    sig = inspect.signature(refinher::L.__init__)
    params = list(sig.parameters.keys())



def test_refinher::c_is_not_abstract():
    assert not inspect.isabstract(refinher::C)


def test_refinher::c_constructor_exists():
    assert callable(refinher::C.__init__)


def test_refinher::c_constructor_args():
    sig = inspect.signature(refinher::C.__init__)
    params = list(sig.parameters.keys())



def test_refinher::e_is_not_abstract():
    assert not inspect.isabstract(refinher::E)


def test_refinher::e_constructor_exists():
    assert callable(refinher::E.__init__)


def test_refinher::e_constructor_args():
    sig = inspect.signature(refinher::E.__init__)
    params = list(sig.parameters.keys())



def test_refinher::h_is_not_abstract():
    assert not inspect.isabstract(refinher::H)


def test_refinher::h_constructor_exists():
    assert callable(refinher::H.__init__)


def test_refinher::h_constructor_args():
    sig = inspect.signature(refinher::H.__init__)
    params = list(sig.parameters.keys())



def test_refinher::named_is_not_abstract():
    assert not inspect.isabstract(refinher::Named)


def test_refinher::named_constructor_exists():
    assert callable(refinher::Named.__init__)


def test_refinher::named_constructor_args():
    sig = inspect.signature(refinher::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_refinher::named_has_name():
    assert hasattr(refinher::Named, "name")
    descriptor = None
    for klass in refinher::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_refinher::k_is_not_abstract():
    assert not inspect.isabstract(refinher::K)


def test_refinher::k_constructor_exists():
    assert callable(refinher::K.__init__)


def test_refinher::k_constructor_args():
    sig = inspect.signature(refinher::K.__init__)
    params = list(sig.parameters.keys())



def test_refinher::b_is_not_abstract():
    assert not inspect.isabstract(refinher::B)


def test_refinher::b_constructor_exists():
    assert callable(refinher::B.__init__)


def test_refinher::b_constructor_args():
    sig = inspect.signature(refinher::B.__init__)
    params = list(sig.parameters.keys())



def test_refinher::a_is_not_abstract():
    assert not inspect.isabstract(refinher::A)


def test_refinher::a_constructor_exists():
    assert callable(refinher::A.__init__)


def test_refinher::a_constructor_args():
    sig = inspect.signature(refinher::A.__init__)
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
refinher::F_strategy = st.builds(
    refinher::F,
)
K_strategy = st.builds(
    K,
)
F_strategy = st.builds(
    F,
)
refinher::I_strategy = st.builds(
    refinher::I,
)
B_strategy = st.builds(
    B,
)
refinher::D_strategy = st.builds(
    refinher::D,
)
Named_strategy = st.builds(
    Named,
)
refinher::G_strategy = st.builds(
    refinher::G,
)
refinher::L_strategy = st.builds(
    refinher::L,
)
refinher::C_strategy = st.builds(
    refinher::C,
)
refinher::E_strategy = st.builds(
    refinher::E,
)
refinher::H_strategy = st.builds(
    refinher::H,
)
refinher::Named_strategy = st.builds(
    refinher::Named,
    name=
        safe_text
)
refinher::K_strategy = st.builds(
    refinher::K,
)
refinher::B_strategy = st.builds(
    refinher::B,
)
refinher::A_strategy = st.builds(
    refinher::A,
)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=refinher::F_strategy)
@settings(max_examples=50)
def test_refinher::f_instantiation(instance):
    assert isinstance(instance, refinher::F)

@given(instance=K_strategy)
@settings(max_examples=50)
def test_k_instantiation(instance):
    assert isinstance(instance, K)

@given(instance=F_strategy)
@settings(max_examples=50)
def test_f_instantiation(instance):
    assert isinstance(instance, F)

@given(instance=refinher::I_strategy)
@settings(max_examples=50)
def test_refinher::i_instantiation(instance):
    assert isinstance(instance, refinher::I)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=refinher::D_strategy)
@settings(max_examples=50)
def test_refinher::d_instantiation(instance):
    assert isinstance(instance, refinher::D)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=refinher::G_strategy)
@settings(max_examples=50)
def test_refinher::g_instantiation(instance):
    assert isinstance(instance, refinher::G)

@given(instance=refinher::L_strategy)
@settings(max_examples=50)
def test_refinher::l_instantiation(instance):
    assert isinstance(instance, refinher::L)

@given(instance=refinher::C_strategy)
@settings(max_examples=50)
def test_refinher::c_instantiation(instance):
    assert isinstance(instance, refinher::C)

@given(instance=refinher::E_strategy)
@settings(max_examples=50)
def test_refinher::e_instantiation(instance):
    assert isinstance(instance, refinher::E)

@given(instance=refinher::H_strategy)
@settings(max_examples=50)
def test_refinher::h_instantiation(instance):
    assert isinstance(instance, refinher::H)

@given(instance=refinher::Named_strategy)
@settings(max_examples=50)
def test_refinher::named_instantiation(instance):
    assert isinstance(instance, refinher::Named)

@given(instance=refinher::Named_strategy)
def test_refinher::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=refinher::Named_strategy)
def test_refinher::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=refinher::K_strategy)
@settings(max_examples=50)
def test_refinher::k_instantiation(instance):
    assert isinstance(instance, refinher::K)

@given(instance=refinher::B_strategy)
@settings(max_examples=50)
def test_refinher::b_instantiation(instance):
    assert isinstance(instance, refinher::B)

@given(instance=refinher::A_strategy)
@settings(max_examples=50)
def test_refinher::a_instantiation(instance):
    assert isinstance(instance, refinher::A)

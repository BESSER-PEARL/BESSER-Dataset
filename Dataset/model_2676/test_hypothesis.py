import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    K,
    F,
    compmultinher::I,
    D,
    compmultinher::F,
    B,
    compmultinher::D,
    compmultinher::Named,
    Named,
    compmultinher::E,
    compmultinher::H,
    compmultinher::L,
    compmultinher::G,
    compmultinher::C,
    compmultinher::K,
    compmultinher::B,
    compmultinher::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_compmultinher::i_is_not_abstract():
    assert not inspect.isabstract(compmultinher::I)


def test_compmultinher::i_constructor_exists():
    assert callable(compmultinher::I.__init__)


def test_compmultinher::i_constructor_args():
    sig = inspect.signature(compmultinher::I.__init__)
    params = list(sig.parameters.keys())



def test_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_d_constructor_exists():
    assert callable(D.__init__)


def test_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_compmultinher::f_is_not_abstract():
    assert not inspect.isabstract(compmultinher::F)


def test_compmultinher::f_constructor_exists():
    assert callable(compmultinher::F.__init__)


def test_compmultinher::f_constructor_args():
    sig = inspect.signature(compmultinher::F.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_compmultinher::d_is_not_abstract():
    assert not inspect.isabstract(compmultinher::D)


def test_compmultinher::d_constructor_exists():
    assert callable(compmultinher::D.__init__)


def test_compmultinher::d_constructor_args():
    sig = inspect.signature(compmultinher::D.__init__)
    params = list(sig.parameters.keys())



def test_compmultinher::named_is_not_abstract():
    assert not inspect.isabstract(compmultinher::Named)


def test_compmultinher::named_constructor_exists():
    assert callable(compmultinher::Named.__init__)


def test_compmultinher::named_constructor_args():
    sig = inspect.signature(compmultinher::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_compmultinher::named_has_name():
    assert hasattr(compmultinher::Named, "name")
    descriptor = None
    for klass in compmultinher::Named.__mro__:
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



def test_compmultinher::e_is_not_abstract():
    assert not inspect.isabstract(compmultinher::E)


def test_compmultinher::e_constructor_exists():
    assert callable(compmultinher::E.__init__)


def test_compmultinher::e_constructor_args():
    sig = inspect.signature(compmultinher::E.__init__)
    params = list(sig.parameters.keys())



def test_compmultinher::h_is_not_abstract():
    assert not inspect.isabstract(compmultinher::H)


def test_compmultinher::h_constructor_exists():
    assert callable(compmultinher::H.__init__)


def test_compmultinher::h_constructor_args():
    sig = inspect.signature(compmultinher::H.__init__)
    params = list(sig.parameters.keys())



def test_compmultinher::l_is_not_abstract():
    assert not inspect.isabstract(compmultinher::L)


def test_compmultinher::l_constructor_exists():
    assert callable(compmultinher::L.__init__)


def test_compmultinher::l_constructor_args():
    sig = inspect.signature(compmultinher::L.__init__)
    params = list(sig.parameters.keys())



def test_compmultinher::g_is_not_abstract():
    assert not inspect.isabstract(compmultinher::G)


def test_compmultinher::g_constructor_exists():
    assert callable(compmultinher::G.__init__)


def test_compmultinher::g_constructor_args():
    sig = inspect.signature(compmultinher::G.__init__)
    params = list(sig.parameters.keys())



def test_compmultinher::c_is_not_abstract():
    assert not inspect.isabstract(compmultinher::C)


def test_compmultinher::c_constructor_exists():
    assert callable(compmultinher::C.__init__)


def test_compmultinher::c_constructor_args():
    sig = inspect.signature(compmultinher::C.__init__)
    params = list(sig.parameters.keys())



def test_compmultinher::k_is_not_abstract():
    assert not inspect.isabstract(compmultinher::K)


def test_compmultinher::k_constructor_exists():
    assert callable(compmultinher::K.__init__)


def test_compmultinher::k_constructor_args():
    sig = inspect.signature(compmultinher::K.__init__)
    params = list(sig.parameters.keys())



def test_compmultinher::b_is_not_abstract():
    assert not inspect.isabstract(compmultinher::B)


def test_compmultinher::b_constructor_exists():
    assert callable(compmultinher::B.__init__)


def test_compmultinher::b_constructor_args():
    sig = inspect.signature(compmultinher::B.__init__)
    params = list(sig.parameters.keys())



def test_compmultinher::a_is_not_abstract():
    assert not inspect.isabstract(compmultinher::A)


def test_compmultinher::a_constructor_exists():
    assert callable(compmultinher::A.__init__)


def test_compmultinher::a_constructor_args():
    sig = inspect.signature(compmultinher::A.__init__)
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
K_strategy = st.builds(
    K,
)
F_strategy = st.builds(
    F,
)
compmultinher::I_strategy = st.builds(
    compmultinher::I,
)
D_strategy = st.builds(
    D,
)
compmultinher::F_strategy = st.builds(
    compmultinher::F,
)
B_strategy = st.builds(
    B,
)
compmultinher::D_strategy = st.builds(
    compmultinher::D,
)
compmultinher::Named_strategy = st.builds(
    compmultinher::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
compmultinher::E_strategy = st.builds(
    compmultinher::E,
)
compmultinher::H_strategy = st.builds(
    compmultinher::H,
)
compmultinher::L_strategy = st.builds(
    compmultinher::L,
)
compmultinher::G_strategy = st.builds(
    compmultinher::G,
)
compmultinher::C_strategy = st.builds(
    compmultinher::C,
)
compmultinher::K_strategy = st.builds(
    compmultinher::K,
)
compmultinher::B_strategy = st.builds(
    compmultinher::B,
)
compmultinher::A_strategy = st.builds(
    compmultinher::A,
)

@given(instance=K_strategy)
@settings(max_examples=50)
def test_k_instantiation(instance):
    assert isinstance(instance, K)

@given(instance=F_strategy)
@settings(max_examples=50)
def test_f_instantiation(instance):
    assert isinstance(instance, F)

@given(instance=compmultinher::I_strategy)
@settings(max_examples=50)
def test_compmultinher::i_instantiation(instance):
    assert isinstance(instance, compmultinher::I)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=compmultinher::F_strategy)
@settings(max_examples=50)
def test_compmultinher::f_instantiation(instance):
    assert isinstance(instance, compmultinher::F)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=compmultinher::D_strategy)
@settings(max_examples=50)
def test_compmultinher::d_instantiation(instance):
    assert isinstance(instance, compmultinher::D)

@given(instance=compmultinher::Named_strategy)
@settings(max_examples=50)
def test_compmultinher::named_instantiation(instance):
    assert isinstance(instance, compmultinher::Named)

@given(instance=compmultinher::Named_strategy)
def test_compmultinher::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=compmultinher::Named_strategy)
def test_compmultinher::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=compmultinher::E_strategy)
@settings(max_examples=50)
def test_compmultinher::e_instantiation(instance):
    assert isinstance(instance, compmultinher::E)

@given(instance=compmultinher::H_strategy)
@settings(max_examples=50)
def test_compmultinher::h_instantiation(instance):
    assert isinstance(instance, compmultinher::H)

@given(instance=compmultinher::L_strategy)
@settings(max_examples=50)
def test_compmultinher::l_instantiation(instance):
    assert isinstance(instance, compmultinher::L)

@given(instance=compmultinher::G_strategy)
@settings(max_examples=50)
def test_compmultinher::g_instantiation(instance):
    assert isinstance(instance, compmultinher::G)

@given(instance=compmultinher::C_strategy)
@settings(max_examples=50)
def test_compmultinher::c_instantiation(instance):
    assert isinstance(instance, compmultinher::C)

@given(instance=compmultinher::K_strategy)
@settings(max_examples=50)
def test_compmultinher::k_instantiation(instance):
    assert isinstance(instance, compmultinher::K)

@given(instance=compmultinher::B_strategy)
@settings(max_examples=50)
def test_compmultinher::b_instantiation(instance):
    assert isinstance(instance, compmultinher::B)

@given(instance=compmultinher::A_strategy)
@settings(max_examples=50)
def test_compmultinher::a_instantiation(instance):
    assert isinstance(instance, compmultinher::A)

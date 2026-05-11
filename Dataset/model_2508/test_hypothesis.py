import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    visualinher::N,
    N,
    visualinher::C,
    A,
    visualinher::I,
    visualinher::D,
    visualinher::E,
    I,
    visualinher::B,
    visualinher::R,
    visualinher::A,
    visualinher::S,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_visualinher::n_is_not_abstract():
    assert not inspect.isabstract(visualinher::N)


def test_visualinher::n_constructor_exists():
    assert callable(visualinher::N.__init__)


def test_visualinher::n_constructor_args():
    sig = inspect.signature(visualinher::N.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_visualinher::n_has_name():
    assert hasattr(visualinher::N, "name")
    descriptor = None
    for klass in visualinher::N.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_n_is_not_abstract():
    assert not inspect.isabstract(N)


def test_n_constructor_exists():
    assert callable(N.__init__)


def test_n_constructor_args():
    sig = inspect.signature(N.__init__)
    params = list(sig.parameters.keys())



def test_visualinher::c_is_not_abstract():
    assert not inspect.isabstract(visualinher::C)


def test_visualinher::c_constructor_exists():
    assert callable(visualinher::C.__init__)


def test_visualinher::c_constructor_args():
    sig = inspect.signature(visualinher::C.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_visualinher::i_is_not_abstract():
    assert not inspect.isabstract(visualinher::I)


def test_visualinher::i_constructor_exists():
    assert callable(visualinher::I.__init__)


def test_visualinher::i_constructor_args():
    sig = inspect.signature(visualinher::I.__init__)
    params = list(sig.parameters.keys())



def test_visualinher::d_is_not_abstract():
    assert not inspect.isabstract(visualinher::D)


def test_visualinher::d_constructor_exists():
    assert callable(visualinher::D.__init__)


def test_visualinher::d_constructor_args():
    sig = inspect.signature(visualinher::D.__init__)
    params = list(sig.parameters.keys())



def test_visualinher::e_is_not_abstract():
    assert not inspect.isabstract(visualinher::E)


def test_visualinher::e_constructor_exists():
    assert callable(visualinher::E.__init__)


def test_visualinher::e_constructor_args():
    sig = inspect.signature(visualinher::E.__init__)
    params = list(sig.parameters.keys())



def test_i_is_not_abstract():
    assert not inspect.isabstract(I)


def test_i_constructor_exists():
    assert callable(I.__init__)


def test_i_constructor_args():
    sig = inspect.signature(I.__init__)
    params = list(sig.parameters.keys())



def test_visualinher::b_is_not_abstract():
    assert not inspect.isabstract(visualinher::B)


def test_visualinher::b_constructor_exists():
    assert callable(visualinher::B.__init__)


def test_visualinher::b_constructor_args():
    sig = inspect.signature(visualinher::B.__init__)
    params = list(sig.parameters.keys())



def test_visualinher::r_is_not_abstract():
    assert not inspect.isabstract(visualinher::R)


def test_visualinher::r_constructor_exists():
    assert callable(visualinher::R.__init__)


def test_visualinher::r_constructor_args():
    sig = inspect.signature(visualinher::R.__init__)
    params = list(sig.parameters.keys())



def test_visualinher::a_is_not_abstract():
    assert not inspect.isabstract(visualinher::A)


def test_visualinher::a_constructor_exists():
    assert callable(visualinher::A.__init__)


def test_visualinher::a_constructor_args():
    sig = inspect.signature(visualinher::A.__init__)
    params = list(sig.parameters.keys())



def test_visualinher::s_is_not_abstract():
    assert not inspect.isabstract(visualinher::S)


def test_visualinher::s_constructor_exists():
    assert callable(visualinher::S.__init__)


def test_visualinher::s_constructor_args():
    sig = inspect.signature(visualinher::S.__init__)
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
visualinher::N_strategy = st.builds(
    visualinher::N,
    name=
        safe_text
)
N_strategy = st.builds(
    N,
)
visualinher::C_strategy = st.builds(
    visualinher::C,
)
A_strategy = st.builds(
    A,
)
visualinher::I_strategy = st.builds(
    visualinher::I,
)
visualinher::D_strategy = st.builds(
    visualinher::D,
)
visualinher::E_strategy = st.builds(
    visualinher::E,
)
I_strategy = st.builds(
    I,
)
visualinher::B_strategy = st.builds(
    visualinher::B,
)
visualinher::R_strategy = st.builds(
    visualinher::R,
)
visualinher::A_strategy = st.builds(
    visualinher::A,
)
visualinher::S_strategy = st.builds(
    visualinher::S,
)

@given(instance=visualinher::N_strategy)
@settings(max_examples=50)
def test_visualinher::n_instantiation(instance):
    assert isinstance(instance, visualinher::N)

@given(instance=visualinher::N_strategy)
def test_visualinher::n_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=visualinher::N_strategy)
def test_visualinher::n_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=N_strategy)
@settings(max_examples=50)
def test_n_instantiation(instance):
    assert isinstance(instance, N)

@given(instance=visualinher::C_strategy)
@settings(max_examples=50)
def test_visualinher::c_instantiation(instance):
    assert isinstance(instance, visualinher::C)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=visualinher::I_strategy)
@settings(max_examples=50)
def test_visualinher::i_instantiation(instance):
    assert isinstance(instance, visualinher::I)

@given(instance=visualinher::D_strategy)
@settings(max_examples=50)
def test_visualinher::d_instantiation(instance):
    assert isinstance(instance, visualinher::D)

@given(instance=visualinher::E_strategy)
@settings(max_examples=50)
def test_visualinher::e_instantiation(instance):
    assert isinstance(instance, visualinher::E)

@given(instance=I_strategy)
@settings(max_examples=50)
def test_i_instantiation(instance):
    assert isinstance(instance, I)

@given(instance=visualinher::B_strategy)
@settings(max_examples=50)
def test_visualinher::b_instantiation(instance):
    assert isinstance(instance, visualinher::B)

@given(instance=visualinher::R_strategy)
@settings(max_examples=50)
def test_visualinher::r_instantiation(instance):
    assert isinstance(instance, visualinher::R)

@given(instance=visualinher::A_strategy)
@settings(max_examples=50)
def test_visualinher::a_instantiation(instance):
    assert isinstance(instance, visualinher::A)

@given(instance=visualinher::S_strategy)
@settings(max_examples=50)
def test_visualinher::s_instantiation(instance):
    assert isinstance(instance, visualinher::S)

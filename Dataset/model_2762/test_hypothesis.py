import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpletest::X,
    simpletest::N,
    N,
    simpletest::L,
    simpletest::B,
    simpletest::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletest::x_is_not_abstract():
    assert not inspect.isabstract(simpletest::X)


def test_simpletest::x_constructor_exists():
    assert callable(simpletest::X.__init__)


def test_simpletest::x_constructor_args():
    sig = inspect.signature(simpletest::X.__init__)
    params = list(sig.parameters.keys())



def test_simpletest::n_is_not_abstract():
    assert not inspect.isabstract(simpletest::N)


def test_simpletest::n_constructor_exists():
    assert callable(simpletest::N.__init__)


def test_simpletest::n_constructor_args():
    sig = inspect.signature(simpletest::N.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpletest::n_has_name():
    assert hasattr(simpletest::N, "name")
    descriptor = None
    for klass in simpletest::N.__mro__:
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



def test_simpletest::l_is_not_abstract():
    assert not inspect.isabstract(simpletest::L)


def test_simpletest::l_constructor_exists():
    assert callable(simpletest::L.__init__)


def test_simpletest::l_constructor_args():
    sig = inspect.signature(simpletest::L.__init__)
    params = list(sig.parameters.keys())



def test_simpletest::b_is_not_abstract():
    assert not inspect.isabstract(simpletest::B)


def test_simpletest::b_constructor_exists():
    assert callable(simpletest::B.__init__)


def test_simpletest::b_constructor_args():
    sig = inspect.signature(simpletest::B.__init__)
    params = list(sig.parameters.keys())



def test_simpletest::a_is_not_abstract():
    assert not inspect.isabstract(simpletest::A)


def test_simpletest::a_constructor_exists():
    assert callable(simpletest::A.__init__)


def test_simpletest::a_constructor_args():
    sig = inspect.signature(simpletest::A.__init__)
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
simpletest::X_strategy = st.builds(
    simpletest::X,
)
simpletest::N_strategy = st.builds(
    simpletest::N,
    name=
        safe_text
)
N_strategy = st.builds(
    N,
)
simpletest::L_strategy = st.builds(
    simpletest::L,
)
simpletest::B_strategy = st.builds(
    simpletest::B,
)
simpletest::A_strategy = st.builds(
    simpletest::A,
)

@given(instance=simpletest::X_strategy)
@settings(max_examples=50)
def test_simpletest::x_instantiation(instance):
    assert isinstance(instance, simpletest::X)

@given(instance=simpletest::N_strategy)
@settings(max_examples=50)
def test_simpletest::n_instantiation(instance):
    assert isinstance(instance, simpletest::N)

@given(instance=simpletest::N_strategy)
def test_simpletest::n_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpletest::N_strategy)
def test_simpletest::n_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=N_strategy)
@settings(max_examples=50)
def test_n_instantiation(instance):
    assert isinstance(instance, N)

@given(instance=simpletest::L_strategy)
@settings(max_examples=50)
def test_simpletest::l_instantiation(instance):
    assert isinstance(instance, simpletest::L)

@given(instance=simpletest::B_strategy)
@settings(max_examples=50)
def test_simpletest::b_instantiation(instance):
    assert isinstance(instance, simpletest::B)

@given(instance=simpletest::A_strategy)
@settings(max_examples=50)
def test_simpletest::a_instantiation(instance):
    assert isinstance(instance, simpletest::A)

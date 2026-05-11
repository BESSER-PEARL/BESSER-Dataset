import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mydsl::W,
    W,
    mydsl::L,
    mydsl::B,
    mydsl::D,
    mydsl::C,
    mydsl::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::w_is_not_abstract():
    assert not inspect.isabstract(mydsl::W)


def test_mydsl::w_constructor_exists():
    assert callable(mydsl::W.__init__)


def test_mydsl::w_constructor_args():
    sig = inspect.signature(mydsl::W.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::w_has_name():
    assert hasattr(mydsl::W, "name")
    descriptor = None
    for klass in mydsl::W.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_w_is_not_abstract():
    assert not inspect.isabstract(W)


def test_w_constructor_exists():
    assert callable(W.__init__)


def test_w_constructor_args():
    sig = inspect.signature(W.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::l_is_not_abstract():
    assert not inspect.isabstract(mydsl::L)


def test_mydsl::l_constructor_exists():
    assert callable(mydsl::L.__init__)


def test_mydsl::l_constructor_args():
    sig = inspect.signature(mydsl::L.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::b_is_not_abstract():
    assert not inspect.isabstract(mydsl::B)


def test_mydsl::b_constructor_exists():
    assert callable(mydsl::B.__init__)


def test_mydsl::b_constructor_args():
    sig = inspect.signature(mydsl::B.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::d_is_not_abstract():
    assert not inspect.isabstract(mydsl::D)


def test_mydsl::d_constructor_exists():
    assert callable(mydsl::D.__init__)


def test_mydsl::d_constructor_args():
    sig = inspect.signature(mydsl::D.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::c_is_not_abstract():
    assert not inspect.isabstract(mydsl::C)


def test_mydsl::c_constructor_exists():
    assert callable(mydsl::C.__init__)


def test_mydsl::c_constructor_args():
    sig = inspect.signature(mydsl::C.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::a_is_not_abstract():
    assert not inspect.isabstract(mydsl::A)


def test_mydsl::a_constructor_exists():
    assert callable(mydsl::A.__init__)


def test_mydsl::a_constructor_args():
    sig = inspect.signature(mydsl::A.__init__)
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
mydsl::W_strategy = st.builds(
    mydsl::W,
    name=
        safe_text
)
W_strategy = st.builds(
    W,
)
mydsl::L_strategy = st.builds(
    mydsl::L,
)
mydsl::B_strategy = st.builds(
    mydsl::B,
)
mydsl::D_strategy = st.builds(
    mydsl::D,
)
mydsl::C_strategy = st.builds(
    mydsl::C,
)
mydsl::A_strategy = st.builds(
    mydsl::A,
)

@given(instance=mydsl::W_strategy)
@settings(max_examples=50)
def test_mydsl::w_instantiation(instance):
    assert isinstance(instance, mydsl::W)

@given(instance=mydsl::W_strategy)
def test_mydsl::w_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mydsl::W_strategy)
def test_mydsl::w_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=W_strategy)
@settings(max_examples=50)
def test_w_instantiation(instance):
    assert isinstance(instance, W)

@given(instance=mydsl::L_strategy)
@settings(max_examples=50)
def test_mydsl::l_instantiation(instance):
    assert isinstance(instance, mydsl::L)

@given(instance=mydsl::B_strategy)
@settings(max_examples=50)
def test_mydsl::b_instantiation(instance):
    assert isinstance(instance, mydsl::B)

@given(instance=mydsl::D_strategy)
@settings(max_examples=50)
def test_mydsl::d_instantiation(instance):
    assert isinstance(instance, mydsl::D)

@given(instance=mydsl::C_strategy)
@settings(max_examples=50)
def test_mydsl::c_instantiation(instance):
    assert isinstance(instance, mydsl::C)

@given(instance=mydsl::A_strategy)
@settings(max_examples=50)
def test_mydsl::a_instantiation(instance):
    assert isinstance(instance, mydsl::A)

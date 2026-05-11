import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    a::c::cc2,
    a::c::cc1,
    a::e::ce2,
    a::e::ce1,
    a::d::cd2,
    a::d::cd1,
    a::b::cb2,
    a::b::cb1,
    a::ca2,
    a::ca1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a::c::cc2_is_not_abstract():
    assert not inspect.isabstract(a::c::cc2)


def test_a::c::cc2_constructor_exists():
    assert callable(a::c::cc2.__init__)


def test_a::c::cc2_constructor_args():
    sig = inspect.signature(a::c::cc2.__init__)
    params = list(sig.parameters.keys())



def test_a::c::cc1_is_not_abstract():
    assert not inspect.isabstract(a::c::cc1)


def test_a::c::cc1_constructor_exists():
    assert callable(a::c::cc1.__init__)


def test_a::c::cc1_constructor_args():
    sig = inspect.signature(a::c::cc1.__init__)
    params = list(sig.parameters.keys())



def test_a::e::ce2_is_not_abstract():
    assert not inspect.isabstract(a::e::ce2)


def test_a::e::ce2_constructor_exists():
    assert callable(a::e::ce2.__init__)


def test_a::e::ce2_constructor_args():
    sig = inspect.signature(a::e::ce2.__init__)
    params = list(sig.parameters.keys())



def test_a::e::ce1_is_not_abstract():
    assert not inspect.isabstract(a::e::ce1)


def test_a::e::ce1_constructor_exists():
    assert callable(a::e::ce1.__init__)


def test_a::e::ce1_constructor_args():
    sig = inspect.signature(a::e::ce1.__init__)
    params = list(sig.parameters.keys())



def test_a::d::cd2_is_not_abstract():
    assert not inspect.isabstract(a::d::cd2)


def test_a::d::cd2_constructor_exists():
    assert callable(a::d::cd2.__init__)


def test_a::d::cd2_constructor_args():
    sig = inspect.signature(a::d::cd2.__init__)
    params = list(sig.parameters.keys())



def test_a::d::cd1_is_not_abstract():
    assert not inspect.isabstract(a::d::cd1)


def test_a::d::cd1_constructor_exists():
    assert callable(a::d::cd1.__init__)


def test_a::d::cd1_constructor_args():
    sig = inspect.signature(a::d::cd1.__init__)
    params = list(sig.parameters.keys())



def test_a::b::cb2_is_not_abstract():
    assert not inspect.isabstract(a::b::cb2)


def test_a::b::cb2_constructor_exists():
    assert callable(a::b::cb2.__init__)


def test_a::b::cb2_constructor_args():
    sig = inspect.signature(a::b::cb2.__init__)
    params = list(sig.parameters.keys())



def test_a::b::cb1_is_not_abstract():
    assert not inspect.isabstract(a::b::cb1)


def test_a::b::cb1_constructor_exists():
    assert callable(a::b::cb1.__init__)


def test_a::b::cb1_constructor_args():
    sig = inspect.signature(a::b::cb1.__init__)
    params = list(sig.parameters.keys())



def test_a::ca2_is_not_abstract():
    assert not inspect.isabstract(a::ca2)


def test_a::ca2_constructor_exists():
    assert callable(a::ca2.__init__)


def test_a::ca2_constructor_args():
    sig = inspect.signature(a::ca2.__init__)
    params = list(sig.parameters.keys())



def test_a::ca1_is_not_abstract():
    assert not inspect.isabstract(a::ca1)


def test_a::ca1_constructor_exists():
    assert callable(a::ca1.__init__)


def test_a::ca1_constructor_args():
    sig = inspect.signature(a::ca1.__init__)
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
a::c::cc2_strategy = st.builds(
    a::c::cc2,
)
a::c::cc1_strategy = st.builds(
    a::c::cc1,
)
a::e::ce2_strategy = st.builds(
    a::e::ce2,
)
a::e::ce1_strategy = st.builds(
    a::e::ce1,
)
a::d::cd2_strategy = st.builds(
    a::d::cd2,
)
a::d::cd1_strategy = st.builds(
    a::d::cd1,
)
a::b::cb2_strategy = st.builds(
    a::b::cb2,
)
a::b::cb1_strategy = st.builds(
    a::b::cb1,
)
a::ca2_strategy = st.builds(
    a::ca2,
)
a::ca1_strategy = st.builds(
    a::ca1,
)

@given(instance=a::c::cc2_strategy)
@settings(max_examples=50)
def test_a::c::cc2_instantiation(instance):
    assert isinstance(instance, a::c::cc2)

@given(instance=a::c::cc1_strategy)
@settings(max_examples=50)
def test_a::c::cc1_instantiation(instance):
    assert isinstance(instance, a::c::cc1)

@given(instance=a::e::ce2_strategy)
@settings(max_examples=50)
def test_a::e::ce2_instantiation(instance):
    assert isinstance(instance, a::e::ce2)

@given(instance=a::e::ce1_strategy)
@settings(max_examples=50)
def test_a::e::ce1_instantiation(instance):
    assert isinstance(instance, a::e::ce1)

@given(instance=a::d::cd2_strategy)
@settings(max_examples=50)
def test_a::d::cd2_instantiation(instance):
    assert isinstance(instance, a::d::cd2)

@given(instance=a::d::cd1_strategy)
@settings(max_examples=50)
def test_a::d::cd1_instantiation(instance):
    assert isinstance(instance, a::d::cd1)

@given(instance=a::b::cb2_strategy)
@settings(max_examples=50)
def test_a::b::cb2_instantiation(instance):
    assert isinstance(instance, a::b::cb2)

@given(instance=a::b::cb1_strategy)
@settings(max_examples=50)
def test_a::b::cb1_instantiation(instance):
    assert isinstance(instance, a::b::cb1)

@given(instance=a::ca2_strategy)
@settings(max_examples=50)
def test_a::ca2_instantiation(instance):
    assert isinstance(instance, a::ca2)

@given(instance=a::ca1_strategy)
@settings(max_examples=50)
def test_a::ca1_instantiation(instance):
    assert isinstance(instance, a::ca1)

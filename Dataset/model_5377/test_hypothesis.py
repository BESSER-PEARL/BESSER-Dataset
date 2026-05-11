import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    xyz::Y,
    xyz::X,
    xyz::Z,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xyz::y_is_not_abstract():
    assert not inspect.isabstract(xyz::Y)


def test_xyz::y_constructor_exists():
    assert callable(xyz::Y.__init__)


def test_xyz::y_constructor_args():
    sig = inspect.signature(xyz::Y.__init__)
    params = list(sig.parameters.keys())



def test_xyz::x_is_not_abstract():
    assert not inspect.isabstract(xyz::X)


def test_xyz::x_constructor_exists():
    assert callable(xyz::X.__init__)


def test_xyz::x_constructor_args():
    sig = inspect.signature(xyz::X.__init__)
    params = list(sig.parameters.keys())



def test_xyz::z_is_not_abstract():
    assert not inspect.isabstract(xyz::Z)


def test_xyz::z_constructor_exists():
    assert callable(xyz::Z.__init__)


def test_xyz::z_constructor_args():
    sig = inspect.signature(xyz::Z.__init__)
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
xyz::Y_strategy = st.builds(
    xyz::Y,
)
xyz::X_strategy = st.builds(
    xyz::X,
)
xyz::Z_strategy = st.builds(
    xyz::Z,
)

@given(instance=xyz::Y_strategy)
@settings(max_examples=50)
def test_xyz::y_instantiation(instance):
    assert isinstance(instance, xyz::Y)

@given(instance=xyz::X_strategy)
@settings(max_examples=50)
def test_xyz::x_instantiation(instance):
    assert isinstance(instance, xyz::X)

@given(instance=xyz::Z_strategy)
@settings(max_examples=50)
def test_xyz::z_instantiation(instance):
    assert isinstance(instance, xyz::Z)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    xyz_Y,
    xyz_X,
    xyz_Z,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xyz_y_is_not_abstract():
    assert not inspect.isabstract(xyz_Y)


def test_xyz_y_constructor_exists():
    assert callable(xyz_Y.__init__)


def test_xyz_y_constructor_args():
    sig = inspect.signature(xyz_Y.__init__)
    params = list(sig.parameters.keys())



def test_xyz_x_is_not_abstract():
    assert not inspect.isabstract(xyz_X)


def test_xyz_x_constructor_exists():
    assert callable(xyz_X.__init__)


def test_xyz_x_constructor_args():
    sig = inspect.signature(xyz_X.__init__)
    params = list(sig.parameters.keys())



def test_xyz_z_is_not_abstract():
    assert not inspect.isabstract(xyz_Z)


def test_xyz_z_constructor_exists():
    assert callable(xyz_Z.__init__)


def test_xyz_z_constructor_args():
    sig = inspect.signature(xyz_Z.__init__)
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
xyz_Y_strategy = st.builds(
    xyz_Y,
)
xyz_X_strategy = st.builds(
    xyz_X,
)
xyz_Z_strategy = st.builds(
    xyz_Z,
)

@given(instance=xyz_Y_strategy)
@settings(max_examples=50)
def test_xyz_y_instantiation(instance):
    assert isinstance(instance, xyz_Y)

@given(instance=xyz_X_strategy)
@settings(max_examples=50)
def test_xyz_x_instantiation(instance):
    assert isinstance(instance, xyz_X)

@given(instance=xyz_Z_strategy)
@settings(max_examples=50)
def test_xyz_z_instantiation(instance):
    assert isinstance(instance, xyz_Z)

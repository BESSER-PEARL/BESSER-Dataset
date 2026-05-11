import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Solver,
    fd::FiniteDifference,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_solver_is_not_abstract():
    assert not inspect.isabstract(Solver)


def test_solver_constructor_exists():
    assert callable(Solver.__init__)


def test_solver_constructor_args():
    sig = inspect.signature(Solver.__init__)
    params = list(sig.parameters.keys())



def test_fd::finitedifference_is_not_abstract():
    assert not inspect.isabstract(fd::FiniteDifference)


def test_fd::finitedifference_constructor_exists():
    assert callable(fd::FiniteDifference.__init__)


def test_fd::finitedifference_constructor_args():
    sig = inspect.signature(fd::FiniteDifference.__init__)
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
Solver_strategy = st.builds(
    Solver,
)
fd::FiniteDifference_strategy = st.builds(
    fd::FiniteDifference,
)

@given(instance=Solver_strategy)
@settings(max_examples=50)
def test_solver_instantiation(instance):
    assert isinstance(instance, Solver)

@given(instance=fd::FiniteDifference_strategy)
@settings(max_examples=50)
def test_fd::finitedifference_instantiation(instance):
    assert isinstance(instance, fd::FiniteDifference)

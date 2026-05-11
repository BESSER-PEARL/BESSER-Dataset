import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Solver,
    rk::RungeKutta,
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



def test_rk::rungekutta_is_not_abstract():
    assert not inspect.isabstract(rk::RungeKutta)


def test_rk::rungekutta_constructor_exists():
    assert callable(rk::RungeKutta.__init__)


def test_rk::rungekutta_constructor_args():
    sig = inspect.signature(rk::RungeKutta.__init__)
    params = list(sig.parameters.keys())
    assert "relativeTolerance" in params, "Missing parameter 'relativeTolerance'"

def test_rk::rungekutta_has_relativeTolerance():
    assert hasattr(rk::RungeKutta, "relativeTolerance")
    descriptor = None
    for klass in rk::RungeKutta.__mro__:
        if "relativeTolerance" in klass.__dict__:
            descriptor = klass.__dict__["relativeTolerance"]
            break
    assert isinstance(descriptor, property)


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
rk::RungeKutta_strategy = st.builds(
    rk::RungeKutta,
    relativeTolerance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Solver_strategy)
@settings(max_examples=50)
def test_solver_instantiation(instance):
    assert isinstance(instance, Solver)

@given(instance=rk::RungeKutta_strategy)
@settings(max_examples=50)
def test_rk::rungekutta_instantiation(instance):
    assert isinstance(instance, rk::RungeKutta)

@given(instance=rk::RungeKutta_strategy)
def test_rk::rungekutta_relativeTolerance_type(instance):
    assert isinstance(instance.relativeTolerance, float)


@given(instance=rk::RungeKutta_strategy)
def test_rk::rungekutta_relativeTolerance_setter(instance):
    original = instance.relativeTolerance
    instance.relativeTolerance = original
    assert instance.relativeTolerance == original

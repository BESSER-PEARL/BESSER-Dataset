import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Solver,
    rk_RungeKutta,
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



def test_rk_rungekutta_is_not_abstract():
    assert not inspect.isabstract(rk_RungeKutta)


def test_rk_rungekutta_constructor_exists():
    assert callable(rk_RungeKutta.__init__)


def test_rk_rungekutta_constructor_args():
    sig = inspect.signature(rk_RungeKutta.__init__)
    params = list(sig.parameters.keys())
    assert "relativeTolerance" in params, "Missing parameter 'relativeTolerance'"

def test_rk_rungekutta_has_relativeTolerance():
    assert hasattr(rk_RungeKutta, "relativeTolerance")
    descriptor = None
    for klass in rk_RungeKutta.__mro__:
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
rk_RungeKutta_strategy = st.builds(
    rk_RungeKutta,
    relativeTolerance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Solver_strategy)
@settings(max_examples=50)
def test_solver_instantiation(instance):
    assert isinstance(instance, Solver)

@given(instance=rk_RungeKutta_strategy)
@settings(max_examples=50)
def test_rk_rungekutta_instantiation(instance):
    assert isinstance(instance, rk_RungeKutta)



@given(instance=rk_RungeKutta_strategy)
def test_rk_rungekutta_relativeTolerance_setter(instance):
    original = instance.relativeTolerance
    instance.relativeTolerance = original
    assert instance.relativeTolerance == original

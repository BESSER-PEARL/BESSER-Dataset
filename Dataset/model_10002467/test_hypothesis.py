import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SudokuBoard,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sudokuboard_is_not_abstract():
    assert not inspect.isabstract(SudokuBoard)


def test_sudokuboard_constructor_exists():
    assert callable(SudokuBoard.__init__)


def test_sudokuboard_constructor_args():
    sig = inspect.signature(SudokuBoard.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
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
SudokuBoard_strategy = st.builds(
    SudokuBoard,
)
User_strategy = st.builds(
    User,
)

@given(instance=SudokuBoard_strategy)
@settings(max_examples=50)
def test_sudokuboard_instantiation(instance):
    assert isinstance(instance, SudokuBoard)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

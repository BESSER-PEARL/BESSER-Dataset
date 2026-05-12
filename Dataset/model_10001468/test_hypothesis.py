import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Card,
    TakeCasch_UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())



def test_takecasch_usecase_is_not_abstract():
    assert not inspect.isabstract(TakeCasch_UseCase)


def test_takecasch_usecase_constructor_exists():
    assert callable(TakeCasch_UseCase.__init__)


def test_takecasch_usecase_constructor_args():
    sig = inspect.signature(TakeCasch_UseCase.__init__)
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
Card_strategy = st.builds(
    Card,
)
TakeCasch_UseCase_strategy = st.builds(
    TakeCasch_UseCase,
)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)

@given(instance=TakeCasch_UseCase_strategy)
@settings(max_examples=50)
def test_takecasch_usecase_instantiation(instance):
    assert isinstance(instance, TakeCasch_UseCase)

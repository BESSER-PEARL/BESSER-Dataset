import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::Yolo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::yolo_is_not_abstract():
    assert not inspect.isabstract(test::Yolo)


def test_test::yolo_constructor_exists():
    assert callable(test::Yolo.__init__)


def test_test::yolo_constructor_args():
    sig = inspect.signature(test::Yolo.__init__)
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
test::Yolo_strategy = st.builds(
    test::Yolo,
)

@given(instance=test::Yolo_strategy)
@settings(max_examples=50)
def test_test::yolo_instantiation(instance):
    assert isinstance(instance, test::Yolo)

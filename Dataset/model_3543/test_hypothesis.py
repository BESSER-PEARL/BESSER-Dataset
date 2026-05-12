import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_Yolo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_yolo_is_not_abstract():
    assert not inspect.isabstract(test_Yolo)


def test_test_yolo_constructor_exists():
    assert callable(test_Yolo.__init__)


def test_test_yolo_constructor_args():
    sig = inspect.signature(test_Yolo.__init__)
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
test_Yolo_strategy = st.builds(
    test_Yolo,
)

@given(instance=test_Yolo_strategy)
@settings(max_examples=50)
def test_test_yolo_instantiation(instance):
    assert isinstance(instance, test_Yolo)

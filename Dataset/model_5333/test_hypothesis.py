import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    root_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_class_is_not_abstract():
    assert not inspect.isabstract(root_Class)


def test_root_class_constructor_exists():
    assert callable(root_Class.__init__)


def test_root_class_constructor_args():
    sig = inspect.signature(root_Class.__init__)
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
root_Class_strategy = st.builds(
    root_Class,
)

@given(instance=root_Class_strategy)
@settings(max_examples=50)
def test_root_class_instantiation(instance):
    assert isinstance(instance, root_Class)

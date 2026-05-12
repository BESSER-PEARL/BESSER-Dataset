import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_foo_is_not_abstract():
    assert not inspect.isabstract(test_foo)


def test_test_foo_constructor_exists():
    assert callable(test_foo.__init__)


def test_test_foo_constructor_args():
    sig = inspect.signature(test_foo.__init__)
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
test_foo_strategy = st.builds(
    test_foo,
)

@given(instance=test_foo_strategy)
@settings(max_examples=50)
def test_test_foo_instantiation(instance):
    assert isinstance(instance, test_foo)

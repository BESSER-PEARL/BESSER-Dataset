import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::foo_is_not_abstract():
    assert not inspect.isabstract(test::foo)


def test_test::foo_constructor_exists():
    assert callable(test::foo.__init__)


def test_test::foo_constructor_args():
    sig = inspect.signature(test::foo.__init__)
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
test::foo_strategy = st.builds(
    test::foo,
)

@given(instance=test::foo_strategy)
@settings(max_examples=50)
def test_test::foo_instantiation(instance):
    assert isinstance(instance, test::foo)

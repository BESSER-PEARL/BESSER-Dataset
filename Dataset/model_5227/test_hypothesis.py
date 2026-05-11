import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    base::test::foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_base::test::foo_is_not_abstract():
    assert not inspect.isabstract(base::test::foo)


def test_base::test::foo_constructor_exists():
    assert callable(base::test::foo.__init__)


def test_base::test::foo_constructor_args():
    sig = inspect.signature(base::test::foo.__init__)
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
base::test::foo_strategy = st.builds(
    base::test::foo,
)

@given(instance=base::test::foo_strategy)
@settings(max_examples=50)
def test_base::test::foo_instantiation(instance):
    assert isinstance(instance, base::test::foo)

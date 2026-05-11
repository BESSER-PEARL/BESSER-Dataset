import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rootpkg2::Token,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rootpkg2::token_is_not_abstract():
    assert not inspect.isabstract(rootpkg2::Token)


def test_rootpkg2::token_constructor_exists():
    assert callable(rootpkg2::Token.__init__)


def test_rootpkg2::token_constructor_args():
    sig = inspect.signature(rootpkg2::Token.__init__)
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
rootpkg2::Token_strategy = st.builds(
    rootpkg2::Token,
)

@given(instance=rootpkg2::Token_strategy)
@settings(max_examples=50)
def test_rootpkg2::token_instantiation(instance):
    assert isinstance(instance, rootpkg2::Token)

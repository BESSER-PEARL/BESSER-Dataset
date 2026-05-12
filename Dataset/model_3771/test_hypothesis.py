import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rootpkg2_Token,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rootpkg2_token_is_not_abstract():
    assert not inspect.isabstract(rootpkg2_Token)


def test_rootpkg2_token_constructor_exists():
    assert callable(rootpkg2_Token.__init__)


def test_rootpkg2_token_constructor_args():
    sig = inspect.signature(rootpkg2_Token.__init__)
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
rootpkg2_Token_strategy = st.builds(
    rootpkg2_Token,
)

@given(instance=rootpkg2_Token_strategy)
@settings(max_examples=50)
def test_rootpkg2_token_instantiation(instance):
    assert isinstance(instance, rootpkg2_Token)

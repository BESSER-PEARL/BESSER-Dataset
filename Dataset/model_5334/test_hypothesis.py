import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Root_ClaferA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_clafera_is_not_abstract():
    assert not inspect.isabstract(Root_ClaferA)


def test_root_clafera_constructor_exists():
    assert callable(Root_ClaferA.__init__)


def test_root_clafera_constructor_args():
    sig = inspect.signature(Root_ClaferA.__init__)
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
Root_ClaferA_strategy = st.builds(
    Root_ClaferA,
)

@given(instance=Root_ClaferA_strategy)
@settings(max_examples=50)
def test_root_clafera_instantiation(instance):
    assert isinstance(instance, Root_ClaferA)

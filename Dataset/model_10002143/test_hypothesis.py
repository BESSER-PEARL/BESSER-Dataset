import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    _unnamed,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test__unnamed_is_not_abstract():
    assert not inspect.isabstract(_unnamed)


def test__unnamed_constructor_exists():
    assert callable(_unnamed.__init__)


def test__unnamed_constructor_args():
    sig = inspect.signature(_unnamed.__init__)
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
_unnamed_strategy = st.builds(
    _unnamed,
)

@given(instance=_unnamed_strategy)
@settings(max_examples=50)
def test__unnamed_instantiation(instance):
    assert isinstance(instance, _unnamed)

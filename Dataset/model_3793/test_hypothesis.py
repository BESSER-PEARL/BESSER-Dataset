import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pack::eCls,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pack::ecls_is_not_abstract():
    assert not inspect.isabstract(pack::eCls)


def test_pack::ecls_constructor_exists():
    assert callable(pack::eCls.__init__)


def test_pack::ecls_constructor_args():
    sig = inspect.signature(pack::eCls.__init__)
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
pack::eCls_strategy = st.builds(
    pack::eCls,
)

@given(instance=pack::eCls_strategy)
@settings(max_examples=50)
def test_pack::ecls_instantiation(instance):
    assert isinstance(instance, pack::eCls)

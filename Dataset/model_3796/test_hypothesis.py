import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pack_Class1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pack_class1_is_not_abstract():
    assert not inspect.isabstract(pack_Class1)


def test_pack_class1_constructor_exists():
    assert callable(pack_Class1.__init__)


def test_pack_class1_constructor_args():
    sig = inspect.signature(pack_Class1.__init__)
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
pack_Class1_strategy = st.builds(
    pack_Class1,
)

@given(instance=pack_Class1_strategy)
@settings(max_examples=50)
def test_pack_class1_instantiation(instance):
    assert isinstance(instance, pack_Class1)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    HardCodedTree::NodeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hardcodedtree::nodekind_is_not_abstract():
    assert not inspect.isabstract(HardCodedTree::NodeKind)


def test_hardcodedtree::nodekind_constructor_exists():
    assert callable(HardCodedTree::NodeKind.__init__)


def test_hardcodedtree::nodekind_constructor_args():
    sig = inspect.signature(HardCodedTree::NodeKind.__init__)
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
HardCodedTree::NodeKind_strategy = st.builds(
    HardCodedTree::NodeKind,
)

@given(instance=HardCodedTree::NodeKind_strategy)
@settings(max_examples=50)
def test_hardcodedtree::nodekind_instantiation(instance):
    assert isinstance(instance, HardCodedTree::NodeKind)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    root_container_border_node_3,
    root_container_border_node_2,
    root_container_border_node_1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_container_border_node_3_is_not_abstract():
    assert not inspect.isabstract(root_container_border_node_3)


def test_root_container_border_node_3_constructor_exists():
    assert callable(root_container_border_node_3.__init__)


def test_root_container_border_node_3_constructor_args():
    sig = inspect.signature(root_container_border_node_3.__init__)
    params = list(sig.parameters.keys())



def test_root_container_border_node_2_is_not_abstract():
    assert not inspect.isabstract(root_container_border_node_2)


def test_root_container_border_node_2_constructor_exists():
    assert callable(root_container_border_node_2.__init__)


def test_root_container_border_node_2_constructor_args():
    sig = inspect.signature(root_container_border_node_2.__init__)
    params = list(sig.parameters.keys())



def test_root_container_border_node_1_is_not_abstract():
    assert not inspect.isabstract(root_container_border_node_1)


def test_root_container_border_node_1_constructor_exists():
    assert callable(root_container_border_node_1.__init__)


def test_root_container_border_node_1_constructor_args():
    sig = inspect.signature(root_container_border_node_1.__init__)
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
root_container_border_node_3_strategy = st.builds(
    root_container_border_node_3,
)
root_container_border_node_2_strategy = st.builds(
    root_container_border_node_2,
)
root_container_border_node_1_strategy = st.builds(
    root_container_border_node_1,
)

@given(instance=root_container_border_node_3_strategy)
@settings(max_examples=50)
def test_root_container_border_node_3_instantiation(instance):
    assert isinstance(instance, root_container_border_node_3)

@given(instance=root_container_border_node_2_strategy)
@settings(max_examples=50)
def test_root_container_border_node_2_instantiation(instance):
    assert isinstance(instance, root_container_border_node_2)

@given(instance=root_container_border_node_1_strategy)
@settings(max_examples=50)
def test_root_container_border_node_1_instantiation(instance):
    assert isinstance(instance, root_container_border_node_1)

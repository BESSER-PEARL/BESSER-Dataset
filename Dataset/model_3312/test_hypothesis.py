import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    transform::Grammar,
    transform::Graph,
    Named,
    transform::Transformation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transform::grammar_is_not_abstract():
    assert not inspect.isabstract(transform::Grammar)


def test_transform::grammar_constructor_exists():
    assert callable(transform::Grammar.__init__)


def test_transform::grammar_constructor_args():
    sig = inspect.signature(transform::Grammar.__init__)
    params = list(sig.parameters.keys())



def test_transform::graph_is_not_abstract():
    assert not inspect.isabstract(transform::Graph)


def test_transform::graph_constructor_exists():
    assert callable(transform::Graph.__init__)


def test_transform::graph_constructor_args():
    sig = inspect.signature(transform::Graph.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_transform::transformation_is_not_abstract():
    assert not inspect.isabstract(transform::Transformation)


def test_transform::transformation_constructor_exists():
    assert callable(transform::Transformation.__init__)


def test_transform::transformation_constructor_args():
    sig = inspect.signature(transform::Transformation.__init__)
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
transform::Grammar_strategy = st.builds(
    transform::Grammar,
)
transform::Graph_strategy = st.builds(
    transform::Graph,
)
Named_strategy = st.builds(
    Named,
)
transform::Transformation_strategy = st.builds(
    transform::Transformation,
)

@given(instance=transform::Grammar_strategy)
@settings(max_examples=50)
def test_transform::grammar_instantiation(instance):
    assert isinstance(instance, transform::Grammar)

@given(instance=transform::Graph_strategy)
@settings(max_examples=50)
def test_transform::graph_instantiation(instance):
    assert isinstance(instance, transform::Graph)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=transform::Transformation_strategy)
@settings(max_examples=50)
def test_transform::transformation_instantiation(instance):
    assert isinstance(instance, transform::Transformation)

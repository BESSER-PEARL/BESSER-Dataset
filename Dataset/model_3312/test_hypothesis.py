import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    transform_Grammar,
    transform_Graph,
    Named,
    transform_Transformation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transform_grammar_is_not_abstract():
    assert not inspect.isabstract(transform_Grammar)


def test_transform_grammar_constructor_exists():
    assert callable(transform_Grammar.__init__)


def test_transform_grammar_constructor_args():
    sig = inspect.signature(transform_Grammar.__init__)
    params = list(sig.parameters.keys())



def test_transform_graph_is_not_abstract():
    assert not inspect.isabstract(transform_Graph)


def test_transform_graph_constructor_exists():
    assert callable(transform_Graph.__init__)


def test_transform_graph_constructor_args():
    sig = inspect.signature(transform_Graph.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_transform_transformation_is_not_abstract():
    assert not inspect.isabstract(transform_Transformation)


def test_transform_transformation_constructor_exists():
    assert callable(transform_Transformation.__init__)


def test_transform_transformation_constructor_args():
    sig = inspect.signature(transform_Transformation.__init__)
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
transform_Grammar_strategy = st.builds(
    transform_Grammar,
)
transform_Graph_strategy = st.builds(
    transform_Graph,
)
Named_strategy = st.builds(
    Named,
)
transform_Transformation_strategy = st.builds(
    transform_Transformation,
)

@given(instance=transform_Grammar_strategy)
@settings(max_examples=50)
def test_transform_grammar_instantiation(instance):
    assert isinstance(instance, transform_Grammar)

@given(instance=transform_Graph_strategy)
@settings(max_examples=50)
def test_transform_graph_instantiation(instance):
    assert isinstance(instance, transform_Graph)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=transform_Transformation_strategy)
@settings(max_examples=50)
def test_transform_transformation_instantiation(instance):
    assert isinstance(instance, transform_Transformation)

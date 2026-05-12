import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NodeCS,
    kiamacs_CompositeCS,
    kiamacs_EObject,
    kiamacs_BaseCS,
    kiamacs_LeafCS,
    BaseCS,
    kiamacs_NodeCS,
    kiamacs_TopCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nodecs_is_not_abstract():
    assert not inspect.isabstract(NodeCS)


def test_nodecs_constructor_exists():
    assert callable(NodeCS.__init__)


def test_nodecs_constructor_args():
    sig = inspect.signature(NodeCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs_compositecs_is_not_abstract():
    assert not inspect.isabstract(kiamacs_CompositeCS)


def test_kiamacs_compositecs_constructor_exists():
    assert callable(kiamacs_CompositeCS.__init__)


def test_kiamacs_compositecs_constructor_args():
    sig = inspect.signature(kiamacs_CompositeCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs_eobject_is_not_abstract():
    assert not inspect.isabstract(kiamacs_EObject)


def test_kiamacs_eobject_constructor_exists():
    assert callable(kiamacs_EObject.__init__)


def test_kiamacs_eobject_constructor_args():
    sig = inspect.signature(kiamacs_EObject.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs_basecs_is_not_abstract():
    assert not inspect.isabstract(kiamacs_BaseCS)


def test_kiamacs_basecs_constructor_exists():
    assert callable(kiamacs_BaseCS.__init__)


def test_kiamacs_basecs_constructor_args():
    sig = inspect.signature(kiamacs_BaseCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs_leafcs_is_not_abstract():
    assert not inspect.isabstract(kiamacs_LeafCS)


def test_kiamacs_leafcs_constructor_exists():
    assert callable(kiamacs_LeafCS.__init__)


def test_kiamacs_leafcs_constructor_args():
    sig = inspect.signature(kiamacs_LeafCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_is_not_abstract():
    assert not inspect.isabstract(BaseCS)


def test_basecs_constructor_exists():
    assert callable(BaseCS.__init__)


def test_basecs_constructor_args():
    sig = inspect.signature(BaseCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs_nodecs_is_not_abstract():
    assert not inspect.isabstract(kiamacs_NodeCS)


def test_kiamacs_nodecs_constructor_exists():
    assert callable(kiamacs_NodeCS.__init__)


def test_kiamacs_nodecs_constructor_args():
    sig = inspect.signature(kiamacs_NodeCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs_topcs_is_not_abstract():
    assert not inspect.isabstract(kiamacs_TopCS)


def test_kiamacs_topcs_constructor_exists():
    assert callable(kiamacs_TopCS.__init__)


def test_kiamacs_topcs_constructor_args():
    sig = inspect.signature(kiamacs_TopCS.__init__)
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
NodeCS_strategy = st.builds(
    NodeCS,
)
kiamacs_CompositeCS_strategy = st.builds(
    kiamacs_CompositeCS,
)
kiamacs_EObject_strategy = st.builds(
    kiamacs_EObject,
)
kiamacs_BaseCS_strategy = st.builds(
    kiamacs_BaseCS,
)
kiamacs_LeafCS_strategy = st.builds(
    kiamacs_LeafCS,
)
BaseCS_strategy = st.builds(
    BaseCS,
)
kiamacs_NodeCS_strategy = st.builds(
    kiamacs_NodeCS,
)
kiamacs_TopCS_strategy = st.builds(
    kiamacs_TopCS,
)

@given(instance=NodeCS_strategy)
@settings(max_examples=50)
def test_nodecs_instantiation(instance):
    assert isinstance(instance, NodeCS)

@given(instance=kiamacs_CompositeCS_strategy)
@settings(max_examples=50)
def test_kiamacs_compositecs_instantiation(instance):
    assert isinstance(instance, kiamacs_CompositeCS)

@given(instance=kiamacs_EObject_strategy)
@settings(max_examples=50)
def test_kiamacs_eobject_instantiation(instance):
    assert isinstance(instance, kiamacs_EObject)

@given(instance=kiamacs_BaseCS_strategy)
@settings(max_examples=50)
def test_kiamacs_basecs_instantiation(instance):
    assert isinstance(instance, kiamacs_BaseCS)

@given(instance=kiamacs_LeafCS_strategy)
@settings(max_examples=50)
def test_kiamacs_leafcs_instantiation(instance):
    assert isinstance(instance, kiamacs_LeafCS)

@given(instance=BaseCS_strategy)
@settings(max_examples=50)
def test_basecs_instantiation(instance):
    assert isinstance(instance, BaseCS)

@given(instance=kiamacs_NodeCS_strategy)
@settings(max_examples=50)
def test_kiamacs_nodecs_instantiation(instance):
    assert isinstance(instance, kiamacs_NodeCS)

@given(instance=kiamacs_TopCS_strategy)
@settings(max_examples=50)
def test_kiamacs_topcs_instantiation(instance):
    assert isinstance(instance, kiamacs_TopCS)

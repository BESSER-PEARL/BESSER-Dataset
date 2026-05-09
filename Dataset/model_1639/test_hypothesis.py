import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NodeCS,
    kiamacs::CompositeCS,
    kiamacs::EObject,
    kiamacs::BaseCS,
    kiamacs::LeafCS,
    BaseCS,
    kiamacs::NodeCS,
    kiamacs::TopCS,
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



def test_kiamacs::compositecs_is_not_abstract():
    assert not inspect.isabstract(kiamacs::CompositeCS)


def test_kiamacs::compositecs_constructor_exists():
    assert callable(kiamacs::CompositeCS.__init__)


def test_kiamacs::compositecs_constructor_args():
    sig = inspect.signature(kiamacs::CompositeCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs::eobject_is_not_abstract():
    assert not inspect.isabstract(kiamacs::EObject)


def test_kiamacs::eobject_constructor_exists():
    assert callable(kiamacs::EObject.__init__)


def test_kiamacs::eobject_constructor_args():
    sig = inspect.signature(kiamacs::EObject.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs::basecs_is_not_abstract():
    assert not inspect.isabstract(kiamacs::BaseCS)


def test_kiamacs::basecs_constructor_exists():
    assert callable(kiamacs::BaseCS.__init__)


def test_kiamacs::basecs_constructor_args():
    sig = inspect.signature(kiamacs::BaseCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs::leafcs_is_not_abstract():
    assert not inspect.isabstract(kiamacs::LeafCS)


def test_kiamacs::leafcs_constructor_exists():
    assert callable(kiamacs::LeafCS.__init__)


def test_kiamacs::leafcs_constructor_args():
    sig = inspect.signature(kiamacs::LeafCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_is_not_abstract():
    assert not inspect.isabstract(BaseCS)


def test_basecs_constructor_exists():
    assert callable(BaseCS.__init__)


def test_basecs_constructor_args():
    sig = inspect.signature(BaseCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs::nodecs_is_not_abstract():
    assert not inspect.isabstract(kiamacs::NodeCS)


def test_kiamacs::nodecs_constructor_exists():
    assert callable(kiamacs::NodeCS.__init__)


def test_kiamacs::nodecs_constructor_args():
    sig = inspect.signature(kiamacs::NodeCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs::topcs_is_not_abstract():
    assert not inspect.isabstract(kiamacs::TopCS)


def test_kiamacs::topcs_constructor_exists():
    assert callable(kiamacs::TopCS.__init__)


def test_kiamacs::topcs_constructor_args():
    sig = inspect.signature(kiamacs::TopCS.__init__)
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
kiamacs::CompositeCS_strategy = st.builds(
    kiamacs::CompositeCS,
)
kiamacs::EObject_strategy = st.builds(
    kiamacs::EObject,
)
kiamacs::BaseCS_strategy = st.builds(
    kiamacs::BaseCS,
)
kiamacs::LeafCS_strategy = st.builds(
    kiamacs::LeafCS,
)
BaseCS_strategy = st.builds(
    BaseCS,
)
kiamacs::NodeCS_strategy = st.builds(
    kiamacs::NodeCS,
)
kiamacs::TopCS_strategy = st.builds(
    kiamacs::TopCS,
)

@given(instance=NodeCS_strategy)
@settings(max_examples=50)
def test_nodecs_instantiation(instance):
    assert isinstance(instance, NodeCS)

@given(instance=kiamacs::CompositeCS_strategy)
@settings(max_examples=50)
def test_kiamacs::compositecs_instantiation(instance):
    assert isinstance(instance, kiamacs::CompositeCS)

@given(instance=kiamacs::EObject_strategy)
@settings(max_examples=50)
def test_kiamacs::eobject_instantiation(instance):
    assert isinstance(instance, kiamacs::EObject)

@given(instance=kiamacs::BaseCS_strategy)
@settings(max_examples=50)
def test_kiamacs::basecs_instantiation(instance):
    assert isinstance(instance, kiamacs::BaseCS)

@given(instance=kiamacs::LeafCS_strategy)
@settings(max_examples=50)
def test_kiamacs::leafcs_instantiation(instance):
    assert isinstance(instance, kiamacs::LeafCS)

@given(instance=BaseCS_strategy)
@settings(max_examples=50)
def test_basecs_instantiation(instance):
    assert isinstance(instance, BaseCS)

@given(instance=kiamacs::NodeCS_strategy)
@settings(max_examples=50)
def test_kiamacs::nodecs_instantiation(instance):
    assert isinstance(instance, kiamacs::NodeCS)

@given(instance=kiamacs::TopCS_strategy)
@settings(max_examples=50)
def test_kiamacs::topcs_instantiation(instance):
    assert isinstance(instance, kiamacs::TopCS)

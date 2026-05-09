import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    kiamacs::EObject,
    kiamacs::BaseCS,
    NodeCS,
    kiamacs::NumCS,
    kiamacs::PlusCS,
    BaseCS,
    kiamacs::NodeCS,
    kiamacs::TopCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_nodecs_is_not_abstract():
    assert not inspect.isabstract(NodeCS)


def test_nodecs_constructor_exists():
    assert callable(NodeCS.__init__)


def test_nodecs_constructor_args():
    sig = inspect.signature(NodeCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs::numcs_is_not_abstract():
    assert not inspect.isabstract(kiamacs::NumCS)


def test_kiamacs::numcs_constructor_exists():
    assert callable(kiamacs::NumCS.__init__)


def test_kiamacs::numcs_constructor_args():
    sig = inspect.signature(kiamacs::NumCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kiamacs::numcs_has_value():
    assert hasattr(kiamacs::NumCS, "value")
    descriptor = None
    for klass in kiamacs::NumCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kiamacs::pluscs_is_not_abstract():
    assert not inspect.isabstract(kiamacs::PlusCS)


def test_kiamacs::pluscs_constructor_exists():
    assert callable(kiamacs::PlusCS.__init__)


def test_kiamacs::pluscs_constructor_args():
    sig = inspect.signature(kiamacs::PlusCS.__init__)
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
kiamacs::EObject_strategy = st.builds(
    kiamacs::EObject,
)
kiamacs::BaseCS_strategy = st.builds(
    kiamacs::BaseCS,
)
NodeCS_strategy = st.builds(
    NodeCS,
)
kiamacs::NumCS_strategy = st.builds(
    kiamacs::NumCS,
    value=
        st.integers()
)
kiamacs::PlusCS_strategy = st.builds(
    kiamacs::PlusCS,
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

@given(instance=kiamacs::EObject_strategy)
@settings(max_examples=50)
def test_kiamacs::eobject_instantiation(instance):
    assert isinstance(instance, kiamacs::EObject)

@given(instance=kiamacs::BaseCS_strategy)
@settings(max_examples=50)
def test_kiamacs::basecs_instantiation(instance):
    assert isinstance(instance, kiamacs::BaseCS)

@given(instance=NodeCS_strategy)
@settings(max_examples=50)
def test_nodecs_instantiation(instance):
    assert isinstance(instance, NodeCS)

@given(instance=kiamacs::NumCS_strategy)
@settings(max_examples=50)
def test_kiamacs::numcs_instantiation(instance):
    assert isinstance(instance, kiamacs::NumCS)

@given(instance=kiamacs::NumCS_strategy)
def test_kiamacs::numcs_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=kiamacs::NumCS_strategy)
def test_kiamacs::numcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=kiamacs::PlusCS_strategy)
@settings(max_examples=50)
def test_kiamacs::pluscs_instantiation(instance):
    assert isinstance(instance, kiamacs::PlusCS)

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

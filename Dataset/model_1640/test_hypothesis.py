import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    kiamacs_EObject,
    kiamacs_BaseCS,
    NodeCS,
    kiamacs_NumCS,
    kiamacs_PlusCS,
    BaseCS,
    kiamacs_NodeCS,
    kiamacs_TopCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_nodecs_is_not_abstract():
    assert not inspect.isabstract(NodeCS)


def test_nodecs_constructor_exists():
    assert callable(NodeCS.__init__)


def test_nodecs_constructor_args():
    sig = inspect.signature(NodeCS.__init__)
    params = list(sig.parameters.keys())



def test_kiamacs_numcs_is_not_abstract():
    assert not inspect.isabstract(kiamacs_NumCS)


def test_kiamacs_numcs_constructor_exists():
    assert callable(kiamacs_NumCS.__init__)


def test_kiamacs_numcs_constructor_args():
    sig = inspect.signature(kiamacs_NumCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kiamacs_numcs_has_value():
    assert hasattr(kiamacs_NumCS, "value")
    descriptor = None
    for klass in kiamacs_NumCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kiamacs_pluscs_is_not_abstract():
    assert not inspect.isabstract(kiamacs_PlusCS)


def test_kiamacs_pluscs_constructor_exists():
    assert callable(kiamacs_PlusCS.__init__)


def test_kiamacs_pluscs_constructor_args():
    sig = inspect.signature(kiamacs_PlusCS.__init__)
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
kiamacs_EObject_strategy = st.builds(
    kiamacs_EObject,
)
kiamacs_BaseCS_strategy = st.builds(
    kiamacs_BaseCS,
)
NodeCS_strategy = st.builds(
    NodeCS,
)
kiamacs_NumCS_strategy = st.builds(
    kiamacs_NumCS,
    value=
        st.integers()
)
kiamacs_PlusCS_strategy = st.builds(
    kiamacs_PlusCS,
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

@given(instance=kiamacs_EObject_strategy)
@settings(max_examples=50)
def test_kiamacs_eobject_instantiation(instance):
    assert isinstance(instance, kiamacs_EObject)

@given(instance=kiamacs_BaseCS_strategy)
@settings(max_examples=50)
def test_kiamacs_basecs_instantiation(instance):
    assert isinstance(instance, kiamacs_BaseCS)

@given(instance=NodeCS_strategy)
@settings(max_examples=50)
def test_nodecs_instantiation(instance):
    assert isinstance(instance, NodeCS)

@given(instance=kiamacs_NumCS_strategy)
@settings(max_examples=50)
def test_kiamacs_numcs_instantiation(instance):
    assert isinstance(instance, kiamacs_NumCS)



@given(instance=kiamacs_NumCS_strategy)
def test_kiamacs_numcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=kiamacs_PlusCS_strategy)
@settings(max_examples=50)
def test_kiamacs_pluscs_instantiation(instance):
    assert isinstance(instance, kiamacs_PlusCS)

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

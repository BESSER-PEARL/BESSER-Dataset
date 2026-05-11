import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testmerge::F,
    testmerge::E,
    testmerge::C,
    testmerge::D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmerge::f_is_not_abstract():
    assert not inspect.isabstract(testmerge::F)


def test_testmerge::f_constructor_exists():
    assert callable(testmerge::F.__init__)


def test_testmerge::f_constructor_args():
    sig = inspect.signature(testmerge::F.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::e_is_not_abstract():
    assert not inspect.isabstract(testmerge::E)


def test_testmerge::e_constructor_exists():
    assert callable(testmerge::E.__init__)


def test_testmerge::e_constructor_args():
    sig = inspect.signature(testmerge::E.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::c_is_not_abstract():
    assert not inspect.isabstract(testmerge::C)


def test_testmerge::c_constructor_exists():
    assert callable(testmerge::C.__init__)


def test_testmerge::c_constructor_args():
    sig = inspect.signature(testmerge::C.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_testmerge::c_has_dataType():
    assert hasattr(testmerge::C, "dataType")
    descriptor = None
    for klass in testmerge::C.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_testmerge::d_is_not_abstract():
    assert not inspect.isabstract(testmerge::D)


def test_testmerge::d_constructor_exists():
    assert callable(testmerge::D.__init__)


def test_testmerge::d_constructor_args():
    sig = inspect.signature(testmerge::D.__init__)
    params = list(sig.parameters.keys())
    assert "emfDataType" in params, "Missing parameter 'emfDataType'"

def test_testmerge::d_has_emfDataType():
    assert hasattr(testmerge::D, "emfDataType")
    descriptor = None
    for klass in testmerge::D.__mro__:
        if "emfDataType" in klass.__dict__:
            descriptor = klass.__dict__["emfDataType"]
            break
    assert isinstance(descriptor, property)


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
testmerge::F_strategy = st.builds(
    testmerge::F,
)
testmerge::E_strategy = st.builds(
    testmerge::E,
)
testmerge::C_strategy = st.builds(
    testmerge::C,
    dataType=
        safe_text
)
testmerge::D_strategy = st.builds(
    testmerge::D,
    emfDataType=
        safe_text
)

@given(instance=testmerge::F_strategy)
@settings(max_examples=50)
def test_testmerge::f_instantiation(instance):
    assert isinstance(instance, testmerge::F)

@given(instance=testmerge::E_strategy)
@settings(max_examples=50)
def test_testmerge::e_instantiation(instance):
    assert isinstance(instance, testmerge::E)

@given(instance=testmerge::C_strategy)
@settings(max_examples=50)
def test_testmerge::c_instantiation(instance):
    assert isinstance(instance, testmerge::C)

@given(instance=testmerge::C_strategy)
def test_testmerge::c_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=testmerge::C_strategy)
def test_testmerge::c_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=testmerge::D_strategy)
@settings(max_examples=50)
def test_testmerge::d_instantiation(instance):
    assert isinstance(instance, testmerge::D)

@given(instance=testmerge::D_strategy)
def test_testmerge::d_emfDataType_type(instance):
    assert isinstance(instance.emfDataType, str)


@given(instance=testmerge::D_strategy)
def test_testmerge::d_emfDataType_setter(instance):
    original = instance.emfDataType
    instance.emfDataType = original
    assert instance.emfDataType == original

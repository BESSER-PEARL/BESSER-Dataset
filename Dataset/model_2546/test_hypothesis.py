import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testmerge_F,
    testmerge_E,
    testmerge_C,
    testmerge_D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmerge_f_is_not_abstract():
    assert not inspect.isabstract(testmerge_F)


def test_testmerge_f_constructor_exists():
    assert callable(testmerge_F.__init__)


def test_testmerge_f_constructor_args():
    sig = inspect.signature(testmerge_F.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_e_is_not_abstract():
    assert not inspect.isabstract(testmerge_E)


def test_testmerge_e_constructor_exists():
    assert callable(testmerge_E.__init__)


def test_testmerge_e_constructor_args():
    sig = inspect.signature(testmerge_E.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_c_is_not_abstract():
    assert not inspect.isabstract(testmerge_C)


def test_testmerge_c_constructor_exists():
    assert callable(testmerge_C.__init__)


def test_testmerge_c_constructor_args():
    sig = inspect.signature(testmerge_C.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_testmerge_c_has_dataType():
    assert hasattr(testmerge_C, "dataType")
    descriptor = None
    for klass in testmerge_C.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_testmerge_d_is_not_abstract():
    assert not inspect.isabstract(testmerge_D)


def test_testmerge_d_constructor_exists():
    assert callable(testmerge_D.__init__)


def test_testmerge_d_constructor_args():
    sig = inspect.signature(testmerge_D.__init__)
    params = list(sig.parameters.keys())
    assert "emfDataType" in params, "Missing parameter 'emfDataType'"

def test_testmerge_d_has_emfDataType():
    assert hasattr(testmerge_D, "emfDataType")
    descriptor = None
    for klass in testmerge_D.__mro__:
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
testmerge_F_strategy = st.builds(
    testmerge_F,
)
testmerge_E_strategy = st.builds(
    testmerge_E,
)
testmerge_C_strategy = st.builds(
    testmerge_C,
    dataType=
        safe_text
)
testmerge_D_strategy = st.builds(
    testmerge_D,
    emfDataType=
        safe_text
)

@given(instance=testmerge_F_strategy)
@settings(max_examples=50)
def test_testmerge_f_instantiation(instance):
    assert isinstance(instance, testmerge_F)

@given(instance=testmerge_E_strategy)
@settings(max_examples=50)
def test_testmerge_e_instantiation(instance):
    assert isinstance(instance, testmerge_E)

@given(instance=testmerge_C_strategy)
@settings(max_examples=50)
def test_testmerge_c_instantiation(instance):
    assert isinstance(instance, testmerge_C)



@given(instance=testmerge_C_strategy)
def test_testmerge_c_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=testmerge_D_strategy)
@settings(max_examples=50)
def test_testmerge_d_instantiation(instance):
    assert isinstance(instance, testmerge_D)



@given(instance=testmerge_D_strategy)
def test_testmerge_d_emfDataType_setter(instance):
    original = instance.emfDataType
    instance.emfDataType = original
    assert instance.emfDataType == original

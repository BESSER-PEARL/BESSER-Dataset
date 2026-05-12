import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_EClass,
    test_EClassToAMap,
    test_EClassToEStringMap,
    test_D,
    test_C,
    test_B,
    test_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_eclass_is_not_abstract():
    assert not inspect.isabstract(test_EClass)


def test_test_eclass_constructor_exists():
    assert callable(test_EClass.__init__)


def test_test_eclass_constructor_args():
    sig = inspect.signature(test_EClass.__init__)
    params = list(sig.parameters.keys())



def test_test_eclasstoamap_is_not_abstract():
    assert not inspect.isabstract(test_EClassToAMap)


def test_test_eclasstoamap_constructor_exists():
    assert callable(test_EClassToAMap.__init__)


def test_test_eclasstoamap_constructor_args():
    sig = inspect.signature(test_EClassToAMap.__init__)
    params = list(sig.parameters.keys())



def test_test_eclasstoestringmap_is_not_abstract():
    assert not inspect.isabstract(test_EClassToEStringMap)


def test_test_eclasstoestringmap_constructor_exists():
    assert callable(test_EClassToEStringMap.__init__)


def test_test_eclasstoestringmap_constructor_args():
    sig = inspect.signature(test_EClassToEStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_test_eclasstoestringmap_has_value():
    assert hasattr(test_EClassToEStringMap, "value")
    descriptor = None
    for klass in test_EClassToEStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_test_d_is_not_abstract():
    assert not inspect.isabstract(test_D)


def test_test_d_constructor_exists():
    assert callable(test_D.__init__)


def test_test_d_constructor_args():
    sig = inspect.signature(test_D.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "yList" in params, "Missing parameter 'yList'"

def test_test_d_has_x():
    assert hasattr(test_D, "x")
    descriptor = None
    for klass in test_D.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_test_d_has_yList():
    assert hasattr(test_D, "yList")
    descriptor = None
    for klass in test_D.__mro__:
        if "yList" in klass.__dict__:
            descriptor = klass.__dict__["yList"]
            break
    assert isinstance(descriptor, property)



def test_test_c_is_not_abstract():
    assert not inspect.isabstract(test_C)


def test_test_c_constructor_exists():
    assert callable(test_C.__init__)


def test_test_c_constructor_args():
    sig = inspect.signature(test_C.__init__)
    params = list(sig.parameters.keys())



def test_test_b_is_not_abstract():
    assert not inspect.isabstract(test_B)


def test_test_b_constructor_exists():
    assert callable(test_B.__init__)


def test_test_b_constructor_args():
    sig = inspect.signature(test_B.__init__)
    params = list(sig.parameters.keys())



def test_test_a_is_not_abstract():
    assert not inspect.isabstract(test_A)


def test_test_a_constructor_exists():
    assert callable(test_A.__init__)


def test_test_a_constructor_args():
    sig = inspect.signature(test_A.__init__)
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
test_EClass_strategy = st.builds(
    test_EClass,
)
test_EClassToAMap_strategy = st.builds(
    test_EClassToAMap,
)
test_EClassToEStringMap_strategy = st.builds(
    test_EClassToEStringMap,
    value=
        safe_text
)
test_D_strategy = st.builds(
    test_D,
    x=
        safe_text,
    yList=
        st.integers()
)
test_C_strategy = st.builds(
    test_C,
)
test_B_strategy = st.builds(
    test_B,
)
test_A_strategy = st.builds(
    test_A,
)

@given(instance=test_EClass_strategy)
@settings(max_examples=50)
def test_test_eclass_instantiation(instance):
    assert isinstance(instance, test_EClass)

@given(instance=test_EClassToAMap_strategy)
@settings(max_examples=50)
def test_test_eclasstoamap_instantiation(instance):
    assert isinstance(instance, test_EClassToAMap)

@given(instance=test_EClassToEStringMap_strategy)
@settings(max_examples=50)
def test_test_eclasstoestringmap_instantiation(instance):
    assert isinstance(instance, test_EClassToEStringMap)



@given(instance=test_EClassToEStringMap_strategy)
def test_test_eclasstoestringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=test_D_strategy)
@settings(max_examples=50)
def test_test_d_instantiation(instance):
    assert isinstance(instance, test_D)



@given(instance=test_D_strategy)
def test_test_d_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=test_D_strategy)
def test_test_d_yList_setter(instance):
    original = instance.yList
    instance.yList = original
    assert instance.yList == original

@given(instance=test_C_strategy)
@settings(max_examples=50)
def test_test_c_instantiation(instance):
    assert isinstance(instance, test_C)

@given(instance=test_B_strategy)
@settings(max_examples=50)
def test_test_b_instantiation(instance):
    assert isinstance(instance, test_B)

@given(instance=test_A_strategy)
@settings(max_examples=50)
def test_test_a_instantiation(instance):
    assert isinstance(instance, test_A)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::B,
    test::A,
    test::EClass,
    test::EClassToAMap,
    test::EClassToEStringMap,
    test::D,
    test::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::b_is_not_abstract():
    assert not inspect.isabstract(test::B)


def test_test::b_constructor_exists():
    assert callable(test::B.__init__)


def test_test::b_constructor_args():
    sig = inspect.signature(test::B.__init__)
    params = list(sig.parameters.keys())



def test_test::a_is_not_abstract():
    assert not inspect.isabstract(test::A)


def test_test::a_constructor_exists():
    assert callable(test::A.__init__)


def test_test::a_constructor_args():
    sig = inspect.signature(test::A.__init__)
    params = list(sig.parameters.keys())



def test_test::eclass_is_not_abstract():
    assert not inspect.isabstract(test::EClass)


def test_test::eclass_constructor_exists():
    assert callable(test::EClass.__init__)


def test_test::eclass_constructor_args():
    sig = inspect.signature(test::EClass.__init__)
    params = list(sig.parameters.keys())



def test_test::eclasstoamap_is_not_abstract():
    assert not inspect.isabstract(test::EClassToAMap)


def test_test::eclasstoamap_constructor_exists():
    assert callable(test::EClassToAMap.__init__)


def test_test::eclasstoamap_constructor_args():
    sig = inspect.signature(test::EClassToAMap.__init__)
    params = list(sig.parameters.keys())



def test_test::eclasstoestringmap_is_not_abstract():
    assert not inspect.isabstract(test::EClassToEStringMap)


def test_test::eclasstoestringmap_constructor_exists():
    assert callable(test::EClassToEStringMap.__init__)


def test_test::eclasstoestringmap_constructor_args():
    sig = inspect.signature(test::EClassToEStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_test::eclasstoestringmap_has_value():
    assert hasattr(test::EClassToEStringMap, "value")
    descriptor = None
    for klass in test::EClassToEStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_test::d_is_not_abstract():
    assert not inspect.isabstract(test::D)


def test_test::d_constructor_exists():
    assert callable(test::D.__init__)


def test_test::d_constructor_args():
    sig = inspect.signature(test::D.__init__)
    params = list(sig.parameters.keys())
    assert "yList" in params, "Missing parameter 'yList'"
    assert "x" in params, "Missing parameter 'x'"

def test_test::d_has_yList():
    assert hasattr(test::D, "yList")
    descriptor = None
    for klass in test::D.__mro__:
        if "yList" in klass.__dict__:
            descriptor = klass.__dict__["yList"]
            break
    assert isinstance(descriptor, property)

def test_test::d_has_x():
    assert hasattr(test::D, "x")
    descriptor = None
    for klass in test::D.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_test::c_is_not_abstract():
    assert not inspect.isabstract(test::C)


def test_test::c_constructor_exists():
    assert callable(test::C.__init__)


def test_test::c_constructor_args():
    sig = inspect.signature(test::C.__init__)
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
test::B_strategy = st.builds(
    test::B,
)
test::A_strategy = st.builds(
    test::A,
)
test::EClass_strategy = st.builds(
    test::EClass,
)
test::EClassToAMap_strategy = st.builds(
    test::EClassToAMap,
)
test::EClassToEStringMap_strategy = st.builds(
    test::EClassToEStringMap,
    value=
        safe_text
)
test::D_strategy = st.builds(
    test::D,
    yList=
        st.integers(),
    x=
        safe_text
)
test::C_strategy = st.builds(
    test::C,
)

@given(instance=test::B_strategy)
@settings(max_examples=50)
def test_test::b_instantiation(instance):
    assert isinstance(instance, test::B)

@given(instance=test::A_strategy)
@settings(max_examples=50)
def test_test::a_instantiation(instance):
    assert isinstance(instance, test::A)

@given(instance=test::EClass_strategy)
@settings(max_examples=50)
def test_test::eclass_instantiation(instance):
    assert isinstance(instance, test::EClass)

@given(instance=test::EClassToAMap_strategy)
@settings(max_examples=50)
def test_test::eclasstoamap_instantiation(instance):
    assert isinstance(instance, test::EClassToAMap)

@given(instance=test::EClassToEStringMap_strategy)
@settings(max_examples=50)
def test_test::eclasstoestringmap_instantiation(instance):
    assert isinstance(instance, test::EClassToEStringMap)

@given(instance=test::EClassToEStringMap_strategy)
def test_test::eclasstoestringmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=test::EClassToEStringMap_strategy)
def test_test::eclasstoestringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=test::D_strategy)
@settings(max_examples=50)
def test_test::d_instantiation(instance):
    assert isinstance(instance, test::D)

@given(instance=test::D_strategy)
def test_test::d_yList_type(instance):
    assert isinstance(instance.yList, int)


@given(instance=test::D_strategy)
def test_test::d_yList_setter(instance):
    original = instance.yList
    instance.yList = original
    assert instance.yList == original

@given(instance=test::D_strategy)
def test_test::d_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=test::D_strategy)
def test_test::d_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=test::C_strategy)
@settings(max_examples=50)
def test_test::c_instantiation(instance):
    assert isinstance(instance, test::C)

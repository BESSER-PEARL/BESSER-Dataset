import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MyClass33,
    MyClass43,
    MyClass23,
    MyClass6,
    MyClass32,
    MyClass42,
    MyClass22,
    MyClass5,
    MyClass4,
    MyClass3,
    MyClass2,
    MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myclass33_is_not_abstract():
    assert not inspect.isabstract(MyClass33)


def test_myclass33_constructor_exists():
    assert callable(MyClass33.__init__)


def test_myclass33_constructor_args():
    sig = inspect.signature(MyClass33.__init__)
    params = list(sig.parameters.keys())



def test_myclass43_is_not_abstract():
    assert not inspect.isabstract(MyClass43)


def test_myclass43_constructor_exists():
    assert callable(MyClass43.__init__)


def test_myclass43_constructor_args():
    sig = inspect.signature(MyClass43.__init__)
    params = list(sig.parameters.keys())



def test_myclass23_is_not_abstract():
    assert not inspect.isabstract(MyClass23)


def test_myclass23_constructor_exists():
    assert callable(MyClass23.__init__)


def test_myclass23_constructor_args():
    sig = inspect.signature(MyClass23.__init__)
    params = list(sig.parameters.keys())



def test_myclass6_is_not_abstract():
    assert not inspect.isabstract(MyClass6)


def test_myclass6_constructor_exists():
    assert callable(MyClass6.__init__)


def test_myclass6_constructor_args():
    sig = inspect.signature(MyClass6.__init__)
    params = list(sig.parameters.keys())



def test_myclass32_is_not_abstract():
    assert not inspect.isabstract(MyClass32)


def test_myclass32_constructor_exists():
    assert callable(MyClass32.__init__)


def test_myclass32_constructor_args():
    sig = inspect.signature(MyClass32.__init__)
    params = list(sig.parameters.keys())



def test_myclass42_is_not_abstract():
    assert not inspect.isabstract(MyClass42)


def test_myclass42_constructor_exists():
    assert callable(MyClass42.__init__)


def test_myclass42_constructor_args():
    sig = inspect.signature(MyClass42.__init__)
    params = list(sig.parameters.keys())



def test_myclass22_is_not_abstract():
    assert not inspect.isabstract(MyClass22)


def test_myclass22_constructor_exists():
    assert callable(MyClass22.__init__)


def test_myclass22_constructor_args():
    sig = inspect.signature(MyClass22.__init__)
    params = list(sig.parameters.keys())



def test_myclass5_is_not_abstract():
    assert not inspect.isabstract(MyClass5)


def test_myclass5_constructor_exists():
    assert callable(MyClass5.__init__)


def test_myclass5_constructor_args():
    sig = inspect.signature(MyClass5.__init__)
    params = list(sig.parameters.keys())



def test_myclass4_is_not_abstract():
    assert not inspect.isabstract(MyClass4)


def test_myclass4_constructor_exists():
    assert callable(MyClass4.__init__)


def test_myclass4_constructor_args():
    sig = inspect.signature(MyClass4.__init__)
    params = list(sig.parameters.keys())



def test_myclass3_is_not_abstract():
    assert not inspect.isabstract(MyClass3)


def test_myclass3_constructor_exists():
    assert callable(MyClass3.__init__)


def test_myclass3_constructor_args():
    sig = inspect.signature(MyClass3.__init__)
    params = list(sig.parameters.keys())



def test_myclass2_is_not_abstract():
    assert not inspect.isabstract(MyClass2)


def test_myclass2_constructor_exists():
    assert callable(MyClass2.__init__)


def test_myclass2_constructor_args():
    sig = inspect.signature(MyClass2.__init__)
    params = list(sig.parameters.keys())



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
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
MyClass33_strategy = st.builds(
    MyClass33,
)
MyClass43_strategy = st.builds(
    MyClass43,
)
MyClass23_strategy = st.builds(
    MyClass23,
)
MyClass6_strategy = st.builds(
    MyClass6,
)
MyClass32_strategy = st.builds(
    MyClass32,
)
MyClass42_strategy = st.builds(
    MyClass42,
)
MyClass22_strategy = st.builds(
    MyClass22,
)
MyClass5_strategy = st.builds(
    MyClass5,
)
MyClass4_strategy = st.builds(
    MyClass4,
)
MyClass3_strategy = st.builds(
    MyClass3,
)
MyClass2_strategy = st.builds(
    MyClass2,
)
MyClass_strategy = st.builds(
    MyClass,
)

@given(instance=MyClass33_strategy)
@settings(max_examples=50)
def test_myclass33_instantiation(instance):
    assert isinstance(instance, MyClass33)

@given(instance=MyClass43_strategy)
@settings(max_examples=50)
def test_myclass43_instantiation(instance):
    assert isinstance(instance, MyClass43)

@given(instance=MyClass23_strategy)
@settings(max_examples=50)
def test_myclass23_instantiation(instance):
    assert isinstance(instance, MyClass23)

@given(instance=MyClass6_strategy)
@settings(max_examples=50)
def test_myclass6_instantiation(instance):
    assert isinstance(instance, MyClass6)

@given(instance=MyClass32_strategy)
@settings(max_examples=50)
def test_myclass32_instantiation(instance):
    assert isinstance(instance, MyClass32)

@given(instance=MyClass42_strategy)
@settings(max_examples=50)
def test_myclass42_instantiation(instance):
    assert isinstance(instance, MyClass42)

@given(instance=MyClass22_strategy)
@settings(max_examples=50)
def test_myclass22_instantiation(instance):
    assert isinstance(instance, MyClass22)

@given(instance=MyClass5_strategy)
@settings(max_examples=50)
def test_myclass5_instantiation(instance):
    assert isinstance(instance, MyClass5)

@given(instance=MyClass4_strategy)
@settings(max_examples=50)
def test_myclass4_instantiation(instance):
    assert isinstance(instance, MyClass4)

@given(instance=MyClass3_strategy)
@settings(max_examples=50)
def test_myclass3_instantiation(instance):
    assert isinstance(instance, MyClass3)

@given(instance=MyClass2_strategy)
@settings(max_examples=50)
def test_myclass2_instantiation(instance):
    assert isinstance(instance, MyClass2)

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)

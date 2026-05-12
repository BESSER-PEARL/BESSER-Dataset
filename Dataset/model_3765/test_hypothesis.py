import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    toppkg_subpkg3_Subpkg3Class2,
    subpkg3_Subpkg3Class2,
    toppkg_subpkg3_Subpkg3Class1,
    subpkg3_Subpkg3Class1,
    toppkg_subpkg2_Subpkg2Class2,
    Subpkg2Class2,
    toppkg_subpkg2_Subpkg2Class1,
    toppkg_subpkg1_Subpkg1Class2,
    Subpkg1Class2,
    toppkg_subpkg1_Subpkg1Class1,
    toppkg_TopClass1,
    Subpkg2Class1,
    Subpkg1Class1,
    toppkg_TopClass2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_toppkg_subpkg3_subpkg3class2_is_not_abstract():
    assert not inspect.isabstract(toppkg_subpkg3_Subpkg3Class2)


def test_toppkg_subpkg3_subpkg3class2_constructor_exists():
    assert callable(toppkg_subpkg3_Subpkg3Class2.__init__)


def test_toppkg_subpkg3_subpkg3class2_constructor_args():
    sig = inspect.signature(toppkg_subpkg3_Subpkg3Class2.__init__)
    params = list(sig.parameters.keys())



def test_subpkg3_subpkg3class2_is_not_abstract():
    assert not inspect.isabstract(subpkg3_Subpkg3Class2)


def test_subpkg3_subpkg3class2_constructor_exists():
    assert callable(subpkg3_Subpkg3Class2.__init__)


def test_subpkg3_subpkg3class2_constructor_args():
    sig = inspect.signature(subpkg3_Subpkg3Class2.__init__)
    params = list(sig.parameters.keys())



def test_toppkg_subpkg3_subpkg3class1_is_not_abstract():
    assert not inspect.isabstract(toppkg_subpkg3_Subpkg3Class1)


def test_toppkg_subpkg3_subpkg3class1_constructor_exists():
    assert callable(toppkg_subpkg3_Subpkg3Class1.__init__)


def test_toppkg_subpkg3_subpkg3class1_constructor_args():
    sig = inspect.signature(toppkg_subpkg3_Subpkg3Class1.__init__)
    params = list(sig.parameters.keys())



def test_subpkg3_subpkg3class1_is_not_abstract():
    assert not inspect.isabstract(subpkg3_Subpkg3Class1)


def test_subpkg3_subpkg3class1_constructor_exists():
    assert callable(subpkg3_Subpkg3Class1.__init__)


def test_subpkg3_subpkg3class1_constructor_args():
    sig = inspect.signature(subpkg3_Subpkg3Class1.__init__)
    params = list(sig.parameters.keys())



def test_toppkg_subpkg2_subpkg2class2_is_not_abstract():
    assert not inspect.isabstract(toppkg_subpkg2_Subpkg2Class2)


def test_toppkg_subpkg2_subpkg2class2_constructor_exists():
    assert callable(toppkg_subpkg2_Subpkg2Class2.__init__)


def test_toppkg_subpkg2_subpkg2class2_constructor_args():
    sig = inspect.signature(toppkg_subpkg2_Subpkg2Class2.__init__)
    params = list(sig.parameters.keys())



def test_subpkg2class2_is_not_abstract():
    assert not inspect.isabstract(Subpkg2Class2)


def test_subpkg2class2_constructor_exists():
    assert callable(Subpkg2Class2.__init__)


def test_subpkg2class2_constructor_args():
    sig = inspect.signature(Subpkg2Class2.__init__)
    params = list(sig.parameters.keys())



def test_toppkg_subpkg2_subpkg2class1_is_not_abstract():
    assert not inspect.isabstract(toppkg_subpkg2_Subpkg2Class1)


def test_toppkg_subpkg2_subpkg2class1_constructor_exists():
    assert callable(toppkg_subpkg2_Subpkg2Class1.__init__)


def test_toppkg_subpkg2_subpkg2class1_constructor_args():
    sig = inspect.signature(toppkg_subpkg2_Subpkg2Class1.__init__)
    params = list(sig.parameters.keys())



def test_toppkg_subpkg1_subpkg1class2_is_not_abstract():
    assert not inspect.isabstract(toppkg_subpkg1_Subpkg1Class2)


def test_toppkg_subpkg1_subpkg1class2_constructor_exists():
    assert callable(toppkg_subpkg1_Subpkg1Class2.__init__)


def test_toppkg_subpkg1_subpkg1class2_constructor_args():
    sig = inspect.signature(toppkg_subpkg1_Subpkg1Class2.__init__)
    params = list(sig.parameters.keys())



def test_subpkg1class2_is_not_abstract():
    assert not inspect.isabstract(Subpkg1Class2)


def test_subpkg1class2_constructor_exists():
    assert callable(Subpkg1Class2.__init__)


def test_subpkg1class2_constructor_args():
    sig = inspect.signature(Subpkg1Class2.__init__)
    params = list(sig.parameters.keys())



def test_toppkg_subpkg1_subpkg1class1_is_not_abstract():
    assert not inspect.isabstract(toppkg_subpkg1_Subpkg1Class1)


def test_toppkg_subpkg1_subpkg1class1_constructor_exists():
    assert callable(toppkg_subpkg1_Subpkg1Class1.__init__)


def test_toppkg_subpkg1_subpkg1class1_constructor_args():
    sig = inspect.signature(toppkg_subpkg1_Subpkg1Class1.__init__)
    params = list(sig.parameters.keys())



def test_toppkg_topclass1_is_not_abstract():
    assert not inspect.isabstract(toppkg_TopClass1)


def test_toppkg_topclass1_constructor_exists():
    assert callable(toppkg_TopClass1.__init__)


def test_toppkg_topclass1_constructor_args():
    sig = inspect.signature(toppkg_TopClass1.__init__)
    params = list(sig.parameters.keys())



def test_subpkg2class1_is_not_abstract():
    assert not inspect.isabstract(Subpkg2Class1)


def test_subpkg2class1_constructor_exists():
    assert callable(Subpkg2Class1.__init__)


def test_subpkg2class1_constructor_args():
    sig = inspect.signature(Subpkg2Class1.__init__)
    params = list(sig.parameters.keys())



def test_subpkg1class1_is_not_abstract():
    assert not inspect.isabstract(Subpkg1Class1)


def test_subpkg1class1_constructor_exists():
    assert callable(Subpkg1Class1.__init__)


def test_subpkg1class1_constructor_args():
    sig = inspect.signature(Subpkg1Class1.__init__)
    params = list(sig.parameters.keys())



def test_toppkg_topclass2_is_not_abstract():
    assert not inspect.isabstract(toppkg_TopClass2)


def test_toppkg_topclass2_constructor_exists():
    assert callable(toppkg_TopClass2.__init__)


def test_toppkg_topclass2_constructor_args():
    sig = inspect.signature(toppkg_TopClass2.__init__)
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
toppkg_subpkg3_Subpkg3Class2_strategy = st.builds(
    toppkg_subpkg3_Subpkg3Class2,
)
subpkg3_Subpkg3Class2_strategy = st.builds(
    subpkg3_Subpkg3Class2,
)
toppkg_subpkg3_Subpkg3Class1_strategy = st.builds(
    toppkg_subpkg3_Subpkg3Class1,
)
subpkg3_Subpkg3Class1_strategy = st.builds(
    subpkg3_Subpkg3Class1,
)
toppkg_subpkg2_Subpkg2Class2_strategy = st.builds(
    toppkg_subpkg2_Subpkg2Class2,
)
Subpkg2Class2_strategy = st.builds(
    Subpkg2Class2,
)
toppkg_subpkg2_Subpkg2Class1_strategy = st.builds(
    toppkg_subpkg2_Subpkg2Class1,
)
toppkg_subpkg1_Subpkg1Class2_strategy = st.builds(
    toppkg_subpkg1_Subpkg1Class2,
)
Subpkg1Class2_strategy = st.builds(
    Subpkg1Class2,
)
toppkg_subpkg1_Subpkg1Class1_strategy = st.builds(
    toppkg_subpkg1_Subpkg1Class1,
)
toppkg_TopClass1_strategy = st.builds(
    toppkg_TopClass1,
)
Subpkg2Class1_strategy = st.builds(
    Subpkg2Class1,
)
Subpkg1Class1_strategy = st.builds(
    Subpkg1Class1,
)
toppkg_TopClass2_strategy = st.builds(
    toppkg_TopClass2,
)

@given(instance=toppkg_subpkg3_Subpkg3Class2_strategy)
@settings(max_examples=50)
def test_toppkg_subpkg3_subpkg3class2_instantiation(instance):
    assert isinstance(instance, toppkg_subpkg3_Subpkg3Class2)

@given(instance=subpkg3_Subpkg3Class2_strategy)
@settings(max_examples=50)
def test_subpkg3_subpkg3class2_instantiation(instance):
    assert isinstance(instance, subpkg3_Subpkg3Class2)

@given(instance=toppkg_subpkg3_Subpkg3Class1_strategy)
@settings(max_examples=50)
def test_toppkg_subpkg3_subpkg3class1_instantiation(instance):
    assert isinstance(instance, toppkg_subpkg3_Subpkg3Class1)

@given(instance=subpkg3_Subpkg3Class1_strategy)
@settings(max_examples=50)
def test_subpkg3_subpkg3class1_instantiation(instance):
    assert isinstance(instance, subpkg3_Subpkg3Class1)

@given(instance=toppkg_subpkg2_Subpkg2Class2_strategy)
@settings(max_examples=50)
def test_toppkg_subpkg2_subpkg2class2_instantiation(instance):
    assert isinstance(instance, toppkg_subpkg2_Subpkg2Class2)

@given(instance=Subpkg2Class2_strategy)
@settings(max_examples=50)
def test_subpkg2class2_instantiation(instance):
    assert isinstance(instance, Subpkg2Class2)

@given(instance=toppkg_subpkg2_Subpkg2Class1_strategy)
@settings(max_examples=50)
def test_toppkg_subpkg2_subpkg2class1_instantiation(instance):
    assert isinstance(instance, toppkg_subpkg2_Subpkg2Class1)

@given(instance=toppkg_subpkg1_Subpkg1Class2_strategy)
@settings(max_examples=50)
def test_toppkg_subpkg1_subpkg1class2_instantiation(instance):
    assert isinstance(instance, toppkg_subpkg1_Subpkg1Class2)

@given(instance=Subpkg1Class2_strategy)
@settings(max_examples=50)
def test_subpkg1class2_instantiation(instance):
    assert isinstance(instance, Subpkg1Class2)

@given(instance=toppkg_subpkg1_Subpkg1Class1_strategy)
@settings(max_examples=50)
def test_toppkg_subpkg1_subpkg1class1_instantiation(instance):
    assert isinstance(instance, toppkg_subpkg1_Subpkg1Class1)

@given(instance=toppkg_TopClass1_strategy)
@settings(max_examples=50)
def test_toppkg_topclass1_instantiation(instance):
    assert isinstance(instance, toppkg_TopClass1)

@given(instance=Subpkg2Class1_strategy)
@settings(max_examples=50)
def test_subpkg2class1_instantiation(instance):
    assert isinstance(instance, Subpkg2Class1)

@given(instance=Subpkg1Class1_strategy)
@settings(max_examples=50)
def test_subpkg1class1_instantiation(instance):
    assert isinstance(instance, Subpkg1Class1)

@given(instance=toppkg_TopClass2_strategy)
@settings(max_examples=50)
def test_toppkg_topclass2_instantiation(instance):
    assert isinstance(instance, toppkg_TopClass2)

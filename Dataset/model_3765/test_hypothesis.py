import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    toppkg::subpkg3::Subpkg3Class2,
    subpkg3::Subpkg3Class2,
    toppkg::subpkg3::Subpkg3Class1,
    subpkg3::Subpkg3Class1,
    toppkg::subpkg2::Subpkg2Class2,
    Subpkg2Class2,
    toppkg::subpkg2::Subpkg2Class1,
    toppkg::subpkg1::Subpkg1Class2,
    Subpkg1Class2,
    toppkg::subpkg1::Subpkg1Class1,
    toppkg::TopClass1,
    Subpkg2Class1,
    Subpkg1Class1,
    toppkg::TopClass2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_toppkg::subpkg3::subpkg3class2_is_not_abstract():
    assert not inspect.isabstract(toppkg::subpkg3::Subpkg3Class2)


def test_toppkg::subpkg3::subpkg3class2_constructor_exists():
    assert callable(toppkg::subpkg3::Subpkg3Class2.__init__)


def test_toppkg::subpkg3::subpkg3class2_constructor_args():
    sig = inspect.signature(toppkg::subpkg3::Subpkg3Class2.__init__)
    params = list(sig.parameters.keys())



def test_subpkg3::subpkg3class2_is_not_abstract():
    assert not inspect.isabstract(subpkg3::Subpkg3Class2)


def test_subpkg3::subpkg3class2_constructor_exists():
    assert callable(subpkg3::Subpkg3Class2.__init__)


def test_subpkg3::subpkg3class2_constructor_args():
    sig = inspect.signature(subpkg3::Subpkg3Class2.__init__)
    params = list(sig.parameters.keys())



def test_toppkg::subpkg3::subpkg3class1_is_not_abstract():
    assert not inspect.isabstract(toppkg::subpkg3::Subpkg3Class1)


def test_toppkg::subpkg3::subpkg3class1_constructor_exists():
    assert callable(toppkg::subpkg3::Subpkg3Class1.__init__)


def test_toppkg::subpkg3::subpkg3class1_constructor_args():
    sig = inspect.signature(toppkg::subpkg3::Subpkg3Class1.__init__)
    params = list(sig.parameters.keys())



def test_subpkg3::subpkg3class1_is_not_abstract():
    assert not inspect.isabstract(subpkg3::Subpkg3Class1)


def test_subpkg3::subpkg3class1_constructor_exists():
    assert callable(subpkg3::Subpkg3Class1.__init__)


def test_subpkg3::subpkg3class1_constructor_args():
    sig = inspect.signature(subpkg3::Subpkg3Class1.__init__)
    params = list(sig.parameters.keys())



def test_toppkg::subpkg2::subpkg2class2_is_not_abstract():
    assert not inspect.isabstract(toppkg::subpkg2::Subpkg2Class2)


def test_toppkg::subpkg2::subpkg2class2_constructor_exists():
    assert callable(toppkg::subpkg2::Subpkg2Class2.__init__)


def test_toppkg::subpkg2::subpkg2class2_constructor_args():
    sig = inspect.signature(toppkg::subpkg2::Subpkg2Class2.__init__)
    params = list(sig.parameters.keys())



def test_subpkg2class2_is_not_abstract():
    assert not inspect.isabstract(Subpkg2Class2)


def test_subpkg2class2_constructor_exists():
    assert callable(Subpkg2Class2.__init__)


def test_subpkg2class2_constructor_args():
    sig = inspect.signature(Subpkg2Class2.__init__)
    params = list(sig.parameters.keys())



def test_toppkg::subpkg2::subpkg2class1_is_not_abstract():
    assert not inspect.isabstract(toppkg::subpkg2::Subpkg2Class1)


def test_toppkg::subpkg2::subpkg2class1_constructor_exists():
    assert callable(toppkg::subpkg2::Subpkg2Class1.__init__)


def test_toppkg::subpkg2::subpkg2class1_constructor_args():
    sig = inspect.signature(toppkg::subpkg2::Subpkg2Class1.__init__)
    params = list(sig.parameters.keys())



def test_toppkg::subpkg1::subpkg1class2_is_not_abstract():
    assert not inspect.isabstract(toppkg::subpkg1::Subpkg1Class2)


def test_toppkg::subpkg1::subpkg1class2_constructor_exists():
    assert callable(toppkg::subpkg1::Subpkg1Class2.__init__)


def test_toppkg::subpkg1::subpkg1class2_constructor_args():
    sig = inspect.signature(toppkg::subpkg1::Subpkg1Class2.__init__)
    params = list(sig.parameters.keys())



def test_subpkg1class2_is_not_abstract():
    assert not inspect.isabstract(Subpkg1Class2)


def test_subpkg1class2_constructor_exists():
    assert callable(Subpkg1Class2.__init__)


def test_subpkg1class2_constructor_args():
    sig = inspect.signature(Subpkg1Class2.__init__)
    params = list(sig.parameters.keys())



def test_toppkg::subpkg1::subpkg1class1_is_not_abstract():
    assert not inspect.isabstract(toppkg::subpkg1::Subpkg1Class1)


def test_toppkg::subpkg1::subpkg1class1_constructor_exists():
    assert callable(toppkg::subpkg1::Subpkg1Class1.__init__)


def test_toppkg::subpkg1::subpkg1class1_constructor_args():
    sig = inspect.signature(toppkg::subpkg1::Subpkg1Class1.__init__)
    params = list(sig.parameters.keys())



def test_toppkg::topclass1_is_not_abstract():
    assert not inspect.isabstract(toppkg::TopClass1)


def test_toppkg::topclass1_constructor_exists():
    assert callable(toppkg::TopClass1.__init__)


def test_toppkg::topclass1_constructor_args():
    sig = inspect.signature(toppkg::TopClass1.__init__)
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



def test_toppkg::topclass2_is_not_abstract():
    assert not inspect.isabstract(toppkg::TopClass2)


def test_toppkg::topclass2_constructor_exists():
    assert callable(toppkg::TopClass2.__init__)


def test_toppkg::topclass2_constructor_args():
    sig = inspect.signature(toppkg::TopClass2.__init__)
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
toppkg::subpkg3::Subpkg3Class2_strategy = st.builds(
    toppkg::subpkg3::Subpkg3Class2,
)
subpkg3::Subpkg3Class2_strategy = st.builds(
    subpkg3::Subpkg3Class2,
)
toppkg::subpkg3::Subpkg3Class1_strategy = st.builds(
    toppkg::subpkg3::Subpkg3Class1,
)
subpkg3::Subpkg3Class1_strategy = st.builds(
    subpkg3::Subpkg3Class1,
)
toppkg::subpkg2::Subpkg2Class2_strategy = st.builds(
    toppkg::subpkg2::Subpkg2Class2,
)
Subpkg2Class2_strategy = st.builds(
    Subpkg2Class2,
)
toppkg::subpkg2::Subpkg2Class1_strategy = st.builds(
    toppkg::subpkg2::Subpkg2Class1,
)
toppkg::subpkg1::Subpkg1Class2_strategy = st.builds(
    toppkg::subpkg1::Subpkg1Class2,
)
Subpkg1Class2_strategy = st.builds(
    Subpkg1Class2,
)
toppkg::subpkg1::Subpkg1Class1_strategy = st.builds(
    toppkg::subpkg1::Subpkg1Class1,
)
toppkg::TopClass1_strategy = st.builds(
    toppkg::TopClass1,
)
Subpkg2Class1_strategy = st.builds(
    Subpkg2Class1,
)
Subpkg1Class1_strategy = st.builds(
    Subpkg1Class1,
)
toppkg::TopClass2_strategy = st.builds(
    toppkg::TopClass2,
)

@given(instance=toppkg::subpkg3::Subpkg3Class2_strategy)
@settings(max_examples=50)
def test_toppkg::subpkg3::subpkg3class2_instantiation(instance):
    assert isinstance(instance, toppkg::subpkg3::Subpkg3Class2)

@given(instance=subpkg3::Subpkg3Class2_strategy)
@settings(max_examples=50)
def test_subpkg3::subpkg3class2_instantiation(instance):
    assert isinstance(instance, subpkg3::Subpkg3Class2)

@given(instance=toppkg::subpkg3::Subpkg3Class1_strategy)
@settings(max_examples=50)
def test_toppkg::subpkg3::subpkg3class1_instantiation(instance):
    assert isinstance(instance, toppkg::subpkg3::Subpkg3Class1)

@given(instance=subpkg3::Subpkg3Class1_strategy)
@settings(max_examples=50)
def test_subpkg3::subpkg3class1_instantiation(instance):
    assert isinstance(instance, subpkg3::Subpkg3Class1)

@given(instance=toppkg::subpkg2::Subpkg2Class2_strategy)
@settings(max_examples=50)
def test_toppkg::subpkg2::subpkg2class2_instantiation(instance):
    assert isinstance(instance, toppkg::subpkg2::Subpkg2Class2)

@given(instance=Subpkg2Class2_strategy)
@settings(max_examples=50)
def test_subpkg2class2_instantiation(instance):
    assert isinstance(instance, Subpkg2Class2)

@given(instance=toppkg::subpkg2::Subpkg2Class1_strategy)
@settings(max_examples=50)
def test_toppkg::subpkg2::subpkg2class1_instantiation(instance):
    assert isinstance(instance, toppkg::subpkg2::Subpkg2Class1)

@given(instance=toppkg::subpkg1::Subpkg1Class2_strategy)
@settings(max_examples=50)
def test_toppkg::subpkg1::subpkg1class2_instantiation(instance):
    assert isinstance(instance, toppkg::subpkg1::Subpkg1Class2)

@given(instance=Subpkg1Class2_strategy)
@settings(max_examples=50)
def test_subpkg1class2_instantiation(instance):
    assert isinstance(instance, Subpkg1Class2)

@given(instance=toppkg::subpkg1::Subpkg1Class1_strategy)
@settings(max_examples=50)
def test_toppkg::subpkg1::subpkg1class1_instantiation(instance):
    assert isinstance(instance, toppkg::subpkg1::Subpkg1Class1)

@given(instance=toppkg::TopClass1_strategy)
@settings(max_examples=50)
def test_toppkg::topclass1_instantiation(instance):
    assert isinstance(instance, toppkg::TopClass1)

@given(instance=Subpkg2Class1_strategy)
@settings(max_examples=50)
def test_subpkg2class1_instantiation(instance):
    assert isinstance(instance, Subpkg2Class1)

@given(instance=Subpkg1Class1_strategy)
@settings(max_examples=50)
def test_subpkg1class1_instantiation(instance):
    assert isinstance(instance, Subpkg1Class1)

@given(instance=toppkg::TopClass2_strategy)
@settings(max_examples=50)
def test_toppkg::topclass2_instantiation(instance):
    assert isinstance(instance, toppkg::TopClass2)

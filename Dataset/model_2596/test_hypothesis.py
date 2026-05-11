import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ClassB,
    root::subpackage::SubA,
    root::subpackage::SuperB,
    SuperB,
    root::subpackage::ClassB,
    root::ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classb_is_not_abstract():
    assert not inspect.isabstract(ClassB)


def test_classb_constructor_exists():
    assert callable(ClassB.__init__)


def test_classb_constructor_args():
    sig = inspect.signature(ClassB.__init__)
    params = list(sig.parameters.keys())



def test_root::subpackage::suba_is_not_abstract():
    assert not inspect.isabstract(root::subpackage::SubA)


def test_root::subpackage::suba_constructor_exists():
    assert callable(root::subpackage::SubA.__init__)


def test_root::subpackage::suba_constructor_args():
    sig = inspect.signature(root::subpackage::SubA.__init__)
    params = list(sig.parameters.keys())



def test_root::subpackage::superb_is_not_abstract():
    assert not inspect.isabstract(root::subpackage::SuperB)


def test_root::subpackage::superb_constructor_exists():
    assert callable(root::subpackage::SuperB.__init__)


def test_root::subpackage::superb_constructor_args():
    sig = inspect.signature(root::subpackage::SuperB.__init__)
    params = list(sig.parameters.keys())



def test_superb_is_not_abstract():
    assert not inspect.isabstract(SuperB)


def test_superb_constructor_exists():
    assert callable(SuperB.__init__)


def test_superb_constructor_args():
    sig = inspect.signature(SuperB.__init__)
    params = list(sig.parameters.keys())



def test_root::subpackage::classb_is_not_abstract():
    assert not inspect.isabstract(root::subpackage::ClassB)


def test_root::subpackage::classb_constructor_exists():
    assert callable(root::subpackage::ClassB.__init__)


def test_root::subpackage::classb_constructor_args():
    sig = inspect.signature(root::subpackage::ClassB.__init__)
    params = list(sig.parameters.keys())



def test_root::classa_is_not_abstract():
    assert not inspect.isabstract(root::ClassA)


def test_root::classa_constructor_exists():
    assert callable(root::ClassA.__init__)


def test_root::classa_constructor_args():
    sig = inspect.signature(root::ClassA.__init__)
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
ClassB_strategy = st.builds(
    ClassB,
)
root::subpackage::SubA_strategy = st.builds(
    root::subpackage::SubA,
)
root::subpackage::SuperB_strategy = st.builds(
    root::subpackage::SuperB,
)
SuperB_strategy = st.builds(
    SuperB,
)
root::subpackage::ClassB_strategy = st.builds(
    root::subpackage::ClassB,
)
root::ClassA_strategy = st.builds(
    root::ClassA,
)

@given(instance=ClassB_strategy)
@settings(max_examples=50)
def test_classb_instantiation(instance):
    assert isinstance(instance, ClassB)

@given(instance=root::subpackage::SubA_strategy)
@settings(max_examples=50)
def test_root::subpackage::suba_instantiation(instance):
    assert isinstance(instance, root::subpackage::SubA)

@given(instance=root::subpackage::SuperB_strategy)
@settings(max_examples=50)
def test_root::subpackage::superb_instantiation(instance):
    assert isinstance(instance, root::subpackage::SuperB)

@given(instance=SuperB_strategy)
@settings(max_examples=50)
def test_superb_instantiation(instance):
    assert isinstance(instance, SuperB)

@given(instance=root::subpackage::ClassB_strategy)
@settings(max_examples=50)
def test_root::subpackage::classb_instantiation(instance):
    assert isinstance(instance, root::subpackage::ClassB)

@given(instance=root::ClassA_strategy)
@settings(max_examples=50)
def test_root::classa_instantiation(instance):
    assert isinstance(instance, root::ClassA)

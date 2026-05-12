import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ClassB,
    root_subpackage_SubA,
    root_subpackage_SuperB,
    SuperB,
    root_subpackage_ClassB,
    root_ClassA,
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



def test_root_subpackage_suba_is_not_abstract():
    assert not inspect.isabstract(root_subpackage_SubA)


def test_root_subpackage_suba_constructor_exists():
    assert callable(root_subpackage_SubA.__init__)


def test_root_subpackage_suba_constructor_args():
    sig = inspect.signature(root_subpackage_SubA.__init__)
    params = list(sig.parameters.keys())



def test_root_subpackage_superb_is_not_abstract():
    assert not inspect.isabstract(root_subpackage_SuperB)


def test_root_subpackage_superb_constructor_exists():
    assert callable(root_subpackage_SuperB.__init__)


def test_root_subpackage_superb_constructor_args():
    sig = inspect.signature(root_subpackage_SuperB.__init__)
    params = list(sig.parameters.keys())



def test_superb_is_not_abstract():
    assert not inspect.isabstract(SuperB)


def test_superb_constructor_exists():
    assert callable(SuperB.__init__)


def test_superb_constructor_args():
    sig = inspect.signature(SuperB.__init__)
    params = list(sig.parameters.keys())



def test_root_subpackage_classb_is_not_abstract():
    assert not inspect.isabstract(root_subpackage_ClassB)


def test_root_subpackage_classb_constructor_exists():
    assert callable(root_subpackage_ClassB.__init__)


def test_root_subpackage_classb_constructor_args():
    sig = inspect.signature(root_subpackage_ClassB.__init__)
    params = list(sig.parameters.keys())



def test_root_classa_is_not_abstract():
    assert not inspect.isabstract(root_ClassA)


def test_root_classa_constructor_exists():
    assert callable(root_ClassA.__init__)


def test_root_classa_constructor_args():
    sig = inspect.signature(root_ClassA.__init__)
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
root_subpackage_SubA_strategy = st.builds(
    root_subpackage_SubA,
)
root_subpackage_SuperB_strategy = st.builds(
    root_subpackage_SuperB,
)
SuperB_strategy = st.builds(
    SuperB,
)
root_subpackage_ClassB_strategy = st.builds(
    root_subpackage_ClassB,
)
root_ClassA_strategy = st.builds(
    root_ClassA,
)

@given(instance=ClassB_strategy)
@settings(max_examples=50)
def test_classb_instantiation(instance):
    assert isinstance(instance, ClassB)

@given(instance=root_subpackage_SubA_strategy)
@settings(max_examples=50)
def test_root_subpackage_suba_instantiation(instance):
    assert isinstance(instance, root_subpackage_SubA)

@given(instance=root_subpackage_SuperB_strategy)
@settings(max_examples=50)
def test_root_subpackage_superb_instantiation(instance):
    assert isinstance(instance, root_subpackage_SuperB)

@given(instance=SuperB_strategy)
@settings(max_examples=50)
def test_superb_instantiation(instance):
    assert isinstance(instance, SuperB)

@given(instance=root_subpackage_ClassB_strategy)
@settings(max_examples=50)
def test_root_subpackage_classb_instantiation(instance):
    assert isinstance(instance, root_subpackage_ClassB)

@given(instance=root_ClassA_strategy)
@settings(max_examples=50)
def test_root_classa_instantiation(instance):
    assert isinstance(instance, root_ClassA)

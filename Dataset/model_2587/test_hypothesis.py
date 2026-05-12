import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Subclass1,
    inheritance_Sub1Subclass,
    Superclass,
    inheritance_Subclass2,
    inheritance_Subclass1,
    inheritance_Superclass,
    Subclass2,
    inheritance_Sub2Subclass,
    inheritance_Subclass3,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_subclass1_is_not_abstract():
    assert not inspect.isabstract(Subclass1)


def test_subclass1_constructor_exists():
    assert callable(Subclass1.__init__)


def test_subclass1_constructor_args():
    sig = inspect.signature(Subclass1.__init__)
    params = list(sig.parameters.keys())



def test_inheritance_sub1subclass_is_not_abstract():
    assert not inspect.isabstract(inheritance_Sub1Subclass)


def test_inheritance_sub1subclass_constructor_exists():
    assert callable(inheritance_Sub1Subclass.__init__)


def test_inheritance_sub1subclass_constructor_args():
    sig = inspect.signature(inheritance_Sub1Subclass.__init__)
    params = list(sig.parameters.keys())



def test_superclass_is_not_abstract():
    assert not inspect.isabstract(Superclass)


def test_superclass_constructor_exists():
    assert callable(Superclass.__init__)


def test_superclass_constructor_args():
    sig = inspect.signature(Superclass.__init__)
    params = list(sig.parameters.keys())



def test_inheritance_subclass2_is_not_abstract():
    assert not inspect.isabstract(inheritance_Subclass2)


def test_inheritance_subclass2_constructor_exists():
    assert callable(inheritance_Subclass2.__init__)


def test_inheritance_subclass2_constructor_args():
    sig = inspect.signature(inheritance_Subclass2.__init__)
    params = list(sig.parameters.keys())



def test_inheritance_subclass1_is_not_abstract():
    assert not inspect.isabstract(inheritance_Subclass1)


def test_inheritance_subclass1_constructor_exists():
    assert callable(inheritance_Subclass1.__init__)


def test_inheritance_subclass1_constructor_args():
    sig = inspect.signature(inheritance_Subclass1.__init__)
    params = list(sig.parameters.keys())



def test_inheritance_superclass_is_not_abstract():
    assert not inspect.isabstract(inheritance_Superclass)


def test_inheritance_superclass_constructor_exists():
    assert callable(inheritance_Superclass.__init__)


def test_inheritance_superclass_constructor_args():
    sig = inspect.signature(inheritance_Superclass.__init__)
    params = list(sig.parameters.keys())



def test_subclass2_is_not_abstract():
    assert not inspect.isabstract(Subclass2)


def test_subclass2_constructor_exists():
    assert callable(Subclass2.__init__)


def test_subclass2_constructor_args():
    sig = inspect.signature(Subclass2.__init__)
    params = list(sig.parameters.keys())



def test_inheritance_sub2subclass_is_not_abstract():
    assert not inspect.isabstract(inheritance_Sub2Subclass)


def test_inheritance_sub2subclass_constructor_exists():
    assert callable(inheritance_Sub2Subclass.__init__)


def test_inheritance_sub2subclass_constructor_args():
    sig = inspect.signature(inheritance_Sub2Subclass.__init__)
    params = list(sig.parameters.keys())



def test_inheritance_subclass3_is_not_abstract():
    assert not inspect.isabstract(inheritance_Subclass3)


def test_inheritance_subclass3_constructor_exists():
    assert callable(inheritance_Subclass3.__init__)


def test_inheritance_subclass3_constructor_args():
    sig = inspect.signature(inheritance_Subclass3.__init__)
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
Subclass1_strategy = st.builds(
    Subclass1,
)
inheritance_Sub1Subclass_strategy = st.builds(
    inheritance_Sub1Subclass,
)
Superclass_strategy = st.builds(
    Superclass,
)
inheritance_Subclass2_strategy = st.builds(
    inheritance_Subclass2,
)
inheritance_Subclass1_strategy = st.builds(
    inheritance_Subclass1,
)
inheritance_Superclass_strategy = st.builds(
    inheritance_Superclass,
)
Subclass2_strategy = st.builds(
    Subclass2,
)
inheritance_Sub2Subclass_strategy = st.builds(
    inheritance_Sub2Subclass,
)
inheritance_Subclass3_strategy = st.builds(
    inheritance_Subclass3,
)

@given(instance=Subclass1_strategy)
@settings(max_examples=50)
def test_subclass1_instantiation(instance):
    assert isinstance(instance, Subclass1)

@given(instance=inheritance_Sub1Subclass_strategy)
@settings(max_examples=50)
def test_inheritance_sub1subclass_instantiation(instance):
    assert isinstance(instance, inheritance_Sub1Subclass)

@given(instance=Superclass_strategy)
@settings(max_examples=50)
def test_superclass_instantiation(instance):
    assert isinstance(instance, Superclass)

@given(instance=inheritance_Subclass2_strategy)
@settings(max_examples=50)
def test_inheritance_subclass2_instantiation(instance):
    assert isinstance(instance, inheritance_Subclass2)

@given(instance=inheritance_Subclass1_strategy)
@settings(max_examples=50)
def test_inheritance_subclass1_instantiation(instance):
    assert isinstance(instance, inheritance_Subclass1)

@given(instance=inheritance_Superclass_strategy)
@settings(max_examples=50)
def test_inheritance_superclass_instantiation(instance):
    assert isinstance(instance, inheritance_Superclass)

@given(instance=Subclass2_strategy)
@settings(max_examples=50)
def test_subclass2_instantiation(instance):
    assert isinstance(instance, Subclass2)

@given(instance=inheritance_Sub2Subclass_strategy)
@settings(max_examples=50)
def test_inheritance_sub2subclass_instantiation(instance):
    assert isinstance(instance, inheritance_Sub2Subclass)

@given(instance=inheritance_Subclass3_strategy)
@settings(max_examples=50)
def test_inheritance_subclass3_instantiation(instance):
    assert isinstance(instance, inheritance_Subclass3)

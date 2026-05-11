import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Subclass1,
    inheritance::Sub1Subclass,
    Superclass,
    inheritance::Subclass2,
    inheritance::Subclass1,
    inheritance::Superclass,
    Subclass2,
    inheritance::Sub2Subclass,
    inheritance::Subclass3,
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



def test_inheritance::sub1subclass_is_not_abstract():
    assert not inspect.isabstract(inheritance::Sub1Subclass)


def test_inheritance::sub1subclass_constructor_exists():
    assert callable(inheritance::Sub1Subclass.__init__)


def test_inheritance::sub1subclass_constructor_args():
    sig = inspect.signature(inheritance::Sub1Subclass.__init__)
    params = list(sig.parameters.keys())



def test_superclass_is_not_abstract():
    assert not inspect.isabstract(Superclass)


def test_superclass_constructor_exists():
    assert callable(Superclass.__init__)


def test_superclass_constructor_args():
    sig = inspect.signature(Superclass.__init__)
    params = list(sig.parameters.keys())



def test_inheritance::subclass2_is_not_abstract():
    assert not inspect.isabstract(inheritance::Subclass2)


def test_inheritance::subclass2_constructor_exists():
    assert callable(inheritance::Subclass2.__init__)


def test_inheritance::subclass2_constructor_args():
    sig = inspect.signature(inheritance::Subclass2.__init__)
    params = list(sig.parameters.keys())



def test_inheritance::subclass1_is_not_abstract():
    assert not inspect.isabstract(inheritance::Subclass1)


def test_inheritance::subclass1_constructor_exists():
    assert callable(inheritance::Subclass1.__init__)


def test_inheritance::subclass1_constructor_args():
    sig = inspect.signature(inheritance::Subclass1.__init__)
    params = list(sig.parameters.keys())



def test_inheritance::superclass_is_not_abstract():
    assert not inspect.isabstract(inheritance::Superclass)


def test_inheritance::superclass_constructor_exists():
    assert callable(inheritance::Superclass.__init__)


def test_inheritance::superclass_constructor_args():
    sig = inspect.signature(inheritance::Superclass.__init__)
    params = list(sig.parameters.keys())



def test_subclass2_is_not_abstract():
    assert not inspect.isabstract(Subclass2)


def test_subclass2_constructor_exists():
    assert callable(Subclass2.__init__)


def test_subclass2_constructor_args():
    sig = inspect.signature(Subclass2.__init__)
    params = list(sig.parameters.keys())



def test_inheritance::sub2subclass_is_not_abstract():
    assert not inspect.isabstract(inheritance::Sub2Subclass)


def test_inheritance::sub2subclass_constructor_exists():
    assert callable(inheritance::Sub2Subclass.__init__)


def test_inheritance::sub2subclass_constructor_args():
    sig = inspect.signature(inheritance::Sub2Subclass.__init__)
    params = list(sig.parameters.keys())



def test_inheritance::subclass3_is_not_abstract():
    assert not inspect.isabstract(inheritance::Subclass3)


def test_inheritance::subclass3_constructor_exists():
    assert callable(inheritance::Subclass3.__init__)


def test_inheritance::subclass3_constructor_args():
    sig = inspect.signature(inheritance::Subclass3.__init__)
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
inheritance::Sub1Subclass_strategy = st.builds(
    inheritance::Sub1Subclass,
)
Superclass_strategy = st.builds(
    Superclass,
)
inheritance::Subclass2_strategy = st.builds(
    inheritance::Subclass2,
)
inheritance::Subclass1_strategy = st.builds(
    inheritance::Subclass1,
)
inheritance::Superclass_strategy = st.builds(
    inheritance::Superclass,
)
Subclass2_strategy = st.builds(
    Subclass2,
)
inheritance::Sub2Subclass_strategy = st.builds(
    inheritance::Sub2Subclass,
)
inheritance::Subclass3_strategy = st.builds(
    inheritance::Subclass3,
)

@given(instance=Subclass1_strategy)
@settings(max_examples=50)
def test_subclass1_instantiation(instance):
    assert isinstance(instance, Subclass1)

@given(instance=inheritance::Sub1Subclass_strategy)
@settings(max_examples=50)
def test_inheritance::sub1subclass_instantiation(instance):
    assert isinstance(instance, inheritance::Sub1Subclass)

@given(instance=Superclass_strategy)
@settings(max_examples=50)
def test_superclass_instantiation(instance):
    assert isinstance(instance, Superclass)

@given(instance=inheritance::Subclass2_strategy)
@settings(max_examples=50)
def test_inheritance::subclass2_instantiation(instance):
    assert isinstance(instance, inheritance::Subclass2)

@given(instance=inheritance::Subclass1_strategy)
@settings(max_examples=50)
def test_inheritance::subclass1_instantiation(instance):
    assert isinstance(instance, inheritance::Subclass1)

@given(instance=inheritance::Superclass_strategy)
@settings(max_examples=50)
def test_inheritance::superclass_instantiation(instance):
    assert isinstance(instance, inheritance::Superclass)

@given(instance=Subclass2_strategy)
@settings(max_examples=50)
def test_subclass2_instantiation(instance):
    assert isinstance(instance, Subclass2)

@given(instance=inheritance::Sub2Subclass_strategy)
@settings(max_examples=50)
def test_inheritance::sub2subclass_instantiation(instance):
    assert isinstance(instance, inheritance::Sub2Subclass)

@given(instance=inheritance::Subclass3_strategy)
@settings(max_examples=50)
def test_inheritance::subclass3_instantiation(instance):
    assert isinstance(instance, inheritance::Subclass3)

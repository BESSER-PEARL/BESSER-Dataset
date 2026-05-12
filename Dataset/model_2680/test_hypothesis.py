import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    formalmetamodel_AA,
    formalmetamodel_C,
    formalmetamodel_B,
    AA,
    formalmetamodel_A,
    formalmetamodel_FormalModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_formalmetamodel_aa_is_not_abstract():
    assert not inspect.isabstract(formalmetamodel_AA)


def test_formalmetamodel_aa_constructor_exists():
    assert callable(formalmetamodel_AA.__init__)


def test_formalmetamodel_aa_constructor_args():
    sig = inspect.signature(formalmetamodel_AA.__init__)
    params = list(sig.parameters.keys())



def test_formalmetamodel_c_is_not_abstract():
    assert not inspect.isabstract(formalmetamodel_C)


def test_formalmetamodel_c_constructor_exists():
    assert callable(formalmetamodel_C.__init__)


def test_formalmetamodel_c_constructor_args():
    sig = inspect.signature(formalmetamodel_C.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_formalmetamodel_c_has_name():
    assert hasattr(formalmetamodel_C, "name")
    descriptor = None
    for klass in formalmetamodel_C.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_formalmetamodel_b_is_not_abstract():
    assert not inspect.isabstract(formalmetamodel_B)


def test_formalmetamodel_b_constructor_exists():
    assert callable(formalmetamodel_B.__init__)


def test_formalmetamodel_b_constructor_args():
    sig = inspect.signature(formalmetamodel_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_formalmetamodel_b_has_name():
    assert hasattr(formalmetamodel_B, "name")
    descriptor = None
    for klass in formalmetamodel_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_aa_is_not_abstract():
    assert not inspect.isabstract(AA)


def test_aa_constructor_exists():
    assert callable(AA.__init__)


def test_aa_constructor_args():
    sig = inspect.signature(AA.__init__)
    params = list(sig.parameters.keys())



def test_formalmetamodel_a_is_not_abstract():
    assert not inspect.isabstract(formalmetamodel_A)


def test_formalmetamodel_a_constructor_exists():
    assert callable(formalmetamodel_A.__init__)


def test_formalmetamodel_a_constructor_args():
    sig = inspect.signature(formalmetamodel_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_formalmetamodel_a_has_name():
    assert hasattr(formalmetamodel_A, "name")
    descriptor = None
    for klass in formalmetamodel_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_formalmetamodel_formalmodel_is_not_abstract():
    assert not inspect.isabstract(formalmetamodel_FormalModel)


def test_formalmetamodel_formalmodel_constructor_exists():
    assert callable(formalmetamodel_FormalModel.__init__)


def test_formalmetamodel_formalmodel_constructor_args():
    sig = inspect.signature(formalmetamodel_FormalModel.__init__)
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
formalmetamodel_AA_strategy = st.builds(
    formalmetamodel_AA,
)
formalmetamodel_C_strategy = st.builds(
    formalmetamodel_C,
    name=
        safe_text
)
formalmetamodel_B_strategy = st.builds(
    formalmetamodel_B,
    name=
        safe_text
)
AA_strategy = st.builds(
    AA,
)
formalmetamodel_A_strategy = st.builds(
    formalmetamodel_A,
    name=
        safe_text
)
formalmetamodel_FormalModel_strategy = st.builds(
    formalmetamodel_FormalModel,
)

@given(instance=formalmetamodel_AA_strategy)
@settings(max_examples=50)
def test_formalmetamodel_aa_instantiation(instance):
    assert isinstance(instance, formalmetamodel_AA)

@given(instance=formalmetamodel_C_strategy)
@settings(max_examples=50)
def test_formalmetamodel_c_instantiation(instance):
    assert isinstance(instance, formalmetamodel_C)



@given(instance=formalmetamodel_C_strategy)
def test_formalmetamodel_c_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=formalmetamodel_B_strategy)
@settings(max_examples=50)
def test_formalmetamodel_b_instantiation(instance):
    assert isinstance(instance, formalmetamodel_B)



@given(instance=formalmetamodel_B_strategy)
def test_formalmetamodel_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AA_strategy)
@settings(max_examples=50)
def test_aa_instantiation(instance):
    assert isinstance(instance, AA)

@given(instance=formalmetamodel_A_strategy)
@settings(max_examples=50)
def test_formalmetamodel_a_instantiation(instance):
    assert isinstance(instance, formalmetamodel_A)



@given(instance=formalmetamodel_A_strategy)
def test_formalmetamodel_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=formalmetamodel_FormalModel_strategy)
@settings(max_examples=50)
def test_formalmetamodel_formalmodel_instantiation(instance):
    assert isinstance(instance, formalmetamodel_FormalModel)

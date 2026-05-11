import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    formalmetamodel::AA,
    formalmetamodel::C,
    formalmetamodel::FormalModel,
    formalmetamodel::B,
    AA,
    formalmetamodel::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_formalmetamodel::aa_is_not_abstract():
    assert not inspect.isabstract(formalmetamodel::AA)


def test_formalmetamodel::aa_constructor_exists():
    assert callable(formalmetamodel::AA.__init__)


def test_formalmetamodel::aa_constructor_args():
    sig = inspect.signature(formalmetamodel::AA.__init__)
    params = list(sig.parameters.keys())



def test_formalmetamodel::c_is_not_abstract():
    assert not inspect.isabstract(formalmetamodel::C)


def test_formalmetamodel::c_constructor_exists():
    assert callable(formalmetamodel::C.__init__)


def test_formalmetamodel::c_constructor_args():
    sig = inspect.signature(formalmetamodel::C.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_formalmetamodel::c_has_name():
    assert hasattr(formalmetamodel::C, "name")
    descriptor = None
    for klass in formalmetamodel::C.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_formalmetamodel::formalmodel_is_not_abstract():
    assert not inspect.isabstract(formalmetamodel::FormalModel)


def test_formalmetamodel::formalmodel_constructor_exists():
    assert callable(formalmetamodel::FormalModel.__init__)


def test_formalmetamodel::formalmodel_constructor_args():
    sig = inspect.signature(formalmetamodel::FormalModel.__init__)
    params = list(sig.parameters.keys())



def test_formalmetamodel::b_is_not_abstract():
    assert not inspect.isabstract(formalmetamodel::B)


def test_formalmetamodel::b_constructor_exists():
    assert callable(formalmetamodel::B.__init__)


def test_formalmetamodel::b_constructor_args():
    sig = inspect.signature(formalmetamodel::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_formalmetamodel::b_has_name():
    assert hasattr(formalmetamodel::B, "name")
    descriptor = None
    for klass in formalmetamodel::B.__mro__:
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



def test_formalmetamodel::a_is_not_abstract():
    assert not inspect.isabstract(formalmetamodel::A)


def test_formalmetamodel::a_constructor_exists():
    assert callable(formalmetamodel::A.__init__)


def test_formalmetamodel::a_constructor_args():
    sig = inspect.signature(formalmetamodel::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_formalmetamodel::a_has_name():
    assert hasattr(formalmetamodel::A, "name")
    descriptor = None
    for klass in formalmetamodel::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
formalmetamodel::AA_strategy = st.builds(
    formalmetamodel::AA,
)
formalmetamodel::C_strategy = st.builds(
    formalmetamodel::C,
    name=
        safe_text
)
formalmetamodel::FormalModel_strategy = st.builds(
    formalmetamodel::FormalModel,
)
formalmetamodel::B_strategy = st.builds(
    formalmetamodel::B,
    name=
        safe_text
)
AA_strategy = st.builds(
    AA,
)
formalmetamodel::A_strategy = st.builds(
    formalmetamodel::A,
    name=
        safe_text
)

@given(instance=formalmetamodel::AA_strategy)
@settings(max_examples=50)
def test_formalmetamodel::aa_instantiation(instance):
    assert isinstance(instance, formalmetamodel::AA)

@given(instance=formalmetamodel::C_strategy)
@settings(max_examples=50)
def test_formalmetamodel::c_instantiation(instance):
    assert isinstance(instance, formalmetamodel::C)

@given(instance=formalmetamodel::C_strategy)
def test_formalmetamodel::c_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=formalmetamodel::C_strategy)
def test_formalmetamodel::c_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=formalmetamodel::FormalModel_strategy)
@settings(max_examples=50)
def test_formalmetamodel::formalmodel_instantiation(instance):
    assert isinstance(instance, formalmetamodel::FormalModel)

@given(instance=formalmetamodel::B_strategy)
@settings(max_examples=50)
def test_formalmetamodel::b_instantiation(instance):
    assert isinstance(instance, formalmetamodel::B)

@given(instance=formalmetamodel::B_strategy)
def test_formalmetamodel::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=formalmetamodel::B_strategy)
def test_formalmetamodel::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AA_strategy)
@settings(max_examples=50)
def test_aa_instantiation(instance):
    assert isinstance(instance, AA)

@given(instance=formalmetamodel::A_strategy)
@settings(max_examples=50)
def test_formalmetamodel::a_instantiation(instance):
    assert isinstance(instance, formalmetamodel::A)

@given(instance=formalmetamodel::A_strategy)
def test_formalmetamodel::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=formalmetamodel::A_strategy)
def test_formalmetamodel::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

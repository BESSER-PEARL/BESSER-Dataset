import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Eclass5,
    ecoreTest::EClass3,
    ecoreTest::EClass2,
    ecoreTest::Eclass1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eclass5_is_not_abstract():
    assert not inspect.isabstract(Eclass5)


def test_eclass5_constructor_exists():
    assert callable(Eclass5.__init__)


def test_eclass5_constructor_args():
    sig = inspect.signature(Eclass5.__init__)
    params = list(sig.parameters.keys())



def test_ecoretest::eclass3_is_not_abstract():
    assert not inspect.isabstract(ecoreTest::EClass3)


def test_ecoretest::eclass3_constructor_exists():
    assert callable(ecoreTest::EClass3.__init__)


def test_ecoretest::eclass3_constructor_args():
    sig = inspect.signature(ecoreTest::EClass3.__init__)
    params = list(sig.parameters.keys())



def test_ecoretest::eclass2_is_not_abstract():
    assert not inspect.isabstract(ecoreTest::EClass2)


def test_ecoretest::eclass2_constructor_exists():
    assert callable(ecoreTest::EClass2.__init__)


def test_ecoretest::eclass2_constructor_args():
    sig = inspect.signature(ecoreTest::EClass2.__init__)
    params = list(sig.parameters.keys())
    assert "eAttribute4" in params, "Missing parameter 'eAttribute4'"
    assert "eAttribute3" in params, "Missing parameter 'eAttribute3'"

def test_ecoretest::eclass2_has_eAttribute4():
    assert hasattr(ecoreTest::EClass2, "eAttribute4")
    descriptor = None
    for klass in ecoreTest::EClass2.__mro__:
        if "eAttribute4" in klass.__dict__:
            descriptor = klass.__dict__["eAttribute4"]
            break
    assert isinstance(descriptor, property)

def test_ecoretest::eclass2_has_eAttribute3():
    assert hasattr(ecoreTest::EClass2, "eAttribute3")
    descriptor = None
    for klass in ecoreTest::EClass2.__mro__:
        if "eAttribute3" in klass.__dict__:
            descriptor = klass.__dict__["eAttribute3"]
            break
    assert isinstance(descriptor, property)



def test_ecoretest::eclass1_is_not_abstract():
    assert not inspect.isabstract(ecoreTest::Eclass1)


def test_ecoretest::eclass1_constructor_exists():
    assert callable(ecoreTest::Eclass1.__init__)


def test_ecoretest::eclass1_constructor_args():
    sig = inspect.signature(ecoreTest::Eclass1.__init__)
    params = list(sig.parameters.keys())
    assert "eAttribute1" in params, "Missing parameter 'eAttribute1'"
    assert "eAttribute2" in params, "Missing parameter 'eAttribute2'"

def test_ecoretest::eclass1_has_eAttribute1():
    assert hasattr(ecoreTest::Eclass1, "eAttribute1")
    descriptor = None
    for klass in ecoreTest::Eclass1.__mro__:
        if "eAttribute1" in klass.__dict__:
            descriptor = klass.__dict__["eAttribute1"]
            break
    assert isinstance(descriptor, property)

def test_ecoretest::eclass1_has_eAttribute2():
    assert hasattr(ecoreTest::Eclass1, "eAttribute2")
    descriptor = None
    for klass in ecoreTest::Eclass1.__mro__:
        if "eAttribute2" in klass.__dict__:
            descriptor = klass.__dict__["eAttribute2"]
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
Eclass5_strategy = st.builds(
    Eclass5,
)
ecoreTest::EClass3_strategy = st.builds(
    ecoreTest::EClass3,
)
ecoreTest::EClass2_strategy = st.builds(
    ecoreTest::EClass2,
    eAttribute4=
        safe_text,
    eAttribute3=
        safe_text
)
ecoreTest::Eclass1_strategy = st.builds(
    ecoreTest::Eclass1,
    eAttribute1=
        safe_text,
    eAttribute2=
        safe_text
)

@given(instance=Eclass5_strategy)
@settings(max_examples=50)
def test_eclass5_instantiation(instance):
    assert isinstance(instance, Eclass5)

@given(instance=ecoreTest::EClass3_strategy)
@settings(max_examples=50)
def test_ecoretest::eclass3_instantiation(instance):
    assert isinstance(instance, ecoreTest::EClass3)

@given(instance=ecoreTest::EClass2_strategy)
@settings(max_examples=50)
def test_ecoretest::eclass2_instantiation(instance):
    assert isinstance(instance, ecoreTest::EClass2)

@given(instance=ecoreTest::EClass2_strategy)
def test_ecoretest::eclass2_eAttribute4_type(instance):
    assert isinstance(instance.eAttribute4, str)


@given(instance=ecoreTest::EClass2_strategy)
def test_ecoretest::eclass2_eAttribute4_setter(instance):
    original = instance.eAttribute4
    instance.eAttribute4 = original
    assert instance.eAttribute4 == original

@given(instance=ecoreTest::EClass2_strategy)
def test_ecoretest::eclass2_eAttribute3_type(instance):
    assert isinstance(instance.eAttribute3, str)


@given(instance=ecoreTest::EClass2_strategy)
def test_ecoretest::eclass2_eAttribute3_setter(instance):
    original = instance.eAttribute3
    instance.eAttribute3 = original
    assert instance.eAttribute3 == original

@given(instance=ecoreTest::Eclass1_strategy)
@settings(max_examples=50)
def test_ecoretest::eclass1_instantiation(instance):
    assert isinstance(instance, ecoreTest::Eclass1)

@given(instance=ecoreTest::Eclass1_strategy)
def test_ecoretest::eclass1_eAttribute1_type(instance):
    assert isinstance(instance.eAttribute1, str)


@given(instance=ecoreTest::Eclass1_strategy)
def test_ecoretest::eclass1_eAttribute1_setter(instance):
    original = instance.eAttribute1
    instance.eAttribute1 = original
    assert instance.eAttribute1 == original

@given(instance=ecoreTest::Eclass1_strategy)
def test_ecoretest::eclass1_eAttribute2_type(instance):
    assert isinstance(instance.eAttribute2, str)


@given(instance=ecoreTest::Eclass1_strategy)
def test_ecoretest::eclass1_eAttribute2_setter(instance):
    original = instance.eAttribute2
    instance.eAttribute2 = original
    assert instance.eAttribute2 == original

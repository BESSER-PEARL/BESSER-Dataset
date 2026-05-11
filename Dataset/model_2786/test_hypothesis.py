import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testModel::EObject,
    BClass,
    testModel::CClass,
    AClass,
    testModel::BClass,
    testModel::AClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmodel::eobject_is_not_abstract():
    assert not inspect.isabstract(testModel::EObject)


def test_testmodel::eobject_constructor_exists():
    assert callable(testModel::EObject.__init__)


def test_testmodel::eobject_constructor_args():
    sig = inspect.signature(testModel::EObject.__init__)
    params = list(sig.parameters.keys())



def test_bclass_is_not_abstract():
    assert not inspect.isabstract(BClass)


def test_bclass_constructor_exists():
    assert callable(BClass.__init__)


def test_bclass_constructor_args():
    sig = inspect.signature(BClass.__init__)
    params = list(sig.parameters.keys())



def test_testmodel::cclass_is_not_abstract():
    assert not inspect.isabstract(testModel::CClass)


def test_testmodel::cclass_constructor_exists():
    assert callable(testModel::CClass.__init__)


def test_testmodel::cclass_constructor_args():
    sig = inspect.signature(testModel::CClass.__init__)
    params = list(sig.parameters.keys())
    assert "CClassAttr2" in params, "Missing parameter 'CClassAttr2'"
    assert "CClassAttr1" in params, "Missing parameter 'CClassAttr1'"

def test_testmodel::cclass_has_CClassAttr2():
    assert hasattr(testModel::CClass, "CClassAttr2")
    descriptor = None
    for klass in testModel::CClass.__mro__:
        if "CClassAttr2" in klass.__dict__:
            descriptor = klass.__dict__["CClassAttr2"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::cclass_has_CClassAttr1():
    assert hasattr(testModel::CClass, "CClassAttr1")
    descriptor = None
    for klass in testModel::CClass.__mro__:
        if "CClassAttr1" in klass.__dict__:
            descriptor = klass.__dict__["CClassAttr1"]
            break
    assert isinstance(descriptor, property)



def test_aclass_is_not_abstract():
    assert not inspect.isabstract(AClass)


def test_aclass_constructor_exists():
    assert callable(AClass.__init__)


def test_aclass_constructor_args():
    sig = inspect.signature(AClass.__init__)
    params = list(sig.parameters.keys())



def test_testmodel::bclass_is_not_abstract():
    assert not inspect.isabstract(testModel::BClass)


def test_testmodel::bclass_constructor_exists():
    assert callable(testModel::BClass.__init__)


def test_testmodel::bclass_constructor_args():
    sig = inspect.signature(testModel::BClass.__init__)
    params = list(sig.parameters.keys())
    assert "BClassAttr1" in params, "Missing parameter 'BClassAttr1'"
    assert "BClassAttr2" in params, "Missing parameter 'BClassAttr2'"

def test_testmodel::bclass_has_BClassAttr1():
    assert hasattr(testModel::BClass, "BClassAttr1")
    descriptor = None
    for klass in testModel::BClass.__mro__:
        if "BClassAttr1" in klass.__dict__:
            descriptor = klass.__dict__["BClassAttr1"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::bclass_has_BClassAttr2():
    assert hasattr(testModel::BClass, "BClassAttr2")
    descriptor = None
    for klass in testModel::BClass.__mro__:
        if "BClassAttr2" in klass.__dict__:
            descriptor = klass.__dict__["BClassAttr2"]
            break
    assert isinstance(descriptor, property)



def test_testmodel::aclass_is_not_abstract():
    assert not inspect.isabstract(testModel::AClass)


def test_testmodel::aclass_constructor_exists():
    assert callable(testModel::AClass.__init__)


def test_testmodel::aclass_constructor_args():
    sig = inspect.signature(testModel::AClass.__init__)
    params = list(sig.parameters.keys())
    assert "AClassAttr2" in params, "Missing parameter 'AClassAttr2'"
    assert "AClassAttr1" in params, "Missing parameter 'AClassAttr1'"

def test_testmodel::aclass_has_AClassAttr2():
    assert hasattr(testModel::AClass, "AClassAttr2")
    descriptor = None
    for klass in testModel::AClass.__mro__:
        if "AClassAttr2" in klass.__dict__:
            descriptor = klass.__dict__["AClassAttr2"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::aclass_has_AClassAttr1():
    assert hasattr(testModel::AClass, "AClassAttr1")
    descriptor = None
    for klass in testModel::AClass.__mro__:
        if "AClassAttr1" in klass.__dict__:
            descriptor = klass.__dict__["AClassAttr1"]
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
testModel::EObject_strategy = st.builds(
    testModel::EObject,
)
BClass_strategy = st.builds(
    BClass,
)
testModel::CClass_strategy = st.builds(
    testModel::CClass,
    CClassAttr2=
        safe_text,
    CClassAttr1=
        st.booleans()
)
AClass_strategy = st.builds(
    AClass,
)
testModel::BClass_strategy = st.builds(
    testModel::BClass,
    BClassAttr1=
        st.booleans(),
    BClassAttr2=
        safe_text
)
testModel::AClass_strategy = st.builds(
    testModel::AClass,
    AClassAttr2=
        safe_text,
    AClassAttr1=
        st.booleans()
)

@given(instance=testModel::EObject_strategy)
@settings(max_examples=50)
def test_testmodel::eobject_instantiation(instance):
    assert isinstance(instance, testModel::EObject)

@given(instance=BClass_strategy)
@settings(max_examples=50)
def test_bclass_instantiation(instance):
    assert isinstance(instance, BClass)

@given(instance=testModel::CClass_strategy)
@settings(max_examples=50)
def test_testmodel::cclass_instantiation(instance):
    assert isinstance(instance, testModel::CClass)

@given(instance=testModel::CClass_strategy)
def test_testmodel::cclass_CClassAttr2_type(instance):
    assert isinstance(instance.CClassAttr2, str)


@given(instance=testModel::CClass_strategy)
def test_testmodel::cclass_CClassAttr2_setter(instance):
    original = instance.CClassAttr2
    instance.CClassAttr2 = original
    assert instance.CClassAttr2 == original

@given(instance=testModel::CClass_strategy)
def test_testmodel::cclass_CClassAttr1_type(instance):
    assert isinstance(instance.CClassAttr1, bool)


@given(instance=testModel::CClass_strategy)
def test_testmodel::cclass_CClassAttr1_setter(instance):
    original = instance.CClassAttr1
    instance.CClassAttr1 = original
    assert instance.CClassAttr1 == original

@given(instance=AClass_strategy)
@settings(max_examples=50)
def test_aclass_instantiation(instance):
    assert isinstance(instance, AClass)

@given(instance=testModel::BClass_strategy)
@settings(max_examples=50)
def test_testmodel::bclass_instantiation(instance):
    assert isinstance(instance, testModel::BClass)

@given(instance=testModel::BClass_strategy)
def test_testmodel::bclass_BClassAttr1_type(instance):
    assert isinstance(instance.BClassAttr1, bool)


@given(instance=testModel::BClass_strategy)
def test_testmodel::bclass_BClassAttr1_setter(instance):
    original = instance.BClassAttr1
    instance.BClassAttr1 = original
    assert instance.BClassAttr1 == original

@given(instance=testModel::BClass_strategy)
def test_testmodel::bclass_BClassAttr2_type(instance):
    assert isinstance(instance.BClassAttr2, str)


@given(instance=testModel::BClass_strategy)
def test_testmodel::bclass_BClassAttr2_setter(instance):
    original = instance.BClassAttr2
    instance.BClassAttr2 = original
    assert instance.BClassAttr2 == original

@given(instance=testModel::AClass_strategy)
@settings(max_examples=50)
def test_testmodel::aclass_instantiation(instance):
    assert isinstance(instance, testModel::AClass)

@given(instance=testModel::AClass_strategy)
def test_testmodel::aclass_AClassAttr2_type(instance):
    assert isinstance(instance.AClassAttr2, str)


@given(instance=testModel::AClass_strategy)
def test_testmodel::aclass_AClassAttr2_setter(instance):
    original = instance.AClassAttr2
    instance.AClassAttr2 = original
    assert instance.AClassAttr2 == original

@given(instance=testModel::AClass_strategy)
def test_testmodel::aclass_AClassAttr1_type(instance):
    assert isinstance(instance.AClassAttr1, bool)


@given(instance=testModel::AClass_strategy)
def test_testmodel::aclass_AClassAttr1_setter(instance):
    original = instance.AClassAttr1
    instance.AClassAttr1 = original
    assert instance.AClassAttr1 == original

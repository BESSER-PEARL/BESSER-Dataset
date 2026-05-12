import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testModel_EObject,
    BClass,
    testModel_CClass,
    AClass,
    testModel_BClass,
    testModel_AClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmodel_eobject_is_not_abstract():
    assert not inspect.isabstract(testModel_EObject)


def test_testmodel_eobject_constructor_exists():
    assert callable(testModel_EObject.__init__)


def test_testmodel_eobject_constructor_args():
    sig = inspect.signature(testModel_EObject.__init__)
    params = list(sig.parameters.keys())



def test_bclass_is_not_abstract():
    assert not inspect.isabstract(BClass)


def test_bclass_constructor_exists():
    assert callable(BClass.__init__)


def test_bclass_constructor_args():
    sig = inspect.signature(BClass.__init__)
    params = list(sig.parameters.keys())



def test_testmodel_cclass_is_not_abstract():
    assert not inspect.isabstract(testModel_CClass)


def test_testmodel_cclass_constructor_exists():
    assert callable(testModel_CClass.__init__)


def test_testmodel_cclass_constructor_args():
    sig = inspect.signature(testModel_CClass.__init__)
    params = list(sig.parameters.keys())
    assert "CClassAttr1" in params, "Missing parameter 'CClassAttr1'"
    assert "CClassAttr2" in params, "Missing parameter 'CClassAttr2'"

def test_testmodel_cclass_has_CClassAttr1():
    assert hasattr(testModel_CClass, "CClassAttr1")
    descriptor = None
    for klass in testModel_CClass.__mro__:
        if "CClassAttr1" in klass.__dict__:
            descriptor = klass.__dict__["CClassAttr1"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_cclass_has_CClassAttr2():
    assert hasattr(testModel_CClass, "CClassAttr2")
    descriptor = None
    for klass in testModel_CClass.__mro__:
        if "CClassAttr2" in klass.__dict__:
            descriptor = klass.__dict__["CClassAttr2"]
            break
    assert isinstance(descriptor, property)



def test_aclass_is_not_abstract():
    assert not inspect.isabstract(AClass)


def test_aclass_constructor_exists():
    assert callable(AClass.__init__)


def test_aclass_constructor_args():
    sig = inspect.signature(AClass.__init__)
    params = list(sig.parameters.keys())



def test_testmodel_bclass_is_not_abstract():
    assert not inspect.isabstract(testModel_BClass)


def test_testmodel_bclass_constructor_exists():
    assert callable(testModel_BClass.__init__)


def test_testmodel_bclass_constructor_args():
    sig = inspect.signature(testModel_BClass.__init__)
    params = list(sig.parameters.keys())
    assert "BClassAttr1" in params, "Missing parameter 'BClassAttr1'"
    assert "BClassAttr2" in params, "Missing parameter 'BClassAttr2'"

def test_testmodel_bclass_has_BClassAttr1():
    assert hasattr(testModel_BClass, "BClassAttr1")
    descriptor = None
    for klass in testModel_BClass.__mro__:
        if "BClassAttr1" in klass.__dict__:
            descriptor = klass.__dict__["BClassAttr1"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_bclass_has_BClassAttr2():
    assert hasattr(testModel_BClass, "BClassAttr2")
    descriptor = None
    for klass in testModel_BClass.__mro__:
        if "BClassAttr2" in klass.__dict__:
            descriptor = klass.__dict__["BClassAttr2"]
            break
    assert isinstance(descriptor, property)



def test_testmodel_aclass_is_not_abstract():
    assert not inspect.isabstract(testModel_AClass)


def test_testmodel_aclass_constructor_exists():
    assert callable(testModel_AClass.__init__)


def test_testmodel_aclass_constructor_args():
    sig = inspect.signature(testModel_AClass.__init__)
    params = list(sig.parameters.keys())
    assert "AClassAttr2" in params, "Missing parameter 'AClassAttr2'"
    assert "AClassAttr1" in params, "Missing parameter 'AClassAttr1'"

def test_testmodel_aclass_has_AClassAttr2():
    assert hasattr(testModel_AClass, "AClassAttr2")
    descriptor = None
    for klass in testModel_AClass.__mro__:
        if "AClassAttr2" in klass.__dict__:
            descriptor = klass.__dict__["AClassAttr2"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_aclass_has_AClassAttr1():
    assert hasattr(testModel_AClass, "AClassAttr1")
    descriptor = None
    for klass in testModel_AClass.__mro__:
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
testModel_EObject_strategy = st.builds(
    testModel_EObject,
)
BClass_strategy = st.builds(
    BClass,
)
testModel_CClass_strategy = st.builds(
    testModel_CClass,
    CClassAttr1=
        st.booleans(),
    CClassAttr2=
        safe_text
)
AClass_strategy = st.builds(
    AClass,
)
testModel_BClass_strategy = st.builds(
    testModel_BClass,
    BClassAttr1=
        st.booleans(),
    BClassAttr2=
        safe_text
)
testModel_AClass_strategy = st.builds(
    testModel_AClass,
    AClassAttr2=
        safe_text,
    AClassAttr1=
        st.booleans()
)

@given(instance=testModel_EObject_strategy)
@settings(max_examples=50)
def test_testmodel_eobject_instantiation(instance):
    assert isinstance(instance, testModel_EObject)

@given(instance=BClass_strategy)
@settings(max_examples=50)
def test_bclass_instantiation(instance):
    assert isinstance(instance, BClass)

@given(instance=testModel_CClass_strategy)
@settings(max_examples=50)
def test_testmodel_cclass_instantiation(instance):
    assert isinstance(instance, testModel_CClass)



@given(instance=testModel_CClass_strategy)
def test_testmodel_cclass_CClassAttr1_setter(instance):
    original = instance.CClassAttr1
    instance.CClassAttr1 = original
    assert instance.CClassAttr1 == original



@given(instance=testModel_CClass_strategy)
def test_testmodel_cclass_CClassAttr2_setter(instance):
    original = instance.CClassAttr2
    instance.CClassAttr2 = original
    assert instance.CClassAttr2 == original

@given(instance=AClass_strategy)
@settings(max_examples=50)
def test_aclass_instantiation(instance):
    assert isinstance(instance, AClass)

@given(instance=testModel_BClass_strategy)
@settings(max_examples=50)
def test_testmodel_bclass_instantiation(instance):
    assert isinstance(instance, testModel_BClass)



@given(instance=testModel_BClass_strategy)
def test_testmodel_bclass_BClassAttr1_setter(instance):
    original = instance.BClassAttr1
    instance.BClassAttr1 = original
    assert instance.BClassAttr1 == original



@given(instance=testModel_BClass_strategy)
def test_testmodel_bclass_BClassAttr2_setter(instance):
    original = instance.BClassAttr2
    instance.BClassAttr2 = original
    assert instance.BClassAttr2 == original

@given(instance=testModel_AClass_strategy)
@settings(max_examples=50)
def test_testmodel_aclass_instantiation(instance):
    assert isinstance(instance, testModel_AClass)



@given(instance=testModel_AClass_strategy)
def test_testmodel_aclass_AClassAttr2_setter(instance):
    original = instance.AClassAttr2
    instance.AClassAttr2 = original
    assert instance.AClassAttr2 == original



@given(instance=testModel_AClass_strategy)
def test_testmodel_aclass_AClassAttr1_setter(instance):
    original = instance.AClassAttr1
    instance.AClassAttr1 = original
    assert instance.AClassAttr1 == original

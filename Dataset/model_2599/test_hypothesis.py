import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ClassInMainPackage,
    MainPackage::Subpackage::InheritingClass,
    MainPackage::Subpackage::ClassInSubpackage,
    MainPackage::EObject,
    MainPackage::Model,
    MainPackage::ClassInMainPackage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classinmainpackage_is_not_abstract():
    assert not inspect.isabstract(ClassInMainPackage)


def test_classinmainpackage_constructor_exists():
    assert callable(ClassInMainPackage.__init__)


def test_classinmainpackage_constructor_args():
    sig = inspect.signature(ClassInMainPackage.__init__)
    params = list(sig.parameters.keys())



def test_mainpackage::subpackage::inheritingclass_is_not_abstract():
    assert not inspect.isabstract(MainPackage::Subpackage::InheritingClass)


def test_mainpackage::subpackage::inheritingclass_constructor_exists():
    assert callable(MainPackage::Subpackage::InheritingClass.__init__)


def test_mainpackage::subpackage::inheritingclass_constructor_args():
    sig = inspect.signature(MainPackage::Subpackage::InheritingClass.__init__)
    params = list(sig.parameters.keys())



def test_mainpackage::subpackage::classinsubpackage_is_not_abstract():
    assert not inspect.isabstract(MainPackage::Subpackage::ClassInSubpackage)


def test_mainpackage::subpackage::classinsubpackage_constructor_exists():
    assert callable(MainPackage::Subpackage::ClassInSubpackage.__init__)


def test_mainpackage::subpackage::classinsubpackage_constructor_args():
    sig = inspect.signature(MainPackage::Subpackage::ClassInSubpackage.__init__)
    params = list(sig.parameters.keys())



def test_mainpackage::eobject_is_not_abstract():
    assert not inspect.isabstract(MainPackage::EObject)


def test_mainpackage::eobject_constructor_exists():
    assert callable(MainPackage::EObject.__init__)


def test_mainpackage::eobject_constructor_args():
    sig = inspect.signature(MainPackage::EObject.__init__)
    params = list(sig.parameters.keys())



def test_mainpackage::model_is_not_abstract():
    assert not inspect.isabstract(MainPackage::Model)


def test_mainpackage::model_constructor_exists():
    assert callable(MainPackage::Model.__init__)


def test_mainpackage::model_constructor_args():
    sig = inspect.signature(MainPackage::Model.__init__)
    params = list(sig.parameters.keys())



def test_mainpackage::classinmainpackage_is_not_abstract():
    assert not inspect.isabstract(MainPackage::ClassInMainPackage)


def test_mainpackage::classinmainpackage_constructor_exists():
    assert callable(MainPackage::ClassInMainPackage.__init__)


def test_mainpackage::classinmainpackage_constructor_args():
    sig = inspect.signature(MainPackage::ClassInMainPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mainpackage::classinmainpackage_has_name():
    assert hasattr(MainPackage::ClassInMainPackage, "name")
    descriptor = None
    for klass in MainPackage::ClassInMainPackage.__mro__:
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
ClassInMainPackage_strategy = st.builds(
    ClassInMainPackage,
)
MainPackage::Subpackage::InheritingClass_strategy = st.builds(
    MainPackage::Subpackage::InheritingClass,
)
MainPackage::Subpackage::ClassInSubpackage_strategy = st.builds(
    MainPackage::Subpackage::ClassInSubpackage,
)
MainPackage::EObject_strategy = st.builds(
    MainPackage::EObject,
)
MainPackage::Model_strategy = st.builds(
    MainPackage::Model,
)
MainPackage::ClassInMainPackage_strategy = st.builds(
    MainPackage::ClassInMainPackage,
    name=
        safe_text
)

@given(instance=ClassInMainPackage_strategy)
@settings(max_examples=50)
def test_classinmainpackage_instantiation(instance):
    assert isinstance(instance, ClassInMainPackage)

@given(instance=MainPackage::Subpackage::InheritingClass_strategy)
@settings(max_examples=50)
def test_mainpackage::subpackage::inheritingclass_instantiation(instance):
    assert isinstance(instance, MainPackage::Subpackage::InheritingClass)

@given(instance=MainPackage::Subpackage::ClassInSubpackage_strategy)
@settings(max_examples=50)
def test_mainpackage::subpackage::classinsubpackage_instantiation(instance):
    assert isinstance(instance, MainPackage::Subpackage::ClassInSubpackage)

@given(instance=MainPackage::EObject_strategy)
@settings(max_examples=50)
def test_mainpackage::eobject_instantiation(instance):
    assert isinstance(instance, MainPackage::EObject)

@given(instance=MainPackage::Model_strategy)
@settings(max_examples=50)
def test_mainpackage::model_instantiation(instance):
    assert isinstance(instance, MainPackage::Model)

@given(instance=MainPackage::ClassInMainPackage_strategy)
@settings(max_examples=50)
def test_mainpackage::classinmainpackage_instantiation(instance):
    assert isinstance(instance, MainPackage::ClassInMainPackage)

@given(instance=MainPackage::ClassInMainPackage_strategy)
def test_mainpackage::classinmainpackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MainPackage::ClassInMainPackage_strategy)
def test_mainpackage::classinmainpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

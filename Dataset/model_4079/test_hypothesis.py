import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Classifier,
    umlMM_Class,
    umlMM_Classifier,
    umlMM_Datatype,
    umlMM_Attribute,
    umlMM_Associaton,
    umlMM_Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmm_class_is_not_abstract():
    assert not inspect.isabstract(umlMM_Class)


def test_umlmm_class_constructor_exists():
    assert callable(umlMM_Class.__init__)


def test_umlmm_class_constructor_args():
    sig = inspect.signature(umlMM_Class.__init__)
    params = list(sig.parameters.keys())



def test_umlmm_classifier_is_not_abstract():
    assert not inspect.isabstract(umlMM_Classifier)


def test_umlmm_classifier_constructor_exists():
    assert callable(umlMM_Classifier.__init__)


def test_umlmm_classifier_constructor_args():
    sig = inspect.signature(umlMM_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm_classifier_has_name():
    assert hasattr(umlMM_Classifier, "name")
    descriptor = None
    for klass in umlMM_Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm_datatype_is_not_abstract():
    assert not inspect.isabstract(umlMM_Datatype)


def test_umlmm_datatype_constructor_exists():
    assert callable(umlMM_Datatype.__init__)


def test_umlmm_datatype_constructor_args():
    sig = inspect.signature(umlMM_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_umlmm_attribute_is_not_abstract():
    assert not inspect.isabstract(umlMM_Attribute)


def test_umlmm_attribute_constructor_exists():
    assert callable(umlMM_Attribute.__init__)


def test_umlmm_attribute_constructor_args():
    sig = inspect.signature(umlMM_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm_attribute_has_name():
    assert hasattr(umlMM_Attribute, "name")
    descriptor = None
    for klass in umlMM_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm_associaton_is_not_abstract():
    assert not inspect.isabstract(umlMM_Associaton)


def test_umlmm_associaton_constructor_exists():
    assert callable(umlMM_Associaton.__init__)


def test_umlmm_associaton_constructor_args():
    sig = inspect.signature(umlMM_Associaton.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm_associaton_has_name():
    assert hasattr(umlMM_Associaton, "name")
    descriptor = None
    for klass in umlMM_Associaton.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm_package_is_not_abstract():
    assert not inspect.isabstract(umlMM_Package)


def test_umlmm_package_constructor_exists():
    assert callable(umlMM_Package.__init__)


def test_umlmm_package_constructor_args():
    sig = inspect.signature(umlMM_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm_package_has_name():
    assert hasattr(umlMM_Package, "name")
    descriptor = None
    for klass in umlMM_Package.__mro__:
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
Classifier_strategy = st.builds(
    Classifier,
)
umlMM_Class_strategy = st.builds(
    umlMM_Class,
)
umlMM_Classifier_strategy = st.builds(
    umlMM_Classifier,
    name=
        safe_text
)
umlMM_Datatype_strategy = st.builds(
    umlMM_Datatype,
)
umlMM_Attribute_strategy = st.builds(
    umlMM_Attribute,
    name=
        safe_text
)
umlMM_Associaton_strategy = st.builds(
    umlMM_Associaton,
    name=
        safe_text
)
umlMM_Package_strategy = st.builds(
    umlMM_Package,
    name=
        safe_text
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=umlMM_Class_strategy)
@settings(max_examples=50)
def test_umlmm_class_instantiation(instance):
    assert isinstance(instance, umlMM_Class)

@given(instance=umlMM_Classifier_strategy)
@settings(max_examples=50)
def test_umlmm_classifier_instantiation(instance):
    assert isinstance(instance, umlMM_Classifier)



@given(instance=umlMM_Classifier_strategy)
def test_umlmm_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM_Datatype_strategy)
@settings(max_examples=50)
def test_umlmm_datatype_instantiation(instance):
    assert isinstance(instance, umlMM_Datatype)

@given(instance=umlMM_Attribute_strategy)
@settings(max_examples=50)
def test_umlmm_attribute_instantiation(instance):
    assert isinstance(instance, umlMM_Attribute)



@given(instance=umlMM_Attribute_strategy)
def test_umlmm_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM_Associaton_strategy)
@settings(max_examples=50)
def test_umlmm_associaton_instantiation(instance):
    assert isinstance(instance, umlMM_Associaton)



@given(instance=umlMM_Associaton_strategy)
def test_umlmm_associaton_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM_Package_strategy)
@settings(max_examples=50)
def test_umlmm_package_instantiation(instance):
    assert isinstance(instance, umlMM_Package)



@given(instance=umlMM_Package_strategy)
def test_umlmm_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

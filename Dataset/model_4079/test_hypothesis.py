import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Classifier,
    umlMM::Class,
    umlMM::Classifier,
    umlMM::Datatype,
    umlMM::Attribute,
    umlMM::Associaton,
    umlMM::Package,
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



def test_umlmm::class_is_not_abstract():
    assert not inspect.isabstract(umlMM::Class)


def test_umlmm::class_constructor_exists():
    assert callable(umlMM::Class.__init__)


def test_umlmm::class_constructor_args():
    sig = inspect.signature(umlMM::Class.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::classifier_is_not_abstract():
    assert not inspect.isabstract(umlMM::Classifier)


def test_umlmm::classifier_constructor_exists():
    assert callable(umlMM::Classifier.__init__)


def test_umlmm::classifier_constructor_args():
    sig = inspect.signature(umlMM::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::classifier_has_name():
    assert hasattr(umlMM::Classifier, "name")
    descriptor = None
    for klass in umlMM::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::datatype_is_not_abstract():
    assert not inspect.isabstract(umlMM::Datatype)


def test_umlmm::datatype_constructor_exists():
    assert callable(umlMM::Datatype.__init__)


def test_umlmm::datatype_constructor_args():
    sig = inspect.signature(umlMM::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_umlmm::attribute_is_not_abstract():
    assert not inspect.isabstract(umlMM::Attribute)


def test_umlmm::attribute_constructor_exists():
    assert callable(umlMM::Attribute.__init__)


def test_umlmm::attribute_constructor_args():
    sig = inspect.signature(umlMM::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::attribute_has_name():
    assert hasattr(umlMM::Attribute, "name")
    descriptor = None
    for klass in umlMM::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::associaton_is_not_abstract():
    assert not inspect.isabstract(umlMM::Associaton)


def test_umlmm::associaton_constructor_exists():
    assert callable(umlMM::Associaton.__init__)


def test_umlmm::associaton_constructor_args():
    sig = inspect.signature(umlMM::Associaton.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::associaton_has_name():
    assert hasattr(umlMM::Associaton, "name")
    descriptor = None
    for klass in umlMM::Associaton.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmm::package_is_not_abstract():
    assert not inspect.isabstract(umlMM::Package)


def test_umlmm::package_constructor_exists():
    assert callable(umlMM::Package.__init__)


def test_umlmm::package_constructor_args():
    sig = inspect.signature(umlMM::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlmm::package_has_name():
    assert hasattr(umlMM::Package, "name")
    descriptor = None
    for klass in umlMM::Package.__mro__:
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
umlMM::Class_strategy = st.builds(
    umlMM::Class,
)
umlMM::Classifier_strategy = st.builds(
    umlMM::Classifier,
    name=
        safe_text
)
umlMM::Datatype_strategy = st.builds(
    umlMM::Datatype,
)
umlMM::Attribute_strategy = st.builds(
    umlMM::Attribute,
    name=
        safe_text
)
umlMM::Associaton_strategy = st.builds(
    umlMM::Associaton,
    name=
        safe_text
)
umlMM::Package_strategy = st.builds(
    umlMM::Package,
    name=
        safe_text
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=umlMM::Class_strategy)
@settings(max_examples=50)
def test_umlmm::class_instantiation(instance):
    assert isinstance(instance, umlMM::Class)

@given(instance=umlMM::Classifier_strategy)
@settings(max_examples=50)
def test_umlmm::classifier_instantiation(instance):
    assert isinstance(instance, umlMM::Classifier)

@given(instance=umlMM::Classifier_strategy)
def test_umlmm::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlMM::Classifier_strategy)
def test_umlmm::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM::Datatype_strategy)
@settings(max_examples=50)
def test_umlmm::datatype_instantiation(instance):
    assert isinstance(instance, umlMM::Datatype)

@given(instance=umlMM::Attribute_strategy)
@settings(max_examples=50)
def test_umlmm::attribute_instantiation(instance):
    assert isinstance(instance, umlMM::Attribute)

@given(instance=umlMM::Attribute_strategy)
def test_umlmm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlMM::Attribute_strategy)
def test_umlmm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM::Associaton_strategy)
@settings(max_examples=50)
def test_umlmm::associaton_instantiation(instance):
    assert isinstance(instance, umlMM::Associaton)

@given(instance=umlMM::Associaton_strategy)
def test_umlmm::associaton_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlMM::Associaton_strategy)
def test_umlmm::associaton_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlMM::Package_strategy)
@settings(max_examples=50)
def test_umlmm::package_instantiation(instance):
    assert isinstance(instance, umlMM::Package)

@given(instance=umlMM::Package_strategy)
def test_umlmm::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlMM::Package_strategy)
def test_umlmm::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UML::Attribute,
    Classifier,
    UML::PrimitiveDataType,
    UML::Class,
    UML::Association,
    UML::Classifier,
    UML::Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml::attribute_is_not_abstract():
    assert not inspect.isabstract(UML::Attribute)


def test_uml::attribute_constructor_exists():
    assert callable(UML::Attribute.__init__)


def test_uml::attribute_constructor_args():
    sig = inspect.signature(UML::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::attribute_has_name():
    assert hasattr(UML::Attribute, "name")
    descriptor = None
    for klass in UML::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(UML::PrimitiveDataType)


def test_uml::primitivedatatype_constructor_exists():
    assert callable(UML::PrimitiveDataType.__init__)


def test_uml::primitivedatatype_constructor_args():
    sig = inspect.signature(UML::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_uml::class_is_not_abstract():
    assert not inspect.isabstract(UML::Class)


def test_uml::class_constructor_exists():
    assert callable(UML::Class.__init__)


def test_uml::class_constructor_args():
    sig = inspect.signature(UML::Class.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml::class_has_kind():
    assert hasattr(UML::Class, "kind")
    descriptor = None
    for klass in UML::Class.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uml::association_is_not_abstract():
    assert not inspect.isabstract(UML::Association)


def test_uml::association_constructor_exists():
    assert callable(UML::Association.__init__)


def test_uml::association_constructor_args():
    sig = inspect.signature(UML::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::association_has_name():
    assert hasattr(UML::Association, "name")
    descriptor = None
    for klass in UML::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml::classifier_is_not_abstract():
    assert not inspect.isabstract(UML::Classifier)


def test_uml::classifier_constructor_exists():
    assert callable(UML::Classifier.__init__)


def test_uml::classifier_constructor_args():
    sig = inspect.signature(UML::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::classifier_has_name():
    assert hasattr(UML::Classifier, "name")
    descriptor = None
    for klass in UML::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml::package_is_not_abstract():
    assert not inspect.isabstract(UML::Package)


def test_uml::package_constructor_exists():
    assert callable(UML::Package.__init__)


def test_uml::package_constructor_args():
    sig = inspect.signature(UML::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::package_has_name():
    assert hasattr(UML::Package, "name")
    descriptor = None
    for klass in UML::Package.__mro__:
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
UML::Attribute_strategy = st.builds(
    UML::Attribute,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
UML::PrimitiveDataType_strategy = st.builds(
    UML::PrimitiveDataType,
)
UML::Class_strategy = st.builds(
    UML::Class,
    kind=
        safe_text
)
UML::Association_strategy = st.builds(
    UML::Association,
    name=
        safe_text
)
UML::Classifier_strategy = st.builds(
    UML::Classifier,
    name=
        safe_text
)
UML::Package_strategy = st.builds(
    UML::Package,
    name=
        safe_text
)

@given(instance=UML::Attribute_strategy)
@settings(max_examples=50)
def test_uml::attribute_instantiation(instance):
    assert isinstance(instance, UML::Attribute)

@given(instance=UML::Attribute_strategy)
def test_uml::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UML::Attribute_strategy)
def test_uml::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_uml::primitivedatatype_instantiation(instance):
    assert isinstance(instance, UML::PrimitiveDataType)

@given(instance=UML::Class_strategy)
@settings(max_examples=50)
def test_uml::class_instantiation(instance):
    assert isinstance(instance, UML::Class)

@given(instance=UML::Class_strategy)
def test_uml::class_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=UML::Class_strategy)
def test_uml::class_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=UML::Association_strategy)
@settings(max_examples=50)
def test_uml::association_instantiation(instance):
    assert isinstance(instance, UML::Association)

@given(instance=UML::Association_strategy)
def test_uml::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UML::Association_strategy)
def test_uml::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UML::Classifier_strategy)
@settings(max_examples=50)
def test_uml::classifier_instantiation(instance):
    assert isinstance(instance, UML::Classifier)

@given(instance=UML::Classifier_strategy)
def test_uml::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UML::Classifier_strategy)
def test_uml::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UML::Package_strategy)
@settings(max_examples=50)
def test_uml::package_instantiation(instance):
    assert isinstance(instance, UML::Package)

@given(instance=UML::Package_strategy)
def test_uml::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=UML::Package_strategy)
def test_uml::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

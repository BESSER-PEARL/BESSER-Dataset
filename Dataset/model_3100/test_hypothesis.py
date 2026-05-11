import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    classdiagram::Attribute,
    Classifier,
    classdiagram::Class,
    classdiagram::PrimitiveDataType,
    classdiagram::Association,
    classdiagram::Classifier,
    classdiagram::Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Attribute)


def test_classdiagram::attribute_constructor_exists():
    assert callable(classdiagram::Attribute.__init__)


def test_classdiagram::attribute_constructor_args():
    sig = inspect.signature(classdiagram::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "is_primary" in params, "Missing parameter 'is_primary'"
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::attribute_has_is_primary():
    assert hasattr(classdiagram::Attribute, "is_primary")
    descriptor = None
    for klass in classdiagram::Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::attribute_has_name():
    assert hasattr(classdiagram::Attribute, "name")
    descriptor = None
    for klass in classdiagram::Attribute.__mro__:
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



def test_classdiagram::class_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Class)


def test_classdiagram::class_constructor_exists():
    assert callable(classdiagram::Class.__init__)


def test_classdiagram::class_constructor_args():
    sig = inspect.signature(classdiagram::Class.__init__)
    params = list(sig.parameters.keys())
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_classdiagram::class_has_is_persistent():
    assert hasattr(classdiagram::Class, "is_persistent")
    descriptor = None
    for klass in classdiagram::Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(classdiagram::PrimitiveDataType)


def test_classdiagram::primitivedatatype_constructor_exists():
    assert callable(classdiagram::PrimitiveDataType.__init__)


def test_classdiagram::primitivedatatype_constructor_args():
    sig = inspect.signature(classdiagram::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::association_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Association)


def test_classdiagram::association_constructor_exists():
    assert callable(classdiagram::Association.__init__)


def test_classdiagram::association_constructor_args():
    sig = inspect.signature(classdiagram::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::association_has_name():
    assert hasattr(classdiagram::Association, "name")
    descriptor = None
    for klass in classdiagram::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::classifier_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Classifier)


def test_classdiagram::classifier_constructor_exists():
    assert callable(classdiagram::Classifier.__init__)


def test_classdiagram::classifier_constructor_args():
    sig = inspect.signature(classdiagram::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::classifier_has_name():
    assert hasattr(classdiagram::Classifier, "name")
    descriptor = None
    for klass in classdiagram::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::package_is_not_abstract():
    assert not inspect.isabstract(classdiagram::Package)


def test_classdiagram::package_constructor_exists():
    assert callable(classdiagram::Package.__init__)


def test_classdiagram::package_constructor_args():
    sig = inspect.signature(classdiagram::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::package_has_name():
    assert hasattr(classdiagram::Package, "name")
    descriptor = None
    for klass in classdiagram::Package.__mro__:
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
classdiagram::Attribute_strategy = st.builds(
    classdiagram::Attribute,
    is_primary=
        st.booleans(),
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
classdiagram::Class_strategy = st.builds(
    classdiagram::Class,
    is_persistent=
        st.booleans()
)
classdiagram::PrimitiveDataType_strategy = st.builds(
    classdiagram::PrimitiveDataType,
)
classdiagram::Association_strategy = st.builds(
    classdiagram::Association,
    name=
        safe_text
)
classdiagram::Classifier_strategy = st.builds(
    classdiagram::Classifier,
    name=
        safe_text
)
classdiagram::Package_strategy = st.builds(
    classdiagram::Package,
    name=
        safe_text
)

@given(instance=classdiagram::Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram::attribute_instantiation(instance):
    assert isinstance(instance, classdiagram::Attribute)

@given(instance=classdiagram::Attribute_strategy)
def test_classdiagram::attribute_is_primary_type(instance):
    assert isinstance(instance.is_primary, bool)


@given(instance=classdiagram::Attribute_strategy)
def test_classdiagram::attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=classdiagram::Attribute_strategy)
def test_classdiagram::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classdiagram::Attribute_strategy)
def test_classdiagram::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=classdiagram::Class_strategy)
@settings(max_examples=50)
def test_classdiagram::class_instantiation(instance):
    assert isinstance(instance, classdiagram::Class)

@given(instance=classdiagram::Class_strategy)
def test_classdiagram::class_is_persistent_type(instance):
    assert isinstance(instance.is_persistent, bool)


@given(instance=classdiagram::Class_strategy)
def test_classdiagram::class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=classdiagram::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_classdiagram::primitivedatatype_instantiation(instance):
    assert isinstance(instance, classdiagram::PrimitiveDataType)

@given(instance=classdiagram::Association_strategy)
@settings(max_examples=50)
def test_classdiagram::association_instantiation(instance):
    assert isinstance(instance, classdiagram::Association)

@given(instance=classdiagram::Association_strategy)
def test_classdiagram::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classdiagram::Association_strategy)
def test_classdiagram::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classdiagram::Classifier_strategy)
@settings(max_examples=50)
def test_classdiagram::classifier_instantiation(instance):
    assert isinstance(instance, classdiagram::Classifier)

@given(instance=classdiagram::Classifier_strategy)
def test_classdiagram::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classdiagram::Classifier_strategy)
def test_classdiagram::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classdiagram::Package_strategy)
@settings(max_examples=50)
def test_classdiagram::package_instantiation(instance):
    assert isinstance(instance, classdiagram::Package)

@given(instance=classdiagram::Package_strategy)
def test_classdiagram::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classdiagram::Package_strategy)
def test_classdiagram::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

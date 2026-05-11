import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Classifier,
    simpleUML::MM::Attribute,
    simpleUML::MM::Class,
    simpleUML::MM::Association,
    simpleUML::MM::Classifier,
    simpleUML::MM::ClassModel,
    simpleUML::MM::PrimitiveDataType,
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



def test_simpleuml::mm::attribute_is_not_abstract():
    assert not inspect.isabstract(simpleUML::MM::Attribute)


def test_simpleuml::mm::attribute_constructor_exists():
    assert callable(simpleUML::MM::Attribute.__init__)


def test_simpleuml::mm::attribute_constructor_args():
    sig = inspect.signature(simpleUML::MM::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "is_primary" in params, "Missing parameter 'is_primary'"
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::mm::attribute_has_is_primary():
    assert hasattr(simpleUML::MM::Attribute, "is_primary")
    descriptor = None
    for klass in simpleUML::MM::Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml::mm::attribute_has_name():
    assert hasattr(simpleUML::MM::Attribute, "name")
    descriptor = None
    for klass in simpleUML::MM::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::mm::class_is_not_abstract():
    assert not inspect.isabstract(simpleUML::MM::Class)


def test_simpleuml::mm::class_constructor_exists():
    assert callable(simpleUML::MM::Class.__init__)


def test_simpleuml::mm::class_constructor_args():
    sig = inspect.signature(simpleUML::MM::Class.__init__)
    params = list(sig.parameters.keys())
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_simpleuml::mm::class_has_is_persistent():
    assert hasattr(simpleUML::MM::Class, "is_persistent")
    descriptor = None
    for klass in simpleUML::MM::Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::mm::association_is_not_abstract():
    assert not inspect.isabstract(simpleUML::MM::Association)


def test_simpleuml::mm::association_constructor_exists():
    assert callable(simpleUML::MM::Association.__init__)


def test_simpleuml::mm::association_constructor_args():
    sig = inspect.signature(simpleUML::MM::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::mm::association_has_name():
    assert hasattr(simpleUML::MM::Association, "name")
    descriptor = None
    for klass in simpleUML::MM::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::mm::classifier_is_not_abstract():
    assert not inspect.isabstract(simpleUML::MM::Classifier)


def test_simpleuml::mm::classifier_constructor_exists():
    assert callable(simpleUML::MM::Classifier.__init__)


def test_simpleuml::mm::classifier_constructor_args():
    sig = inspect.signature(simpleUML::MM::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::mm::classifier_has_name():
    assert hasattr(simpleUML::MM::Classifier, "name")
    descriptor = None
    for klass in simpleUML::MM::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::mm::classmodel_is_not_abstract():
    assert not inspect.isabstract(simpleUML::MM::ClassModel)


def test_simpleuml::mm::classmodel_constructor_exists():
    assert callable(simpleUML::MM::ClassModel.__init__)


def test_simpleuml::mm::classmodel_constructor_args():
    sig = inspect.signature(simpleUML::MM::ClassModel.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::mm::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(simpleUML::MM::PrimitiveDataType)


def test_simpleuml::mm::primitivedatatype_constructor_exists():
    assert callable(simpleUML::MM::PrimitiveDataType.__init__)


def test_simpleuml::mm::primitivedatatype_constructor_args():
    sig = inspect.signature(simpleUML::MM::PrimitiveDataType.__init__)
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
Classifier_strategy = st.builds(
    Classifier,
)
simpleUML::MM::Attribute_strategy = st.builds(
    simpleUML::MM::Attribute,
    is_primary=
        st.booleans(),
    name=
        safe_text
)
simpleUML::MM::Class_strategy = st.builds(
    simpleUML::MM::Class,
    is_persistent=
        st.booleans()
)
simpleUML::MM::Association_strategy = st.builds(
    simpleUML::MM::Association,
    name=
        safe_text
)
simpleUML::MM::Classifier_strategy = st.builds(
    simpleUML::MM::Classifier,
    name=
        safe_text
)
simpleUML::MM::ClassModel_strategy = st.builds(
    simpleUML::MM::ClassModel,
)
simpleUML::MM::PrimitiveDataType_strategy = st.builds(
    simpleUML::MM::PrimitiveDataType,
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleUML::MM::Attribute_strategy)
@settings(max_examples=50)
def test_simpleuml::mm::attribute_instantiation(instance):
    assert isinstance(instance, simpleUML::MM::Attribute)

@given(instance=simpleUML::MM::Attribute_strategy)
def test_simpleuml::mm::attribute_is_primary_type(instance):
    assert isinstance(instance.is_primary, bool)


@given(instance=simpleUML::MM::Attribute_strategy)
def test_simpleuml::mm::attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=simpleUML::MM::Attribute_strategy)
def test_simpleuml::mm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleUML::MM::Attribute_strategy)
def test_simpleuml::mm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleUML::MM::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::mm::class_instantiation(instance):
    assert isinstance(instance, simpleUML::MM::Class)

@given(instance=simpleUML::MM::Class_strategy)
def test_simpleuml::mm::class_is_persistent_type(instance):
    assert isinstance(instance.is_persistent, bool)


@given(instance=simpleUML::MM::Class_strategy)
def test_simpleuml::mm::class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=simpleUML::MM::Association_strategy)
@settings(max_examples=50)
def test_simpleuml::mm::association_instantiation(instance):
    assert isinstance(instance, simpleUML::MM::Association)

@given(instance=simpleUML::MM::Association_strategy)
def test_simpleuml::mm::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleUML::MM::Association_strategy)
def test_simpleuml::mm::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleUML::MM::Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml::mm::classifier_instantiation(instance):
    assert isinstance(instance, simpleUML::MM::Classifier)

@given(instance=simpleUML::MM::Classifier_strategy)
def test_simpleuml::mm::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleUML::MM::Classifier_strategy)
def test_simpleuml::mm::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleUML::MM::ClassModel_strategy)
@settings(max_examples=50)
def test_simpleuml::mm::classmodel_instantiation(instance):
    assert isinstance(instance, simpleUML::MM::ClassModel)

@given(instance=simpleUML::MM::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleuml::mm::primitivedatatype_instantiation(instance):
    assert isinstance(instance, simpleUML::MM::PrimitiveDataType)

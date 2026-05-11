import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleClass::Attribute,
    Classifier,
    simpleClass::PrimitiveDataType,
    simpleClass::Class,
    simpleClass::Association,
    simpleClass::Classifier,
    simpleClass::ClassModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleclass::attribute_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Attribute)


def test_simpleclass::attribute_constructor_exists():
    assert callable(simpleClass::Attribute.__init__)


def test_simpleclass::attribute_constructor_args():
    sig = inspect.signature(simpleClass::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_simpleclass::attribute_has_name():
    assert hasattr(simpleClass::Attribute, "name")
    descriptor = None
    for klass in simpleClass::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpleclass::attribute_has_id():
    assert hasattr(simpleClass::Attribute, "id")
    descriptor = None
    for klass in simpleClass::Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(simpleClass::PrimitiveDataType)


def test_simpleclass::primitivedatatype_constructor_exists():
    assert callable(simpleClass::PrimitiveDataType.__init__)


def test_simpleclass::primitivedatatype_constructor_args():
    sig = inspect.signature(simpleClass::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::class_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Class)


def test_simpleclass::class_constructor_exists():
    assert callable(simpleClass::Class.__init__)


def test_simpleclass::class_constructor_args():
    sig = inspect.signature(simpleClass::Class.__init__)
    params = list(sig.parameters.keys())
    assert "persistent" in params, "Missing parameter 'persistent'"

def test_simpleclass::class_has_persistent():
    assert hasattr(simpleClass::Class, "persistent")
    descriptor = None
    for klass in simpleClass::Class.__mro__:
        if "persistent" in klass.__dict__:
            descriptor = klass.__dict__["persistent"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass::association_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Association)


def test_simpleclass::association_constructor_exists():
    assert callable(simpleClass::Association.__init__)


def test_simpleclass::association_constructor_args():
    sig = inspect.signature(simpleClass::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass::association_has_name():
    assert hasattr(simpleClass::Association, "name")
    descriptor = None
    for klass in simpleClass::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass::classifier_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Classifier)


def test_simpleclass::classifier_constructor_exists():
    assert callable(simpleClass::Classifier.__init__)


def test_simpleclass::classifier_constructor_args():
    sig = inspect.signature(simpleClass::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass::classifier_has_name():
    assert hasattr(simpleClass::Classifier, "name")
    descriptor = None
    for klass in simpleClass::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass::classmodel_is_not_abstract():
    assert not inspect.isabstract(simpleClass::ClassModel)


def test_simpleclass::classmodel_constructor_exists():
    assert callable(simpleClass::ClassModel.__init__)


def test_simpleclass::classmodel_constructor_args():
    sig = inspect.signature(simpleClass::ClassModel.__init__)
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
simpleClass::Attribute_strategy = st.builds(
    simpleClass::Attribute,
    name=
        safe_text,
    id=
        st.booleans()
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleClass::PrimitiveDataType_strategy = st.builds(
    simpleClass::PrimitiveDataType,
)
simpleClass::Class_strategy = st.builds(
    simpleClass::Class,
    persistent=
        st.booleans()
)
simpleClass::Association_strategy = st.builds(
    simpleClass::Association,
    name=
        safe_text
)
simpleClass::Classifier_strategy = st.builds(
    simpleClass::Classifier,
    name=
        safe_text
)
simpleClass::ClassModel_strategy = st.builds(
    simpleClass::ClassModel,
)

@given(instance=simpleClass::Attribute_strategy)
@settings(max_examples=50)
def test_simpleclass::attribute_instantiation(instance):
    assert isinstance(instance, simpleClass::Attribute)

@given(instance=simpleClass::Attribute_strategy)
def test_simpleclass::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleClass::Attribute_strategy)
def test_simpleclass::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleClass::Attribute_strategy)
def test_simpleclass::attribute_id_type(instance):
    assert isinstance(instance.id, bool)


@given(instance=simpleClass::Attribute_strategy)
def test_simpleclass::attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleClass::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleclass::primitivedatatype_instantiation(instance):
    assert isinstance(instance, simpleClass::PrimitiveDataType)

@given(instance=simpleClass::Class_strategy)
@settings(max_examples=50)
def test_simpleclass::class_instantiation(instance):
    assert isinstance(instance, simpleClass::Class)

@given(instance=simpleClass::Class_strategy)
def test_simpleclass::class_persistent_type(instance):
    assert isinstance(instance.persistent, bool)


@given(instance=simpleClass::Class_strategy)
def test_simpleclass::class_persistent_setter(instance):
    original = instance.persistent
    instance.persistent = original
    assert instance.persistent == original

@given(instance=simpleClass::Association_strategy)
@settings(max_examples=50)
def test_simpleclass::association_instantiation(instance):
    assert isinstance(instance, simpleClass::Association)

@given(instance=simpleClass::Association_strategy)
def test_simpleclass::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleClass::Association_strategy)
def test_simpleclass::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleClass::Classifier_strategy)
@settings(max_examples=50)
def test_simpleclass::classifier_instantiation(instance):
    assert isinstance(instance, simpleClass::Classifier)

@given(instance=simpleClass::Classifier_strategy)
def test_simpleclass::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleClass::Classifier_strategy)
def test_simpleclass::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleClass::ClassModel_strategy)
@settings(max_examples=50)
def test_simpleclass::classmodel_instantiation(instance):
    assert isinstance(instance, simpleClass::ClassModel)

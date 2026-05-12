import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleClass_Attribute,
    Classifier,
    simpleClass_PrimitiveDataType,
    simpleClass_Class,
    simpleClass_Association,
    simpleClass_Classifier,
    simpleClass_ClassModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleclass_attribute_is_not_abstract():
    assert not inspect.isabstract(simpleClass_Attribute)


def test_simpleclass_attribute_constructor_exists():
    assert callable(simpleClass_Attribute.__init__)


def test_simpleclass_attribute_constructor_args():
    sig = inspect.signature(simpleClass_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass_attribute_has_id():
    assert hasattr(simpleClass_Attribute, "id")
    descriptor = None
    for klass in simpleClass_Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_simpleclass_attribute_has_name():
    assert hasattr(simpleClass_Attribute, "name")
    descriptor = None
    for klass in simpleClass_Attribute.__mro__:
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



def test_simpleclass_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(simpleClass_PrimitiveDataType)


def test_simpleclass_primitivedatatype_constructor_exists():
    assert callable(simpleClass_PrimitiveDataType.__init__)


def test_simpleclass_primitivedatatype_constructor_args():
    sig = inspect.signature(simpleClass_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass_class_is_not_abstract():
    assert not inspect.isabstract(simpleClass_Class)


def test_simpleclass_class_constructor_exists():
    assert callable(simpleClass_Class.__init__)


def test_simpleclass_class_constructor_args():
    sig = inspect.signature(simpleClass_Class.__init__)
    params = list(sig.parameters.keys())
    assert "persistent" in params, "Missing parameter 'persistent'"

def test_simpleclass_class_has_persistent():
    assert hasattr(simpleClass_Class, "persistent")
    descriptor = None
    for klass in simpleClass_Class.__mro__:
        if "persistent" in klass.__dict__:
            descriptor = klass.__dict__["persistent"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass_association_is_not_abstract():
    assert not inspect.isabstract(simpleClass_Association)


def test_simpleclass_association_constructor_exists():
    assert callable(simpleClass_Association.__init__)


def test_simpleclass_association_constructor_args():
    sig = inspect.signature(simpleClass_Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass_association_has_name():
    assert hasattr(simpleClass_Association, "name")
    descriptor = None
    for klass in simpleClass_Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass_classifier_is_not_abstract():
    assert not inspect.isabstract(simpleClass_Classifier)


def test_simpleclass_classifier_constructor_exists():
    assert callable(simpleClass_Classifier.__init__)


def test_simpleclass_classifier_constructor_args():
    sig = inspect.signature(simpleClass_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass_classifier_has_name():
    assert hasattr(simpleClass_Classifier, "name")
    descriptor = None
    for klass in simpleClass_Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass_classmodel_is_not_abstract():
    assert not inspect.isabstract(simpleClass_ClassModel)


def test_simpleclass_classmodel_constructor_exists():
    assert callable(simpleClass_ClassModel.__init__)


def test_simpleclass_classmodel_constructor_args():
    sig = inspect.signature(simpleClass_ClassModel.__init__)
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
simpleClass_Attribute_strategy = st.builds(
    simpleClass_Attribute,
    id=
        st.booleans(),
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleClass_PrimitiveDataType_strategy = st.builds(
    simpleClass_PrimitiveDataType,
)
simpleClass_Class_strategy = st.builds(
    simpleClass_Class,
    persistent=
        st.booleans()
)
simpleClass_Association_strategy = st.builds(
    simpleClass_Association,
    name=
        safe_text
)
simpleClass_Classifier_strategy = st.builds(
    simpleClass_Classifier,
    name=
        safe_text
)
simpleClass_ClassModel_strategy = st.builds(
    simpleClass_ClassModel,
)

@given(instance=simpleClass_Attribute_strategy)
@settings(max_examples=50)
def test_simpleclass_attribute_instantiation(instance):
    assert isinstance(instance, simpleClass_Attribute)



@given(instance=simpleClass_Attribute_strategy)
def test_simpleclass_attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=simpleClass_Attribute_strategy)
def test_simpleclass_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleClass_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleclass_primitivedatatype_instantiation(instance):
    assert isinstance(instance, simpleClass_PrimitiveDataType)

@given(instance=simpleClass_Class_strategy)
@settings(max_examples=50)
def test_simpleclass_class_instantiation(instance):
    assert isinstance(instance, simpleClass_Class)



@given(instance=simpleClass_Class_strategy)
def test_simpleclass_class_persistent_setter(instance):
    original = instance.persistent
    instance.persistent = original
    assert instance.persistent == original

@given(instance=simpleClass_Association_strategy)
@settings(max_examples=50)
def test_simpleclass_association_instantiation(instance):
    assert isinstance(instance, simpleClass_Association)



@given(instance=simpleClass_Association_strategy)
def test_simpleclass_association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleClass_Classifier_strategy)
@settings(max_examples=50)
def test_simpleclass_classifier_instantiation(instance):
    assert isinstance(instance, simpleClass_Classifier)



@given(instance=simpleClass_Classifier_strategy)
def test_simpleclass_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleClass_ClassModel_strategy)
@settings(max_examples=50)
def test_simpleclass_classmodel_instantiation(instance):
    assert isinstance(instance, simpleClass_ClassModel)

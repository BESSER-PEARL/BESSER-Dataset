import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UML_Attribute,
    Classifier,
    UML_PrimitiveDataType,
    UML_Class,
    UML_Association,
    UML_Classifier,
    UML_Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml_attribute_is_not_abstract():
    assert not inspect.isabstract(UML_Attribute)


def test_uml_attribute_constructor_exists():
    assert callable(UML_Attribute.__init__)


def test_uml_attribute_constructor_args():
    sig = inspect.signature(UML_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml_attribute_has_name():
    assert hasattr(UML_Attribute, "name")
    descriptor = None
    for klass in UML_Attribute.__mro__:
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



def test_uml_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(UML_PrimitiveDataType)


def test_uml_primitivedatatype_constructor_exists():
    assert callable(UML_PrimitiveDataType.__init__)


def test_uml_primitivedatatype_constructor_args():
    sig = inspect.signature(UML_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_uml_class_is_not_abstract():
    assert not inspect.isabstract(UML_Class)


def test_uml_class_constructor_exists():
    assert callable(UML_Class.__init__)


def test_uml_class_constructor_args():
    sig = inspect.signature(UML_Class.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml_class_has_kind():
    assert hasattr(UML_Class, "kind")
    descriptor = None
    for klass in UML_Class.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uml_association_is_not_abstract():
    assert not inspect.isabstract(UML_Association)


def test_uml_association_constructor_exists():
    assert callable(UML_Association.__init__)


def test_uml_association_constructor_args():
    sig = inspect.signature(UML_Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml_association_has_name():
    assert hasattr(UML_Association, "name")
    descriptor = None
    for klass in UML_Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml_classifier_is_not_abstract():
    assert not inspect.isabstract(UML_Classifier)


def test_uml_classifier_constructor_exists():
    assert callable(UML_Classifier.__init__)


def test_uml_classifier_constructor_args():
    sig = inspect.signature(UML_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml_classifier_has_name():
    assert hasattr(UML_Classifier, "name")
    descriptor = None
    for klass in UML_Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml_package_is_not_abstract():
    assert not inspect.isabstract(UML_Package)


def test_uml_package_constructor_exists():
    assert callable(UML_Package.__init__)


def test_uml_package_constructor_args():
    sig = inspect.signature(UML_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml_package_has_name():
    assert hasattr(UML_Package, "name")
    descriptor = None
    for klass in UML_Package.__mro__:
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
UML_Attribute_strategy = st.builds(
    UML_Attribute,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
UML_PrimitiveDataType_strategy = st.builds(
    UML_PrimitiveDataType,
)
UML_Class_strategy = st.builds(
    UML_Class,
    kind=
        safe_text
)
UML_Association_strategy = st.builds(
    UML_Association,
    name=
        safe_text
)
UML_Classifier_strategy = st.builds(
    UML_Classifier,
    name=
        safe_text
)
UML_Package_strategy = st.builds(
    UML_Package,
    name=
        safe_text
)

@given(instance=UML_Attribute_strategy)
@settings(max_examples=50)
def test_uml_attribute_instantiation(instance):
    assert isinstance(instance, UML_Attribute)



@given(instance=UML_Attribute_strategy)
def test_uml_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_uml_primitivedatatype_instantiation(instance):
    assert isinstance(instance, UML_PrimitiveDataType)

@given(instance=UML_Class_strategy)
@settings(max_examples=50)
def test_uml_class_instantiation(instance):
    assert isinstance(instance, UML_Class)



@given(instance=UML_Class_strategy)
def test_uml_class_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=UML_Association_strategy)
@settings(max_examples=50)
def test_uml_association_instantiation(instance):
    assert isinstance(instance, UML_Association)



@given(instance=UML_Association_strategy)
def test_uml_association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UML_Classifier_strategy)
@settings(max_examples=50)
def test_uml_classifier_instantiation(instance):
    assert isinstance(instance, UML_Classifier)



@given(instance=UML_Classifier_strategy)
def test_uml_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UML_Package_strategy)
@settings(max_examples=50)
def test_uml_package_instantiation(instance):
    assert isinstance(instance, UML_Package)



@given(instance=UML_Package_strategy)
def test_uml_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

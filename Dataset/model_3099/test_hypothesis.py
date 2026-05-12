import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UML_Attribute,
    Classifier,
    UML_Class,
    UML_PrimitiveDataType,
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
    assert "is_primary" in params, "Missing parameter 'is_primary'"

def test_uml_attribute_has_name():
    assert hasattr(UML_Attribute, "name")
    descriptor = None
    for klass in UML_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_uml_attribute_has_is_primary():
    assert hasattr(UML_Attribute, "is_primary")
    descriptor = None
    for klass in UML_Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_class_is_not_abstract():
    assert not inspect.isabstract(UML_Class)


def test_uml_class_constructor_exists():
    assert callable(UML_Class.__init__)


def test_uml_class_constructor_args():
    sig = inspect.signature(UML_Class.__init__)
    params = list(sig.parameters.keys())
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_uml_class_has_is_persistent():
    assert hasattr(UML_Class, "is_persistent")
    descriptor = None
    for klass in UML_Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_uml_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(UML_PrimitiveDataType)


def test_uml_primitivedatatype_constructor_exists():
    assert callable(UML_PrimitiveDataType.__init__)


def test_uml_primitivedatatype_constructor_args():
    sig = inspect.signature(UML_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



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
        safe_text,
    is_primary=
        st.booleans()
)
Classifier_strategy = st.builds(
    Classifier,
)
UML_Class_strategy = st.builds(
    UML_Class,
    is_persistent=
        st.booleans()
)
UML_PrimitiveDataType_strategy = st.builds(
    UML_PrimitiveDataType,
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



@given(instance=UML_Attribute_strategy)
def test_uml_attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML_Class_strategy)
@settings(max_examples=50)
def test_uml_class_instantiation(instance):
    assert isinstance(instance, UML_Class)



@given(instance=UML_Class_strategy)
def test_uml_class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=UML_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_uml_primitivedatatype_instantiation(instance):
    assert isinstance(instance, UML_PrimitiveDataType)

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

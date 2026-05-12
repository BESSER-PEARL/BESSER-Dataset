import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rcd_ClassModel,
    Classifier,
    rcd_PrimitiveDataType,
    rcd_Attribute,
    rcd_Class,
    rcd_Association,
    rcd_Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rcd_classmodel_is_not_abstract():
    assert not inspect.isabstract(rcd_ClassModel)


def test_rcd_classmodel_constructor_exists():
    assert callable(rcd_ClassModel.__init__)


def test_rcd_classmodel_constructor_args():
    sig = inspect.signature(rcd_ClassModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcd_classmodel_has_name():
    assert hasattr(rcd_ClassModel, "name")
    descriptor = None
    for klass in rcd_ClassModel.__mro__:
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



def test_rcd_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(rcd_PrimitiveDataType)


def test_rcd_primitivedatatype_constructor_exists():
    assert callable(rcd_PrimitiveDataType.__init__)


def test_rcd_primitivedatatype_constructor_args():
    sig = inspect.signature(rcd_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_rcd_attribute_is_not_abstract():
    assert not inspect.isabstract(rcd_Attribute)


def test_rcd_attribute_constructor_exists():
    assert callable(rcd_Attribute.__init__)


def test_rcd_attribute_constructor_args():
    sig = inspect.signature(rcd_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "name" in params, "Missing parameter 'name'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "is_primary" in params, "Missing parameter 'is_primary'"

def test_rcd_attribute_has_upper():
    assert hasattr(rcd_Attribute, "upper")
    descriptor = None
    for klass in rcd_Attribute.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_rcd_attribute_has_name():
    assert hasattr(rcd_Attribute, "name")
    descriptor = None
    for klass in rcd_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rcd_attribute_has_lower():
    assert hasattr(rcd_Attribute, "lower")
    descriptor = None
    for klass in rcd_Attribute.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_rcd_attribute_has_is_primary():
    assert hasattr(rcd_Attribute, "is_primary")
    descriptor = None
    for klass in rcd_Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)



def test_rcd_class_is_not_abstract():
    assert not inspect.isabstract(rcd_Class)


def test_rcd_class_constructor_exists():
    assert callable(rcd_Class.__init__)


def test_rcd_class_constructor_args():
    sig = inspect.signature(rcd_Class.__init__)
    params = list(sig.parameters.keys())
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_rcd_class_has_is_persistent():
    assert hasattr(rcd_Class, "is_persistent")
    descriptor = None
    for klass in rcd_Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_rcd_association_is_not_abstract():
    assert not inspect.isabstract(rcd_Association)


def test_rcd_association_constructor_exists():
    assert callable(rcd_Association.__init__)


def test_rcd_association_constructor_args():
    sig = inspect.signature(rcd_Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_rcd_association_has_name():
    assert hasattr(rcd_Association, "name")
    descriptor = None
    for klass in rcd_Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rcd_association_has_lower():
    assert hasattr(rcd_Association, "lower")
    descriptor = None
    for klass in rcd_Association.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_rcd_association_has_upper():
    assert hasattr(rcd_Association, "upper")
    descriptor = None
    for klass in rcd_Association.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_rcd_classifier_is_not_abstract():
    assert not inspect.isabstract(rcd_Classifier)


def test_rcd_classifier_constructor_exists():
    assert callable(rcd_Classifier.__init__)


def test_rcd_classifier_constructor_args():
    sig = inspect.signature(rcd_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcd_classifier_has_name():
    assert hasattr(rcd_Classifier, "name")
    descriptor = None
    for klass in rcd_Classifier.__mro__:
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
rcd_ClassModel_strategy = st.builds(
    rcd_ClassModel,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
rcd_PrimitiveDataType_strategy = st.builds(
    rcd_PrimitiveDataType,
)
rcd_Attribute_strategy = st.builds(
    rcd_Attribute,
    upper=
        safe_text,
    name=
        safe_text,
    lower=
        safe_text,
    is_primary=
        st.booleans()
)
rcd_Class_strategy = st.builds(
    rcd_Class,
    is_persistent=
        st.booleans()
)
rcd_Association_strategy = st.builds(
    rcd_Association,
    name=
        safe_text,
    lower=
        safe_text,
    upper=
        safe_text
)
rcd_Classifier_strategy = st.builds(
    rcd_Classifier,
    name=
        safe_text
)

@given(instance=rcd_ClassModel_strategy)
@settings(max_examples=50)
def test_rcd_classmodel_instantiation(instance):
    assert isinstance(instance, rcd_ClassModel)



@given(instance=rcd_ClassModel_strategy)
def test_rcd_classmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=rcd_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_rcd_primitivedatatype_instantiation(instance):
    assert isinstance(instance, rcd_PrimitiveDataType)

@given(instance=rcd_Attribute_strategy)
@settings(max_examples=50)
def test_rcd_attribute_instantiation(instance):
    assert isinstance(instance, rcd_Attribute)



@given(instance=rcd_Attribute_strategy)
def test_rcd_attribute_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=rcd_Attribute_strategy)
def test_rcd_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rcd_Attribute_strategy)
def test_rcd_attribute_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=rcd_Attribute_strategy)
def test_rcd_attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=rcd_Class_strategy)
@settings(max_examples=50)
def test_rcd_class_instantiation(instance):
    assert isinstance(instance, rcd_Class)



@given(instance=rcd_Class_strategy)
def test_rcd_class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=rcd_Association_strategy)
@settings(max_examples=50)
def test_rcd_association_instantiation(instance):
    assert isinstance(instance, rcd_Association)



@given(instance=rcd_Association_strategy)
def test_rcd_association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rcd_Association_strategy)
def test_rcd_association_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=rcd_Association_strategy)
def test_rcd_association_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=rcd_Classifier_strategy)
@settings(max_examples=50)
def test_rcd_classifier_instantiation(instance):
    assert isinstance(instance, rcd_Classifier)



@given(instance=rcd_Classifier_strategy)
def test_rcd_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

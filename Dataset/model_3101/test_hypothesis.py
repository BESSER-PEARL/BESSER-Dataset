import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rcd::ClassModel,
    Classifier,
    rcd::PrimitiveDataType,
    rcd::Attribute,
    rcd::Class,
    rcd::Association,
    rcd::Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rcd::classmodel_is_not_abstract():
    assert not inspect.isabstract(rcd::ClassModel)


def test_rcd::classmodel_constructor_exists():
    assert callable(rcd::ClassModel.__init__)


def test_rcd::classmodel_constructor_args():
    sig = inspect.signature(rcd::ClassModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcd::classmodel_has_name():
    assert hasattr(rcd::ClassModel, "name")
    descriptor = None
    for klass in rcd::ClassModel.__mro__:
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



def test_rcd::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(rcd::PrimitiveDataType)


def test_rcd::primitivedatatype_constructor_exists():
    assert callable(rcd::PrimitiveDataType.__init__)


def test_rcd::primitivedatatype_constructor_args():
    sig = inspect.signature(rcd::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_rcd::attribute_is_not_abstract():
    assert not inspect.isabstract(rcd::Attribute)


def test_rcd::attribute_constructor_exists():
    assert callable(rcd::Attribute.__init__)


def test_rcd::attribute_constructor_args():
    sig = inspect.signature(rcd::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "is_primary" in params, "Missing parameter 'is_primary'"
    assert "name" in params, "Missing parameter 'name'"

def test_rcd::attribute_has_lower():
    assert hasattr(rcd::Attribute, "lower")
    descriptor = None
    for klass in rcd::Attribute.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_rcd::attribute_has_upper():
    assert hasattr(rcd::Attribute, "upper")
    descriptor = None
    for klass in rcd::Attribute.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_rcd::attribute_has_is_primary():
    assert hasattr(rcd::Attribute, "is_primary")
    descriptor = None
    for klass in rcd::Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)

def test_rcd::attribute_has_name():
    assert hasattr(rcd::Attribute, "name")
    descriptor = None
    for klass in rcd::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rcd::class_is_not_abstract():
    assert not inspect.isabstract(rcd::Class)


def test_rcd::class_constructor_exists():
    assert callable(rcd::Class.__init__)


def test_rcd::class_constructor_args():
    sig = inspect.signature(rcd::Class.__init__)
    params = list(sig.parameters.keys())
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_rcd::class_has_is_persistent():
    assert hasattr(rcd::Class, "is_persistent")
    descriptor = None
    for klass in rcd::Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_rcd::association_is_not_abstract():
    assert not inspect.isabstract(rcd::Association)


def test_rcd::association_constructor_exists():
    assert callable(rcd::Association.__init__)


def test_rcd::association_constructor_args():
    sig = inspect.signature(rcd::Association.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "name" in params, "Missing parameter 'name'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_rcd::association_has_lower():
    assert hasattr(rcd::Association, "lower")
    descriptor = None
    for klass in rcd::Association.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_rcd::association_has_name():
    assert hasattr(rcd::Association, "name")
    descriptor = None
    for klass in rcd::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rcd::association_has_upper():
    assert hasattr(rcd::Association, "upper")
    descriptor = None
    for klass in rcd::Association.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_rcd::classifier_is_not_abstract():
    assert not inspect.isabstract(rcd::Classifier)


def test_rcd::classifier_constructor_exists():
    assert callable(rcd::Classifier.__init__)


def test_rcd::classifier_constructor_args():
    sig = inspect.signature(rcd::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rcd::classifier_has_name():
    assert hasattr(rcd::Classifier, "name")
    descriptor = None
    for klass in rcd::Classifier.__mro__:
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
rcd::ClassModel_strategy = st.builds(
    rcd::ClassModel,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
rcd::PrimitiveDataType_strategy = st.builds(
    rcd::PrimitiveDataType,
)
rcd::Attribute_strategy = st.builds(
    rcd::Attribute,
    lower=
        safe_text,
    upper=
        safe_text,
    is_primary=
        st.booleans(),
    name=
        safe_text
)
rcd::Class_strategy = st.builds(
    rcd::Class,
    is_persistent=
        st.booleans()
)
rcd::Association_strategy = st.builds(
    rcd::Association,
    lower=
        safe_text,
    name=
        safe_text,
    upper=
        safe_text
)
rcd::Classifier_strategy = st.builds(
    rcd::Classifier,
    name=
        safe_text
)

@given(instance=rcd::ClassModel_strategy)
@settings(max_examples=50)
def test_rcd::classmodel_instantiation(instance):
    assert isinstance(instance, rcd::ClassModel)

@given(instance=rcd::ClassModel_strategy)
def test_rcd::classmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rcd::ClassModel_strategy)
def test_rcd::classmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=rcd::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_rcd::primitivedatatype_instantiation(instance):
    assert isinstance(instance, rcd::PrimitiveDataType)

@given(instance=rcd::Attribute_strategy)
@settings(max_examples=50)
def test_rcd::attribute_instantiation(instance):
    assert isinstance(instance, rcd::Attribute)

@given(instance=rcd::Attribute_strategy)
def test_rcd::attribute_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=rcd::Attribute_strategy)
def test_rcd::attribute_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=rcd::Attribute_strategy)
def test_rcd::attribute_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=rcd::Attribute_strategy)
def test_rcd::attribute_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=rcd::Attribute_strategy)
def test_rcd::attribute_is_primary_type(instance):
    assert isinstance(instance.is_primary, bool)


@given(instance=rcd::Attribute_strategy)
def test_rcd::attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=rcd::Attribute_strategy)
def test_rcd::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rcd::Attribute_strategy)
def test_rcd::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rcd::Class_strategy)
@settings(max_examples=50)
def test_rcd::class_instantiation(instance):
    assert isinstance(instance, rcd::Class)

@given(instance=rcd::Class_strategy)
def test_rcd::class_is_persistent_type(instance):
    assert isinstance(instance.is_persistent, bool)


@given(instance=rcd::Class_strategy)
def test_rcd::class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=rcd::Association_strategy)
@settings(max_examples=50)
def test_rcd::association_instantiation(instance):
    assert isinstance(instance, rcd::Association)

@given(instance=rcd::Association_strategy)
def test_rcd::association_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=rcd::Association_strategy)
def test_rcd::association_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=rcd::Association_strategy)
def test_rcd::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rcd::Association_strategy)
def test_rcd::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rcd::Association_strategy)
def test_rcd::association_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=rcd::Association_strategy)
def test_rcd::association_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=rcd::Classifier_strategy)
@settings(max_examples=50)
def test_rcd::classifier_instantiation(instance):
    assert isinstance(instance, rcd::Classifier)

@given(instance=rcd::Classifier_strategy)
def test_rcd::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rcd::Classifier_strategy)
def test_rcd::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

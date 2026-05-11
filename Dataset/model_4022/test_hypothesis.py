import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Classifier,
    classmm::Class,
    classmm::DataType,
    NamedElt,
    classmm::Parameter,
    classmm::Package,
    classmm::Method,
    classmm::Attribute,
    classmm::Classifier,
    classmm::NamedElt,
    Visibility,
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



def test_classmm::class_is_not_abstract():
    assert not inspect.isabstract(classmm::Class)


def test_classmm::class_constructor_exists():
    assert callable(classmm::Class.__init__)


def test_classmm::class_constructor_args():
    sig = inspect.signature(classmm::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_classmm::class_has_isAbstract():
    assert hasattr(classmm::Class, "isAbstract")
    descriptor = None
    for klass in classmm::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_classmm::class_has_visibility():
    assert hasattr(classmm::Class, "visibility")
    descriptor = None
    for klass in classmm::Class.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_classmm::datatype_is_not_abstract():
    assert not inspect.isabstract(classmm::DataType)


def test_classmm::datatype_constructor_exists():
    assert callable(classmm::DataType.__init__)


def test_classmm::datatype_constructor_args():
    sig = inspect.signature(classmm::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_classmm::parameter_is_not_abstract():
    assert not inspect.isabstract(classmm::Parameter)


def test_classmm::parameter_constructor_exists():
    assert callable(classmm::Parameter.__init__)


def test_classmm::parameter_constructor_args():
    sig = inspect.signature(classmm::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_classmm::package_is_not_abstract():
    assert not inspect.isabstract(classmm::Package)


def test_classmm::package_constructor_exists():
    assert callable(classmm::Package.__init__)


def test_classmm::package_constructor_args():
    sig = inspect.signature(classmm::Package.__init__)
    params = list(sig.parameters.keys())



def test_classmm::method_is_not_abstract():
    assert not inspect.isabstract(classmm::Method)


def test_classmm::method_constructor_exists():
    assert callable(classmm::Method.__init__)


def test_classmm::method_constructor_args():
    sig = inspect.signature(classmm::Method.__init__)
    params = list(sig.parameters.keys())



def test_classmm::attribute_is_not_abstract():
    assert not inspect.isabstract(classmm::Attribute)


def test_classmm::attribute_constructor_exists():
    assert callable(classmm::Attribute.__init__)


def test_classmm::attribute_constructor_args():
    sig = inspect.signature(classmm::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_classmm::attribute_has_multivalued():
    assert hasattr(classmm::Attribute, "multivalued")
    descriptor = None
    for klass in classmm::Attribute.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)

def test_classmm::attribute_has_visibility():
    assert hasattr(classmm::Attribute, "visibility")
    descriptor = None
    for klass in classmm::Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_classmm::classifier_is_not_abstract():
    assert not inspect.isabstract(classmm::Classifier)


def test_classmm::classifier_constructor_exists():
    assert callable(classmm::Classifier.__init__)


def test_classmm::classifier_constructor_args():
    sig = inspect.signature(classmm::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classmm::namedelt_is_not_abstract():
    assert not inspect.isabstract(classmm::NamedElt)


def test_classmm::namedelt_constructor_exists():
    assert callable(classmm::NamedElt.__init__)


def test_classmm::namedelt_constructor_args():
    sig = inspect.signature(classmm::NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmm::namedelt_has_name():
    assert hasattr(classmm::NamedElt, "name")
    descriptor = None
    for klass in classmm::NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "public",
        "protected",
        "package",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"


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
classmm::Class_strategy = st.builds(
    classmm::Class,
    isAbstract=
        st.booleans(),
    visibility=
        safe_text
)
classmm::DataType_strategy = st.builds(
    classmm::DataType,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
classmm::Parameter_strategy = st.builds(
    classmm::Parameter,
)
classmm::Package_strategy = st.builds(
    classmm::Package,
)
classmm::Method_strategy = st.builds(
    classmm::Method,
)
classmm::Attribute_strategy = st.builds(
    classmm::Attribute,
    multivalued=
        st.booleans(),
    visibility=
        safe_text
)
classmm::Classifier_strategy = st.builds(
    classmm::Classifier,
)
classmm::NamedElt_strategy = st.builds(
    classmm::NamedElt,
    name=
        safe_text
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=classmm::Class_strategy)
@settings(max_examples=50)
def test_classmm::class_instantiation(instance):
    assert isinstance(instance, classmm::Class)

@given(instance=classmm::Class_strategy)
def test_classmm::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=classmm::Class_strategy)
def test_classmm::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=classmm::Class_strategy)
def test_classmm::class_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=classmm::Class_strategy)
def test_classmm::class_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=classmm::DataType_strategy)
@settings(max_examples=50)
def test_classmm::datatype_instantiation(instance):
    assert isinstance(instance, classmm::DataType)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=classmm::Parameter_strategy)
@settings(max_examples=50)
def test_classmm::parameter_instantiation(instance):
    assert isinstance(instance, classmm::Parameter)

@given(instance=classmm::Package_strategy)
@settings(max_examples=50)
def test_classmm::package_instantiation(instance):
    assert isinstance(instance, classmm::Package)

@given(instance=classmm::Method_strategy)
@settings(max_examples=50)
def test_classmm::method_instantiation(instance):
    assert isinstance(instance, classmm::Method)

@given(instance=classmm::Attribute_strategy)
@settings(max_examples=50)
def test_classmm::attribute_instantiation(instance):
    assert isinstance(instance, classmm::Attribute)

@given(instance=classmm::Attribute_strategy)
def test_classmm::attribute_multivalued_type(instance):
    assert isinstance(instance.multivalued, bool)


@given(instance=classmm::Attribute_strategy)
def test_classmm::attribute_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=classmm::Attribute_strategy)
def test_classmm::attribute_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=classmm::Attribute_strategy)
def test_classmm::attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=classmm::Classifier_strategy)
@settings(max_examples=50)
def test_classmm::classifier_instantiation(instance):
    assert isinstance(instance, classmm::Classifier)

@given(instance=classmm::NamedElt_strategy)
@settings(max_examples=50)
def test_classmm::namedelt_instantiation(instance):
    assert isinstance(instance, classmm::NamedElt)

@given(instance=classmm::NamedElt_strategy)
def test_classmm::namedelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classmm::NamedElt_strategy)
def test_classmm::namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

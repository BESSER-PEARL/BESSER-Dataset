import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Classifier,
    classmm_Class,
    classmm_DataType,
    NamedElt,
    classmm_Attribute,
    classmm_Package,
    classmm_Parameter,
    classmm_Method,
    classmm_Classifier,
    classmm_NamedElt,
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



def test_classmm_class_is_not_abstract():
    assert not inspect.isabstract(classmm_Class)


def test_classmm_class_constructor_exists():
    assert callable(classmm_Class.__init__)


def test_classmm_class_constructor_args():
    sig = inspect.signature(classmm_Class.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_classmm_class_has_visibility():
    assert hasattr(classmm_Class, "visibility")
    descriptor = None
    for klass in classmm_Class.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_classmm_class_has_isAbstract():
    assert hasattr(classmm_Class, "isAbstract")
    descriptor = None
    for klass in classmm_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_classmm_datatype_is_not_abstract():
    assert not inspect.isabstract(classmm_DataType)


def test_classmm_datatype_constructor_exists():
    assert callable(classmm_DataType.__init__)


def test_classmm_datatype_constructor_args():
    sig = inspect.signature(classmm_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_classmm_attribute_is_not_abstract():
    assert not inspect.isabstract(classmm_Attribute)


def test_classmm_attribute_constructor_exists():
    assert callable(classmm_Attribute.__init__)


def test_classmm_attribute_constructor_args():
    sig = inspect.signature(classmm_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_classmm_attribute_has_multivalued():
    assert hasattr(classmm_Attribute, "multivalued")
    descriptor = None
    for klass in classmm_Attribute.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)

def test_classmm_attribute_has_visibility():
    assert hasattr(classmm_Attribute, "visibility")
    descriptor = None
    for klass in classmm_Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_classmm_package_is_not_abstract():
    assert not inspect.isabstract(classmm_Package)


def test_classmm_package_constructor_exists():
    assert callable(classmm_Package.__init__)


def test_classmm_package_constructor_args():
    sig = inspect.signature(classmm_Package.__init__)
    params = list(sig.parameters.keys())



def test_classmm_parameter_is_not_abstract():
    assert not inspect.isabstract(classmm_Parameter)


def test_classmm_parameter_constructor_exists():
    assert callable(classmm_Parameter.__init__)


def test_classmm_parameter_constructor_args():
    sig = inspect.signature(classmm_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_classmm_method_is_not_abstract():
    assert not inspect.isabstract(classmm_Method)


def test_classmm_method_constructor_exists():
    assert callable(classmm_Method.__init__)


def test_classmm_method_constructor_args():
    sig = inspect.signature(classmm_Method.__init__)
    params = list(sig.parameters.keys())



def test_classmm_classifier_is_not_abstract():
    assert not inspect.isabstract(classmm_Classifier)


def test_classmm_classifier_constructor_exists():
    assert callable(classmm_Classifier.__init__)


def test_classmm_classifier_constructor_args():
    sig = inspect.signature(classmm_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classmm_namedelt_is_not_abstract():
    assert not inspect.isabstract(classmm_NamedElt)


def test_classmm_namedelt_constructor_exists():
    assert callable(classmm_NamedElt.__init__)


def test_classmm_namedelt_constructor_args():
    sig = inspect.signature(classmm_NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmm_namedelt_has_name():
    assert hasattr(classmm_NamedElt, "name")
    descriptor = None
    for klass in classmm_NamedElt.__mro__:
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
        "private",
        "package",
        "protected",
        "public",
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
classmm_Class_strategy = st.builds(
    classmm_Class,
    visibility=
        safe_text,
    isAbstract=
        st.booleans()
)
classmm_DataType_strategy = st.builds(
    classmm_DataType,
)
NamedElt_strategy = st.builds(
    NamedElt,
)
classmm_Attribute_strategy = st.builds(
    classmm_Attribute,
    multivalued=
        st.booleans(),
    visibility=
        safe_text
)
classmm_Package_strategy = st.builds(
    classmm_Package,
)
classmm_Parameter_strategy = st.builds(
    classmm_Parameter,
)
classmm_Method_strategy = st.builds(
    classmm_Method,
)
classmm_Classifier_strategy = st.builds(
    classmm_Classifier,
)
classmm_NamedElt_strategy = st.builds(
    classmm_NamedElt,
    name=
        safe_text
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=classmm_Class_strategy)
@settings(max_examples=50)
def test_classmm_class_instantiation(instance):
    assert isinstance(instance, classmm_Class)



@given(instance=classmm_Class_strategy)
def test_classmm_class_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=classmm_Class_strategy)
def test_classmm_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=classmm_DataType_strategy)
@settings(max_examples=50)
def test_classmm_datatype_instantiation(instance):
    assert isinstance(instance, classmm_DataType)

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=classmm_Attribute_strategy)
@settings(max_examples=50)
def test_classmm_attribute_instantiation(instance):
    assert isinstance(instance, classmm_Attribute)



@given(instance=classmm_Attribute_strategy)
def test_classmm_attribute_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original



@given(instance=classmm_Attribute_strategy)
def test_classmm_attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=classmm_Package_strategy)
@settings(max_examples=50)
def test_classmm_package_instantiation(instance):
    assert isinstance(instance, classmm_Package)

@given(instance=classmm_Parameter_strategy)
@settings(max_examples=50)
def test_classmm_parameter_instantiation(instance):
    assert isinstance(instance, classmm_Parameter)

@given(instance=classmm_Method_strategy)
@settings(max_examples=50)
def test_classmm_method_instantiation(instance):
    assert isinstance(instance, classmm_Method)

@given(instance=classmm_Classifier_strategy)
@settings(max_examples=50)
def test_classmm_classifier_instantiation(instance):
    assert isinstance(instance, classmm_Classifier)

@given(instance=classmm_NamedElt_strategy)
@settings(max_examples=50)
def test_classmm_namedelt_instantiation(instance):
    assert isinstance(instance, classmm_NamedElt)



@given(instance=classmm_NamedElt_strategy)
def test_classmm_namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

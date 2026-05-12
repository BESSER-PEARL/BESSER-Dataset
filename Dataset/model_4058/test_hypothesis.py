import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    simple_OO_concept_Behavior,
    simple_OO_concept_Parameter,
    Feature,
    simple_OO_concept_Feature,
    simple_OO_concept_NamedElement,
    simple_OO_concept_Dependency,
    NamedElement,
    simple_OO_concept_Attribute,
    simple_OO_concept_Operation,
    simple_OO_concept_Class,
    simple_OO_concept_Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_simple_oo_concept_behavior_is_not_abstract():
    assert not inspect.isabstract(simple_OO_concept_Behavior)


def test_simple_oo_concept_behavior_constructor_exists():
    assert callable(simple_OO_concept_Behavior.__init__)


def test_simple_oo_concept_behavior_constructor_args():
    sig = inspect.signature(simple_OO_concept_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_simple_oo_concept_parameter_is_not_abstract():
    assert not inspect.isabstract(simple_OO_concept_Parameter)


def test_simple_oo_concept_parameter_constructor_exists():
    assert callable(simple_OO_concept_Parameter.__init__)


def test_simple_oo_concept_parameter_constructor_args():
    sig = inspect.signature(simple_OO_concept_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_simple_oo_concept_feature_is_not_abstract():
    assert not inspect.isabstract(simple_OO_concept_Feature)


def test_simple_oo_concept_feature_constructor_exists():
    assert callable(simple_OO_concept_Feature.__init__)


def test_simple_oo_concept_feature_constructor_args():
    sig = inspect.signature(simple_OO_concept_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isProtected" in params, "Missing parameter 'isProtected'"
    assert "isPrivate" in params, "Missing parameter 'isPrivate'"
    assert "isPublic" in params, "Missing parameter 'isPublic'"

def test_simple_oo_concept_feature_has_isProtected():
    assert hasattr(simple_OO_concept_Feature, "isProtected")
    descriptor = None
    for klass in simple_OO_concept_Feature.__mro__:
        if "isProtected" in klass.__dict__:
            descriptor = klass.__dict__["isProtected"]
            break
    assert isinstance(descriptor, property)

def test_simple_oo_concept_feature_has_isPrivate():
    assert hasattr(simple_OO_concept_Feature, "isPrivate")
    descriptor = None
    for klass in simple_OO_concept_Feature.__mro__:
        if "isPrivate" in klass.__dict__:
            descriptor = klass.__dict__["isPrivate"]
            break
    assert isinstance(descriptor, property)

def test_simple_oo_concept_feature_has_isPublic():
    assert hasattr(simple_OO_concept_Feature, "isPublic")
    descriptor = None
    for klass in simple_OO_concept_Feature.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)



def test_simple_oo_concept_namedelement_is_not_abstract():
    assert not inspect.isabstract(simple_OO_concept_NamedElement)


def test_simple_oo_concept_namedelement_constructor_exists():
    assert callable(simple_OO_concept_NamedElement.__init__)


def test_simple_oo_concept_namedelement_constructor_args():
    sig = inspect.signature(simple_OO_concept_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simple_oo_concept_namedelement_has_name():
    assert hasattr(simple_OO_concept_NamedElement, "name")
    descriptor = None
    for klass in simple_OO_concept_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simple_oo_concept_dependency_is_not_abstract():
    assert not inspect.isabstract(simple_OO_concept_Dependency)


def test_simple_oo_concept_dependency_constructor_exists():
    assert callable(simple_OO_concept_Dependency.__init__)


def test_simple_oo_concept_dependency_constructor_args():
    sig = inspect.signature(simple_OO_concept_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simple_oo_concept_attribute_is_not_abstract():
    assert not inspect.isabstract(simple_OO_concept_Attribute)


def test_simple_oo_concept_attribute_constructor_exists():
    assert callable(simple_OO_concept_Attribute.__init__)


def test_simple_oo_concept_attribute_constructor_args():
    sig = inspect.signature(simple_OO_concept_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_simple_oo_concept_operation_is_not_abstract():
    assert not inspect.isabstract(simple_OO_concept_Operation)


def test_simple_oo_concept_operation_constructor_exists():
    assert callable(simple_OO_concept_Operation.__init__)


def test_simple_oo_concept_operation_constructor_args():
    sig = inspect.signature(simple_OO_concept_Operation.__init__)
    params = list(sig.parameters.keys())



def test_simple_oo_concept_class_is_not_abstract():
    assert not inspect.isabstract(simple_OO_concept_Class)


def test_simple_oo_concept_class_constructor_exists():
    assert callable(simple_OO_concept_Class.__init__)


def test_simple_oo_concept_class_constructor_args():
    sig = inspect.signature(simple_OO_concept_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_simple_oo_concept_class_has_isAbstract():
    assert hasattr(simple_OO_concept_Class, "isAbstract")
    descriptor = None
    for klass in simple_OO_concept_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_simple_oo_concept_package_is_not_abstract():
    assert not inspect.isabstract(simple_OO_concept_Package)


def test_simple_oo_concept_package_constructor_exists():
    assert callable(simple_OO_concept_Package.__init__)


def test_simple_oo_concept_package_constructor_args():
    sig = inspect.signature(simple_OO_concept_Package.__init__)
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
Class_strategy = st.builds(
    Class,
)
simple_OO_concept_Behavior_strategy = st.builds(
    simple_OO_concept_Behavior,
)
simple_OO_concept_Parameter_strategy = st.builds(
    simple_OO_concept_Parameter,
)
Feature_strategy = st.builds(
    Feature,
)
simple_OO_concept_Feature_strategy = st.builds(
    simple_OO_concept_Feature,
    isProtected=
        st.booleans(),
    isPrivate=
        st.booleans(),
    isPublic=
        st.booleans()
)
simple_OO_concept_NamedElement_strategy = st.builds(
    simple_OO_concept_NamedElement,
    name=
        safe_text
)
simple_OO_concept_Dependency_strategy = st.builds(
    simple_OO_concept_Dependency,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simple_OO_concept_Attribute_strategy = st.builds(
    simple_OO_concept_Attribute,
)
simple_OO_concept_Operation_strategy = st.builds(
    simple_OO_concept_Operation,
)
simple_OO_concept_Class_strategy = st.builds(
    simple_OO_concept_Class,
    isAbstract=
        st.booleans()
)
simple_OO_concept_Package_strategy = st.builds(
    simple_OO_concept_Package,
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=simple_OO_concept_Behavior_strategy)
@settings(max_examples=50)
def test_simple_oo_concept_behavior_instantiation(instance):
    assert isinstance(instance, simple_OO_concept_Behavior)

@given(instance=simple_OO_concept_Parameter_strategy)
@settings(max_examples=50)
def test_simple_oo_concept_parameter_instantiation(instance):
    assert isinstance(instance, simple_OO_concept_Parameter)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=simple_OO_concept_Feature_strategy)
@settings(max_examples=50)
def test_simple_oo_concept_feature_instantiation(instance):
    assert isinstance(instance, simple_OO_concept_Feature)



@given(instance=simple_OO_concept_Feature_strategy)
def test_simple_oo_concept_feature_isProtected_setter(instance):
    original = instance.isProtected
    instance.isProtected = original
    assert instance.isProtected == original



@given(instance=simple_OO_concept_Feature_strategy)
def test_simple_oo_concept_feature_isPrivate_setter(instance):
    original = instance.isPrivate
    instance.isPrivate = original
    assert instance.isPrivate == original



@given(instance=simple_OO_concept_Feature_strategy)
def test_simple_oo_concept_feature_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=simple_OO_concept_NamedElement_strategy)
@settings(max_examples=50)
def test_simple_oo_concept_namedelement_instantiation(instance):
    assert isinstance(instance, simple_OO_concept_NamedElement)



@given(instance=simple_OO_concept_NamedElement_strategy)
def test_simple_oo_concept_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simple_OO_concept_Dependency_strategy)
@settings(max_examples=50)
def test_simple_oo_concept_dependency_instantiation(instance):
    assert isinstance(instance, simple_OO_concept_Dependency)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simple_OO_concept_Attribute_strategy)
@settings(max_examples=50)
def test_simple_oo_concept_attribute_instantiation(instance):
    assert isinstance(instance, simple_OO_concept_Attribute)

@given(instance=simple_OO_concept_Operation_strategy)
@settings(max_examples=50)
def test_simple_oo_concept_operation_instantiation(instance):
    assert isinstance(instance, simple_OO_concept_Operation)

@given(instance=simple_OO_concept_Class_strategy)
@settings(max_examples=50)
def test_simple_oo_concept_class_instantiation(instance):
    assert isinstance(instance, simple_OO_concept_Class)



@given(instance=simple_OO_concept_Class_strategy)
def test_simple_oo_concept_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=simple_OO_concept_Package_strategy)
@settings(max_examples=50)
def test_simple_oo_concept_package_instantiation(instance):
    assert isinstance(instance, simple_OO_concept_Package)

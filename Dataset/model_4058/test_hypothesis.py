import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Class,
    simple::OO::concept::Behavior,
    simple::OO::concept::Parameter,
    Feature,
    simple::OO::concept::Feature,
    simple::OO::concept::NamedElement,
    simple::OO::concept::Dependency,
    NamedElement,
    simple::OO::concept::Attribute,
    simple::OO::concept::Operation,
    simple::OO::concept::Class,
    simple::OO::concept::Package,
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



def test_simple::oo::concept::behavior_is_not_abstract():
    assert not inspect.isabstract(simple::OO::concept::Behavior)


def test_simple::oo::concept::behavior_constructor_exists():
    assert callable(simple::OO::concept::Behavior.__init__)


def test_simple::oo::concept::behavior_constructor_args():
    sig = inspect.signature(simple::OO::concept::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_simple::oo::concept::parameter_is_not_abstract():
    assert not inspect.isabstract(simple::OO::concept::Parameter)


def test_simple::oo::concept::parameter_constructor_exists():
    assert callable(simple::OO::concept::Parameter.__init__)


def test_simple::oo::concept::parameter_constructor_args():
    sig = inspect.signature(simple::OO::concept::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_simple::oo::concept::feature_is_not_abstract():
    assert not inspect.isabstract(simple::OO::concept::Feature)


def test_simple::oo::concept::feature_constructor_exists():
    assert callable(simple::OO::concept::Feature.__init__)


def test_simple::oo::concept::feature_constructor_args():
    sig = inspect.signature(simple::OO::concept::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "isProtected" in params, "Missing parameter 'isProtected'"
    assert "isPrivate" in params, "Missing parameter 'isPrivate'"

def test_simple::oo::concept::feature_has_isPublic():
    assert hasattr(simple::OO::concept::Feature, "isPublic")
    descriptor = None
    for klass in simple::OO::concept::Feature.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_simple::oo::concept::feature_has_isProtected():
    assert hasattr(simple::OO::concept::Feature, "isProtected")
    descriptor = None
    for klass in simple::OO::concept::Feature.__mro__:
        if "isProtected" in klass.__dict__:
            descriptor = klass.__dict__["isProtected"]
            break
    assert isinstance(descriptor, property)

def test_simple::oo::concept::feature_has_isPrivate():
    assert hasattr(simple::OO::concept::Feature, "isPrivate")
    descriptor = None
    for klass in simple::OO::concept::Feature.__mro__:
        if "isPrivate" in klass.__dict__:
            descriptor = klass.__dict__["isPrivate"]
            break
    assert isinstance(descriptor, property)



def test_simple::oo::concept::namedelement_is_not_abstract():
    assert not inspect.isabstract(simple::OO::concept::NamedElement)


def test_simple::oo::concept::namedelement_constructor_exists():
    assert callable(simple::OO::concept::NamedElement.__init__)


def test_simple::oo::concept::namedelement_constructor_args():
    sig = inspect.signature(simple::OO::concept::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simple::oo::concept::namedelement_has_name():
    assert hasattr(simple::OO::concept::NamedElement, "name")
    descriptor = None
    for klass in simple::OO::concept::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simple::oo::concept::dependency_is_not_abstract():
    assert not inspect.isabstract(simple::OO::concept::Dependency)


def test_simple::oo::concept::dependency_constructor_exists():
    assert callable(simple::OO::concept::Dependency.__init__)


def test_simple::oo::concept::dependency_constructor_args():
    sig = inspect.signature(simple::OO::concept::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simple::oo::concept::attribute_is_not_abstract():
    assert not inspect.isabstract(simple::OO::concept::Attribute)


def test_simple::oo::concept::attribute_constructor_exists():
    assert callable(simple::OO::concept::Attribute.__init__)


def test_simple::oo::concept::attribute_constructor_args():
    sig = inspect.signature(simple::OO::concept::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_simple::oo::concept::operation_is_not_abstract():
    assert not inspect.isabstract(simple::OO::concept::Operation)


def test_simple::oo::concept::operation_constructor_exists():
    assert callable(simple::OO::concept::Operation.__init__)


def test_simple::oo::concept::operation_constructor_args():
    sig = inspect.signature(simple::OO::concept::Operation.__init__)
    params = list(sig.parameters.keys())



def test_simple::oo::concept::class_is_not_abstract():
    assert not inspect.isabstract(simple::OO::concept::Class)


def test_simple::oo::concept::class_constructor_exists():
    assert callable(simple::OO::concept::Class.__init__)


def test_simple::oo::concept::class_constructor_args():
    sig = inspect.signature(simple::OO::concept::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_simple::oo::concept::class_has_isAbstract():
    assert hasattr(simple::OO::concept::Class, "isAbstract")
    descriptor = None
    for klass in simple::OO::concept::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_simple::oo::concept::package_is_not_abstract():
    assert not inspect.isabstract(simple::OO::concept::Package)


def test_simple::oo::concept::package_constructor_exists():
    assert callable(simple::OO::concept::Package.__init__)


def test_simple::oo::concept::package_constructor_args():
    sig = inspect.signature(simple::OO::concept::Package.__init__)
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
simple::OO::concept::Behavior_strategy = st.builds(
    simple::OO::concept::Behavior,
)
simple::OO::concept::Parameter_strategy = st.builds(
    simple::OO::concept::Parameter,
)
Feature_strategy = st.builds(
    Feature,
)
simple::OO::concept::Feature_strategy = st.builds(
    simple::OO::concept::Feature,
    isPublic=
        st.booleans(),
    isProtected=
        st.booleans(),
    isPrivate=
        st.booleans()
)
simple::OO::concept::NamedElement_strategy = st.builds(
    simple::OO::concept::NamedElement,
    name=
        safe_text
)
simple::OO::concept::Dependency_strategy = st.builds(
    simple::OO::concept::Dependency,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simple::OO::concept::Attribute_strategy = st.builds(
    simple::OO::concept::Attribute,
)
simple::OO::concept::Operation_strategy = st.builds(
    simple::OO::concept::Operation,
)
simple::OO::concept::Class_strategy = st.builds(
    simple::OO::concept::Class,
    isAbstract=
        st.booleans()
)
simple::OO::concept::Package_strategy = st.builds(
    simple::OO::concept::Package,
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=simple::OO::concept::Behavior_strategy)
@settings(max_examples=50)
def test_simple::oo::concept::behavior_instantiation(instance):
    assert isinstance(instance, simple::OO::concept::Behavior)

@given(instance=simple::OO::concept::Parameter_strategy)
@settings(max_examples=50)
def test_simple::oo::concept::parameter_instantiation(instance):
    assert isinstance(instance, simple::OO::concept::Parameter)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=simple::OO::concept::Feature_strategy)
@settings(max_examples=50)
def test_simple::oo::concept::feature_instantiation(instance):
    assert isinstance(instance, simple::OO::concept::Feature)

@given(instance=simple::OO::concept::Feature_strategy)
def test_simple::oo::concept::feature_isPublic_type(instance):
    assert isinstance(instance.isPublic, bool)


@given(instance=simple::OO::concept::Feature_strategy)
def test_simple::oo::concept::feature_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=simple::OO::concept::Feature_strategy)
def test_simple::oo::concept::feature_isProtected_type(instance):
    assert isinstance(instance.isProtected, bool)


@given(instance=simple::OO::concept::Feature_strategy)
def test_simple::oo::concept::feature_isProtected_setter(instance):
    original = instance.isProtected
    instance.isProtected = original
    assert instance.isProtected == original

@given(instance=simple::OO::concept::Feature_strategy)
def test_simple::oo::concept::feature_isPrivate_type(instance):
    assert isinstance(instance.isPrivate, bool)


@given(instance=simple::OO::concept::Feature_strategy)
def test_simple::oo::concept::feature_isPrivate_setter(instance):
    original = instance.isPrivate
    instance.isPrivate = original
    assert instance.isPrivate == original

@given(instance=simple::OO::concept::NamedElement_strategy)
@settings(max_examples=50)
def test_simple::oo::concept::namedelement_instantiation(instance):
    assert isinstance(instance, simple::OO::concept::NamedElement)

@given(instance=simple::OO::concept::NamedElement_strategy)
def test_simple::oo::concept::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simple::OO::concept::NamedElement_strategy)
def test_simple::oo::concept::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simple::OO::concept::Dependency_strategy)
@settings(max_examples=50)
def test_simple::oo::concept::dependency_instantiation(instance):
    assert isinstance(instance, simple::OO::concept::Dependency)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simple::OO::concept::Attribute_strategy)
@settings(max_examples=50)
def test_simple::oo::concept::attribute_instantiation(instance):
    assert isinstance(instance, simple::OO::concept::Attribute)

@given(instance=simple::OO::concept::Operation_strategy)
@settings(max_examples=50)
def test_simple::oo::concept::operation_instantiation(instance):
    assert isinstance(instance, simple::OO::concept::Operation)

@given(instance=simple::OO::concept::Class_strategy)
@settings(max_examples=50)
def test_simple::oo::concept::class_instantiation(instance):
    assert isinstance(instance, simple::OO::concept::Class)

@given(instance=simple::OO::concept::Class_strategy)
def test_simple::oo::concept::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=simple::OO::concept::Class_strategy)
def test_simple::oo::concept::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=simple::OO::concept::Package_strategy)
@settings(max_examples=50)
def test_simple::oo::concept::package_instantiation(instance):
    assert isinstance(instance, simple::OO::concept::Package)

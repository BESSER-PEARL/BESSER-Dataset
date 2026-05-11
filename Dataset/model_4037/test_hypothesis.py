import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Class,
    uml::Element,
    Type,
    PackageableElement,
    uml::Type,
    Classifier,
    uml::Class,
    Package,
    uml::Model,
    TypedElement,
    uml::Behavior,
    NamedElement,
    uml::Feature,
    uml::TypedElement,
    Feature,
    Element,
    uml::Dependency,
    uml::Package,
    uml::Parameter,
    uml::NamedElement,
    uml::PackageableElement,
    uml::Property,
    uml::Classifier,
    uml::Operation,
    VisibilityKind,
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



def test_uml::element_is_not_abstract():
    assert not inspect.isabstract(uml::Element)


def test_uml::element_constructor_exists():
    assert callable(uml::Element.__init__)


def test_uml::element_constructor_args():
    sig = inspect.signature(uml::Element.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::type_is_not_abstract():
    assert not inspect.isabstract(uml::Type)


def test_uml::type_constructor_exists():
    assert callable(uml::Type.__init__)


def test_uml::type_constructor_args():
    sig = inspect.signature(uml::Type.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::class_is_not_abstract():
    assert not inspect.isabstract(uml::Class)


def test_uml::class_constructor_exists():
    assert callable(uml::Class.__init__)


def test_uml::class_constructor_args():
    sig = inspect.signature(uml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_uml::class_has_isAbstract():
    assert hasattr(uml::Class, "isAbstract")
    descriptor = None
    for klass in uml::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_uml::class_has_isLeaf():
    assert hasattr(uml::Class, "isLeaf")
    descriptor = None
    for klass in uml::Class.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_uml::model_is_not_abstract():
    assert not inspect.isabstract(uml::Model)


def test_uml::model_constructor_exists():
    assert callable(uml::Model.__init__)


def test_uml::model_constructor_args():
    sig = inspect.signature(uml::Model.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::behavior_is_not_abstract():
    assert not inspect.isabstract(uml::Behavior)


def test_uml::behavior_constructor_exists():
    assert callable(uml::Behavior.__init__)


def test_uml::behavior_constructor_args():
    sig = inspect.signature(uml::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::feature_is_not_abstract():
    assert not inspect.isabstract(uml::Feature)


def test_uml::feature_constructor_exists():
    assert callable(uml::Feature.__init__)


def test_uml::feature_constructor_args():
    sig = inspect.signature(uml::Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml::typedelement_is_not_abstract():
    assert not inspect.isabstract(uml::TypedElement)


def test_uml::typedelement_constructor_exists():
    assert callable(uml::TypedElement.__init__)


def test_uml::typedelement_constructor_args():
    sig = inspect.signature(uml::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml::dependency_is_not_abstract():
    assert not inspect.isabstract(uml::Dependency)


def test_uml::dependency_constructor_exists():
    assert callable(uml::Dependency.__init__)


def test_uml::dependency_constructor_args():
    sig = inspect.signature(uml::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml::package_is_not_abstract():
    assert not inspect.isabstract(uml::Package)


def test_uml::package_constructor_exists():
    assert callable(uml::Package.__init__)


def test_uml::package_constructor_args():
    sig = inspect.signature(uml::Package.__init__)
    params = list(sig.parameters.keys())



def test_uml::parameter_is_not_abstract():
    assert not inspect.isabstract(uml::Parameter)


def test_uml::parameter_constructor_exists():
    assert callable(uml::Parameter.__init__)


def test_uml::parameter_constructor_args():
    sig = inspect.signature(uml::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_uml::namedelement_is_not_abstract():
    assert not inspect.isabstract(uml::NamedElement)


def test_uml::namedelement_constructor_exists():
    assert callable(uml::NamedElement.__init__)


def test_uml::namedelement_constructor_args():
    sig = inspect.signature(uml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml::namedelement_has_name():
    assert hasattr(uml::NamedElement, "name")
    descriptor = None
    for klass in uml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_uml::namedelement_has_visibility():
    assert hasattr(uml::NamedElement, "visibility")
    descriptor = None
    for klass in uml::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_uml::packageableelement_is_not_abstract():
    assert not inspect.isabstract(uml::PackageableElement)


def test_uml::packageableelement_constructor_exists():
    assert callable(uml::PackageableElement.__init__)


def test_uml::packageableelement_constructor_args():
    sig = inspect.signature(uml::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::property_is_not_abstract():
    assert not inspect.isabstract(uml::Property)


def test_uml::property_constructor_exists():
    assert callable(uml::Property.__init__)


def test_uml::property_constructor_args():
    sig = inspect.signature(uml::Property.__init__)
    params = list(sig.parameters.keys())



def test_uml::classifier_is_not_abstract():
    assert not inspect.isabstract(uml::Classifier)


def test_uml::classifier_constructor_exists():
    assert callable(uml::Classifier.__init__)


def test_uml::classifier_constructor_args():
    sig = inspect.signature(uml::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::operation_is_not_abstract():
    assert not inspect.isabstract(uml::Operation)


def test_uml::operation_constructor_exists():
    assert callable(uml::Operation.__init__)


def test_uml::operation_constructor_args():
    sig = inspect.signature(uml::Operation.__init__)
    params = list(sig.parameters.keys())

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "package",
        "protected",
        "public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"


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
uml::Element_strategy = st.builds(
    uml::Element,
)
Type_strategy = st.builds(
    Type,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uml::Type_strategy = st.builds(
    uml::Type,
)
Classifier_strategy = st.builds(
    Classifier,
)
uml::Class_strategy = st.builds(
    uml::Class,
    isAbstract=
        safe_text,
    isLeaf=
        safe_text
)
Package_strategy = st.builds(
    Package,
)
uml::Model_strategy = st.builds(
    uml::Model,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
uml::Behavior_strategy = st.builds(
    uml::Behavior,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml::Feature_strategy = st.builds(
    uml::Feature,
)
uml::TypedElement_strategy = st.builds(
    uml::TypedElement,
)
Feature_strategy = st.builds(
    Feature,
)
Element_strategy = st.builds(
    Element,
)
uml::Dependency_strategy = st.builds(
    uml::Dependency,
)
uml::Package_strategy = st.builds(
    uml::Package,
)
uml::Parameter_strategy = st.builds(
    uml::Parameter,
)
uml::NamedElement_strategy = st.builds(
    uml::NamedElement,
    name=
        safe_text,
    visibility=
        safe_text
)
uml::PackageableElement_strategy = st.builds(
    uml::PackageableElement,
)
uml::Property_strategy = st.builds(
    uml::Property,
)
uml::Classifier_strategy = st.builds(
    uml::Classifier,
)
uml::Operation_strategy = st.builds(
    uml::Operation,
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=uml::Element_strategy)
@settings(max_examples=50)
def test_uml::element_instantiation(instance):
    assert isinstance(instance, uml::Element)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=uml::Type_strategy)
@settings(max_examples=50)
def test_uml::type_instantiation(instance):
    assert isinstance(instance, uml::Type)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=uml::Class_strategy)
@settings(max_examples=50)
def test_uml::class_instantiation(instance):
    assert isinstance(instance, uml::Class)

@given(instance=uml::Class_strategy)
def test_uml::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=uml::Class_strategy)
def test_uml::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=uml::Class_strategy)
def test_uml::class_isLeaf_type(instance):
    assert isinstance(instance.isLeaf, str)


@given(instance=uml::Class_strategy)
def test_uml::class_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=uml::Model_strategy)
@settings(max_examples=50)
def test_uml::model_instantiation(instance):
    assert isinstance(instance, uml::Model)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=uml::Behavior_strategy)
@settings(max_examples=50)
def test_uml::behavior_instantiation(instance):
    assert isinstance(instance, uml::Behavior)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uml::Feature_strategy)
@settings(max_examples=50)
def test_uml::feature_instantiation(instance):
    assert isinstance(instance, uml::Feature)

@given(instance=uml::TypedElement_strategy)
@settings(max_examples=50)
def test_uml::typedelement_instantiation(instance):
    assert isinstance(instance, uml::TypedElement)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=uml::Dependency_strategy)
@settings(max_examples=50)
def test_uml::dependency_instantiation(instance):
    assert isinstance(instance, uml::Dependency)

@given(instance=uml::Package_strategy)
@settings(max_examples=50)
def test_uml::package_instantiation(instance):
    assert isinstance(instance, uml::Package)

@given(instance=uml::Parameter_strategy)
@settings(max_examples=50)
def test_uml::parameter_instantiation(instance):
    assert isinstance(instance, uml::Parameter)

@given(instance=uml::NamedElement_strategy)
@settings(max_examples=50)
def test_uml::namedelement_instantiation(instance):
    assert isinstance(instance, uml::NamedElement)

@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml::PackageableElement_strategy)
@settings(max_examples=50)
def test_uml::packageableelement_instantiation(instance):
    assert isinstance(instance, uml::PackageableElement)

@given(instance=uml::Property_strategy)
@settings(max_examples=50)
def test_uml::property_instantiation(instance):
    assert isinstance(instance, uml::Property)

@given(instance=uml::Classifier_strategy)
@settings(max_examples=50)
def test_uml::classifier_instantiation(instance):
    assert isinstance(instance, uml::Classifier)

@given(instance=uml::Operation_strategy)
@settings(max_examples=50)
def test_uml::operation_instantiation(instance):
    assert isinstance(instance, uml::Operation)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OO::concept::Dependency,
    OO::concept::Generalization,
    StructuralFeature,
    Class,
    OO::concept::Behavior,
    Feature,
    OO::concept::StructuralFeature,
    OO::concept::BehavioralFeature,
    BehavioralFeature,
    TypedElement,
    OO::concept::Parameter,
    Package,
    OO::concept::Model,
    OO::concept::NamedElement,
    OO::concept::Classifier,
    OO::concept::Property,
    OO::concept::Operation,
    Type,
    Classifier,
    NamedElement,
    OO::concept::Feature,
    OO::concept::Type,
    OO::concept::TypedElement,
    PackageableElement,
    OO::concept::Class,
    OO::concept::Package,
    OO::concept::PackageableElement,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oo::concept::dependency_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Dependency)


def test_oo::concept::dependency_constructor_exists():
    assert callable(OO::concept::Dependency.__init__)


def test_oo::concept::dependency_constructor_args():
    sig = inspect.signature(OO::concept::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::generalization_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Generalization)


def test_oo::concept::generalization_constructor_exists():
    assert callable(OO::concept::Generalization.__init__)


def test_oo::concept::generalization_constructor_args():
    sig = inspect.signature(OO::concept::Generalization.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::behavior_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Behavior)


def test_oo::concept::behavior_constructor_exists():
    assert callable(OO::concept::Behavior.__init__)


def test_oo::concept::behavior_constructor_args():
    sig = inspect.signature(OO::concept::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(OO::concept::StructuralFeature)


def test_oo::concept::structuralfeature_constructor_exists():
    assert callable(OO::concept::StructuralFeature.__init__)


def test_oo::concept::structuralfeature_constructor_args():
    sig = inspect.signature(OO::concept::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(OO::concept::BehavioralFeature)


def test_oo::concept::behavioralfeature_constructor_exists():
    assert callable(OO::concept::BehavioralFeature.__init__)


def test_oo::concept::behavioralfeature_constructor_args():
    sig = inspect.signature(OO::concept::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::parameter_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Parameter)


def test_oo::concept::parameter_constructor_exists():
    assert callable(OO::concept::Parameter.__init__)


def test_oo::concept::parameter_constructor_args():
    sig = inspect.signature(OO::concept::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::model_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Model)


def test_oo::concept::model_constructor_exists():
    assert callable(OO::concept::Model.__init__)


def test_oo::concept::model_constructor_args():
    sig = inspect.signature(OO::concept::Model.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::namedelement_is_not_abstract():
    assert not inspect.isabstract(OO::concept::NamedElement)


def test_oo::concept::namedelement_constructor_exists():
    assert callable(OO::concept::NamedElement.__init__)


def test_oo::concept::namedelement_constructor_args():
    sig = inspect.signature(OO::concept::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_oo::concept::namedelement_has_isAbstract():
    assert hasattr(OO::concept::NamedElement, "isAbstract")
    descriptor = None
    for klass in OO::concept::NamedElement.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_oo::concept::namedelement_has_visibility():
    assert hasattr(OO::concept::NamedElement, "visibility")
    descriptor = None
    for klass in OO::concept::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_oo::concept::namedelement_has_name():
    assert hasattr(OO::concept::NamedElement, "name")
    descriptor = None
    for klass in OO::concept::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oo::concept::classifier_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Classifier)


def test_oo::concept::classifier_constructor_exists():
    assert callable(OO::concept::Classifier.__init__)


def test_oo::concept::classifier_constructor_args():
    sig = inspect.signature(OO::concept::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::property_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Property)


def test_oo::concept::property_constructor_exists():
    assert callable(OO::concept::Property.__init__)


def test_oo::concept::property_constructor_args():
    sig = inspect.signature(OO::concept::Property.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::operation_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Operation)


def test_oo::concept::operation_constructor_exists():
    assert callable(OO::concept::Operation.__init__)


def test_oo::concept::operation_constructor_args():
    sig = inspect.signature(OO::concept::Operation.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::feature_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Feature)


def test_oo::concept::feature_constructor_exists():
    assert callable(OO::concept::Feature.__init__)


def test_oo::concept::feature_constructor_args():
    sig = inspect.signature(OO::concept::Feature.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::type_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Type)


def test_oo::concept::type_constructor_exists():
    assert callable(OO::concept::Type.__init__)


def test_oo::concept::type_constructor_args():
    sig = inspect.signature(OO::concept::Type.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::typedelement_is_not_abstract():
    assert not inspect.isabstract(OO::concept::TypedElement)


def test_oo::concept::typedelement_constructor_exists():
    assert callable(OO::concept::TypedElement.__init__)


def test_oo::concept::typedelement_constructor_args():
    sig = inspect.signature(OO::concept::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::class_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Class)


def test_oo::concept::class_constructor_exists():
    assert callable(OO::concept::Class.__init__)


def test_oo::concept::class_constructor_args():
    sig = inspect.signature(OO::concept::Class.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::package_is_not_abstract():
    assert not inspect.isabstract(OO::concept::Package)


def test_oo::concept::package_constructor_exists():
    assert callable(OO::concept::Package.__init__)


def test_oo::concept::package_constructor_args():
    sig = inspect.signature(OO::concept::Package.__init__)
    params = list(sig.parameters.keys())



def test_oo::concept::packageableelement_is_not_abstract():
    assert not inspect.isabstract(OO::concept::PackageableElement)


def test_oo::concept::packageableelement_constructor_exists():
    assert callable(OO::concept::PackageableElement.__init__)


def test_oo::concept::packageableelement_constructor_args():
    sig = inspect.signature(OO::concept::PackageableElement.__init__)
    params = list(sig.parameters.keys())

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "package",
        "private",
        "public",
        "protected",
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
OO::concept::Dependency_strategy = st.builds(
    OO::concept::Dependency,
)
OO::concept::Generalization_strategy = st.builds(
    OO::concept::Generalization,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
Class_strategy = st.builds(
    Class,
)
OO::concept::Behavior_strategy = st.builds(
    OO::concept::Behavior,
)
Feature_strategy = st.builds(
    Feature,
)
OO::concept::StructuralFeature_strategy = st.builds(
    OO::concept::StructuralFeature,
)
OO::concept::BehavioralFeature_strategy = st.builds(
    OO::concept::BehavioralFeature,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
OO::concept::Parameter_strategy = st.builds(
    OO::concept::Parameter,
)
Package_strategy = st.builds(
    Package,
)
OO::concept::Model_strategy = st.builds(
    OO::concept::Model,
)
OO::concept::NamedElement_strategy = st.builds(
    OO::concept::NamedElement,
    isAbstract=
        st.booleans(),
    visibility=
        safe_text,
    name=
        safe_text
)
OO::concept::Classifier_strategy = st.builds(
    OO::concept::Classifier,
)
OO::concept::Property_strategy = st.builds(
    OO::concept::Property,
)
OO::concept::Operation_strategy = st.builds(
    OO::concept::Operation,
)
Type_strategy = st.builds(
    Type,
)
Classifier_strategy = st.builds(
    Classifier,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
OO::concept::Feature_strategy = st.builds(
    OO::concept::Feature,
)
OO::concept::Type_strategy = st.builds(
    OO::concept::Type,
)
OO::concept::TypedElement_strategy = st.builds(
    OO::concept::TypedElement,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
OO::concept::Class_strategy = st.builds(
    OO::concept::Class,
)
OO::concept::Package_strategy = st.builds(
    OO::concept::Package,
)
OO::concept::PackageableElement_strategy = st.builds(
    OO::concept::PackageableElement,
)

@given(instance=OO::concept::Dependency_strategy)
@settings(max_examples=50)
def test_oo::concept::dependency_instantiation(instance):
    assert isinstance(instance, OO::concept::Dependency)

@given(instance=OO::concept::Generalization_strategy)
@settings(max_examples=50)
def test_oo::concept::generalization_instantiation(instance):
    assert isinstance(instance, OO::concept::Generalization)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=OO::concept::Behavior_strategy)
@settings(max_examples=50)
def test_oo::concept::behavior_instantiation(instance):
    assert isinstance(instance, OO::concept::Behavior)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=OO::concept::StructuralFeature_strategy)
@settings(max_examples=50)
def test_oo::concept::structuralfeature_instantiation(instance):
    assert isinstance(instance, OO::concept::StructuralFeature)

@given(instance=OO::concept::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_oo::concept::behavioralfeature_instantiation(instance):
    assert isinstance(instance, OO::concept::BehavioralFeature)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=OO::concept::Parameter_strategy)
@settings(max_examples=50)
def test_oo::concept::parameter_instantiation(instance):
    assert isinstance(instance, OO::concept::Parameter)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=OO::concept::Model_strategy)
@settings(max_examples=50)
def test_oo::concept::model_instantiation(instance):
    assert isinstance(instance, OO::concept::Model)

@given(instance=OO::concept::NamedElement_strategy)
@settings(max_examples=50)
def test_oo::concept::namedelement_instantiation(instance):
    assert isinstance(instance, OO::concept::NamedElement)

@given(instance=OO::concept::NamedElement_strategy)
def test_oo::concept::namedelement_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=OO::concept::NamedElement_strategy)
def test_oo::concept::namedelement_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=OO::concept::NamedElement_strategy)
def test_oo::concept::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=OO::concept::NamedElement_strategy)
def test_oo::concept::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=OO::concept::NamedElement_strategy)
def test_oo::concept::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OO::concept::NamedElement_strategy)
def test_oo::concept::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OO::concept::Classifier_strategy)
@settings(max_examples=50)
def test_oo::concept::classifier_instantiation(instance):
    assert isinstance(instance, OO::concept::Classifier)

@given(instance=OO::concept::Property_strategy)
@settings(max_examples=50)
def test_oo::concept::property_instantiation(instance):
    assert isinstance(instance, OO::concept::Property)

@given(instance=OO::concept::Operation_strategy)
@settings(max_examples=50)
def test_oo::concept::operation_instantiation(instance):
    assert isinstance(instance, OO::concept::Operation)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=OO::concept::Feature_strategy)
@settings(max_examples=50)
def test_oo::concept::feature_instantiation(instance):
    assert isinstance(instance, OO::concept::Feature)

@given(instance=OO::concept::Type_strategy)
@settings(max_examples=50)
def test_oo::concept::type_instantiation(instance):
    assert isinstance(instance, OO::concept::Type)

@given(instance=OO::concept::TypedElement_strategy)
@settings(max_examples=50)
def test_oo::concept::typedelement_instantiation(instance):
    assert isinstance(instance, OO::concept::TypedElement)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=OO::concept::Class_strategy)
@settings(max_examples=50)
def test_oo::concept::class_instantiation(instance):
    assert isinstance(instance, OO::concept::Class)

@given(instance=OO::concept::Package_strategy)
@settings(max_examples=50)
def test_oo::concept::package_instantiation(instance):
    assert isinstance(instance, OO::concept::Package)

@given(instance=OO::concept::PackageableElement_strategy)
@settings(max_examples=50)
def test_oo::concept::packageableelement_instantiation(instance):
    assert isinstance(instance, OO::concept::PackageableElement)

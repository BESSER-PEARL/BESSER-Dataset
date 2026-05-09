import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    uml::Model,
    Feature,
    Namespace,
    uml::BehavioralFeature,
    BehavioralFeature,
    uml::Operation,
    uml::Parameter,
    Dependency,
    uml::Abstraction,
    Abstraction,
    uml::Realization,
    Realization,
    uml::Substitution,
    uml::Feature,
    uml::Property,
    Classifier,
    uml::Class,
    TypedElement,
    Type,
    uml::Classifier,
    DirectedRelationship,
    uml::Generalization,
    uml::PackageImport,
    uml::ElementImport,
    NamedElement,
    uml::TypedElement,
    Relationship,
    uml::Association,
    uml::DirectedRelationship,
    PackageableElement,
    uml::ValueSpecification,
    uml::Type,
    uml::Package,
    uml::Namespace,
    uml::Dependency,
    uml::PackageableElement,
    uml::Element,
    Element,
    uml::NamedElement,
    uml::Relationship,
    uml::Comment,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml::model_is_not_abstract():
    assert not inspect.isabstract(uml::Model)


def test_uml::model_constructor_exists():
    assert callable(uml::Model.__init__)


def test_uml::model_constructor_args():
    sig = inspect.signature(uml::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::model_has_name():
    assert hasattr(uml::Model, "name")
    descriptor = None
    for klass in uml::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(uml::BehavioralFeature)


def test_uml::behavioralfeature_constructor_exists():
    assert callable(uml::BehavioralFeature.__init__)


def test_uml::behavioralfeature_constructor_args():
    sig = inspect.signature(uml::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml::behavioralfeature_has_isAbstract():
    assert hasattr(uml::BehavioralFeature, "isAbstract")
    descriptor = None
    for klass in uml::BehavioralFeature.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml::operation_is_not_abstract():
    assert not inspect.isabstract(uml::Operation)


def test_uml::operation_constructor_exists():
    assert callable(uml::Operation.__init__)


def test_uml::operation_constructor_args():
    sig = inspect.signature(uml::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_uml::operation_has_isOrdered():
    assert hasattr(uml::Operation, "isOrdered")
    descriptor = None
    for klass in uml::Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_uml::operation_has_lower():
    assert hasattr(uml::Operation, "lower")
    descriptor = None
    for klass in uml::Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_uml::operation_has_isUnique():
    assert hasattr(uml::Operation, "isUnique")
    descriptor = None
    for klass in uml::Operation.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_uml::operation_has_upper():
    assert hasattr(uml::Operation, "upper")
    descriptor = None
    for klass in uml::Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml::operation_has_isQuery():
    assert hasattr(uml::Operation, "isQuery")
    descriptor = None
    for klass in uml::Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_uml::parameter_is_not_abstract():
    assert not inspect.isabstract(uml::Parameter)


def test_uml::parameter_constructor_exists():
    assert callable(uml::Parameter.__init__)


def test_uml::parameter_constructor_args():
    sig = inspect.signature(uml::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "isStream" in params, "Missing parameter 'isStream'"
    assert "isException" in params, "Missing parameter 'isException'"
    assert "default" in params, "Missing parameter 'default'"

def test_uml::parameter_has_isStream():
    assert hasattr(uml::Parameter, "isStream")
    descriptor = None
    for klass in uml::Parameter.__mro__:
        if "isStream" in klass.__dict__:
            descriptor = klass.__dict__["isStream"]
            break
    assert isinstance(descriptor, property)

def test_uml::parameter_has_isException():
    assert hasattr(uml::Parameter, "isException")
    descriptor = None
    for klass in uml::Parameter.__mro__:
        if "isException" in klass.__dict__:
            descriptor = klass.__dict__["isException"]
            break
    assert isinstance(descriptor, property)

def test_uml::parameter_has_default():
    assert hasattr(uml::Parameter, "default")
    descriptor = None
    for klass in uml::Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml::abstraction_is_not_abstract():
    assert not inspect.isabstract(uml::Abstraction)


def test_uml::abstraction_constructor_exists():
    assert callable(uml::Abstraction.__init__)


def test_uml::abstraction_constructor_args():
    sig = inspect.signature(uml::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml::realization_is_not_abstract():
    assert not inspect.isabstract(uml::Realization)


def test_uml::realization_constructor_exists():
    assert callable(uml::Realization.__init__)


def test_uml::realization_constructor_args():
    sig = inspect.signature(uml::Realization.__init__)
    params = list(sig.parameters.keys())



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml::substitution_is_not_abstract():
    assert not inspect.isabstract(uml::Substitution)


def test_uml::substitution_constructor_exists():
    assert callable(uml::Substitution.__init__)


def test_uml::substitution_constructor_args():
    sig = inspect.signature(uml::Substitution.__init__)
    params = list(sig.parameters.keys())



def test_uml::feature_is_not_abstract():
    assert not inspect.isabstract(uml::Feature)


def test_uml::feature_constructor_exists():
    assert callable(uml::Feature.__init__)


def test_uml::feature_constructor_args():
    sig = inspect.signature(uml::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_uml::feature_has_isStatic():
    assert hasattr(uml::Feature, "isStatic")
    descriptor = None
    for klass in uml::Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_uml::property_is_not_abstract():
    assert not inspect.isabstract(uml::Property)


def test_uml::property_constructor_exists():
    assert callable(uml::Property.__init__)


def test_uml::property_constructor_args():
    sig = inspect.signature(uml::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::property_has_name():
    assert hasattr(uml::Property, "name")
    descriptor = None
    for klass in uml::Property.__mro__:
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



def test_uml::class_is_not_abstract():
    assert not inspect.isabstract(uml::Class)


def test_uml::class_constructor_exists():
    assert callable(uml::Class.__init__)


def test_uml::class_constructor_args():
    sig = inspect.signature(uml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "name" in params, "Missing parameter 'name'"

def test_uml::class_has_isActive():
    assert hasattr(uml::Class, "isActive")
    descriptor = None
    for klass in uml::Class.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_uml::class_has_name():
    assert hasattr(uml::Class, "name")
    descriptor = None
    for klass in uml::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uml::classifier_is_not_abstract():
    assert not inspect.isabstract(uml::Classifier)


def test_uml::classifier_constructor_exists():
    assert callable(uml::Classifier.__init__)


def test_uml::classifier_constructor_args():
    sig = inspect.signature(uml::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml::classifier_has_isAbstract():
    assert hasattr(uml::Classifier, "isAbstract")
    descriptor = None
    for klass in uml::Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_uml::generalization_is_not_abstract():
    assert not inspect.isabstract(uml::Generalization)


def test_uml::generalization_constructor_exists():
    assert callable(uml::Generalization.__init__)


def test_uml::generalization_constructor_args():
    sig = inspect.signature(uml::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_uml::generalization_has_isSubstitutable():
    assert hasattr(uml::Generalization, "isSubstitutable")
    descriptor = None
    for klass in uml::Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_uml::packageimport_is_not_abstract():
    assert not inspect.isabstract(uml::PackageImport)


def test_uml::packageimport_constructor_exists():
    assert callable(uml::PackageImport.__init__)


def test_uml::packageimport_constructor_args():
    sig = inspect.signature(uml::PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml::packageimport_has_visibility():
    assert hasattr(uml::PackageImport, "visibility")
    descriptor = None
    for klass in uml::PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_uml::elementimport_is_not_abstract():
    assert not inspect.isabstract(uml::ElementImport)


def test_uml::elementimport_constructor_exists():
    assert callable(uml::ElementImport.__init__)


def test_uml::elementimport_constructor_args():
    sig = inspect.signature(uml::ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml::elementimport_has_alias():
    assert hasattr(uml::ElementImport, "alias")
    descriptor = None
    for klass in uml::ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_uml::elementimport_has_visibility():
    assert hasattr(uml::ElementImport, "visibility")
    descriptor = None
    for klass in uml::ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::typedelement_is_not_abstract():
    assert not inspect.isabstract(uml::TypedElement)


def test_uml::typedelement_constructor_exists():
    assert callable(uml::TypedElement.__init__)


def test_uml::typedelement_constructor_args():
    sig = inspect.signature(uml::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml::association_is_not_abstract():
    assert not inspect.isabstract(uml::Association)


def test_uml::association_constructor_exists():
    assert callable(uml::Association.__init__)


def test_uml::association_constructor_args():
    sig = inspect.signature(uml::Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_uml::association_has_isDerived():
    assert hasattr(uml::Association, "isDerived")
    descriptor = None
    for klass in uml::Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_uml::directedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml::DirectedRelationship)


def test_uml::directedrelationship_constructor_exists():
    assert callable(uml::DirectedRelationship.__init__)


def test_uml::directedrelationship_constructor_args():
    sig = inspect.signature(uml::DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::valuespecification_is_not_abstract():
    assert not inspect.isabstract(uml::ValueSpecification)


def test_uml::valuespecification_constructor_exists():
    assert callable(uml::ValueSpecification.__init__)


def test_uml::valuespecification_constructor_args():
    sig = inspect.signature(uml::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::type_is_not_abstract():
    assert not inspect.isabstract(uml::Type)


def test_uml::type_constructor_exists():
    assert callable(uml::Type.__init__)


def test_uml::type_constructor_args():
    sig = inspect.signature(uml::Type.__init__)
    params = list(sig.parameters.keys())



def test_uml::package_is_not_abstract():
    assert not inspect.isabstract(uml::Package)


def test_uml::package_constructor_exists():
    assert callable(uml::Package.__init__)


def test_uml::package_constructor_args():
    sig = inspect.signature(uml::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::package_has_name():
    assert hasattr(uml::Package, "name")
    descriptor = None
    for klass in uml::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml::namespace_is_not_abstract():
    assert not inspect.isabstract(uml::Namespace)


def test_uml::namespace_constructor_exists():
    assert callable(uml::Namespace.__init__)


def test_uml::namespace_constructor_args():
    sig = inspect.signature(uml::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml::dependency_is_not_abstract():
    assert not inspect.isabstract(uml::Dependency)


def test_uml::dependency_constructor_exists():
    assert callable(uml::Dependency.__init__)


def test_uml::dependency_constructor_args():
    sig = inspect.signature(uml::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml::packageableelement_is_not_abstract():
    assert not inspect.isabstract(uml::PackageableElement)


def test_uml::packageableelement_constructor_exists():
    assert callable(uml::PackageableElement.__init__)


def test_uml::packageableelement_constructor_args():
    sig = inspect.signature(uml::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::element_is_not_abstract():
    assert not inspect.isabstract(uml::Element)


def test_uml::element_constructor_exists():
    assert callable(uml::Element.__init__)


def test_uml::element_constructor_args():
    sig = inspect.signature(uml::Element.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml::namedelement_is_not_abstract():
    assert not inspect.isabstract(uml::NamedElement)


def test_uml::namedelement_constructor_exists():
    assert callable(uml::NamedElement.__init__)


def test_uml::namedelement_constructor_args():
    sig = inspect.signature(uml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_uml::namedelement_has_qualifiedName():
    assert hasattr(uml::NamedElement, "qualifiedName")
    descriptor = None
    for klass in uml::NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
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

def test_uml::namedelement_has_name():
    assert hasattr(uml::NamedElement, "name")
    descriptor = None
    for klass in uml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml::relationship_is_not_abstract():
    assert not inspect.isabstract(uml::Relationship)


def test_uml::relationship_constructor_exists():
    assert callable(uml::Relationship.__init__)


def test_uml::relationship_constructor_args():
    sig = inspect.signature(uml::Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml::comment_is_not_abstract():
    assert not inspect.isabstract(uml::Comment)


def test_uml::comment_constructor_exists():
    assert callable(uml::Comment.__init__)


def test_uml::comment_constructor_args():
    sig = inspect.signature(uml::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_uml::comment_has_body():
    assert hasattr(uml::Comment, "body")
    descriptor = None
    for klass in uml::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "public",
        "protected",
        "package",
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
uml::Model_strategy = st.builds(
    uml::Model,
    name=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
Namespace_strategy = st.builds(
    Namespace,
)
uml::BehavioralFeature_strategy = st.builds(
    uml::BehavioralFeature,
    isAbstract=
        safe_text
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
uml::Operation_strategy = st.builds(
    uml::Operation,
    isOrdered=
        safe_text,
    lower=
        safe_text,
    isUnique=
        safe_text,
    upper=
        safe_text,
    isQuery=
        safe_text
)
uml::Parameter_strategy = st.builds(
    uml::Parameter,
    isStream=
        safe_text,
    isException=
        safe_text,
    default=
        safe_text
)
Dependency_strategy = st.builds(
    Dependency,
)
uml::Abstraction_strategy = st.builds(
    uml::Abstraction,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
uml::Realization_strategy = st.builds(
    uml::Realization,
)
Realization_strategy = st.builds(
    Realization,
)
uml::Substitution_strategy = st.builds(
    uml::Substitution,
)
uml::Feature_strategy = st.builds(
    uml::Feature,
    isStatic=
        safe_text
)
uml::Property_strategy = st.builds(
    uml::Property,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
uml::Class_strategy = st.builds(
    uml::Class,
    isActive=
        safe_text,
    name=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
Type_strategy = st.builds(
    Type,
)
uml::Classifier_strategy = st.builds(
    uml::Classifier,
    isAbstract=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
uml::Generalization_strategy = st.builds(
    uml::Generalization,
    isSubstitutable=
        safe_text
)
uml::PackageImport_strategy = st.builds(
    uml::PackageImport,
    visibility=
        safe_text
)
uml::ElementImport_strategy = st.builds(
    uml::ElementImport,
    alias=
        safe_text,
    visibility=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml::TypedElement_strategy = st.builds(
    uml::TypedElement,
)
Relationship_strategy = st.builds(
    Relationship,
)
uml::Association_strategy = st.builds(
    uml::Association,
    isDerived=
        safe_text
)
uml::DirectedRelationship_strategy = st.builds(
    uml::DirectedRelationship,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uml::ValueSpecification_strategy = st.builds(
    uml::ValueSpecification,
)
uml::Type_strategy = st.builds(
    uml::Type,
)
uml::Package_strategy = st.builds(
    uml::Package,
    name=
        safe_text
)
uml::Namespace_strategy = st.builds(
    uml::Namespace,
)
uml::Dependency_strategy = st.builds(
    uml::Dependency,
)
uml::PackageableElement_strategy = st.builds(
    uml::PackageableElement,
)
uml::Element_strategy = st.builds(
    uml::Element,
)
Element_strategy = st.builds(
    Element,
)
uml::NamedElement_strategy = st.builds(
    uml::NamedElement,
    qualifiedName=
        safe_text,
    visibility=
        safe_text,
    name=
        safe_text
)
uml::Relationship_strategy = st.builds(
    uml::Relationship,
)
uml::Comment_strategy = st.builds(
    uml::Comment,
    body=
        safe_text
)

@given(instance=uml::Model_strategy)
@settings(max_examples=50)
def test_uml::model_instantiation(instance):
    assert isinstance(instance, uml::Model)

@given(instance=uml::Model_strategy)
def test_uml::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::Model_strategy)
def test_uml::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=uml::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml::behavioralfeature_instantiation(instance):
    assert isinstance(instance, uml::BehavioralFeature)

@given(instance=uml::BehavioralFeature_strategy)
def test_uml::behavioralfeature_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=uml::BehavioralFeature_strategy)
def test_uml::behavioralfeature_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=uml::Operation_strategy)
@settings(max_examples=50)
def test_uml::operation_instantiation(instance):
    assert isinstance(instance, uml::Operation)

@given(instance=uml::Operation_strategy)
def test_uml::operation_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=uml::Operation_strategy)
def test_uml::operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=uml::Operation_strategy)
def test_uml::operation_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=uml::Operation_strategy)
def test_uml::operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=uml::Operation_strategy)
def test_uml::operation_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=uml::Operation_strategy)
def test_uml::operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=uml::Operation_strategy)
def test_uml::operation_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=uml::Operation_strategy)
def test_uml::operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=uml::Operation_strategy)
def test_uml::operation_isQuery_type(instance):
    assert isinstance(instance.isQuery, str)


@given(instance=uml::Operation_strategy)
def test_uml::operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=uml::Parameter_strategy)
@settings(max_examples=50)
def test_uml::parameter_instantiation(instance):
    assert isinstance(instance, uml::Parameter)

@given(instance=uml::Parameter_strategy)
def test_uml::parameter_isStream_type(instance):
    assert isinstance(instance.isStream, str)


@given(instance=uml::Parameter_strategy)
def test_uml::parameter_isStream_setter(instance):
    original = instance.isStream
    instance.isStream = original
    assert instance.isStream == original

@given(instance=uml::Parameter_strategy)
def test_uml::parameter_isException_type(instance):
    assert isinstance(instance.isException, str)


@given(instance=uml::Parameter_strategy)
def test_uml::parameter_isException_setter(instance):
    original = instance.isException
    instance.isException = original
    assert instance.isException == original

@given(instance=uml::Parameter_strategy)
def test_uml::parameter_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=uml::Parameter_strategy)
def test_uml::parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=uml::Abstraction_strategy)
@settings(max_examples=50)
def test_uml::abstraction_instantiation(instance):
    assert isinstance(instance, uml::Abstraction)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=uml::Realization_strategy)
@settings(max_examples=50)
def test_uml::realization_instantiation(instance):
    assert isinstance(instance, uml::Realization)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=uml::Substitution_strategy)
@settings(max_examples=50)
def test_uml::substitution_instantiation(instance):
    assert isinstance(instance, uml::Substitution)

@given(instance=uml::Feature_strategy)
@settings(max_examples=50)
def test_uml::feature_instantiation(instance):
    assert isinstance(instance, uml::Feature)

@given(instance=uml::Feature_strategy)
def test_uml::feature_isStatic_type(instance):
    assert isinstance(instance.isStatic, str)


@given(instance=uml::Feature_strategy)
def test_uml::feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=uml::Property_strategy)
@settings(max_examples=50)
def test_uml::property_instantiation(instance):
    assert isinstance(instance, uml::Property)

@given(instance=uml::Property_strategy)
def test_uml::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::Property_strategy)
def test_uml::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=uml::Class_strategy)
@settings(max_examples=50)
def test_uml::class_instantiation(instance):
    assert isinstance(instance, uml::Class)

@given(instance=uml::Class_strategy)
def test_uml::class_isActive_type(instance):
    assert isinstance(instance.isActive, str)


@given(instance=uml::Class_strategy)
def test_uml::class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=uml::Class_strategy)
def test_uml::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::Class_strategy)
def test_uml::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=uml::Classifier_strategy)
@settings(max_examples=50)
def test_uml::classifier_instantiation(instance):
    assert isinstance(instance, uml::Classifier)

@given(instance=uml::Classifier_strategy)
def test_uml::classifier_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=uml::Classifier_strategy)
def test_uml::classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=uml::Generalization_strategy)
@settings(max_examples=50)
def test_uml::generalization_instantiation(instance):
    assert isinstance(instance, uml::Generalization)

@given(instance=uml::Generalization_strategy)
def test_uml::generalization_isSubstitutable_type(instance):
    assert isinstance(instance.isSubstitutable, str)


@given(instance=uml::Generalization_strategy)
def test_uml::generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=uml::PackageImport_strategy)
@settings(max_examples=50)
def test_uml::packageimport_instantiation(instance):
    assert isinstance(instance, uml::PackageImport)

@given(instance=uml::PackageImport_strategy)
def test_uml::packageimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=uml::PackageImport_strategy)
def test_uml::packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml::ElementImport_strategy)
@settings(max_examples=50)
def test_uml::elementimport_instantiation(instance):
    assert isinstance(instance, uml::ElementImport)

@given(instance=uml::ElementImport_strategy)
def test_uml::elementimport_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=uml::ElementImport_strategy)
def test_uml::elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=uml::ElementImport_strategy)
def test_uml::elementimport_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=uml::ElementImport_strategy)
def test_uml::elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uml::TypedElement_strategy)
@settings(max_examples=50)
def test_uml::typedelement_instantiation(instance):
    assert isinstance(instance, uml::TypedElement)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=uml::Association_strategy)
@settings(max_examples=50)
def test_uml::association_instantiation(instance):
    assert isinstance(instance, uml::Association)

@given(instance=uml::Association_strategy)
def test_uml::association_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=uml::Association_strategy)
def test_uml::association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=uml::DirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml::directedrelationship_instantiation(instance):
    assert isinstance(instance, uml::DirectedRelationship)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=uml::ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml::valuespecification_instantiation(instance):
    assert isinstance(instance, uml::ValueSpecification)

@given(instance=uml::Type_strategy)
@settings(max_examples=50)
def test_uml::type_instantiation(instance):
    assert isinstance(instance, uml::Type)

@given(instance=uml::Package_strategy)
@settings(max_examples=50)
def test_uml::package_instantiation(instance):
    assert isinstance(instance, uml::Package)

@given(instance=uml::Package_strategy)
def test_uml::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::Package_strategy)
def test_uml::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml::Namespace_strategy)
@settings(max_examples=50)
def test_uml::namespace_instantiation(instance):
    assert isinstance(instance, uml::Namespace)

@given(instance=uml::Dependency_strategy)
@settings(max_examples=50)
def test_uml::dependency_instantiation(instance):
    assert isinstance(instance, uml::Dependency)

@given(instance=uml::PackageableElement_strategy)
@settings(max_examples=50)
def test_uml::packageableelement_instantiation(instance):
    assert isinstance(instance, uml::PackageableElement)

@given(instance=uml::Element_strategy)
@settings(max_examples=50)
def test_uml::element_instantiation(instance):
    assert isinstance(instance, uml::Element)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=uml::NamedElement_strategy)
@settings(max_examples=50)
def test_uml::namedelement_instantiation(instance):
    assert isinstance(instance, uml::NamedElement)

@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::NamedElement_strategy)
def test_uml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml::Relationship_strategy)
@settings(max_examples=50)
def test_uml::relationship_instantiation(instance):
    assert isinstance(instance, uml::Relationship)

@given(instance=uml::Comment_strategy)
@settings(max_examples=50)
def test_uml::comment_instantiation(instance):
    assert isinstance(instance, uml::Comment)

@given(instance=uml::Comment_strategy)
def test_uml::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uml::Comment_strategy)
def test_uml::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

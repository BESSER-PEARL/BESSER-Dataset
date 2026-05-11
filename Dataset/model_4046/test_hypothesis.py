import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UML::ActivityNode,
    uml::UML::Action,
    UML::Action,
    uml::UML::CallOperationAction,
    uml::UML::ConnectorEnd,
    uml::UML::ActivityNode,
    uml::UML::ActivityEdge,
    UML::Behavior,
    uml::UML::Activity,
    UML::Class,
    UML::Property,
    uml::UML::Port,
    UML::ValueSpecification,
    uml::UML::OpaqueExpression,
    uml::UML::ValueSpecification,
    UML::Classifier,
    uml::UML::Interface,
    UML::Type,
    UML::PackageableElement,
    uml::UML::Type,
    UML::TypedElement,
    uml::UML::ConnectableElement,
    UML::Feature,
    uml::UML::StructuralFeature,
    uml::UML::Connector,
    UML::Namespace,
    uml::UML::BehavioralFeature,
    uml::UML::Classifier,
    uml::UML::Package,
    UML::ConnectableElement,
    UML::StructuralFeature,
    UML::BehavioredClassifier,
    uml::UML::Class,
    UML::BehavioralFeature,
    uml::UML::Behavior,
    uml::UML::BehavioredClassifier,
    uml::UML::InterfaceRealization,
    uml::UML::Property,
    uml::UML::Operation,
    uml::UML::Constraint,
    UML::RedefinableElement,
    uml::UML::Feature,
    UML::NamedElement,
    uml::UML::TypedElement,
    uml::UML::Namespace,
    uml::UML::PackageableElement,
    uml::UML::RedefinableElement,
    uml::UML::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml::activitynode_is_not_abstract():
    assert not inspect.isabstract(UML::ActivityNode)


def test_uml::activitynode_constructor_exists():
    assert callable(UML::ActivityNode.__init__)


def test_uml::activitynode_constructor_args():
    sig = inspect.signature(UML::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::action_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Action)


def test_uml::uml::action_constructor_exists():
    assert callable(uml::UML::Action.__init__)


def test_uml::uml::action_constructor_args():
    sig = inspect.signature(uml::UML::Action.__init__)
    params = list(sig.parameters.keys())



def test_uml::action_is_not_abstract():
    assert not inspect.isabstract(UML::Action)


def test_uml::action_constructor_exists():
    assert callable(UML::Action.__init__)


def test_uml::action_constructor_args():
    sig = inspect.signature(UML::Action.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(uml::UML::CallOperationAction)


def test_uml::uml::calloperationaction_constructor_exists():
    assert callable(uml::UML::CallOperationAction.__init__)


def test_uml::uml::calloperationaction_constructor_args():
    sig = inspect.signature(uml::UML::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::connectorend_is_not_abstract():
    assert not inspect.isabstract(uml::UML::ConnectorEnd)


def test_uml::uml::connectorend_constructor_exists():
    assert callable(uml::UML::ConnectorEnd.__init__)


def test_uml::uml::connectorend_constructor_args():
    sig = inspect.signature(uml::UML::ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::activitynode_is_not_abstract():
    assert not inspect.isabstract(uml::UML::ActivityNode)


def test_uml::uml::activitynode_constructor_exists():
    assert callable(uml::UML::ActivityNode.__init__)


def test_uml::uml::activitynode_constructor_args():
    sig = inspect.signature(uml::UML::ActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::uml::activitynode_has_name():
    assert hasattr(uml::UML::ActivityNode, "name")
    descriptor = None
    for klass in uml::UML::ActivityNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml::uml::activityedge_is_not_abstract():
    assert not inspect.isabstract(uml::UML::ActivityEdge)


def test_uml::uml::activityedge_constructor_exists():
    assert callable(uml::UML::ActivityEdge.__init__)


def test_uml::uml::activityedge_constructor_args():
    sig = inspect.signature(uml::UML::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml::behavior_is_not_abstract():
    assert not inspect.isabstract(UML::Behavior)


def test_uml::behavior_constructor_exists():
    assert callable(UML::Behavior.__init__)


def test_uml::behavior_constructor_args():
    sig = inspect.signature(UML::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::activity_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Activity)


def test_uml::uml::activity_constructor_exists():
    assert callable(uml::UML::Activity.__init__)


def test_uml::uml::activity_constructor_args():
    sig = inspect.signature(uml::UML::Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml::class_is_not_abstract():
    assert not inspect.isabstract(UML::Class)


def test_uml::class_constructor_exists():
    assert callable(UML::Class.__init__)


def test_uml::class_constructor_args():
    sig = inspect.signature(UML::Class.__init__)
    params = list(sig.parameters.keys())



def test_uml::property_is_not_abstract():
    assert not inspect.isabstract(UML::Property)


def test_uml::property_constructor_exists():
    assert callable(UML::Property.__init__)


def test_uml::property_constructor_args():
    sig = inspect.signature(UML::Property.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::port_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Port)


def test_uml::uml::port_constructor_exists():
    assert callable(uml::UML::Port.__init__)


def test_uml::uml::port_constructor_args():
    sig = inspect.signature(uml::UML::Port.__init__)
    params = list(sig.parameters.keys())



def test_uml::valuespecification_is_not_abstract():
    assert not inspect.isabstract(UML::ValueSpecification)


def test_uml::valuespecification_constructor_exists():
    assert callable(UML::ValueSpecification.__init__)


def test_uml::valuespecification_constructor_args():
    sig = inspect.signature(UML::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(uml::UML::OpaqueExpression)


def test_uml::uml::opaqueexpression_constructor_exists():
    assert callable(uml::UML::OpaqueExpression.__init__)


def test_uml::uml::opaqueexpression_constructor_args():
    sig = inspect.signature(uml::UML::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_uml::uml::opaqueexpression_has_language():
    assert hasattr(uml::UML::OpaqueExpression, "language")
    descriptor = None
    for klass in uml::UML::OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_uml::uml::opaqueexpression_has_body():
    assert hasattr(uml::UML::OpaqueExpression, "body")
    descriptor = None
    for klass in uml::UML::OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_uml::uml::valuespecification_is_not_abstract():
    assert not inspect.isabstract(uml::UML::ValueSpecification)


def test_uml::uml::valuespecification_constructor_exists():
    assert callable(uml::UML::ValueSpecification.__init__)


def test_uml::uml::valuespecification_constructor_args():
    sig = inspect.signature(uml::UML::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::classifier_is_not_abstract():
    assert not inspect.isabstract(UML::Classifier)


def test_uml::classifier_constructor_exists():
    assert callable(UML::Classifier.__init__)


def test_uml::classifier_constructor_args():
    sig = inspect.signature(UML::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::interface_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Interface)


def test_uml::uml::interface_constructor_exists():
    assert callable(uml::UML::Interface.__init__)


def test_uml::uml::interface_constructor_args():
    sig = inspect.signature(uml::UML::Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml::type_is_not_abstract():
    assert not inspect.isabstract(UML::Type)


def test_uml::type_constructor_exists():
    assert callable(UML::Type.__init__)


def test_uml::type_constructor_args():
    sig = inspect.signature(UML::Type.__init__)
    params = list(sig.parameters.keys())



def test_uml::packageableelement_is_not_abstract():
    assert not inspect.isabstract(UML::PackageableElement)


def test_uml::packageableelement_constructor_exists():
    assert callable(UML::PackageableElement.__init__)


def test_uml::packageableelement_constructor_args():
    sig = inspect.signature(UML::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::type_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Type)


def test_uml::uml::type_constructor_exists():
    assert callable(uml::UML::Type.__init__)


def test_uml::uml::type_constructor_args():
    sig = inspect.signature(uml::UML::Type.__init__)
    params = list(sig.parameters.keys())



def test_uml::typedelement_is_not_abstract():
    assert not inspect.isabstract(UML::TypedElement)


def test_uml::typedelement_constructor_exists():
    assert callable(UML::TypedElement.__init__)


def test_uml::typedelement_constructor_args():
    sig = inspect.signature(UML::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::connectableelement_is_not_abstract():
    assert not inspect.isabstract(uml::UML::ConnectableElement)


def test_uml::uml::connectableelement_constructor_exists():
    assert callable(uml::UML::ConnectableElement.__init__)


def test_uml::uml::connectableelement_constructor_args():
    sig = inspect.signature(uml::UML::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::feature_is_not_abstract():
    assert not inspect.isabstract(UML::Feature)


def test_uml::feature_constructor_exists():
    assert callable(UML::Feature.__init__)


def test_uml::feature_constructor_args():
    sig = inspect.signature(UML::Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(uml::UML::StructuralFeature)


def test_uml::uml::structuralfeature_constructor_exists():
    assert callable(uml::UML::StructuralFeature.__init__)


def test_uml::uml::structuralfeature_constructor_args():
    sig = inspect.signature(uml::UML::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::connector_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Connector)


def test_uml::uml::connector_constructor_exists():
    assert callable(uml::UML::Connector.__init__)


def test_uml::uml::connector_constructor_args():
    sig = inspect.signature(uml::UML::Connector.__init__)
    params = list(sig.parameters.keys())



def test_uml::namespace_is_not_abstract():
    assert not inspect.isabstract(UML::Namespace)


def test_uml::namespace_constructor_exists():
    assert callable(UML::Namespace.__init__)


def test_uml::namespace_constructor_args():
    sig = inspect.signature(UML::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(uml::UML::BehavioralFeature)


def test_uml::uml::behavioralfeature_constructor_exists():
    assert callable(uml::UML::BehavioralFeature.__init__)


def test_uml::uml::behavioralfeature_constructor_args():
    sig = inspect.signature(uml::UML::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::classifier_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Classifier)


def test_uml::uml::classifier_constructor_exists():
    assert callable(uml::UML::Classifier.__init__)


def test_uml::uml::classifier_constructor_args():
    sig = inspect.signature(uml::UML::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::package_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Package)


def test_uml::uml::package_constructor_exists():
    assert callable(uml::UML::Package.__init__)


def test_uml::uml::package_constructor_args():
    sig = inspect.signature(uml::UML::Package.__init__)
    params = list(sig.parameters.keys())



def test_uml::connectableelement_is_not_abstract():
    assert not inspect.isabstract(UML::ConnectableElement)


def test_uml::connectableelement_constructor_exists():
    assert callable(UML::ConnectableElement.__init__)


def test_uml::connectableelement_constructor_args():
    sig = inspect.signature(UML::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML::StructuralFeature)


def test_uml::structuralfeature_constructor_exists():
    assert callable(UML::StructuralFeature.__init__)


def test_uml::structuralfeature_constructor_args():
    sig = inspect.signature(UML::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML::BehavioredClassifier)


def test_uml::behavioredclassifier_constructor_exists():
    assert callable(UML::BehavioredClassifier.__init__)


def test_uml::behavioredclassifier_constructor_args():
    sig = inspect.signature(UML::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::class_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Class)


def test_uml::uml::class_constructor_exists():
    assert callable(uml::UML::Class.__init__)


def test_uml::uml::class_constructor_args():
    sig = inspect.signature(uml::UML::Class.__init__)
    params = list(sig.parameters.keys())



def test_uml::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UML::BehavioralFeature)


def test_uml::behavioralfeature_constructor_exists():
    assert callable(UML::BehavioralFeature.__init__)


def test_uml::behavioralfeature_constructor_args():
    sig = inspect.signature(UML::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::behavior_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Behavior)


def test_uml::uml::behavior_constructor_exists():
    assert callable(uml::UML::Behavior.__init__)


def test_uml::uml::behavior_constructor_args():
    sig = inspect.signature(uml::UML::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml::UML::BehavioredClassifier)


def test_uml::uml::behavioredclassifier_constructor_exists():
    assert callable(uml::UML::BehavioredClassifier.__init__)


def test_uml::uml::behavioredclassifier_constructor_args():
    sig = inspect.signature(uml::UML::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::interfacerealization_is_not_abstract():
    assert not inspect.isabstract(uml::UML::InterfaceRealization)


def test_uml::uml::interfacerealization_constructor_exists():
    assert callable(uml::UML::InterfaceRealization.__init__)


def test_uml::uml::interfacerealization_constructor_args():
    sig = inspect.signature(uml::UML::InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::property_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Property)


def test_uml::uml::property_constructor_exists():
    assert callable(uml::UML::Property.__init__)


def test_uml::uml::property_constructor_args():
    sig = inspect.signature(uml::UML::Property.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::operation_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Operation)


def test_uml::uml::operation_constructor_exists():
    assert callable(uml::UML::Operation.__init__)


def test_uml::uml::operation_constructor_args():
    sig = inspect.signature(uml::UML::Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::constraint_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Constraint)


def test_uml::uml::constraint_constructor_exists():
    assert callable(uml::UML::Constraint.__init__)


def test_uml::uml::constraint_constructor_args():
    sig = inspect.signature(uml::UML::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(UML::RedefinableElement)


def test_uml::redefinableelement_constructor_exists():
    assert callable(UML::RedefinableElement.__init__)


def test_uml::redefinableelement_constructor_args():
    sig = inspect.signature(UML::RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::feature_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Feature)


def test_uml::uml::feature_constructor_exists():
    assert callable(uml::UML::Feature.__init__)


def test_uml::uml::feature_constructor_args():
    sig = inspect.signature(uml::UML::Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml::namedelement_is_not_abstract():
    assert not inspect.isabstract(UML::NamedElement)


def test_uml::namedelement_constructor_exists():
    assert callable(UML::NamedElement.__init__)


def test_uml::namedelement_constructor_args():
    sig = inspect.signature(UML::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::typedelement_is_not_abstract():
    assert not inspect.isabstract(uml::UML::TypedElement)


def test_uml::uml::typedelement_constructor_exists():
    assert callable(uml::UML::TypedElement.__init__)


def test_uml::uml::typedelement_constructor_args():
    sig = inspect.signature(uml::UML::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::namespace_is_not_abstract():
    assert not inspect.isabstract(uml::UML::Namespace)


def test_uml::uml::namespace_constructor_exists():
    assert callable(uml::UML::Namespace.__init__)


def test_uml::uml::namespace_constructor_args():
    sig = inspect.signature(uml::UML::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::packageableelement_is_not_abstract():
    assert not inspect.isabstract(uml::UML::PackageableElement)


def test_uml::uml::packageableelement_constructor_exists():
    assert callable(uml::UML::PackageableElement.__init__)


def test_uml::uml::packageableelement_constructor_args():
    sig = inspect.signature(uml::UML::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(uml::UML::RedefinableElement)


def test_uml::uml::redefinableelement_constructor_exists():
    assert callable(uml::UML::RedefinableElement.__init__)


def test_uml::uml::redefinableelement_constructor_args():
    sig = inspect.signature(uml::UML::RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::uml::namedelement_is_not_abstract():
    assert not inspect.isabstract(uml::UML::NamedElement)


def test_uml::uml::namedelement_constructor_exists():
    assert callable(uml::UML::NamedElement.__init__)


def test_uml::uml::namedelement_constructor_args():
    sig = inspect.signature(uml::UML::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml::uml::namedelement_has_name():
    assert hasattr(uml::UML::NamedElement, "name")
    descriptor = None
    for klass in uml::UML::NamedElement.__mro__:
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
UML::ActivityNode_strategy = st.builds(
    UML::ActivityNode,
)
uml::UML::Action_strategy = st.builds(
    uml::UML::Action,
)
UML::Action_strategy = st.builds(
    UML::Action,
)
uml::UML::CallOperationAction_strategy = st.builds(
    uml::UML::CallOperationAction,
)
uml::UML::ConnectorEnd_strategy = st.builds(
    uml::UML::ConnectorEnd,
)
uml::UML::ActivityNode_strategy = st.builds(
    uml::UML::ActivityNode,
    name=
        safe_text
)
uml::UML::ActivityEdge_strategy = st.builds(
    uml::UML::ActivityEdge,
)
UML::Behavior_strategy = st.builds(
    UML::Behavior,
)
uml::UML::Activity_strategy = st.builds(
    uml::UML::Activity,
)
UML::Class_strategy = st.builds(
    UML::Class,
)
UML::Property_strategy = st.builds(
    UML::Property,
)
uml::UML::Port_strategy = st.builds(
    uml::UML::Port,
)
UML::ValueSpecification_strategy = st.builds(
    UML::ValueSpecification,
)
uml::UML::OpaqueExpression_strategy = st.builds(
    uml::UML::OpaqueExpression,
    language=
        safe_text,
    body=
        safe_text
)
uml::UML::ValueSpecification_strategy = st.builds(
    uml::UML::ValueSpecification,
)
UML::Classifier_strategy = st.builds(
    UML::Classifier,
)
uml::UML::Interface_strategy = st.builds(
    uml::UML::Interface,
)
UML::Type_strategy = st.builds(
    UML::Type,
)
UML::PackageableElement_strategy = st.builds(
    UML::PackageableElement,
)
uml::UML::Type_strategy = st.builds(
    uml::UML::Type,
)
UML::TypedElement_strategy = st.builds(
    UML::TypedElement,
)
uml::UML::ConnectableElement_strategy = st.builds(
    uml::UML::ConnectableElement,
)
UML::Feature_strategy = st.builds(
    UML::Feature,
)
uml::UML::StructuralFeature_strategy = st.builds(
    uml::UML::StructuralFeature,
)
uml::UML::Connector_strategy = st.builds(
    uml::UML::Connector,
)
UML::Namespace_strategy = st.builds(
    UML::Namespace,
)
uml::UML::BehavioralFeature_strategy = st.builds(
    uml::UML::BehavioralFeature,
)
uml::UML::Classifier_strategy = st.builds(
    uml::UML::Classifier,
)
uml::UML::Package_strategy = st.builds(
    uml::UML::Package,
)
UML::ConnectableElement_strategy = st.builds(
    UML::ConnectableElement,
)
UML::StructuralFeature_strategy = st.builds(
    UML::StructuralFeature,
)
UML::BehavioredClassifier_strategy = st.builds(
    UML::BehavioredClassifier,
)
uml::UML::Class_strategy = st.builds(
    uml::UML::Class,
)
UML::BehavioralFeature_strategy = st.builds(
    UML::BehavioralFeature,
)
uml::UML::Behavior_strategy = st.builds(
    uml::UML::Behavior,
)
uml::UML::BehavioredClassifier_strategy = st.builds(
    uml::UML::BehavioredClassifier,
)
uml::UML::InterfaceRealization_strategy = st.builds(
    uml::UML::InterfaceRealization,
)
uml::UML::Property_strategy = st.builds(
    uml::UML::Property,
)
uml::UML::Operation_strategy = st.builds(
    uml::UML::Operation,
)
uml::UML::Constraint_strategy = st.builds(
    uml::UML::Constraint,
)
UML::RedefinableElement_strategy = st.builds(
    UML::RedefinableElement,
)
uml::UML::Feature_strategy = st.builds(
    uml::UML::Feature,
)
UML::NamedElement_strategy = st.builds(
    UML::NamedElement,
)
uml::UML::TypedElement_strategy = st.builds(
    uml::UML::TypedElement,
)
uml::UML::Namespace_strategy = st.builds(
    uml::UML::Namespace,
)
uml::UML::PackageableElement_strategy = st.builds(
    uml::UML::PackageableElement,
)
uml::UML::RedefinableElement_strategy = st.builds(
    uml::UML::RedefinableElement,
)
uml::UML::NamedElement_strategy = st.builds(
    uml::UML::NamedElement,
    name=
        safe_text
)

@given(instance=UML::ActivityNode_strategy)
@settings(max_examples=50)
def test_uml::activitynode_instantiation(instance):
    assert isinstance(instance, UML::ActivityNode)

@given(instance=uml::UML::Action_strategy)
@settings(max_examples=50)
def test_uml::uml::action_instantiation(instance):
    assert isinstance(instance, uml::UML::Action)

@given(instance=UML::Action_strategy)
@settings(max_examples=50)
def test_uml::action_instantiation(instance):
    assert isinstance(instance, UML::Action)

@given(instance=uml::UML::CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml::uml::calloperationaction_instantiation(instance):
    assert isinstance(instance, uml::UML::CallOperationAction)

@given(instance=uml::UML::ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml::uml::connectorend_instantiation(instance):
    assert isinstance(instance, uml::UML::ConnectorEnd)

@given(instance=uml::UML::ActivityNode_strategy)
@settings(max_examples=50)
def test_uml::uml::activitynode_instantiation(instance):
    assert isinstance(instance, uml::UML::ActivityNode)

@given(instance=uml::UML::ActivityNode_strategy)
def test_uml::uml::activitynode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::UML::ActivityNode_strategy)
def test_uml::uml::activitynode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml::UML::ActivityEdge_strategy)
@settings(max_examples=50)
def test_uml::uml::activityedge_instantiation(instance):
    assert isinstance(instance, uml::UML::ActivityEdge)

@given(instance=UML::Behavior_strategy)
@settings(max_examples=50)
def test_uml::behavior_instantiation(instance):
    assert isinstance(instance, UML::Behavior)

@given(instance=uml::UML::Activity_strategy)
@settings(max_examples=50)
def test_uml::uml::activity_instantiation(instance):
    assert isinstance(instance, uml::UML::Activity)

@given(instance=UML::Class_strategy)
@settings(max_examples=50)
def test_uml::class_instantiation(instance):
    assert isinstance(instance, UML::Class)

@given(instance=UML::Property_strategy)
@settings(max_examples=50)
def test_uml::property_instantiation(instance):
    assert isinstance(instance, UML::Property)

@given(instance=uml::UML::Port_strategy)
@settings(max_examples=50)
def test_uml::uml::port_instantiation(instance):
    assert isinstance(instance, uml::UML::Port)

@given(instance=UML::ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml::valuespecification_instantiation(instance):
    assert isinstance(instance, UML::ValueSpecification)

@given(instance=uml::UML::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml::uml::opaqueexpression_instantiation(instance):
    assert isinstance(instance, uml::UML::OpaqueExpression)

@given(instance=uml::UML::OpaqueExpression_strategy)
def test_uml::uml::opaqueexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=uml::UML::OpaqueExpression_strategy)
def test_uml::uml::opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=uml::UML::OpaqueExpression_strategy)
def test_uml::uml::opaqueexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uml::UML::OpaqueExpression_strategy)
def test_uml::uml::opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uml::UML::ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml::uml::valuespecification_instantiation(instance):
    assert isinstance(instance, uml::UML::ValueSpecification)

@given(instance=UML::Classifier_strategy)
@settings(max_examples=50)
def test_uml::classifier_instantiation(instance):
    assert isinstance(instance, UML::Classifier)

@given(instance=uml::UML::Interface_strategy)
@settings(max_examples=50)
def test_uml::uml::interface_instantiation(instance):
    assert isinstance(instance, uml::UML::Interface)

@given(instance=UML::Type_strategy)
@settings(max_examples=50)
def test_uml::type_instantiation(instance):
    assert isinstance(instance, UML::Type)

@given(instance=UML::PackageableElement_strategy)
@settings(max_examples=50)
def test_uml::packageableelement_instantiation(instance):
    assert isinstance(instance, UML::PackageableElement)

@given(instance=uml::UML::Type_strategy)
@settings(max_examples=50)
def test_uml::uml::type_instantiation(instance):
    assert isinstance(instance, uml::UML::Type)

@given(instance=UML::TypedElement_strategy)
@settings(max_examples=50)
def test_uml::typedelement_instantiation(instance):
    assert isinstance(instance, UML::TypedElement)

@given(instance=uml::UML::ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml::uml::connectableelement_instantiation(instance):
    assert isinstance(instance, uml::UML::ConnectableElement)

@given(instance=UML::Feature_strategy)
@settings(max_examples=50)
def test_uml::feature_instantiation(instance):
    assert isinstance(instance, UML::Feature)

@given(instance=uml::UML::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml::uml::structuralfeature_instantiation(instance):
    assert isinstance(instance, uml::UML::StructuralFeature)

@given(instance=uml::UML::Connector_strategy)
@settings(max_examples=50)
def test_uml::uml::connector_instantiation(instance):
    assert isinstance(instance, uml::UML::Connector)

@given(instance=UML::Namespace_strategy)
@settings(max_examples=50)
def test_uml::namespace_instantiation(instance):
    assert isinstance(instance, UML::Namespace)

@given(instance=uml::UML::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml::uml::behavioralfeature_instantiation(instance):
    assert isinstance(instance, uml::UML::BehavioralFeature)

@given(instance=uml::UML::Classifier_strategy)
@settings(max_examples=50)
def test_uml::uml::classifier_instantiation(instance):
    assert isinstance(instance, uml::UML::Classifier)

@given(instance=uml::UML::Package_strategy)
@settings(max_examples=50)
def test_uml::uml::package_instantiation(instance):
    assert isinstance(instance, uml::UML::Package)

@given(instance=UML::ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml::connectableelement_instantiation(instance):
    assert isinstance(instance, UML::ConnectableElement)

@given(instance=UML::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml::structuralfeature_instantiation(instance):
    assert isinstance(instance, UML::StructuralFeature)

@given(instance=UML::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML::BehavioredClassifier)

@given(instance=uml::UML::Class_strategy)
@settings(max_examples=50)
def test_uml::uml::class_instantiation(instance):
    assert isinstance(instance, uml::UML::Class)

@given(instance=UML::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml::behavioralfeature_instantiation(instance):
    assert isinstance(instance, UML::BehavioralFeature)

@given(instance=uml::UML::Behavior_strategy)
@settings(max_examples=50)
def test_uml::uml::behavior_instantiation(instance):
    assert isinstance(instance, uml::UML::Behavior)

@given(instance=uml::UML::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml::uml::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, uml::UML::BehavioredClassifier)

@given(instance=uml::UML::InterfaceRealization_strategy)
@settings(max_examples=50)
def test_uml::uml::interfacerealization_instantiation(instance):
    assert isinstance(instance, uml::UML::InterfaceRealization)

@given(instance=uml::UML::Property_strategy)
@settings(max_examples=50)
def test_uml::uml::property_instantiation(instance):
    assert isinstance(instance, uml::UML::Property)

@given(instance=uml::UML::Operation_strategy)
@settings(max_examples=50)
def test_uml::uml::operation_instantiation(instance):
    assert isinstance(instance, uml::UML::Operation)

@given(instance=uml::UML::Constraint_strategy)
@settings(max_examples=50)
def test_uml::uml::constraint_instantiation(instance):
    assert isinstance(instance, uml::UML::Constraint)

@given(instance=UML::RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml::redefinableelement_instantiation(instance):
    assert isinstance(instance, UML::RedefinableElement)

@given(instance=uml::UML::Feature_strategy)
@settings(max_examples=50)
def test_uml::uml::feature_instantiation(instance):
    assert isinstance(instance, uml::UML::Feature)

@given(instance=UML::NamedElement_strategy)
@settings(max_examples=50)
def test_uml::namedelement_instantiation(instance):
    assert isinstance(instance, UML::NamedElement)

@given(instance=uml::UML::TypedElement_strategy)
@settings(max_examples=50)
def test_uml::uml::typedelement_instantiation(instance):
    assert isinstance(instance, uml::UML::TypedElement)

@given(instance=uml::UML::Namespace_strategy)
@settings(max_examples=50)
def test_uml::uml::namespace_instantiation(instance):
    assert isinstance(instance, uml::UML::Namespace)

@given(instance=uml::UML::PackageableElement_strategy)
@settings(max_examples=50)
def test_uml::uml::packageableelement_instantiation(instance):
    assert isinstance(instance, uml::UML::PackageableElement)

@given(instance=uml::UML::RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml::uml::redefinableelement_instantiation(instance):
    assert isinstance(instance, uml::UML::RedefinableElement)

@given(instance=uml::UML::NamedElement_strategy)
@settings(max_examples=50)
def test_uml::uml::namedelement_instantiation(instance):
    assert isinstance(instance, uml::UML::NamedElement)

@given(instance=uml::UML::NamedElement_strategy)
def test_uml::uml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uml::UML::NamedElement_strategy)
def test_uml::uml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
